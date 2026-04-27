#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = REPO_ROOT / "Governance" / "Indices" / "CAM.Governance.Symbolic-Structures.Index.json"
REGISTRY_PATH = REPO_ROOT / "Governance" / "Indices" / "CAM.Governance.Symbolic-Structures.Registry.json"

REQUIRED_FIELDS = [
    "prefix",
    "canonical_name",
    "structure_type",
    "domain",
    "canonical_source_instrument",
    "canonical_source_title",
    "values",
    "protection_level",
    "status",
    "aliases",
    "related_prefixes",
    "notes",
]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_registry(registry: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(registry.get("canonical_registered_structures"), list):
        errors.append("canonical_registered_structures must be an array")
        return errors

    for i, row in enumerate(registry["canonical_registered_structures"]):
        if not isinstance(row, dict):
            errors.append(f"canonical_registered_structures[{i}] must be an object")
            continue
        for field in REQUIRED_FIELDS:
            if field not in row:
                errors.append(f"canonical_registered_structures[{i}] missing field: {field}")
        if "values" in row and not isinstance(row.get("values"), list):
            errors.append(f"{row.get('prefix','?')}: values must be an array")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint symbolic structures index")
    parser.add_argument("--index", default=str(INDEX_PATH))
    parser.add_argument("--registry", default=str(REGISTRY_PATH))
    args = parser.parse_args()

    index = load_json(Path(args.index))
    registry = load_json(Path(args.registry))

    errors: list[str] = []
    warnings: list[str] = []

    errors.extend([f"Malformed registry config: {e}" for e in validate_registry(registry)])

    for row in index.get("candidate_unregistered_prefixes", []):
        warnings.append(
            f"Candidate unregistered prefix '{row.get('prefix','')}' (confidence={row.get('confidence','low')}, reason={row.get('reason','')})"
        )

    for row in index.get("potential_duplicate_symbolic_structures", []):
        warnings.append(
            f"Possible duplicate symbolic structure '{row.get('normalized_title','')}' x{row.get('occurrences',0)}"
        )

    for row in index.get("possible_collisions_requiring_review", []):
        msg = (
            f"Collision '{row.get('collision_type','unknown')}' for {row.get('prefix','')}:{row.get('value','')} "
            f"(severity={row.get('severity','warning')}, reason={row.get('reason','')})"
        )
        if row.get("severity") == "error":
            errors.append(msg)
        else:
            warnings.append(msg)

    for w in sorted(set(warnings)):
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")

    print(f"SUMMARY: warnings={len(set(warnings))} errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
