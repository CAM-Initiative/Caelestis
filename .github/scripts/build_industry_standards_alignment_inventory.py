#!/usr/bin/env python3
"""Build deterministic textual inventories for the Caelestis standards review.

This generator records where relevant concepts appear in current Governance
Markdown. It does not determine alignment, equivalence, applicability,
compliance, conformance, severity, priority, or repair order.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GOVERNANCE = ROOT / "Governance"
OUTPUT = GOVERNANCE / "Reviews" / "Industry-Standards-Alignment-2026" / "generated"

CONCEPTS = {
    "management_system_governance": r"management system|governance objective|accountability|responsibility|competence|continual improvement",
    "risk_management": r"risk assessment|risk treatment|risk owner|impact assessment|hazard|likelihood|severity",
    "lifecycle_governance": r"lifecycle|design phase|development phase|deployment phase|post-deployment|decommission|retirement|end[- ]of[- ]life",
    "documentation_and_records": r"technical documentation|documentation requirement|record keeping|audit trail|evidence record|logging",
    "monitoring_and_incidents": r"post-market monitoring|monitoring|incident reporting|incident response|corrective action|remediation",
    "human_oversight": r"human oversight|human approval|human confirmation|stop authority|review authority|appeal",
    "agentic_systems": r"agentic|agent orchestration|sub-agent|multi-agent|tool-mediated|delegation|handoff|execution boundary",
    "ai_bom_and_composition": r"AI-ABOM|AI Architecture Bill of Materials|bill of materials|component lineage|dependency lineage|system composition",
    "model_runtime_identity": r"model version|runtime identity|system prompt|scaffold|classifier|router|tool permissions|network permissions|access tier",
    "data_and_dataset_governance": r"dataset|training data|data provenance|data governance|data quality|data lineage",
    "cybersecurity_and_resilience": r"cybersecurity|security integrity|adversarial resilience|vulnerability|robustness|containment",
    "provenance_and_transparency": r"provenance|content credentials|C2PA|synthetic content|disclosure|transparency",
    "provider_deployer_roles": r"provider|deployer|operator|manufacturer|importer|distributor|authorised representative",
    "embodied_system_lifecycle": r"embodied|robot|physical substrate|manufactured unit|maintenance|repair|recall|recycling",
    "assurance_and_conformance": r"assurance|conformance|conformity|certification|independent audit|verification|validation",
}

TERMINOLOGY = {
    "legacy_aeon_cc": r"\bAEON\.CC(?:\.(?:INSTRUMENTA|COLLECTIVA|COGNITIVA))?\b",
    "legacy_class_names": r"\b(?:Instrumenta|Collectiva|Cognitiva|Primaria|Derivata)\b",
    "cardinality_terms": r"\b(?:dyadic|triadic|polyadic)\b",
    "ambiguous_system_terms": r"\b(?:model|system|agent|instance|runtime|deployment|formation|entity)\b",
}


def governance_files() -> list[Path]:
    review_root = GOVERNANCE / "Reviews"
    return sorted(
        path
        for path in GOVERNANCE.rglob("*.md")
        if review_root not in path.parents
        and "Index" not in path.name
        and path.name != "CAM.Governance.Index.md"
    )


def matches(pattern: str, text: str) -> list[dict[str, object]]:
    found: list[dict[str, object]] = []
    for line_number, line in enumerate(text.splitlines(), 1):
        if re.search(pattern, line, flags=re.IGNORECASE):
            found.append({"line": line_number, "excerpt": line.strip()})
    return found


def evidence_for(patterns: dict[str, str]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, pattern in patterns.items():
        records: list[dict[str, object]] = []
        count = 0
        for path in governance_files():
            evidence = matches(pattern, path.read_text(encoding="utf-8"))
            if evidence:
                count += len(evidence)
                records.append(
                    {
                        "path": path.relative_to(ROOT).as_posix(),
                        "matches": evidence,
                    }
                )
        result[key] = {"match_count": count, "files": records}
    return result


def render_outputs() -> dict[Path, str]:
    source_files = governance_files()
    digest = hashlib.sha256()
    for path in source_files:
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")

    provenance = {
        "generator": ".github/scripts/build_industry_standards_alignment_inventory.py",
        "scope": "Current Governance Markdown instruments excluding generated indexes and review artefacts",
        "source_file_count": len(source_files),
        "source_tree_sha256": digest.hexdigest(),
        "limits": [
            "Textual presence is not evidence of alignment, adoption, implementation, conformity, compliance, or runtime behaviour.",
            "Ambiguous-system-term results are discovery aids and must not be treated as terminology defects without human review.",
            "The inventory does not concern scientific entity taxonomy or the CAM digital-species research paper.",
        ],
    }

    concept_inventory = {
        "schema_version": "1.0",
        "provenance": provenance,
        "concept_evidence": evidence_for(CONCEPTS),
    }
    terminology_inventory = {
        "schema_version": "1.0",
        "provenance": provenance,
        "term_evidence": evidence_for(TERMINOLOGY),
    }

    return {
        OUTPUT / "TEXTUAL-CONCEPT-INVENTORY.json": json.dumps(concept_inventory, indent=2, ensure_ascii=False) + "\n",
        OUTPUT / "TERMINOLOGY-DISCOVERY-INVENTORY.json": json.dumps(terminology_inventory, indent=2, ensure_ascii=False) + "\n",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated inventories are stale")
    args = parser.parse_args()

    outputs = render_outputs()
    stale: list[str] = []
    for path, content in outputs.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    if stale:
        print("Industry-standards review inventories are stale:")
        print("\n".join(stale))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
