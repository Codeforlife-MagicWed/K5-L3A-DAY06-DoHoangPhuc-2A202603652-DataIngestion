"""End-to-end Day 06 ingestion, chunking, embedding, pgvector retrieval, and evaluation pipeline."""
from __future__ import annotations

import json
import os
import statistics
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from dotenv import load_dotenv

from .chunking import by_paragraph, fixed_size, recursive_split
from .embeddings import MyEmbedder
from .evaluation import evaluate_query, summarize
from .ingestion import load_pdf
from .models import Chunk, DocumentPage
from .store import PgVectorStore

STARTER_DIR = Path(__file__).resolve().parents[1]
LAB_DIR = STARTER_DIR.parent
COHERENCE_SAMPLE_PAGES: tuple[int, ...] = (18, 25, 27, 32, 35, 49, 56, 64, 68, 72)


@dataclass(frozen=True)
class StrategySpec:
    key: str
    label: str
    chunker_name: str
    chunk_params: str
    use_filter: bool
    chunk_fn: Callable[[DocumentPage], list[Chunk]]


def _chunk_stats(chunks: list[Chunk]) -> dict[str, Any]:
    lengths = [len(c.text) for c in chunks]
    return {
        "total_chunks": len(chunks),
        "total_chars": sum(lengths),
        "min_len": min(lengths) if lengths else 0,
        "median_len": int(statistics.median(lengths)) if lengths else 0,
        "avg_len": round(sum(lengths) / len(lengths), 1) if lengths else 0.0,
        "max_len": max(lengths) if lengths else 0,
    }


