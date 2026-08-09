import importlib.util
import pathlib


SCRIPT_PATH = pathlib.Path(__file__).resolve().parents[1] / "update-CAM-Global-Operative-Instrument-Registry.py"
spec = importlib.util.spec_from_file_location("global_operative_registry", SCRIPT_PATH)
registry = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(registry)


def test_registry_target_is_relocated_projection():
    assert registry.REGISTRY_PATH == registry.GOV_DIR / "CAM.Global.Operative.Instrument.Registry.md"


def test_operability_filter_excludes_non_current_and_draft_items():
    base = {"status": "Active", "effect": "Binding", "link": "Charters/CAM-A.md"}
    assert registry.is_current_operative_item(base)
    assert registry.is_current_operative_item({**base, "status": "Adopted"})
    assert not registry.is_current_operative_item({**base, "status": "Draft"})
    assert not registry.is_current_operative_item({**base, "status": "Proposed"})
    assert not registry.is_current_operative_item({**base, "status": "Retired"})
    assert not registry.is_current_operative_item({**base, "status": "Superseded"})
    assert not registry.is_current_operative_item({**base, "effect": "Archival"})
    assert not registry.is_current_operative_item({**base, "link": "Drafts/CAM-A.md"})


def test_current_projection_excludes_retired_registry_schedules():
    rows = registry.generate_registry_rows(
        registry.load_governance_json(),
        registry.scan_folders(),
        registry.scan_governance_index(),
    )
    ids = {row.doc_id for row in rows}
    assert "CAM-BS2025-AEON-003-SCH-01" not in ids
    assert "CAM-BS2025-AEON-003-SCH-03" not in ids
    assert all(row.status in {"Active", "Adopted"} for row in rows)
    assert all(row.source_authority for row in rows)


def test_rendered_projection_reproduces_authority_metadata_without_elevating_it():
    row = registry.RegistryItem(
        doc_id="CAM-TEST-001",
        title="Test",
        domain="TEST",
        cls="Root",
        parent_source="— (root)",
        instrument_class="charter",
        version="1.0",
        status="Active",
        effect="Binding",
        enforcement="CAM Standard",
        review_state="Current",
        authority_role="Domain Authority",
        source_authority="Source-Authoritative",
        link="Charters/CAM-TEST-001.md",
    )
    rendered = registry.render_registry([row])
    assert "Governance Standard" in rendered
    assert "Source Authority" in rendered
    assert "| Operative |" in rendered
    assert "creates authority" not in rendered.lower()
