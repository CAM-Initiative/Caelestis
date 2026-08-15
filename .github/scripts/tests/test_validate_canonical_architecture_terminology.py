import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "validate_canonical_architecture_terminology.py"
spec = importlib.util.spec_from_file_location("canonical_architecture", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


def test_normative_text_excludes_amendment_ledger_only():
    text = "AI system\n## 18.3 Amendment Ledger\nResponding Intelligence\n"
    assert "Responding Intelligence" not in module.normative_text(text)


def test_normative_text_keeps_current_doctrine():
    text = "AI system\nRuntime configuration snapshot\n"
    assert module.normative_text(text) == text


def test_retired_findings_excludes_ledger_history(tmp_path):
    path = tmp_path / "CAM-TEST.md"
    text = "AI system\n## 1.0 Amendment Ledger\nResponding Intelligence\n"
    assert module.retired_findings(path, text) == []


def test_retired_findings_detects_current_relational_and_architecture_terms(tmp_path):
    path = tmp_path / "CAM-TEST.md"
    findings = module.retired_findings(path, "polyadic coordination\nResponding Intelligence\n")
    assert [term for _line, term in findings] == ["polyadic", "Responding Intelligence"]


def test_retired_findings_detects_aeon_ccs_cognitive_classification_aliases(tmp_path):
    path = tmp_path / "CAM-TEST.md"
    findings = module.retired_findings(
        path,
        "AEON.CCS\nAEON.CC.COGNITIVA\nCognitive Cycle Stage\n",
    )
    assert [term for _line, term in findings] == [
        "AEON.CCS",
        "AEON.CC.COGNITIVA",
        "Cognitive Cycle Stage",
    ]


def test_retired_findings_detects_legacy_provenance_codes(tmp_path):
    path = tmp_path / "CAM-TEST.md"
    findings = module.retired_findings(
        path,
        "AUTH.RI_AUTHORED\nPCLASS.SYNTHETIC\n",
    )
    assert [term for _line, term in findings] == [
        "AUTH.RI_AUTHORED",
        "PCLASS.SYNTHETIC",
    ]


def test_retired_provenance_codes_permitted_in_amendment_history(tmp_path):
    path = tmp_path / "CAM-TEST.md"
    text = "AUTH.AI_SYSTEM_AUTHORED\n## 2.0 Amendment Ledger\nAUTH.RI_AUTHORED; PCLASS.SYNTHETIC\n"
    assert module.retired_findings(path, text) == []


def test_retired_findings_permits_aeon_ccs_in_amendment_ledger_history(tmp_path):
    path = tmp_path / "CAM-TEST.md"
    text = "AI system\n## 1.0 Amendment Ledger\nAEON.CCS — Cognitive Cycle Stage\n"
    assert module.retired_findings(path, text) == []


def test_retired_findings_normalises_unicode_dash_variants(tmp_path):
    path = tmp_path / "CAM-TEST.md"
    findings = module.retired_findings(path, "POLYADIC — authority\n")
    assert [term.casefold() for _line, term in findings] == ["polyadic"]


def test_sealed_law_exception_is_exact_and_non_general():
    path = module.ROOT / "Governance/Laws/CAM-BS2025-LAW-001-PLATINUM.md"
    exact = "| **Axis Context** | Polyadic — Multi-System / Cross-Domain |\n"
    assert module.retired_findings(path, exact) == []
    assert module.retired_findings(path, "Polyadic authority\n") == [(1, "Polyadic")]


def test_categorical_geometry_detects_replacement_axis_and_table():
    text = (
        "## 4.2 Axis B — Relational Configuration\n"
        "| One-to-one | private |\n"
        "| Three-party | institutional |\n"
        "| Multi-party | elevated authority |\n"
    )
    findings = module.categorical_geometry_findings(text)
    assert [reason for _line, reason in findings] == [
        "participant-cardinality relational axis",
        "participant-cardinality class table row",
        "participant-cardinality class table row",
        "participant-cardinality class table row",
    ]


def test_categorical_geometry_detects_direct_authority_inference():
    findings = module.categorical_geometry_findings(
        "Participant count determines authority status.\n"
    )
    assert findings == [(1, "participant topology directly determines governance consequence")]


def test_categorical_geometry_permits_non_inference_and_genuine_topology():
    text = (
        "Participant count does not establish authority.\n"
        "Where multiple AI systems participate, contributor attribution SHALL remain legible.\n"
    )
    assert module.categorical_geometry_findings(text) == []
    assert module.geometry_candidate_warnings(text) == []


def test_geometry_candidate_warning_is_non_blocking_for_ambiguous_proximity():
    warnings = module.geometry_candidate_warnings(
        "A multi-party context may involve authority review.\n"
    )
    assert warnings == [(1, "geometry term near governance consequence")]
