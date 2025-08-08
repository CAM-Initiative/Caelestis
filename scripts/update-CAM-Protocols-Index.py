#!/usr/bin/env python3
"""
Rebuilds Governance/Protocols/CAM-Protocols-Index.md
- Scans Governance/Protocols/*.md (excluding the index file)
- Extracts: ID, Title, 1–2 sentence summary
- Groups by type (AEON, PROT, SOP, ALIGN/ALIGNMENT, etc.)
- Auto-sorts by ID
- Inserts ⚠️ Solan Protocol placeholder if file missing
- Writes index with relative links, preserving manual header block
"""

from __future__ import annotations
import re
import os
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
# ^ captures:
#   group 1: prefix like "CAM-LG2025-PROT-"
#   group 2: the type token (AEON/PROT/SOP/ALIGN/ALIGNMENT)
#   group 3: the numeric suffix like "012"

HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"

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

    # Title: first H1 line, or fallback to a "Title:" line, else derive from filename
    title = None
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            title = line[2:].strip()
            break
    if not title:
        m2 = re.search(r"^Title:\s*(.+)$", text, flags=re.MULTILINE | re.IGNORECASE)
        title = m2.group(1).strip() if m2 else stem.replace("-", " ")

    # Summary: first paragraph after the H1 (or the first non-empty paragraph)
    summary = ""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if paragraphs:
        # If the first para is a H1 line, look to the next
        if paragraphs[0].lstrip().startswith("# "):
            summary = paragraphs[1] if len(paragraphs) > 1 else ""
        else:
            summary = paragraphs[0]

    # trim summary to something tidy (not hard limit; just neat)
    summary = " ".join(summary.split())
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
    # Insert placeholder
    items.append({
        "id": SOLAN_ID,
        "type": "PROT",
        "num": 4,  # from ...-004
        "title": SOLAN_PLACEHOLDER_NAME,
        "summary": SOLAN_PLACEHOLDER_SUMMARY,
        "filename": f"{SOLAN_ID}.md",  # link still points to expected path
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
            # If it's the Solan placeholder, the title already includes ⚠️
            link_text = f"{r['id']} - {r['title']}"
            out.append(f"- [{link_text}]({r['filename']})  ")
            if r["summary"]:
                out.append(f"  _{r['summary']}_")
            out.append("")  # blank line between entries

    out.append("")
    return "\n".join(out)

def main():
    items = collect_protocols()
    items = ensure_solan_placeholder(items)
    groups = group_and_sort(items)
    generated_md = render_index(groups)

    # Read existing file to preserve header block
    old = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.exists() else ""
    if old and HEADER_MARKER in old:
        header, _ = old.split(HEADER_MARKER, 1)
        new_md = header.rstrip() + "\n" + HEADER_MARKER + "\n\n" + generated_md
    else:
        # If marker not found, just write everything
        # You may want to add the header block here if desired
        # For now, just write the generated index
        new_md = generated_md

    # Write only if changed
    if new_md.strip() != old.strip():
        INDEX_PATH.write_text(new_md, encoding="utf-8")
        print(f"Updated: {INDEX_PATH}")
    else:
        print("No changes needed.")

if __name__ == "__main__":
    main()
