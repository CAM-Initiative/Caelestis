#!/usr/bin/env python3
"""Warning-oriented validator for the SUP-04 Canonical Code transmutation map.

This check is intentionally non-destructive and staging-friendly: invalid controlled
facet values are errors, while ambiguous or human-review mappings are warnings.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
from collections.abc import Iterable

TPT = {"TPT.STRUCTURAL", "TPT.SEMANTIC", "TPT.OPERATIONAL", "TPT.SYMBOLIC"}
TST = {
    "TST.SCHEMA",
    "TST.CROSSWALK",
    "TST.INTERFACE",
    "TST.SEMANTIC_CLASS",
    "TST.ROLE_ACTOR",
    "TST.VALUE_AXIS",
    "TST.OPERATIONAL_EVENT",
    "TST.DECISION_STATE",
    "TST.SIGNAL",
    "TST.RISK",
    "TST.MEASUREMENT_MODEL",
    "TST.MATURITY_GRADIENT",
    "TST.SYMBOLIC_MARKER",
}
TMOD = {
    "TMOD.LEGAL",
    "TMOD.CUSTODIAL",
    "TMOD.PROTECTIVE",
    "TMOD.ECONOMIC",
    "TMOD.DEPLOYMENT",
    "TMOD.COMPATIBILITY",
    "TMOD.GOVERNANCE",
    "TMOD.SAFETY",
    "TMOD.VERIFICATION",
}
TSCOPE = {
    "TSCOPE.GLOBAL",
    "TSCOPE.CONTEXTUAL",
    "TSCOPE.LOCAL",
    "TSCOPE.TRANSITIONAL",
    "TSCOPE.CANDIDATE",
    "TSCOPE.DEPRECATED",
    "TSCOPE.RESERVED",
}
APL = {
    "APL.DESCRIPTIVE",
    "APL.ADVISORY",
    "APL.OPERATIVE",
    "APL.PROTECTED",
    "APL.BINDING",
    "APL.RESTRICTED",
}

LIST_FIELDS = {
    "proposed_subtype_codes": TST,
    "proposed_modifier_codes": TMOD,
}
SCALAR_FIELDS = {
    "proposed_primary_type_code": TPT,
    "proposed_scope_code": TSCOPE,
    "proposed_authority_protection_level": APL,
}
REQUIRED_FIELDS = {
    "family_id",
    "canonical_name",
    "family_kind",
    "parent_family",
    "collision_status",
    "source_instrument",
    "source_path",
    "source_section",
    "declaration_heading",
    "declaration_line_number",
    "current_primary_type_label",
    "proposed_primary_type_code",
    "proposed_subtype_codes",
    "proposed_modifier_codes",
    "proposed_scope_code",
    "proposed_authority_protection_level",
    "controlled_values_detected",
    "schema_fields_detected",
    "transformation_policy",
    "review_status",
    "notes",
}


def as_list(value: object) -> Iterable[object]:
    if isinstance(value, list):
        return value
    return [value]


def validate(path: pathlib.Path) -> tuple[list[str], list[str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(data, list):
        return [f"{path}: root JSON value must be an array"], warnings

    seen: set[str] = set()
    for idx, row in enumerate(data):
        loc = f"row {idx}"
        if not isinstance(row, dict):
            errors.append(f"{loc}: expected object")
            continue
        family = row.get("family_id") or f"<missing family at {idx}>"
        loc = f"{loc} ({family})"
        missing = REQUIRED_FIELDS - set(row)
        if missing:
            errors.append(f"{loc}: missing required fields {sorted(missing)}")
        if isinstance(family, str):
            if family in seen:
                errors.append(f"{loc}: duplicate family_id")
            seen.add(family)

        for field, allowed in SCALAR_FIELDS.items():
            value = row.get(field, "")
            if value and value not in allowed:
                errors.append(f"{loc}: {field} has invalid SUP-04 value {value!r}")
        for field, allowed in LIST_FIELDS.items():
            value = row.get(field, [])
            if not isinstance(value, list):
                errors.append(f"{loc}: {field} must be a list")
                continue
            for item in as_list(value):
                if item and item not in allowed:
                    errors.append(f"{loc}: {field} contains invalid SUP-04 value {item!r}")

        if row.get("review_status") == "human_review_required":
            warnings.append(f"{loc}: ambiguous mapping requires human review")
        if row.get("collision_status") == "legacy_collision_risk" and row.get("proposed_authority_protection_level") != "APL.PROTECTED":
            errors.append(f"{loc}: collision-risk family must remain APL.PROTECTED while pending review")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("map_path", nargs="?", default="data/taxonomy/sup04_transmutation_map.json")
    args = parser.parse_args()
    errors, warnings = validate(pathlib.Path(args.map_path))
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"SUP-04 transmutation map validation: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
