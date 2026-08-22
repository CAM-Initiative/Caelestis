#!/usr/bin/env python3
"""Validate the constitutional Runtime-processing architecture contract.

This validator protects the frozen ten-phase constitutional topology and authority
boundaries. It deliberately does not prescribe implementation-style per-phase
fields or require domain-specific doctrine to appear in the constitutional engine.
It also runs the runtime-migration assurance check so the historic schedule
consolidation cannot silently lose a disposition or current owner.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENGINE = Path("Governance/Constitution/CAM-BS2025-AEON-003-SCH-02.md")
OPERATIONS = Path("Governance/Charters/CAM-EQ2026-OPERATIONS-001-PLATINUM.md")
TRANSITIONS = Path("Governance/Charters/CAM-EQ2026-OPERATIONS-001-SUP-02.md")
MIGRATION_VALIDATOR = Path(__file__).with_name("validate_runtime_migration_assurance.py")
PROFILES = (
    Path("Governance/Standards/CAM-RUNTIME-STATE-PROFILE.md"),
    Path("Governance/Standards/CAM-LIFECYCLE-ACTOR-AGENTIC-PROFILE.md"),
    Path("Governance/Standards/CAM-AI-BOM-PROFILE.md"),
)

PHASES = (
    "Runtime Entry and Context",
    "Pre-Classification",
    "Domain Determination",
    "Authority Resolution",
    "Governed Response or Action Preparation",
    "Execution-Boundary Evaluation",
    "Bounded Commitment",
    "Execution",
    "Representation and Delivery",
    "Preservation, Closure and Reassessment",
)

REQUIRED_AUTHORITIES = (
    "CAM-BS2025-AEON-001-SCH-01",
    "CAM-BS2025-AEON-005-PLATINUM",
    "CAM-BS2025-AEON-005-SCH-04",
    "CAM-BS2026-AEON-013-SCH-01",
)

TECHNICAL_PHASE_LABELS = (
    "**Entry:**",
    "**Required state:**",
    "**Invocation:**",
    "**Output:**",
    "**Exit:**",
)

# Domain code families are legitimate in their source instruments, but embedding
# them in the operative constitutional processing spine couples the Constitution
# to subordinate classifications. Exact instrument identifiers remain permitted.
SCOPED_DOMAIN_CODE_RE = re.compile(
    r"\b(?:RLN|OPS|SEC|ETH|ID|ECON|LATTICE|MENTIS|STW)\.[A-Z0-9][A-Z0-9._-]*\b"
)


def section(text: str, start: str, end: str) -> str:
    """Return text between two exact Markdown headings."""
    start_at = text.find(start)
    end_at = text.find(end, start_at + len(start)) if start_at >= 0 else -1
    if start_at < 0 or end_at < 0:
        return ""
    return text[start_at:end_at]


def instrument_ids(root: Path) -> set[str]:
    return {path.stem for path in (root / "Governance").rglob("CAM-*.md")}


def operative_engine_text(engine: str) -> str:
    marker = "## 6. Provenance & Metadata"
    return engine.split(marker, 1)[0] if marker in engine else engine


def migration_assurance_issues(root: Path) -> list[str]:
    spec = importlib.util.spec_from_file_location("runtime_migration_assurance", MIGRATION_VALIDATOR)
    if spec is None or spec.loader is None:
        return ["runtime migration assurance validator cannot be loaded"]
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return [f"migration assurance: {issue}" for issue in module.validate(root)]


def validate(root: Path = ROOT) -> list[str]:
    issues: list[str] = []
    engine_path = root / ENGINE
    if not engine_path.exists():
        return [f"missing constitutional engine: {ENGINE}"]
    engine = engine_path.read_text(encoding="utf-8")
    operative = operative_engine_text(engine)

    positions: list[int] = []
    for number, name in enumerate(PHASES, start=1):
        heading = f"### 2.{number} Phase {number} — {name}"
        count = engine.count(heading)
        if count != 1:
            issues.append(f"Phase {number} heading count is {count}, expected 1")
            continue
        positions.append(engine.index(heading))
        next_heading = (
            f"### 2.{number + 1} Phase {number + 1} — {PHASES[number]}"
            if number < len(PHASES)
            else "## 3. Sequencing non-derogation"
        )
        phase = section(engine, heading, next_heading)
        if not re.search(r"\b(?:SHALL|MUST|MUST NOT|SHALL NOT)\b", phase):
            issues.append(f"Phase {number} lacks a normative constitutional requirement")

    if positions and positions != sorted(positions):
        issues.append("phase headings are not in canonical order")

    for label in TECHNICAL_PHASE_LABELS:
        if label in operative:
            issues.append(f"constitutional phase uses implementation-style field label: {label}")

    code_leakage = sorted(set(SCOPED_DOMAIN_CODE_RE.findall(operative)))
    if code_leakage:
        issues.append(
            "constitutional processing spine embeds subordinate domain code families: "
            + ", ".join(code_leakage)
        )

    required_invariants = (
        "The canonical order is Phase 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10.",
        "No phase may be treated as satisfied by the result of a later phase.",
        "Commitment does not create authority.",
        "Representation does not create authority, execution, success or completion.",
        "Evidence does not retroactively authorise an action that lacked authority when undertaken.",
        "A material change invalidates every prior determination whose basis it changes.",
    )
    for invariant in required_invariants:
        if invariant not in operative:
            issues.append(f"constitutional runtime invariant is absent: {invariant}")

    if "Tendeka" not in operative:
        issues.append("constitutional runtime engine lacks Tendeka interruption/re-entry treatment")
    if "earliest materially affected phase" not in operative:
        issues.append("constitutional runtime engine lacks earliest-affected-phase re-entry")
    if "linked Phase 1 cycle" not in operative:
        issues.append("material subordinate actions lack linked Phase 1 re-entry")

    existing = instrument_ids(root)
    for authority in REQUIRED_AUTHORITIES:
        if authority not in existing:
            issues.append(f"constitutional authority does not exist: {authority}")

    operations = (root / OPERATIONS).read_text(encoding="utf-8")
    transitions = (root / TRANSITIONS).read_text(encoding="utf-8")
    if "MUST NOT reorder, omit or independently redefine the constitutional phases" not in operations:
        issues.append("OPERATIONS lacks topology non-redefinition boundary")
    if "No exceptional transition may be recorded as execution success" not in transitions:
        issues.append("operational transitions may manufacture execution success")
    if "never directly to Phase 7 or Phase 8" not in transitions:
        issues.append("operational pause release may bypass governance re-entry")
    if "Open a linked Phase 1 cycle" not in transitions:
        issues.append("tool-mediated sub-actions lack linked governance re-entry")

    profile_authority = re.compile(
        r"(?:profile|record|serialization).{0,80}(?:creates?|grants?|confers?|authori[sz]es?) execution authority",
        re.IGNORECASE | re.DOTALL,
    )
    for profile in PROFILES:
        text = (root / profile).read_text(encoding="utf-8")
        if profile_authority.search(text):
            issues.append(f"profile creates execution authority: {profile}")

    issues.extend(migration_assurance_issues(root))
    return issues


def main() -> int:
    issues = validate()
    if issues:
        print("Runtime-processing architecture validation failed:", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(
        "Runtime-processing architecture validation passed "
        "(10-phase constitutional topology; authority, re-entry, representation and migration-assurance boundaries intact)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
