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
FNAME_RE = re.compile(
    r"^CAM-([A-Z]{2}\d{4})-([A-Z]+)-(\d{3})(?:-([A-Z]+))?\.md$", re.IGNORECASE
)

# Match leading ID followed by a separator (hyphen/en-dash/em-dash) and trailing text
TITLE_ID_PREFIX_RE = re.compile(
    r"^\s*(CAM-[A-Za-z0-9\-]+)\s*[-—–]\s*(.+)$"
)

# Also accept titles where ID is followed by newline then the real title
TITLE_ID_PREFIX_NEWLINE_RE = re.compile(
    r"^\s*(CAM-[A-Za-z0-9\-]+)\s*\n\s*(.+)$", re.IGNORECASE | re.DOTALL
)

def infer_seal_from_token(token: str | None, filename: str) -> str:
    # Return "" (blank) for explicit PLATINUM token per request
    if token:
        t = token.upper()
        if "PLAT" in t or "PLATINUM" in t:
            return ""   # blank when explicitly platinum
        if "RED" in t:
            return "Red"
        if "BLACK" in t:
            return "Black"
        return token.capitalize()
    # fallback: inspect filename for markers; PLATINUM -> blank
    fname = filename.upper()
    if "PLATINUM" in fname or "-PLAT" in fname:
        return ""
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
    raw_title = ""
    for l in lines:
        s = l.strip()
        if s.startswith("# "):
            raw_title = s.lstrip("# ").strip()
            break
    if not raw_title:
        for l in lines:
            if l.strip():
                raw_title = l.strip()
                break

    # If title starts with an ID + separator (dash/en/em) or ID + newline, strip that prefix
    m = TITLE_ID_PREFIX_RE.match(raw_title)
    if m:
        # only strip when there is text after the separator (m.group(2))
        title = m.group(2).strip()
    else:
        m2 = TITLE_ID_PREFIX_NEWLINE_RE.match(text)
        if m2:
            title = m2.group(2).strip().splitlines()[0].strip()
        else:
            title = raw_title

    # Build first paragraph (join lines until blank)
    para_lines = []
    started = False
    for l in lines:
        if not l.strip() and started:
            break
        if l.strip():
            started = True
            para_lines.append(l.strip())
    para = " ".join(para_lines)

    # Truncate to 1-2 sentences: prefer up to two sentences
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
            print(f"WARNING: filename does not match expected pattern: {p.name}", file=sys.stderr)
            id_field = p.name
            seal = infer_seal_from_token(None, p.name)
        try:
            rel_path = str(p.relative_to(REPO_ROOT)).replace(os.sep, "/")
        except Exception:
            rel_path = os.path.relpath(p, REPO_ROOT).replace(os.sep, "/")
        items.append({
            "id": id_field,
            "filename": p.name,
            "title": title,
            "summary": summary,
            "seal": seal,
            "path": rel_path,
        })
    return sorted(items, key=lambda it: it["id"])

def render_table(items: list[dict]) -> str:
    out = []
    out.append("| id | filename | title | seal | link | summary |")
    out.append("|---|---|---|---|---|---|")
    for it in items:
        safe_title = it["title"].replace("|", "\\|")
        safe_summary = it["summary"].replace("|", "\\|")
        seal_cell = it["seal"] or ""  # blank for explicit Platinum
        out.append(
            f"| {it['id']} | {it['filename']} | {safe_title} | {seal_cell} | "
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
