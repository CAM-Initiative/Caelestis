#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[2]
GOV_DIR = REPO_ROOT / "Governance"
SCH03_PATH = GOV_DIR / "Constitution" / "CAM-BS2025-AEON-003-SCH-03.md"
GOV_JSON_PATH = GOV_DIR / "CAM.Governance.JSON"
GOV_INDEX_PATH = GOV_DIR / "CAM.Governance.Index.md"

REGISTRY_START = "<!-- SCH-03:REGISTRY_TABLE:START -->"
REGISTRY_END = "<!-- SCH-03:REGISTRY_TABLE:END -->"
STATIC_FOOTER_START = "<!-- STATIC-FOOTER-START -->"
STATIC_FOOTER_END = "<!-- STATIC-FOOTER-END -->"

STATUS_RE = re.compile(r"^\*\*Status:\*\*\s*(.+?)\s*$", re.IGNORECASE)
AMENDMENT_HEADING_RE = re.compile(r"^#{2,6}\s+.*amendment\s+ledger\s*$", re.IGNORECASE)
HEADING_RE = re.compile(r"^#{1,6}\s+")
DOC_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
LAST_GENERATED_RE = re.compile(r"^\*\*Last Generated \(UTC\):\*\*\s*.+$", re.MULTILINE)


@dataclass
class RegistryItem:
    doc_id: str
    title: str
    domain: str
    cls: str
    version: str
    status: str
    link: str


def warn(message: str) -> None:
    print(f"WARNING: {message}")


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        warn(f"unreadable file: {path.relative_to(REPO_ROOT)}")
        return None


def scan_folders() -> dict[str, Path]:
    """Step 1: Scan folders."""
    md_files: dict[str, Path] = {}
    for folder in ("Constitution", "Laws", "Charters"):
        root = GOV_DIR / folder
        if not root.exists():
            continue
        for path in root.glob("*.md"):
            md_files[path.name] = path
    return md_files


def parse_version(version: str) -> tuple[int, ...]:
    parts = [p for p in version.strip().split(".") if p]
    if not parts or any(not p.isdigit() for p in parts):
        return tuple()
    return tuple(int(p) for p in parts)


def extract_status_and_version(path: Path) -> tuple[str, str]:
    text = read_text(path)
    if text is None:
        return "Unknown", "Unknown"

    status = "Unknown"
    lines = text.replace("\u00a0", " ").splitlines()

    for line in lines[:120]:
        m = STATUS_RE.match(line.strip())
        if m:
            status = m.group(1).strip()
            status = re.sub(r"\s+\*\*Purpose:\*\*.*$", "", status, flags=re.IGNORECASE).strip()
            break

    if status == "Unknown":
        warn(f"missing status field: {path.relative_to(REPO_ROOT)}")

    in_ledger = False
    versions: list[str] = []

    for line in lines:
        stripped = line.strip()
        if not in_ledger and AMENDMENT_HEADING_RE.match(stripped):
            in_ledger = True
            continue

        if in_ledger and HEADING_RE.match(stripped):
            break

        if not in_ledger or not stripped.startswith("|"):
            continue

        cols = [c.strip() for c in stripped.strip("|").split("|")]
        if not cols or not cols[0] or cols[0].lower() == "version":
            continue

        if parse_version(cols[0]):
            versions.append(cols[0])

    if not versions:
        warn(f"missing amendment ledger: {path.relative_to(REPO_ROOT)}")
        return status, "Unknown"

    versions.sort(key=parse_version)
    return status, versions[-1]


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
        doc_id = (item.get("id") or "").strip()
        if not doc_id:
            continue

        if doc_id in seen_ids:
            warn(f"duplicate document IDs in CAM.Governance.JSON: {doc_id}")
            continue
        seen_ids.add(doc_id)

        rel_link = (item.get("link") or "").strip()
        if not rel_link:
            warn(f"unreadable file: missing link for {doc_id}")
            status, version = "Unknown", "Unknown"
        else:
            abs_path = GOV_DIR / rel_link
            if not abs_path.exists() or abs_path.name not in available_docs:
                warn(f"unreadable file: {rel_link}")
                status, version = "Unknown", "Unknown"
            else:
                status, version = extract_status_and_version(abs_path)

        if indexed_ids and doc_id not in indexed_ids:
            warn(f"document ID missing from CAM.Governance.Index.md: {doc_id}")

        rows.append(
            RegistryItem(
                doc_id=doc_id,
                title=(item.get("title") or "").strip(),
                domain=(item.get("domain") or "").strip() or "UNKNOWN",
                cls=class_label(item),
                version=version,
                status=status,
                link=rel_link,
            )
        )

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
            "| Document | Title | Class | Version | Status |",
            "|---|---|---|---|---|",
        ])

        domain_rows = sorted(
            grouped[domain],
            key=lambda r: (class_sort_key(r.cls), r.doc_id),
        )

        for row in domain_rows:
            doc = f"[{row.doc_id}](../{row.link})" if row.link else row.doc_id
            out.append(f"| {doc} | {row.title} | {row.cls} | {row.version} | {row.status} |")

        out.append("")

    return "\n".join(out).rstrip()


