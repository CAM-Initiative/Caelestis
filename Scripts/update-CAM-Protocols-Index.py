#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

# ================= CONFIG =================

REPO_ROOT = Path(__file__).resolve().parents[1]
PROT_DIR = REPO_ROOT / "Governance" / "Protocols"

INDEX_MD = PROT_DIR / "CAM-Protocols-Index.md"
INDEX_JSON = PROT_DIR / "protocols.index.json"

HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"

FNAME_RE = re.compile(
    r"^CAM-([A-Z]{2}\d{4})-([A-Z]+)-(\d{3})(?:-([A-Z]+))?\.md$",
    re.IGNORECASE,
)

# ================= HELPERS =================

def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""

def infer_seal(token: str | None, filename: str) -> str:
    if token:
        t = token.upper()
        if "PLAT" in t:
            return "Platinum"
        if "RED" in t:
            return "Red"
        if "BLACK" in t:
            return "Black"
        return token.capitalize()

    f = filename.upper()
    if "PLATINUM" in f:
        return "Platinum"
    if "-RED" in f:
        return "Red"
    if "-BLACK" in f:
        return "Black"
    return "Gold"

def get_git_info(path: Path) -> tuple[str, str]:
    try:
        out = subprocess.check_output(
            ["git", "log", "-n", "1", "--format=%H|%aI", "--", str(path)],
            cwd=REPO_ROOT,
            text=True,
        ).strip()
        sha, iso = out.split("|", 1)
        return sha, iso
    except Exception:
        return "", ""

# ================= PARSING =================

def extract_title_and_summary(text: str, doc_id: str | None) -> tuple[str, str]:
    lines = [ln.rstrip() for ln in text.splitlines()]

    # ---------- TITLE ----------
    h1 = None
    h1_idx = None
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            h1 = ln[2:].strip()
            h1_idx = i
            break

    title = ""

    # Case 1: "# ID — Title"
    if h1:
        m = re.match(r"^(CAM-[A-Za-z0-9\-]+)\s*[-—–]\s*(.+)$", h1)
        if m:
            title = m.group(2).strip()
        else:
            # Strip seal suffixes from ID-only H1s
            stripped = re.sub(
                r"-(PLATINUM|GOLD|RED|BLACK)$",
                "",
                h1,
                flags=re.IGNORECASE,
            )
            if doc_id and stripped.upper() == doc_id.upper():
                title = ""

    # Case 2: ID-only H1 → first H2 is title
    if not title and h1_idx is not None:
        for ln in lines[h1_idx + 1:]:
            if ln.startswith("## "):
                candidate = ln[3:].strip()
                if ":" not in candidate:
                    title = candidate
                break
            if ln.startswith("# "):
                break

    # ---------- SUMMARY ----------
    summary = ""
    preferred = {"purpose", "preamble", "intent"}

    # Prefer summary under named sections
    for i, ln in enumerate(lines):
        if ln.startswith("## "):
            heading = ln[3:].strip().lower()
            if heading in preferred:
                for ln2 in lines[i + 1:]:
                    s = ln2.strip()
                    if not s:
                        continue
                    if s.startswith("#") or s.startswith("|"):
                        break
                    if s.startswith("**") and ":" in s:
                        continue
                    sentences = re.split(r"(?<=[.!?])\s+", s)
                    summary = " ".join(sentences[:2]).strip()
                    return title, summary

    # Fallback: first real paragraph anywhere
    buf = []
    for ln in lines:
        s = ln.strip()
        if not s:
            if buf:
                break
            continue
        if s.startswith("#") or s.startswith("|"):
            continue
        if s.startswith("**") and ":" in s:
            continue
        buf.append(s)

    if buf:
        sentences = re.split(r"(?<=[.!?])\s+", " ".join(buf))
        summary = " ".join(sentences[:2]).strip()

    return title, summary

# ================= COLLECTION =================

def collect_items():
    items = []

    for p in sorted(PROT_DIR.glob("*.md")):
        if p.name == INDEX_MD.name:
            continue

        text = read_text(p)
        m = FNAME_RE.match(p.name)

        if not m:
            print(f"WARNING: filename pattern mismatch: {p.name}", file=sys.stderr)
            continue

        cycle, typ, num, seal_token = m.groups()
        doc_id = f"CAM-{cycle}-{typ}-{num}"
        seal = infer_seal(seal_token, p.name)

        title, summary = extract_title_and_summary(text, doc_id)
        sha, updated_at = get_git_info(p)

        items.append({
            "id": doc_id,
            "title": title,
            "type": typ.upper(),
            "seal": seal,
            "link": p.name,
            "summary": summary,
            "pinned_sha": sha,
            "updated_at": updated_at,
        })

    return sorted(items, key=lambda x: x["id"])

# ================= OUTPUT =================

def render_markdown(items):
    out = []
    out.append("| Document ID | title | type | seal | link | summary |")
    out.append("|---|---|---|---|---|---|")

    for it in items:
        safe_title = it["title"].replace("|", "\\|")
        safe_summary = it["summary"].replace("|", "\\|")

        out.append(
            f"| {it['id']} | {safe_title} | {it['type']} | {it['seal']} | "
            f"[{it['id']}]({it['link']}) | {safe_summary} |"
        )

    return "\n".join(out)

def write_json(items):
    payload = {
        "generated_from": INDEX_MD.name,
        "folder": "Governance/Protocols",
        "count": len(items),
        "items": items,
    }
    INDEX_JSON.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

# ================= MAIN =================

def main():
    items = collect_items()
    table = render_markdown(items)

    old = read_text(INDEX_MD)
    if old and HEADER_MARKER in old:
        header, _ = old.split(HEADER_MARKER, 1)
        new_md = header.rstrip() + "\n" + HEADER_MARKER + "\n\n" + table + "\n"
    else:
        new_md = table + "\n"

    if new_md.strip() != old.strip():
        INDEX_MD.write_text(new_md, encoding="utf-8")
        print(f"Updated: {INDEX_MD}")
    else:
        print("No changes needed.")

    write_json(items)
    print(f"Wrote: {INDEX_JSON}")

if __name__ == "__main__":
    main()
