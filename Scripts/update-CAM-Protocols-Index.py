#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path
import os
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
PROT_DIR = REPO_ROOT / "Governance" / "Protocols"
INDEX_PATH = PROT_DIR / "CAM-Protocols-Index.md"
HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"

# Strict filename pattern:
# CAM-CYCLE-TYPE-NNN[-SEAL].md
# e.g. CAM-BS2025-PROT-001-PLATINUM.md
FNAME_RE = re.compile(
    r"^CAM-([A-Z]{2}\d{4})-([A-Z]+)-(\d{3})(?:-([A-Z]+))?\.md$", re.IGNORECASE
)

def infer_seal_from_token(token: str | None, filename: str) -> str:
    if token:
        t = token.upper()
        if "PLAT" in t:
            return "Platinum"
        if "RED" in t:
            return "Red"
        if "BLACK" in t:
            return "Black"
        # unknown explicit token -> return token-cased
        return token.capitalize()
    # fallback: inspect filename for common markers
    fname = filename.upper()
    if "-PLAT" in fname or "PLATINUM" in fname:
        return "Platinum"
    if "-RED" in fname:
        return "Red"
    if "-BLACK" in fname:
        return "Black"
    return "Gold"

def read_md(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""

def extract_title_and_summary(text: str) -> tuple[str, str]:
    lines = [l.rstrip() for l in text.splitlines()]
    title = ""
    for l in lines:
        s = l.strip()
        if s.startswith("# "):
            title = s.lstrip("# ").strip()
            break
    if not title:
        for l in lines:
            if l.strip():
                title = l.strip()
                break
    # first paragraph (join until blank)
    para_lines = []
    started = False
    for l in lines:
        if not l.strip() and started:
            break
        if l.strip():
            started = True
            para_lines.append(l.strip())
    para = " ".join(para_lines)
    sentences = re.split(r'(?<=[.!?])\s+', para)
    summary = " ".join(sentences[:2]).strip()
    return title or "", summary or ""

def parse_filename(fname: str) -> tuple[str, str, str, str] | None:
    m = FNAME_RE.match(fname)
    if not m:
        return None
    cycle, typ, num, seal_token = m.groups()
    id_field = f"CAM-{cycle}-{typ}-{num}"
    return id_field, cycle, typ, seal_token or ""

def collect_items() -> list[dict]:
    items = []
    for p in sorted(PROT_DIR.glob("*.md")):
        if p.name == INDEX_PATH.name:
            continue
        text = read_md(p)
        title, summary = extract_title_and_summary(text)
        parsed = parse_filename(p.name)
        if parsed:
            id_field, cycle, typ, seal_token = parsed
            seal = infer_seal_from_token(seal_token, p.name)
        else:
            # log non-conforming filename
            print(f"WARNING: filename does not match expected pattern: {p.name}", file=sys.stderr)
            id_field = p.name
            seal = infer_seal_from_token(None, p.name)
        items.append({
            "id": id_field,
            "filename": p.name,
            "title": title,
            "summary": summary,
            "seal": seal,
            "path": os.path.relpath(p, REPO_ROOT).replace(os.sep, "/"),
        })
    # sort: try by id (CAM-...), fallback to filename
    def sort_key(it):
        return it["id"]
    return sorted(items, key=sort_key)

def render_table(items: list[dict]) -> str:
    out = []
    out.append("| id | filename | title | seal | link | summary |")
    out.append("|---|---|---|---|---|---|")
    for it in items:
        safe_title = it["title"].replace("|", "\\|")
        safe_summary = it["summary"].replace("|", "\\|")
        out.append(
            f"| {it['id']} | {it['filename']} | {safe_title} | {it['seal']} | "
            f"[{it['filename']}]({it['path']}) | {safe_summary} |"
        )
    return "\n".join(out)

def main() -> None:
    items = collect_items()
    body = render_table(items)
    old = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.exists() else ""
    if old and HEADER_MARKER in old:
        header, _ = old.split(HEADER_MARKER, 1)
        new_md = header.rstrip() + "\n" + HEADER_MARKER + "\n\n" + body
    else:
        new_md = body
    if new_md.strip() != old.strip():
        INDEX_PATH.write_text(new_md, encoding="utf-8")
        print(f"Updated: {INDEX_PATH}")
    else:
        print("No changes needed.")

if __name__ == "__main__":
    main()
