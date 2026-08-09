import importlib.util
import pathlib


spec = importlib.util.spec_from_file_location(
    "metadata_audit",
    pathlib.Path(__file__).resolve().parents[1] / "audit_metadata_authority_contract.py",
)
metadata_audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metadata_audit)


def valid_meta(**overrides):
    meta = {
        "Status": "Adopted",
        "Effect": "Operational",
        "Governance Standard": "CAM Standard",
        "Review State": "Current",
        "Authority Role": "Operational Authority",
        "Source Authority": "Derived Authority",
        "Parent Instrument": "CAM-EQ2026-OPERATIONS-001-PLATINUM — Governance Operations Charter",
    }
    meta.update(overrides)
    return meta


def codes(found):
    return {issue["code"] for issue in found}


def test_derived_authority_requires_parent():
    path = metadata_audit.ROOT / "Governance/Charters/CAM-EQ2026-OPERATIONS-002-PLATINUM.md"
    found = metadata_audit.evaluate(
        path,
        False,
        valid_meta(**{"Parent Instrument": ""}),
        {path.stem, "CAM-EQ2026-OPERATIONS-001-PLATINUM"},
    )
    assert "derived_or_applied_parent_missing" in codes(found)


def test_parent_identifier_must_resolve():
    path = metadata_audit.ROOT / "Governance/Charters/CAM-EQ2026-OPERATIONS-002-PLATINUM.md"
    found = metadata_audit.evaluate(path, False, valid_meta(), {path.stem})
    assert "unresolved_parent_instrument" in codes(found)


def test_constitution_adjacent_law_may_use_constitutional_role():
    path = metadata_audit.ROOT / "Governance/Laws/CAM-BS2025-LAW-001-PLATINUM.md"
    meta = valid_meta(
        Effect="Binding",
        **{
            "Authority Role": "Constitutional Authority",
            "Source Authority": "Source-Authoritative",
            "Parent Instrument": "",
        },
    )
    found = metadata_audit.evaluate(path, False, meta, {path.stem})
    assert "constitutional_role_outside_constitution" not in codes(found)


def test_circular_parent_lineage_is_reported():
    records = [
        {
            "path": "Governance/Charters/CAM-EQ2026-TEST-001-PLATINUM.md",
            "metadata": {"Parent Instrument": "CAM-EQ2026-TEST-002-PLATINUM"},
            "issues": [],
        },
        {
            "path": "Governance/Charters/CAM-EQ2026-TEST-002-PLATINUM.md",
            "metadata": {"Parent Instrument": "CAM-EQ2026-TEST-001-PLATINUM"},
            "issues": [],
        },
    ]
    issues = []
    metadata_audit.add_circular_lineage_issues(records, issues)
    assert issues
    assert {issue["code"] for issue in issues} == {"circular_parent_lineage"}
