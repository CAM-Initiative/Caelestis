#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, pathlib, re, sys
from typing import NamedTuple

CANONICAL_SECTION_RE = re.compile(r"^#+\s+(?:\d+(?:\.\d+)*\s+)?Canonical Code & Reference Set Declarations\s*$", re.IGNORECASE)
SUBSECTION_RE = re.compile(r"^###\s+(.*)$")
REQUIRED_FIELD = "Code Family"
EXPECTED_FIELDS = {
    "Code Family","Canonical Name","Primary Type","Subtype","Modifier","Scope","Status",
    "Controlled Values Defined","Schema Field(s)","Source Instrument","Source Section",
    "Domain Namespace","Authority / Protection Level","Consumes Code Families",
    "Crosswalks Code Families","Operationalises or Applies Code Families",
}

class Entry(NamedTuple):
    code_family: str
    canonical_name: str
    primary_type: str
    subtype: str
    modifier: str
    scope: str
    status: str
    controlled_values_defined: list[str]
    schema_fields: str
    source_instrument: str
    source_section: str
    domain_namespace: str
    authority_protection_level: str
    consumes_code_families: list[str]
    crosswalks_code_families: list[str]
    operationalises_or_applies_code_families: list[str]
    declaration_heading: str
    declaration_line_number: int
    source_path: str
    family_id: str
    family_kind: str
    parent_family: str
    hierarchy_path: list[str]
    collision_status: str
    registry_note: str
    table: dict[str, str]


def split_list(v: str) -> list[str]:
    if not v.strip():
        return []
    return [x.strip() for x in v.split(",") if x.strip()]


def norm_heading(line: str) -> str:
    return re.sub(r"^#+\s*", "", line).strip()


def parse_table(lines: list[str], start_idx: int) -> tuple[dict[str, str], int]:
    data: dict[str, str] = {}
    i = start_idx
    while i < len(lines):
        s = lines[i].strip()
        if not s.startswith("|"):
            break
        cols = [c.strip() for c in s.strip().strip("|").split("|")]
        if len(cols) < 2:
            break
        if cols[0].lower() in {"field", "---", ""} or set(cols[0]) <= {"-",":"}:
            i += 1
            continue
        data[cols[0]] = cols[1]
        i += 1
    return data, i


def scan(root: pathlib.Path) -> list[Entry]:
    out: list[Entry] = []
    for p in sorted(root.glob("**/*.md")):
        lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
        i = 0
        in_canonical = False
        while i < len(lines):
            s = lines[i].strip()
            hm = re.match(r"^(#+)\s+", s)
            if hm and len(hm.group(1)) <= 2:
                in_canonical = bool(CANONICAL_SECTION_RE.match(s))
            if in_canonical:
                sub = SUBSECTION_RE.match(s)
                if sub:
                    heading = sub.group(1).strip()
                    line_no = i + 1
                    j = i + 1
                    while j < len(lines) and not lines[j].strip().startswith("|"):
                        if lines[j].strip().startswith("###") or lines[j].strip().startswith("##"):
                            break
                        j += 1
                    if j < len(lines) and lines[j].strip().startswith("|"):
                        table, end_i = parse_table(lines, j)
                        if REQUIRED_FIELD in table:
                            family_id = table.get("Code Family", "").strip()
                            heading_code = ""
                            hm = re.match(r"^\d+(?:\.\d+)*\s+([A-Z][A-Z0-9_.-]*)\s+[—-]\s+.+$", heading)
                            if hm:
                                heading_code = hm.group(1).strip()

                            explicit_parent = table.get("Parent Family", "").strip()
                            explicit_kind = table.get("Family Kind", "").strip().lower()
                            registry_note = table.get("Registry Note", "").strip()

                            if heading_code and heading_code.startswith(family_id + "."):
                                if not explicit_parent:
                                    explicit_parent = family_id
                                family_id = heading_code
                                if not explicit_kind:
                                    explicit_kind = "subfamily"

                            if not explicit_kind:
                                if explicit_parent:
                                    explicit_kind = "subfamily"
                                elif "." in family_id:
                                    explicit_kind = "standalone_family"
                                elif len(family_id) == 1 and family_id.isalpha():
                                    explicit_kind = "legacy_global_family"
                                else:
                                    explicit_kind = "standalone_family"

                            hierarchy_path = family_id.split(".") if family_id else []
                            if explicit_parent and not family_id.startswith(explicit_parent + "."):
                                collision_status = "invalid_parent"
                            elif explicit_kind == "subfamily" and not explicit_parent:
                                collision_status = "ambiguous_subfamily"
                            elif explicit_kind == "legacy_global_family":
                                collision_status = "legacy_collision_risk"
                            else:
                                collision_status = "none"

                            out.append(Entry(
                                code_family=family_id,
                                canonical_name=table.get("Canonical Name", "").strip(),
                                primary_type=table.get("Primary Type", "").strip(),
                                subtype=table.get("Subtype", "").strip(),
                                modifier=table.get("Modifier", "").strip(),
                                scope=table.get("Scope", "").strip(),
                                status=table.get("Status", "").strip(),
                                controlled_values_defined=split_list(table.get("Controlled Values Defined", "")),
                                schema_fields=table.get("Schema Field(s)", "").strip(),
                                source_instrument=table.get("Source Instrument", "").strip() or p.stem,
                                source_section=table.get("Source Section", "").strip(),
                                domain_namespace=table.get("Domain Namespace", "").strip(),
                                authority_protection_level=table.get("Authority / Protection Level", "").strip(),
                                consumes_code_families=split_list(table.get("Consumes Code Families", "")),
                                crosswalks_code_families=split_list(table.get("Crosswalks Code Families", "")),
                                operationalises_or_applies_code_families=split_list(table.get("Operationalises or Applies Code Families", "")),
                                declaration_heading=heading,
                                declaration_line_number=line_no,
                                source_path=str(p.as_posix()),
                                family_id=family_id,
                                family_kind=explicit_kind,
                                parent_family=explicit_parent,
                                hierarchy_path=hierarchy_path,
                                collision_status=collision_status,
                                registry_note=registry_note,
                                table=table,
                            ))
                        i = end_i
                        continue
            i += 1
    return out


