#!/usr/bin/env python3
"""Migrate governed instruments to amendment-level provenance metadata."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.append(str(SCRIPT_DIR / "lib"))

from amendment_ledger import REQUIRED_HEADERS, VERSION_RE, split_markdown_row

REPO_ROOT = SCRIPT_DIR.parents[1]
SCOPES = (REPO_ROOT / "Governance" / "Constitution", REPO_ROOT / "Governance" / "Charters")
HISTORICAL_AMENDMENT_AGENT = "Caelen"
HISTORICAL_MODEL = "GPT-5 Series"
HISTORICAL_REVIEWER = "Dr M.V. O'Rourke"
MIGRATION_SUMMARY = (
    "Migrated amendment-level provenance metadata to the seven-column Amendment Ledger schema; "
    "removed static authorship and review metadata; no substantive doctrine altered."
)
MIGRATION_MARKER = "Migrated amendment-level provenance metadata to the seven-column Amendment Ledger schema"
HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$")
LEDGER_TITLE_RE = re.compile(r"amendment\s+ledger", re.IGNORECASE)
PROVENANCE_TITLE_RE = re.compile(r"provenance\s*(?:&|and)\s*metadata", re.IGNORECASE)
STATIC_AUTHORSHIP_RE = re.compile(
    r"^(?:\d+(?:\.\d+)*\.?\s+)?authorship(?:\s*(?:&|and)\s*stewardship)?\s*$",
    re.IGNORECASE,
)
STATIC_REVIEW_RE = re.compile(
    r"^(?:\d+(?:\.\d+)*\.?\s+)?review\s*(?:&|and)\s*validation\s*$",
    re.IGNORECASE,
)


def governed_paths() -> list[Path]:
    return [
        path
        for scope in SCOPES
        for path in sorted(scope.glob("*.md"))
        if not path.name.endswith("Index.md")
    ]


def registry_missing_paths() -> list[Path]:
    registry = REPO_ROOT / "Governance" / "CAM.Governance.JSON"
    if not registry.exists():
        return []
    payload = json.loads(registry.read_text(encoding="utf-8"))
    missing: list[Path] = []
    for item in payload.get("items", []):
        link = str(item.get("link") or "")
        if not (link.startswith("Constitution/") or link.startswith("Charters/")):
            continue
        path = REPO_ROOT / "Governance" / link
        if not path.exists():
            missing.append(path)
    return sorted(missing)


def remove_static_footer_sections(text: str) -> tuple[str, int]:
    lines = text.splitlines(keepends=True)
    provenance_start = 0
    for idx, line in enumerate(lines):
        match = HEADING_RE.match(line.rstrip("\r\n"))
        if match and PROVENANCE_TITLE_RE.search(match.group(2)):
            provenance_start = idx

    removals: list[tuple[int, int]] = []
    for idx in range(provenance_start, len(lines)):
        match = HEADING_RE.match(lines[idx].rstrip("\r\n"))
        if not match:
            continue
        title = match.group(2).strip()
        if not (STATIC_AUTHORSHIP_RE.fullmatch(title) or STATIC_REVIEW_RE.fullmatch(title)):
            continue
        level = len(match.group(1))
        end = len(lines)
        for next_idx in range(idx + 1, len(lines)):
            next_match = HEADING_RE.match(lines[next_idx].rstrip("\r\n"))
            if next_match and len(next_match.group(1)) <= level:
                end = next_idx
                break
        removals.append((idx, end))

    for start, end in reversed(removals):
        del lines[start:end]
    return "".join(lines), len(removals)


def bump_minor(version: str) -> str:
    parts = [int(part) for part in version.split(".")]
    if len(parts) < 2:
        raise ValueError(f"Cannot bump ledger version {version!r}")
    return f"{parts[0]}.{parts[1] + 1}"


def ledger_line_bounds(lines: list[str]) -> tuple[int, int]:
    for idx, line in enumerate(lines):
        match = HEADING_RE.match(line.rstrip("\r\n"))
        if not match or not LEDGER_TITLE_RE.search(match.group(2)):
            continue
        level = len(match.group(1))
        end = len(lines)
        for next_idx in range(idx + 1, len(lines)):
            next_match = HEADING_RE.match(lines[next_idx].rstrip("\r\n"))
            if next_match and len(next_match.group(1)) <= level:
                end = next_idx
                break
        return idx, end
    raise ValueError("missing Amendment Ledger")


def render_row(cells: list[str], ending: str = "\n") -> str:
    return "| " + " | ".join(cells) + " |" + ending


def migrate_ledger(text: str, *, timestamp: str, model: str) -> tuple[str, str, bool]:
    lines = text.splitlines(keepends=True)
    start, end = ledger_line_bounds(lines)
    header_idx = None
    separator_idx = None
    version_rows: list[tuple[int, list[str]]] = []
    for idx in range(start, end):
        stripped = lines[idx].strip()
        if not stripped.startswith("|"):
            continue
        cells = split_markdown_row(stripped)
        if cells and cells[0] == "Version":
            header_idx = idx
            continue
        if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            if header_idx is not None and separator_idx is None:
                separator_idx = idx
            continue
        if cells and VERSION_RE.fullmatch(cells[0]):
            version_rows.append((idx, cells))

    if header_idx is None or separator_idx is None or not version_rows:
        raise ValueError("ledger table is missing a header, separator, or version row")

    already_migrated = tuple(split_markdown_row(lines[header_idx])) == REQUIRED_HEADERS
    if already_migrated:
        all_rows_canonical = all(len(cells) == len(REQUIRED_HEADERS) for _idx, cells in version_rows)
        migration_recorded = any(MIGRATION_MARKER.lower() in cells[1].lower() for _idx, cells in version_rows)
        if all_rows_canonical and migration_recorded:
            return text, version_rows[-1][1][0], False

    migrated_rows: list[tuple[int, list[str]]] = []
    for idx, cells in version_rows:
        if len(cells) == 4:
            version, summary, row_timestamp, reference_hash = cells
        elif len(cells) == len(REQUIRED_HEADERS):
            version, summary, row_timestamp, _agent, _model, _reviewer, reference_hash = cells
        else:
            raise ValueError(f"ledger row {cells[0]!r} has {len(cells)} cells")
        migrated_rows.append(
            (idx, [version, summary, row_timestamp, HISTORICAL_AMENDMENT_AGENT, HISTORICAL_MODEL, HISTORICAL_REVIEWER, reference_hash])
        )

    last_idx, latest = migrated_rows[-1]
    latest_was_open = latest[-1].strip() == ""
    if latest_was_open:
        if MIGRATION_SUMMARY.lower() not in latest[1].lower():
            latest[1] = latest[1].rstrip() + " " + MIGRATION_SUMMARY
        latest[2] = timestamp
        latest[3:6] = [HISTORICAL_AMENDMENT_AGENT, model, HISTORICAL_REVIEWER]
        latest[-1] = ""
        migration_version = latest[0]
    else:
        migration_version = bump_minor(latest[0])
        new_row = [
            migration_version,
            MIGRATION_SUMMARY,
            timestamp,
            HISTORICAL_AMENDMENT_AGENT,
            model,
            HISTORICAL_REVIEWER,
            "",
        ]
        ending = "\r\n" if lines[last_idx].endswith("\r\n") else "\n"
        lines.insert(last_idx + 1, render_row(new_row, ending))
        for pos, (idx, cells) in enumerate(migrated_rows):
            migrated_rows[pos] = (idx, cells)

    header_ending = "\r\n" if lines[header_idx].endswith("\r\n") else "\n"
    lines[header_idx] = render_row(list(REQUIRED_HEADERS), header_ending)
    lines[separator_idx] = render_row(["---"] * len(REQUIRED_HEADERS), header_ending)
    for idx, cells in migrated_rows:
        ending = "\r\n" if lines[idx].endswith("\r\n") else "\n"
        lines[idx] = render_row(cells, ending)
    return "".join(lines), migration_version, True


def migrate_text(text: str, *, timestamp: str, model: str) -> tuple[str, str, int, bool]:
    without_static, removed = remove_static_footer_sections(text)
    migrated, version, ledger_changed = migrate_ledger(without_static, timestamp=timestamp, model=model)
    return migrated, version, removed, ledger_changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Write migrated instruments")
    parser.add_argument("--timestamp", required=True, help="UTC timestamp for the migration amendment")
    parser.add_argument("--model", default="GPT-5.6 Thinking", help="Exact model designation for the migration amendment")
    args = parser.parse_args()

    changed: list[str] = []
    failures: list[str] = [
        f"generated registry references missing source instrument: {path.relative_to(REPO_ROOT)}"
        for path in registry_missing_paths()
    ]
    for path in governed_paths():
        try:
            original = path.read_text(encoding="utf-8")
            migrated, version, removed, ledger_changed = migrate_text(
                original, timestamp=args.timestamp, model=args.model
            )
        except ValueError as exc:
            failures.append(f"{path.relative_to(REPO_ROOT)}: {exc}")
            continue
        if migrated != original:
            changed.append(f"{path.relative_to(REPO_ROOT)} -> {version} (removed static sections: {removed})")
            if args.apply:
                path.write_text(migrated, encoding="utf-8")
        elif ledger_changed:
            failures.append(f"{path.relative_to(REPO_ROOT)}: inconsistent migration state")

    for item in changed:
        print(item)
    for failure in failures:
        print(f"ERROR: {failure}")
    if failures:
        return 1
    if changed and not args.apply:
        print(f"Migration required for {len(changed)} instruments (run with --apply).")
        return 1
    print(f"Migration complete; changed instruments: {len(changed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
