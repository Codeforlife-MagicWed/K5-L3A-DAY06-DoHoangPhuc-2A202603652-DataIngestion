"""Implement fixed-size, paragraph-aware, and recursive chunking with metadata preservation."""
from __future__ import annotations

import re

from .models import Chunk, DocumentPage

_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.?!])\s+")
_RECURSIVE_SEPARATORS: tuple[str, ...] = ("\n\n", "\n", ". ", "? ", "! ", " ")


def _build_chunk(
    page: DocumentPage,
    chunk_index: int,
    text: str,
    strategy_label: str,
    extra_meta: dict[str, int] | None = None,
) -> Chunk:
    """Create a Chunk copying all page-level traceability metadata."""
    meta = dict(page.metadata)
    meta["chunk_index"] = chunk_index
    meta["char_len"] = len(text)
    meta["chunking_strategy"] = strategy_label
    if extra_meta:
        meta.update(extra_meta)

    return Chunk(
        chunk_id=f"{page.document_id}_p{page.page:03d}_c{chunk_index:02d}",
        document_id=page.document_id,
        source=page.source,
        page=page.page,
        text=text,
        metadata=meta,
    )


def _split_long_unit(text: str, max_size: int) -> list[str]:
    """Split an oversized paragraph along line breaks (for tables/lists), sentences, or word boundaries."""
    if "\n" in text and ("| --- |" in text or "\n| " in text):
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        if lines and all(len(ln) <= max_size for ln in lines):
            grouped_rows: list[str] = []
            buf = ""
            for ln in lines:
                cand = f"{buf}\n{ln}" if buf else ln
                if len(cand) <= max_size:
                    buf = cand
                else:
                    if buf:
                        grouped_rows.append(buf)
                    buf = ln
            if buf:
                grouped_rows.append(buf)
            return grouped_rows

    sentences = [s.strip() for s in _SENTENCE_SPLIT_RE.split(text) if s.strip()]
    if len(sentences) <= 1:
        # No sentence boundaries found (e.g., long table or code block): split on whitespace.
        units: list[str] = []
        remaining = text.strip()
        while len(remaining) > max_size:
            cut = remaining.rfind(" ", 0, max_size + 1)
            if cut <= max_size // 2:
                cut = max_size
            units.append(remaining[:cut].strip())
            remaining = remaining[cut:].strip()
        if remaining:
            units.append(remaining)
        return units

    grouped: list[str] = []
    current = ""
    for sent in sentences:
        if len(sent) > max_size:
            if current:
                grouped.append(current)
                current = ""
            grouped.extend(_split_long_unit(sent, max_size))
            continue

        candidate = f"{current} {sent}".strip() if current else sent
        if len(candidate) <= max_size:
            current = candidate
        else:
            if current:
                grouped.append(current)
            current = sent

    if current:
        grouped.append(current)
    return grouped


def fixed_size(page: DocumentPage, size: int = 500, overlap: int = 50) -> list[Chunk]:
    """Split page text into overlapping fixed-size character windows and retain metadata."""
    if size <= 0:
        raise ValueError(f"size must be positive, got {size}")
    if overlap < 0 or overlap >= size:
        raise ValueError(f"overlap must satisfy 0 <= overlap < size, got overlap={overlap}, size={size}")

    text = page.text.strip()
    if not text:
        return []

    chunks: list[Chunk] = []
    step = size - overlap
    start = 0
    chunk_index = 1

    while start < len(text):
        end = min(start + size, len(text))
        window = text[start:end].strip()
        if window:
            chunks.append(
                _build_chunk(
                    page=page,
                    chunk_index=chunk_index,
                    text=window,
                    strategy_label="fixed_size",
                    extra_meta={"start_char": start, "end_char": end},
                )
            )
            chunk_index += 1
        if end >= len(text):
            break
        start += step

    return chunks


def by_paragraph(page: DocumentPage, max_size: int = 500) -> list[Chunk]:
    """Group whole paragraphs up to max_size, splitting oversized paragraphs cleanly."""
    if max_size <= 0:
        raise ValueError(f"max_size must be positive, got {max_size}")

    raw_paragraphs = [p.strip() for p in page.text.split("\n\n") if p.strip()]
    if not raw_paragraphs:
        return []

    units: list[str] = []
    for para in raw_paragraphs:
        if len(para) <= max_size:
            units.append(para)
        else:
            units.extend(_split_long_unit(para, max_size))

    packed: list[str] = []
    current = ""
    for unit in units:
        candidate = f"{current}\n\n{unit}".strip() if current else unit
        if len(candidate) <= max_size:
            current = candidate
        else:
            if current:
                packed.append(current)
            current = unit

    if current:
        packed.append(current)

    return [
        _build_chunk(
            page=page,
            chunk_index=idx,
            text=block,
            strategy_label="by_paragraph",
        )
        for idx, block in enumerate(packed, start=1)
    ]


