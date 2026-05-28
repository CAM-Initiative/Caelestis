#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))


import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from ledger_sha_policy import classify_ledger_sha
from ledger_sha_exceptions import allows_blank_sha

REPO_ROOT = Path(__file__).resolve().parents[2]

SCOPED_PREFIXES = (
    "Governance/Constitution/",
    "Governance/Charters/",
)

AMENDMENT_HEADING_RE = re.compile(r"^##+\s+.*amendment\s+ledger", re.IGNORECASE | re.MULTILINE)
NEXT_HEADING_RE = re.compile(r"^##+\s+", re.MULTILINE)
VERSION_CELL_RE = re.compile(r"^\d+\.\d+(?:\.\d+)?$")
PLACEHOLDER_HASHES = {"-", "—"}
VALIDATION_STAGES = {"pre_fix", "fix", "post_fix", "downstream_block"}

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

FORMATTING_ONLY_MARKERS = (
    "minor formatting patch",
    "formatting correction",
    "metadata formatting correction",
    "formatting-only",
    "formatting only",
    "numbering-only",
    "numbering only",
    "metadata-ordering",
    "metadata ordering",
    "table-alignment",
    "table alignment",
    "heading-format",
    "heading format",
    "whitespace-only",
    "whitespace only",
)

SUBSTANTIVE_CHANGE_MARKERS = (
    "substantive",
    "clause change",
    "clause changes",
    "article change",
    "article changes",
    "body change",
    "body changes",
    "normative change",
    "normative changes",
)


def is_formatting_only_description(description: str) -> bool:
    normalized = description.strip().lower()
    return any(marker in normalized for marker in FORMATTING_ONLY_MARKERS)


def has_substantive_change_marker(description: str) -> bool:
    normalized = description.strip().lower()
    return any(marker in normalized for marker in SUBSTANTIVE_CHANGE_MARKERS)


def extract_ledger_hash_cells(full_text: str) -> list[str]:
    bounds = get_amendment_section_bounds(full_text)
    if not bounds:
        return []
    start, end = bounds
    section = full_text[start:end]
    hashes: list[str] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cols = split_markdown_table_row(stripped)
        if not cols:
            continue
        first = cols[0]
        if first.lower() == "version" or (first and set(first) <= {"-"}):
            continue
        if VERSION_CELL_RE.match(first):
            while len(cols) < 4:
                cols.append("")
            hashes.append(cols[-1].strip())
    return hashes




def extract_ledger_hash_rows_with_lines(full_text: str) -> list[tuple[int, str, str]]:
    bounds = get_amendment_section_bounds(full_text)
    if not bounds:
        return []
    start, end = bounds
    rows: list[tuple[int, str, str]] = []
    section = full_text[start:end]
    section_start_line = full_text[:start].count("\n") + 1
    for offset, line in enumerate(section.splitlines(), start=0):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cols = split_markdown_table_row(stripped)
        if not cols:
            continue
        first = cols[0]
        if first.lower() == "version" or (first and set(first) <= {"-"}):
            continue
        if VERSION_CELL_RE.match(first):
            while len(cols) < 4:
                cols.append("")
            rows.append((section_start_line + offset, first, cols[-1].strip()))
    return rows

