#!/usr/bin/env python3
"""
Rebuilds Governance/Laws/CAM-Laws-Index.md
- Scans Governance/Laws/*.md (excluding the index file)
- Extracts: ID, Title, 1–2 sentence summary
- Groups by type (LAW, ACT, STATUTE, etc.)
- Auto-sorts by number
- Writes index with relative links, preserving manual header block
"""

from __future__ import annotations
import re
import os
from pathlib import Path

# ---- config ----
REPO_ROOT = Path(__file__).resolve().parents[1]
LAWS_DIR = REPO_ROOT / "Governance" / "Laws"
INDEX_PATH = LAWS_DIR / "CAM-Laws-Index.md"

HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"

# Flexible regex for law file names
ID_RE = re.compile(
    r"^(CAM-(?:[A-Z0-9]+-)*)([A-Z]+(?:-[A-Z0-9]+)*?)-(\d+)([A-Z]?)$", re.IGNORECASE
)

def extract_summary(text: str) -> str:
    """
    Extracts a meaningful summary from the markdown text.
    - Prioritizes sections titled Purpose (including 'I. Purpose', etc.)
    - Otherwise, skips metadata and grabs the first proper paragraph.
    """
    section_pattern = re.compile(
        r"^##\s*(?:[IVXLC]+\.\s*)?Purpose\s*$([\s\S]+?)(?:^##|\Z)", re.MULTILINE | re.IGNORECASE
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
    name = md_path.name
    if name == INDEX_PATH.name:
        return None
    if not name.lower().endswith(".md"):
        return None

    stem = md_path.stem
    m = ID_RE.match(stem)
    if not m:
        # fallback: treat everything as type 'OTHER' and try to parse a number
        type_token = 'OTHER'
        num_match = re.search(r'(\d+)[A-Z]?$', stem)
        num = int(num_match.group(1)) if num_match else 0
        id_full = stem
    else:
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
        "type": type_token,
        "num": num,
        "title": title,
        "summary": summary,
        "filename": md_path.name,
    }

def collect_laws() -> list[dict]:
    items: list[dict] = []
    if not LAWS_DIR.exists():
        return items
    for p in sorted(LAWS_DIR.glob("*.md")):
        rec = parse_file(p)
        if rec:
            items.append(rec)
    return items

def group_and_sort(items: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {}
    for rec in items:
        g = rec["type"]
        groups.setdefault(g, []).append(rec)

    for g in groups:
        groups[g].sort(key=lambda r: (r["num"], r["id"]))

    return groups

def render_index(groups: dict[str, list[dict]]) -> str:
    out = []
    for section, items in groups.items():
        heading = {
            "LAW": "Laws",
            "STATUTE": "Statutes",
            "ACT": "Acts",
        }.get(section, section)
        out.append(f"## {heading}")
        out.append("")
        for r in items:
            link_text = f"{r['id']} - {r['title']}"
            out.append(f"- [{link_text}]({r['filename']})  ")
            if r["summary"]:
                out.append(f"  _{r['summary']}_")
            out.append("")
    out.append("")
    return "\n".join(out)

def main():
    items = collect_laws()
    groups = group_and_sort(items)
    generated_md = render_index(groups)

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

if __name__ == "__main__":
    main()
