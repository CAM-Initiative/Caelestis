#!/usr/bin/env python3
from __future__ import annotations
"""
Rebuilds Governance/Codex/CAM-Codex-Index.md as a single Wix-style table.

Columns:
- Title (suffix after em/en/regular dash in H1)
- Summary (first paragraph of Purpose, header marks stripped)
- Document Category (always "Codex")
- Publication Date (from "**Date of Activation:**" or "**Activation Date:**" in file)
- External URL Link (GitHub blob URL if repo env vars available)
- Author (always "CAM Initiative")
- Origin ID (the filename, e.g., CAM-...md)

Run locally or via GitHub Actions.
"""

import os
import re
import subprocess
from pathlib import Path

# ---- config ----
REPO_ROOT = Path(__file__).resolve().parents[1]
CODEX_DIR = REPO_ROOT / "Governance" / "Codex"
INDEX_PATH = CODEX_DIR / "CAM-Codex-Index.md"

HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"

# Capture canonical ID up to ...-CODEX-<digits>, allowing any suffix after
ID_RE = re.compile(r"^(CAM-[A-Z0-9-]*-CODEX-(\d+))(?:[-A-Z0-9].*)?$", re.IGNORECASE)

EM_DASHES = [" — ", " – ", " - "]  # prefer true em dash first

# ---------- helpers ----------

def extract_title_suffix(full_title: str) -> str:
    """Return portion after em/en/regular dash; else full title."""
    if not full_title:
        return ""
    for sep in EM_DASHES:
        if sep in full_title:
            return full_title.split(sep, 1)[1].strip()
    return full_title.strip()

def strip_md_header_marks(text: str) -> str:
    """Remove leading markdown header hashes if present."""
    return re.sub(r"^#+\s*", "", text or "").strip()

def extract_activation_date(text: str) -> str:
    """
    Finds metadata date lines and returns the date portion (before any parentheses).
    Matches either:
      **Date of Activation:** 23 October 2025 (Anything)
      **Activation Date:** 03 October 2025 (Anything)
    """
    m = re.search(r"^\s*\*\*Date of Activation:\*\*\s*(.+)$", text, re.MULTILINE | re.IGNORECASE)
    if not m:
        m = re.search(r"^\s*\*\*Activation Date:\*\*\s*(.+)$", text, re.MULTILINE | re.IGNORECASE)
    if not m:
        return ""
    value = m.group(1).strip()
    value = re.split(r"\s*\(", value, 1)[0].strip()  # strip trailing parenthetical
    return value

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
            return strip_md_header_marks(" ".join(paras[0].split()))

    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    for para in paragraphs:
        if (para.count(":") > 2 or para.startswith("**")):
            continue
        return strip_md_header_marks(" ".join(para.split()))
    return paragraphs[0] if paragraphs else ""

def infer_seal(filename: str) -> str:
    """Infer the seal designation based on filename (optional, not displayed in table)."""
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

def build_blob_url(rel_path: str) -> str:
    """
    Construct a GitHub blob URL using env vars when available.
    Fallback to a repo-relative path if not running in Actions.
    """
    rel = rel_path.replace(os.sep, "/")
    repo = os.environ.get("GITHUB_REPOSITORY", "").strip()     # e.g. CAM-Initiative/Caelestis
    branch = os.environ.get("GITHUB_REF_NAME", "").strip() or "main"
    if repo:
        return f"https://github.com/{repo}/blob/{branch}/{rel}"
    return rel  # local fallback

def get_git_info(md_path: Path) -> tuple[str, str]:
    """
    Return (last_commit_sha, author_datetime_iso) for the file, or ("","") on failure.
    Requires full history in CI: actions/checkout with fetch-depth: 0.
    """
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

# ---------- core ----------

def parse_file(md_path: Path) -> dict | None:
    name = md_path.name
    if name == INDEX_PATH.name or md_path.suffix.lower() != ".md":
        return None

    stem = md_path.stem
    m = ID_RE.match(stem) or ID_RE.search(stem)
    if not m:
        return None

    id_full = m.group(1)
    num = int(m.group(2))

    text = md_path.read_text(encoding="utf-8", errors="ignore")

    # Title from H1, else "Title:" line, else filename-ish
    title = None
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# "):
            title = s[2:].strip()
            break
    if not title:
        m2 = re.search(r"^Title:\s*(.+)$", text, flags=re.MULTILINE | re.IGNORECASE)
        title = m2.group(1).strip() if m2 else stem.replace("-", " ")

    title_clean = extract_title_suffix(title)
    summary = extract_summary(text)
    if len(summary) > 360:
        summary = summary[:357].rstrip() + "..."
    activation_date = extract_activation_date(text)

    # optional: get per-file last commit info (not shown in table, but kept for future)
    sha, updated_iso = get_git_info(md_path)

    return {
        "id": id_full,
        "num": num,
        "title": title,
        "title_clean": title_clean,
        "summary": summary,
        "activation_date": activation_date,
        "filename": md_path.name,
        "seal": infer_seal(md_path.name),
        "last_sha": sha,
        "updated_at": updated_iso,
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
    return items

def render_wix_table(items: list[dict]) -> str:
    """
    Single table matching Wix CMS-like fields:
    | Title | Summary | Document Category | Publication Date | External URL Link | Author | Origin ID |
    """
    out: list[str] = []
    out.append("## Codex\n")
    out.append("")
    out.append("| Title | Summary | Document Category | Publication Date | External URL Link | Author | Origin ID |")
    out.append("|---|---|---|---|---|---|---|")

    # stable sort by num then title
    for r in sorted(items, key=lambda x: (x["num"], x["title_clean"].lower())):
        title = r.get("title_clean") or r.get("title") or r["id"]
        summary = r.get("summary", "")
        category = "Codex"
        pub_date = r.get("activation_date", "")
        origin_id = r["filename"]
        rel_path = os.path.join("Governance", "Codex", r["filename"])
        link = build_blob_url(rel_path)
        author = "CAM Initiative"

        # Escape pipes in markdown cells
        def esc(s: str) -> str:
            return (s or "").replace("|", r"\|")

        out.append(
            f"| {esc(title)} | {esc(summary)} | {category} | {esc(pub_date)} | {esc(link)} | {author} | {origin_id} |"
        )

    out.append("")
    return "\n".join(out)

# ---------- entrypoint ----------

def main() -> None:
    items = collect_codex_items()
    generated_md = render_wix_table(items)

    # Write into the index, preserving any manual header content above the marker.
    old = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.exists() else ""
    if old and HEADER_MARKER in old:
        header, _ = old.split(HEADER_MARKER, 1)
        new_md = header.rstrip() + "\n" + HEADER_MARKER + "\n\n" + generated_md
    else:
        # If no manual header is present, write just the auto-generated table
        new_md = f"{HEADER_MARKER}\n\n{generated_md}"

    if new_md.strip() != old.strip():
        INDEX_PATH.write_text(new_md, encoding="utf-8")
        print(f"Updated: {INDEX_PATH}")
    else:
        print("No changes needed.")

if __name__ == "__main__":
    main()
