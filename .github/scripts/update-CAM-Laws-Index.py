#!/usr/bin/env python3
import os
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
from instrument_parser import parse_instrument_filename

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from instrument_state import extract_status_and_version

TARGET_DIR = REPO_ROOT / "Governance" / "Laws"
INDEX_MD = TARGET_DIR / "CAM-Laws-Index.md"
INDEX_JSON = TARGET_DIR / "laws.index.json"
HEADER_MARKER = "<!-- BEGIN AUTO-GENERATED -->"
SUMMARY_KEYWORDS = {"jurisdiction", "standing", "scope", "application", "purpose", "preamble", "intent"}
SEAL_WORDS = {"platinum", "gold", "red", "black"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def get_git_info(path: Path) -> tuple[str, str]:
    out = subprocess.check_output(
        ["git", "log", "--follow", "-n", "1", "--format=%H|%cI", "--", str(path)],
        cwd=REPO_ROOT,
        text=True,
    ).strip()
    if not out:
        return "", ""
    sha, iso = out.split("|", 1)
    dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return sha, dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def manifest_sha_by_path() -> dict[str, str]:
    manifest_path = REPO_ROOT / "MANIFEST.json"
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    return {str(e.get("path")): str(e.get("sha256") or "").strip().lower() for e in payload.get("files", [])}

def normalise(text: str) -> str:
    return re.sub(r"[^\w\s]", "", text).lower()


def extract_title_and_summary(text: str, doc_id: str) -> tuple[str, str]:
    lines = [ln.rstrip() for ln in text.splitlines()]
    title = ""
    summary = ""
    h1_idx = None

    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            h1_idx = i
            h = ln[2:].strip()
            m = re.match(r"^(CAM-[\w\-]+)\s*[-—–]\s*(.+)$", h)
            if m and normalise(m.group(2).strip()) not in SEAL_WORDS:
                title = m.group(2).strip()
            break

    if not title and h1_idx is not None:
        for ln in lines[h1_idx + 1 :]:
            if ln.startswith("#"):
                cand = ln.lstrip("#").strip()
                n = normalise(cand)
                if n and n != normalise(doc_id) and n not in SEAL_WORDS and not any(k in n for k in SUMMARY_KEYWORDS):
                    title = cand
                    break

    for i, ln in enumerate(lines):
        if ln.startswith("#") and any(k in normalise(ln) for k in SUMMARY_KEYWORDS):
            for ln2 in lines[i + 1 :]:
                s = ln2.strip()
                if not s:
                    continue
                if s.startswith("#") or s.startswith("|"):
                    break
                if s.startswith("**") and s.endswith("**"):
                    continue
                summary = " ".join(re.split(r"(?<=[.!?])\s+", s)[:2]).strip()
                return title, summary

    return title, summary


def collect_items() -> tuple[list[dict], list[str], int]:
    items = []
    skipped = []
    md_files = sorted(p for p in TARGET_DIR.glob("*.md") if p.name != INDEX_MD.name)
    print(f"[debug] {TARGET_DIR.name}: detected markdown files={len(md_files)}")

    manifest = manifest_sha_by_path()

    for p in md_files:
        parsed = parse_instrument_filename(p.name, "laws")
        if not parsed:
            skipped.append(f"{p.name}: filename did not match instrument pattern")
            continue

        text = read_text(p)
        title, summary = extract_title_and_summary(text, parsed["id"])
        sha, updated_at = get_git_info(p)
        status, version = extract_status_and_version(p.resolve())
        rel = p.relative_to(REPO_ROOT).as_posix()
        content_hash = manifest.get(rel, "")
        parsed.update({
            "link": p.name,
            "title": title,
            "summary": summary,
            "status": status,
            "version": version,
            "HASH": content_hash,
            "pinned_sha": sha,
            "updated_at": updated_at,
            "last_updated_utc": updated_at,
        })
        items.append(parsed)

    return sorted(items, key=lambda x: x["id"]), skipped, len(md_files)


def render_markdown(items: list[dict]) -> str:
    out = ["| ID | Class | Seal | Link | Title |", "|---|---|---|---|---|"]
    for it in items:
        seal = it["seal"] or ""
        out.append(
            f"| {it['id']} | {it['instrument_class']} | {seal} | [{it['id']}]({it['link']}) | {it['title']} |"
        )
    return "\n".join(out)


def write_json(items: list[dict]) -> None:
    payload = {
        "count": len(items),
        "items": items,
    }
    INDEX_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    items, skipped, detected = collect_items()
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
    print(f"[debug] files detected={detected}")
    print(f"[debug] entries written={len(items)}")
    if skipped:
        print("[debug] skipped files:")
        for s in skipped:
            print(f"[debug] - {s}")
    else:
        print("[debug] skipped files: none")


if __name__ == "__main__":
    main()
