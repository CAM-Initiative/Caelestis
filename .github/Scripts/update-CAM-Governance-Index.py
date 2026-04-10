#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GOV_DIR = REPO_ROOT / "Governance"
OUT_MD = GOV_DIR / "CAM.Governance.Index.md"
OUT_JSON = GOV_DIR / "CAM.Governance.JSON"

SOURCES = [
    ("constitution", GOV_DIR / "Constitution" / "constitution.index.json", "Constitution"),
    ("law", GOV_DIR / "Laws" / "laws.index.json", "Laws"),
    ("charter", GOV_DIR / "Charters" / "charters.index.json", "Charters"),
]


def load_items() -> list[dict]:
    rows: list[dict] = []
    for default_class, src, subdir in SOURCES:
        if not src.exists():
            continue
        payload = json.loads(src.read_text(encoding="utf-8"))
        for item in payload.get("items", []):
            row = dict(item)
            row["instrument_class"] = row.get("instrument_class") or default_class
            row["purpose"] = (row.get("purpose") or row.get("summary") or "").strip()
            link_name = (row.get("link") or "").strip()
            if link_name:
                row["link"] = f"{subdir}/{link_name}"
            rows.append(row)

    rows.sort(key=lambda x: x.get("id", ""))
    return rows


def render_md(items: list[dict]) -> str:
    generated = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    out: list[str] = [
        "# CAM Governance Index",
        "",
        f"Generated: {generated}",
        "",
        "## Constitution & Instruments",
        "",
    ]

    def render_table(table_items: list[dict]) -> None:
        out.extend([
            "| ID | Class | Hierarchy | Parent | Document | Title | Purpose |",
            "|---|---|---|---|---|---|---|",
        ])
        for it in table_items:
            link = it.get("link", "")
            link_md = f"[{it.get('id', '')}]({link})" if link else ""
            out.append(
                "| {id} | {instrument_class} | {hierarchy} | {parent} | {link_md} | {title} | {purpose} |".format(
                    id=it.get("id", ""),
                    instrument_class=it.get("instrument_class", ""),
                    hierarchy=it.get("hierarchy_type") or "root",
                    parent=it.get("parent_id") or "",
                    link_md=link_md,
                    title=it.get("title", ""),
                    purpose=it.get("purpose", ""),
                )
            )
        out.append("")

    constitution_items = [it for it in items if it.get("instrument_class") == "constitution"]
    render_table(constitution_items)

    domain_items = [it for it in items if it.get("instrument_class") != "constitution"]
    domain_names = sorted({it.get("domain", "") for it in domain_items if it.get("domain")})

    for domain in domain_names:
        out.extend([f"## Domain: {domain}", ""])
        domain_group = [it for it in domain_items if it.get("domain") == domain]
        domain_group.sort(key=lambda x: x.get("id", ""))
        render_table(domain_group)

    return "\n".join(out).rstrip() + "\n"


def write_json(items: list[dict]) -> None:
    normalized_items: list[dict] = []
    for item in items:
        row = dict(item)
        row["purpose"] = (row.get("purpose") or row.get("summary") or "").strip()
        normalized_items.append(row)

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "count": len(normalized_items),
        "items": normalized_items,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    items = load_items()
    OUT_MD.write_text(render_md(items), encoding="utf-8")
    write_json(items)
    print(f"Updated: {OUT_MD}")
    print(f"Wrote:   {OUT_JSON}")


if __name__ == "__main__":
    main()
