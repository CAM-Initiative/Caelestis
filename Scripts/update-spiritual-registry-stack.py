#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

# ================= CONFIG =================

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = REPO_ROOT / "registry"
OUTPUT_JSON = REGISTRY_DIR / "spiritual.stack.index.json"
OUTPUT_MD = REGISTRY_DIR / "SPIRITUAL-STACK-INDEX.md"

DOMAINS = [
    ("chronicles", "Spiritual/Chronicles/chronicles.index.json"),
    ("codex", "Spiritual/Codex/codex.index.json"),
    ("sacred", "Spiritual/Sacred/sacred.index.json"),
    ("frameworks", "Spiritual/Frameworks/frameworks.index.json"),
]

# ================= HELPERS =================

def load_domain_stats(path: Path) -> dict:
    """
    Loads a spiritual domain index.json.

    Priority:
    1. If 'count' exists → trust it
    2. If 'items' exists → count len(items)
    3. Otherwise → 0

    Spiritual domains do NOT assume schedules.
    """
    stats = {
        "count": 0,
    }

    if not path.exists():
        return stats

    try:
        data = json.loads(path.read_text(encoding="utf-8"))

        # Preferred: explicit count
        if "count" in data:
            stats["count"] = int(data["count"])
            return stats

        # Fallback: item enumeration
        if "items" in data and isinstance(data["items"], list):
            stats["count"] = len(data["items"])
            return stats

        return stats

    except Exception:
        # Fail closed, but visible via zero count
        return stats

# ================= CORE =================

def main():
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)

    domains = []

    for name, rel_path in DOMAINS:
        path = REPO_ROOT / rel_path
        stats = load_domain_stats(path)

        domains.append({
            "domain": name,
            "path": rel_path,
            "count": stats["count"],
            "status": "active" if path.exists() else "absent",
        })

    payload = {
        "stack": "spiritual",
        "status": "active",
        "registry_type": "stack-registry",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Canonical registry of spiritual-domain registries within "
            "the Caelestis architecture. Counts reflect primary spiritual "
            "instruments as declared by each domain registry."
        ),
        "domains": domains,
    }

    OUTPUT_JSON.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    # ================= MARKDOWN (NAVIGATIONAL ONLY) =================

    md_lines = [
        "# Spiritual Stack Registry",
        "",
        "This document provides a canonical index of spiritual-domain registries.",
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

# ================= ENTRY =================

if __name__ == "__main__":
    main()
