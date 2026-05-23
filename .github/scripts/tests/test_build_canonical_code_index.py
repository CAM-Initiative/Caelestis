import importlib.util, pathlib

spec = importlib.util.spec_from_file_location('cc', pathlib.Path(__file__).resolve().parents[1] / 'build-canonical-code-index.py')
cc = importlib.util.module_from_spec(spec)
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
    assert rows[0].controlled_values_defined == ['I0', 'I1', 'I2', 'I3', 'I4']


def test_no_false_positives_from_body_tables(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## Symbolic Structures\n| Field | Entry |\n|---|---|\n| Code Family | CA |\n')
    rows = cc.scan(tmp_path/'Governance')
    assert rows == []


def test_numbered_heading_support(tmp_path):
    f = tmp_path/'Governance'/'A.md'
    w(f, '## 15.3 Canonical Code & Reference Set Declarations\n### H\n' + decl('I'))
    assert cc.scan(tmp_path/'Governance')[0].code_family == 'I'


def test_duplicate_code_family_across_instruments(tmp_path):
    w(tmp_path/'Governance'/'A.md', '## Canonical Code & Reference Set Declarations\n### H\n' + decl('I'))
    w(tmp_path/'Governance'/'B.md', '## Canonical Code & Reference Set Declarations\n### H\n' + decl('I'))
    errs = cc.validate(cc.scan(tmp_path/'Governance'))
    assert any('Duplicate Code Family across instruments' in e for e in errs)


def test_conflicting_primary_type_for_same_code_family(tmp_path):
    w(tmp_path/'Governance'/'A.md', '## Canonical Code & Reference Set Declarations\n### H\n' + decl('I', primary='Semantic'))
    w(tmp_path/'Governance'/'B.md', '## Canonical Code & Reference Set Declarations\n### H\n' + decl('I', primary='Operational'))
    errs = cc.validate(cc.scan(tmp_path/'Governance'))
    assert any('Conflicting Primary Type for Code Family I' in e for e in errs)
