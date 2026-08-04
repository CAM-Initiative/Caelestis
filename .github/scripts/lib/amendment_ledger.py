"""Canonical Amendment Ledger parsing helpers.

The ledger is a governed seven-column Markdown table.  Callers identify
values by canonical header name rather than relying on a historical cell
position.
"""
from __future__ import annotations

from dataclasses import dataclass
import re

REQUIRED_HEADERS = (
    "Version",
    "Change Summary",
    "Timestamp (UTC)",
    "Agent",
    "Model",
    "Reviewer",
    "Reference Hash",
)

VERSION_RE = re.compile(r"^\d+(?:\.\d+)+$")
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def split_markdown_row(line: str) -> list[str]:
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    return [cell.strip() for cell in value.split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def header_map(cells: list[str]) -> dict[str, int]:
    return {name: cells.index(name) for name in REQUIRED_HEADERS if name in cells}


def has_exact_headers(cells: list[str]) -> bool:
    return tuple(cells) == REQUIRED_HEADERS


@dataclass(frozen=True)
class LedgerRow:
    line_number: int
    cells: tuple[str, ...]
    columns: dict[str, int]

    def get(self, header: str) -> str:
        return self.cells[self.columns[header]]


def parse_rows(section: str, *, require_exact_header: bool = True) -> tuple[list[str] | None, list[LedgerRow]]:
    """Return the table header and dotted-version rows in a ledger section."""
    header: list[str] | None = None
    columns: dict[str, int] = {}
    rows: list[LedgerRow] = []
    for line_number, line in enumerate(section.splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = split_markdown_row(stripped)
        if cells and cells[0] == "Version":
            header = cells
            columns = header_map(cells)
            if require_exact_header and not has_exact_headers(cells):
                columns = {}
            continue
        if cells and VERSION_RE.fullmatch(cells[0]):
            rows.append(LedgerRow(line_number, tuple(cells), dict(columns)))
    return header, rows


def latest_reference_hash(section: str) -> str:
    header, rows = parse_rows(section)
    if not header or not has_exact_headers(header) or not rows:
        return ""
    latest = rows[-1]
    if len(latest.cells) != len(REQUIRED_HEADERS):
        return ""
    return latest.get("Reference Hash").strip()
