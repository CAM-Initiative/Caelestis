import importlib.util
import pathlib


SCRIPT_PATH = pathlib.Path(__file__).resolve().parents[1] / "update-CAM-Constitutional-Schedule-Registry.py"
spec = importlib.util.spec_from_file_location("constitutional_schedule_registry", SCRIPT_PATH)
registry = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(registry)


EXPECTED_CURRENT_SCHEDULES = [
    "CAM-BS2025-AEON-001-SCH-01",
    "CAM-BS2025-AEON-002-SCH-01",
    "CAM-BS2025-AEON-003-SCH-02",
    "CAM-BS2025-AEON-005-SCH-04",
    "CAM-BS2026-AEON-007-SCH-01",
    "CAM-BS2026-AEON-010-SCH-01",
    "CAM-BS2026-AEON-013-SCH-01",
]


def schedule_item(instrument_id: str, **overrides):
    item = {
        "id": instrument_id,
        "title": "Schedule",
        "link": f"Constitution/{instrument_id}.md",
        "version": "1.0",
        "status": "** Active",
        "instrument_class": "constitution",
        "hierarchy_type": "schedule",
        "parent_id": "CAM-BS2025-AEON-100",
    }
    item.update(overrides)
    return item


def test_selection_uses_authoritative_metadata_not_identifier_shape():
    valid_without_sch_syntax = schedule_item("CAM-TEST-CONSTITUTIONAL-01")
    syntax_only = schedule_item(
        "CAM-BS2025-AEON-100-SCH-01",
        hierarchy_type="supplement",
        instrument_class="charter",
        link="Charters/CAM-BS2025-AEON-100-SCH-01.md",
    )
    retired = schedule_item("CAM-BS2025-AEON-100-SCH-02", status="Retired")
    draft = schedule_item("CAM-BS2025-AEON-100-SCH-03", status="Draft")

    rows = registry.build_rows([syntax_only, retired, draft, valid_without_sch_syntax])
    assert [row.instrument_id for row in rows] == ["CAM-TEST-CONSTITUTIONAL-01"]


def test_current_fixture_contains_exactly_seven_constitutional_schedules():
    rows = registry.build_rows(registry.load_governance_items())
    assert [row.instrument_id for row in rows] == EXPECTED_CURRENT_SCHEDULES


def test_registry_target_is_relocated_projection():
    assert registry.REGISTRY_PATH == registry.GOV_DIR / "CAM.Constitutional.Schedule.Registry.md"


def test_model_term_classification_is_conservative():
    assert registry.classify_model_term("Caelestis Architecture Model") == "Architecture Model"
    assert registry.classify_model_term("Runtime Governance Execution Model") == "Execution Model"
    assert registry.classify_model_term("Integrity State Model") == "Security Model"
    assert registry.classify_model_term("pricing models") == "Generic / Non-Canonical Usage"


def test_model_term_review_status_non_blocking_defaults():
    assert registry.classify_review_status("Execution Model") == "Declared / Recognised"
    assert registry.classify_review_status("Security Model") == "Declared / Recognised"
    assert registry.classify_review_status("Generic / Non-Canonical Usage") == "Generic Usage"
    assert registry.classify_review_status("Unclassified / Review") == "Needs Review"


def test_strip_generated_blocks_ignores_current_generated_regions():
    text = f"""
before Runtime Governance Execution Model
{registry.REGISTRY_START}
Runtime Governance Execution Model
{registry.REGISTRY_END}
middle
{registry.MODEL_REGISTER_START}
Integrity State Model
{registry.MODEL_REGISTER_END}
after pricing models
"""
    cleaned = registry.strip_generated_blocks_for_scan(text)
    assert "before Runtime Governance Execution Model" in cleaned
    assert "after pricing models" in cleaned
    assert registry.REGISTRY_START not in cleaned
    assert registry.MODEL_REGISTER_START not in cleaned
    assert "\nRuntime Governance Execution Model\n" not in cleaned
    assert "\nIntegrity State Model\n" not in cleaned


def test_render_model_register_suppresses_generic_usage_rows():
    rows = [
        registry.ModelTerminologyItem("CAM-A", "H1", "pricing models", "Generic / Non-Canonical Usage", "Generic Usage"),
        registry.ModelTerminologyItem("CAM-B", "H2", "Runtime Governance Execution Model", "Execution Model", "Declared / Recognised"),
        registry.ModelTerminologyItem("CAM-C", "H3", "Attribution & Dependency Model", "Economic Model", "Declared / Recognised"),
    ]
    out = registry.render_model_terminology_register(rows)
    assert "**Total model-term matches scanned:** 3" in out
    assert "**Generic usages suppressed:** 1" in out
    assert "Runtime Governance Execution Model" in out
    assert "Attribution & Dependency Model" in out
    assert "pricing models" not in out


def test_render_model_summary_has_counts_and_audit_path_only():
    rows = [
        registry.ModelTerminologyItem("CAM-A", "H1", "pricing models", "Generic / Non-Canonical Usage", "Generic Usage"),
        registry.ModelTerminologyItem("CAM-B", "H2", "Runtime Governance Execution Model", "Execution Model", "Declared / Recognised"),
    ]
    summary = registry.render_model_terminology_summary(rows)
    assert "**Total model-term matches scanned:** 2" in summary
    assert "**Generic usages suppressed:** 1" in summary
    assert "Instrument | Section / Heading | Term Used" not in summary
    assert ".github/Indices/CAM.Governance.Model-Terminology.Audit.md" in summary


def test_render_model_register_is_deterministic():
    rows = [
        registry.ModelTerminologyItem("CAM-B", "H2", "Runtime Governance Execution Model", "Execution Model", "Declared / Recognised"),
        registry.ModelTerminologyItem("CAM-A", "H1", "pricing models", "Generic / Non-Canonical Usage", "Generic Usage"),
        registry.ModelTerminologyItem("CAM-C", "H3", "Attribution & Dependency Model", "Economic Model", "Declared / Recognised"),
    ]
    assert registry.render_model_terminology_register(rows) == registry.render_model_terminology_register(rows)
    assert "pricing models" not in registry.render_model_terminology_register(rows)
