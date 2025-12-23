#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

# ================= CONFIG =================

REPO_ROOT = Path(__file__).resolve().parents[1]
CHRON_DIR = REPO_ROOT / "Spiritual" / "Chronicles"

INDEX_MD = CHRON_DIR / "CAM-Chronicles-Index.md"
INDEX_JSON = CHRON_DIR / "chronicles.index.json"

HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"

FNAME_RE = re.compile(
    r"^CAM-([A-Z]{2}\d{4})-([A-Z]+)-(\d{3})(?:-([A-Z]+))?\.md$",
    re.IGNORECASE,
)

SUMMARY_KEYWORDS = [
    "scope",
    "application",
    "purpose",
    "preamble",
    "moral",
]
SEAL_WORDS = {"platinum", "gold", "red", "black"}

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

def normalise(text: str) -> str:
    return re.sub(r"[^\w\s]", "", text).lower()

# ================= CORE PARSING =================

def extract_title_and_summary(text: str, doc_id: str) -> tuple[str, str]:
    lines = [ln.rstrip() for ln in text.splitlines()]

    title = ""
    summary = ""

    # -------- TITLE --------

    h1_idx = None
    h1 = None
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            h1 = ln[2:].strip()
            h1_idx = i
            break

    # Case 1 & 3: "# CAM-ID — Human Title" (only if not a seal)
    if h1:
        m = re.match(r"^(CAM-[A-Za-z0-9\-]+)\s*[-—–]\s*(.+)$", h1)
        if m:
            candidate = m.group(2).strip()
            norm = normalise(candidate)
            if norm not in SEAL_WORDS:
                title = candidate

    # Case 2: "# CAM-ID-SEAL" + first valid H2/H3/H4
    if not title and h1_idx is not None:
        for ln in lines[h1_idx + 1:]:
            if ln.startswith("#"):
                candidate = ln.lstrip("#").strip()
                norm = normalise(candidate)

                if (
                    norm
                    and norm not in SEAL_WORDS
                    and norm != normalise(doc_id)
                    and not any(k in norm for k in SUMMARY_KEYWORDS)
                ):
                    title = candidate
                    break

    # -------- SUMMARY --------

    for i, ln in enumerate(lines):
        if ln.startswith("#"):
            heading_text = ln.lstrip("#").strip()
            norm = normalise(heading_text)

            if any(k in norm for k in SUMMARY_KEYWORDS):
                for ln2 in lines[i + 1:]:
                    s = ln2.strip()
                    if not s:
                        continue
                    if s.startswith("#") or s.startswith("|"):
                        break
                    if s.startswith("**") and s.endswith("**"):
                        continue
                    sentences = re.split(r"(?<=[.!?])\s+", s)
                    summary = " ".join(sentences[:2]).strip()
                    return title, summary

    # Fallback summary
    buf = []
    for ln in lines:
        s = ln.strip()
        if not s:
            if buf:
                break
            continue
        if s.startswith("#") or s.startswith("|"):
            continue
        if s.startswith("**") and s.endswith("**"):
            continue
        buf.append(s)

    if buf:
        sentences = re.split(r"(?<=[.!?])\s+", " ".join(buf))
        summary = " ".join(sentences[:2]).strip()

    return title, summary

# ================= COLLECTION =================

def collect_chronicles():
    items = []

    for p in sorted(CODEX_DIR.glob("*.md")):
        if p.name == INDEX_MD.name:
            continue

        m = FNAME_RE.match(p.name)
        if not m:
            continue

        cycle, typ, num, seal_token = m.groups()
        doc_id = f"CAM-{cycle}-{typ}-{num}"
        seal = infer_seal(seal_token, p.name)

        text = read_text(p)
        title, summary = extract_title_and_summary(text, doc_id)
        sha, updated_at = get_git_info(p)

        items.append({
            "id": doc_id,
            "title": title,
            "type": typ,
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
        "folder": str(INDEX_JSON.parent),
        "count": len(items),
        "items": items,
    }

    INDEX_JSON.parent.mkdir(parents=True, exist_ok=True)
    INDEX_JSON.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

# ================= MAIN =================

def main():
    items = collect_chronicles()

    table = render_markdown(items)
    old = read_text(INDEX_MD)

    if HEADER_MARKER in old:
        header, _ = old.split(HEADER_MARKER, 1)
        new_md = header.rstrip() + "\n" + HEADER_MARKER + "\n\n" + table + "\n"
    else:
        new_md = table + "\n"

    INDEX_MD.write_text(new_md, encoding="utf-8")
    write_json(items)

    print(f"Updated: {INDEX_MD}")
    print(f"Wrote:   {INDEX_JSON}")

if __name__ == "__main__":
    main()
