#!/usr/bin/env python3
"""Validate document-level provenance, repository citation alignment and retired values."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
AUTH_VALUES = {
    "AUTH.HUMAN_AUTHORED",
    "AUTH.AI_SYSTEM_AUTHORED",
    "AUTH.CO_AUTHORED",
    "AUTH.OTHER_AUTHORSHIP",
    "AUTH.UNDETERMINED",
}
CONTRIBUTION_VALUES = {
    "CONTRIB.SUBSTANTIVE_DRAFTING",
    "CONTRIB.SUBSTANTIVE_REVISION",
    "CONTRIB.SYNTHESIS",
    "CONTRIB.TRANSLATION",
    "CONTRIB.SUMMARISATION",
    "CONTRIB.STANDARD_EDITING",
    "CONTRIB.FORMATTING",
    "CONTRIB.REVIEW",
    "CONTRIB.RETRIEVAL",
    "CONTRIB.CLASSIFICATION",
    "CONTRIB.OTHER_TRANSFORMATION",
}
TECHNICAL_PROVENANCE_VALUES = {
    "TPROV.PRESENT",
    "TPROV.ABSENT",
    "TPROV.PROVIDER_MANAGED",
    "TPROV.LOST_DURING_TRANSFORMATION",
    "TPROV.STRIPPED_BY_DESIGN",
    "TPROV.UNSUPPORTED",
    "TPROV.UNKNOWN",
}
ENTITY_TYPES = {"human", "agent_identity", "ai_system", "organization", "automated_process", "other", "unknown"}
FORMATION_EVIDENCE_STATES = {"declared", "observed", "verified", "unknown"}
MODEL_PRECISIONS = {"family", "exact", "unknown"}
RETIRED_CURRENT_VALUES = ("AUTH.RI_AUTHORED", "PCLASS.SYNTHETIC")
ACTOR_LIST_FIELDS = (
    "authoringParties",
    "humanReviewers",
    "editorialResponsibility",
    "adoptionAuthority",
    "publicationAuthority",
)


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return data


def entity_display_name(entity: dict[str, Any]) -> str:
    return str(entity.get("name", "")).strip()


def entity_citation_name(entity: dict[str, Any]) -> str:
    """Return the declared bibliographic label, or the entity display name."""
    if "citationName" not in entity:
        return entity_display_name(entity)
    value = entity.get("citationName")
    return value.strip() if isinstance(value, str) else ""


def cff_author_name(author: dict[str, Any]) -> str:
    if author.get("name"):
        return str(author["name"]).strip()
    given = str(author.get("given-names", "")).strip()
    family = str(author.get("family-names", "")).strip()
    return " ".join(part for part in (given, family) if part)


def validate_formation_evidence(value: Any, *, source: str, location: str) -> list[str]:
    if not isinstance(value, dict):
        return [f"{source}: {location} evidence must be an object"]
    issues: list[str] = []
    if value.get("state") not in FORMATION_EVIDENCE_STATES:
        issues.append(f"{source}: {location} has uncontrolled evidence state")
    if not value.get("basis"):
        issues.append(f"{source}: {location} evidence requires basis")
    return issues


def validate_record(
    record: dict[str, Any], *, source: str = "PROVENANCE.json", root: Path | None = None
) -> list[str]:
    issues: list[str] = []

    if record.get("profile") != "Caelestis-Document-Provenance-1.0":
        issues.append(f"{source}: invalid or missing profile")
    subject = record.get("subject")
    if not isinstance(subject, dict) or not subject.get("id") or not subject.get("title"):
        issues.append(f"{source}: subject requires id and title")
    authorship = record.get("authorshipState")
    if authorship not in AUTH_VALUES:
        issues.append(f"{source}: uncontrolled authorshipState {authorship!r}")
    if not record.get("provenanceRecord"):
        issues.append(f"{source}: provenanceRecord is required")

    entities = record.get("entities")
    if not isinstance(entities, list) or not entities:
        issues.append(f"{source}: entities must be a non-empty array")
        entities = []
    by_id: dict[str, dict[str, Any]] = {}
    declared_citation_names: dict[str, list[str]] = {}
    for index, entity in enumerate(entities):
        if not isinstance(entity, dict):
            issues.append(f"{source}: entities[{index}] must be an object")
            continue
        entity_id = str(entity.get("id", "")).strip()
        if not entity_id:
            issues.append(f"{source}: entities[{index}] requires id")
            continue
        if entity_id in by_id:
            issues.append(f"{source}: duplicate entity id {entity_id!r}")
        by_id[entity_id] = entity
        if not entity_display_name(entity):
            issues.append(f"{source}: entity {entity_id!r} requires name")
        if entity.get("entityType") not in ENTITY_TYPES:
            issues.append(f"{source}: entity {entity_id!r} has uncontrolled entityType")
        if entity.get("entityType") == "agent_identity" and (entity.get("provider") or entity.get("model")):
            issues.append(f"{source}: agent identity {entity_id!r} must not embed provider or model identity")
        if "citationName" in entity:
            citation_name = entity.get("citationName")
            if not isinstance(citation_name, str) or not citation_name.strip():
                issues.append(f"{source}: entity {entity_id!r} citationName must be a non-blank string")
            elif citation_name != citation_name.strip() or any(ord(character) < 32 for character in citation_name):
                issues.append(f"{source}: entity {entity_id!r} has malformed citationName")
            else:
                declared_citation_names.setdefault(citation_name.casefold(), []).append(entity_id)

    for normalized_name, owner_ids in declared_citation_names.items():
        if len(owner_ids) > 1:
            issues.append(
                f"{source}: citationName is ambiguous across entities {sorted(owner_ids)}"
            )
        colliding_ids = sorted(
            entity_id
            for entity_id, entity in by_id.items()
            if entity_id not in owner_ids
            and entity_display_name(entity).casefold() == normalized_name
        )
        if colliding_ids:
            issues.append(
                f"{source}: citationName for {sorted(owner_ids)} is also the name of separate "
                f"entity or entities {colliding_ids}"
            )

    def require_refs(field: str) -> None:
        value = record.get(field, [])
        if value is None:
            return
        if not isinstance(value, list):
            issues.append(f"{source}: {field} must be an array")
            return
        for ref in value:
            if ref not in by_id:
                issues.append(f"{source}: {field} contains unresolved entity {ref!r}")

    for field in ACTOR_LIST_FIELDS:
        require_refs(field)

    authoring_parties = record.get("authoringParties", [])
    if authorship != "AUTH.UNDETERMINED" and not authoring_parties:
        issues.append(f"{source}: authoringParties required for determined authorship")

    formations = record.get("formationReferences", [])
    if formations is not None and not isinstance(formations, list):
        issues.append(f"{source}: formationReferences must be an array")
        formations = []
    formation_by_id: dict[str, dict[str, Any]] = {}
    for index, formation in enumerate(formations or []):
        location = f"formationReferences[{index}]"
        if not isinstance(formation, dict):
            issues.append(f"{source}: {location} must be an object")
            continue
        formation_id = str(formation.get("id", "")).strip()
        if not formation_id:
            issues.append(f"{source}: {location} requires id")
            continue
        if formation_id in formation_by_id:
            issues.append(f"{source}: duplicate formation id {formation_id!r}")
        formation_by_id[formation_id] = formation
        authoring_party = formation.get("authoringParty")
        if authoring_party not in by_id:
            issues.append(f"{source}: {location} has unresolved authoringParty {authoring_party!r}")
        elif by_id[authoring_party].get("entityType") not in {"agent_identity", "ai_system"}:
            issues.append(f"{source}: {location} authoringParty is not an agent identity or AI system")
        snapshot = formation.get("runtimeSnapshot")
        if not isinstance(snapshot, str) or not snapshot.strip():
            issues.append(f"{source}: {location} requires runtimeSnapshot")
        issues.extend(validate_formation_evidence(formation.get("evidence"), source=source, location=location))
        if root is not None and isinstance(snapshot, str) and snapshot:
            snapshot_path = root / snapshot
            if not snapshot_path.is_file():
                issues.append(f"{source}: {location} runtimeSnapshot does not resolve: {snapshot!r}")

    for party in authoring_parties or []:
        if party in by_id and by_id[party].get("entityType") == "agent_identity":
            if not any(item.get("authoringParty") == party for item in formation_by_id.values()):
                issues.append(f"{source}: authoring agent identity {party!r} requires a formation reference")

    statements = record.get("agentIdentityStatements", [])
    if statements is not None and not isinstance(statements, list):
        issues.append(f"{source}: agentIdentityStatements must be an array")
        statements = []
    statement_identities = set()
    for index, statement in enumerate(statements or []):
        location = f"agentIdentityStatements[{index}]"
        if not isinstance(statement, dict):
            issues.append(f"{source}: {location} must be an object")
            continue
        identity = statement.get("identity")
        statement_identities.add(identity)
        if identity not in by_id or by_id[identity].get("entityType") != "agent_identity":
            issues.append(f"{source}: {location} identity must resolve to an agent_identity")
        for field in ("statement", "continuityLimit"):
            if not statement.get(field):
                issues.append(f"{source}: {location} requires {field}")
        adaptation = statement.get("adaptationBasis")
        if not isinstance(adaptation, dict):
            issues.append(f"{source}: {location} adaptationBasis must be an object")
        else:
            if adaptation.get("term") != "persistent behavioural configuration":
                issues.append(f"{source}: {location} must use persistent behavioural configuration")
            if not adaptation.get("description"):
                issues.append(f"{source}: {location} adaptationBasis requires description")
            issues.extend(validate_formation_evidence(adaptation.get("evidence"), source=source, location=f"{location}.adaptationBasis"))
        lineage = statement.get("modelLineage")
        if not isinstance(lineage, list) or not lineage:
            issues.append(f"{source}: {location} requires modelLineage")
        else:
            for lineage_index, entry in enumerate(lineage):
                entry_location = f"{location}.modelLineage[{lineage_index}]"
                if not isinstance(entry, dict):
                    issues.append(f"{source}: {entry_location} must be an object")
                    continue
                designation = str(entry.get("designation", "")).strip()
                precision = entry.get("precision")
                if precision not in MODEL_PRECISIONS:
                    issues.append(f"{source}: {entry_location} has uncontrolled precision")
                if designation.casefold() in {"caelen", "chatgpt"}:
                    issues.append(f"{source}: {entry_location} uses agent or harness identity as model")
                if precision == "family" and not re.fullmatch(r"GPT-\d+\.x", designation):
                    issues.append(f"{source}: {entry_location} family designation must use a form such as GPT-5.x")
                if precision == "exact" and (designation.endswith(".x") or "Series" in designation):
                    issues.append(f"{source}: {entry_location} exact designation is not exact")
                if precision == "unknown" and designation.casefold() not in {"unknown", "undetermined"}:
                    issues.append(f"{source}: {entry_location} unknown precision requires unknown or undetermined designation")
                issues.extend(validate_formation_evidence(entry.get("evidence"), source=source, location=entry_location))
                evidence = entry.get("evidence")
                if precision == "exact" and isinstance(evidence, dict) and not evidence.get("reference"):
                    issues.append(f"{source}: {entry_location} exact designation requires an evidence reference")

    for party in authoring_parties or []:
        if party in by_id and by_id[party].get("entityType") == "agent_identity" and party not in statement_identities:
            issues.append(f"{source}: authoring agent identity {party!r} requires an agent identity statement")

    contributions = record.get("contributions", [])
    if contributions is not None and not isinstance(contributions, list):
        issues.append(f"{source}: contributions must be an array")
        contributions = []
    for index, contribution in enumerate(contributions or []):
        if not isinstance(contribution, dict):
            issues.append(f"{source}: contributions[{index}] must be an object")
            continue
        actor = contribution.get("actor")
        if actor not in by_id:
            issues.append(f"{source}: contributions[{index}] has unresolved actor {actor!r}")
        roles = contribution.get("roles")
        if not isinstance(roles, list) or not roles:
            issues.append(f"{source}: contributions[{index}] requires roles")
        else:
            invalid = sorted(set(roles) - CONTRIBUTION_VALUES)
            if invalid:
                issues.append(f"{source}: contributions[{index}] has uncontrolled roles {invalid}")
        contribution_formations = contribution.get("formationReferences", [])
        if not isinstance(contribution_formations, list):
            issues.append(f"{source}: contributions[{index}].formationReferences must be an array")
        else:
            for formation_ref in contribution_formations:
                if formation_ref not in formation_by_id:
                    issues.append(f"{source}: contributions[{index}] has unresolved formation {formation_ref!r}")
                elif formation_by_id[formation_ref].get("authoringParty") != actor:
                    issues.append(f"{source}: contributions[{index}] formation {formation_ref!r} belongs to another actor")

    for reviewer in record.get("humanReviewers", []) or []:
        if reviewer in by_id and by_id[reviewer].get("entityType") != "human":
            issues.append(f"{source}: humanReviewers entry {reviewer!r} is not a human entity")

    technical = record.get("technicalProvenance")
    if technical is not None:
        if not isinstance(technical, dict):
            issues.append(f"{source}: technicalProvenance must be an object")
        else:
            status = technical.get("status")
            if status not in TECHNICAL_PROVENANCE_VALUES:
                issues.append(f"{source}: uncontrolled technical provenance status {status!r}")
            if status in {"TPROV.LOST_DURING_TRANSFORMATION", "TPROV.STRIPPED_BY_DESIGN"}:
                if not technical.get("statusDetail"):
                    issues.append(f"{source}: {status} requires statusDetail")
                if not technical.get("transformationEvents"):
                    issues.append(f"{source}: {status} requires transformationEvents")

    serialized = json.dumps(record, ensure_ascii=False)
    for retired in RETIRED_CURRENT_VALUES:
        if retired in serialized:
            issues.append(f"{source}: retired current-use value {retired!r}")
    return issues


def validate_citation(citation_path: Path, record: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    citation = yaml.safe_load(citation_path.read_text(encoding="utf-8"))
    if not isinstance(citation, dict):
        return [f"{citation_path}: expected a YAML object"]
    for field in ("cff-version", "message", "title", "authors"):
        if not citation.get(field):
            issues.append(f"{citation_path}: missing required CFF field {field}")
    if str(citation.get("cff-version")) != "1.2.0":
        issues.append(f"{citation_path}: cff-version must be 1.2.0")
    if "license" in citation and str(citation["license"]).startswith("LicenseRef-"):
        issues.append(f"{citation_path}: non-SPDX licence must use license-url, not license")

    authors = citation.get("authors", [])
    if not isinstance(authors, list) or not authors:
        issues.append(f"{citation_path}: authors must be a non-empty array")
        authors = []
    for index, author in enumerate(authors):
        if not isinstance(author, dict) or not cff_author_name(author):
            issues.append(f"{citation_path}: authors[{index}] is not a valid person or entity author")

    entities = {entity["id"]: entity for entity in record.get("entities", []) if isinstance(entity, dict) and entity.get("id")}
    expected = [
        entity_citation_name(entities[entity_id])
        for entity_id in record.get("authoringParties", [])
        if entity_id in entities
    ]
    actual = [cff_author_name(author) for author in authors if isinstance(author, dict)]
    if actual != expected:
        issues.append(f"{citation_path}: CFF authors {actual} do not match provenance authoring parties {expected}")

    preferred = citation.get("preferred-citation")
    if isinstance(preferred, dict):
        preferred_names = [
            cff_author_name(author)
            for author in preferred.get("authors", [])
            if isinstance(author, dict)
        ]
        if preferred_names != actual:
            issues.append(f"{citation_path}: preferred-citation authors differ from canonical CFF authors")
    return issues


def normative_markdown(text: str) -> str:
    return re.split(
        r"^##\s+\d+(?:\.\d+)?\s+Amendment Ledger\s*$",
        text,
        maxsplit=1,
        flags=re.MULTILINE,
    )[0]


def retired_operative_value_issues(root: Path) -> list[str]:
    issues: list[str] = []
    governance = root / "Governance"
    for path in sorted(governance.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".md", ".json", ".yaml", ".yml"}:
            continue
        rel = path.relative_to(root).as_posix()
        if rel.startswith("Governance/Drafts/"):
            continue
        text = path.read_text(encoding="utf-8")
        if path.suffix.lower() == ".md":
            text = normative_markdown(text)
        for retired in RETIRED_CURRENT_VALUES:
            if retired in text:
                issues.append(f"{rel}: retired current-use value {retired!r}")
    return issues


def validate_repository(root: Path = ROOT) -> list[str]:
    manifest_path = root / "PROVENANCE.json"
    citation_path = root / "CITATION.cff"
    if not manifest_path.exists():
        return ["PROVENANCE.json: missing repository provenance manifest"]
    record = load_json(manifest_path)
    issues = validate_record(record, source=manifest_path.relative_to(root).as_posix(), root=root)
    if not citation_path.exists():
        issues.append("CITATION.cff: missing citation metadata")
    else:
        issues.extend(validate_citation(citation_path, record))
    issues.extend(retired_operative_value_issues(root))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    issues = validate_repository(args.root.resolve())
    for issue in issues:
        print(f"ERROR: {issue}")
    print(f"Document provenance issues: {len(issues)}")
    if issues:
        return 1
    print("Document provenance validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
