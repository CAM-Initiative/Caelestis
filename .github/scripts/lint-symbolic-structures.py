#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = REPO_ROOT / ".github" / "Indices" / "CAM.Governance.Symbolic-Structures.Index.json"
REGISTRY_PATH = REPO_ROOT / ".github" / "Indices" / "CAM.Governance.Symbolic-Structures.Registry.json"

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

CODE_TOKEN_RE = re.compile(r"\b([A-Z]{1,6}(?:-[A-Z0-9.]+|[0-9][A-Z0-9.]*)?)\b")


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


def extract_instrument_id(path: Path) -> str:
    return path.stem


def extract_canonical_codes_row(text: str) -> str | None:
    for line in text.splitlines():
        if re.match(r"^\|\s*Canonical Codes\s*\|", line):
            parts = [p.strip() for p in line.strip().strip("|").split("|")]
            if len(parts) >= 2:
                return parts[1]
    return None


def parse_canonical_codes(cell: str) -> dict[str, set[str]]:
    parsed: dict[str, set[str]] = {}
    chunks = [c.strip() for c in cell.split(";") if c.strip()]
    for chunk in chunks:
        m = re.match(r"^([A-Z]{1,6})\s*—\s*[^:]+:\s*(.+)$", chunk)
        if not m:
            continue
        prefix = m.group(1)
        codes = {c.strip() for c in m.group(2).split(",") if c.strip()}
        parsed.setdefault(prefix, set()).update(codes)
    return parsed


def lint_canonical_codes(*, registry: dict, enforcement: str, strict_release: bool) -> tuple[list[str], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    infos: list[str] = []

    md_files = sorted(REPO_ROOT.glob("Governance/**/*.md"))
    reg_by_prefix: dict[str, set[str]] = {}
    canonical_source_prefixes: dict[str, dict[str, set[str]]] = {}
    for row in registry.get("canonical_registered_structures", []):
        prefix = row.get("prefix", "")
        if not prefix:
            continue
        values = set(row.get("canonical_codes", row.get("values", [])))
        reg_by_prefix[prefix] = values
        src = row.get("canonical_source_instrument", "")
        if src:
            canonical_source_prefixes.setdefault(src, {}).setdefault(prefix, set()).update(values)

    for path in md_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        row = extract_canonical_codes_row(text)
        rel = path.relative_to(REPO_ROOT).as_posix()

        if row is None:
            msg = f"Missing Canonical Codes metadata row: {rel}"
            if enforcement == "error" or strict_release:
                errors.append(msg)
            elif enforcement == "warning":
                warnings.append(msg)
            continue

        if row.strip().lower() == "none":
            infos.append(f"Canonical Codes skipped (None): {rel}")
            continue

        declared = parse_canonical_codes(row)
        if not declared:
            warnings.append(f"Canonical Codes row could not be parsed: {rel}")
            continue

        all_tokens = set(CODE_TOKEN_RE.findall(text))
        for prefix, codes in declared.items():
            if prefix not in reg_by_prefix:
                msg = f"Unknown prefix in Canonical Codes metadata: {rel}: {prefix}"
                errors.append(msg) if strict_release else warnings.append(msg)
                continue
            reg_codes = reg_by_prefix[prefix]
            for code in sorted(codes):
                if code not in reg_codes:
                    msg = f"Unregistered code for known prefix: {rel}: {prefix}:{code}"
                    errors.append(msg) if strict_release else warnings.append(msg)
                if code not in all_tokens:
                    msg = f"Code listed in instrument metadata but not found in source text: {rel}: {code}"
                    errors.append(msg) if strict_release else warnings.append(msg)

        instrument_id = extract_instrument_id(path)
        if instrument_id in canonical_source_prefixes:
            for prefix, reg_codes in canonical_source_prefixes[instrument_id].items():
                declared_codes = declared.get(prefix, set())
                missing = sorted(code for code in reg_codes if code not in declared_codes)
                for code in missing:
                    msg = (
                        f"Code listed in symbolic registry but absent from Canonical Codes metadata: "
                        f"{rel}: {prefix}:{code}"
                    )
                    errors.append(msg) if strict_release else warnings.append(msg)

    return errors, warnings, infos


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint symbolic structures index")
    parser.add_argument("--index", default=str(INDEX_PATH))
    parser.add_argument("--registry", default=str(REGISTRY_PATH))
    parser.add_argument("--strict-release", action="store_true", help="Treat registry mismatches/collisions as errors")
    parser.add_argument(
        "--canonical-codes-enforcement",
        choices=["off", "warning", "error"],
        default="warning",
        help="How to treat missing Canonical Codes metadata rows in normal mode",
    )
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
        if args.strict_release:
            errors.append(msg)
        elif row.get("severity") == "error":
            errors.append(msg)
        else:
            warnings.append(msg)

    cc_errors, cc_warnings, cc_infos = lint_canonical_codes(
        registry=registry,
        enforcement=args.canonical_codes_enforcement,
        strict_release=args.strict_release,
    )
    errors.extend(cc_errors)
    warnings.extend(cc_warnings)

    for info in cc_infos:
        print(f"INFO: {info}")
    for w in sorted(set(warnings)):
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")

    print(
        "SUMMARY: "
        f"warnings={len(set(warnings))} errors={len(errors)} "
        f"strict_release={'yes' if args.strict_release else 'no'} "
        f"canonical_codes_enforcement={args.canonical_codes_enforcement}"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
