#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
GOV_DIR = REPO_ROOT / "Governance"

SOURCE_INDEXES = [
    GOV_DIR / "Constitution" / "constitution.index.json",
    GOV_DIR / "Charters" / "charters.index.json",
    GOV_DIR / "Covenants" / "covenants.index.json",
    GOV_DIR / "Laws" / "laws.index.json",
]

OUT_JSON = GOV_DIR / "CAM.Governance.JSON"
OUT_MD = GOV_DIR / "CAM.Governance.Index.md"


def load_items(path: Path) -> list[dict]:
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("items", [])


def merge_items() -> list[dict]:
    by_id: dict[str, dict] = {}
    for index_file in SOURCE_INDEXES:
        for item in load_items(index_file):
            item_id = item.get("id")
            if item_id and item_id not in by_id:
                by_id[item_id] = item
    return [by_id[k] for k in sorted(by_id)]


def write_json(items: list[dict]) -> None:
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "count": len(items),
        "items": items,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_markdown(items: list[dict]) -> None:
    lines = [
        "# CAM Governance Index",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')}",
        "",
        "| ID | Class | Domain | Hierarchy | Parent | Link |",
        "|---|---|---|---|---|---|",
    ]

    for item in items:
        hierarchy = item.get("hierarchy_type") or "root"
        parent = item.get("parent_id") or ""
        link = item.get("link") or ""
        lines.append(
            f"| {item.get('id', '')} | {item.get('instrument_class', '')} | {item.get('domain', '')} | "
            f"{hierarchy} | {parent} | {link} |"
        )

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    items = merge_items()
    write_json(items)
    write_markdown(items)
    print(f"Wrote: {OUT_JSON}")
    print(f"Wrote: {OUT_MD}")


if __name__ == "__main__":
    main()
