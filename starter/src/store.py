"""Store and search chunk vectors with metadata filtering in PostgreSQL + pgvector."""
from __future__ import annotations

import json
import math
import re
from typing import Any

import psycopg
from psycopg import sql
from psycopg.rows import dict_row

from .models import Chunk

_VALID_IDENT_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_ALLOWED_COLUMN_FILTERS: frozenset[str] = frozenset({"chapter", "section", "document_id", "source", "page"})
_ALLOWED_JSONB_FILTERS: frozenset[str] = frozenset({"book_page", "chunking_strategy"})


def _format_vector_literal(vector: list[float], expected_dims: int) -> str:
    """Validate finite dimensions and serialize a float list as a pgvector literal."""
    if len(vector) != expected_dims:
        raise ValueError(f"Vector dimension mismatch: expected {expected_dims}, got {len(vector)}.")
    floats = [float(x) for x in vector]
    if not all(math.isfinite(x) for x in floats):
        raise ValueError("Vector contains NaN or Inf values.")
    return json.dumps(floats)


class PgVectorStore:
    """PostgreSQL + pgvector backend supporting idempotent upsert and cosine search."""

    def __init__(
        self,
        database_url: str,
        dimensions: int,
        *,
        table_name: str = "document_chunks",
    ) -> None:
        if not database_url or not database_url.strip():
            raise ValueError("database_url cannot be empty.")
        if dimensions <= 0:
            raise ValueError(f"dimensions must be positive, got {dimensions}.")
        if not _VALID_IDENT_RE.match(table_name):
            raise ValueError(f"Invalid SQL table name: {table_name!r}")

        self.database_url: str = database_url.strip()
        self.dimensions: int = dimensions
        self.table_name: str = table_name

    def create_schema(self) -> None:
        """Create pgvector extension, chunk table, and traceability/filter indexes."""
        tbl = sql.Identifier(self.table_name)
        idx_doc = sql.Identifier(f"idx_{self.table_name}_strategy_doc")
        idx_chap = sql.Identifier(f"idx_{self.table_name}_strategy_chapter")
        idx_meta = sql.Identifier(f"idx_{self.table_name}_metadata_gin")

        ddl = sql.SQL(
            """
            CREATE EXTENSION IF NOT EXISTS vector;
            CREATE TABLE IF NOT EXISTS {tbl} (
                strategy TEXT NOT NULL,
                chunk_id TEXT NOT NULL,
                document_id TEXT NOT NULL,
                source TEXT NOT NULL,
                page INTEGER NOT NULL,
                text TEXT NOT NULL,
                chapter TEXT,
                section TEXT,
                metadata JSONB NOT NULL,
                embedding vector({dims}) NOT NULL,
                updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                PRIMARY KEY (strategy, chunk_id)
            );
            CREATE INDEX IF NOT EXISTS {idx_doc} ON {tbl} (strategy, document_id);
            CREATE INDEX IF NOT EXISTS {idx_chap} ON {tbl} (strategy, chapter);
            CREATE INDEX IF NOT EXISTS {idx_meta} ON {tbl} USING GIN (metadata);
            """
        ).format(
            tbl=tbl,
            dims=sql.Literal(self.dimensions),
            idx_doc=idx_doc,
            idx_chap=idx_chap,
            idx_meta=idx_meta,
        )

        with psycopg.connect(self.database_url) as conn:
            with conn.cursor() as cur:
                cur.execute(ddl)
            conn.commit()

    def upsert(self, strategy: str, chunks: list[Chunk], vectors: list[list[float]]) -> None:
        """Idempotently upsert chunks + vectors and prune obsolete chunks for updated documents."""
        if not strategy or not strategy.strip():
            raise ValueError("strategy cannot be empty.")
        if len(chunks) != len(vectors):
            raise ValueError(f"chunks/vectors length mismatch: {len(chunks)} != {len(vectors)}.")
        if not chunks:
            return

        strategy_key = strategy.strip()
        seen_ids: set[str] = set()
        by_doc: dict[str, list[str]] = {}
        rows: list[tuple[Any, ...]] = []

        for chunk, vec in zip(chunks, vectors):
            if chunk.chunk_id in seen_ids:
                raise ValueError(f"Duplicate chunk_id {chunk.chunk_id!r} in upsert batch for {strategy_key!r}.")
            seen_ids.add(chunk.chunk_id)
            vec_lit = _format_vector_literal(vec, self.dimensions)
            meta = dict(chunk.metadata or {})
            chapter = str(meta["chapter"]) if meta.get("chapter") is not None else None
            section = str(meta["section"]) if meta.get("section") is not None else None

            by_doc.setdefault(chunk.document_id, []).append(chunk.chunk_id)
            rows.append(
                (
                    strategy_key,
                    chunk.chunk_id,
                    chunk.document_id,
                    chunk.source,
                    int(chunk.page),
                    chunk.text,
                    chapter,
                    section,
                    json.dumps(meta, ensure_ascii=False),
                    vec_lit,
                )
            )

        tbl = sql.Identifier(self.table_name)
        delete_stale_sql = sql.SQL(
            "DELETE FROM {tbl} WHERE strategy = %s AND document_id = %s AND NOT (chunk_id = ANY(%s))"
        ).format(tbl=tbl)
        upsert_sql = sql.SQL(
            """
            INSERT INTO {tbl} (
                strategy, chunk_id, document_id, source, page, text,
                chapter, section, metadata, embedding
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, %s::vector)
            ON CONFLICT (strategy, chunk_id) DO UPDATE SET
                document_id = EXCLUDED.document_id,
                source = EXCLUDED.source,
                page = EXCLUDED.page,
                text = EXCLUDED.text,
                chapter = EXCLUDED.chapter,
                section = EXCLUDED.section,
                metadata = EXCLUDED.metadata,
                embedding = EXCLUDED.embedding,
                updated_at = NOW()
            """
        ).format(tbl=tbl)

        with psycopg.connect(self.database_url) as conn:
            with conn.cursor() as cur:
                for doc_id, active_ids in by_doc.items():
                    cur.execute(delete_stale_sql, (strategy_key, doc_id, active_ids))
                cur.executemany(upsert_sql, rows)
            conn.commit()

    def count_chunks(self, strategy: str) -> int:
        """Return number of stored chunks for a strategy."""
        tbl = sql.Identifier(self.table_name)
        query = sql.SQL("SELECT COUNT(*) FROM {tbl} WHERE strategy = %s").format(tbl=tbl)
        with psycopg.connect(self.database_url) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (strategy.strip(),))
                row = cur.fetchone()
                return int(row[0]) if row else 0

    def search(
        self,
        strategy: str,
        query_vector: list[float],
        top_k: int = 3,
        filters: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        """Filter permitted metadata in SQL, rank by exact cosine distance, and return top-k hits."""
        if not strategy or not strategy.strip():
            raise ValueError("strategy cannot be empty.")
        if top_k <= 0:
            raise ValueError(f"top_k must be positive, got {top_k}.")

        vec_lit = _format_vector_literal(query_vector, self.dimensions)
        where_clauses: list[sql.Composable] = [sql.SQL("strategy = %s")]
        filter_params: list[Any] = [strategy.strip()]

        if filters:
            for key, value in filters.items():
                if value is None:
                    continue
                if key in _ALLOWED_COLUMN_FILTERS:
                    col = sql.Identifier(key)
                    if isinstance(value, (list, tuple)):
                        where_clauses.append(sql.SQL("{col} = ANY(%s)").format(col=col))
                        filter_params.append(list(value))
                    else:
                        where_clauses.append(sql.SQL("{col} = %s").format(col=col))
                        filter_params.append(value)
                elif key in _ALLOWED_JSONB_FILTERS:
                    where_clauses.append(sql.SQL("metadata @> %s::jsonb"))
                    filter_params.append(json.dumps({key: value}, ensure_ascii=False))
                else:
                    raise ValueError(f"Unsupported metadata filter key: {key!r}")

        tbl = sql.Identifier(self.table_name)
        where_sql = sql.SQL(" AND ").join(where_clauses)
        query_sql = sql.SQL(
            """
            SELECT
                chunk_id,
                document_id,
                source,
                page,
                text,
                metadata,
                (embedding <=> %s::vector) AS distance,
                1.0 - (embedding <=> %s::vector) AS score
            FROM {tbl}
            WHERE {where_sql}
            ORDER BY embedding <=> %s::vector ASC, chunk_id ASC
            LIMIT %s
            """
        ).format(tbl=tbl, where_sql=where_sql)

        params: list[Any] = [vec_lit, vec_lit, *filter_params, vec_lit, top_k]
        with psycopg.connect(self.database_url, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(query_sql, params)
                rows = cur.fetchall()

        results: list[dict[str, Any]] = []
        for row in rows:
            meta = row["metadata"]
            if isinstance(meta, str):
                meta = json.loads(meta)
            results.append(
                {
                    "chunk_id": row["chunk_id"],
                    "document_id": row["document_id"],
                    "source": row["source"],
                    "page": int(row["page"]),
                    "text": row["text"],
                    "metadata": meta,
                    "distance": float(row["distance"]),
                    "score": float(row["score"]),
                }
            )
        return results
