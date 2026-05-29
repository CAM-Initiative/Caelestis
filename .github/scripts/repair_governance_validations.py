#!/usr/bin/env python3
"""Deterministic, agent-safe governance validation repair loop.

Repairs only:
- short document refs when exactly one full CAM filename candidate exists;
- missing sections when exactly one strong heading match exists;
- malformed amendment-ledger rows with deterministic normalization.
"""
from __future__ import annotations

import argparse
import csv
import pathlib
import re
import subprocess
import sys
from typing import NamedTuple

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
SECTION_VALIDATOR = [sys.executable, ".github/scripts/validate_markdown_section_refs.py", "--root", "Governance", "--report-file", "validation-reports/section-reference-report.tsv"]
LEDGER_VALIDATOR = [sys.executable, ".github/scripts/lint_amendment_ledger.py", "--all", "--strict"]

HEADER_RE = re.compile(r"^(#+)\s+(.*)$")
SECTION_RE = re.compile(r"^(\d+(?:\.\d+)*)\b")
DOC_ID_RE = re.compile(r"\b(CAM-[A-Z0-9]+(?:-[A-Z0-9]+)+)\b")
SHORT_REF_RE = re.compile(r"\b(RELATION-\d{3}|AEON-\d{3}|Annex\s+[A-Z]|Appendix\s+[A-Z]|Schedule\s+\d+)\s*§(\d+(?:\.\d+)*)\b", re.IGNORECASE)
LEDGER_FAILURE_RE = re.compile(r"^(Governance/.+\.md):(\d+): Malformed Amendment Ledger row\..*")

class Unresolved(NamedTuple):
    kind: str
    file_path: str
    line_number: int
    detail: str


def run_cmd(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, cwd=REPO_ROOT, text=True, capture_output=True)
    return proc.returncode, proc.stdout + proc.stderr


def load_doc_index(root: pathlib.Path) -> dict[str, pathlib.Path]:
    out = {}
    for p in root.glob("**/*.md"):
        if p.stem.startswith("CAM-"):
            out[p.stem] = p
    return out


def section_map(path: pathlib.Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        m = HEADER_RE.match(line.strip())
        if not m:
            continue
        n = SECTION_RE.match(m.group(2).strip())
        if n:
            out[n.group(1)] = m.group(2).strip()
    return out


def strong_section_match(target: str, sections: dict[str, str]) -> str | None:
    if target in sections:
        return target
    near = [k for k in sections if k.split(".")[0] == target.split(".")[0]]
    return near[0] if len(near) == 1 else None


def fix_short_ref(line: str, doc_index: dict[str, pathlib.Path]) -> tuple[str, bool, str]:
    m = SHORT_REF_RE.search(line)
    if not m:
        return line, False, "no_short_ref"
    label, sec = m.group(1), m.group(2)
    token = label.upper().replace(" ", "-")
    candidates = [k for k in doc_index if token in k]
    if len(candidates) != 1:
        return line, False, f"TODO ambiguous short ref '{label} §{sec}'"
    fixed = line.replace(m.group(0), f"{candidates[0]}, §{sec}")
    return fixed, True, ""


def fix_row(row: str) -> tuple[str, bool]:
    cols = [c.strip() for c in row.strip().strip("|").split("|")]
    if len(cols) < 4:
        cols += [""] * (4 - len(cols))
    v, summary, ts, h = cols[0], cols[1], cols[2], cols[3]
    if not re.match(r"^\d+\.\d+(?:\.\d+)?$", v):
        return row, False
    if not summary or not ts:
        return row, False
    return f"| {v} | {summary} | {ts} | {h} |\n", True


def apply_repairs(section_report: pathlib.Path, ledger_output: str) -> list[Unresolved]:
    unresolved: list[Unresolved] = []
    doc_index = load_doc_index(REPO_ROOT / "Governance")

    if section_report.exists():
        rows = list(csv.DictReader(section_report.open(encoding="utf-8"), delimiter="\t"))
        for r in rows:
            status = r["status"]
            if status not in {"fail_short_document_reference", "fail_cross_document_section_missing"}:
                continue
            fp = REPO_ROOT / r["file path"]
            ln = int(r["line number"])
            lines = fp.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
            old = lines[ln - 1]
            if status == "fail_short_document_reference":
                new, changed, todo = fix_short_ref(old, doc_index)
                if changed:
                    lines[ln - 1] = new if new.endswith("\n") else new + "\n"
                    fp.write_text("".join(lines), encoding="utf-8")
                else:
                    unresolved.append(Unresolved("ambiguous_ref", r["file path"], ln, todo))
            elif status == "fail_cross_document_section_missing":
                target = r["target document"]
                if target in doc_index:
                    smap = section_map(doc_index[target])
                    match = strong_section_match(r["reference found"].lstrip("§"), smap)
                    if match and match != r["reference found"].lstrip("§"):
                        lines[ln - 1] = old.replace(r["reference found"], f"§{match}")
                        fp.write_text("".join(lines), encoding="utf-8")
                    else:
                        unresolved.append(Unresolved("missing_section", r["file path"], ln, "TODO no unique strong section match"))

    for m in LEDGER_FAILURE_RE.finditer(ledger_output):
        rel, line = m.group(1), int(m.group(2))
        fp = REPO_ROOT / rel
        lines = fp.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
        new, changed = fix_row(lines[line - 1])
        if changed:
            lines[line - 1] = new
            fp.write_text("".join(lines), encoding="utf-8")
        else:
            unresolved.append(Unresolved("ledger_row", rel, line, "TODO deterministic repair unavailable"))

    return unresolved


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-attempts", type=int, default=3)
    parser.add_argument("--unresolved-report", default="validation-reports/unresolved-repairs.md")
    args = parser.parse_args()

    unresolved: list[Unresolved] = []
    for _ in range(args.max_attempts):
        rc1, out1 = run_cmd(SECTION_VALIDATOR)
        rc2, out2 = run_cmd(LEDGER_VALIDATOR)
        if rc1 == 0 and rc2 == 0:
            break
        unresolved = apply_repairs(REPO_ROOT / "validation-reports/section-reference-report.tsv", out2)
    else:
        pass

    rc1, out1 = run_cmd(SECTION_VALIDATOR)
    rc2, out2 = run_cmd(LEDGER_VALIDATOR)
    if rc1 == 0 and rc2 == 0:
        return 0

    out = pathlib.Path(args.unresolved_report)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        f.write("| Kind | File | Line | Detail |\n|---|---|---:|---|\n")
        for u in unresolved:
            f.write(f"| {u.kind} | `{u.file_path}` | {u.line_number} | {u.detail} |\n")
    print(out1)
    print(out2)
    print(f"Unresolved report written: {out}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