def _recursive_split_pieces(
    text: str,
    max_size: int,
    separators: tuple[str, ...] = _RECURSIVE_SEPARATORS,
) -> list[str]:
    """Recursively break text along the highest-priority separator until every piece fits."""
    stripped = text.strip()
    if not stripped:
        return []
    if len(stripped) <= max_size:
        return [stripped]
    if not separators:
        return [stripped[i : i + max_size].strip() for i in range(0, len(stripped), max_size) if stripped[i : i + max_size].strip()]

    sep = separators[0]
    rest = separators[1:]
    if sep not in stripped:
        return _recursive_split_pieces(stripped, max_size, rest)

    raw_parts = stripped.split(sep)
    joiner = " " if sep in {". ", "? ", "! "} else sep
    keep_punct = sep.rstrip() if sep in {". ", "? ", "! "} else ""

    pieces: list[tuple[str, str]] = []
    for idx, part in enumerate(raw_parts):
        cleaned = part.strip()
        if not cleaned:
            continue
        if keep_punct and idx < len(raw_parts) - 1 and not cleaned.endswith(keep_punct):
            cleaned = f"{cleaned}{keep_punct}"
        if len(cleaned) <= max_size:
            pieces.append((cleaned, joiner))
        else:
            for sub in _recursive_split_pieces(cleaned, max_size, rest):
                pieces.append((sub, joiner))

    merged: list[str] = []
    buf = ""
    for piece, j in pieces:
        candidate = f"{buf}{j}{piece}".strip() if buf else piece
        if len(candidate) <= max_size:
            buf = candidate
        else:
            if buf:
                merged.append(buf)
            buf = piece
    if buf:
        merged.append(buf)
    return merged


def recursive_split(
    page: DocumentPage,
    chunk_size: int = 650,
    overlap: int = 100,
) -> list[Chunk]:
    """Split text recursively using separator hierarchy and retain trailing boundary overlap."""
    if chunk_size <= 0:
        raise ValueError(f"chunk_size must be positive, got {chunk_size}")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            f"overlap must satisfy 0 <= overlap < chunk_size, got overlap={overlap}, chunk_size={chunk_size}"
        )

    text = page.text.strip()
    if not text:
        return []

    # Step 1: produce clean semantic atoms (paragraphs / sentences <= chunk_size)
    atoms: list[str] = []
    for para in text.split("\n\n"):
        para = para.strip()
        if not para:
            continue
        if len(para) <= chunk_size:
            if "| --- |" in para:
                atoms.append(para)
            else:
                atoms.extend(
                    _recursive_split_pieces(
                        para,
                        max_size=max(120, chunk_size // 3),
                        separators=("\n", ". ", "? ", "! ", " "),
                    )
                )
        else:
            atoms.extend(_recursive_split_pieces(para, max_size=chunk_size))

    # Step 2: pack atoms up to chunk_size, carrying up to `overlap` chars of trailing atoms
    packed: list[str] = []
    window: list[str] = []

    def _window_len(items: list[str]) -> int:
        return len("\n\n".join(items))

    for atom in atoms:
        if not window:
            window.append(atom)
            continue

        if _window_len(window + [atom]) <= chunk_size:
            window.append(atom)
            continue

        packed.append("\n\n".join(window))

        # Carry trailing atoms into the next window up to `overlap` while leaving room for `atom`
        carry: list[str] = []
        for prev in reversed(window):
            candidate_carry = [prev] + carry
            if len("\n\n".join(candidate_carry)) <= overlap and _window_len(candidate_carry + [atom]) <= chunk_size:
                carry = candidate_carry
            else:
                break
        window = carry + [atom]

    if window:
        packed.append("\n\n".join(window))

    return [
        _build_chunk(
            page=page,
            chunk_index=idx,
            text=block,
            strategy_label="recursive",
            extra_meta={"chunk_size": chunk_size, "overlap": overlap},
        )
        for idx, block in enumerate(packed, start=1)
    ]
