#!/usr/bin/env python3
"""Validate canonical top document headers for governed markdown instruments."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import NamedTuple

REPO_ROOT = Path(__file__).resolve().parents[2]
GOVERNED_PREFIXES = (
    "Governance/Constitution/",
    "Governance/Charters/",
    "Governance/Laws/",
)

CANONICAL_H1_RE = re.compile(r"^#\s+(CAM-[A-Z0-9]+(?:-[A-Z0-9]+)+)\s+—\s+(.+?)\s*$")
ANY_H1_RE = re.compile(r"^#\s+(.+?)\s*$")
METADATA_RE = re.compile(r"^\*\*([^:*]+):\*\*\s*(.*)$")
METADATA_BLOCK_MIN_KEYS = 2


class HeaderIssue(NamedTuple):
    path: str
    line: int
    code: str
    message: str

    def render(self) -> str:
        return f"{self.path}:{self.line}: {self.code}: {self.message}"


def is_governed_markdown(path: Path) -> bool:
    rel = path.relative_to(REPO_ROOT).as_posix()
    if not rel.endswith(".md"):
        return False
    if not rel.startswith(GOVERNED_PREFIXES):
        return False
    return not path.name.endswith("Index.md")


def governed_markdown_files(root: Path = REPO_ROOT) -> list[Path]:
    paths: list[Path] = []
    for prefix in GOVERNED_PREFIXES:
        scope = root / prefix
        if not scope.exists():
            continue
        paths.extend(p for p in sorted(scope.glob("*.md")) if is_governed_markdown(p))
    return sorted(paths)


def first_non_empty_line(lines: list[str]) -> tuple[int, str] | None:
    for idx, line in enumerate(lines, start=1):
        if line.strip():
            return idx, line.rstrip("\n\r")
    return None


def top_header_region(lines: list[str]) -> list[tuple[int, str]]:
    """Return the initial title/metadata block before the first divider or body H2."""
    region: list[tuple[int, str]] = []
    for idx, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n\r")
        stripped = line.strip()
        if idx > 1 and (stripped == "---" or stripped.startswith("## ")):
            break
        region.append((idx, line))
    return region


def metadata_blocks_in_header(lines: list[str]) -> list[tuple[int, int, list[str]]]:
    blocks: list[tuple[int, int, list[str]]] = []
    active_start: int | None = None
    active_end: int | None = None
    active_keys: list[str] = []

    def flush() -> None:
        nonlocal active_start, active_end, active_keys
        if active_start is not None and len(active_keys) >= METADATA_BLOCK_MIN_KEYS:
            blocks.append((active_start, active_end or active_start, active_keys[:]))
        active_start = None
        active_end = None
        active_keys = []

    for line_no, line in top_header_region(lines):
        m = METADATA_RE.match(line.strip())
        if m:
            if active_start is None:
                active_start = line_no
            active_end = line_no
            active_keys.append(m.group(1).strip().lower())
        else:
            flush()
    flush()
    return blocks


def validate_text(path: str, text: str, *, expected_id: str | None = None) -> list[HeaderIssue]:
    lines = text.splitlines()
    expected = expected_id or Path(path).stem
    issues: list[HeaderIssue] = []

    first = first_non_empty_line(lines)
    if first is None:
        issues.append(HeaderIssue(path, 1, "missing_h1", "file is empty; expected canonical H1 title"))
        return issues

    first_line_no, first_line = first
    if first_line_no != 1:
        issues.append(HeaderIssue(path, first_line_no, "h1_not_first_non_empty", "canonical H1 must be the first non-empty line"))

    if not first_line.startswith("# "):
        issues.append(HeaderIssue(path, first_line_no, "missing_h1", "first non-empty line must be a single H1 heading"))
    else:
        canonical = CANONICAL_H1_RE.match(first_line)
        any_h1 = ANY_H1_RE.match(first_line)
        if not canonical:
            h1_text = any_h1.group(1).strip() if any_h1 else ""
            if h1_text == expected or h1_text.startswith(expected) and "—" not in h1_text:
                issues.append(HeaderIssue(path, first_line_no, "h1_only_instrument_id", "canonical H1 must include an em dash and full title"))
            elif "—" not in first_line:
                issues.append(HeaderIssue(path, first_line_no, "h1_missing_emdash", "canonical H1 must contain an em dash separator (—)"))
            elif first_line.rstrip().endswith("—") or not first_line.split("—", 1)[1].strip():
                issues.append(HeaderIssue(path, first_line_no, "h1_missing_full_title", "canonical H1 must include the full canonical title after the em dash"))
            else:
                issues.append(HeaderIssue(path, first_line_no, "malformed_h1", "canonical H1 must match '# {INSTRUMENT_ID} — {FULL_CANONICAL_TITLE}'"))
        else:
            h1_id, title = canonical.groups()
            if h1_id != expected:
                issues.append(HeaderIssue(path, first_line_no, "instrument_id_mismatch", f"filename instrument ID {expected!r} does not match H1 instrument ID {h1_id!r}"))
            if not title.strip():
                issues.append(HeaderIssue(path, first_line_no, "h1_missing_full_title", "canonical H1 must include the full canonical title after the em dash"))

    region = top_header_region(lines)
    canonical_h1s = [(line_no, line) for line_no, line in region if line.startswith("# ") and line_no != first_line_no]
    for line_no, _line in canonical_h1s:
        issues.append(HeaderIssue(path, line_no, "duplicated_h1", "duplicate top-level H1 found inside the canonical header/metadata block"))

    blocks = metadata_blocks_in_header(lines)
    if len(blocks) > 1:
        first_block = blocks[0]
        for start, _end, _keys in blocks[1:]:
            issues.append(HeaderIssue(path, start, "duplicated_metadata_block", f"duplicate top-level metadata/header block near document top; first metadata block starts at line {first_block[0]}"))
    elif blocks:
        seen: dict[str, int] = {}
        for start, _end, keys in blocks:
            for offset, key in enumerate(keys):
                line_no = start + offset
                if key in seen:
                    issues.append(HeaderIssue(path, line_no, "duplicated_metadata_heading", f"duplicate metadata heading {key!r} near document top; first seen at line {seen[key]}"))
                else:
                    seen[key] = line_no

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate governed markdown canonical H1 headers.")
    parser.add_argument("paths", nargs="*", help="Optional governed markdown files to validate.")
    parser.add_argument("--strict", action="store_true", help="Return non-zero when structural header issues are found.")
    args = parser.parse_args()

    if args.paths:
        paths = [REPO_ROOT / path for path in args.paths]
    else:
        paths = governed_markdown_files(REPO_ROOT)

    issues: list[HeaderIssue] = []
    checked = 0
    for path in paths:
        if not path.exists() or not is_governed_markdown(path):
            continue
        checked += 1
        rel = path.relative_to(REPO_ROOT).as_posix()
        issues.extend(validate_text(rel, path.read_text(encoding="utf-8"), expected_id=path.stem))

    for issue in issues:
        print(("ERROR" if args.strict else "WARNING") + f": {issue.render()}")
    print(f"Canonical header files checked: {checked}")
    print(f"Canonical header issues: {len(issues)}")
    if issues and args.strict:
        return 1
    print("Canonical header validation passed" if not issues else "Canonical header validation completed with warnings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
