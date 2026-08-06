#!/usr/bin/env python3
"""Build deterministic evidence inventories for the 2026 standards-alignment audit.

The script intentionally records textual evidence only.  It does not determine
alignment, adoption, compliance, or runtime conformance; those are human review
judgements recorded in the audit crosswalk and gap register.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GOVERNANCE = ROOT / "Governance"
OUTPUT = ROOT / ".github" / "Audit" / "Standards-Alignment-2026"

CONCEPTS = {
    "ai_abom": r"\bAI-ABOM\b|AI Architecture Bill of Materials",
    "runtime_identity": r"runtime identity|model version|system prompt|tool permissions|network permissions",
    "authority_and_oversight": r"human approval gates|stop authority|re-arbitration|authority validation|execution authority",
    "agentic_orchestration": r"agentic harness|tool-mediated execution|tool permissions|execution boundary",
    "embodied_lifecycle": r"machine civil identity|lifecycle stewardship|physical substrate|embodiment linkage",
    "identity_continuity": r"identity continuity|continuity integrity|identity-bearing formation|identity threshold",
    "telemetry_and_custody": r"telemetry custody|evidence custody|controlled identifiers|incident-time snapshot",
}

TERMS = {
    "retired_aeon_cc": r"\bAEON\.CC(?:\.(?:INSTRUMENTA|COLLECTIVA|COGNITIVA))?\b",
    "retired_class_names": r"\b(?:Instrumenta|Collectiva|Cognitiva)\b",
    "retired_origin_names": r"\b(?:Primaria|Derivata)\b",
    "relational_cardinality": r"\b(?:dyadic|triadic|polyadic)\b",
    "singular_arbitration_assumption": r"\b(?:unified arbitration locus|arbitration engine)\b",
}


def governance_files() -> list[Path]:
    return sorted(
        path
        for path in GOVERNANCE.rglob("*.md")
        if "Index" not in path.name and path.name != "CAM.Governance.Index.md"
    )


def matches(pattern: str, text: str) -> list[dict[str, object]]:
    found = []
    for line_number, line in enumerate(text.splitlines(), 1):
        if re.search(pattern, line, flags=re.IGNORECASE):
            found.append({"line": line_number, "excerpt": line.strip()})
    return found


def evidence_for(patterns: dict[str, str]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, pattern in patterns.items():
        records = []
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
        "generator": ".github/scripts/build_standards_alignment_audit.py",
        "scope": "Governance Markdown instruments excluding generated indexes",
        "source_file_count": len(source_files),
        "source_tree_sha256": digest.hexdigest(),
        "limits": [
            "Textual presence is not evidence of adoption, implementation, conformity, or legal compliance.",
            "The inventories must be read with STANDARDS-CROSSWALK.json and GAP-REGISTER.json.",
        ],
    }
    inventory = {
        "schema_version": "1.0",
        "provenance": provenance,
        "concept_evidence": evidence_for(CONCEPTS),
    }
    residual = {
        "schema_version": "1.0",
        "provenance": provenance,
        "term_evidence": evidence_for(TERMS),
    }
    return {
        OUTPUT / "CORPUS-CONCEPT-INVENTORY.json": json.dumps(inventory, indent=2, ensure_ascii=False) + "\n",
        OUTPUT / "TERMINOLOGY-RESIDUAL-SCAN.json": json.dumps(residual, indent=2, ensure_ascii=False) + "\n",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()
    outputs = render_outputs()
    stale = []
    for path, content in outputs.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    if stale:
        print("Standards-alignment audit outputs are stale:")
        print("\n".join(stale))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
