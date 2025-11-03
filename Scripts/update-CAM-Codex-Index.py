#!/usr/bin/env python3
from __future__ import annotations
"""
Rebuilds Governance/Codex/CAM-Codex-Index.md
- Scans Governance/Codex/*.md (excluding the index file)
- Extracts: ID, Title, 1–2 sentence summary (from Purpose section)
- Auto-sorts by filename
- Writes index with relative links, preserving manual header block

Also appends a **Library** table with short fields: id, title, type, seal, path, pinned git sha, timestamp.
"""

import re
import os
import subprocess
from pathlib import Path

# ---- config ----
REPO_ROOT = Path(__file__).resolve().parents[1]
CODEX_DIR = REPO_ROOT / "Governance" / "Codex"
INDEX_PATH = CODEX_DIR / "CAM-Codex-Index.md"

HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"

# Capture canonical ID up to ...-CODEX-<digits>, allowing any suffix after
ID_RE = re.compile(r"^(CAM-[A-Z0-9-]*-CODEX-(\d+))(?:[-A-Z0-9].*)?$", re.IGNORECASE)

def extract_summary(text: str) -> str:
    """Gets the first paragraph under a 'Purpose' section, or the first non-header paragraph."""
    section_pattern = re.compile(
        r"^##\s*(?:[IVXLC]+\.\s*)?Purpose\s*$([\s\S]+?)(?:^##|\Z)",
        re.MULTILINE | re.IGNORECASE
    )
    m = section_pattern.search(text)
    if m:
        section = m.group(1)
        paras = [p.strip() for p in re.split(r"\n\s*\n", section) if p.strip()]
        if paras:
            return " ".join(paras[0].split())

    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    for para in paragraphs:
        if (para.count(":") > 2 or para.startswith("**")):
            continue
        return " ".join(para.split())
    return paragraphs[0] if paragraphs else ""

def parse_file(md_path: Path) -> dict | None:
    name = md_path.name
    if name == INDEX_PATH.name or md_path.suffix.lower() != ".md":
        return None

    stem = md_path.stem
    m = ID_RE.match(stem) or ID_RE.search(stem)
    if not m:
        # Uncomment to debug: print(f"[SKIP] No ID match: {name}")
        return None

    id_full = m.group(1)
    num = int(m.group(2))

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
        "num": num,
        "title": title,
        "summary": summary,
        "filename": md_path.name,
    }

def collect_codex_items() -> list[dict]:
    items: list[dict] = []
    if not CODEX_DIR.exists():
        print(f"[WARN] CODEX_DIR not found: {CODEX_DIR}")
        return items

    for p in sorted(CODEX_DIR.iterdir()):
        if not p.is_file():
            continue
        if p.suffix.lower() != ".md":
            continue
        rec = parse_file(p)
        if rec:
            items.append(rec)
        # else: uncomment to debug skipped files
        # else:
        #     print(f"[SKIP] No ID match: {p.name}")

    # Optional: visibility
    # print(f"[INFO] Collected {len(items)} codex items")
    return items

def infer_seal(filename: str) -> str:
    """Infer the seal designation based on filename."""
    fname = filename.upper()
    if "-RED" in fname:
        return "Red"
    if "-BLACK" in fname:
        return "Black"
    if "-PLATINUM" in fname:
        return "Platinum"
    if "-GOLD" in fname:
        return "Gold"
    return ""

def get_git_info(md_path: Path) -> tuple[str, str]:
    try:
        result = subprocess.check_output(
            ["git", "log", "-n", "1", "--format=%H|%aI", "--", str(md_path)],
            cwd=REPO_ROOT,
            text=True,
        ).strip()
        if not result:
            return "", ""
        sha, iso_date = result.split("|", 1)
        return sha, iso_date
    except Exception:
        return "", ""

def render_library(items: list[dict]) -> str:
    rows = []
    for rec in items:
        md_path = CODEX_DIR / rec["filename"]
        sha, date = get_git_info(md_path)
        seal = infer_seal(rec["filename"])
        rel_path = os.path.relpath(md_path, REPO_ROOT).replace(os.sep, "/")
        rows.append({
            "id": rec["id"],
            "title": rec["title"],
            "type": "Codex",
            "seal": seal,
            "path": rel_path,
            "sha": sha,
            "date": date,
        })

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

def render_index(items: list[dict]) -> str:
    out: list[str] = []
    out.append("## Codex\n")
    for r in sorted(items, key=lambda r: r["num"]):
        link_text = f"{r['id']} - {r['title']}"
        out.append(f"- [{link_text}]({r['filename']})  ")
        if r["summary"]:
            out.append(f"  _{r['summary']}_")
        out.append("")
    out.append("")
    return "\n".join(out)

def main() -> None:
    items = collect_codex_items()
    generated_md = render_index(items) + render_library(items)

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
