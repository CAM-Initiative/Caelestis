from __future__ import annotations

import hashlib
import re
import unicodedata
from pathlib import Path

META_LINE_RE = re.compile(r"^\s*(?:\*\*)?\s*([A-Za-z][A-Za-z ]*[A-Za-z])\s*:\s*(.+?)\s*(?:\*\*)?\s*$")
AMENDMENT_HEADING_RE = re.compile(r"amendment\s+ledger", re.IGNORECASE)
VERSION_RE = re.compile(r"\d+(?:\.\d+)+")
VERSION_META_RE = re.compile(r"^\*\*Version:\*\*\s*(.+?)\s*$", re.IGNORECASE)


def parse_version(version: str) -> tuple[int, ...]:
    parts = [p for p in version.strip().split(".") if p]
    if not parts or any(not p.isdigit() for p in parts):
        return tuple()
    return tuple(int(p) for p in parts)


def _normalise_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    return text.replace("\u00a0", " ").replace("\u200b", "").replace("\ufeff", "")


def compute_full_document_sha256(text: str) -> str:
    """Return SHA-256 for the full, post-modification document content."""
    normalised = _normalise_text(text)
    return hashlib.sha256(normalised.encode("utf-8")).hexdigest()


def extract_status_and_version(path: Path) -> tuple[str, str]:
    text = _normalise_text(path.read_text(encoding="utf-8"))
    lines = text.splitlines()

    status = "Unknown"
    version_from_header = "Unknown"
    metadata = extract_instrument_metadata(path)
    if metadata.get("status"):
        status = metadata["status"]

    for line in lines[:160]:
        stripped = line.strip()

        if version_from_header == "Unknown":
            m_version = VERSION_META_RE.match(stripped)
            if m_version:
                vm = VERSION_RE.search(m_version.group(1))
                if vm and parse_version(vm.group(0)):
                    version_from_header = vm.group(0)

        if status != "Unknown" and version_from_header != "Unknown":
            break

    in_ledger = False
    versions: list[str] = []
    for line in lines:
        stripped = line.strip()

        if stripped.startswith("#") and AMENDMENT_HEADING_RE.search(stripped):
            in_ledger = True
            continue

        if in_ledger and stripped.startswith("##") and not AMENDMENT_HEADING_RE.search(stripped):
            # relaxed: stop at first sibling section, keep parsing within amendment subsections
            break

        if not in_ledger:
            continue

        if "|" in stripped:
            cols = [c.strip() for c in stripped.strip("|").split("|")]
            if not cols:
                continue
            if cols[0].lower() == "version":
                continue
            candidate = cols[0]
            if parse_version(candidate):
                versions.append(candidate)
                continue
            vm = VERSION_RE.search(candidate)
            if vm and parse_version(vm.group(0)):
                versions.append(vm.group(0))
        else:
            # relaxed fallback: allow plain bullet/line entries such as "- v1.2.3"
            vm = VERSION_RE.search(stripped)
            if vm and parse_version(vm.group(0)):
                versions.append(vm.group(0))

    latest_version = "Unknown"
    if versions:
        latest_version = sorted(versions, key=parse_version)[-1]
    elif version_from_header != "Unknown":
        latest_version = version_from_header

    return status or "Unknown", latest_version


def extract_instrument_metadata(path: Path) -> dict[str, str]:
    text = _normalise_text(path.read_text(encoding="utf-8"))
    lines = text.splitlines()

    key_map = {
        "status": "status",
        "effect": "effect",
        "enforcement": "enforcement",
        "review state": "review_state",
        "authority role": "authority_role",
    }
    out: dict[str, str] = {}
    for line in lines[:220]:
        stripped = line.rstrip()
        if not stripped:
            continue
        m = META_LINE_RE.match(stripped)
        if not m:
            continue
        key = re.sub(r"\s+", " ", m.group(1).strip().lower())
        if key not in key_map:
            continue
        value = m.group(2).strip().rstrip()
        value = re.sub(r"\s{2,}$", "", value)
        value = re.sub(r"\s{2,}", " ", value)
        if value and key_map[key] not in out:
            out[key_map[key]] = value
    return out


def extract_status_hash_and_version(path: Path) -> tuple[str, str, str]:
    status, version = extract_status_and_version(path)
    text = _normalise_text(path.read_text(encoding="utf-8"))
    content_hash = compute_full_document_sha256(text)
    return status, content_hash, version


def extract_status__HASH_and_version(path: Path) -> tuple[str, str, str]:
    """Compatibility wrapper with requested naming."""
    return extract_status_hash_and_version(path)
