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

HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"

def extract_summary(text: str) -> str:
    """
    Extracts a meaningful summary from the markdown text.
    - Prioritizes sections titled Purpose (including 'I. Purpose', etc.)
    - Otherwise, skips metadata and grabs the first proper paragraph.
    """
    section_pattern = re.compile(
        r"^##\s*(?:[IVXLC]+\.\s*)?Purpose\s*$([\s\S]+?)(?:^##|\Z)",
        re.MULTILINE | re.IGNORECASE
    )
    m = section_pattern.search(text)
    if m:
        section = m.group(1)
        paras = [p.strip() for p in re.split(r"\n\s*\n", section) if p.strip()]
        if paras:
            summary = paras[0]
            return " ".join(summary.split())
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    for para in paragraphs:
        if (para.count(":") > 2 or para.startswith("**")):
            continue
        return " ".join(para.split())
    return paragraphs[0] if paragraphs else ""

def parse_file(md_path: Path) -> dict | None:
    """Extract ID, type, title, summary from a protocol markdown file."""
    name = md_path.name
    if name == INDEX_PATH.name:
        return None
    if not name.lower().endswith(".md"):
        return None
    stem = md_path.stem  # filename without .md
    m = ID_RE.match(stem)
    if not m:
        # File doesn't match expected ID pattern — skip cleanly
        return None
    id_full = stem
    type_token = m.group(2).upper()
    num = int(m.group(3))
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    title = None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            title = line[2:].strip()
            break
    if not title:
        m2 = re.search(r"^Title:\s*(.+)$", text, flags=re.MULTILINE | re.IGNORECASE)
        title = m2.group(1).strip() if m2 else stem.replace("-", " ")
    summary = extract_summary(text)
    if len(summary) > 360:
        summary = summary[:357].rstrip() + "..."
    return {
        "id": id_full,
        "type": "ALIGN" if type_token == "ALIGNMENT" else type_token,
        "num": num,
        "title": title,
        "summary": summary,
        "filename": md_path.name,  # relative link target from index file
    }

def collect_protocols() -> list[dict]:
    items: list[dict] = []
    if not PROT_DIR.exists():
        return items
    for p in sorted(PROT_DIR.glob("*.md")):
        rec = parse_file(p)
        if rec:
            items.append(rec)
    return items

def ensure_solan_placeholder(items: list[dict]) -> list[dict]:
    """If Solan file doesn't exist, insert a placeholder entry (marked with ⚠️)."""
    has_solan = any(r["id"] == SOLAN_ID for r in items)
    if has_solan:
        return items
    items.append({
        "id": SOLAN_ID,
        "type": "PROT",
        "num": 4,  # from ...-004
        "title": SOLAN_PLACEHOLDER_NAME,
        "summary": SOLAN_PLACEHOLDER_SUMMARY,
        "filename": f"{SOLAN_ID}.md",
    })
    return items

def group_and_sort(items: list[dict]) -> dict[str, list[dict]]:
    # group by type
    groups: dict[str, list[dict]] = {}
    for rec in items:
        g = rec["type"] if rec["type"] in GROUP_ORDER else "OTHER"
        groups.setdefault(g, []).append(rec)
    # sort each group by numeric suffix (id number), then by id as tie-breaker
    for g in groups:
        groups[g].sort(key=lambda r: (r["num"], r["id"]))
    return groups

def infer_seal(filename: str) -> str:
    """
    Infer the seal designation based on filename.
    Documents containing -RED indicate Red seal, -BLACK indicate Black seal,
    otherwise default to Gold.
    """
    fname = filename.upper()
    if "-RED" in fname:
        return "Red"
    if "-BLACK" in fname:
        return "Black"
    return "Gold"

def get_git_info(md_path: Path) -> tuple[str, str]:
    """
    Returns the last commit SHA and ISO timestamp for the given file.
    If git is unavailable or an error occurs, empty strings are returned.
    """
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
    """
    Renders a machine-friendly library table for automated parsing.
    Excludes long prose; includes id, title, type, seal, relative path, pinned_sha and date.
    """
    rows = []
    for rec in items:
        md_path = PROT_DIR / rec["filename"]
        sha, date = get_git_info(md_path)
        seal = infer_seal(rec["filename"])
        # Relative path from repo root
        rel_path = os.path.relpath(md_path, REPO_ROOT)
        rows.append({
            "id": rec["id"],
            "title": rec["title"],
            "type": rec["type"],
            "seal": seal,
            "path": rel_path.replace(os.sep, "/"),
            "sha": sha,
            "date": date,
        })
    # sort rows by id for deterministic order
    rows.sort(key=lambda r: r["id"])
    out: list[str] = []
    out.append("### Library")
    out.append("")
    out.append("| id | title | type | seal | path | pinned_sha | updated_at |")
    out.append("|---|---|---|---|---|---|---|")
    for row in rows:
        out.append(
            f"| {row['id']} | {row['title']} | {row['type']} | {row['seal']} | {row['path']} | {row['sha']} | {row['date']} |"
        )
    out.append("")
    return "\n".join(out)

def render_index(groups: dict[str, list[dict]]) -> str:
    # Title + note, omitted here because preserved from header block
    out = []
    # stable section order
    for section in GROUP_ORDER:
        items = groups.get(section, [])
        if not items:
            continue
        heading = {
            "AEON": "AEON Tier Protocols",
            "PROT": "Protocol Tier",
            "SOP": "Standard Operating Procedures",
            "ALIGN": "Alignment Documents",
            "ALIGNMENT": "Alignment Documents",
            "OTHER": "Other",
        }.get(section, section)
        out.append(f"## {heading}")
        out.append("")
        for r in items:
            link_text = f"{r['id']} - {r['title']}"
            out.append(f"- [{link_text}]({r['filename']})  ")
            if r["summary"]:
                out.append(f"  _{r['summary']}_")
            out.append("")  # blank line between entries
    out.append("")
    return "\n".join(out)

def main() -> None:
    items = collect_protocols()
    items = ensure_solan_placeholder(items)
    groups = group_and_sort(items)
    # Build index list (bulleted with summaries)
    generated_md = render_index(groups)
    # Append the library table after the list for machine-readable access
    generated_md = generated_md + render_library(items)
    # Read existing file to preserve header block
    old = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.exists() else ""
    if old and HEADER_MARKER in old:
        header, _ = old.split(HEADER_MARKER, 1)
        new_md = header.rstrip() + "\n" + HEADER_MARKER + "\n\n" + generated_md
    else:
        # If marker not found, just write everything
        new_md = generated_md
    # Write only if changed
    if new_md.strip() != old.strip():
        INDEX_PATH.write_text(new_md, encoding="utf-8")
        print(f"Updated: {INDEX_PATH}")
    else:
        print("No changes needed.")

if __name__ == "__main__":
    main()