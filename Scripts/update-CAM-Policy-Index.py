#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

# ================= CONFIG =================

REPO_ROOT = Path(__file__).resolve().parents[1]
POLICY_DIR = REPO_ROOT / "Governance" / "Policies"

INDEX_MD = PROT_DIR / "CAM-Policy-Index.md"
INDEX_JSON = PROT_DIR / "policy.index.json"

HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"

FNAME_RE = re.compile(
    r"^CAM-([A-Z]{2}\d{4})-([A-Z]+)-(\d{3})(?:-([A-Z]+))?\.md$",
    re.IGNORECASE,
)

SEAL_WORDS = {"PLATINUM", "GOLD", "RED", "BLACK"}
SUMMARY_HEADINGS = {"purpose", "preamble", "intent"}

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

# ================= CORE PARSING =================

def extract_title_and_summary(text: str, doc_id: str) -> tuple[str, str]:
    lines = [ln.rstrip() for ln in text.splitlines()]

    h1_idx = None
    h1 = None
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

    # Case 2: ID-only H1 (including seal suffix)
    if not title and h1:
        stripped = re.sub(
            r"-(PLATINUM|GOLD|RED|BLACK)$",
            "",
            h1,
            flags=re.IGNORECASE,
        )
        if stripped.upper() == doc_id.upper():
            title = ""

    # Case 3: SOLAN-style — first H2 is ALWAYS the title
    if not title and h1_idx is not None:
        for ln in lines[h1_idx + 1:]:
            if ln.startswith("## "):
                title = ln[3:].strip()
                break
            if ln.startswith("# "):
                break

    # Absolute guard
    if title.upper() in {"PLATINUM", "GOLD", "RED", "BLACK"}:
        title = ""

    # -------- SUMMARY --------
    summary = ""
    preferred = {"purpose", "preamble", "intent"}

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
        if s.startswith("**") and ":" in s:
            continue
        buf.append(s)

    if buf:
        sentences = re.split(r"(?<=[.!?])\s+", " ".join(buf))
        summary = " ".join(sentences[:2]).strip()

    return title, summary

# ================= COLLECTION =================

def collect_policies():
    items = []

    for p in sorted(POLICY_DIR.glob("*.md")):
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
            "link": p.name,               # correct relative link
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
        "folder": "Governance/Policies",
        "count": len(items),
        "items": items,
    }
    INDEX_JSON.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

# ================= MAIN =================

def main():
    items = collect_policies()

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
