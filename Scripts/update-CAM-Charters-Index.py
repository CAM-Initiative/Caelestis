#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from datetime import datetime, timezone

# ================= CONFIG =================

REPO_ROOT = Path(__file__).resolve().parents[1]
CHARTERS_DIR = REPO_ROOT / "Governance" / "Charters"

INDEX_MD = CHARTERS_DIR / "CAM-Charters-Index.md"
INDEX_JSON = CHARTERS_DIR / "charters.index.json"

HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"

# Supports:
# CAM-BS2026-CHARTER-015-PLATINUM.md
# CAM-BS2026-CHARTER-015-SCH-01.md
FNAME_RE = re.compile(
    r"^CAM-([A-Z]{2}\d{4})-(CHARTER)-(\d{3})"
    r"(?:-(?:SCH|SCHEDULE)-([A-Z0-9]+))?"
    r"(?:-([A-Z]+))?\.md$",
    re.IGNORECASE,
)

SUMMARY_KEYWORDS = {"purpose", "preamble", "intent", "context"}
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
    return "Gold"

def get_git_info(path: Path) -> tuple[str, str]:
    try:
        out = subprocess.check_output(
            [
                "git",
                "log",
                "--follow",
                "-n",
                "1",
                "--format=%H|%cI",
                "--",
                str(path),
            ],
            cwd=REPO_ROOT,
            text=True,
        ).strip()

        sha, iso = out.split("|", 1)
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        iso_utc = dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
        return sha, iso_utc
    except Exception:
        return "", ""

def normalise(text: str) -> str:
    return re.sub(r"[^\w\s]", "", text).lower()

# ================= CORE =================

def extract_title_and_summary(text: str, doc_id: str) -> tuple[str, str]:
    lines = [ln.rstrip() for ln in text.splitlines()]
    title = ""
    summary = ""

    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            h = ln[2:].strip()
            m = re.match(r"^(CAM-[\w\-]+)\s*[-—–]\s*(.+)$", h)
            if m:
                title = m.group(2).strip()
            break

    for i, ln in enumerate(lines):
        if ln.startswith("#"):
            if any(k in normalise(ln) for k in SUMMARY_KEYWORDS):
                for ln2 in lines[i + 1:]:
                    s = ln2.strip()
                    if not s or s.startswith("#") or s.startswith("|"):
                        break
                    summary = s
                    return title, summary

    return title, summary

# ================= COLLECTION =================

def collect_charters():
    items = []

    for p in sorted(CHARTERS_DIR.glob("*.md")):
        if p.name == INDEX_MD.name:
            continue

        m = FNAME_RE.match(p.name)
        if not m:
            continue

        cycle, typ, num, schedule, seal_token = m.groups()

        parent_id = f"CAM-{cycle}-{typ}-{num}"
        if schedule:
            doc_id = f"{parent_id}-SCH-{schedule}"
            kind = "schedule"
        else:
            doc_id = parent_id
            kind = "charter"

        seal = infer_seal(seal_token, p.name)
        text = read_text(p)
        title, summary = extract_title_and_summary(text, doc_id)
        sha, updated_at = get_git_info(p)

        items.append({
            "id": doc_id,
            "parent_id": None if kind == "charter" else parent_id,
            "kind": kind,
            "type": typ,
            "seal": seal,
            "link": p.name,
            "title": title,
            "summary": summary,
            "pinned_sha": sha,
            "updated_at": updated_at,
        })

    return sorted(items, key=lambda x: x["id"])

# ================= OUTPUT =================

def render_markdown(items):
    out = []
    out.append("| ID | Kind | Parent | Seal | Link | Title |")
    out.append("|---|---|---|---|---|---|")

    for it in items:
        parent = it["parent_id"] or ""
        out.append(
            f"| {it['id']} | {it['kind']} | {parent} | {it['seal']} | "
            f"[{it['id']}]({it['link']}) | {it['title']} |"
        )

    return "\n".join(out)

def write_json(items):
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "count": len(items),
        "items": items,
    }

    INDEX_JSON.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

def main():
    items = collect_charters()
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
