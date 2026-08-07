#!/usr/bin/env python3
"""Validate separation between operative Caelestis instruments and drafts."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DRAFT_ROOT = ROOT / "Governance/Drafts"
OPERATIVE_DIRS = [ROOT / "Governance/Charters", ROOT / "Governance/Constitution"]
GENERATED = [
    ROOT / "Governance/Charters/CAM-Charters-Index.md",
    ROOT / "Governance/Charters/charters.index.json",
    ROOT / "Governance/Constitution/CAM-Constitution-Index.md",
    ROOT / "Governance/Constitution/constitution.index.json",
    ROOT / "Governance/CAM.Governance.Index.md",
    ROOT / "Governance/CAM.Governance.JSON",
    ROOT / "Governance/CAM.Canonical.Code.Index.md",
    ROOT / "Governance/CAM.Canonical.Code.Index.json",
]
OLD_IDS = {
    "CAM-EQ2026-ECONOMICS-008-PLATINUM",
    "CAM-EQ2026-ECONOMICS-009-PLATINUM",
    "CAM-EQ2026-STEWARD-005-PLATINUM",
}
DRAFT_IDS = {
    "CAM-EQ2026-ECONOMICS-008",
    "CAM-EQ2026-ECONOMICS-009",
    "CAM-EQ2026-STEWARD-005",
    "CAM-EQ2026-IDENTITY-001-SUP-03",
    "CAM-BS2025-AEON-002-SCH-02",
    "CAM-BS2025-AEON-003-SCH-05",
}


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> None:
    failures: list[str] = []
    draft_files = sorted(DRAFT_ROOT.rglob("*.md"))
    if len([p for p in draft_files if p.name != "README.md"]) != 6:
        fail("Expected exactly six draft instruments", failures)

    for path in draft_files:
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        if "PLATINUM" in path.stem:
            fail(f"Draft filename carries PLATINUM: {path.relative_to(ROOT)}", failures)
        if "**DRAFT — NON-OPERATIVE**" not in text:
            fail(f"Draft banner missing: {path.relative_to(ROOT)}", failures)
        first = text.splitlines()[0] if text.splitlines() else ""
        if "PLATINUM" in first:
            fail(f"Draft H1 carries PLATINUM: {path.relative_to(ROOT)}", failures)
        if "SIGIL-PLATINUM" in text or "Boundary Binding Seal" in text:
            fail(f"Draft retains Platinum binding presentation: {path.relative_to(ROOT)}", failures)

    for directory in OPERATIVE_DIRS:
        for path in directory.glob("*.md"):
            if path.name.endswith("Index.md"):
                continue
            head = "\n".join(path.read_text(encoding="utf-8").splitlines()[:20])
            if re.search(r"\*\*Status:\*\*\s*Draft", head, re.IGNORECASE):
                fail(f"Draft remains in operative directory: {path.relative_to(ROOT)}", failures)
            if re.search(r"\*\*Governance Standard:\*\*\s*Not Enforceable", head, re.IGNORECASE):
                fail(f"Non-enforceable instrument remains operative: {path.relative_to(ROOT)}", failures)

    forbidden = OLD_IDS | DRAFT_IDS
    for path in GENERATED:
        if not path.exists():
            fail(f"Generated output missing: {path.relative_to(ROOT)}", failures)
            continue
        text = path.read_text(encoding="utf-8")
        for identifier in sorted(forbidden):
            if identifier in text:
                fail(f"Generated operative output exposes draft {identifier}: {path.relative_to(ROOT)}", failures)

    if failures:
        print("Draft-boundary validation failed:")
        for item in failures:
            print(f"- {item}")
        raise SystemExit(1)

    print("Draft-boundary validation passed")
    print(json.dumps({"draft_instruments": 6, "operative_outputs_checked": len(GENERATED)}))


if __name__ == "__main__":
    main()
