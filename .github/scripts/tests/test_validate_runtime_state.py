import importlib.util
import json
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "validate_runtime_state.py"
spec = importlib.util.spec_from_file_location("runtime_state", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


def base_record():
    return {
        "profile": "Caelestis-Runtime-State-1.0",
        "aiSystemId": "system:example",
        "deploymentId": "deployment:example",
        "snapshotAt": "2026-08-15T00:00:00Z",
        "lifecycleState": "operation",
        "relational": {
            "participantCount": 2,
            "participantTypes": ["human_participant", "ai_agent"],
            "coordination": "human_mediated",
            "institutionalMediation": "service_mediated",
            "distribution": "single_service",
            "persistence": "cross_session",
            "dependency": "moderate",
            "jurisdictionalReach": "multi_jurisdiction",
            "impactScope": "public_population",
        },
        "reviewTriggers": ["model_change"],
        "evidence": {"posture": "observed", "basis": "snapshot"},
    }


def test_effective_elements_require_ai_bom_reference():
    record = base_record()
    record["effectiveElements"] = {"cognitionModelRef": "model:one"}
    assert any("requires aiBomReference" in issue for issue in module.validate(record))


def test_provider_harness_and_model_references_must_be_distinct():
    record = base_record()
    record["aiBomReference"] = "bom.json"
    record["effectiveElements"] = {
        "harnessRef": "element:same",
        "cognitionModelRef": "element:same",
    }
    assert any("must use distinct" in issue for issue in module.validate(record))


def test_cognition_model_and_harness_roles_are_checked(tmp_path):
    bom = {
        "elements": [
            {"id": "runtime:chatgpt", "type": "agent_runtime", "name": "ChatGPT"},
            {"id": "model:caelen", "type": "ai_model", "name": "Caelen"},
        ]
    }
    (tmp_path / "bom.json").write_text(json.dumps(bom), encoding="utf-8")
    record = base_record()
    record["aiBomReference"] = "bom.json"
    record["effectiveElements"] = {
        "harnessRef": "model:caelen",
        "cognitionModelRef": "runtime:chatgpt",
    }
    issues = module.validate(record, source_path=tmp_path / "runtime.json", root=tmp_path)
    assert any("cognitionModelRef must resolve to an ai_model" in issue for issue in issues)
    assert any("harnessRef must not resolve to an ai_model" in issue for issue in issues)
