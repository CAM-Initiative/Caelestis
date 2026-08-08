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

def validate(doc):
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
        errors=validate(doc)
        if errors: print(f"FAIL {path}: " + "; ".join(errors)); failed=True
        else: print(f"PASS {path}")
    return 1 if failed else 0
if __name__ == "__main__": raise SystemExit(main())
