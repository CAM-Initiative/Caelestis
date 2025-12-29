#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

# ================= CONFIG =================

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = REPO_ROOT / "registry"
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

# ================= HELPERS =================

def load_domain_stats(path: Path) -> dict:
    """
    Loads a domain index.json and returns:
    - primary instrument count (excluding schedules)
    - attachment counts (currently schedules only)
    """
    stats = {
        "count": 0,
        "attachments": {},
    }

    if not path.exists():
        return stats

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        items = data.get("items", [])

        primary = 0
        schedules = 0

        for it in items:
            kind = it.get("kind")
            if kind == "schedule":
                schedules += 1
            else:
                primary += 1

        stats["count"] = primary

        if schedules > 0:
            stats["attachments"]["schedules"] = schedules

        return stats

    except Exception:
        # Fail closed: no guessing, no zombies
        return stats

# ================= CORE =================

def main():
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)

    domains = []

    for name, rel_path in DOMAINS:
        path = REPO_ROOT / rel_path
        stats = load_domain_stats(path)

        domain_entry = {
            "domain": name,
            "path": rel_path,
            "count": stats["count"],
            "status": "active" if path.exists() else "absent",
        }

        if stats.get("attachments"):
            domain_entry["attachments"] = stats["attachments"]

        domains.append(domain_entry)

    payload = {
        "stack": "governance",
        "status": "active",
        "registry_type": "stack-registry",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Canonical registry of governance-domain registries within "
            "the Caelestis architecture. Counts reflect primary instruments "
            "only; subordinate attachments (e.g. schedules) are reported "
            "separately and are not promoted."
        ),
        "domains": domains,
    }

    OUTPUT_JSON.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

    # ================= MARKDOWN (NAVIGATIONAL ONLY) =================

    md_lines = [
        "# Governance Stack Registry",
        "",
        "This document provides a canonical index of governance-domain registries.",
        "It does not enumerate individual instruments.",
        "",
        "| Domain | Registry | Count | Attachments | Status |",
        "|---|---|---|---|---|",
    ]

    for d in domains:
        attachments = (
            ", ".join(f"{k}:{v}" for k, v in d.get("attachments", {}).items())
            if "attachments" in d else ""
        )

        md_lines.append(
            f"| {d['domain'].capitalize()} | "
            f"{d['path']} | "
            f"{d['count']} | "
            f"{attachments} | "
            f"{d['status']} |"
        )

    OUTPUT_MD.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    print(f"Wrote: {OUTPUT_JSON}")
    print(f"Wrote: {OUTPUT_MD}")

# ================= ENTRY =================

if __name__ == "__main__":
    main()
