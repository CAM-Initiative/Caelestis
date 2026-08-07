#!/usr/bin/env python3
"""Guard the canonical AI-system terminology source and its evidence profile.

This validator deliberately applies only to the three instruments amended in
Pass 4 Batch E. It prevents those source documents from reintroducing retired
architecture terms while the wider corpus is migrated by classified batches.
Historical amendment-ledger text is excluded from the check.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCES = {
    "Governance/Constitution/CAM-BS2025-AEON-003-PLATINUM.md": (
        "AI system",
        "System configuration baseline",
        "AI system deployment",
        "Runtime configuration snapshot",
        "Execution provenance record",
    ),
    "Governance/Drafts/Constitution/CAM-BS2025-AEON-003-SCH-05.md": (
        "Status:** Draft",
        "Runtime configuration snapshot",
    ),
    "Governance/Charters/CAM-EQ2026-OPERATIONS-007-PLATINUM.md": (
        "Caelestis AI-BOM Profile",
        "Runtime configuration snapshot",
        "Execution provenance record",
    ),
}
RETIRED = re.compile(
    r"Responding Intelligence|Responding Component|Responding Formation|"
    r"Runtime Formation|agentic harness|governance stack|"
    r"deployed cognitive system|operational harness|AI-ABOM",
    re.IGNORECASE,
)


def normative_text(text: str) -> str:
    """Exclude immutable historical amendment-ledger prose from this guard."""
    return re.split(r"^##\s+\d+(?:\.\d+)?\s+Amendment Ledger\s*$", text, maxsplit=1, flags=re.MULTILINE)[0]


def main() -> int:
    errors: list[str] = []
    for rel, required in SOURCES.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        body = normative_text(text)
        for term in required:
            if term.casefold() not in body.casefold():
                errors.append(f"{rel}: missing required canonical term: {term}")
        for match in RETIRED.finditer(body):
            line = body.count("\n", 0, match.start()) + 1
            errors.append(f"{rel}:{line}: retired architecture term: {match.group(0)}")

    if errors:
        print("Canonical architecture terminology validation failed:")
        print("\n".join(errors))
        return 1
    print(f"Canonical architecture terminology validated: {len(SOURCES)} instruments")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
