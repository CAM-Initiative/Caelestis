#!/usr/bin/env python3
"""Validate disposition coverage for the pre-refactor constitutional runtime schedules."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / ".github/Reviews/RUNTIME-MIGRATION-ASSURANCE-REGISTER.json"
CONSTITUTION = ROOT / "Governance/Constitution"

EXPECTED_LEGACY_SCHEDULES = {
    "CAM-BS2025-AEON-001-SCH-01",
    "CAM-BS2025-AEON-002-SCH-01",
    "CAM-BS2025-AEON-002-SCH-02",
    "CAM-BS2025-AEON-003-SCH-01",
    "CAM-BS2025-AEON-003-SCH-02",
    "CAM-BS2025-AEON-003-SCH-03",
    "CAM-BS2025-AEON-003-SCH-04",
    "CAM-BS2025-AEON-003-SCH-05",
    "CAM-BS2025-AEON-005-SCH-01",
    "CAM-BS2025-AEON-005-SCH-02",
    "CAM-BS2025-AEON-005-SCH-03",
    "CAM-BS2025-AEON-005-SCH-04",
    "CAM-BS2025-AEON-006-SCH-01",
    "CAM-BS2025-AEON-006-SCH-02",
    "CAM-BS2025-AEON-006-SCH-03",
    "CAM-BS2025-AEON-006-SCH-04",
    "CAM-BS2025-AEON-006-SCH-05",
    "CAM-BS2025-AEON-006-SCH-06",
    "CAM-BS2025-AEON-006-SCH-07",
    "CAM-BS2026-AEON-007-SCH-01",
    "CAM-BS2026-AEON-008-SCH-01",
    "CAM-BS2026-AEON-008-SCH-02",
    "CAM-BS2026-AEON-008-SCH-03",
    "CAM-BS2026-AEON-010-SCH-01",
    "CAM-BS2026-AEON-013-SCH-01",
    "CAM-BS2026-AEON-013-SCH-02",
    "CAM-BS2026-AEON-014-SCH-01",
}

EXPECTED_CURRENT_SCHEDULES = {
    "CAM-BS2025-AEON-001-SCH-01",
    "CAM-BS2025-AEON-002-SCH-01",
    "CAM-BS2025-AEON-003-SCH-02",
    "CAM-BS2025-AEON-005-SCH-04",
    "CAM-BS2026-AEON-007-SCH-01",
    "CAM-BS2026-AEON-010-SCH-01",
    "CAM-BS2026-AEON-013-SCH-01",
}

ALLOWED_COVERAGE = {
    "exact",
    "semantic-equivalent",
    "partial",
    "missing",
    "conflicting",
    "deliberately-retired-nonoperative",
}
UNRESOLVED_COVERAGE = {"partial", "missing", "conflicting"}


def load_register(root: Path = ROOT) -> dict:
    path = root / REGISTER.relative_to(ROOT)
    return json.loads(path.read_text(encoding="utf-8"))


def current_schedule_ids(root: Path = ROOT) -> set[str]:
    constitution = root / CONSTITUTION.relative_to(ROOT)
    return {path.stem for path in constitution.glob("CAM-*-SCH-*.md")}


def validate(root: Path = ROOT) -> list[str]:
    issues: list[str] = []
    path = root / REGISTER.relative_to(ROOT)
    if not path.exists():
        return [f"missing runtime migration assurance register: {path.relative_to(root)}"]

    data = load_register(root)
    records = data.get("records", [])
    ids = [record.get("legacy_instrument") for record in records]

    if len(ids) != len(set(ids)):
        issues.append("runtime migration assurance register contains duplicate legacy_instrument values")

    actual_ids = {value for value in ids if isinstance(value, str)}
    missing = EXPECTED_LEGACY_SCHEDULES - actual_ids
    extra = actual_ids - EXPECTED_LEGACY_SCHEDULES
    if missing:
        issues.append("legacy runtime schedules lack disposition: " + ", ".join(sorted(missing)))
    if extra:
        issues.append("unexpected legacy schedule disposition entries: " + ", ".join(sorted(extra)))

    baseline = data.get("source_baseline", {})
    if baseline.get("main_schedule_count") != len(EXPECTED_LEGACY_SCHEDULES):
        issues.append("main_schedule_count does not match the protected legacy schedule inventory")
    if baseline.get("current_constitutional_schedule_count") != len(EXPECTED_CURRENT_SCHEDULES):
        issues.append("current_constitutional_schedule_count does not match the protected current schedule set")

    rules = data.get("rules", {})
    if rules.get("runtime_phase_count_frozen") != 10:
        issues.append("runtime_phase_count_frozen must remain 10")
    if rules.get("constitutional_topology_changes_are_out_of_scope") is not True:
        issues.append("constitutional topology must remain explicitly out of scope for migration assurance")

    actual_current = current_schedule_ids(root)
    if actual_current != EXPECTED_CURRENT_SCHEDULES:
        issues.append(
            "current constitutional schedule set drifted; expected "
            + ", ".join(sorted(EXPECTED_CURRENT_SCHEDULES))
            + "; found "
            + ", ".join(sorted(actual_current))
        )

    for record in records:
        legacy = record.get("legacy_instrument", "<unknown>")
        coverage = record.get("coverage")
        if coverage not in ALLOWED_COVERAGE:
            issues.append(f"{legacy}: invalid coverage value {coverage!r}")
        if coverage in UNRESOLVED_COVERAGE:
            issues.append(f"{legacy}: unresolved migration coverage remains {coverage}")

        owners = record.get("current_owners")
        if not isinstance(owners, list) or not owners:
            issues.append(f"{legacy}: current_owners must be a non-empty list")
            continue
        for owner in owners:
            if not isinstance(owner, str) or not owner.strip():
                issues.append(f"{legacy}: current owner path is blank or invalid")
                continue
            if not (root / owner).exists():
                issues.append(f"{legacy}: current owner does not exist: {owner}")

        basis = record.get("assurance_basis")
        action = record.get("action")
        if not isinstance(basis, str) or not basis.strip():
            issues.append(f"{legacy}: assurance_basis is required")
        if not isinstance(action, str) or not action.strip():
            issues.append(f"{legacy}: action is required")

        if coverage == "deliberately-retired-nonoperative":
            text = f"{basis or ''} {action or ''}".casefold()
            if not any(term in text for term in ("draft", "nonoperative", "not enforceable", "non-enforceable")):
                issues.append(f"{legacy}: deliberate retirement lacks a non-operative authority basis")

    return issues


def main() -> int:
    issues = validate()
    if issues:
        print("Runtime migration assurance validation failed:", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(
        "Runtime migration assurance validation passed "
        f"({len(EXPECTED_LEGACY_SCHEDULES)} legacy schedules dispositioned; "
        f"{len(EXPECTED_CURRENT_SCHEDULES)} current constitutional schedules protected)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