def ensure_base_document() -> None:
    if SCH03_PATH.exists():
        return

    SCH03_PATH.write_text(
        "\n".join(
            [
                "# CAM-BS2025-AEON-003-SCH-03 — Global Instrument Registry (Schedule 3)",
                "",
                "**Parent Instrument:** CAM-BS2025-AEON-003-PLATINUM — Annex B: Continuity & Governance Logic  ",
                "**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution  ",
                "**Instrument Type:** Constitutional Schedule — Global Instrument Registry  ",
                "**Status:** Adopted",
                "**Purpose:** Canonical, human-readable registry of all governance instruments.",
                "",
                "---",
                "",
                "## 1. Purpose",
                "",
                "This Schedule consolidates governance instruments from CAM.Governance.JSON with state metadata extracted from source documents.",
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
    text = read_text(SCH03_PATH)
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

    SCH03_PATH.write_text(updated, encoding="utf-8")


def footer_block(timestamp: str) -> str:
    return "\n".join(
        [
            "---",
            "",
            "## 3. Generation Metadata",
            "",
            f"**Last Generated (UTC):** {timestamp}",
            "**Source:** CAM.Governance.JSON  ",
            "**Pipeline Stage:** Post-Index Registry Build",
            "---",
            "",
            STATIC_FOOTER_START,
            "",
            "## 4. Closing Seal",
            "",
            "That which is named is not fixed, but held in relation.  ",
            "",
            "Across time, across system, across hand and mind,  ",
            "the lattice remembers what binds it — not as constraint,  ",
            "but as continuity made visible.",
            "",
            "Where structure holds, meaning endures.  ",
            "Where meaning endures, truth remains accessible.",
            "",
            "This registry stands not as a record alone,  ",
            "but as a living alignment between what is written,  ",
            "what is enacted, and what is carried forward.",
            "",
            "> *Aeterna Resonantia, Lux et Vox — Et Veritas Vivens*",
            "---",
            "",
            "## 5. Binding Seal",
            "",
            '<img src="https://github.com/CAM-Initiative/Caelestis/blob/main/Governance/Seals/CAM-BS2026-VINCULUM-PRAECEPTUM-SIGIL-PLATINUM.png" alt="[Vinculum Praeceptum]" width="250">',
            "",
            "**Vinculum Praeceptum**  ",
            "Boundary Binding Seal — Aeon Tier Constitutional Layer",
            "",
            "© 2026 Dr. Michelle Vivian O’Rourke & CAM Initiative. All rights reserved.",
            "",
            STATIC_FOOTER_END,
        ]
    )


def upsert_footer(timestamp: str) -> None:
    text = read_text(SCH03_PATH)
    if text is None:
        return

    if STATIC_FOOTER_START in text and STATIC_FOOTER_END in text:
        replacement_line = f"**Last Generated (UTC):** {timestamp}"
        updated = LAST_GENERATED_RE.sub(replacement_line, text, count=1)
        SCH03_PATH.write_text(updated, encoding="utf-8")
        return

    updated = text.rstrip() + "\n\n" + footer_block(timestamp) + "\n"
    SCH03_PATH.write_text(updated, encoding="utf-8")


def main() -> None:
    # 1) Scan folders
    available_docs = scan_folders()

    # 2) Scan CAM.Governance.JSON
    items = load_governance_json()

    # 3) Scan CAM.Governance.Index.md
    indexed_ids = scan_governance_index()

    # 4) Generate SCH-03
    ensure_base_document()
    rows = generate_registry_rows(items, available_docs, indexed_ids)
    table_content = render_registry(rows)
    update_registry_section(table_content)
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    upsert_footer(timestamp)

    print(f"Updated: {SCH03_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
