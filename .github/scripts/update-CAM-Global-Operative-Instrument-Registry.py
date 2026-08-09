#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))


import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from instrument_state import extract_instrument_metadata, extract_status_and_version

GOV_DIR = REPO_ROOT / "Governance"
REGISTRY_PATH = GOV_DIR / "CAM.Global.Operative.Instrument.Registry.md"
GOV_JSON_PATH = GOV_DIR / "CAM.Governance.JSON"
GOV_INDEX_PATH = GOV_DIR / "CAM.Governance.Index.md"

OPERATIVE_STATUSES = {"active", "adopted"}

REGISTRY_START = "<!-- GLOBAL-OPERATIVE-INSTRUMENT-REGISTRY:START -->"
REGISTRY_END = "<!-- GLOBAL-OPERATIVE-INSTRUMENT-REGISTRY:END -->"
STATIC_FOOTER_START = "<!-- STATIC-FOOTER-START -->"
STATIC_FOOTER_END = "<!-- STATIC-FOOTER-END -->"

DOC_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def normalize_cell_text(value: str) -> str:
    cleaned = re.sub(r"^\s*\*+\s*", "", value)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


@dataclass
class RegistryItem:
    doc_id: str
    title: str
    domain: str
    cls: str
    parent_source: str
    instrument_class: str
    version: str
    status: str
    effect: str
    enforcement: str
    review_state: str
    authority_role: str
    source_authority: str
    link: str


def warn(message: str) -> None:
    print(f"WARNING: {message}")


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        warn(f"unreadable file: {path.relative_to(REPO_ROOT)}")
        return None


def fail(message: str) -> None:
    raise RuntimeError(message)


def normalized_metadata_value(value: object) -> str:
    return normalize_cell_text(str(value or "")).lower()


def is_current_operative_item(item: dict) -> bool:
    link = str(item.get("link") or "").strip()
    return (
        normalized_metadata_value(item.get("status")) in OPERATIVE_STATUSES
        and normalized_metadata_value(item.get("effect")) != "archival"
        and link != ""
        and not link.startswith("Drafts/")
    )


def scan_folders() -> dict[str, Path]:
    """Step 1: Scan folders."""
    md_files: dict[str, Path] = {}
    for folder in ("Constitution", "Laws", "Charters", "Standards"):
        root = GOV_DIR / folder
        if not root.exists():
            continue
        for path in root.glob("*.md"):
            md_files[path.name] = path
    return md_files


def load_governance_json() -> list[dict]:
    """Step 2: Scan CAM.Governance.JSON."""
    payload_text = read_text(GOV_JSON_PATH)
    if payload_text is None:
        return []
    try:
        payload = json.loads(payload_text)
    except json.JSONDecodeError:
        warn(f"invalid JSON: {GOV_JSON_PATH.relative_to(REPO_ROOT)}")
        return []
    return payload.get("items", [])


def scan_governance_index() -> set[str]:
    """Step 3: Scan CAM.Governance.Index.md."""
    text = read_text(GOV_INDEX_PATH)
    if text is None:
        return set()

    ids: set[str] = set()
    seen_dupes: set[str] = set()

    for line in text.splitlines():
        if "| [" not in line:
            continue
        m = DOC_LINK_RE.search(line)
        if not m:
            continue
        doc_id = m.group(1).strip()
        if doc_id in ids and doc_id not in seen_dupes:
            warn(f"duplicate document IDs in CAM.Governance.Index.md: {doc_id}")
            seen_dupes.add(doc_id)
        ids.add(doc_id)
    return ids


def class_label(item: dict) -> str:
    hierarchy = (item.get("hierarchy_type") or "").strip().lower()
    if not hierarchy:
        return "Root"
    return hierarchy.capitalize()


def class_sort_key(cls: str) -> tuple[int, str]:
    order = {
        "root": 0,
        "appendix": 1,
        "annex": 2,
        "supplement": 3,
        "schedule": 4,
    }
    key = cls.strip().lower()
    return order.get(key, 99), key