def evaluate_historical_and_latest_hashes(path: str, full_text: str, failures: list[str], warnings: list[str], summary: dict[str,int], *, strict_latest: bool = False) -> None:
    rows = extract_ledger_hash_rows_with_lines(full_text)
    if not rows:
        return
    trailing_blank_rows = 0
    for _line_no, _version, h in reversed(rows):
        if h.strip() == "":
            trailing_blank_rows += 1
        else:
            break
    if trailing_blank_rows > 1:
        failures.append(
            f"{path}: Open Amendment Cycle Fragmentation detected ({trailing_blank_rows} trailing unsealed rows). "
            "Only the latest Amendment Ledger row may remain blank; consolidate unsealed rows into one latest open row."
        )
    latest = rows[-1]
    historical = rows[:-1]
    for line_no, version, h in historical:
        classification = classify_ledger_sha(h, is_latest=False, strict_latest=False)
        if classification == "valid_hash":
            summary["valid_historical_sha"] = summary.get("valid_historical_sha", 0) + 1
        elif classification == "known_null":
            summary["historical_known_null_shas"] = summary.get("historical_known_null_shas", 0) + 1
        else:
            summary["invalid_historical_sha"] = summary.get("invalid_historical_sha", 0) + 1
            reason = "blank_historical" if classification == "blank_historical" else "malformed_historical"
            failures.append(f"{path}:{line_no}: Historical Amendment Ledger SHA invalid (version {version}, hash={h!r}, reason={reason})")

    latest_line, latest_version, latest_hash = latest
    doc_id = Path(path).stem
    latest_class = classify_ledger_sha(latest_hash, is_latest=True, strict_latest=strict_latest)
    if latest_class == "valid_hash":
        summary["valid_latest_sha"] = summary.get("valid_latest_sha", 0) + 1
    elif latest_class == "latest_pending_blank":
        summary["blank_latest_sha_allowed"] = summary.get("blank_latest_sha_allowed", 0) + 1
        warnings.append(f"{path}: latest ledger SHA is blank; allowed for pending/current ledger entry")
    elif allows_blank_sha(doc_id) and latest_hash.strip() == "":
        summary["blank_latest_sha_allowed"] = summary.get("blank_latest_sha_allowed", 0) + 1
        warnings.append(f"Allowed blank SHA: {doc_id}")
    else:
        summary["blank_latest_sha_rejected"] = summary.get("blank_latest_sha_rejected", 0) + 1
        failures.append(f"{path}: latest ledger SHA is blank/placeholder and strict-latest mode is enabled")

EXCLUDED_LEDGER_DOC_IDS = {"CAM-BS2025-AEON-003-SCH-01", "CAM-BS2025-AEON-003-SCH-03"}


def is_excluded_ledger_path(path: str) -> bool:
    stem = Path(path).stem
    return stem in EXCLUDED_LEDGER_DOC_IDS



def run_git(args: list[str], check: bool = True) -> str:
    proc = subprocess.run(["git", *args], cwd=REPO_ROOT, text=True, capture_output=True)
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout


def list_modified_files(base: str, head: str, *, staged: bool = False) -> list[str]:
    if staged:
        out = run_git(["diff", "--cached", "--name-only", "--diff-filter=ACMR"])
    else:
        out = run_git(["diff", "--name-only", f"{base}..{head}"])
    paths = []
    for raw in out.splitlines():
        path = raw.strip()
        if not path.endswith(".md"):
            continue
        if not path.startswith(SCOPED_PREFIXES):
            continue
        if is_excluded_ledger_path(path):
            continue
        paths.append(path)
    return paths


def list_scoped_markdown_files() -> list[str]:
    paths: list[str] = []
    for prefix in SCOPED_PREFIXES:
        scope = REPO_ROOT / prefix
        if not scope.exists():
            continue
        for md in sorted(scope.glob("*.md")):
            rel = md.relative_to(REPO_ROOT).as_posix()
            if is_excluded_ledger_path(rel):
                continue
            paths.append(rel)
    return paths


def get_blob(rev: str, path: str) -> str:
    if rev == ":":
        blob_ref = f":{path}"
    else:
        blob_ref = f"{rev}:{path}"
    proc = subprocess.run(["git", "show", blob_ref], cwd=REPO_ROOT, text=True, capture_output=True)
    if proc.returncode != 0:
        return ""
    return proc.stdout


def normalize_for_whitespace_compare(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.splitlines()).strip()


def get_amendment_section_bounds(text: str) -> tuple[int, int] | None:
    m = AMENDMENT_HEADING_RE.search(text)
    if not m:
        return None

    start = m.start()
    tail = text[m.end():]
    nxt = NEXT_HEADING_RE.search(tail)
    end = (m.end() + nxt.start()) if nxt else len(text)
    return (start, end)


