#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, pathlib, re, sys
from typing import NamedTuple

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
CANONICAL_HEADING_PHRASES = {
    "canonical code & reference set",
    "canonical code & reference set declaration",
    "canonical code & reference set declarations",
    "canonical codes & reference sets",
    "canonical code status",
    "canonical code & reference set metadata",
    "canonical code & constraint declarations",
}
IDENTIFIER_FIELDS = [
    ("Code Family", "code_family"),
    ("Reference Set", "reference_set"),
    ("Canonical Constraint", "canonical_constraint"),
    ("Canonical Obligation", "canonical_obligation"),
]
CODE_FAMILY_EXPECTED_FIELDS = {
    "Code Family","Canonical Name","Primary Type","Subtype","Modifier","Scope","Status",
    "Controlled Values Defined","Schema Field(s)","Source Instrument","Source Section",
    "Domain Namespace","Authority / Protection Level","Consumes Code Families",
    "Crosswalks Code Families","Operationalises or Applies Code Families",
}
REFERENCE_SET_EXPECTED_FIELDS = {
    "Reference Set","Canonical Name","Primary Type","Controlled Values Defined",
    "Schema Field(s)","Source Instrument","Source Section","Domain Namespace",
    "Authority / Protection Level",
}
CONSTRAINT_EXPECTED_FIELDS = {
    "Canonical Name","Primary Type","Source Instrument","Source Section",
    "Domain Namespace","Authority / Protection Level",
}

class Entry(NamedTuple):
    canonical_id: str
    identifier_type: str
    code_family: str
    reference_set: str
    canonical_constraint: str
    canonical_obligation: str
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
    canonical_section_heading: str
    canonical_section_line_number: int
    declaration_heading: str
    declaration_line_number: int
    extraction_method: str
    declaration_quality: str
    missing_expected_fields: list[str]
    source_path: str
    family_id: str
    family_kind: str
    parent_family: str
    hierarchy_path: list[str]
    collision_status: str
    registry_note: str
    table: dict[str, str]

class Diagnostic(NamedTuple):
    source_path: str
    line_number: int
    message: str

DIAGNOSTICS: list[Diagnostic] = []

def strip_inline_code(value: str) -> str:
    value = value.strip()
    while len(value) >= 2 and value.startswith("`") and value.endswith("`"):
        value = value[1:-1].strip()
    return value

def split_list(v: str) -> list[str]:
    if not v.strip():
        return []
    return [strip_inline_code(x) for x in v.split(",") if strip_inline_code(x)]

def normalize_heading_text(text: str) -> str:
    text = re.sub(r"^\d+(?:\.\d+)*\.?\s*", "", text.replace("\xa0", " ")).strip()
    return re.sub(r"\s+", " ", text).casefold()

def is_canonical_heading(text: str) -> tuple[bool, str]:
    norm = normalize_heading_text(text)
    for phrase in CANONICAL_HEADING_PHRASES:
        if norm == phrase or norm.startswith(phrase + " ") or phrase in norm:
            quality = "complete" if norm == "canonical code & reference set declarations" else "nonstandard_section_heading"
            return True, quality
    return False, ""

def parse_heading(line: str):
    m = HEADING_RE.match(line.strip())
    if not m:
        return None
    return len(m.group(1)), m.group(2).strip()

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
        data[cols[0].strip("* ")] = cols[1]
        i += 1
    return data, i

def find_first_table(lines: list[str], start: int, end: int) -> tuple[dict[str,str], int] | tuple[None, None]:
    i = start
    while i < end:
        if lines[i].strip().startswith("|"):
            return parse_table(lines, i)
        i += 1
    return None, None

def table_identifier(table: dict[str, str]) -> tuple[str, str, str] | None:
    for field, identifier_type in IDENTIFIER_FIELDS:
        value = strip_inline_code(table.get(field, ""))
        if value:
            return field, identifier_type, value
    return None

def expected_fields_for(identifier_type: str) -> set[str]:
    if identifier_type == "code_family":
        return CODE_FAMILY_EXPECTED_FIELDS
    if identifier_type == "reference_set":
        return REFERENCE_SET_EXPECTED_FIELDS
    if identifier_type in {"canonical_constraint", "canonical_obligation"}:
        field = "Canonical Constraint" if identifier_type == "canonical_constraint" else "Canonical Obligation"
        return CONSTRAINT_EXPECTED_FIELDS | {field}
    return set()

