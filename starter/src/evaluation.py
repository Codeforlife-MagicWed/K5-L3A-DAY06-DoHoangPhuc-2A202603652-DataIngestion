"""Evaluate retrieved Top-K hits against verifiable gold evidence and preserve full traces."""
from __future__ import annotations

import re
from typing import Any


def _norm_ws(text: str) -> str:
    """Collapse arbitrary whitespace runs for robust verbatim quote verification."""
    return re.sub(r"\s+", " ", text or "").strip()


def _is_filter_compliant(hit_metadata: dict[str, Any], filters: dict[str, Any] | None) -> bool | None:
    """Return True/False if question specifies metadata filters, else None."""
    if not filters:
        return None
    for key, expected in filters.items():
        if expected is None:
            continue
        actual = hit_metadata.get(key)
        if isinstance(expected, (list, tuple, set)):
            if actual not in expected:
                return False
        elif actual != expected:
            return False
    return True


def evaluate_query(question: dict[str, Any], hits: list[dict[str, Any]]) -> dict[str, Any]:
    """Evaluate retrieved hits for a benchmark question without inferring manual audit labels."""
    gold_source_id = question.get("gold_source_id")
    valid_pages = sorted({int(p) for p in (question.get("valid_pages") or [question["gold_page"]])})
    valid_page_set = set(valid_pages)

    raw_quote = question["evidence_quote"]
    parts = [_norm_ws(part) for part in raw_quote.split(" ... ") if part.strip()]
    if not parts:
        raise ValueError(f"Question {question.get('id')} has empty evidence_quote.")

    filters = question.get("filter")
    evaluated_hits: list[dict[str, Any]] = []
    union_matched_parts_on_valid_pages: set[int] = set()

    for rank, hit in enumerate(hits, start=1):
        hit_doc = hit.get("document_id")
        hit_page = int(hit["page"])
        hit_meta = dict(hit.get("metadata") or {})
        hit_text_norm = _norm_ws(hit.get("text", ""))

        source_ok = not gold_source_id or hit_doc == gold_source_id
        page_match = source_ok and (hit_page in valid_page_set)

        matched_indices = [idx for idx, part in enumerate(parts) if part in hit_text_norm]
        if page_match:
            union_matched_parts_on_valid_pages.update(matched_indices)

        is_gold_hit = page_match and (len(matched_indices) == len(parts))
        filter_ok = _is_filter_compliant(hit_meta, filters)

        evaluated_hits.append(
            {
                "rank": rank,
                "chunk_id": hit["chunk_id"],
                "document_id": hit_doc,
                "source": hit.get("source"),
                "page": hit_page,
                "score": round(float(hit["score"]), 6),
                "distance": round(float(hit.get("distance", 1.0 - float(hit["score"]))), 6),
                "metadata": hit_meta,
                "page_match": page_match,
                "matched_parts": len(matched_indices),
                "total_parts": len(parts),
                "is_gold_evidence_hit": is_gold_hit,
                "filter_compliant": filter_ok,
                "text": hit.get("text", ""),
            }
        )

    top3 = evaluated_hits[:3]
    hit_at_1 = bool(evaluated_hits and evaluated_hits[0]["is_gold_evidence_hit"])
    evidence_hit_at_3 = any(item["is_gold_evidence_hit"] for item in top3)
    page_hit_at_3 = any(item["page_match"] for item in top3)
    multi_chunk_top3_covered = len(union_matched_parts_on_valid_pages) == len(parts)

    if filters:
        filter_compliant_top3: bool | None = bool(top3) and all(
            item["filter_compliant"] is True for item in top3
        )
    else:
        filter_compliant_top3 = None

    return {
        "question_id": question["id"],
        "split": question["split"],
        "type": question.get("type", "unknown"),
        "question": question["question"],
        "expected_answer": question["expected_answer"],
        "gold_source_id": gold_source_id,
        "gold_page": int(question["gold_page"]),
        "valid_pages": valid_pages,
        "evidence_quote": raw_quote,
        "filter": filters,
        "hit_at_1": hit_at_1,
        "evidence_hit_at_3": evidence_hit_at_3,
        "source_page_hit_at_3": page_hit_at_3,
        "multi_chunk_top3_covered": multi_chunk_top3_covered,
        "filter_compliant_top3": filter_compliant_top3,
        "hits": top3,
    }


def _aggregate_subset(items: list[dict[str, Any]]) -> dict[str, Any]:
    """Compute exact counts and ratios for a subset of query traces."""
    n = len(items)
    if n == 0:
        return {
            "count": 0,
            "hit1_count": 0,
            "hit1_rate": 0.0,
            "hit3_count": 0,
            "hit3_rate": 0.0,
            "page_hit3_count": 0,
            "multi_chunk_top3_count": 0,
            "filter_applicable_count": 0,
            "filter_compliant_count": 0,
            "filter_compliance": "N/A",
        }

    hit1_count = sum(1 for t in items if t["hit_at_1"])
    hit3_count = sum(1 for t in items if t["evidence_hit_at_3"])
    page_hit3_count = sum(1 for t in items if t["source_page_hit_at_3"])
    multi_chunk_count = sum(1 for t in items if t["multi_chunk_top3_covered"])

    filtered_items = [t for t in items if t["filter_compliant_top3"] is not None]
    f_total = len(filtered_items)
    f_ok = sum(1 for t in filtered_items if t["filter_compliant_top3"] is True)
    f_display = f"{f_ok}/{f_total}" if f_total > 0 else "N/A"

    return {
        "count": n,
        "hit1_count": hit1_count,
        "hit1_rate": round(hit1_count / n, 4),
        "hit3_count": hit3_count,
        "hit3_rate": round(hit3_count / n, 4),
        "page_hit3_count": page_hit3_count,
        "multi_chunk_top3_count": multi_chunk_count,
        "filter_applicable_count": f_total,
        "filter_compliant_count": f_ok,
        "filter_compliance": f_display,
    }


def summarize(traces: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate Hit@1, Evidence Hit@3, and filter compliance across overall, dev, and test splits."""
    dev_traces = [t for t in traces if t["split"] == "dev"]
    test_traces = [t for t in traces if t["split"] == "test"]
    filtered_traces = [t for t in traces if t["filter"] is not None]

    return {
        "overall": _aggregate_subset(traces),
        "dev": _aggregate_subset(dev_traces),
        "test": _aggregate_subset(test_traces),
        "filtered_only": _aggregate_subset(filtered_traces),
        "missed_hit3_ids": [t["question_id"] for t in traces if not t["evidence_hit_at_3"]],
        "missed_hit1_ids": [t["question_id"] for t in traces if not t["hit_at_1"]],
    }