def generate_registry_rows(items: Iterable[dict], available_docs: dict[str, Path], indexed_ids: set[str]) -> list[RegistryItem]:
    rows: list[RegistryItem] = []
    seen_ids: set[str] = set()

    for item in items:
        if not is_current_operative_item(item):
            continue

        doc_id = (item.get("id") or "").strip()
        if not doc_id:
            continue

        if doc_id in seen_ids:
            warn(f"duplicate document IDs in CAM.Governance.JSON: {doc_id}")
            continue
        seen_ids.add(doc_id)

        rel_link = (item.get("link") or "").strip()
        status = normalize_cell_text((item.get("status") or "").strip())
        effect = normalize_cell_text((item.get("effect") or "").strip())
        enforcement = normalize_cell_text((item.get("enforcement") or "").strip())
        review_state = normalize_cell_text((item.get("review_state") or "").strip())
        authority_role = normalize_cell_text((item.get("authority_role") or "").strip())
        source_authority = normalize_cell_text((item.get("source_authority") or "").strip())
        version = (item.get("version") or "").strip()
        instrument_class = (item.get("instrument_class") or "").strip().lower()
        parent_source = (item.get("parent_id") or item.get("constitutional_source") or "").strip()

        if not rel_link:
            warn(f"unreadable file: missing link for {doc_id}")
            status = status or "Unknown"
            version = version or "Unknown"
        else:
            abs_path = GOV_DIR / rel_link
            if not abs_path.exists() or abs_path.name not in available_docs:
                warn(f"unreadable file: {rel_link}")
                status = status or "Unknown"
                version = version or "Unknown"
            else:
                # Always read canonical metadata from source documents.
                # This avoids stale Version/Status values when CAM.Governance.JSON
                # has not yet been refreshed in the current run.
                extracted_status, extracted_version = extract_status_and_version(abs_path)
                metadata = extract_instrument_metadata(abs_path)
                status = normalize_cell_text(extracted_status) if extracted_status != "Unknown" else (status or "Unknown")
                version = extracted_version if extracted_version != "Unknown" else (version or "Unknown")
                effect = normalize_cell_text(metadata.get("effect", effect))
                enforcement = normalize_cell_text(metadata.get("enforcement", enforcement))
                review_state = normalize_cell_text(metadata.get("review_state", review_state))
                authority_role = normalize_cell_text(metadata.get("authority_role", authority_role))
                source_authority = normalize_cell_text(metadata.get("source_authority", source_authority))

        if indexed_ids and doc_id not in indexed_ids:
            warn(f"document ID missing from CAM.Governance.Index.md: {doc_id}")

        rows.append(
            RegistryItem(
                doc_id=doc_id,
                title=(item.get("title") or "").strip(),
                domain=(item.get("domain") or "").strip() or "UNKNOWN",
                cls=class_label(item),
                parent_source=parent_source,
                instrument_class=instrument_class,
                version=version,
                status=status,
                effect=effect,
                enforcement=enforcement,
                review_state=review_state,
                authority_role=authority_role,
                source_authority=source_authority,
                link=rel_link,
            )
        )

    for row in rows:
        if row.instrument_class == "law" or "/laws/" in row.link.lower() or "-law-" in row.doc_id.lower():
            row.parent_source = row.parent_source or "Pre-constitutional Law"
        elif not row.parent_source:
            row.parent_source = "— (root)"

        required = {
            "status": row.status,
            "effect": row.effect,
            "governance standard": row.enforcement,
            "review state": row.review_state,
            "authority role": row.authority_role,
            "source authority": row.source_authority,
        }
        missing = [name for name, value in required.items() if not value or value == "Unknown"]
        if missing:
            fail(f"missing controlled metadata for {row.doc_id}: {', '.join(missing)}")

    return rows


