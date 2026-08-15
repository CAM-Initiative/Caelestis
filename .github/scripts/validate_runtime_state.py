#!/usr/bin/env python3
"""Validate the Caelestis Runtime State Profile's deterministic invariants."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PROFILE = "Caelestis-Runtime-State-1.0"
ENUMS = {
    "lifecycleState": {"design", "development", "evaluation", "deployment", "operation", "modification", "suspension", "investigation", "retirement", "unknown"},
    "coordination": {"independent", "coordinated", "orchestrated", "federated", "shared_control", "human_mediated", "unknown"},
    "institutionalMediation": {"unmediated", "service_mediated", "organisation_mediated", "employer_mediated", "public_authority_mediated", "other_mediated", "unknown"},
    "distribution": {"local", "single_service", "cross_service", "distributed", "external_service_dependent", "unknown"},
    "persistence": {"execution_only", "session", "cross_session", "deployment_persistent", "successor_persistent", "unknown"},
    "dependency": {"none", "low", "moderate", "high", "critical", "unknown"},
    "jurisdictionalReach": {"single_jurisdiction", "multi_jurisdiction", "unknown"},
    "impactScope": {"individual", "defined_group", "organisation", "public_population", "unknown"},
}
POSTURES = {"declared", "configured", "observed", "verified", "inferred", "unknown"}
SINGLE_EFFECTIVE_REFS = ("providerInfrastructureRef", "harnessRef", "cognitionModelRef")
LIST_EFFECTIVE_REFS = (
    "governanceConfigurationRefs", "adaptationContinuityRefs", "memoryContextRefs", "toolingRefs",
)

def validate(doc, *, source_path=None, root=ROOT):
    errors=[]
    for key in ("profile", "aiSystemId", "deploymentId", "snapshotAt", "lifecycleState", "relational", "evidence"):
        if key not in doc: errors.append(f"missing {key}")
    if doc.get("profile") != PROFILE: errors.append("invalid profile")
    if doc.get("lifecycleState") not in ENUMS["lifecycleState"]: errors.append("invalid lifecycleState")
    rel=doc.get("relational", {})
    if not isinstance(rel, dict): return errors+["relational must be an object"]
    for key, values in ENUMS.items():
        if key != "lifecycleState" and rel.get(key) not in values: errors.append(f"invalid relational.{key}")
    count=rel.get("participantCount")
    if count != "unknown" and (not isinstance(count, int) or count < 0): errors.append("participantCount must be a non-negative integer or unknown")
    if not isinstance(rel.get("participantTypes"), list) or not rel["participantTypes"]: errors.append("participantTypes must be a non-empty list")
    evidence=doc.get("evidence", {})
    if not isinstance(evidence, dict) or evidence.get("posture") not in POSTURES or not evidence.get("basis"):
        errors.append("evidence requires controlled posture and basis")
    if evidence.get("posture") == "inferred" and not evidence.get("reference"):
        errors.append("inferred state requires an evidence reference")
    effective = doc.get("effectiveElements")
    if effective is not None:
        if not isinstance(effective, dict) or not effective:
            errors.append("effectiveElements must be a non-empty object")
            effective = {}
        if not doc.get("aiBomReference"):
            errors.append("effectiveElements requires aiBomReference")
        scalar_refs = []
        for key in SINGLE_EFFECTIVE_REFS:
            value = effective.get(key)
            if value is not None and (not isinstance(value, str) or not value.strip()):
                errors.append(f"effectiveElements.{key} must be a non-empty string")
            elif value:
                scalar_refs.append(value)
        if len(scalar_refs) != len(set(scalar_refs)):
            errors.append("provider, harness and cognition model must use distinct element references")
        for key in LIST_EFFECTIVE_REFS:
            value = effective.get(key, [])
            if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
                errors.append(f"effectiveElements.{key} must be an array of non-empty strings")

        if source_path is not None and doc.get("aiBomReference"):
            bom_path = root / doc["aiBomReference"]
            try:
                bom = json.loads(bom_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"aiBomReference does not resolve: {exc}")
            else:
                elements = {
                    element.get("id"): element
                    for element in bom.get("elements", [])
                    if isinstance(element, dict) and element.get("id")
                }
                refs = [(key, effective.get(key)) for key in SINGLE_EFFECTIVE_REFS if effective.get(key)]
                refs.extend(
                    (key, ref)
                    for key in LIST_EFFECTIVE_REFS
                    for ref in effective.get(key, [])
                )
                for key, ref in refs:
                    if ref not in elements:
                        errors.append(f"effectiveElements.{key} contains unresolved AI-BOM element {ref!r}")
                cognition_ref = effective.get("cognitionModelRef")
                if cognition_ref in elements:
                    cognition = elements[cognition_ref]
                    if cognition.get("type") != "ai_model":
                        errors.append("cognitionModelRef must resolve to an ai_model element")
                    if str(cognition.get("name", "")).strip().casefold() in {"caelen", "chatgpt"}:
                        errors.append("cognitionModelRef must not identify Caelen or ChatGPT")
                for key in ("providerInfrastructureRef", "harnessRef"):
                    ref = effective.get(key)
                    if ref in elements and elements[ref].get("type") == "ai_model":
                        errors.append(f"{key} must not resolve to an ai_model element")
    triggers=doc.get("reviewTriggers", [])
    if not isinstance(triggers, list): errors.append("reviewTriggers must be a list")
    # Persisting or materially dependent state cannot omit reassessment.
    if rel.get("persistence") in {"cross_session", "deployment_persistent", "successor_persistent"} and not triggers:
        errors.append("persistent state requires reviewTriggers")
    if rel.get("dependency") in {"high", "critical"} and not triggers:
        errors.append("high/critical dependency requires reviewTriggers")
    return errors

def main():
    paths=[pathlib.Path(p) for p in sys.argv[1:]] or [ROOT / "Governance/Standards/examples/caelestis-runtime-state-1.0.example.json"]
    failed=False
    for path in paths:
        try: doc=json.loads(path.read_text())
        except Exception as exc: print(f"FAIL {path}: {exc}"); failed=True; continue
        errors=validate(doc, source_path=path)
        if errors: print(f"FAIL {path}: " + "; ".join(errors)); failed=True
        else: print(f"PASS {path}")
    return 1 if failed else 0
if __name__ == "__main__": raise SystemExit(main())
