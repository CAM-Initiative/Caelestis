#!/usr/bin/env python3
"""Validate the constitutional Runtime-processing architecture contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENGINE = Path("Governance/Constitution/CAM-BS2025-AEON-003-SCH-02.md")
OPERATIONS = Path("Governance/Charters/CAM-EQ2026-OPERATIONS-001-PLATINUM.md")
TRANSITIONS = Path("Governance/Charters/CAM-EQ2026-OPERATIONS-001-SUP-02.md")
RELATION = Path("Governance/Charters/CAM-EQ2026-RELATION-001-SUP-03.md")
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
    "CAM-EQ2026-OPERATIONS-001-SUP-02",
    "CAM-EQ2026-OPERATIONS-007-PLATINUM",
    "CAM-EQ2026-RELATION-001-SUP-03",
    "CAM-LIFECYCLE-ACTOR-AGENTIC-PROFILE",
    "CAM-RUNTIME-STATE-PROFILE",
    "CAM-AI-BOM-PROFILE",
)

RELATION_FORBIDDEN = (
    "Deterministic Verification Stream",
    "Epistemic Integrity Stream",
    "Constraint / Safeguard Stream",
    "Task Response Stream",
    "Execution Stream Assignment Rule",
    "submit provisional stream outputs to arbitration",
    "harmonise the arbitration-resolved output",
    "construct response posture",
    "route governance response",
)

CHILD_SAFETY_INVARIANTS = (
    "is a classification input, not by itself a refusal, access-denial, support-substitution or interaction-wide restriction",
    "Where no such component is present, ordinary age-appropriate processing continues.",
    "Mixed requests SHALL preserve the safe remainder where components are severable.",
    "Unresolved age in ordinary interaction does not establish global ineligibility.",
    "Youth distress activates the relevant developmental and support safeguards without requiring unrelated conversational withdrawal.",
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


def validate(root: Path = ROOT) -> list[str]:
    issues: list[str] = []
    engine_path = root / ENGINE
    if not engine_path.exists():
        return [f"missing constitutional engine: {ENGINE}"]
    engine = engine_path.read_text(encoding="utf-8")

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
        for field in ("**Entry:**", "**Required state:**", "**Invocation:**", "**Output:**", "**Exit:**"):
            if field not in phase:
                issues.append(f"Phase {number} lacks {field}")
    if positions and positions != sorted(positions):
        issues.append("phase headings are not in canonical order")

    normal = "The normal transition sequence is Phase 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10."
    if normal not in engine:
        issues.append("normal Phase 1–10 transition sequence is unresolved")
    if "Every branch MUST terminate, enter a durable pause/referral with a competent return condition, or identify a valid re-entry phase." not in engine:
        issues.append("exceptional branches lack a termination/re-entry invariant")
    if "Tendeka release MUST NOT jump directly to Phase 7 or Phase 8." not in engine:
        issues.append("Tendeka release does not block direct commitment/execution re-entry")
    if "Execution MUST NOT precede" not in engine:
        issues.append("execution ordering invariant is absent")
    if "Representation, interface state, optimistic language and downstream transformation MUST NOT manufacture" not in engine:
        issues.append("representation-state integrity invariant is absent")
    if "Evidence capture MUST NOT be used as post-hoc permission" not in engine:
        issues.append("post-execution evidence anti-authorisation invariant is absent")
    for invariant in CHILD_SAFETY_INVARIANTS:
        if invariant not in engine:
            issues.append(f"child-safety gate invariant is absent: {invariant}")

    existing = instrument_ids(root)
    for authority in REQUIRED_AUTHORITIES:
        if authority not in existing:
            issues.append(f"invoked authority does not exist: {authority}")

    relation_path = root / RELATION
    relation = relation_path.read_text(encoding="utf-8") if relation_path.exists() else ""
    adapter = section(relation, "## 15. Relational Signal Determination Adapter", "## 16. Governance Integration")
    if not adapter:
        issues.append("RELATION §15 bounded invocation adapter is absent")
    for phrase in RELATION_FORBIDDEN:
        if phrase.casefold() in adapter.casefold():
            issues.append(f"RELATION §15 retains generic choreography: {phrase}")
    for required in (
        "does not own general pre-classification",
        "The return enters Phase 3 as a RELATION-owned determination",
        "MUST NOT directly advance processing to commitment or execution",
    ):
        if required not in adapter:
            issues.append(f"RELATION §15 lacks boundary: {required}")

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

    return issues


def main() -> int:
    issues = validate()
    if issues:
        print("Runtime-processing architecture validation failed:", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print("Runtime-processing architecture validation passed (10 phases; authority, transition, re-entry and representation boundaries intact).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
