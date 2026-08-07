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
