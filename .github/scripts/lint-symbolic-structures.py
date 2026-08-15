#!/usr/bin/env python3
"""Validate current canonical references against source-derived declarations.

The historical symbolic registry is not an authority input. The operative
contract is derived from the same declarations used to build
Governance/CAM.Canonical.Code.Index.json, then applied to current Governance
Markdown. Dots are never used to infer parentage.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INDEX = REPO_ROOT / "Governance" / "CAM.Canonical.Code.Index.json"
LEGACY_REGISTRY = REPO_ROOT / ".github" / "Indices" / "CAM.Governance.Symbolic-Structures.Registry.json"
TOKEN = r"[A-Z][A-Z0-9]*(?:[._-][A-Z0-9](?:[A-Z0-9_.-]*[A-Z0-9])?)*"
INLINE_SPAN_RE = re.compile(r"`([^`]+)`")
TOKEN_RE = re.compile(r"^(" + TOKEN + r")$")
INSTRUMENT_RE = re.compile(r"^(?:CAM|VIGIL)-[A-Z0-9-]+$")
HISTORICAL_HEADINGS = (
    "amendment ledger", "historical", "retired", "superseded",
    "legacy compatibility", "migration record",
)
AMBIGUOUS_HEADINGS = ("example", "illustrative", "template", "syntax", "construction pattern", "proposed")


def is_active_status(status: str) -> bool:
    norm = status.strip().casefold()
    return not norm.startswith(("retired", "deprecated", "proposed", "historical", "superseded"))


def load_builder():
    path = Path(__file__).with_name("build-canonical-code-index.py")
    spec = importlib.util.spec_from_file_location("canonical_index_builder", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load canonical index builder: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root.parent).as_posix()
    except ValueError:
        return path.as_posix()


def operative_markdown(root: Path) -> list[Path]:
    excluded = {"CAM.Canonical.Code.Index.md", "CAM.Governance.JSON.md"}
    return [
        path for path in sorted(root.glob("**/*.md"))
        if "Drafts" not in path.parts and path.name not in excluded
    ]


def heading_context(lines: list[str]) -> list[str]:
    stack: list[tuple[int, str]] = []
    contexts: list[str] = []
    for line in lines:
        match = re.match(r"^(#{1,6})\s+(.*?)\s*$", line.strip())
        if match:
            level = len(match.group(1))
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, match.group(2)))
        contexts.append(" > ".join(text for _, text in stack))
    return contexts


def candidate_tokens(line: str, roots: set[str], identifiers: set[str], values: set[str]) -> set[str]:
    found = set()
    for span in INLINE_SPAN_RE.findall(line):
        match = TOKEN_RE.fullmatch(span.strip())
        if match:
            token = match.group(1)
            if "." in token or token in identifiers or token in values:
                found.add(token)
    # Plain-text scanning is namespace-bound. Unknown namespaces still fail
    # when expressed as inline-code governance identifiers.
    if roots:
        root_pattern = "|".join(sorted((re.escape(root) for root in roots), key=len, reverse=True))
        found.update(re.findall(r"(?<![A-Z0-9-])(?:" + root_pattern + r")(?:\.[A-Z0-9][A-Z0-9_.-]*)+\b", line))
    for token in identifiers | values:
        if len(token) == 1 and re.search(r"(?<![A-Z0-9_.-])" + re.escape(token) + r"(?![A-Z0-9_.-])", line):
            found.add(token)
    return {
        token.rstrip(".,;:") for token in found
        if not INSTRUMENT_RE.match(token)
        and not re.match(r"^[A-Z]+-\d{3}(?:-|$)", token)
        and not token.endswith(("-", ".", "_"))
    }


def source_projection(builder: Any, root: Path) -> tuple[list[Any], list[str]]:
    rows = builder.mark_duplicate_source_declarations(builder.sort_entries(builder.scan(root)))
    return rows, builder.validate(rows)


def generated_index_errors(index_path: Path, rows: list[Any]) -> list[str]:
    if not index_path.exists():
        return [f"Required current canonical index not found: {index_path}"]
    try:
        loaded = json.loads(index_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Unable to load current canonical index {index_path}: {exc}"]
    if not isinstance(loaded, list):
        return [f"Current canonical index must be a JSON array: {index_path}"]
    if loaded != [row._asdict() for row in rows]:
        return ["Generated canonical index disagrees with source-derived declarations; rebuild Governance/CAM.Canonical.Code.Index.json"]
    return []


def alias_tokens(row: Any) -> set[str]:
    aliases = set()
    for field in ("Aliases", "Compatibility Aliases", "Deprecated Aliases"):
        aliases.update(re.findall(TOKEN, row.table.get(field, "")))
    return aliases


def classify_references(root: Path, rows: list[Any]) -> tuple[list[dict[str, Any]], list[str]]:
    by_id = {row.canonical_id: row for row in rows}
    by_family = {row.family_id: row for row in rows}
    identifiers = set(by_id) | set(by_family)
    values: dict[str, Any] = {}
    aliases: dict[str, Any] = {}
    for row in rows:
        for value in row.controlled_values_defined:
            values[value] = row
        for alias in alias_tokens(row):
            aliases[alias] = row
    roots = {token.split(".", 1)[0].split("-", 1)[0] for token in identifiers | set(values)}
    errors: list[str] = []
    inventory: list[dict[str, Any]] = []

    for path in operative_markdown(root):
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        contexts = heading_context(lines)
        rel = relative(path, root)
        for line_no, (line, section) in enumerate(zip(lines, contexts), start=1):
            historical = any(term in section.casefold() for term in HISTORICAL_HEADINGS)
            expressly_historical = (
                "retired and historical only" in line.casefold()
                or "retired and retained only" in line.casefold()
                or "historical version context" in line.casefold()
                or ("former" in line.casefold() and "is retired" in line.casefold())
            )
            illustrative = (
                any(term in section.casefold() for term in AMBIGUOUS_HEADINGS)
                or "shall not be promoted as" in line.casefold()
                or "should not be created" in line.casefold()
                or "<domain>" in line.casefold()
            )
            for token in sorted(candidate_tokens(line, roots, identifiers, set(values))):
                row = by_id.get(token) or by_family.get(token)
                owner = row.source_path if row else ""
                role = "consumption"
                status = ""
                family = ""
                result = "ambiguous-token"

                if row:
                    status = row.status or "Active"
                    family = row.family_id
                    active = is_active_status(status)
                    if (historical or expressly_historical) and not active:
                        result = "permitted-historical-use"
                    elif not active and Path(owner).as_posix() == path.as_posix():
                        result = "valid-alias-or-compatibility-use"
                        role = "definition"
                    elif not active:
                        result = "stale-or-retired-current-use"
                    elif row.identifier_type == "reference_set":
                        result = "valid-reference-set"
                    elif row.identifier_type in {"canonical_constraint", "canonical_obligation"}:
                        result = "valid-constraint-or-obligation"
                    elif row.family_kind == "subfamily":
                        result = "valid-subfamily-reference"
                    else:
                        result = "valid-family-reference"
                    if Path(owner).as_posix() == path.as_posix() and (
                        "canonical" in section.casefold() or "declaration" in section.casefold()
                    ):
                        role = "definition"
                elif token in values:
                    row = values[token]
                    owner = row.source_path
                    family = row.family_id
                    status = row.status or "Active"
                    active = is_active_status(status)
                    if (historical or expressly_historical) and not active:
                        result = "permitted-historical-use"
                    elif not active and Path(owner).as_posix() == path.as_posix() and (
                        "canonical" in section.casefold() or "declaration" in section.casefold()
                    ):
                        result = "valid-alias-or-compatibility-use"
                        role = "definition"
                    elif not active:
                        result = "stale-or-retired-current-use"
                    else:
                        result = "valid-controlled-value"
                elif token in aliases:
                    row = aliases[token]
                    owner = row.source_path
                    family = row.family_id
                    status = row.status or "Active"
                    result = "permitted-historical-use" if historical else "valid-alias-or-compatibility-use"
                elif historical:
                    result = "permitted-historical-use"
                elif illustrative:
                    result = "ambiguous-token"
                else:
                    prefix_rows = [
                        (candidate, candidate_row)
                        for candidate, candidate_row in by_family.items()
                        if token.startswith(candidate + ".") or token.startswith(candidate + "-")
                    ]
                    if prefix_rows:
                        family, row = max(prefix_rows, key=lambda item: len(item[0]))
                        owner = row.source_path
                        status = row.status or "Active"
                        result = "unknown-value"
                    else:
                        result = "unknown-family"

                item = {
                    "code": token,
                    "family": family,
                    "sourceFile": rel,
                    "line": line_no,
                    "section": section,
                    "semanticRole": role,
                    "expectedSourceAuthority": owner,
                    "status": status,
                    "resolution": result,
                }
                inventory.append(item)

                if result in {"unknown-family", "unknown-value", "stale-or-retired-current-use"}:
                    errors.append(f"{rel}:{line_no} {result}: {token}")
                owner_claim = re.search(
                    r"\bthis\s+(?:charter|instrument|appendix|annex|schedule|supplement)\s+source-authoritatively\s+defines\b(.*)",
                    line,
                    re.IGNORECASE,
                )
                if row and owner_claim:
                    claimed = candidate_tokens(owner_claim.group(1), roots, identifiers, set(values))
                    first_claimed = next(iter(sorted(claimed, key=lambda value: line.find(value))), None)
                    if token == first_claimed and Path(owner).name != path.name:
                        errors.append(f"{rel}:{line_no} wrong-source-owner: {token} is owned by {owner}")

    return inventory, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate source-derived canonical reference integrity")
    parser.add_argument("--root", default="Governance")
    parser.add_argument("--index", default=str(DEFAULT_INDEX))
    parser.add_argument("--registry", default=str(LEGACY_REGISTRY))
    parser.add_argument("--require-index", action="store_true")
    parser.add_argument("--require-registry", action="store_true")
    parser.add_argument("--strict-release", action="store_true")
    parser.add_argument("--canonical-codes-enforcement", choices=["off", "warning", "error"], default="error")
    parser.add_argument("--inventory-out")
    args = parser.parse_args()

    root = Path(args.root)
    builder = load_builder()
    rows, declaration_errors = source_projection(builder, root)
    errors = list(declaration_errors)
    errors.extend(generated_index_errors(Path(args.index), rows))
    inventory, reference_errors = classify_references(root, rows)
    errors.extend(reference_errors)

    registry_path = Path(args.registry)
    if registry_path.exists():
        print(f"INFO: legacy symbolic registry present but not used as source authority: {registry_path}")
    elif args.require_registry:
        errors.append(f"Required legacy registry file not found: {registry_path}")
    else:
        print("INFO: legacy symbolic registry absent; current source-derived reference validation remains active")

    counts = Counter(item["resolution"] for item in inventory)
    report = {
        "schemaVersion": "1.0",
        "declarationCount": len(rows),
        "referenceCount": len(inventory),
        "resolutionTotals": dict(sorted(counts.items())),
        "references": inventory,
    }
    if args.inventory_out:
        output = Path(args.inventory_out)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    for error in sorted(set(errors)):
        print(f"ERROR: {error}")
    print(
        f"SUMMARY: declarations={len(rows)} references={len(inventory)} "
        f"errors={len(set(errors))} source_derived=yes"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