def render_registry(rows: list[RegistryItem]) -> str:
    grouped: dict[str, list[RegistryItem]] = defaultdict(list)
    for row in rows:
        grouped[row.domain].append(row)

    def domain_sort_key(domain: str) -> tuple[int, str]:
        if domain.strip().lower() == "aeon tier constitution":
            return (0, domain.lower())
        return (1, domain.lower())

    out: list[str] = []
    for domain in sorted(grouped.keys(), key=domain_sort_key):
        out.extend([
            f"## {domain}",
            "",
            "| Document | Title | Class | Parent / Source | Version | Status | Effect | Governance Standard | Review State | Authority Role | Source Authority | Disposition |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|",
        ])

        domain_rows = sorted(
            grouped[domain],
            key=lambda r: (class_sort_key(r.cls), r.doc_id),
        )

        for row in domain_rows:
            doc = f"[{row.doc_id}]({row.link})" if row.link else row.doc_id
            out.append(
                f"| {doc} | {row.title} | {row.cls} | {row.parent_source} | {row.version} | "
                f"{row.status} | {row.effect} | {row.enforcement} | {row.review_state} | "
                f"{row.authority_role} | {row.source_authority} | Operative |"
            )

        out.append("")

    return "\n".join(out).rstrip()


def ensure_base_document() -> None:
    if REGISTRY_PATH.exists():
        return

    REGISTRY_PATH.write_text(
        "\n".join(
            [
                "# Global Operative-Instrument Registry",
                "",
                "**Specification authority:** CAM-EQ2026-OPERATIONS-001-SUP-04 §11.1  ",
                "**Status:** Deterministic generated projection; not an independent governance instrument  ",
                "**Historical source:** CAM-BS2025-AEON-003-SCH-03 (retired)",
                "",
                "---",
                "",
                "## 1. Purpose",
                "",
                "This generated registry consolidates operative governance instruments from CAM.Governance.JSON with controlled state metadata extracted from governed source documents. Registry presence or aggregation creates no governance authority, execution order, lifecycle state or canonical declaration.",
                "",
                "## 2. Registry",
                "",
                REGISTRY_START,
                REGISTRY_END,
                "",
            ]
        ),
        encoding="utf-8",
    )


def update_registry_section(table_content: str) -> None:
    text = read_text(REGISTRY_PATH)
    if text is None:
        return

    if REGISTRY_START not in text or REGISTRY_END not in text:
        text = text.rstrip() + "\n\n## 2. Registry\n\n" + REGISTRY_START + "\n" + REGISTRY_END + "\n"

    pattern = re.compile(
        rf"{re.escape(REGISTRY_START)}.*?{re.escape(REGISTRY_END)}",
        re.DOTALL,
    )
    replacement = f"{REGISTRY_START}\n{table_content}\n{REGISTRY_END}"
    updated = pattern.sub(replacement, text)

    REGISTRY_PATH.write_text(updated, encoding="utf-8")


def metadata_block() -> str:
    return "\n".join(
        [
            "---",
            "",
            "## 3. Generation Metadata",
            "",
            "**Generation:** Deterministic (timestamp omitted)  ",
            "**Source:** CAM.Governance.JSON  ",
            "**Pipeline Stage:** Post-Index Registry Build  ",
            "",
            "---",
            "",
            "",
        ]
    )


def upsert_footer() -> None:
    text = read_text(REGISTRY_PATH)
    if text is None:
        return

    metadata_heading = text.find("\n---\n\n## 3. Generation Metadata")
    if metadata_heading != -1:
        updated = text[:metadata_heading].rstrip() + "\n\n" + metadata_block()
    else:
        updated = text.rstrip() + "\n\n" + metadata_block()
    REGISTRY_PATH.write_text(updated, encoding="utf-8")


def main() -> None:
    # 1) Scan folders
    available_docs = scan_folders()

    # 2) Scan CAM.Governance.JSON
    items = load_governance_json()

    # 3) Scan CAM.Governance.Index.md
    indexed_ids = scan_governance_index()

    # 4) Generate the non-authoritative operative-instrument projection.
    ensure_base_document()
    rows = generate_registry_rows(items, available_docs, indexed_ids)
    table_content = render_registry(rows)
    update_registry_section(table_content)
    upsert_footer()

    print(f"Updated: {REGISTRY_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