def validate(entries: list[Entry]) -> list[str]:
    errs: list[str] = []
    by_family: dict[str, list[Entry]] = {}
    for e in entries:
        if not e.code_family:
            errs.append(f"Malformed canonical declaration row: {e.source_path}:{e.declaration_line_number} missing Code Family")
        missing = EXPECTED_FIELDS - set(e.table.keys())
        if missing:
            errs.append(f"Malformed canonical declaration row: {e.source_path}:{e.declaration_line_number} missing fields {sorted(missing)}")
        by_family.setdefault(e.code_family, []).append(e)
    for fam, rows in by_family.items():
        instruments = {pathlib.Path(r.source_path).stem for r in rows}
        if len(instruments) > 1:
            errs.append(f"Duplicate Code Family across instruments: {fam} -> {sorted(instruments)}")
        ptypes = {r.primary_type for r in rows if r.primary_type}
        if len(ptypes) > 1:
            errs.append(f"Conflicting Primary Type for Code Family {fam}: {sorted(ptypes)}")
    return errs


def write_md(path: pathlib.Path, entries: list[Entry]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write("# Canonical Code Index\n\n")
        f.write("| Family ID | Canonical Name | Family Kind | Parent Family | Collision Status | Primary Type | Source Instrument | Source Path | Declaration Heading | Line |\n")
        f.write("|---|---|---|---|---|---|---|---|---|---:|\n")
        for e in entries:
            parent = e.parent_family if e.parent_family else "—"
            note = f" ({e.registry_note})" if e.registry_note else ""
            f.write(f"| `{e.family_id}` | {e.canonical_name} | {e.family_kind}{note} | `{parent}` | {e.collision_status} | {e.primary_type} | `{e.source_instrument}` | `{e.source_path}` | {e.declaration_heading} | {e.declaration_line_number} |\n")


def sort_entries(entries: list[Entry]) -> list[Entry]:
    return sorted(
        entries,
        key=lambda e: (e.code_family.casefold(), e.source_instrument.casefold(), e.source_path.casefold(), e.declaration_line_number),
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="Governance")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--md-out", default=".github/Indices/canonical-code-index.md")
    ap.add_argument("--json-out", default=".github/Indices/canonical-code-index.json")
    args = ap.parse_args()
    entries = sort_entries(scan(pathlib.Path(args.root)))
    write_md(pathlib.Path(args.md_out), entries)
    pathlib.Path(args.json_out).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(args.json_out).write_text(json.dumps([e._asdict() for e in entries], indent=2), encoding="utf-8")
    errs = validate(entries)
    for e in errs:
        print(f"WARNING: {e}")
    return 1 if args.check and errs else 0

if __name__ == "__main__":
    sys.exit(main())
