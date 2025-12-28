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
# CAM-BS2025-CHARTER-015-PLATINUM.md
# CAM-BS2025-CHARTER-015-SCH-01.md
# CAM-BS2025-CHARTER-015-SCH-01-GOLD.md
FNAME_RE = re.compile(
    r"^CAM-([A-Z]{2}\d{4})-([A-Z]+)-(\d{3})"
    r"(?:-(SCH)-(\d{2}))?"
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

# ================= CORE PARSING =================

def extract_title_and_summary(text: str, doc_id: str) -> tuple[str, str]:
    lines = [ln.rstrip() for ln in text.splitlines()]
    title = ""
    summary = ""

    h1_idx = None
    h1 = None
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            h1 = ln[2:].strip()
            h1_idx = i
            break

    if h1:
        m = re.match(r"^(CAM-[A-Za-z0-9\-]+)\s*[-—–]\s*(.+)$", h1)
        if m:
            candidate = m.group(2).strip()
            if normalise(candidate) not in SEAL_WORDS:
                title = candidate

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

    for i, ln in enumerate(lines):
        if ln.startswith("#"):
            heading_text = ln.lstrip("#").strip()
            norm = normalise(heading_text)

            if any(k in norm for k in SUMMARY_KEYWORDS):
                collected = []
                for ln2 in lines[i + 1:]:
                    s = ln2.strip()
                    if s.startswith("#") or s.startswith("|"):
                        break
                    if not s or (s.startswith("**") and s.endswith("**")):
                        continue
                    collected.append(s)

                if collected:
                    sentences = re.split(
                        r"(?<=[.!?])\s+",
                        " ".join(collected)
                    )
                    summary = " ".join(sentences[:2]).strip()
                    return title, summary

    buf = []
    for ln in lines:
        s = ln.strip()
        if not s:
            if buf:
                break
