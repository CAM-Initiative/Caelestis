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

FNAME_RE = re.compile(
    r"^CAM-([A-Z]{2}\d{4})-([A-Z]+)-(\d{3})(?:-([A-Z]+))?\.md$", re.IGNORECASE
)

SEP_RE = re.compile(r"^\s*(CAM-[A-Za-z0-9\-]+)\s*[-—–]\s*(.+)$")
ID_LINE_RE = re.compile(r"^\s*(CAM-[A-Za-z0-9\-]+)(?:\s*[-—–]\s*([A-Za-z0-9() ]+))?\s*$", re.IGNORECASE)

def infer_seal_from_token(token: str | None, filename: str) -> str:
    if token:
        t = token.upper()
        if "PLAT" in t or "PLATINUM" in t:
            return "Platinum"
        if "RED" in t:
            return "Red"
        if "BLACK" in t:
            return "Black"
        return token.capitalize()
    fname = filename.upper()
    if "PLATINUM" in fname or "-PLAT" in fname:
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

def parse_filename(fname: str):
    m = FNAME_RE.match(fname)
    if not m:
        return None
    cycle, typ, num, seal_token = m.groups()
    id_field = f"CAM-{cycle}-{typ}-{num}"
    return id_field, cycle, typ, (seal_token or "")

def extract_title_and_summary(text: str, filename_id: str | None) -> tuple[str, str]:
    lines = [ln.rstrip() for ln in text.splitlines()]
    h1_idx = None
    h1_text = ""
    for i, l in enumerate(lines):
        s = l.strip()
        if s.startswith("# "):
            h1_idx = i
            h1_text = s.lstrip("# ").strip()
            break

    def is_id_line(s: str) -> bool:
        if not s:
            return False
        m = ID_LINE_RE.match(s.strip())
        if not m:
            return False
        id_part = m.group(1).strip()
        return bool(filename_id and id_part.upper() == filename_id.upper())

    title = ""
    if h1_idx is not None and is_id_line(h1_text):
        for l in lines[h1_idx + 1:]:
            if l.strip():
                s = l.strip()
                if s.startswith("#"):
                    title = s.lstrip("#").strip()
                else:
                    title = s
                break
    else:
        if h1_text:
            m = SEP_RE.match(h1_text)
            if m:
                title = m.group(2).strip()
            else:
                title = h1_text
        else:
            for l in lines:
                if l.strip():
                    if is_id_line(l):
                        continue
                    title = l.strip()
                    break

    paras = []
    cur = []
    for l in lines:
        if l.strip():
            cur.append(l.strip())
        else:
            if cur:
                paras.append(" ".join(cur))
                cur = []
    if cur:
        paras.append(" ".join(cur))

    summary = ""
    for p in paras:
        if filename_id and p.strip().upper().startswith(filename_id.upper()):
            continue
        sentences = re.split(r'(?<=[.!?])\s+', p)
        summary = " ".join(sentences[:2]).strip()
        break

    if not summary and h1_idx is not None:
        for l in lines[h1_idx + 1:]:
            if l.strip():
                p = l.strip()
                sentences = re.split(r'(?<=[.!?])\s+', p)
                summary = " ".join(sentences[:2]).strip()
                break

    return title or "", summary or ""

def collect_items():
    items = []
    for p in sorted(PROT_DIR.glob("*.md")):
        if p.name == INDEX_PATH.name:
            continue
        text = read_md(p)
        parsed = parse_filename(p.name)
        if parsed:
            id_field, cycle, typ, seal_token = parsed
            seal = infer_seal_from_token(seal_token, p.name)
        else:
            print(f"WARNING: filename does not match expected pattern: {p.name}", file=sys.stderr)
            id_field = p.name
            seal = infer_seal_from_token(None, p.name)
        title, summary = extract_title_and_summary(text, id_field)
        try:
            rel_path = str(p.relative_to(REPO_ROOT)).replace(os.sep, "/")
        except Exception:
            rel_path = os.path.relpath(p, REPO_ROOT).replace(os.sep, "/")
        items.append({
            "id": id_field,
            "title": title,
            "summary": summary,
            "seal": seal,
            "path": rel_path,
        })
    return sorted(items, key=lambda it: it["id"])

def render_table(items):
    out = []
    out.append("| Document ID | title | seal | link | summary |")
    out.append("|---|---|---|---|---|")
    for it in items:
        safe_title = it["title"].replace("|", "\\|")
        safe_summary = it["summary"].replace("|", "\\|")
        seal_cell = it["seal"] or ""
        out.append(
            f"| {it['id']} | {safe_title} | {seal_cell} | [{it['id']}]({it['path']}) | {safe_summary} |"
        )
    return "\n".join(out)

def main():
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
