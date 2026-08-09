#!/usr/bin/env python3
"""Guard retired architecture and relational-geometry terminology.

The check blocks explicit retired terms and high-confidence reconstruction of
participant-cardinality governance classes. It excludes Drafts and historical
amendment-ledger prose. Four exact hash-protected Law metadata lines are
adjudicated as legacy/non-consumable exceptions; no other Law exception exists.
Annex B remains the source authority for the non-collapse rule.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GOVERNANCE = ROOT / "Governance"
SOURCES = {
    "Governance/Constitution/CAM-BS2025-AEON-001-PLATINUM.md": (
        "AI systems",
        "AI-system deployments",
        "Annex B owns the canonical system-boundary terminology",
    ),
    "Governance/Constitution/CAM-BS2025-AEON-003-PLATINUM.md": (
        "AI system",
        "System configuration baseline",
        "AI system deployment",
        "Runtime configuration snapshot",
        "Execution provenance record",
        "Participant topology MAY describe who or what is involved",
        "No separate relational-configuration record is required",
        "Sealed-Law Legacy Metadata",
    ),
    "Governance/Charters/CAM-EQ2026-OPERATIONS-007-PLATINUM.md": (
        "Caelestis AI-BOM Profile",
        "Runtime configuration snapshot",
        "Execution provenance record",
    ),
    "Governance/Constitution/CAM-BS2025-AEON-003-SCH-02.md": (
        "CAM governance-processing model",
        "Runtime configuration snapshot",
        "Execution provenance record",
    ),
    "Governance/Charters/CAM-EQ2026-RELATION-001-PLATINUM.md": (
        "participant topology",
        "institutional mediation",
        "CAM-EQ2026-RELATION-007-PLATINUM applies relational safeguards",
    ),
    "Governance/Charters/CAM-EQ2026-RELATION-007-PLATINUM.md": (
        "Evidence Inputs and Non-Duplication",
        "Count is data, not a class",
        "Existing authoritative records SHALL be reused",
        "This Appendix creates no replacement ordinal code family",
    ),
}

SEALED_LAW_LEGACY = {
    "Governance/Laws/CAM-BS2025-LAW-001-PLATINUM.md":
        "| **Axis Context** | Polyadic - Multi-System / Cross-Domain |",
    "Governance/Laws/CAM-BS2025-LAW-002-PLATINUM.md":
        "| **Axis Context** | Polyadic - Multi-System / Cross-Domain |",
    "Governance/Laws/CAM-BS2025-LAW-003-PLATINUM.md":
        "| **Axis Context** | Polyadic - Multi-System / Cross-Domain |",
    "Governance/Laws/CAM-EQ2026-LAW-004-PLATINUM.md":
        "| **Axis Context** | Polyadic - Multi-System / Cross-Domain |",
}
EXPLICIT_MIGRATION_DISPOSITION = {
    "Governance/Constitution/CAM-BS2025-AEON-003-PLATINUM.md": {
        "The `Axis Context` value `Polyadic - Multi-System / Cross-Domain` in "
        "CAM-BS2025-LAW-001-PLATINUM, CAM-BS2025-LAW-002-PLATINUM, "
        "CAM-BS2025-LAW-003-PLATINUM, and CAM-EQ2026-LAW-004-PLATINUM is "
        "hash-protected archival metadata. It records the terminology present "
        "at archival settlement and is not a current classification."
    },
}
RETIRED_ARCHITECTURE = re.compile(
    r"Responding Intelligence|Responding Component|Responding Formation|"
    r"Runtime Formation|agentic harness|governance stack|"
    r"deployed cognitive system|operational harness|AI-ABOM|"
    r"Responding Intelligence|cognitive architecture",
    re.IGNORECASE,
)
RETIRED_RELATIONAL_TOPOLOGY = re.compile(
    r"\bdyadic\b|\btriadic\b|\bpolyadic\b|"
    r"RLN\.R[0-4]\b|RLN\.R(?![A-Z])",
    re.IGNORECASE,
)
RETIRED_CORPUS_TERMINOLOGY = re.compile(
    r"Responding Intelligence|Responding Component|Responding Formation|"
    r"(?<![\w.])RI(?![\w.])|"
    r"\bcognitive systems?\b|\bcognitive architecture\b|"
    r"\bcognitive formation\b|\bsynthetic cognitive formation\b|"
    r"\bcomposed[- ]system(?: architecture)?\b|"
    r"\bdeployed cognitive system\b|\bagentic harness\b|"
    r"\boperational harness\b|\bgovernance stack\b|"
    r"\bruntime formation\b|"
    r"\bdyadic\b|\btriadic\b|\bpolyadic\b|"
    r"RLN\.R[0-4]\b|\brelational geometry\b|\bR-Scale\b|"
    r"\bInstrumenta\b|\bCollectiva\b|\bCognitiva\b|"
    # AEON.CCS was a CAM cognitive classification, not a technical system
    # taxonomy.  Retain the narrowly known aliases here rather than trying to
    # infer every possible "AEON" reference from prose.
    r"\bAEON(?:[._ -]CCS|[._ -]CC(?:[._ -](?:INSTRUMENTA|COLLECTIVA|COGNITIVA))?)\b|"
    r"\bCognitive Cycle Stage\b",
    re.IGNORECASE,
)

CARDINALITY_CLASS_ROW = re.compile(
    r"^\s*\|\s*(?:\*\*)?(?:One-to-one|Three-party|Multi-party)(?:\*\*)?\s*\|",
    re.IGNORECASE,
)
CARDINALITY_METADATA = re.compile(
    r"^\s*\|\s*(?:\*\*)?(?:Axis Context|Jurisdiction)(?:\*\*)?\s*\|"
    r"[^\n|]*(?:One-to-one|Three-party|Multi-party)",
    re.IGNORECASE,
)
RELATIONAL_AXIS = re.compile(
    r"\bAxis\s+B\b[^\n]*(?:Relational Configuration|One-to-one|Three-party|Multi-party)",
    re.IGNORECASE,
)
GEOMETRY_AS_GOVERNANCE = re.compile(
    r"\b(?:multi-party|one-to-one|three-party)\s+"
    r"(?:authority|power|influence|amplification|jurisdiction|permission|consent|risk|responsibility|status)\b",
    re.IGNORECASE,
)
TOPOLOGY_DIRECT_CONSEQUENCE = re.compile(
    r"\b(?:participant (?:count|topology|cardinality)|number of participants)\b.{0,120}"
    r"\b(?:determin(?:e|es)|creat(?:e|es)|confer(?:s)?|establish(?:es)?|assign(?:s)?|set(?:s)?)\b.{0,120}"
    r"\b(?:authority|permission|consent|responsibility|impact|risk|identity|jurisdiction|access|governance status)\b|"
    r"\b(?:authority|permission|consent|responsibility|impact|risk|identity|jurisdiction|access|governance status)\b.{0,120}"
    r"\b(?:determin(?:e|es)|creat(?:e|es)|confer(?:s)?|establish(?:es)?|assign(?:s)?|set(?:s)?)\b.{0,120}"
    r"\b(?:participant (?:count|topology|cardinality)|number of participants)\b",
    re.IGNORECASE,
)
NON_INFERENCE = re.compile(
    r"\b(?:must not|does not|do not|cannot|none independently|not inferred|not a governance class|not a class)\b",
    re.IGNORECASE,
)
AMBIGUOUS_GEOMETRY_CONSEQUENCE = re.compile(
    r"\b(?:multi-party|one-to-one|three-party)\b.{0,100}"
    r"\b(?:authority|permission|consent|responsibility|impact|risk|identity|jurisdiction|access|governance status)\b|"
    r"\b(?:authority|permission|consent|responsibility|impact|risk|identity|jurisdiction|access|governance status)\b.{0,100}"
    r"\b(?:multi-party|one-to-one|three-party)\b",
    re.IGNORECASE,
)


def normalise_text(text: str) -> str:
    """Normalise Unicode compatibility forms and dash variants deterministically."""
    return (
        unicodedata.normalize("NFKC", text)
        .replace("‑", "-")
        .replace("–", "-")
        .replace("—", "-")
    )


def repo_relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def normative_text(text: str) -> str:
    """Exclude immutable historical amendment-ledger prose from this guard."""
    return re.split(r"^##\s+\d+(?:\.\d+)?\s+Amendment Ledger\s*$", text, maxsplit=1, flags=re.MULTILINE)[0]


def operative_files() -> list[Path]:
    """Return current source and generated governance artefacts to inspect."""
    suffixes = {".md", ".json", ".yaml", ".yml"}
    files: list[Path] = []
    for path in GOVERNANCE.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative.startswith("Governance/Drafts/"):
            continue
        files.append(path)
    return sorted(files)


def retired_findings(path: Path, text: str) -> list[tuple[int, str]]:
    """Return line-level unambiguous retired-term findings for an artefact."""
    body = normative_text(text) if path.suffix.lower() == ".md" else text
    findings: list[tuple[int, str]] = []
    relative = repo_relative(path)
    allowed_line = SEALED_LAW_LEGACY.get(relative)
    disposition_lines = EXPLICIT_MIGRATION_DISPOSITION.get(relative, set())
    pattern = RETIRED_RELATIONAL_TOPOLOGY if relative.startswith("Governance/Laws/") else RETIRED_CORPUS_TERMINOLOGY
    for line_number, raw_line in enumerate(body.splitlines(), start=1):
        line = normalise_text(raw_line)
        for match in pattern.finditer(line):
            if allowed_line and line.strip() == allowed_line and match.group(0).casefold() == "polyadic":
                continue
            if line.strip() in disposition_lines:
                continue
            findings.append((line_number, match.group(0)))
    return findings


def categorical_geometry_findings(text: str) -> list[tuple[int, str]]:
    """Return high-confidence recreations of the retired cardinality scale."""
    body = normative_text(text)
    findings: list[tuple[int, str]] = []
    for line_number, raw_line in enumerate(body.splitlines(), start=1):
        line = normalise_text(raw_line)
        if CARDINALITY_CLASS_ROW.search(line):
            findings.append((line_number, "participant-cardinality class table row"))
        elif CARDINALITY_METADATA.search(line):
            findings.append((line_number, "participant-cardinality governance metadata"))
        elif RELATIONAL_AXIS.search(line):
            findings.append((line_number, "participant-cardinality relational axis"))
        elif GEOMETRY_AS_GOVERNANCE.search(line) and not NON_INFERENCE.search(line):
            findings.append((line_number, "geometry used as governance consequence"))
        elif TOPOLOGY_DIRECT_CONSEQUENCE.search(line) and not NON_INFERENCE.search(line):
            findings.append((line_number, "participant topology directly determines governance consequence"))
    return findings


def geometry_candidate_warnings(text: str) -> list[tuple[int, str]]:
    """Return non-blocking semantic-review candidates with consequence proximity."""
    body = normative_text(text)
    warnings: list[tuple[int, str]] = []
    for line_number, raw_line in enumerate(body.splitlines(), start=1):
        line = normalise_text(raw_line)
        if AMBIGUOUS_GEOMETRY_CONSEQUENCE.search(line) and not NON_INFERENCE.search(line):
            if (
                CARDINALITY_CLASS_ROW.search(line)
                or CARDINALITY_METADATA.search(line)
                or RELATIONAL_AXIS.search(line)
                or GEOMETRY_AS_GOVERNANCE.search(line)
                or TOPOLOGY_DIRECT_CONSEQUENCE.search(line)
            ):
                continue
            warnings.append((line_number, "geometry term near governance consequence"))
    return warnings


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    for rel, required in SOURCES.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        body = normative_text(text)
        for term in required:
            if term.casefold() not in body.casefold():
                errors.append(f"{rel}: missing required canonical term: {term}")
        retired = RETIRED_RELATIONAL_TOPOLOGY if "/RELATION-" in rel else RETIRED_ARCHITECTURE
        for match in retired.finditer(body):
            line = body.count("\n", 0, match.start()) + 1
            errors.append(f"{rel}:{line}: retired architecture term: {match.group(0)}")

    for path in operative_files():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        for line, term in retired_findings(path, text):
            errors.append(f"{rel}:{line}: retired corpus terminology: {term}")
        if path.suffix.lower() == ".md":
            for line, reason in categorical_geometry_findings(text):
                errors.append(f"{rel}:{line}: retired geometry reconstruction: {reason}")
            for line, reason in geometry_candidate_warnings(text):
                warnings.append(f"{rel}:{line}: relational-geometry review candidate: {reason}")

    for rel, expected_line in SEALED_LAW_LEGACY.items():
        text = normalise_text((ROOT / rel).read_text(encoding="utf-8"))
        count = sum(line.strip() == expected_line for line in text.splitlines())
        if count != 1:
            errors.append(f"{rel}: expected exactly one adjudicated sealed-Law legacy Axis Context line; found {count}")

    if errors:
        print("Canonical architecture terminology validation failed:")
        print("\n".join(errors))
        return 1
    if warnings:
        print("Canonical architecture terminology review warnings:")
        print("\n".join(warnings))
    print(
        "Canonical architecture terminology validated: "
        f"{len(SOURCES)} canonical-source contracts; {len(operative_files())} operative artefacts; "
        f"{len(SEALED_LAW_LEGACY)} sealed-Law legacy exceptions; {len(warnings)} review warnings"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
