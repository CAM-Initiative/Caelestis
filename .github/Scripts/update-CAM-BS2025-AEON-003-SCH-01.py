#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GOV_DIR = REPO_ROOT / "Governance"
GOV_JSON_PATH = GOV_DIR / "CAM.Governance.JSON"
SCH01_PATH = GOV_DIR / "Constitution" / "CAM-BS2025-AEON-003-SCH-01.md"

REGISTRY_START = "<!-- SCH-01:RUNTIME_REGISTRY:START -->"
REGISTRY_END = "<!-- SCH-01:RUNTIME_REGISTRY:END -->"


@dataclass(frozen=True)
class RuntimeRegistryItem:
    instrument_id: str
    title: str
    domain: str
    version: str
    status: str
    runtime_layer: str


def warn(message: str) -> None:
    print(f"WARNING: {message}")


def fail(message: str) -> None:
    raise RuntimeError(message)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:
        fail(f"unreadable file: {path.relative_to(REPO_ROOT)} ({exc})")


def load_governance_items() -> list[dict]:
    payload = json.loads(read_text(GOV_JSON_PATH))
    items = payload.get("items", [])
    if not isinstance(items, list):
        fail(f"invalid items payload in: {GOV_JSON_PATH.relative_to(REPO_ROOT)}")
    return items


def from_metadata(item: dict) -> str | None:
    # Preferred: explicit runtime layer fields in CAM.Governance.JSON
    direct_keys = ("runtime_layer", "runtimeLayer", "Runtime Layer", "RuntimeLayer")
    for key in direct_keys:
        value = item.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()

    metadata = item.get("metadata")
    if isinstance(metadata, dict):
        for key in direct_keys:
            value = metadata.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()

    return None


def find_lineage_section(markdown: str) -> str:
    header = re.search(r"(?im)^##+\s+[^\n]*Lineage\s*&\s*Metadata[^\n]*$", markdown)
    if not header:
        return ""

    start = header.end()
    rest = markdown[start:]
    nxt = re.search(r"(?m)^##+\s+", rest)
    end = start + nxt.start() if nxt else len(markdown)
    return markdown[start:end]


def from_markdown_lineage(markdown: str) -> str | None:
    section = find_lineage_section(markdown)
    if not section:
        return None

    table_row = re.search(
        r"(?im)^\|\s*\*{0,2}\s*Runtime\s+Layer\s*\*{0,2}\s*\|\s*(.+?)\s*\|\s*$",
        section,
    )
    if table_row:
        return table_row.group(1).strip()

    bullet_decl = re.search(
        r"(?im)^\s*[-*]\s*\*{0,2}\s*Runtime\s+Layer\s*\*{0,2}\s*:\s*(.+?)\s*$",
        section,
    )
    if bullet_decl:
        return bullet_decl.group(1).strip()

    inline_decl = re.search(
        r"(?im)^\s*\*{0,2}\s*Runtime\s+Layer\s*\*{0,2}\s*:\s*(.+?)\s*$",
        section,
    )
    if inline_decl:
        return inline_decl.group(1).strip()

    return None


def extract_runtime_layer(item: dict) -> str:
    metadata_layer = from_metadata(item)
    if metadata_layer:
        return metadata_layer

    rel_link = (item.get("link") or "").strip()
    if not rel_link:
        return "UNBOUND"

    markdown_path = GOV_DIR / rel_link
    if not markdown_path.exists():
        warn(f"missing markdown for runtime-layer lookup: {rel_link}")
        return "UNBOUND"

    runtime_layer = from_markdown_lineage(read_text(markdown_path))
    return runtime_layer or "UNBOUND"


def build_rows(items: list[dict]) -> list[RuntimeRegistryItem]:
    schedule_items = [item for item in items if "-SCH-" in str(item.get("id") or "")]

    seen_ids: set[str] = set()
    duplicates: set[str] = set()
    rows: list[RuntimeRegistryItem] = []

    for item in schedule_items:
        instrument_id = str(item.get("id") or "").strip()
        if not instrument_id:
            continue

        if instrument_id in seen_ids:
            duplicates.add(instrument_id)
            continue
        seen_ids.add(instrument_id)

        runtime_layer = extract_runtime_layer(item)
        if runtime_layer == "UNBOUND":
            warn(f"Runtime Layer is UNBOUND for {instrument_id}")

        rows.append(
            RuntimeRegistryItem(
                instrument_id=instrument_id,
                title=str(item.get("title") or "").strip() or "UNKNOWN",
                domain=str(item.get("domain") or "").strip() or "UNKNOWN",
                version=str(item.get("version") or "").strip() or "UNKNOWN",
                status=str(item.get("status") or "").strip() or "UNKNOWN",
                runtime_layer=runtime_layer,
            )
        )

    if duplicates:
        dupes = ", ".join(sorted(duplicates))
        fail(f"duplicate instrument IDs detected in CAM.Governance.JSON: {dupes}")

    rows.sort(key=lambda r: (r.runtime_layer.lower(), r.domain.lower(), r.instrument_id.lower()))
    return rows


def render_registry(rows: list[RuntimeRegistryItem], timestamp: str) -> str:
    lines = [
        "| Instrument ID | Instrument Name | Domain | Runtime Layer |",
        "|---------------|----------------|--------|----------------|",
    ]

    for row in rows:
        lines.append(
            f"| {row.instrument_id} | {row.title} | {row.domain} | {row.runtime_layer} |"
        )

    lines.extend(
        [
            "",
            f"Last Generated (UTC): {timestamp}",
            "Source: CAM.Governance.JSON",
            "Pipeline Stage: Runtime Registry Build",
        ]
    )

    return "\n".join(lines)


def update_registry_block(table_block: str) -> None:
    text = read_text(SCH01_PATH)

    if REGISTRY_START not in text or REGISTRY_END not in text:
        fail(f"missing runtime registry markers in {SCH01_PATH.relative_to(REPO_ROOT)}")

    pattern = re.compile(
        rf"{re.escape(REGISTRY_START)}.*?{re.escape(REGISTRY_END)}",
        re.DOTALL,
    )
    updated = pattern.sub(f"{REGISTRY_START}\n{table_block}\n{REGISTRY_END}", text)
    SCH01_PATH.write_text(updated, encoding="utf-8")


def main() -> None:
    items = load_governance_items()
    rows = build_rows(items)
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    block = render_registry(rows, timestamp)
    update_registry_block(block)
    print(f"Updated: {SCH01_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
