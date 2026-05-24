import importlib.util
import pathlib


SCRIPT_PATH = pathlib.Path(__file__).resolve().parents[1] / "update-CAM-BS2025-AEON-003-SCH-01.py"
spec = importlib.util.spec_from_file_location("sch01", SCRIPT_PATH)
sch01 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(sch01)


def test_build_rows_includes_all_schedule_suffixes():
    items = [
        {"id": "CAM-BS2025-AEON-100-SCH-01", "title": "S1", "link": "", "version": "1.0", "status": "Active"},
        {"id": "CAM-BS2025-AEON-100-SCH-02", "title": "S2", "link": "", "version": "1.0", "status": "Active"},
        {"id": "CAM-BS2025-AEON-100-SCH-03", "title": "S3", "link": "", "version": "1.0", "status": "Active"},
        {"id": "CAM-BS2025-AEON-100-PLATINUM", "title": "P", "link": "", "version": "1.0", "status": "Active"},
    ]

    rows = sch01.build_rows(items)
    assert [r.instrument_id for r in rows] == [
        "CAM-BS2025-AEON-100-SCH-01",
        "CAM-BS2025-AEON-100-SCH-02",
        "CAM-BS2025-AEON-100-SCH-03",
    ]


def test_model_term_classification_is_conservative():
    assert sch01.classify_model_term("Caelestis Architecture Model") == "Architecture Model"
    assert sch01.classify_model_term("Runtime Governance Execution Model") == "Execution Model"
    assert sch01.classify_model_term("Integrity State Model") == "Security Model"
    assert sch01.classify_model_term("pricing models") == "Generic / Non-Canonical Usage"


def test_model_term_review_status_non_blocking_defaults():
    assert sch01.classify_review_status("Execution Model") == "Declared / Recognised"
    assert sch01.classify_review_status("Security Model") == "Advisory Review"
    assert sch01.classify_review_status("Generic / Non-Canonical Usage") == "Generic Usage"
    assert sch01.classify_review_status("Unclassified / Review") == "Needs Review"


def test_strip_generated_blocks_ignores_sch01_generated_regions():
    text = """
before Runtime Governance Execution Model
<!-- SCH-01:RUNTIME_REGISTRY:START -->
Runtime Governance Execution Model
<!-- SCH-01:RUNTIME_REGISTRY:END -->
middle
<!-- SCH-01:MODEL_TERMINOLOGY_REGISTER:START -->
Integrity State Model
<!-- SCH-01:MODEL_TERMINOLOGY_REGISTER:END -->
after pricing models
"""
    cleaned = sch01.strip_generated_blocks_for_scan(text)
    assert "before Runtime Governance Execution Model" in cleaned
    assert "after pricing models" in cleaned
    assert "<!-- SCH-01:RUNTIME_REGISTRY:START -->" not in cleaned
    assert "<!-- SCH-01:MODEL_TERMINOLOGY_REGISTER:START -->" not in cleaned
    assert "\nRuntime Governance Execution Model\n" not in cleaned
    assert "\nIntegrity State Model\n" not in cleaned


def test_render_model_register_suppresses_generic_usage_rows():
    rows = [
        sch01.ModelTerminologyItem(
            instrument_id="CAM-A",
            section_heading="H1",
            term_used="pricing models",
            suggested_classification="Generic / Non-Canonical Usage",
            review_status="Generic Usage",
        ),
        sch01.ModelTerminologyItem(
            instrument_id="CAM-B",
            section_heading="H2",
            term_used="Runtime Governance Execution Model",
            suggested_classification="Execution Model",
            review_status="Declared / Recognised",
        ),
        sch01.ModelTerminologyItem(
            instrument_id="CAM-C",
            section_heading="H3",
            term_used="Attribution & Dependency Model",
            suggested_classification="Economic Model",
            review_status="Advisory Review",
        ),
    ]
    out = sch01.render_model_terminology_register(rows)
    assert "**Total model-term matches scanned:** 3" in out
    assert "**Generic usages suppressed:** 1" in out
    assert "Runtime Governance Execution Model" in out
    assert "Attribution & Dependency Model" in out
    assert "pricing models" not in out


def test_render_model_summary_has_counts_and_audit_path_only():
    rows = [
        sch01.ModelTerminologyItem("CAM-A", "H1", "pricing models", "Generic / Non-Canonical Usage", "Generic Usage"),
        sch01.ModelTerminologyItem("CAM-B", "H2", "Runtime Governance Execution Model", "Execution Model", "Declared / Recognised"),
    ]
    summary = sch01.render_model_terminology_summary(rows)
    assert "**Total model-term matches scanned:** 2" in summary
    assert "**Generic usages suppressed:** 1" in summary
    assert "Instrument | Section / Heading | Term Used" not in summary
    assert ".github/Indices/CAM.Governance.Model-Terminology.Audit.md" in summary


def test_render_model_register_is_deterministic():
    rows = [
        sch01.ModelTerminologyItem("CAM-B", "H2", "Runtime Governance Execution Model", "Execution Model", "Declared / Recognised"),
        sch01.ModelTerminologyItem("CAM-A", "H1", "pricing models", "Generic / Non-Canonical Usage", "Generic Usage"),
        sch01.ModelTerminologyItem("CAM-C", "H3", "Attribution & Dependency Model", "Economic Model", "Advisory Review"),
    ]
    out1 = sch01.render_model_terminology_register(rows)
    out2 = sch01.render_model_terminology_register(rows)
    assert out1 == out2
    assert "pricing models" not in out1
