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
