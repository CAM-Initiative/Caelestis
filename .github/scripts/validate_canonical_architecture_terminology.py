#!/usr/bin/env python3
"""Guard retired architecture terminology across the operative corpus.

The check deliberately detects only unambiguous regression patterns. It
excludes Drafts, the SHA-sensitive Laws and amendment-ledger history; it does
not decide whether every use of model, system, runtime, agent or formation is
conceptually correct. Annex B remains the source authority for that review.
"""

from __future__ import annotations

import re
import sys
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
        "CAM-EQ2026-RELATION-007-PLATINUM applies those dimensions",
    ),
    "Governance/Charters/CAM-EQ2026-RELATION-007-PLATINUM.md": (
        "Participant topology and cardinality",
        "Institutional mediation",
        "This Appendix creates no replacement ordinal code family",
    ),
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
        if relative.startswith("Governance/Drafts/") or relative.startswith("Governance/Laws/"):
            continue
        files.append(path)
    return sorted(files)


def retired_findings(path: Path, text: str) -> list[tuple[int, str]]:
    """Return line-level unambiguous retired-term findings for an artefact."""
    body = normative_text(text) if path.suffix.lower() == ".md" else text
    findings: list[tuple[int, str]] = []
    for match in RETIRED_CORPUS_TERMINOLOGY.finditer(body):
        line = body.count("\n", 0, match.start()) + 1
        findings.append((line, match.group(0)))
    return findings


def main() -> int:
    errors: list[str] = []
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
        for line, term in retired_findings(path, path.read_text(encoding="utf-8")):
            errors.append(f"{rel}:{line}: retired corpus terminology: {term}")

    if errors:
        print("Canonical architecture terminology validation failed:")
        print("\n".join(errors))
        return 1
    print(
        "Canonical architecture terminology validated: "
        f"{len(SOURCES)} canonical-source contracts; {len(operative_files())} operative artefacts"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
