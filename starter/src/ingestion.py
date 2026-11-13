"""Read and normalize source PDF data with page-level traceability and metadata."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Any

from pypdf import PdfReader

from .models import DocumentPage

DEFAULT_PAGE_RANGE: tuple[int, int] = (17, 76)
MIN_CONTENT_CHARS: int = 80

_LIGATURE_MAP: dict[str, str] = {
    "\ufb00": "ff",
    "\ufb01": "fi",
    "\ufb02": "fl",
    "\ufb03": "ffi",
    "\ufb04": "ffl",
    "\u00a0": " ",
}

_FOOTER_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"^Access for free at openstax\.org\.?$", re.IGNORECASE),
    re.compile(r"^\d+\s+[12]\s*•\s*(?:Statements|Expressions)\s*$"),
    re.compile(r"^[12]\.\d+\s*•\s*.+?\s+\d+\s*$"),
)

_TABLE_CAPTION_RE = re.compile(
    r"^Table\s+\d+\.\d+(?!(?:\s+(?:shows|lists|gives|summarizes|provides|illustrates|contains|below|above))\b)"
)
_NON_TABLE_BLOCK_RE = re.compile(
    r"^(?:•|[12]\.\d+\s+[A-Z]|\d+\s*\.\s+|[a-d]\.\s+|"
    r"Learning [Oo]bjectives\b|CHECKPOINT\b|CONCEPTS IN PRACTICE\b|"
    r"EXPLORING FURTHER\b|TRY IT\b|EXAMPLE\s+\d+\.\d+\b|"
    r"Chapter Outline\b|Introduction\b|Figure\s+\d+\.\d+\b)"
)
_SENTENCE_END_RE = re.compile(r'(?:[.?!:]|["\')\]][.?!:]?|[.?!]["\')])$')
_SECTION_HEADING_RE = re.compile(r"(?:^|\n)\s*([12]\.\d+)\s+(?!•)[A-Z]")
_SECTION_FOOTER_RE = re.compile(r"([12]\.\d+)\s*•\s*.+?\s+\d+\s*$")


def _strip_running_headers_and_footers(lines: list[str], *, preserve_layout: bool = False) -> list[str]:
    """Remove OpenStax running headers/footers while optionally keeping indentation and blank lines."""
    cleaned: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if preserve_layout and cleaned and cleaned[-1] != "":
                cleaned.append("")
            continue
        if any(pat.match(stripped) for pat in _FOOTER_PATTERNS):
            continue
        cleaned.append(line.rstrip() if preserve_layout else stripped)

    while cleaned and not cleaned[-1].strip():
        cleaned.pop()

    # Chapter opener pages end with standalone chapter title + chapter number (e.g. "Statements" / "1")
    non_empty_idx = [i for i, ln in enumerate(cleaned) if ln.strip()]
    if (
        len(non_empty_idx) >= 2
        and cleaned[non_empty_idx[-2]].strip() in {"Statements", "Expressions"}
        and cleaned[non_empty_idx[-1]].strip() in {"1", "2"}
    ):
        del cleaned[non_empty_idx[-2]:]
        while cleaned and not cleaned[-1].strip():
            cleaned.pop()

    return cleaned


def _split_layout_blocks(lines: list[str]) -> list[list[str]]:
    """Group non-empty layout lines into blocks separated by one or more blank lines."""
    blocks: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        if not line.strip():
            if current:
                blocks.append(current)
                current = []
        else:
            current.append(line)
    if current:
        blocks.append(current)
    return blocks


def _has_column_gap(line: str, min_gap: int = 3) -> bool:
    """Return True if a layout line contains wide horizontal column spacing after its left margin."""
    stripped = line.strip()
    return bool(re.search(rf"\S\s{{{min_gap},}}\S", stripped))


def _is_tabular_block(block: list[str]) -> bool:
    """Check whether a layout block represents a table row/header rather than prose, list, or numbered code."""
    first_stripped = block[0].strip()
    if _NON_TABLE_BLOCK_RE.match(first_stripped):
        return False
    # Exclude line-numbered code listings (e.g. "  1   # Display the menu...")
    if all(re.match(r"^\s*\d+\s{2,}(?:#|[A-Za-z_])", ln) for ln in block):
        return False
    return any(_has_column_gap(ln, min_gap=3) for ln in block)


def _is_table_divider_block(block: list[str]) -> bool:
    """Check whether a single-line block is an internal 1-column table category divider."""
    if len(block) != 1 or _has_column_gap(block[0], min_gap=3):
        return False
    text = re.sub(r"\s+", " ", block[0]).strip()
    if _NON_TABLE_BLOCK_RE.match(text) or _SENTENCE_END_RE.search(text):
        return False
    words = text.split()
    return 1 <= len(words) <= 4 and words[0][0].isupper()


def _find_column_slices(table_lines: list[str], min_gutter: int = 2) -> list[tuple[int, int]]:
    """Detect column character intervals by finding vertical whitespace gutters across table lines."""
    if not table_lines:
        return []
    width = max(len(ln) for ln in table_lines)
    occupied = [False] * width
    for ln in table_lines:
        for idx, ch in enumerate(ln):
            if ch != " ":
                occupied[idx] = True

    # Find gaps of >= min_gutter spaces inside the active horizontal span.
    active_indices = [i for i, occ in enumerate(occupied) if occ]
    if not active_indices:
        return []
    left_edge, right_edge = active_indices[0], active_indices[-1] + 1

    gutters: list[tuple[int, int]] = []
    gap_start: int | None = None
    for idx in range(left_edge, right_edge):
        if not occupied[idx]:
            if gap_start is None:
                gap_start = idx
        else:
            if gap_start is not None and idx - gap_start >= min_gutter:
                gutters.append((gap_start, idx))
            gap_start = None

    slices: list[tuple[int, int]] = []
    cursor = 0
    for g_start, g_end in gutters:
        slices.append((cursor, g_start))
        cursor = g_end
    slices.append((cursor, width))

    # Merge adjacent slices that never appear together on the same line (e.g. centered header over short left-aligned data).
    merged_slices: list[tuple[int, int]] = [slices[0]]
    for s_start, s_end in slices[1:]:
        prev_start, prev_end = merged_slices[-1]
        co_occur = any(
            ln[prev_start:prev_end].strip() and ln[s_start:s_end].strip()
            for ln in table_lines
        )
        if co_occur:
            merged_slices.append((s_start, s_end))
        else:
            merged_slices[-1] = (prev_start, s_end)
    return merged_slices


_LIST_ITEM_START_RE = re.compile(r"^(?:•\s+|[a-d]\.\s+|\d+\s*\.\s+)")


def _join_wrapped_lines(lines: list[str], *, preserve_list_newlines: bool = False) -> str:
    """Join physically wrapped lines while preserving hyphenated breaks, URLs, and optional list items."""
    cleaned = [re.sub(r"[ \t]+", " ", ln).strip() for ln in lines if ln.strip()]
    if not cleaned:
        return ""
    out = cleaned[0]
    for nxt in cleaned[1:]:
        if preserve_list_newlines and _LIST_ITEM_START_RE.match(nxt):
            out = f"{out}\n{nxt}"
        elif out.endswith("/") or re.search(r"[A-Za-z0-9]-$", out):
            out = f"{out}{nxt}"
        else:
            out = f"{out} {nxt}"
    return out


def _looks_like_header_row(cells: list[str]) -> bool:
    """Heuristic check so headerless tables (e.g. Keyword grid, Code/Output) keep all data rows."""
    non_empty = [c for c in cells if c]
    if not non_empty or len(non_empty) == 1:
        return False
    lowered = {c.lower() for c in non_empty}
    if lowered & {"false", "none", "true", "await", "elif", "yield"}:
        return False
    header_keywords = {
        "valid string", "invalid string", "code", "output", "operator", "description",
        "example", "examples", "result", "mistake", "error message", "explanation",
        "function", "syntax", "constant", "value", "guideline", "common mistakes",
        "field", "example use of python", "application", "provided input", "expected output",
    }
    if any(c.lower() in header_keywords for c in non_empty):
        return True
    return all(len(c.split()) <= 4 and not re.search(r"[=()\"'0-9]", c) for c in non_empty)


def _format_table_markdown(row_blocks: list[list[str]]) -> str:
    """Convert layout-aligned table row blocks into a clean Markdown pipe table."""
    col_basis_lines = [ln for blk in row_blocks if not _is_table_divider_block(blk) for ln in blk]
    col_slices = _find_column_slices(col_basis_lines, min_gutter=2)
    if len(col_slices) <= 1:
        return "\n\n".join(_join_wrapped_lines(blk) for blk in row_blocks)

    num_cols = len(col_slices)
    rows: list[list[str]] = []
    for blk in row_blocks:
        if _is_table_divider_block(blk):
            label = re.sub(r"\s+", " ", blk[0]).strip()
            rows.append([f"**{label}**"] + [""] * (num_cols - 1))
            continue

        row_cells: list[str] = []
        for c_start, c_end in col_slices:
            cell_parts = [ln[c_start:c_end].strip() for ln in blk if c_start < len(ln)]
            cell_text = _join_wrapped_lines(cell_parts).replace("|", "\\|")
            row_cells.append(cell_text)
        if any(row_cells):
            rows.append(row_cells)

    if not rows:
        return ""

    if _looks_like_header_row(rows[0]):
        header = rows[0]
        body = rows[1:]
    else:
        header = [f"Col {i + 1}" for i in range(num_cols)]
        body = rows

    # Avoid duplicating embedded subheaders as Markdown separator breaks; keep them as bold rows cleanly.
    lines_md = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * num_cols) + " |",
    ]
    for r in body:
        lines_md.append("| " + " | ".join(r) + " |")
    return "\n".join(lines_md)


def _normalize_layout_blocks(blocks: list[list[str]]) -> str:
    """Render detected table groups as Markdown tables and prose blocks as clean paragraphs."""
    # Map block index -> formatted Markdown string for table groups anchored by Table captions.
    table_spans: dict[int, tuple[int, str]] = {}
    claimed: set[int] = set()

    for idx, blk in enumerate(blocks):
        caption_text = _join_wrapped_lines(blk)
        if not _TABLE_CAPTION_RE.match(caption_text):
            continue

        start = idx
        scan = idx - 1
        while scan >= 0 and scan not in claimed:
            cand = blocks[scan]
            cand_text = _join_wrapped_lines(cand)
            if _TABLE_CAPTION_RE.match(cand_text):
                break
            if _is_tabular_block(cand):
                start = scan
                scan -= 1
            elif (
                _is_table_divider_block(cand)
                and scan - 1 >= 0
                and scan - 1 not in claimed
                and _is_tabular_block(blocks[scan - 1])
            ):
                start = scan
                scan -= 1
            else:
                break

        if start < idx:
            md_table = _format_table_blocks_if_valid(blocks[start:idx])
            if md_table:
                table_spans[start] = (idx, f"{md_table}\n\n{caption_text}")
                for k in range(start, idx + 1):
                    claimed.add(k)

    rendered: list[str] = []
    i = 0
    while i < len(blocks):
        if i in table_spans:
            end_idx, table_md = table_spans[i]
            rendered.append(table_md)
            i = end_idx + 1
            continue
        rendered.append(_join_wrapped_lines(blocks[i], preserve_list_newlines=True))
        i += 1

    return "\n\n".join(part for part in rendered if part)


def _format_table_blocks_if_valid(row_blocks: list[list[str]]) -> str:
    """Format table blocks only when column structure is detected; otherwise return empty string."""
    col_basis_lines = [ln for blk in row_blocks if not _is_table_divider_block(blk) for ln in blk]
    if len(_find_column_slices(col_basis_lines, min_gutter=2)) <= 1:
        return ""
    return _format_table_markdown(row_blocks)


def normalize_text(text: str) -> str:
    """Normalize Unicode, preserve layout paragraph/table structure, and drop headers/footers."""
    if not text:
        return ""

    normalized = unicodedata.normalize("NFC", text)
    for src, target in _LIGATURE_MAP.items():
        normalized = normalized.replace(src, target)

    normalized = normalized.replace("\r\n", "\n").replace("\r", "\n")
    raw_lines = normalized.split("\n")
    lines = _strip_running_headers_and_footers(raw_lines, preserve_layout=True)
    if not lines:
        return ""

    blocks = _split_layout_blocks(lines)
    return _normalize_layout_blocks(blocks)


def _infer_chapter(page_num: int) -> str:
    """Map 1-indexed PDF page to manifest chapter ID."""
    if 17 <= page_num <= 45:
        return "ch1_statements"
    if 47 <= page_num <= 76:
        return "ch2_expressions"
    return "other"


def _detect_section(raw_text: str, page_num: int, current_section: str) -> str:
    """Detect section number from page headings or odd-page footers, falling back cleanly."""
    if page_num == 17:
        return "1.0"
    if page_num == 47:
        return "2.0"

    footer_match = _SECTION_FOOTER_RE.search(raw_text)
    if footer_match:
        return footer_match.group(1)

    heading_matches = _SECTION_HEADING_RE.findall(raw_text)
    if heading_matches:
        return heading_matches[0]

    return current_section


def load_pdf(
    path: Path,
    document_id: str,
    source: str,
    page_range: tuple[int, int] | None = DEFAULT_PAGE_RANGE,
    empty_pages_log: list[dict[str, Any]] | None = None,
) -> list[DocumentPage]:
    """Extract selected physical PDF pages, normalize text, and retain traceability metadata.

    Blank or non-content pages (such as PDF page 46) are skipped and optionally recorded in
    ``empty_pages_log`` instead of polluting downstream chunks.
    """
    pdf_path = Path(path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF corpus not found: {pdf_path}")

    reader = PdfReader(str(pdf_path))
    total_pages = len(reader.pages)

    start_page = page_range[0] if page_range else 1
    end_page = page_range[1] if page_range else total_pages
    if start_page < 1 or end_page > total_pages or start_page > end_page:
        raise ValueError(
            f"Invalid page_range ({start_page}, {end_page}) for PDF with {total_pages} pages."
        )

    pages: list[DocumentPage] = []
    current_section = "1.0" if start_page <= 45 else "2.0"

    for page_num in range(start_page, end_page + 1):
        raw_text = reader.pages[page_num - 1].extract_text(extraction_mode="layout") or ""
        chapter = _infer_chapter(page_num)
        current_section = _detect_section(raw_text, page_num, current_section)

        clean_text = normalize_text(raw_text)
        if len(clean_text) < MIN_CONTENT_CHARS:
            if empty_pages_log is not None:
                empty_pages_log.append(
                    {
                        "document_id": document_id,
                        "source": source,
                        "page": page_num,
                        "book_page": page_num - 10,
                        "raw_chars": len(raw_text),
                        "normalized_chars": len(clean_text),
                        "reason": "empty_or_header_only_page",
                    }
                )
            continue

        pages.append(
            DocumentPage(
                document_id=document_id,
                source=source,
                page=page_num,
                text=clean_text,
                metadata={
                    "book_page": page_num - 10,
                    "chapter": chapter,
                    "section": current_section,
                    "char_count": len(clean_text),
                },
            )
        )

    return pages
