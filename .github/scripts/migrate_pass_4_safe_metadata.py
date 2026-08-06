#!/usr/bin/env python3
"""Apply the bounded Pass 4 metadata migration that does not adjudicate operative doctrine.

Scope:
- five instruments already separated into Governance/Drafts/**;
- the governance metadata standard itself.

The four constitutional-adjacent Laws and all other operative instruments are deliberately
excluded. Their source-authority assignment requires SHA-aware or instrument-level review.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

DRAFTS = [
    ROOT / "Governance/Drafts/Charters/CAM-EQ2026-ECONOMICS-008.md",
    ROOT / "Governance/Drafts/Charters/CAM-EQ2026-ECONOMICS-009.md",
    ROOT / "Governance/Drafts/Charters/CAM-EQ2026-IDENTITY-001-SUP-03.md",
    ROOT / "Governance/Drafts/Charters/CAM-EQ2026-STEWARD-005.md",
    ROOT / "Governance/Drafts/Constitution/CAM-BS2025-AEON-002-SCH-02.md",
]
STANDARD = ROOT / "Governance/Standards/CAM-GOVERNANCE-METADATA-STANDARD.md"

FIELD_ORDER = [
    "Status",
    "Effect",
    "Governance Standard",
    "Review State",
    "Authority Role",
    "Source Authority",
]
META_RE = re.compile(r"^(?P<prefix>\*\*)?(?P<key>Status|Effect|Governance Standard|Review State|Authority Role|Source Authority):(?P<suffix>\*\*)?\s*(?P<value>.*?)(?:\s{2})?$")


def replace_metadata(path: Path, values: dict[str, str]) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    positions: dict[str, int] = {}
    for idx, line in enumerate(lines[:100]):
        plain = line.strip()
        m = META_RE.match(plain)
        if m:
            positions[m.group("key")] = idx

    # Replace existing fields first.
    for key, value in values.items():
        if key in positions:
            lines[positions[key]] = f"**{key}:** {value}  "

    # Insert missing fields after the latest controlled metadata field, or after H1.
    missing = [k for k in FIELD_ORDER if k in values and k not in positions]
    if missing:
        existing_positions = [positions[k] for k in FIELD_ORDER if k in positions]
        insert_at = max(existing_positions) + 1 if existing_positions else 1
        for offset, key in enumerate(missing):
            lines.insert(insert_at + offset, f"**{key}:** {values[key]}  ")

    updated = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    changed = []
    for path in DRAFTS:
        if replace_metadata(path, {
            "Status": "Draft",
            "Effect": "Interpretive",
            "Governance Standard": "Not Enforceable",
            "Review State": "Under Review",
            "Authority Role": "No Independent Authority",
            "Source Authority": "Non-Operative Draft",
        }):
            changed.append(path.relative_to(ROOT).as_posix())

    if replace_metadata(STANDARD, {
        "Status": "Active",
        "Effect": "Operational",
        "Governance Standard": "Registry Standard",
        "Review State": "Current",
        "Authority Role": "Metadata Authority",
        "Source Authority": "Source-Authoritative",
    }):
        changed.append(STANDARD.relative_to(ROOT).as_posix())

    print(f"Pass 4 safe metadata migration complete; changed={len(changed)}")
    for item in changed:
        print(item)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