def extract_amendment_section(text: str) -> str:
    bounds = get_amendment_section_bounds(text)
    if not bounds:
        return ""
    start, end = bounds
    return text[start:end]


def has_amendment_ledger(text: str) -> bool:
    return AMENDMENT_HEADING_RE.search(text) is not None


def parse_ledger_versions(section: str) -> list[str]:
    versions: list[str] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cols = [c.strip() for c in stripped.strip("|").split("|")]
        if not cols:
            continue
        first = cols[0]
        if first.lower() == "version":
            continue
        if set(first) <= {"-"}:
            continue
        if VERSION_CELL_RE.match(first):
            versions.append(first)
    return versions


def normalize_for_hash(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = "\n".join(line.rstrip() for line in normalized.split("\n"))
    return normalized


def compute_content_hash(text: str) -> str:
    normalized = normalize_for_hash(text)
    data = normalized.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def split_markdown_table_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def replace_last_table_cell(line: str, value: str) -> str:
    pipe_positions = [idx for idx, ch in enumerate(line) if ch == "|"]
    if len(pipe_positions) < 3:
        return line

    penultimate = pipe_positions[-2]
    last = pipe_positions[-1]
    cell = line[penultimate + 1:last]
    leading_ws_len = len(cell) - len(cell.lstrip(" "))
    trailing_ws_len = len(cell) - len(cell.rstrip(" "))
    leading_ws = cell[:leading_ws_len]
    trailing_ws = cell[len(cell) - trailing_ws_len:] if trailing_ws_len > 0 else ""
    return f"{line[:penultimate + 1]}{leading_ws}{value}{trailing_ws}{line[last:]}"


def get_last_ledger_row_info(full_text: str) -> tuple[int, str, str] | None:
    bounds = get_amendment_section_bounds(full_text)
    if not bounds:
        return None

    start, end = bounds
    lines = full_text.splitlines(keepends=True)
    cursor = 0
    start_line_idx = None
    end_line_idx = None
    for idx, line in enumerate(lines):
        line_start = cursor
        line_end = cursor + len(line)
        if start_line_idx is None and line_end > start:
            start_line_idx = idx
        if end_line_idx is None and line_start >= end:
            end_line_idx = idx
            break
        cursor = line_end

    if start_line_idx is None:
        return None
    if end_line_idx is None:
        end_line_idx = len(lines)

    last_version_idx = None
    stored_hash = ""
    for idx in range(start_line_idx, end_line_idx):
        line = lines[idx]
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cols = split_markdown_table_row(stripped)
        if not cols:
            continue
        first = cols[0]
        if first.lower() == "version" or (first and set(first) <= {"-"}):
            continue
        if VERSION_CELL_RE.match(first):
            while len(cols) < 4:
                cols.append("")
            last_version_idx = idx
            stored_hash = cols[-1].strip()

    if last_version_idx is None:
        return None
    return (last_version_idx, lines[last_version_idx], stored_hash)


def compute_hash_with_last_row_hash_blank(full_text: str) -> tuple[str, str | None]:
    row_info = get_last_ledger_row_info(full_text)
    if not row_info:
        return compute_content_hash(full_text), None

    last_idx, last_line, stored_hash = row_info
    lines = full_text.splitlines(keepends=True)
    lines[last_idx] = replace_last_table_cell(last_line, "")
    reconstructed = "".join(lines)
    return compute_content_hash(reconstructed), stored_hash




def normalize_historical_blank_hashes(full_text: str) -> tuple[str, int]:
    """Replace blank historical ledger SHA cells with known-null '-' marker."""
    bounds = get_amendment_section_bounds(full_text)
    if not bounds:
        return full_text, 0
    row_info = get_last_ledger_row_info(full_text)
    if not row_info:
        return full_text, 0
    last_idx, _, _ = row_info
    lines = full_text.splitlines(keepends=True)
    changed = 0
    for idx, line in enumerate(lines):
        if idx == last_idx:
            continue
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cols = split_markdown_table_row(stripped)
        if not cols or not VERSION_CELL_RE.match(cols[0]):
            continue
        while len(cols) < 4:
            cols.append("")
        if cols[-1].strip() == "":
            lines[idx] = replace_last_table_cell(line, "-")
            changed += 1
    return "".join(lines), changed

def update_last_ledger_hash_cell(
    full_text: str,
    *,
    fix: bool,
    allow_blank_latest: bool = False,
) -> tuple[str, str | None, bool, bool]:
    """
    Returns:
      (updated_text, stored_hash, changed, mismatch)
    """
    row_info = get_last_ledger_row_info(full_text)
    if not row_info:
        return full_text, None, False, False

    computed_hash, stored_hash = compute_hash_with_last_row_hash_blank(full_text)
    if stored_hash is None:
        return full_text, None, False, False
    is_empty = stored_hash == ""
    is_placeholder = stored_hash in PLACEHOLDER_HASHES
    if fix and allow_blank_latest and is_empty:
        return full_text, stored_hash, False, False
    mismatch = (stored_hash not in ("", *PLACEHOLDER_HASHES)) and (stored_hash != computed_hash)

    if not fix:
        return full_text, stored_hash, False, mismatch

    should_write = is_empty or is_placeholder or mismatch
    if not should_write:
        return full_text, stored_hash, False, mismatch

    last_idx, last_line, _ = row_info
    lines = full_text.splitlines(keepends=True)
    lines[last_idx] = replace_last_table_cell(last_line, computed_hash)
    updated_text = "".join(lines)
    return updated_text, stored_hash, updated_text != full_text, mismatch


def classify_latest_sha_status(
    *,
    full_text: str,
    stored_hash: str | None,
    mismatch: bool,
) -> str:
    if has_malformed_ledger_row(full_text):
        return "malformed"
    if stored_hash is None:
        return "missing"
    if stored_hash in PLACEHOLDER_HASHES:
        return "invalid"
    if (stored_hash or "").strip() == "":
        return "unsealed"
    if mismatch:
        return "invalid"
    return "sealed"


def evaluate_hash_state(
    *,
    path: str,
    stored_hash: str | None,
    mismatch: bool,
    strict: bool,
    failures: list[str],
    warnings: list[str],
    stage: str,
) -> None:
    if stored_hash is None:
        return
    if stored_hash in PLACEHOLDER_HASHES:
        failures.append(f"{path}: Last Amendment Ledger hash must be empty or computed SHA-256, not placeholder")
        return
    if (stored_hash or "").strip() == "":
        msg = (
            f"{path}: Latest Amendment Ledger row is unsealed: SHA-256 cell is blank. "
            "This is expected before the ledger bot runs; run with --fix to seal the row."
        )
        if strict:
            if stage == "downstream_block":
                failures.append(
                    "Downstream generated ledger update blocked because source ledger remains unsealed "
                    f"after ledger bot stage: {path}"
                )
            else:
                failures.append(msg)
        else:
            warnings.append(msg)
        return
    if mismatch:
        if strict:
            failures.append(f"{path}: Latest Amendment Ledger hash does not match computed content SHA-256")
        else:
            warnings.append(f"{path}: Existing last-row Amendment Ledger hash does not match computed content hash")


def report_status(
    *,
    path: str,
    ledger_present: bool,
    latest_row_present: bool,
    latest_sha_status: str,
    action_required: str,
    stage: str,
) -> None:
    record = {
        "file": path,
        "ledger_present": "yes" if ledger_present else "no",
        "latest_row_present": "yes" if latest_row_present else "no",
        "latest_sha_status": latest_sha_status,
        "action_required": action_required,
        "stage": stage,
    }
    print(f"LEDGER_STATUS {json.dumps(record, sort_keys=True)}")


def has_malformed_ledger_row(full_text: str) -> bool:
    return len(get_malformed_ledger_rows(full_text)) > 0


def get_malformed_ledger_rows(full_text: str) -> list[tuple[int, str]]:
    bounds = get_amendment_section_bounds(full_text)
    if not bounds:
        return []

    start, end = bounds
    lines = full_text.splitlines(keepends=True)
    cursor = 0
    start_line_idx = None
    end_line_idx = None
    for idx, line in enumerate(lines):
        line_start = cursor
        line_end = cursor + len(line)
        if start_line_idx is None and line_end > start:
            start_line_idx = idx
        if end_line_idx is None and line_start >= end:
            end_line_idx = idx
            break
        cursor = line_end
    if start_line_idx is None:
        return []
    if end_line_idx is None:
        end_line_idx = len(lines)

    malformed: list[tuple[int, str]] = []
    for idx in range(start_line_idx, end_line_idx):
        stripped = lines[idx].strip()
        if not stripped.startswith("|"):
            continue
        cols = split_markdown_table_row(stripped)
        if not cols:
            continue
        first = cols[0]
        if first.lower() == "version" or set(first) <= {"-"}:
            continue
        line_no = idx + 1
        if len(cols) < 4:
            malformed.append((line_no, "Row has fewer than 4 cells."))
            continue
        if not VERSION_CELL_RE.match(first):
            malformed.append((line_no, "First column must be a valid version like 1.0 or 2.3."))
            continue
        if cols[0].strip() == "":
            malformed.append((line_no, "Version cell is blank."))
            continue
        change_summary = cols[1].strip()
        timestamp = cols[2].strip()
        if change_summary == "" or timestamp == "":
            malformed.append((line_no, "Change Summary and Timestamp (UTC) must be non-blank."))
            continue
        if is_formatting_only_description(change_summary) and has_substantive_change_marker(change_summary):
            malformed.append((line_no, "Formatting-only Change Summary must not also claim substantive body/clause changes."))
            continue
    return malformed


def lint_all(*, fix: bool = False, strict: bool = False, stage: str = "pre_fix") -> int:
    failures: list[str] = []
    warnings: list[str] = []
    fixed_files: list[str] = []
    scanned = 0
    summary: dict[str,int] = {}

    for path in list_scoped_markdown_files():
        working_path = REPO_ROOT / path
        working_text = working_path.read_text(encoding="utf-8")
        if not has_amendment_ledger(working_text):
            continue
        scanned += 1

        malformed_rows = get_malformed_ledger_rows(working_text)
        if malformed_rows:
            for line_no, reason in malformed_rows:
                failures.append(
                    f"{path}:{line_no}: Malformed Amendment Ledger row. "
                    "Expected format: | Version | Change Summary | Timestamp (UTC) | Reference Hash |; "
                    "| 2.1 | Meaningful change summary | 2026-05-20T00:00:00Z | <blank or sha256> |. "
                    f"{reason}"
                )
            report_status(
                path=path,
                ledger_present=True,
                latest_row_present=False,
                latest_sha_status="malformed",
                action_required="fix malformed ledger row",
                stage=stage,
            )
            continue

        if fix:
            working_text, normalized_count = normalize_historical_blank_hashes(working_text)
            if normalized_count:
                working_path.write_text(working_text, encoding="utf-8")
                fixed_files.append(path)
        updated_text, stored_hash, changed, mismatch = update_last_ledger_hash_cell(
            working_text,
            fix=fix,
            allow_blank_latest=allows_blank_sha(Path(path).stem),
        )
        if changed:
            working_path.write_text(updated_text, encoding="utf-8")
            fixed_files.append(path)
            recomputed_hash, _ = compute_hash_with_last_row_hash_blank(updated_text)
            stored_hash = recomputed_hash
        evaluate_historical_and_latest_hashes(path, updated_text if changed else working_text, failures, warnings, summary, strict_latest=strict)
        latest_sha_status = classify_latest_sha_status(
            full_text=updated_text if changed else working_text,
            stored_hash=stored_hash,
            mismatch=mismatch,
        )
        action_required = "none"
        if latest_sha_status == "unsealed":
            action_required = "run --fix to seal latest row"
        elif latest_sha_status == "invalid":
            action_required = "repair latest SHA-256 value"
        elif latest_sha_status in {"missing", "malformed"}:
            action_required = "repair amendment ledger row structure"
        report_status(
            path=path,
            ledger_present=True,
            latest_row_present=stored_hash is not None,
            latest_sha_status=latest_sha_status,
            action_required=action_required,
            stage=stage,
        )

        if not fix:
            evaluate_hash_state(
                path=path,
                stored_hash=stored_hash,
                mismatch=mismatch,
                strict=strict,
                failures=failures,
                warnings=warnings,
                stage=stage,
            )

    for warning in warnings:
        print(f"WARNING: {warning}")
    if fixed_files:
        print("Updated files:")
        for path in fixed_files:
            print(f"- {path}")
    print(f"Scanned ledger files: {scanned}")
    for k in ["valid_historical_sha","historical_known_null_shas","invalid_historical_sha","valid_latest_sha","blank_latest_sha_allowed","blank_latest_sha_rejected"]:
        print(f"{k.upper()}={summary.get(k,0)}")

    if failures:
        for failure in failures:
            print(failure)
        return 1

    print("Amendment Ledger lint passed")
    return 0


def parse_semantic_version(version: str) -> tuple[int, int, int] | None:
    if not VERSION_CELL_RE.match(version):
        return None
    parts = [int(part) for part in version.split(".")]
    if len(parts) == 2:
        parts.append(0)
    return (parts[0], parts[1], parts[2])


def version_sort_key(version: str) -> tuple[int, int, int]:
    parsed = parse_semantic_version(version)
    if parsed is None:
        raise ValueError(f"Invalid amendment version: {version}")
    return parsed


def is_minor_only_increment(previous: str, current: str) -> bool:
    prev = parse_semantic_version(previous)
    curr = parse_semantic_version(current)
    if prev is None or curr is None:
        return False
    prev_major_i, prev_minor_i, prev_patch_i = prev
    curr_major_i, curr_minor_i, curr_patch_i = curr
    # Allow either:
    # - patch bump under same minor: 2.4 -> 2.4.1 or 2.4.1 -> 2.4.2
    # - traditional minor bump within same major: 1.7 -> 1.8
    # - major bump with minor reset: 1.7 -> 2.0
    if curr_major_i == prev_major_i and curr_minor_i == prev_minor_i:
        return curr_patch_i == prev_patch_i + 1
    if curr_major_i == prev_major_i:
        return curr_minor_i == prev_minor_i + 1 and curr_patch_i == 0
    if curr_major_i == prev_major_i + 1:
        return curr_minor_i == 0 and curr_patch_i == 0
    return False


def bump_minor_version(version: str) -> str:
    parsed = parse_semantic_version(version)
    if parsed is None:
        raise ValueError(f"Invalid amendment version: {version}")
    major, minor, _patch = parsed
    return f"{major}.{minor + 1}"


def append_amendment_ledger_entry(
    full_text: str,
    *,
    description: str,
    timestamp_utc: str,
) -> tuple[str, bool]:
    row_info = get_last_ledger_row_info(full_text)
    if not row_info:
        return full_text, False

    last_idx, last_line, _ = row_info
    cols = split_markdown_table_row(last_line.strip())
    if not cols or not VERSION_CELL_RE.match(cols[0]):
        return full_text, False

    next_version = bump_minor_version(cols[0])
    lines = full_text.splitlines(keepends=True)
    line_ending = "\n"
    if lines and lines[last_idx].endswith("\r\n"):
        line_ending = "\r\n"

    new_row = f"| {next_version} | {description} | {timestamp_utc} |  |{line_ending}"
    lines.insert(last_idx + 1, new_row)
    return "".join(lines), True


def latest_ledger_row_is_open(full_text: str) -> bool:
    """An open amendment cycle is represented by a blank latest SHA cell."""
    row_info = get_last_ledger_row_info(full_text)
    if not row_info:
        return False
    _, last_line, _ = row_info
    cols = split_markdown_table_row(last_line.strip())
    if not cols:
        return False
    while len(cols) < 4:
        cols.append("")
    return cols[-1].strip() == ""


def latest_ledger_hash_is_blank(full_text: str) -> bool:
    row_info = get_last_ledger_row_info(full_text)
    if not row_info:
        return False
    _idx, _line, stored_hash = row_info
    return stored_hash.strip() == ""


def list_blank_sha_repair_candidate_files() -> list[str]:
    candidates: list[str] = []
    for path in list_scoped_markdown_files():
        doc_id = Path(path).stem
        if allows_blank_sha(doc_id):
            continue
        full_text = (REPO_ROOT / path).read_text(encoding="utf-8")
        if has_amendment_ledger(full_text) and latest_ledger_hash_is_blank(full_text):
            candidates.append(path)
    return candidates


def lint(
    base: str,
    head: str,
    *,
    fix: bool = False,
    staged: bool = False,
    strict: bool = False,
    stage: str = "pre_fix",
) -> int:
    failures: list[str] = []
    warnings: list[str] = []
    fixed_files: list[str] = []
    amended_files: list[str] = []
    summary: dict[str,int] = {}

    changed_paths: list[str] = []
    for path in list_modified_files(base, head, staged=staged):
        before = get_blob(base, path)
        after = get_blob(head, path)
        if normalize_for_whitespace_compare(before) == normalize_for_whitespace_compare(after):
            continue
        if not has_amendment_ledger(after):
            continue
        changed_paths.append(path)

    candidate_paths = list(changed_paths)
    if fix:
        for path in list_blank_sha_repair_candidate_files():
            if path not in candidate_paths:
                candidate_paths.append(path)

    for path in candidate_paths:
        is_changed_path = path in changed_paths
        before = get_blob(base, path) if is_changed_path else ""
        after = get_blob(head, path) if is_changed_path else ""

        working_path = REPO_ROOT / path
        working_text = working_path.read_text(encoding="utf-8")
        malformed_rows = get_malformed_ledger_rows(working_text)
        if malformed_rows:
            for line_no, reason in malformed_rows:
                failures.append(
                    f"{path}:{line_no}: Malformed Amendment Ledger row. "
                    "Expected format: | Version | Change Summary | Timestamp (UTC) | Reference Hash |; "
                    "| 2.1 | Meaningful change summary | 2026-05-20T00:00:00Z | <blank or sha256> |. "
                    f"{reason}"
                )
            report_status(
                path=path,
                ledger_present=True,
                latest_row_present=False,
                latest_sha_status="malformed",
                action_required="fix malformed ledger row",
                stage=stage,
            )
            continue

        before_ledger = extract_amendment_section(before) if is_changed_path else ""
        after_ledger = extract_amendment_section(after) if is_changed_path else ""
        if is_changed_path and before_ledger == after_ledger and fix and not latest_ledger_row_is_open(working_text):
            failures.append(
                f"{path}: Amendment Ledger not updated; add a new row with a meaningful Change Summary."
            )
            report_status(
                path=path,
                ledger_present=True,
                latest_row_present=True,
                latest_sha_status="missing",
                action_required="add a meaningful amendment ledger row manually",
                stage=stage,
            )
            continue

        if fix:
            working_text, normalized_count = normalize_historical_blank_hashes(working_text)
            if normalized_count:
                working_path.write_text(working_text, encoding="utf-8")
                fixed_files.append(path)
                if staged and is_changed_path:
                    run_git(["add", "--", path])

        updated_text, stored_hash, changed, mismatch = update_last_ledger_hash_cell(
            working_text,
            fix=fix,
            allow_blank_latest=allows_blank_sha(Path(path).stem),
        )
        if changed:
            working_path.write_text(updated_text, encoding="utf-8")
            fixed_files.append(path)
            if staged and is_changed_path:
                run_git(["add", "--", path])
            working_text = updated_text
            after = updated_text if is_changed_path else after
            recomputed_hash, _ = compute_hash_with_last_row_hash_blank(updated_text)
            stored_hash = recomputed_hash

        evaluate_historical_and_latest_hashes(path, working_text, failures, warnings, summary, strict_latest=strict)
        if not fix:
            evaluate_hash_state(
                path=path,
                stored_hash=stored_hash,
                mismatch=mismatch,
                strict=strict,
                failures=failures,
                warnings=warnings,
                stage=stage,
            )

        if is_changed_path:
            if before_ledger == after_ledger:
                failures.append(path)
                report_status(
                    path=path,
                    ledger_present=True,
                    latest_row_present=stored_hash is not None,
                    latest_sha_status="missing",
                    action_required="append a new amendment ledger row",
                    stage=stage,
                )
                continue

            before_versions = parse_ledger_versions(before_ledger)
            after_versions = parse_ledger_versions(after_ledger)
            if len(after_versions) >= 2:
                previous_version = after_versions[-2]
                current_version = after_versions[-1]
                if not is_minor_only_increment(previous_version, current_version):
                    failures.append(
                        f"{path}: Amendment version must increment by +0.1, +0.0.1 patch, or by +1.0 with minor reset (x.0)"
                    )
            elif before_versions and after_versions:
                previous_version = before_versions[-1]
                current_version = after_versions[-1]
                if previous_version != current_version and not is_minor_only_increment(previous_version, current_version):
                    failures.append(
                        f"{path}: Amendment version must increment by +0.1, +0.0.1 patch, or by +1.0 with minor reset (x.0)"
                    )

        latest_sha_status = classify_latest_sha_status(
            full_text=working_text,
            stored_hash=stored_hash,
            mismatch=mismatch,
        )
        action_required = "none"
        if latest_sha_status == "unsealed":
            action_required = "run --fix to seal latest row"
        elif latest_sha_status == "invalid":
            action_required = "repair latest SHA-256 value"
        elif latest_sha_status in {"missing", "malformed"}:
            action_required = "append/fix amendment ledger row" if is_changed_path else "repair amendment ledger row structure"
        report_status(
            path=path,
            ledger_present=True,
            latest_row_present=stored_hash is not None,
            latest_sha_status=latest_sha_status,
            action_required=action_required,
            stage=stage,
        )

    if failures:
        for failure in failures:
            if ": " in failure:
                print(failure)
            else:
                print(f"{failure}: Amendment Ledger not updated")
        for warning in warnings:
            print(f"WARNING: {warning}")
        if fixed_files:
            print("Updated files:")
            for path in sorted(set(fixed_files)):
                print(f"- {path}")
        return 1

    for warning in warnings:
        print(f"WARNING: {warning}")
    if fixed_files:
        print("Updated files:")
        for path in sorted(set(fixed_files)):
            print(f"- {path}")
    if amended_files:
        print("Added amendment ledger rows:")
        for path in amended_files:
            print(f"- {path}")
    print("Amendment Ledger lint passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Ensure modified governance docs update Amendment Ledger. Historical rows require valid SHA/placeholder; latest blank SHA is allowed by default.")
    parser.add_argument("--base", default="HEAD~1")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--fix", action="store_true", help="Populate/fix last Amendment Ledger SHA-256 hash in modified files")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat blank/placeholder latest Amendment Ledger SHA as hard failures (strict latest finalisation mode).",
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Process staged changes (index) against HEAD; useful for pre-commit hooks",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process all scoped governance markdown files instead of just git-modified files",
    )
    parser.add_argument(
        "--stage",
        default="pre_fix",
        choices=sorted(VALIDATION_STAGES),
        help="Label status output for lifecycle phase reporting.",
    )
    args = parser.parse_args()
    if args.all:
        return lint_all(fix=args.fix, strict=args.strict, stage=args.stage)
    base = args.base
    head = args.head
    if args.staged:
        base = "HEAD"
        head = ":"
    return lint(base, head, fix=args.fix, staged=args.staged, strict=args.strict, stage=args.stage)


if __name__ == "__main__":
    sys.exit(main())
