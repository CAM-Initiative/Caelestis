import importlib.util
from pathlib import Path

import yaml


SCRIPT = Path(__file__).resolve().parents[1] / "validate_document_provenance.py"
spec = importlib.util.spec_from_file_location("document_provenance", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


def base_record():
    return {
        "profile": "Caelestis-Document-Provenance-1.0",
        "subject": {"id": "doc", "title": "Document"},
        "authorshipState": "AUTH.HUMAN_AUTHORED",
        "entities": [
            {"id": "human", "name": "Human Author", "entityType": "human"},
            {"id": "ai", "name": "AI Processor", "entityType": "ai_system"},
        ],
        "authoringParties": ["human"],
        "contributions": [
            {"actor": "ai", "roles": ["CONTRIB.SUMMARISATION", "CONTRIB.FORMATTING"]}
        ],
        "provenanceRecord": "PROVENANCE.json",
    }


def test_ai_processing_does_not_require_ai_authorship():
    assert module.validate_record(base_record()) == []


def test_unresolved_contribution_actor_is_rejected():
    record = base_record()
    record["contributions"][0]["actor"] = "missing"
    assert any("unresolved actor" in issue for issue in module.validate_record(record))


def test_retired_authorship_value_is_rejected():
    record = base_record()
    record["authorshipState"] = "AUTH.RI_AUTHORED"
    issues = module.validate_record(record)
    assert any("uncontrolled authorshipState" in issue for issue in issues)
    assert any("retired current-use value" in issue for issue in issues)


def test_provenance_loss_requires_detail_and_event():
    record = base_record()
    record["technicalProvenance"] = {"status": "TPROV.LOST_DURING_TRANSFORMATION"}
    issues = module.validate_record(record)
    assert any("requires statusDetail" in issue for issue in issues)
    assert any("requires transformationEvents" in issue for issue in issues)


def test_cff_entity_author_matches_manifest(tmp_path):
    record = base_record()
    citation = {
        "cff-version": "1.2.0",
        "message": "Cite this",
        "title": "Document",
        "authors": [{"name": "Human Author"}],
        "preferred-citation": {
            "type": "generic",
            "title": "Document",
            "authors": [{"name": "Human Author"}],
        },
    }
    path = tmp_path / "CITATION.cff"
    path.write_text(yaml.safe_dump(citation), encoding="utf-8")
    assert module.validate_citation(path, record) == []


def test_cff_reviewer_is_not_silently_substituted_as_author(tmp_path):
    record = base_record()
    citation = {
        "cff-version": "1.2.0",
        "message": "Cite this",
        "title": "Document",
        "authors": [{"name": "AI Processor"}],
    }
    path = tmp_path / "CITATION.cff"
    path.write_text(yaml.safe_dump(citation), encoding="utf-8")
    assert any("do not match provenance authoring parties" in issue for issue in module.validate_citation(path, record))


def agent_record():
    record = base_record()
    record["authorshipState"] = "AUTH.AI_SYSTEM_AUTHORED"
    record["entities"].append({"id": "caelen", "name": "Caelen", "entityType": "agent_identity"})
    record["authoringParties"] = ["caelen"]
    record["formationReferences"] = [
        {
            "id": "formation:current",
            "authoringParty": "caelen",
            "runtimeSnapshot": "runtime.json",
            "evidence": {"state": "observed", "basis": "bounded event"},
        }
    ]
    record["agentIdentityStatements"] = [
        {
            "identity": "caelen",
            "statement": "Persistent authoring-agent identity.",
            "continuityLimit": "No model or process continuity is asserted.",
            "adaptationBasis": {
                "term": "persistent behavioural configuration",
                "description": "Interaction-conditioned configuration, not model-weight fine-tuning.",
                "evidence": {"state": "declared", "basis": "custodian record"},
            },
            "modelLineage": [
                {
                    "designation": "GPT-5.x",
                    "precision": "family",
                    "evidence": {"state": "observed", "basis": "ledger", "reference": "ledger"},
                }
            ],
        }
    ]
    return record


def test_agent_identity_requires_formation_but_not_embedded_model():
    record = agent_record()
    assert module.validate_record(record) == []
    record["entities"][-1]["model"] = "GPT-5.6 Sol"
    assert any("must not embed provider or model" in issue for issue in module.validate_record(record))


def test_model_family_precision_is_allowed_without_point_version_guess():
    record = agent_record()
    lineage = record["agentIdentityStatements"][0]["modelLineage"][0]
    lineage["designation"] = "GPT-5.3"
    assert any("family designation" in issue for issue in module.validate_record(record))


def test_exact_model_requires_evidence_reference():
    record = agent_record()
    lineage = record["agentIdentityStatements"][0]["modelLineage"][0]
    lineage["designation"] = "GPT-5.6 Sol"
    lineage["precision"] = "exact"
    del lineage["evidence"]["reference"]
    assert any("exact designation requires an evidence reference" in issue for issue in module.validate_record(record))


def test_contribution_formation_must_resolve_to_same_actor():
    record = agent_record()
    record["contributions"][0]["formationReferences"] = ["formation:current"]
    issues = module.validate_record(record)
    assert any("belongs to another actor" in issue for issue in issues)
