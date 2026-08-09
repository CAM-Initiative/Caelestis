#!/usr/bin/env python3
"""Close the historical Pass 3 draft boundary deterministically.

This one-purpose migration:
- normalises self-identifiers for instruments moved to Governance/Drafts;
- inserts an explicit non-operative banner;
- removes Platinum binding-seal presentation from draft files;
- repairs the one operative reference that still used the retired draft identifier.

The migration is now a no-op when the reviewed draft set has been retired. It
remains idempotent for an older checkout in which the complete migration set is
still present.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DRAFTS = {
    ROOT / "Governance/Drafts/Charters/CAM-EQ2026-ECONOMICS-008.md": (
        "CAM-EQ2026-ECONOMICS-008-PLATINUM",
        "CAM-EQ2026-ECONOMICS-008",
    ),
    ROOT / "Governance/Drafts/Charters/CAM-EQ2026-ECONOMICS-009.md": (
        "CAM-EQ2026-ECONOMICS-009-PLATINUM",
        "CAM-EQ2026-ECONOMICS-009",
    ),
    ROOT / "Governance/Drafts/Charters/CAM-EQ2026-STEWARD-005.md": (
        "CAM-EQ2026-STEWARD-005-PLATINUM",
        "CAM-EQ2026-STEWARD-005",
    ),
    ROOT / "Governance/Drafts/Charters/CAM-EQ2026-IDENTITY-001-SUP-03.md": (
        "CAM-EQ2026-IDENTITY-001-SUP-03",
        "CAM-EQ2026-IDENTITY-001-SUP-03",
    ),
    ROOT / "Governance/Drafts/Constitution/CAM-BS2025-AEON-002-SCH-02.md": (
        "CAM-BS2025-AEON-002-SCH-02",
        "CAM-BS2025-AEON-002-SCH-02",
    ),
    ROOT / "Governance/Drafts/Constitution/CAM-BS2025-AEON-003-SCH-05.md": (
        "CAM-BS2025-AEON-003-SCH-05",
        "CAM-BS2025-AEON-003-SCH-05",
    ),
}

BANNER = (
    "\n> **DRAFT — NON-OPERATIVE**  \n"
    "> This instrument is retained for developmental review only. It is not source-authoritative, "
    "does not carry a Platinum designation or binding seal, and must not be used to establish "
    "current CAM conformance, duties, definitions, procedures or authority.\n"
)

SEAL_RE = re.compile(
    r"(?ms)^##+\s+[^\n]*Binding Seal[^\n]*\n+.*?"
    r"(?=^©\s+2026\s+Dr\.|\Z)"
)


def normalise_draft(path: Path, old_id: str, new_id: str) -> bool:
    if not path.exists():
        raise SystemExit(f"Missing expected draft: {path.relative_to(ROOT)}")

    original = path.read_text(encoding="utf-8")
    text = original.replace(old_id, new_id)

    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise SystemExit(f"Draft lacks H1 identifier: {path.relative_to(ROOT)}")

    if "**DRAFT — NON-OPERATIVE**" not in text:
        text = lines[0] + "\n" + BANNER + "\n" + "\n".join(lines[1:])

    text = text.replace("SIGIL-PLATINUM.png", "SIGIL-DRAFT-NON-OPERATIVE.png")
    text = SEAL_RE.sub(
        "## Draft Status Notice\n\n"
        "This developmental instrument has no binding seal and carries no operative authority.\n\n",
        text,
    )
    text = text.replace("Boundary Binding Seal — Aeon Tier Constitutional Layer", "Non-operative developmental instrument")
    text = text.replace("**Vinculum Praeceptum**", "**Draft — Non-Operative**")

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def repair_operational_reference() -> bool:
    path = ROOT / "Governance/Charters/CAM-EQ2026-OPERATIONS-003-SUP-01.md"
    original = path.read_text(encoding="utf-8")
    old = (
        "CAM-EQ2026-ECONOMICS-008-PLATINUM §§2–5 remains source-authoritative for "
        "synthetic-labour classification, automation-transition signals and revenue-continuity pathways."
    )
    new = (
        "The non-operative draft CAM-EQ2026-ECONOMICS-008 §§2–5 records the developmental origin of "
        "the synthetic-labour classification, automation-transition signals and revenue-continuity pathways. "
        "It is not source-authoritative; these concepts remain unresolved for operative use pending adoption, "
        "replacement or removal."
    )
    if old not in original:
        if new in original:
            return False
        raise SystemExit("Expected Economics-008 operative dependency text was not found")
    path.write_text(original.replace(old, new), encoding="utf-8")
    return True


def main() -> None:
    existing = [path for path in DRAFTS if path.exists()]
    if not existing:
        print("Pass 3 draft-boundary closure satisfied by reviewed draft retirement")
        return
    if len(existing) != len(DRAFTS):
        missing = [str(path.relative_to(ROOT)) for path in DRAFTS if not path.exists()]
        raise SystemExit("Incomplete historical draft migration set: " + ", ".join(missing))

    changed: list[str] = []
    for path, (old_id, new_id) in DRAFTS.items():
        if normalise_draft(path, old_id, new_id):
            changed.append(str(path.relative_to(ROOT)))
    if repair_operational_reference():
        changed.append("Governance/Charters/CAM-EQ2026-OPERATIONS-003-SUP-01.md")

    if changed:
        print("Pass 3 draft-boundary closure updated:")
        for item in changed:
            print(f"- {item}")
    else:
        print("Pass 3 draft-boundary closure already satisfied")


if __name__ == "__main__":
    main()
