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

REPO_ROOT = Path(__file__).resolve().parents[2]

SCOPED_PREFIXES = (
    "Governance/Constitution/",
    "Governance/Charters/",
)

AMENDMENT_HEADING_RE = re.compile(r"^##+\s+.*amendment\s+ledger", re.IGNORECASE | re.MULTILINE)
NEXT_HEADING_RE = re.compile(r"^##+\s+", re.MULTILINE)
VERSION_CELL_RE = re.compile(r"^\d+\.\d+$")
PLACEHOLDER_HASHES = {"-", "—"}
VALIDATION_STAGES = {"pre_fix", "fix", "post_fix", "downstream_block"}

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
        if first.lower() == "version" or set(first) <= {"-"}:
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


def update_last_ledger_hash_cell(
    full_text: str,
    *,
    fix: bool,
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
    bounds = get_amendment_section_bounds(full_text)
    if not bounds:
        return False

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
        return False
    if end_line_idx is None:
        end_line_idx = len(lines)

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
        if VERSION_CELL_RE.match(first) and len(cols) < 4:
            return True
    return False


def lint_all(*, fix: bool = False, strict: bool = False, stage: str = "pre_fix") -> int:
    failures: list[str] = []
    warnings: list[str] = []
    fixed_files: list[str] = []
    scanned = 0

    for path in list_scoped_markdown_files():
        working_path = REPO_ROOT / path
        working_text = working_path.read_text(encoding="utf-8")
        if not has_amendment_ledger(working_text):
            continue
        scanned += 1

        if has_malformed_ledger_row(working_text):
            failures.append(f"{path}: Malformed Amendment Ledger row (expected at least 4 table columns)")
            report_status(
                path=path,
                ledger_present=True,
                latest_row_present=False,
                latest_sha_status="malformed",
                action_required="fix malformed ledger row",
                stage=stage,
            )
            continue

        updated_text, stored_hash, changed, mismatch = update_last_ledger_hash_cell(
            working_text,
            fix=fix,
        )
        if changed:
            working_path.write_text(updated_text, encoding="utf-8")
            fixed_files.append(path)
            recomputed_hash, _ = compute_hash_with_last_row_hash_blank(updated_text)
            stored_hash = recomputed_hash
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

    if failures:
        for failure in failures:
            print(failure)
        return 1

    print("Amendment Ledger lint passed")
    return 0


def is_minor_only_increment(previous: str, current: str) -> bool:
    prev_major, prev_minor = previous.split(".")
    curr_major, curr_minor = current.split(".")
    prev_major_i, prev_minor_i = int(prev_major), int(prev_minor)
    curr_major_i, curr_minor_i = int(curr_major), int(curr_minor)
    # Allow either:
    # - traditional minor bump within same major: 1.7 -> 1.8
    # - major bump with minor reset: 1.7 -> 2.0
    if curr_major_i == prev_major_i:
        return curr_minor_i == prev_minor_i + 1
    if curr_major_i == prev_major_i + 1:
        return curr_minor_i == 0
    return False


def bump_minor_version(version: str) -> str:
    major, minor = version.split(".")
    return f"{major}.{int(minor) + 1}"


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
    auto_description = "Automated amendment ledger entry via lint_amendment_ledger.py"
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    for path in list_modified_files(base, head, staged=staged):
        before = get_blob(base, path)
        after = get_blob(head, path)

        if normalize_for_whitespace_compare(before) == normalize_for_whitespace_compare(after):
            continue

        if not has_amendment_ledger(after):
            continue

        working_path = REPO_ROOT / path
        working_text = working_path.read_text(encoding="utf-8")
        if has_malformed_ledger_row(working_text):
            failures.append(f"{path}: Malformed Amendment Ledger row (expected at least 4 table columns)")
            report_status(
                path=path,
                ledger_present=True,
                latest_row_present=False,
                latest_sha_status="malformed",
                action_required="fix malformed ledger row",
                stage=stage,
            )
            continue

        before_ledger = extract_amendment_section(before)
        after_ledger = extract_amendment_section(after)
        if before_ledger == after_ledger and fix:
            working_text, added = append_amendment_ledger_entry(
                working_text,
                description=auto_description,
                timestamp_utc=now_utc,
            )
            if added:
                amended_files.append(path)
                working_path.write_text(working_text, encoding="utf-8")
                after = working_text
                after_ledger = extract_amendment_section(after)

        updated_text, stored_hash, changed, mismatch = update_last_ledger_hash_cell(
            working_text,
            fix=fix,
        )
        if changed:
            working_path.write_text(updated_text, encoding="utf-8")
            fixed_files.append(path)
            if staged:
                run_git(["add", "--", path])
            working_text = updated_text
            after = updated_text
            recomputed_hash, _ = compute_hash_with_last_row_hash_blank(updated_text)
            stored_hash = recomputed_hash
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
                failures.append(f"{path}: Amendment version must increment by +0.1 or by +1.0 with minor reset (x.0)")
        elif before_versions and after_versions:
            previous_version = before_versions[-1]
            current_version = after_versions[-1]
            if previous_version != current_version and not is_minor_only_increment(previous_version, current_version):
                failures.append(f"{path}: Amendment version must increment by +0.1 or by +1.0 with minor reset (x.0)")

        latest_sha_status = classify_latest_sha_status(
            full_text=after if after else working_text,
            stored_hash=stored_hash,
            mismatch=mismatch,
        )
        action_required = "none"
        if latest_sha_status == "unsealed":
            action_required = "run --fix to seal latest row"
        elif latest_sha_status == "invalid":
            action_required = "repair latest SHA-256 value"
        elif latest_sha_status in {"missing", "malformed"}:
            action_required = "append/fix amendment ledger row"
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
            for path in fixed_files:
                print(f"- {path}")
        return 1

    for warning in warnings:
        print(f"WARNING: {warning}")
    if fixed_files:
        print("Updated files:")
        for path in fixed_files:
            print(f"- {path}")
    if amended_files:
        print("Added amendment ledger rows:")
        for path in amended_files:
            print(f"- {path}")
    print("Amendment Ledger lint passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Ensure modified governance docs update Amendment Ledger")
    parser.add_argument("--base", default="HEAD~1")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--fix", action="store_true", help="Populate/fix last Amendment Ledger SHA-256 hash in modified files")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat empty/mismatched latest Amendment Ledger SHA-256 as hard failures (post-fixer validation mode).",
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
