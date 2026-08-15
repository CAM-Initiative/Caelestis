#!/usr/bin/env python3
"""Validate the repository's Caelestis AI-BOM canonical-profile invariants.

This uses only the Python standard library so it remains usable in the
governance rebuild workflow.  It validates profile rules in addition to the
published JSON Schema; exchange artefacts must separately be checked against
the applicable upstream SPDX or CycloneDX schema by their consumer.
"""
import argparse
import json
import pathlib
import re
import sys


PROFILE = "Caelestis-AI-BOM-1.0"
EVIDENCE_STATES = {"declared", "observed", "verified", "unknown_undisclosed"}
RELATIONSHIP_TYPES = {
    "contains", "depends_on", "invokes", "routes_to", "retrieves_from",
    "controls", "monitors", "deployed_on",
}
ELEMENT_TYPES = {
    "ai_model", "software", "dataset_or_knowledge", "memory_service",
    "tool_or_connector", "configuration", "orchestration_component",
    "agent_runtime", "infrastructure", "control", "interface", "service",
    "hardware", "other",
}
FORBIDDEN_KEY_RE = re.compile(r"(?:^|[_-])(secret|password|private[_-]?key)(?:$|[_-])", re.IGNORECASE)


def load_json(path: pathlib.Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, f"cannot parse JSON: {exc}"


def validate_evidence(evidence, location):
    errors = []
    if not isinstance(evidence, dict):
        return [f"{location}.evidence must be an object"]
    state = evidence.get("state")
    if state not in EVIDENCE_STATES:
        return [f"{location}.evidence.state must be one of {sorted(EVIDENCE_STATES)}"]
    if state in {"declared", "observed", "verified"} and not evidence.get("basis"):
        errors.append(f"{location}.evidence.basis is required for {state}")
    if state == "observed" and not evidence.get("observedAt"):
        errors.append(f"{location}.evidence.observedAt is required for observed")
    if state == "verified":
        for key in ("verifiedAt", "verifier"):
            if not evidence.get(key):
                errors.append(f"{location}.evidence.{key} is required for verified")
    if state == "unknown_undisclosed" and not evidence.get("knowledgeLimit"):
        errors.append(f"{location}.evidence.knowledgeLimit is required for unknown_undisclosed")
    return errors


def find_forbidden_keys(value, location="$"):
    errors = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_location = f"{location}.{key}"
            if FORBIDDEN_KEY_RE.search(key) and key != "secretReference":
                errors.append(f"{child_location} is prohibited; serialize a controlled reference, not a secret")
            errors.extend(find_forbidden_keys(child, child_location))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            errors.extend(find_forbidden_keys(child, f"{location}[{index}]"))
    return errors


def validate_document(document):
    errors = []
    if not isinstance(document, dict):
        return ["document must be a JSON object"]
    if document.get("profile") != PROFILE:
        errors.append(f"profile must equal {PROFILE}")

    bom = document.get("bom")
    if not isinstance(bom, dict):
        errors.append("bom must be an object")
    else:
        for key in ("serial", "version", "issuedAt"):
            if not bom.get(key):
                errors.append(f"bom.{key} is required")
        if not isinstance(bom.get("version"), int) or bom.get("version", 0) < 1:
            errors.append("bom.version must be an integer greater than or equal to 1")

    subject = document.get("subject")
    if not isinstance(subject, dict):
        errors.append("subject must be an object")
    else:
        for key in ("aiSystemId", "name"):
            if not subject.get(key):
                errors.append(f"subject.{key} is required")

    elements = document.get("elements")
    if not isinstance(elements, list) or not elements:
        errors.append("elements must be a non-empty array")
        elements = []
    element_ids = set()
    for index, element in enumerate(elements):
        location = f"elements[{index}]"
        if not isinstance(element, dict):
            errors.append(f"{location} must be an object")
            continue
        for key in ("id", "type", "name", "evidence"):
            if not element.get(key):
                errors.append(f"{location}.{key} is required")
        element_id = element.get("id")
        if element_id:
            if element_id in element_ids:
                errors.append(f"duplicate element id: {element_id}")
            element_ids.add(element_id)
        if element.get("type") not in ELEMENT_TYPES:
            errors.append(f"{location}.type is not a profile element type")
        if element.get("type") == "ai_model":
            model_name = str(element.get("name", "")).strip().casefold()
            model_id = str(element.get("id", "")).strip().casefold()
            if model_name in {"caelen", "chatgpt"} or model_id in {"caelen", "model:caelen", "model:chatgpt"}:
                errors.append(f"{location} uses an agent identity or Runtime harness as an AI-model identifier")
        errors.extend(validate_evidence(element.get("evidence"), location))
        controlled = element.get("controlledReference")
        if controlled is not None:
            if not isinstance(controlled, dict):
                errors.append(f"{location}.controlledReference must be an object")
            else:
                for key in ("reference", "role", "effectiveInterval", "custodian", "accessPath"):
                    if not controlled.get(key):
                        errors.append(f"{location}.controlledReference.{key} is required")

    relationships = document.get("relationships")
    if not isinstance(relationships, list):
        errors.append("relationships must be an array")
        relationships = []
    relationship_ids = set()
    valid_endpoints = set(element_ids)
    if isinstance(subject, dict) and subject.get("aiSystemId"):
        valid_endpoints.add(subject["aiSystemId"])
    for index, relationship in enumerate(relationships):
        location = f"relationships[{index}]"
        if not isinstance(relationship, dict):
            errors.append(f"{location} must be an object")
            continue
        for key in ("id", "from", "to", "type", "evidence"):
            if not relationship.get(key):
                errors.append(f"{location}.{key} is required")
        relationship_id = relationship.get("id")
        if relationship_id:
            if relationship_id in relationship_ids:
                errors.append(f"duplicate relationship id: {relationship_id}")
            relationship_ids.add(relationship_id)
        if relationship.get("type") not in RELATIONSHIP_TYPES:
            errors.append(f"{location}.type is not a profile relationship type")
        for endpoint in ("from", "to"):
            if relationship.get(endpoint) and relationship[endpoint] not in valid_endpoints:
                errors.append(f"{location}.{endpoint} does not resolve to an element or subject")
        errors.extend(validate_evidence(relationship.get("evidence"), location))

    links = document.get("evidenceLinks", [])
    if not isinstance(links, list):
        errors.append("evidenceLinks must be an array when present")
    else:
        for index, link in enumerate(links):
            location = f"evidenceLinks[{index}]"
            if not isinstance(link, dict) or not link.get("type") or not link.get("reference"):
                errors.append(f"{location} requires type and reference")
                continue
            if "evidence" in link:
                errors.extend(validate_evidence(link["evidence"], location))

    errors.extend(find_forbidden_keys(document))
    return errors


def properties_as_map(properties):
    if not isinstance(properties, list):
        return {}
    return {
        item.get("name"): item.get("value")
        for item in properties
        if isinstance(item, dict) and item.get("name")
    }


def validate_cyclonedx_exchange(document):
    """Check profile invariants in a CycloneDX exchange artefact.

    This is intentionally not a substitute for CycloneDX's upstream JSON Schema.
    """
    errors = []
    if document.get("bomFormat") != "CycloneDX":
        errors.append("bomFormat must equal CycloneDX")
    if document.get("specVersion") != "1.7":
        errors.append("specVersion must equal 1.7")
    if not document.get("serialNumber") or not isinstance(document.get("version"), int):
        errors.append("serialNumber and integer version are required")
    metadata = document.get("metadata")
    if not isinstance(metadata, dict) or not metadata.get("timestamp"):
        errors.append("metadata.timestamp is required")
    component = metadata.get("component") if isinstance(metadata, dict) else None
    profile_properties = properties_as_map(component.get("properties") if isinstance(component, dict) else None)
    if profile_properties.get("org.caelestis.aibom.profile") != PROFILE:
        errors.append("metadata.component must declare org.caelestis.aibom.profile")
    if not any(isinstance(item, dict) and item.get("type") == "machine-learning-model" for item in document.get("components", [])):
        errors.append("exchange artefact must include a machine-learning-model component")
    root_properties = properties_as_map(document.get("properties"))
    if root_properties.get("org.caelestis.aibom.execution-evidence") != "not-asserted":
        errors.append("exchange artefact must preserve the non-execution-evidence boundary")
    return errors


def validate_mapping_contract(document):
    errors = []
    if document.get("profile") != PROFILE or document.get("version") != "1.0":
        errors.append("mapping contract profile/version is invalid")
    sources = document.get("sources")
    if not isinstance(sources, dict):
        errors.append("mapping contract must declare sources")
    else:
        if sources.get("cyclonedx", {}).get("version") != "1.7":
            errors.append("mapping contract must declare CycloneDX 1.7")
        if sources.get("spdx", {}).get("version") != "3.0.1":
            errors.append("mapping contract must declare SPDX 3.0.1")
    if not isinstance(document.get("fields"), list) or not document["fields"]:
        errors.append("mapping contract must contain field mappings")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=pathlib.Path, help="Canonical or mapped AI-BOM JSON artefacts")
    args = parser.parse_args(argv)
    root = pathlib.Path(__file__).resolve().parents[2]
    paths = args.paths or [
        root / "Governance/Standards/examples/caelestis-ai-bom-1.0.example.json",
        root / "Governance/Standards/examples/caelestis-ai-bom-1.0.cyclonedx-1.7.example.json",
        root / "Governance/Standards/mappings/caelestis-ai-bom-1.0.mappings.json",
    ]
    failed = False
    for path in paths:
        loaded = load_json(path)
        if isinstance(loaded, tuple):
            document, parse_error = loaded
        else:
            document, parse_error = loaded, None
        if parse_error:
            errors = [parse_error]
        elif document.get("bomFormat") == "CycloneDX":
            errors = validate_cyclonedx_exchange(document)
        elif "sources" in document and "fields" in document:
            errors = validate_mapping_contract(document)
        else:
            errors = validate_document(document)
        if errors:
            failed = True
            for error in errors:
                print(f"FAIL {path}: {error}")
        else:
            print(f"PASS {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
