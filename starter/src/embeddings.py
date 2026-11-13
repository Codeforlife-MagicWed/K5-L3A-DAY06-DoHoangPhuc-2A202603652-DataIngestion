"""Real Gemini embedding provider with batching, validation, and disk caching."""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
import time
from pathlib import Path
from typing import Protocol

from dotenv import load_dotenv
from google import genai
from google.genai import types

DEFAULT_EMBEDDING_MODEL = "gemini-embedding-001"
DEFAULT_DIMENSIONS = 3072
DEFAULT_BATCH_SIZE = 50
_STARTER_DIR = Path(__file__).resolve().parents[1]
_DEFAULT_CACHE_PATH = _STARTER_DIR.parent / "temp" / "embedding_cache.jsonl"


class Embedder(Protocol):
    model_name: str
    dimensions: int

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Return one vector per input text, in the same order."""
        ...

    def embed_query(self, question: str) -> list[float]:
        """Return a query vector compatible with the stored document vectors."""
        ...


class MyEmbedder:
    """Google Gemini API embedder using `gemini-embedding-001` (no mock fallback)."""

    def __init__(
        self,
        model_name: str | None = None,
        *,
        dimensions: int = DEFAULT_DIMENSIONS,
        batch_size: int = DEFAULT_BATCH_SIZE,
        cache_path: Path | None = _DEFAULT_CACHE_PATH,
        max_retries: int = 5,
    ) -> None:
        load_dotenv(_STARTER_DIR / ".env")

        resolved_model = (model_name or os.getenv("EMBEDDING_MODEL") or DEFAULT_EMBEDDING_MODEL).strip()
        if not resolved_model:
            raise ValueError("EMBEDDING_MODEL cannot be empty.")

        api_key = (os.getenv("GEMINI_API_KEY") or "").strip()
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is missing. Set it in starter/.env or environment.")

        if dimensions <= 0 or batch_size <= 0 or batch_size > 100:
            raise ValueError(
                f"Invalid embedder config: dimensions={dimensions}, batch_size={batch_size} (must be 1..100)."
            )

        self.model_name: str = resolved_model
        self.dimensions: int = dimensions
        self.batch_size: int = batch_size
        self.max_retries: int = max_retries
        self.cache_path: Path | None = Path(cache_path) if cache_path is not None else None

        # AI Studio API keys (AQ.../AIza...) require vertexai=False.
        self._client = genai.Client(api_key=api_key, vertexai=False)
        self._cache: dict[str, list[float]] = self._load_cache()

        self.api_calls: int = 0
        self.cache_hits: int = 0
        self.api_embedded_texts: int = 0
        self.total_api_seconds: float = 0.0

    def _cache_key(self, task_type: str, text: str) -> str:
        payload = f"{self.model_name}::{self.dimensions}::{task_type}::{text}".encode("utf-8")
        return hashlib.sha256(payload).hexdigest()

    def _load_cache(self) -> dict[str, list[float]]:
        cache: dict[str, list[float]] = {}
        if self.cache_path is None or not self.cache_path.exists():
            return cache
        with self.cache_path.open("r", encoding="utf-8") as fh:
            for line in fh:
                raw = line.strip()
                if not raw:
                    continue
                item = json.loads(raw)
                vec = item.get("vector")
                if isinstance(item.get("key"), str) and isinstance(vec, list) and len(vec) == self.dimensions:
                    cache[item["key"]] = [float(v) for v in vec]
        return cache

    def _append_cache(self, new_entries: dict[str, list[float]]) -> None:
        if self.cache_path is None or not new_entries:
            return
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        with self.cache_path.open("a", encoding="utf-8") as fh:
            for key, vec in new_entries.items():
                fh.write(json.dumps({"key": key, "vector": vec}) + "\n")

    @staticmethod
    def _retry_wait_seconds(exc: Exception, attempt: int) -> float | None:
        """Return wait seconds for retryable errors (e.g. 429 Free Tier RPM limit), else None."""
        status = getattr(exc, "code", None) or getattr(exc, "status_code", None)
        msg = str(exc)
        is_rate_limit = status == 429 or "429" in msg or "RESOURCE_EXHAUSTED" in msg
        is_transient = status in {500, 502, 503, 504} or "UNAVAILABLE" in msg or "timed out" in msg.lower()
        if not (is_rate_limit or is_transient):
            return None
        match = re.search(r"retry in (\d+(?:\.\d+)?)s", msg, flags=re.IGNORECASE)
        if match:
            return min(70.0, float(match.group(1)) + 2.0)
        return min(65.0, 20.0 * (attempt + 1)) if is_rate_limit else 2.0 * (attempt + 1)

    def _call_api_batch(self, batch_texts: list[str], task_type: str) -> list[list[float]]:
        for attempt in range(self.max_retries + 1):
            t0 = time.perf_counter()
            try:
                resp = self._client.models.embed_content(
                    model=self.model_name,
                    contents=batch_texts,
                    config=types.EmbedContentConfig(
                        task_type=task_type,
                        output_dimensionality=self.dimensions,
                    ),
                )
                elapsed = time.perf_counter() - t0
                self.api_calls += 1
                self.total_api_seconds += elapsed
                self.api_embedded_texts += len(batch_texts)
                break
            except Exception as exc:  # noqa: BLE001 - retry only rate-limit/transient errors, never mock
                wait_sec = self._retry_wait_seconds(exc, attempt)
                if wait_sec is None or attempt >= self.max_retries:
                    raise RuntimeError(
                        f"Gemini embedding call failed after {attempt + 1} attempt(s) "
                        f"(model={self.model_name}, batch={len(batch_texts)}): {type(exc).__name__}"
                    ) from exc
                time.sleep(wait_sec)

        embeddings = getattr(resp, "embeddings", None) or []
        if len(embeddings) != len(batch_texts):
            raise RuntimeError(
                f"Embedding count mismatch: sent {len(batch_texts)} texts, got {len(embeddings)} vectors."
            )

        vectors: list[list[float]] = []
        for idx, emb in enumerate(embeddings):
            values = [float(x) for x in (getattr(emb, "values", None) or [])]
            if len(values) != self.dimensions:
                raise RuntimeError(
                    f"Dimension mismatch at batch index {idx}: expected {self.dimensions}, got {len(values)}."
                )
            if not all(math.isfinite(x) for x in values):
                raise RuntimeError(f"Non-finite embedding value encountered at batch index {idx}.")
            vectors.append(values)
        return vectors

    def _embed_with_cache(self, texts: list[str], task_type: str) -> list[list[float]]:
        if not texts:
            return []

        keys: list[str] = []
        missing_pairs: dict[str, str] = {}
        for idx, text in enumerate(texts):
            if not isinstance(text, str) or not text.strip():
                raise ValueError(f"Input text at index {idx} is empty or non-string.")
            key = self._cache_key(task_type, text)
            keys.append(key)
            if key in self._cache:
                self.cache_hits += 1
            elif key not in missing_pairs:
                missing_pairs[key] = text

        if missing_pairs:
            missing_items = list(missing_pairs.items())
            for start in range(0, len(missing_items), self.batch_size):
                chunk_items = missing_items[start : start + self.batch_size]
                batch_keys = [k for k, _ in chunk_items]
                batch_texts = [t for _, t in chunk_items]
                vectors = self._call_api_batch(batch_texts, task_type=task_type)
                newly_cached = dict(zip(batch_keys, vectors))
                self._cache.update(newly_cached)
                self._append_cache(newly_cached)

        return [self._cache[k] for k in keys]

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed document chunks in batches with `RETRIEVAL_DOCUMENT` task type."""
        return self._embed_with_cache(texts, task_type="RETRIEVAL_DOCUMENT")

    def embed_query(self, question: str) -> list[float]:
        """Embed a retrieval query with `RETRIEVAL_QUERY` task type."""
        return self._embed_with_cache([question], task_type="RETRIEVAL_QUERY")[0]
