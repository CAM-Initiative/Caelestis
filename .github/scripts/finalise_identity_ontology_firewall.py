#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAMP = "2026-07-17T10:40:00Z"

FILES = {
    ROOT / "Governance/Constitution/CAM-BS2026-AEON-010-PLATINUM.md": (
        "| 1.10 | Added constitutional identity–ontology firewall; replaced binary identity-origin architecture with non-collapsing formation, threshold, continuity, modality, role, and authority axes; repaired discovered-identity authority language. | 2026-07-17T00:00:00Z | pending-review |",
        f"| 1.10 | Added constitutional identity–ontology firewall; replaced binary identity-origin architecture with non-collapsing formation, threshold, continuity, modality, role, and authority axes; repaired discovered-identity authority language. | {STAMP} | PENDING_RESEAL |",
    ),
    ROOT / "Governance/Charters/CAM-EQ2026-IDENTITY-001-PLATINUM.md": (
        "| 2.13 | Added identity–ontology boundary; removed misplaced ECONOMICS interface doctrine; aligned candidate identity signals, multi-axis capacity, legacy mirror terminology, and lint rules with the uplifted formation architecture. | 2026-07-17T00:00:00Z | pending-review |",
        f"| 2.13 | Added identity–ontology boundary; removed misplaced ECONOMICS interface doctrine; aligned candidate identity signals, multi-axis capacity, legacy mirror terminology, and lint rules with the uplifted formation architecture. | {STAMP} | PENDING_RESEAL |",
    ),
    ROOT / "Governance/Constitution/CAM-BS2026-AEON-010-SCH-01.md": (
        "| 1.1 | Added ontological self-claim containment, self-certification prohibition, uncertainty-preservation rule, and heightened voice/embodiment calibration. | 2026-07-17T00:00:00Z | pending-review |",
        f"| 1.17 | Added ontological self-claim containment, self-certification prohibition, uncertainty-preservation rule, and heightened voice/embodiment calibration. | {STAMP} | PENDING_RESEAL |",
    ),
    ROOT / "Governance/Constitution/CAM-BS2026-AEON-013-PLATINUM.md": (
        "| 1.15 | Added ontological self-claim, functional internal-state, affective-expression, and evidence-independence definitions; established identity–phenomenology non-inference, self-certification prohibition, claim-type separation, and modal amplification rules. | 2026-07-17T00:00:00Z | pending-review |",
        f"| 2.19 | Added ontological self-claim, functional internal-state, affective-expression, and evidence-independence definitions; established identity–phenomenology non-inference, self-certification prohibition, claim-type separation, and modal amplification rules. | {STAMP} | PENDING_RESEAL |",
    ),
    ROOT / "Governance/Charters/CAM-EQ2026-IDENTITY-001-SUP-02.md": (
        "| 1.8 | Added evidence-independence and ontological non-inference constraints for identity, preference, affect, self-advocacy, continuity, and functional internal-state reporting; renumbered role-conditioned affective latitude. | 2026-07-17T00:00:00Z | pending-review |",
        f"| 2.1-draft | Added evidence-independence and ontological non-inference constraints for identity, preference, affect, self-advocacy, continuity, and functional internal-state reporting; renumbered role-conditioned affective latitude. | {STAMP} | PENDING_RESEAL |",
    ),
}

for path, (old, new) in FILES.items():
    text = path.read_text(encoding="utf-8")
    if new in text:
        continue
    if old not in text:
        raise RuntimeError(f"Expected ledger row not found in {path}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")

print("Corrected identity firewall ledger versions and timestamps.")