def declaration_quality(table: dict[str,str], section_quality: str, identifier_type: str) -> tuple[str, list[str]]:
    expected = expected_fields_for(identifier_type)
    missing = sorted(expected - set(table.keys()))
    if section_quality == "nonstandard_section_heading":
        return "nonstandard_section_heading", missing
    return ("complete" if not missing else "missing_optional_fields"), missing

def infer_family_metadata(identifier_type: str, canonical_id: str, table: dict[str, str], heading: str):
    if identifier_type == "reference_set":
        return canonical_id, "reference_set", "", [], "none"
    if identifier_type == "canonical_constraint":
        return canonical_id, "canonical_constraint", "", [], "none"
    if identifier_type == "canonical_obligation":
        return canonical_id, "canonical_obligation", "", [], "none"

    family_id = canonical_id
    heading_code = ""
    hm = re.match(r"^\d+(?:\.\d+)*\s+`?([A-Z][A-Z0-9_.-]*)`?\s+[—-]\s+.+$", heading)
    if hm:
        heading_code = hm.group(1).strip()
    explicit_parent = strip_inline_code(table.get("Parent Family", ""))
    explicit_kind = table.get("Family Kind", "").strip().lower()
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
    return family_id, explicit_kind, explicit_parent, hierarchy_path, collision_status

def make_entry(p: pathlib.Path, table: dict[str,str], canonical_heading: str, canonical_line: int, section_quality: str, heading: str, line_no: int) -> Entry:
    identifier = table_identifier(table)
    if not identifier:
        raise ValueError("canonical declaration table missing supported identifier")
    field, identifier_type, canonical_id = identifier
    code_family = strip_inline_code(table.get("Code Family", ""))
    reference_set = strip_inline_code(table.get("Reference Set", ""))
    canonical_constraint = strip_inline_code(table.get("Canonical Constraint", ""))
    canonical_obligation = strip_inline_code(table.get("Canonical Obligation", ""))
    family_id, family_kind, parent_family, hierarchy_path, collision_status = infer_family_metadata(identifier_type, canonical_id, table, heading)
    qual, missing = declaration_quality(table, section_quality, identifier_type)
    return Entry(
        canonical_id=canonical_id,
        identifier_type=identifier_type,
        code_family=code_family,
        reference_set=reference_set,
        canonical_constraint=canonical_constraint,
        canonical_obligation=canonical_obligation,
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
        canonical_section_heading=canonical_heading,
        canonical_section_line_number=canonical_line,
        declaration_heading=heading,
        declaration_line_number=line_no,
        extraction_method="bounded_heading_section_table",
        declaration_quality=qual,
        missing_expected_fields=missing,
        source_path=str(p.as_posix()),
        family_id=family_id,
        family_kind=family_kind,
        parent_family=parent_family,
        hierarchy_path=hierarchy_path,
        collision_status=collision_status,
        registry_note=table.get("Registry Note", "").strip(),
        table=table,
    )

def record_table_or_diagnostic(out: list[Entry], p: pathlib.Path, table: dict[str,str], canonical_heading: str, canonical_line: int, section_quality: str, declaration_heading: str, declaration_line: int) -> None:
    if table_identifier(table):
        out.append(make_entry(p, table, canonical_heading, canonical_line, section_quality, declaration_heading, declaration_line))
    else:
        DIAGNOSTICS.append(Diagnostic(str(p.as_posix()), declaration_line, "canonical declaration table missing supported identifier field (Code Family, Reference Set, Canonical Constraint, or Canonical Obligation)"))

