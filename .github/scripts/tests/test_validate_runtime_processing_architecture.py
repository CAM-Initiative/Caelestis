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


def test_ten_phase_topology_is_frozen():
    assert module.PHASES == (
        "Runtime Entry and Context",
        "Pre-Classification",
        "Domain Determination",
        "Authority Resolution",
        "Governed Response or Action Preparation",
        "Execution-Boundary Evaluation",
        "Bounded Commitment",
        "Execution",
        "Representation and Delivery",
        "Preservation, Closure and Reassessment",
    )


def test_constitutional_engine_does_not_use_implementation_field_contracts():
    engine = (module.ROOT / module.ENGINE).read_text(encoding="utf-8")
    operative = module.operative_engine_text(engine)
    for label in module.TECHNICAL_PHASE_LABELS:
        assert label not in operative


def test_constitutional_engine_does_not_embed_subordinate_domain_codes():
    engine = (module.ROOT / module.ENGINE).read_text(encoding="utf-8")
    operative = module.operative_engine_text(engine)
    assert module.SCOPED_DOMAIN_CODE_RE.findall(operative) == []
