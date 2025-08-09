#!/usr/bin/env python3
"""
Rebuilds Governance/SOPs/CAM-SOP-Index.md
- Scans Governance/SOPs/*.md (excluding the index file)
- Extracts: ID, Title, 1–2 sentence summary (from Purpose section)
- Auto-sorts by SOP number
- Writes index with relative links, preserving manual header block
"""

from __future__ import annotations
import re
from pathlib import Path

# ---- config ----
REPO_ROOT = Path(__file__).resolve().parents[1]
SOP_DIR = REPO_ROOT / "Governance" / "SOPs"
INDEX_PATH = SOP_DIR / "CAM-SOP-Index.md"

HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"

# Regex for SOP files like CAM-LG2025-SOP-001.md
ID_RE = re.compile(r"^(CAM-[A-Z0-9]+-SOP-(\d+))[A-Z]?$", re.IGNORECASE)

def extract_summary(text: str) -> str:
    """
    Gets the first paragraph under a 'Purpose' section, or first non-header paragraph.
    """
    section_pattern = re.compile(
        r"^##\s*(?:[IVXLC]+\.\s*)?Purpose\s*$([\s\S]+?)(?:^##|\Z)", re.MULTILINE | re.IGNORECASE
    )
    m = section_pattern.search(text)
    if m:
        section = m.group(1)
        paras = [p.strip() for p in re.split(r"\n\s*\n", section) if p.strip()]
        if paras:
            return " ".join(paras[0].split())
    # Fallback: first non-header paragraph
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    for para in paragraphs:
        if (para.count(":") > 2 or para.startswith("**")):
            continue
        return " ".join(para.split())
    return paragraphs[0] if paragraphs else ""

def parse_file(md_path: Path) -> dict | None:
    name = md_path.name
    if name == INDEX_PATH.name or not name.lower().endswith(".md"):
        return None
    stem = md_path.stem
    m = ID_RE.match(stem)
    if not m:
        return None
    id_full = m.group(1)
    num = int(m.group(2))
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    # Title: first H1, else fallback to "Title:" line, else derive from filename
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
        "num": num,
        "title": title,
        "summary": summary,
        "filename": md_path.name,
    }

def collect_sops() -> list[dict]:
    items: list[dict] = []
    if not SOP_DIR.exists():
        return items
    for p in sorted(SOP_DIR.glob("*.md")):
        rec = parse_file(p)
        if rec:
            items.append(rec)
    return items

def render_index(items: list[dict]) -> str:
    out = []
    out.append("## Standard Operating Procedures\n")
    for r in sorted(items, key=lambda r: r["num"]):
        link_text = f"{r['id']} - {r['title']}"
        out.append(f"- [{link_text}]({r['filename']})  ")
        if r["summary"]:
            out.append(f"  _{r['summary']}_")
        out.append("")
    out.append("")
    return "\n".join(out)

def main():
    items = collect_sops()
    generated_md = render_index(items)
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
