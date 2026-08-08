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


def test_retired_findings_permits_aeon_ccs_in_amendment_ledger_history(tmp_path):
    path = tmp_path / "CAM-TEST.md"
    text = "AI system\n## 1.0 Amendment Ledger\nAEON.CCS — Cognitive Cycle Stage\n"
    assert module.retired_findings(path, text) == []
