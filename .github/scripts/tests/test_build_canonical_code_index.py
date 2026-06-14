import importlib.util, pathlib, sys

spec = importlib.util.spec_from_file_location('cc', pathlib.Path(__file__).resolve().parents[1] / 'build-canonical-code-index.py')
cc = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = cc
spec.loader.exec_module(cc)


def w(p, t):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(t)


def decl(code_family: str, primary: str = 'Semantic', controlled: str = '') -> str:
    return f"""| Field | Entry |
|---|---|
| Code Family | {code_family} |
| Canonical Name | X |
| Primary Type | {primary} |
| Subtype | S |
| Modifier | M |
| Scope | Global |
| Status | Active |
| Controlled Values Defined | {controlled} |
| Schema Field(s) | f |
| Source Instrument | CAM-EQ2026-RELATION-005-PLATINUM |
| Source Section | 15.3 |
| Domain Namespace | dn |
| Authority / Protection Level | A |
| Consumes Code Families | |
| Crosswalks Code Families | |
| Operationalises or Applies Code Families | |
"""


def test_single_letter_and_two_letter_code_family_and_controlled_values(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## 15.3 Canonical Code & Reference Set Declarations\n### Identity Family\n' + decl('I', controlled='I0, I1, I2, I3, I4') + '\n### Capability Family\n' + decl('CA'))
    rows = cc.scan(tmp_path/'Governance')
    assert [r.code_family for r in rows] == ['I', 'CA']
    assert [r.canonical_id for r in rows] == ['I', 'CA']
    assert [r.identifier_type for r in rows] == ['code_family', 'code_family']
    assert rows[0].canonical_section_heading == '15.3 Canonical Code & Reference Set Declarations'
    assert rows[0].canonical_section_line_number == 1
    assert rows[0].extraction_method == 'bounded_heading_section_table'
    assert rows[0].controlled_values_defined == ['I0', 'I1', 'I2', 'I3', 'I4']
    assert rows[0].family_kind == 'legacy_global_family'


def test_no_false_positives_from_body_tables(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## Symbolic Structures\n| Field | Entry |\n|---|---|\n| Code Family | CA |\n')
    assert cc.scan(tmp_path/'Governance') == []


def test_exact_shortened_numbered_and_level_three_canonical_headings(tmp_path):
    w(tmp_path/'Governance'/'A.md', '## Canonical Code & Reference Set Declarations\n### H\n' + decl('A'))
    w(tmp_path/'Governance'/'B.md', '## Canonical Code & Reference Set\n### H\n' + decl('B'))
    w(tmp_path/'Governance'/'C.md', '## 15.3 Canonical Code & Reference Set Declarations\n### H\n' + decl('C'))
    w(tmp_path/'Governance'/'D.md', '### 16.4 Canonical Code & Reference Set Declarations\n#### H\n' + decl('D'))
    rows = cc.scan(tmp_path/'Governance')
    assert [r.code_family for r in rows] == ['A', 'B', 'C', 'D']
    assert rows[1].declaration_quality == 'nonstandard_section_heading'
    assert rows[3].declaration_line_number == 2


def test_section_boundary_stops_at_same_or_higher_heading(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## 15.3 Canonical Code & Reference Set Declarations\n### H\n' + decl('I') + '\n## 15.4 Review\n### Not canonical\n' + decl('X'))
    assert [r.code_family for r in cc.scan(tmp_path/'Governance')] == ['I']


def test_declaration_subsections_at_level_three_and_four(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## Canonical Code & Reference Set Declarations\n### H3\n' + decl('A') + '\n### Group\n#### H4\n' + decl('B'))
    assert [r.code_family for r in cc.scan(tmp_path/'Governance')] == ['A', 'B']


def refset(identifier: str) -> str:
    return f"""| Field | Entry |
|---|---|
| Reference Set | {identifier} |
| Canonical Name | Ref |
| Primary Type | Structural / Operational |
| Controlled Values Defined | {identifier}.A, {identifier}.B |
| Schema Field(s) | ref_field |
| Source Instrument | CAM-EQ2026-OPERATIONS-003-SUP-01 |
| Source Section | 11.3 |
| Domain Namespace | OPERATIONS |
| Authority / Protection Level | A |
"""


def test_reference_set_table_is_indexed(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## Canonical Code & Reference Set Declarations\n### Reference Set\n' + refset('OPS.FMA'))
    rows = cc.scan(tmp_path/'Governance')
    assert len(rows) == 1
    assert rows[0].canonical_id == 'OPS.FMA'
    assert rows[0].identifier_type == 'reference_set'
    assert rows[0].reference_set == 'OPS.FMA'
    assert rows[0].code_family == ''
    assert rows[0].family_kind == 'reference_set'


def test_malformed_table_without_supported_identifier_warns(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## Canonical Code & Reference Set Declarations\n### Broken\n| Field | Entry |\n|---|---|\n| Canonical Name | Missing Identifier |\n')
    rows = cc.scan(tmp_path/'Governance')
    assert rows == []
    errs = cc.validate(rows)
    assert any('missing supported identifier field' in e for e in errs)


def test_canonical_section_containing_code_family_and_reference_set(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## Canonical Code & Reference Set Declarations\n### Failure Family\n' + decl('OPS.FF') + '\n### Metadata Axis\n' + refset('OPS.FMA'))
    rows = cc.scan(tmp_path/'Governance')
    assert [(r.canonical_id, r.identifier_type) for r in rows] == [('OPS.FF', 'code_family'), ('OPS.FMA', 'reference_set')]


def test_operations_style_reference_sets_are_indexed(tmp_path):
    f = tmp_path/'Governance'/'Ops.md'
    w(f, '## 11.3 Canonical Code & Reference Set Declarations\n### 11.3.1 `OPS.FF` — Failure Family\n' + decl('OPS.FF') + '\n### 11.3.2 `OPS.FMA` — Failure Metadata Axis\n' + refset('OPS.FMA') + '\n### 11.3.3 `OPS.AGMA` — Architectural & Governance Metadata Axis\n' + refset('OPS.AGMA') + '\n### 11.3.4 `OPS.FCS` — Failure Classification Status\n' + decl('OPS.FCS'))
    rows = cc.scan(tmp_path/'Governance')
    assert [(r.canonical_id, r.identifier_type) for r in rows] == [
        ('OPS.FF', 'code_family'),
        ('OPS.FMA', 'reference_set'),
        ('OPS.AGMA', 'reference_set'),
        ('OPS.FCS', 'code_family'),
    ]

def test_duplicate_code_family_across_instruments(tmp_path):
    w(tmp_path/'Governance'/'A.md', '## Canonical Code & Reference Set Declarations\n### H\n' + decl('I'))
    w(tmp_path/'Governance'/'B.md', '## Canonical Code & Reference Set Declarations\n### H\n' + decl('I'))
    errs = cc.validate(cc.scan(tmp_path/'Governance'))
    assert any('Duplicate Code Family across instruments' in e for e in errs)


def test_conflicting_primary_type_for_same_code_family(tmp_path):
    w(tmp_path/'Governance'/'A.md', '## Canonical Code & Reference Set Declarations\n### H\n' + decl('I', primary='Semantic'))
    w(tmp_path/'Governance'/'B.md', '## Canonical Code & Reference Set Declarations\n### H\n' + decl('I', primary='Operational'))
    errs = cc.validate(cc.scan(tmp_path/'Governance'))
    assert any('Conflicting Primary Type for Canonical ID I' in e for e in errs)


def test_heading_subfamily_promoted_from_parent_code_family(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## Canonical Code & Reference Set Declarations\n### 13.3.4 ECON.REI.DW — Dependency Weight\n' + decl('ECON.REI'))
    row = cc.scan(tmp_path/'Governance')[0]
    assert row.family_id == 'ECON.REI.DW'
    assert row.parent_family == 'ECON.REI'
    assert row.family_kind == 'subfamily'


def test_code_spans_are_stripped_from_family_ids_and_values(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## Canonical Code & Reference Set Declarations\n### 1.1 `ID.IFP` — Identity Formation Pathway\n' + decl('`ID.IFP`', controlled='`ID.IFP-1`, `ID.IFP-2`'))
    row = cc.scan(tmp_path/'Governance')[0]
    assert row.code_family == 'ID.IFP'
    assert row.family_id == 'ID.IFP'
    assert row.controlled_values_defined == ['ID.IFP-1', 'ID.IFP-2']



def test_canonical_constraint_and_obligation_identifier_fields(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## Canonical Code & Constraint Declarations\n### PCO Constraint\n| Field | Entry |\n|---|---|\n| Canonical Constraint | AEON.PCO |\n| Canonical Name | Proportional Constraint Obligation |\n| Primary Type | Constitutional Constraint / Governance Obligation |\n| Source Instrument | CAM-BS2025-AEON-002-PLATINUM |\n| Source Section | 3.8 |\n| Domain Namespace | AEON |\n| Authority / Protection Level | A |\n### PCO Obligation\n| Field | Entry |\n|---|---|\n| Canonical Obligation | AEON.PCO.OBL |\n| Canonical Name | PCO Obligation |\n| Primary Type | Constitutional Obligation |\n| Source Instrument | CAM-BS2025-AEON-002-PLATINUM |\n| Source Section | 3.8 |\n| Domain Namespace | AEON |\n| Authority / Protection Level | A |\n')
    rows = cc.scan(tmp_path/'Governance')
    assert [(r.canonical_id, r.identifier_type, r.family_kind) for r in rows] == [
        ('AEON.PCO', 'canonical_constraint', 'canonical_constraint'),
        ('AEON.PCO.OBL', 'canonical_obligation', 'canonical_obligation'),
    ]

def test_duplicate_source_declarations_are_marked(tmp_path):
    w(tmp_path/'Governance'/'A.md', '## Canonical Code & Reference Set Declarations\n### A\n' + decl('DUP.HARM'))
    w(tmp_path/'Governance'/'B.md', '## Canonical Code & Reference Set Declarations\n### B\n' + decl('DUP.HARM'))
    rows = cc.mark_duplicate_source_declarations(cc.sort_entries(cc.scan(tmp_path/'Governance')))
    assert [r.collision_status for r in rows] == [
        'duplicate_source_declaration',
        'duplicate_source_declaration',
    ]

def test_registered_domain_harm_family_tables_are_registry_only(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## Canonical Code & Reference Set Declarations\n### Registry Reference\n| Field | Entry |\n|---|---|\n| Registered Domain Harm Family | DUP.HARM |\n| Source Authority Instrument | CAM-EQ2026-ETHICS-003-PLATINUM |\n| Registry Relationship | Registered under AEON.HARM global harm registry |\n')
    assert cc.scan(tmp_path/'Governance') == []
    assert cc.validate([]) == []

def test_default_output_paths_are_governance():
    parser_defaults = pathlib.Path(cc.main.__code__.co_filename).read_text()
    assert 'default="Governance/CAM.Canonical.Code.Index.md"' in parser_defaults
    assert 'default="Governance/CAM.Canonical.Code.Index.json"' in parser_defaults
