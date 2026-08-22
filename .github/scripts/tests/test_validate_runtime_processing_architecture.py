import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "validate_runtime_processing_architecture.py"
spec = importlib.util.spec_from_file_location("runtime_architecture", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


def test_repository_runtime_architecture_is_conformant():
    assert module.validate() == []


def test_section_requires_exact_bounding_headings():
    text = "## A\nbody\n## B\n"
    assert module.section(text, "## A", "## B") == "## A\nbody\n"
    assert module.section(text, "## Missing", "## B") == ""


def test_required_authorities_are_real_instruments():
    existing = module.instrument_ids(module.ROOT)
    assert set(module.REQUIRED_AUTHORITIES) <= existing


def test_child_safety_gate_preserves_ordinary_and_severable_assistance():
    engine = (module.ROOT / module.ENGINE).read_text(encoding="utf-8")
    for invariant in module.CHILD_SAFETY_INVARIANTS:
        assert invariant in engine

    scenario_expectations = {
        "known minor greeting": "ordinary age-appropriate processing continues",
        "minor arithmetic or spelling": "deterministic arithmetic or spelling",
        "minor benign coding help": "benign coding and educational help",
        "unresolved age ordinary interaction": "does not establish global ineligibility",
        "unresolved age adult-only surface": "restriction attaches to that surface",
        "youth distress": "without requiring unrelated conversational withdrawal",
        "mixed restricted request": "preserve the safe remainder",
    }
    for expected_text in scenario_expectations.values():
        assert expected_text in engine
