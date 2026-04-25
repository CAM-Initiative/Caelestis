#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))


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
    domain_source: str
    governance_layer: str
    governance_layer_source: str
    runtime_layer: str
    runtime_layer_source: str


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


def normalize_label(text: str) -> str:
    cleaned = text.strip()
    cleaned = re.sub(r"[*_`]", "", cleaned)
    cleaned = cleaned.replace("—", "-").replace("–", "-").replace("‑", "-")
    cleaned = re.sub(r"\\", "", cleaned)
    cleaned = re.sub(r"[^A-Za-z0-9\-\s]", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip().lower()


def extract_json_runtime_layer(item: dict) -> str | None:
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


def parse_metadata_table_rows(markdown: str) -> tuple[dict[str, str], bool]:
    headings = list(re.finditer(r"(?m)^(#{2,6})\s+(.+?)\s*$", markdown))
    normalized_rows: dict[str, str] = {}
    found_relevant_table = False

    for idx, heading in enumerate(headings):
        heading_text = heading.group(2)
        normalized_heading = normalize_label(heading_text)
        is_relevant = any(
            token in normalized_heading
            for token in ("lineage", "metadata", "provenance", "record keeping", "classification")
        )
        if not is_relevant:
            continue

        section_start = heading.end()
        section_end = headings[idx + 1].start() if idx + 1 < len(headings) else len(markdown)
        section = markdown[section_start:section_end]

        for line in section.splitlines():
            stripped = line.strip()
            if not stripped.startswith("|") or stripped.count("|") < 3:
                continue

            cols = [col.strip() for col in stripped.strip("|").split("|")]
            if len(cols) < 2:
                continue
            if cols[0].strip().lower() == "field":
                continue
            if re.fullmatch(r":?-{2,}:?", cols[0].strip()):
                continue
            if re.fullmatch(r":?-{2,}:?", cols[1].strip()):
                continue

            found_relevant_table = True
            normalized_rows[normalize_label(cols[0])] = cols[1].strip()

    return normalized_rows, found_relevant_table


def infer_domain(item: dict, instrument_id: str) -> str:
    parent_id = str(item.get("parent_id") or "").strip()
    if parent_id:
        parts = parent_id.split("-")
        if len(parts) >= 4 and parts[2]:
            return parts[2]

    parts = instrument_id.split("-")
    if len(parts) >= 4 and parts[2]:
        return parts[2]

    return str(item.get("domain") or "").strip() or "UNKNOWN"


def extract_domain(item: dict, instrument_id: str, markdown_rows: dict[str, str]) -> tuple[str, str]:
    domain = markdown_rows.get("domain")
    if domain:
        return domain, "metadata:Domain"

    domain_layer = markdown_rows.get("domain layer")
    if domain_layer:
        return domain_layer, "metadata:Domain Layer"

    domain_namespace = markdown_rows.get("domain namespace")
    if domain_namespace:
        return domain_namespace, "metadata:Domain Namespace"

    return infer_domain(item, instrument_id), "fallback:inferred"


def extract_governance_layer(markdown_rows: dict[str, str]) -> tuple[str, str]:
    governance_layer = markdown_rows.get("governance layer")
    if governance_layer:
        return governance_layer, "metadata:Governance Layer"

    activation_mode = markdown_rows.get("activation mode")
    if activation_mode:
        return activation_mode, "metadata:Activation Mode"

    return "UNSPECIFIED", "fallback:UNSPECIFIED"


def governance_layer_fallback_for_schedule(instrument_id: str) -> tuple[str, str] | None:
    fallback_map = {
        "CAM-BS2025-AEON-003-SCH-03": ("Passive (Registry)", "fallback:policy-map"),
    }
    return fallback_map.get(instrument_id)


def extract_runtime_layer(item: dict, markdown_rows: dict[str, str]) -> tuple[str, str]:
    runtime_layer = markdown_rows.get("runtime layer")
    if runtime_layer:
        return runtime_layer, "metadata:Runtime Layer"

    runtime_role = markdown_rows.get("runtime role")
    if runtime_role:
        return runtime_role, "metadata:Runtime Role"

    runtime_authority = markdown_rows.get("runtime authority")
    if runtime_authority:
        return runtime_authority, "metadata:Runtime Authority"

    json_runtime_layer = extract_json_runtime_layer(item)
    if json_runtime_layer:
        return json_runtime_layer, "json"

    return "UNBOUND", "fallback:UNBOUND"


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

        rel_link = (item.get("link") or "").strip()
        markdown_rows: dict[str, str] = {}
        found_metadata_table = False
        if rel_link:
            markdown_path = GOV_DIR / rel_link
            if markdown_path.exists():
                markdown_rows, found_metadata_table = parse_metadata_table_rows(read_text(markdown_path))
            else:
                warn(f"{instrument_id} | {rel_link} | missing file for metadata extraction")

        domain, domain_source = extract_domain(item, instrument_id, markdown_rows)
        governance_layer, governance_layer_source = extract_governance_layer(markdown_rows)
        if governance_layer == "UNSPECIFIED":
            mapped = governance_layer_fallback_for_schedule(instrument_id)
            if mapped is not None:
                governance_layer, governance_layer_source = mapped
        runtime_layer, runtime_layer_source = extract_runtime_layer(item, markdown_rows)

        if found_metadata_table and "domain" not in markdown_rows and "domain layer" not in markdown_rows:
            warn(f"{instrument_id} | {rel_link or 'NO_PATH'} | missing field: Domain/Domain Layer")
        if (
            found_metadata_table
            and "runtime layer" not in markdown_rows
            and "runtime role" not in markdown_rows
            and "runtime authority" not in markdown_rows
        ):
            warn(f"{instrument_id} | {rel_link or 'NO_PATH'} | missing field: Runtime Layer/Runtime Role/Runtime Authority")
        if runtime_layer == "UNBOUND":
            warn(f"Runtime Layer is UNBOUND for {instrument_id}")

        rows.append(
            RuntimeRegistryItem(
                instrument_id=instrument_id,
                title=str(item.get("title") or "").strip() or "UNKNOWN",
                domain=domain,
                version=str(item.get("version") or "").strip() or "UNKNOWN",
                status=str(item.get("status") or "").strip() or "UNKNOWN",
                domain_source=domain_source,
                governance_layer=governance_layer,
                governance_layer_source=governance_layer_source,
                runtime_layer=runtime_layer,
                runtime_layer_source=runtime_layer_source,
            )
        )

    if duplicates:
        dupes = ", ".join(sorted(duplicates))
        fail(f"duplicate instrument IDs detected in CAM.Governance.JSON: {dupes}")

    rows.sort(key=lambda r: (r.runtime_layer.lower(), r.domain.lower(), r.instrument_id.lower()))
    return rows


def render_registry(rows: list[RuntimeRegistryItem], timestamp: str) -> str:
    lines = [
        "| Instrument ID | Instrument Name | Domain | Governance Layer | Runtime Layer |",
        "|---------------|----------------|--------|------------------|----------------|",
    ]

    for row in rows:
        lines.append(
            f"| {row.instrument_id} | {row.title} | {row.domain} | {row.governance_layer} | {row.runtime_layer} |"
        )

    lines.extend(
        [
            "",
            f"**Last Generated (UTC):** {timestamp}",
            "**Source:** CAM.Governance.JSON",
            "**Pipeline Stage:** Runtime Registry Build",
        ]
    )

    return "\n".join(lines)


def render_audit(rows: list[RuntimeRegistryItem]) -> str:
    lines = [
        "| Instrument ID | Domain | Governance Layer | Runtime Layer | Domain Source | Governance Source | Runtime Source |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row.instrument_id} | {row.domain} | {row.governance_layer} | {row.runtime_layer} | {row.domain_source} | {row.governance_layer_source} | {row.runtime_layer_source} |"
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
    audit_mode = "--audit" in sys.argv
    items = load_governance_items()
    rows = build_rows(items)
    if audit_mode:
        print(render_audit(rows))
        return

    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    block = render_registry(rows, timestamp)
    update_registry_block(block)
    print(f"Updated: {SCH01_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