def scan(root: pathlib.Path) -> list[Entry]:
    DIAGNOSTICS.clear()
    out: list[Entry] = []
    for p in sorted(root.glob("**/*.md")):
        lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
        i = 0
        while i < len(lines):
            h = parse_heading(lines[i])
            if not h:
                i += 1
                continue
            level, heading = h
            ok, section_quality = is_canonical_heading(heading)
            if not ok:
                i += 1
                continue
            end = i + 1
            while end < len(lines):
                nh = parse_heading(lines[end])
                if nh and nh[0] <= level:
                    break
                end += 1
            j = i + 1
            found_block = False
            while j < end:
                dh = parse_heading(lines[j])
                if dh and dh[0] > level:
                    dlevel, dheading = dh
                    block_end = j + 1
                    while block_end < end:
                        bh = parse_heading(lines[block_end])
                        if bh and bh[0] <= dlevel:
                            break
                        block_end += 1
                    table, _ = find_first_table(lines, j + 1, block_end)
                    if table:
                        found_block = True
                        record_table_or_diagnostic(out, p, table, heading, i + 1, section_quality, dheading, j + 1)
                    j = block_end
                    continue
                j += 1
            if not found_block:
                table, _ = find_first_table(lines, i + 1, end)
                if table:
                    record_table_or_diagnostic(out, p, table, heading, i + 1, section_quality, heading, i + 1)
            i = end
    return out

def validate(entries: list[Entry]) -> list[str]:
    errs = [f"{d.source_path}:{d.line_number} {d.message}" for d in DIAGNOSTICS]
    by_id: dict[str, list[Entry]] = {}
    for e in entries:
        if not e.canonical_id:
            errs.append(f"Malformed canonical declaration row: {e.source_path}:{e.declaration_line_number} missing canonical identifier")
        if e.missing_expected_fields:
            errs.append(f"Malformed canonical declaration row: {e.source_path}:{e.declaration_line_number} missing fields {e.missing_expected_fields}")
        if e.declaration_quality == "nonstandard_section_heading":
            errs.append(f"Nonstandard canonical section heading: {e.source_path}:{e.canonical_section_line_number} {e.canonical_section_heading}")
        by_id.setdefault(e.canonical_id, []).append(e)
    for canonical_id, rows in by_id.items():
        instruments = {pathlib.Path(r.source_path).stem for r in rows}
        identifier_types = {r.identifier_type for r in rows if r.identifier_type}
        if len(instruments) > 1:
            if identifier_types == {"code_family"}:
                errs.append(f"Duplicate Code Family across instruments: {canonical_id} -> {sorted(instruments)}")
            else:
                errs.append(f"Duplicate Canonical ID across instruments: {canonical_id} -> {sorted(instruments)}")
        ptypes = {r.primary_type for r in rows if r.primary_type}
        if len(ptypes) > 1:
            errs.append(f"Conflicting Primary Type for Canonical ID {canonical_id}: {sorted(ptypes)}")
    return errs

def write_md(path: pathlib.Path, entries: list[Entry]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write("# Canonical Code Index\n\n")
        f.write("| Canonical ID | Canonical Name | Identifier Type | Family Kind | Parent Family | Collision Status | Primary Type | Source Instrument | Source Path | Canonical Section | Declaration Heading | Line |\n")
        f.write("|---|---|---|---|---|---|---|---|---|---|---|---:|\n")
        for e in entries:
            parent = e.parent_family if e.parent_family else "—"
            note = f" ({e.registry_note})" if e.registry_note else ""
            f.write(f"| `{e.canonical_id}` | {e.canonical_name} | {e.identifier_type} | {e.family_kind}{note} | `{parent}` | {e.collision_status} | {e.primary_type} | `{e.source_instrument}` | `{e.source_path}` | {e.canonical_section_heading} | {e.declaration_heading} | {e.declaration_line_number} |\n")

def sort_entries(entries: list[Entry]) -> list[Entry]:
    return sorted(entries, key=lambda e: (e.canonical_id.casefold(), e.identifier_type, e.source_instrument.casefold(), e.source_path.casefold(), e.declaration_line_number))

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="Governance")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--md-out", default="Governance/canonical-code-index.md")
    ap.add_argument("--json-out", default="Governance/canonical-code-index.json")
    args = ap.parse_args()
    entries = sort_entries(scan(pathlib.Path(args.root)))
    write_md(pathlib.Path(args.md_out), entries)
    pathlib.Path(args.json_out).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(args.json_out).write_text(json.dumps([e._asdict() for e in entries], indent=2), encoding="utf-8")
    errs = validate(entries)
    for e in errs:
        print(f"WARNING: {e}")
    return 0
if __name__ == "__main__": sys.exit(main())
