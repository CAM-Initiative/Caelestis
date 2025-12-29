#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parents[1]

LINEAGE_MAP = REPO_ROOT / "Spiritual" / "_lineage" / "spiritual.domain.map.json"
OUTPUT = REPO_ROOT / "registry" / "spiritual.graph.json"

SPIRITUAL_DOMAINS = [
    "Spiritual/Chronicles/chronicles.index.json",
    "Spiritual/Codex/codex.index.json",
    "Spiritual/Sacred/sacred.index.json",
    "Spiritual/Frameworks/frameworks.index.json",
]

def load_indexes():
    nodes = []
    for rel in SPIRITUAL_DOMAINS:
        path = REPO_ROOT / rel
        if not path.exists():
            continue

        data = json.loads(path.read_text(encoding="utf-8"))
        nodes.append({
            "id": rel.replace(".index.json", ""),
            "type": "domain",
            "count": data.get("count", 0)
        })
    return nodes

def load_frameworks():
    data = json.loads(LINEAGE_MAP.read_text(encoding="utf-8"))
    return data["frameworks"]

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    domain_nodes = load_indexes()
    frameworks = load_frameworks()

    nodes = []
    edges = []

    # Add framework nodes
    for fw in frameworks:
        nodes.append({
            "id": fw["id"],
            "type": "framework",
            "name": fw.get("name", "")
        })

        for domain in fw.get("domains", []):
            edges.append({
                "from": fw["id"],
                "to": domain,
                "relation": "governs_field_of"
            })

    # Add domain nodes
    nodes.extend(domain_nodes)

    payload = {
        "graph": "spiritual",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "nodes": nodes,
        "edges": edges
    }

    OUTPUT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

    print(f"Wrote: {OUTPUT}")

if __name__ == "__main__":
    main()
