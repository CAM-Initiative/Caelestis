from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one match in {path}, found {count}: {old!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


root = Path(__file__).resolve().parents[2]

lattice = root / "Governance/Charters/CAM-EQ2026-LATTICE-001-PLATINUM.md"
steward = root / "Governance/Charters/CAM-EQ2026-STEWARD-003-PLATINUM.md"
sch04 = root / "Governance/Constitution/CAM-BS2025-AEON-006-SCH-04.md"

replace_once(
    lattice,
    "| 2.1 | Added constitutional-authority recognition, recursive suspicion and authority-laundering prohibition, aggregate-to-individual conversion, commercial-data non-evasion, and the `LAT.DEPLOY` deployment-posture family; replaced generic capability sanctions with function-specific constraints; normalised metadata and clause formatting. Provenance: VIGIL-2026-PATCH-0022. | 2026-07-16T14:55:00Z |  715a3c341ce0624ebe97312235b981893fb9f52be851e0c2670721e5f3d59568  |",
    "| 3.9 | Added constitutional-authority recognition, recursive suspicion and authority-laundering prohibition, aggregate-to-individual conversion, commercial-data non-evasion, and the `LAT.DEPLOY` deployment-posture family; replaced generic capability sanctions with function-specific constraints; normalised metadata and clause formatting. Provenance: VIGIL-2026-PATCH-0022. | 2026-07-16T14:55:00Z |  715a3c341ce0624ebe97312235b981893fb9f52be851e0c2670721e5f3d59568  |",
)

replace_once(
    steward,
    "| 1.6 | Harmonised the full instrument to CAM constitutional tone and formatting; normalised metadata and title; integrated neutrality disclosure requirements into the main assurance architecture; strengthened oversight durability, protected dissent, institutional-memory continuity, and neutrality-degradation criteria; clarified executive and sovereign circumvention as evidence of capture rather than override authority. Provenance: VIGIL-2026-PATCH-0022. | 2026-07-16T14:55:00Z |  075cb8debad2b553dcd53136a0d2d95953e605fd2d5b73bc617887f8e4bbb1a6  |",
    "| 2.2 | Harmonised the full instrument to CAM constitutional tone and formatting; normalised metadata and title; integrated neutrality disclosure requirements into the main assurance architecture; strengthened oversight durability, protected dissent, institutional-memory continuity, and neutrality-degradation criteria; clarified executive and sovereign circumvention as evidence of capture rather than override authority. Provenance: VIGIL-2026-PATCH-0022. | 2026-07-16T14:55:00Z |  075cb8debad2b553dcd53136a0d2d95953e605fd2d5b73bc617887f8e4bbb1a6  |",
)

timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
sch04_anchor = "| 2.8.3 | Updated top-level governance metadata to align with CAM Governance Metadata Standard; no substantive doctrine altered. | 2026-06-21T14:33:04Z |  4746dee21b2013d4464f1669fb83b713062108473c9b4a283c033ce818a90aea  |"
sch04_row = (
    f"{sch04_anchor}\n"
    "| 2.9 | Aligned §5.6 salience interface and §15.2 cross-referenced instrument metadata with the promoted CAM-EQ2026-IDENTITY-003-PLATINUM Appendix B, replacing references to retired IDENTITY-001-SUP-01. "
    f"| {timestamp} | |"
)
replace_once(sch04, sch04_anchor, sch04_row)

print("PR #99 amendment-ledger repairs applied.")
