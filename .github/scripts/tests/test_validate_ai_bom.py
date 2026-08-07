import importlib.util
import pathlib


spec = importlib.util.spec_from_file_location(
    "validator", pathlib.Path(__file__).resolve().parents[1] / "validate_ai_bom.py"
)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def valid_document():
    return {
        "profile": "Caelestis-AI-BOM-1.0",
        "bom": {"serial": "urn:uuid:test", "version": 1, "issuedAt": "2026-08-07T18:00:00Z"},
        "subject": {"aiSystemId": "system:example", "name": "Example"},
        "elements": [{"id": "model:one", "type": "ai_model", "name": "One", "evidence": {"state": "verified", "basis": "manifest", "verifiedAt": "2026-08-07T18:00:00Z", "verifier": "assurance"}}],
        "relationships": [{"id": "rel:one", "from": "system:example", "to": "model:one", "type": "contains", "evidence": {"state": "declared", "basis": "baseline"}}],
    }


def test_valid_document_passes():
    assert validator.validate_document(valid_document()) == []


def test_observed_requires_timestamp():
    document = valid_document()
    document["elements"][0]["evidence"] = {"state": "observed", "basis": "scan"}
    assert any("observedAt" in error for error in validator.validate_document(document))


def test_relationship_endpoint_must_resolve():
    document = valid_document()
    document["relationships"][0]["to"] = "model:missing"
    assert any("does not resolve" in error for error in validator.validate_document(document))


def test_secret_value_is_rejected():
    document = valid_document()
    document["elements"][0]["private_key"] = "not allowed"
    assert any("prohibited" in error for error in validator.validate_document(document))


def test_cyclonedx_exchange_preserves_profile_boundary():
    exchange = {
        "bomFormat": "CycloneDX", "specVersion": "1.7", "serialNumber": "urn:uuid:test", "version": 1,
        "metadata": {"timestamp": "2026-08-07T18:00:00Z", "component": {"properties": [{"name": "org.caelestis.aibom.profile", "value": "Caelestis-AI-BOM-1.0"}]}},
        "components": [{"type": "machine-learning-model"}],
        "properties": [{"name": "org.caelestis.aibom.execution-evidence", "value": "not-asserted"}],
    }
    assert validator.validate_cyclonedx_exchange(exchange) == []
