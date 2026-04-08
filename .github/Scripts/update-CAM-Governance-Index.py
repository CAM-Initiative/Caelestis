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
            link_name = (row.get("link") or "").strip()
            if link_name:
                row["link"] = f"{subdir}/{link_name}"
            rows.append(row)

    rows.sort(key=lambda x: x.get("id", ""))
    return rows


def render_md(items: list[dict]) -> str:
    generated = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    out = [
        "# CAM Governance Index",
        "",
        f"Generated: {generated}",
        "",
        "| ID | Class | Domain | Hierarchy | Parent | Link |",
        "|---|---|---|---|---|---|",
    ]

    for it in items:
        out.append(
            "| {id} | {instrument_class} | {domain} | {hierarchy} | {parent} | {link} |".format(
                id=it.get("id", ""),
                instrument_class=it.get("instrument_class", ""),
                domain=it.get("domain", ""),
                hierarchy=it.get("hierarchy_type") or "root",
                parent=it.get("parent_id") or "",
                link=it.get("link", ""),
            )
        )
    return "\n".join(out) + "\n"


def write_json(items: list[dict]) -> None:
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "count": len(items),
        "items": items,
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
