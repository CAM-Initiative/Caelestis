import importlib.util
import pathlib

spec = importlib.util.spec_from_file_location(
    'sup04_map_validator',
    pathlib.Path(__file__).resolve().parents[1] / 'validate_sup04_transmutation_map.py',
)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def base_row(**overrides):
    row = {
        'family_id': 'X',
        'canonical_name': 'Example',
        'family_kind': 'standalone_family',
        'parent_family': '',
        'collision_status': 'none',
        'source_instrument': 'CAM-EXAMPLE',
        'source_path': 'Governance/Example.md',
        'source_section': '§1',
        'declaration_heading': 'Example',
        'declaration_line_number': 1,
        'current_primary_type_label': 'Operational / Governance',
        'proposed_primary_type_code': 'TPT.OPERATIONAL',
        'proposed_subtype_codes': ['TST.DECISION_STATE'],
        'proposed_modifier_codes': ['TMOD.GOVERNANCE'],
        'proposed_scope_code': 'TSCOPE.CONTEXTUAL',
        'proposed_authority_protection_level': 'APL.PROTECTED',
        'controlled_values_detected': [],
        'schema_fields_detected': [],
        'transformation_policy': 'facet_transmutation_candidate; preserve_evidence_fields; no_source_rewrite',
        'review_status': 'deterministic_proposed',
        'notes': 'test',
    }
    row.update(overrides)
    return row


def test_valid_map_passes_with_human_review_warning(tmp_path):
    path = tmp_path / 'map.json'
    path.write_text(__import__('json').dumps([base_row(review_status='human_review_required')]))
    errors, warnings = validator.validate(path)
    assert errors == []
    assert any('ambiguous mapping requires human review' in w for w in warnings)


def test_invalid_sup04_value_fails(tmp_path):
    path = tmp_path / 'map.json'
    path.write_text(__import__('json').dumps([base_row(proposed_primary_type_code='TPT.LEGAL')]))
    errors, warnings = validator.validate(path)
    assert any('proposed_primary_type_code has invalid SUP-04 value' in e for e in errors)


def test_collision_risk_must_remain_protected(tmp_path):
    path = tmp_path / 'map.json'
    path.write_text(__import__('json').dumps([
        base_row(
            family_id='A',
            collision_status='legacy_collision_risk',
            proposed_authority_protection_level='APL.DESCRIPTIVE',
        )
    ]))
    errors, warnings = validator.validate(path)
    assert any('collision-risk family must remain APL.PROTECTED' in e for e in errors)