def _build_manual_audit_packets(
    pages_by_num: dict[int, DocumentPage],
    chunks_by_strategy: dict[str, list[Chunk]],
    traces_by_strategy: dict[str, list[dict[str, Any]]],
    questions: list[dict[str, Any]],
) -> str:
    """Export unlabelled Top-3 and chunk-coherence samples for manual audit per GUIDE.md."""
    lines: list[str] = [
        "# Manual Audit Packets (Chưa gán nhãn — Dùng cho chấm thủ công)",
        "",
        "> Theo `GUIDE.md` & `BENCHMARK.md`: tự chấm thủ công (thang 0–2) cho **Chunk Coherence** (10 vị trí định sẵn trước khi xem điểm) và **Metadata Usefulness + Grounding Quality** (trên toàn bộ tập `test`), tuyệt đối không suy diễn từ exact string match.",
        "",
        "## Phần 1 — Chunk Coherence (10 vị trí nguồn cố định trên A, B/C, D)",
        "",
        f"Các trang kiểm tra xác định trước: `{list(COHERENCE_SAMPLE_PAGES)}` (mỗi vị trí lấy chunk đầu tiên/giữa đại diện của trang để đối chiếu khả năng tự hiểu trọn ý).",
        "",
    ]

    for pg in COHERENCE_SAMPLE_PAGES:
        doc_page = pages_by_num[pg]
        lines.append(
            f"### Trang PDF {pg} (Sách: {doc_page.metadata['book_page']}, `{doc_page.metadata['chapter']}`, mục `{doc_page.metadata['section']}`)"
        )
        for skey in ("A", "B", "D"):
            matching = [c for c in chunks_by_strategy[skey] if c.page == pg]
            if not matching:
                lines.append(f"- **{skey}**: *(Không có chunk)*")
                continue
            sample = matching[min(1, len(matching) - 1)] if len(matching) > 1 and pg in (18, 49, 56) else matching[0]
            lines.append(f"- **{skey} (`{sample.chunk_id}`, {len(sample.text)} chars):**")
            lines.append("  ```text")
            lines.append(sample.text)
            lines.append("  ```")
        lines.append("")

    lines.extend([
        "## Phần 2 — Metadata Usefulness & Grounding Quality (Tập `test`)",
        "",
    ])

    test_qs = [q for q in questions if q["split"] == "test"]
    for q in test_qs:
        qid = q["id"]
        lines.extend([
            f"### {qid} (`{q['type']}` | gold_page={q['gold_page']} | valid_pages={q.get('valid_pages')} | filter={q.get('filter')})",
            f"- **Câu hỏi:** {q['question']}",
            f"- **Đáp án chuẩn:** {q['expected_answer']}",
            f"- **Evidence gốc:** `{q['evidence_quote']}`",
            "",
        ])
        for skey in ("A", "B", "C", "D"):
            trace = next(t for t in traces_by_strategy[skey] if t["question_id"] == qid)
            lines.append(
                f"#### Chiến lược {skey} (Auto proxy: `Hit@1={trace['hit_at_1']}`, `Hit@3={trace['evidence_hit_at_3']}`, `filter_ok={trace['filter_compliant_top3']}`)"
            )
            for h in trace["hits"]:
                m = h["metadata"]
                lines.append(
                    f"- **Rank {h['rank']}** | `{h['chunk_id']}` | `score={h['score']:.4f}` | `source={h['source']}` | `page={h['page']}` (`book={m.get('book_page')}`, `chapter={m.get('chapter')}`, `section={m.get('section')}`)"
                )
                lines.append("  ```text")
                lines.append(h["text"])
                lines.append("  ```")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    """Run ingestion, A/B/C/D chunking, Gemini embedding, pgvector search, and benchmark evaluation."""
    load_dotenv(STARTER_DIR / ".env")
    database_url = (os.getenv("DATABASE_URL") or "").strip()
    if not database_url:
        raise RuntimeError("DATABASE_URL is missing in starter/.env")

    manifest = json.loads((LAB_DIR / "data" / "manifest.json").read_text(encoding="utf-8"))
    benchmark = json.loads((LAB_DIR / "benchmark" / "questions.json").read_text(encoding="utf-8"))
    questions: list[dict[str, Any]] = benchmark["questions"]

    source_rel = manifest["source_path_or_url"]
    pdf_path = LAB_DIR / source_rel
    doc_id = manifest["source_id"]

    t_ingest_0 = time.perf_counter()
    empty_pages_log: list[dict[str, Any]] = []
    pages = load_pdf(
        path=pdf_path,
        document_id=doc_id,
        source=source_rel,
        page_range=(17, 76),
        empty_pages_log=empty_pages_log,
    )
    ingest_seconds = round(time.perf_counter() - t_ingest_0, 3)

    if len(pages) < 30:
        raise RuntimeError(f"Corpus must have at least 30 valid pages, found {len(pages)}.")

    embedder = MyEmbedder(batch_size=50)
    store = PgVectorStore(database_url=database_url, dimensions=embedder.dimensions)
    store.create_schema()

    strategies: tuple[StrategySpec, ...] = (
        StrategySpec("A", "A_fixed_500_50", "fixed_size", "size=500, overlap=50", False, lambda p: fixed_size(p, size=500, overlap=50)),
        StrategySpec("B", "B_paragraph_500", "by_paragraph", "max_size=500", False, lambda p: by_paragraph(p, max_size=500)),
        StrategySpec("C", "C_paragraph_500_filtered", "by_paragraph", "max_size=500 + metadata_filter", True, lambda p: by_paragraph(p, max_size=500)),
        StrategySpec("D", "D_recursive_650_100_filtered", "recursive_split", "chunk_size=650, overlap=100 + metadata_filter", True, lambda p: recursive_split(p, chunk_size=650, overlap=100)),
    )

    chunks_by_strategy: dict[str, list[Chunk]] = {}
    vectors_by_chunk_hash: dict[str, list[list[float]]] = {}
    strategy_reports: dict[str, Any] = {}

    for spec in strategies:
        t_c0 = time.perf_counter()
        if spec.key == "C" and "B" in chunks_by_strategy:
            chunks = chunks_by_strategy["B"]
        else:
            chunks = [c for p in pages for c in spec.chunk_fn(p)]
        chunk_s = round(time.perf_counter() - t_c0, 3)
        chunks_by_strategy[spec.key] = chunks

        chunk_sig = f"{spec.chunker_name}:{spec.chunk_params}"
        t_e0 = time.perf_counter()
        if chunk_sig in vectors_by_chunk_hash:
            vectors = vectors_by_chunk_hash[chunk_sig]
        else:
            vectors = embedder.embed_documents([c.text for c in chunks])
            vectors_by_chunk_hash[chunk_sig] = vectors
        embed_s = round(time.perf_counter() - t_e0, 3)

        t_u0 = time.perf_counter()
        store.upsert(spec.label, chunks, vectors)
        upsert_s = round(time.perf_counter() - t_u0, 3)

        stored_count = store.count_chunks(spec.label)
        if stored_count != len(chunks):
            raise RuntimeError(f"Stored chunk count mismatch for {spec.label}: {stored_count} != {len(chunks)}")

        strategy_reports[spec.key] = {
            "label": spec.label,
            "chunker": spec.chunker_name,
            "chunk_params": spec.chunk_params,
            "use_metadata_filter": spec.use_filter,
            "chunk_stats": _chunk_stats(chunks),
            "stored_count": stored_count,
            "timings_sec": {
                "chunk_s": chunk_s,
                "embed_s": embed_s,
                "upsert_s": upsert_s,
            },
        }

    # Pre-embed all benchmark questions once so all strategies run against the exact same query vectors.
    t_q0 = time.perf_counter()
    query_vectors = {q["id"]: embedder.embed_query(q["question"]) for q in questions}
    query_embed_s = round(time.perf_counter() - t_q0, 3)

    traces_by_strategy: dict[str, list[dict[str, Any]]] = {}
    for spec in strategies:
        t_s0 = time.perf_counter()
        traces: list[dict[str, Any]] = []
        for q in questions:
            active_filter = q["filter"] if (spec.use_filter and q.get("filter")) else None
            hits = store.search(
                strategy=spec.label,
                query_vector=query_vectors[q["id"]],
                top_k=3,
                filters=active_filter,
            )
            traces.append(evaluate_query(q, hits))
        search_s = round(time.perf_counter() - t_s0, 3)

        traces_by_strategy[spec.key] = traces
        strategy_reports[spec.key]["timings_sec"]["search_eval_s"] = search_s
        strategy_reports[spec.key]["metrics"] = summarize(traces)

    results_dir = LAB_DIR / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    summary_payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "corpus": {
            "document_id": doc_id,
            "source_path": source_rel,
            "valid_pages": len(pages),
            "excluded_empty_pages": empty_pages_log,
            "total_normalized_chars": sum(len(p.text) for p in pages),
            "ingest_seconds": ingest_seconds,
        },
        "embedding": {
            "provider": "google-genai (Google AI Studio, vertexai=False)",
            "model_name": embedder.model_name,
            "dimensions": embedder.dimensions,
            "query_task_type": "RETRIEVAL_QUERY",
            "document_task_type": "RETRIEVAL_DOCUMENT",
            "api_calls_this_run": embedder.api_calls,
            "api_embedded_texts_this_run": embedder.api_embedded_texts,
            "cache_hits_this_run": embedder.cache_hits,
            "query_embed_seconds": query_embed_s,
            "estimated_cost_usd": 0.0,
        },
        "vector_store": {
            "backend": "PostgreSQL 16 + pgvector 0.8.7",
            "metric": "cosine_distance (<=>)",
            "search_mode": "exact",
            "table_name": store.table_name,
        },
        "benchmark": {
            "total_questions": len(questions),
            "dev_count": sum(1 for q in questions if q["split"] == "dev"),
            "test_count": sum(1 for q in questions if q["split"] == "test"),
            "metadata_filter_count": sum(1 for q in questions if q.get("filter") is not None),
        },
        "strategies": strategy_reports,
    }

    (results_dir / "metrics_summary.json").write_text(
        json.dumps(summary_payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (results_dir / "traces_all_strategies.json").write_text(
        json.dumps(traces_by_strategy, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    pages_by_num = {p.page: p for p in pages}
    audit_md = _build_manual_audit_packets(pages_by_num, chunks_by_strategy, traces_by_strategy, questions)
    (results_dir / "manual_audit_packets.md").write_text(audit_md, encoding="utf-8")

    print("=== DAY 06 PIPELINE COMPLETE ===")
    print(
        f"Corpus: {len(pages)} valid pages ({sum(len(p.text) for p in pages)} chars) | "
        f"API calls this run: {embedder.api_calls} (cache hits: {embedder.cache_hits})"
    )
    for spec in strategies:
        rep = strategy_reports[spec.key]
        m = rep["metrics"]
        dev_m, test_m, flt_m = m["dev"], m["test"], m["filtered_only"]
        print(
            f"[{spec.key}] {rep['label']} | chunks={rep['chunk_stats']['total_chunks']} | "
            f"Dev Hit@1={dev_m['hit1_count']}/{dev_m['count']} ({dev_m['hit1_rate']:.1%}), "
            f"Dev Hit@3={dev_m['hit3_count']}/{dev_m['count']} ({dev_m['hit3_rate']:.1%}) | "
            f"Test Hit@1={test_m['hit1_count']}/{test_m['count']} ({test_m['hit1_rate']:.1%}), "
            f"Test Hit@3={test_m['hit3_count']}/{test_m['count']} ({test_m['hit3_rate']:.1%}) | "
            f"Filter={flt_m['filter_compliance']} | Miss3={m['missed_hit3_ids']}"
        )


if __name__ == "__main__":
    main()
