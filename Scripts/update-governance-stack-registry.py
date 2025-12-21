#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = REPO_ROOT / "Governance" / "registry"
OUTPUT_JSON = REGISTRY_DIR / "governance.stack.index.json"
OUTPUT_MD = REGISTRY_DIR / "GOVERNANCE-STACK-INDEX.md"

DOMAINS = [
    ("constitution", "Governance/Constitution/constitution.index.json"),
    ("charters", "Governance/Charters/charters.index.json"),
    ("covenants", "Governance/Covenants/covenants.index.json"),
    ("laws", "Governance/Laws/laws.index.json"),
    ("protocols", "Governance/Protocols/protocols.index.json"),
    ("policies", "Governance/Policies/policy.index.json"),
]

def load_count(path: Path) -> int:
    if not path.exists():
        return 0
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return int(data.get("count", len(data.get("items", []))))
    except Exception:
        return 0

def main():
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)

    domains = []
    for name, rel_path in DOMAINS:
        path = REPO_ROOT / rel_path
        domains.append({
            "domain": name,
            "path": rel_path,
            "count": load_count(path),
            "status": "active" if path.exists() else "absent"
        })

    payload = {
        "stack": "governance",
        "status": "active",
        "registry_type": "stack-registry",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "description": "Canonical registry of governance-domain registries within the Caelestis architecture.",
        "domains": domains,
    }

    OUTPUT_JSON.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

    # Minimal Markdown companion (navigational only)
    md_lines = [
        "# Governance Stack Registry",
        "",
        "This document provides a canonical index of governance-domain registries.",
        "It does not enumerate individual instruments.",
        "",
        "| Domain | Registry | Count | Status |",
        "|---|---|---|---|",
    ]

    for d in domains:
        md_lines.append(
            f"| {d['domain'].capitalize()} | "
            f"{d['path']} | "
            f"{d['count']} | "
            f"{d['status']} |"
        )

    OUTPUT_MD.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    print(f"Wrote: {OUTPUT_JSON}")
    print(f"Wrote: {OUTPUT_MD}")

if __name__ == "__main__":
    main()
