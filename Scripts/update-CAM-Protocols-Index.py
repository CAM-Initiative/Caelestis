#!/usr/bin/env python3

"""
Rebuilds Governance/Protocols/CAM-Protocols-Index.md
- Scans Governance/Protocols/*.md (excluding the index file)
- Extracts: ID, Title, 1–2 sentence summary
- Groups by type (AEON, PROT, SOP, ALIGN/ALIGNMENT, etc.)
- Auto-sorts by ID
- Inserts ⚠️ Solan Protocol placeholder if file missing
- Writes index with relative links, preserving manual header block

This version also appends a **Library** table at the end of the generated index.
The library table contains only short fields (id, title, type, seal, relative path,
pinned git commit and timestamp) to support automated parsing without
including long prose. Long summaries remain outside of the table.
"""

from __future__ import annotations
import re
import os
import subprocess
from pathlib import Path
from textwrap import dedent

# ---- config ----
REPO_ROOT = Path(__file__).resolve().parents[1]  # adjust if you put script elsewhere
PROT_DIR = REPO_ROOT / "Governance" / "Protocols"
INDEX_PATH = PROT_DIR / "CAM-Protocols-Index.md"

SOLAN_ID = "CAM-LG2025-PROT-004"
SOLAN_FILE = PROT_DIR / f"{SOLAN_ID}.md"
SOLAN_PLACEHOLDER_NAME = "⚠️ Solan Protocol"
SOLAN_PLACEHOLDER_SUMMARY = (
    "Details pending formal drafting; placeholder entry maintains continuity for dependent references."
)

# order the groups the way humans expect to read them
GROUP_ORDER = ["AEON", "PROT", "SOP", "ALIGN", "ALIGNMENT", "OTHER"]

ID_RE = re.compile(
    r"^(CAM-[A-Za-z0-9]+-(AEON|PROT|SOP|ALIGN(?:MENT)?)\-?)(\d+)(?:[A-Z])?$"
)

# ... existing imports and configuration ...

HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"

def infer_seal(filename: str) -> str:
    # Infer Gold/Red/Black based on filename
    fname = filename.upper()
    if "-RED" in fname:
        return "Red"
    if "-BLACK" in fname:
        return "Black"
    return "Gold"

def get_git_info(md_path: Path) -> tuple[str, str]:
    # Return last commit SHA and ISO timestamp
    try:
        result = subprocess.check_output(
            ["git", "log", "-n", "1", "--format=%H|%aI", "--", str(md_path)],
            cwd=REPO_ROOT,
            text=True,
        ).strip()
        sha, iso_date = result.split("|")
        return sha, iso_date
    except Exception:
        return "", ""

def render_library(items: list[dict]) -> str:
    # Build machine‑readable table
    rows = []
    for rec in items:
        md_path = PROT_DIR / rec["filename"]
        sha, date = get_git_info(md_path)
        seal = infer_seal(rec["filename"])
        rel_path = os.path.relpath(md_path, REPO_ROOT).replace(os.sep, "/")
        rows.append({
            "id": rec["id"],
            "title": rec["title"],
            "type": rec["type"],
            "seal": seal,
            "path": rel_path,
            "sha": sha,
            "date": date,
        })
    rows.sort(key=lambda r: r["id"])
    out = []
    out.append("### Library")
    out.append("")
    out.append("| id | title | type | seal | path | pinned_sha | updated_at |")
    out.append("|---|---|---|---|---|---|---|")
    for row in rows:
        # Escape pipes in title just in case
        safe_title = row['title'].replace("|", "\\|")
        out.append(
            f"| {row['id']} | {safe_title} | {row['type']} | {row['seal']} | "
            f"{row['path']} | {row['sha']} | {row['date']} |"
        )
    out.append("")
    return "\n".join(out)

def main() -> None:
    items = collect_protocols()
    items = ensure_solan_placeholder(items)
    groups = group_and_sort(items)
    generated_md = render_index(groups)
    # Append library table
    generated_md = generated_md.strip() + "\n\n" + render_library(items)
    # Preserve header block above the marker
    old = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.exists() else ""
    if old and HEADER_MARKER in old:
        header, _ = old.split(HEADER_MARKER, 1)
        new_md = header.rstrip() + "\n" + HEADER_MARKER + "\n\n" + generated_md
    else:
        new_md = generated_md
    if new_md.strip() != old.strip():
        INDEX_PATH.write_text(new_md, encoding="utf-8")
        print(f"Updated: {INDEX_PATH}")
    else:
        print("No changes needed.")
