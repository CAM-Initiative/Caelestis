#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OPERATIVE_DIRS = [
    ROOT / "Governance" / "Constitution",
    ROOT / "Governance" / "Charters",
    ROOT / "Governance" / "Laws",
    ROOT / "Governance" / "Standards",
]
DRAFT_DIR = ROOT / "Governance" / "Drafts"

FIELDS = {
    "status": "Status",
    "effect": "Effect",
    "governance standard": "Governance Standard",
    "review state": "Review State",
    "authority role": "Authority Role",
    "source authority": "Source Authority",
    "parent instrument": "Parent Instrument",
    "constitutional authority": "Constitutional Authority",
}

ALLOWED = {
    "Status": {"Draft", "Proposed", "Adopted", "Active", "Deprecated", "Superseded", "Retired"},
    "Effect": {"Interpretive", "Operational", "Binding", "Transitional", "Archival"},
    "Governance Standard": {"Not Enforceable", "Registry Standard", "CAM Standard", "CAM Enhanced Standard", "Architectum Standard", "Archival"},
    "Review State": {"Current", "Review Required", "Under Review", "Verification Required", "Migration Review", "No Further Review Scheduled", "Historical Record"},
    "Authority Role": {"Constitutional Authority", "Constitutional Schedule Authority", "Domain Authority", "Supplementary Authority", "Operational Authority", "Metadata Authority", "Registry Authority", "Interpretive Authority", "Assurance Authority", "No Independent Authority"},
    "Source Authority": {"Source-Authoritative", "Derived Authority", "Applied Authority", "Informative Only", "Non-Operative Draft", "Historical Only"},
}

META_RE = re.compile(r"^\s*(?:\*\*)?([A-Za-z][A-Za-z ]*[A-Za-z])(?:\*\*)?\s*:\s*(.+?)\s*$")
INSTRUMENT_ID_RE = re.compile(r"\bCAM-[A-Z0-9]+(?:-[A-Z0-9]+)+\b")


def clean(value: str) -> str:
    value = value.strip()
    if value.endswith("  "):
        value = value[:-2].rstrip()
    value = re.sub(r"^\*\*|\*\*$", "", value).strip()
    return value


def parse(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines()[:220]:
        match = META_RE.match(line)
        if not match:
            continue
        key = re.sub(r"\s+", " ", match.group(1).strip().lower())
        if key in FIELDS and FIELDS[key] not in out:
            out[FIELDS[key]] = clean(match.group(2))
    return out


def files() -> list[tuple[Path, bool]]:
    found: list[tuple[Path, bool]] = []
    for directory in OPERATIVE_DIRS:
        if directory.exists():
            for path in directory.rglob("*.md"):
                if "Index" not in path.name and not path.name.endswith("README.md"):
                    found.append((path, False))
    if DRAFT_DIR.exists():
        for path in DRAFT_DIR.rglob("*.md"):
            if path.name != "README.md":
                found.append((path, True))
    return sorted(found, key=lambda item: str(item[0]))


def known_instrument_ids(found: list[tuple[Path, bool]]) -> set[str]:
    return {path.stem for path, is_draft in found if not is_draft}


def evaluate(path: Path, is_draft: bool, meta: dict[str, str], known_ids: set[str]) -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []
    rel = path.relative_to(ROOT).as_posix()

    for field in ALLOWED:
        value = meta.get(field, "")
        if not value:
            issues.append({"path": rel, "field": field, "value": "", "code": "missing_required_field", "severity": "error"})
        elif value not in ALLOWED[field]:
            issues.append({"path": rel, "field": field, "value": value, "code": "uncontrolled_value", "severity": "error"})

    status = meta.get("Status", "")
    effect = meta.get("Effect", "")
    tier = meta.get("Governance Standard", "")
    role = meta.get("Authority Role", "")
    source = meta.get("Source Authority", "")
    parent = meta.get("Parent Instrument", "")

    def add(code: str, field: str, value: str, severity: str = "error") -> None:
        issues.append({"path": rel, "field": field, "value": value, "code": code, "severity": severity})

    if is_draft:
        if status != "Draft": add("draft_namespace_status_mismatch", "Status", status)
        if tier != "Not Enforceable": add("draft_namespace_tier_mismatch", "Governance Standard", tier)
        if source != "Non-Operative Draft": add("draft_namespace_source_mismatch", "Source Authority", source)
        if role != "No Independent Authority": add("draft_namespace_role_mismatch", "Authority Role", role)
    elif status in {"Draft", "Proposed"}:
        add("nonoperative_status_in_operative_namespace", "Status", status)

    if status in {"Draft", "Proposed"}:
        if tier != "Not Enforceable": add("nonoperative_status_enforceable_tier", "Governance Standard", tier)
        if source not in {"Non-Operative Draft", "Informative Only"}: add("nonoperative_status_authority_conflict", "Source Authority", source)

    if status in {"Active", "Adopted"} and source in {"Non-Operative Draft", "Historical Only"}:
        add("operative_status_nonoperative_source", "Source Authority", source)

    if status in {"Superseded", "Retired"} and effect not in {"Archival", "Transitional"}:
        add("historical_status_nonhistorical_effect", "Effect", effect)

    if effect == "Archival":
        if tier != "Archival": add("archival_effect_tier_conflict", "Governance Standard", tier)
        if source != "Historical Only": add("archival_effect_source_conflict", "Source Authority", source)

    if effect == "Binding":
        if status not in {"Adopted", "Active"}: add("binding_effect_lifecycle_conflict", "Status", status)
        if source in {"Informative Only", "Non-Operative Draft", "Historical Only", ""}: add("binding_effect_source_conflict", "Source Authority", source)

    if tier == "Registry Standard" and role not in {"Metadata Authority", "Registry Authority", "Operational Authority", "Assurance Authority"}:
        add("registry_tier_role_conflict", "Authority Role", role)

    if role == "No Independent Authority" and source == "Source-Authoritative":
        add("no_authority_source_authoritative_conflict", "Source Authority", source)

    if role == "Constitutional Authority" and not any(namespace in f"/{rel}" for namespace in {"/Constitution/", "/Laws/"}):
        add("constitutional_role_outside_constitution", "Authority Role", role)

    if role == "Constitutional Schedule Authority":
        if "/Constitution/" not in f"/{rel}":
            add("constitutional_schedule_role_outside_constitution", "Authority Role", role)
        if not parent:
            add("constitutional_schedule_parent_missing", "Parent Instrument", parent)

    if role == "Domain Authority" and "/Charters/" not in f"/{rel}":
        add("domain_role_outside_charters", "Authority Role", role)

    if source in {"Derived Authority", "Applied Authority"} and not parent:
        add("derived_or_applied_parent_missing", "Parent Instrument", parent)

    if source == "Informative Only":
        if role != "No Independent Authority":
            add("informative_source_role_conflict", "Authority Role", role)
        if effect == "Binding":
            add("informative_source_binding_conflict", "Effect", effect)

    if parent:
        identifiers = INSTRUMENT_ID_RE.findall(parent)
        if not identifiers:
            add("parent_identifier_missing", "Parent Instrument", parent)
        else:
            parent_id = identifiers[0]
            if parent_id == path.stem:
                add("self_parent_lineage", "Parent Instrument", parent)
            elif parent_id not in known_ids:
                add("unresolved_parent_instrument", "Parent Instrument", parent)

    return issues


def add_circular_lineage_issues(records: list[dict], issues: list[dict]) -> None:
    by_id = {Path(record["path"]).stem: record for record in records}
    parent_by_id: dict[str, str] = {}
    for instrument_id, record in by_id.items():
        parent = record["metadata"].get("Parent Instrument", "")
        identifiers = INSTRUMENT_ID_RE.findall(parent)
        if identifiers and identifiers[0] in by_id:
            parent_by_id[instrument_id] = identifiers[0]

    for instrument_id, record in by_id.items():
        seen: set[str] = set()
        current = instrument_id
        while current in parent_by_id:
            if current in seen:
                issue = {
                    "path": record["path"],
                    "field": "Parent Instrument",
                    "value": record["metadata"].get("Parent Instrument", ""),
                    "code": "circular_parent_lineage",
                    "severity": "error",
                }
                record["issues"].append(issue)
                issues.append(issue)
                break
            seen.add(current)
            current = parent_by_id[current]


def render_md(summary: dict, records: list[dict], issues: list[dict]) -> str:
    lines = [
        "# Pass 4 — Metadata and Source-Authority Inventory",
        "",
        "Generated by `.github/scripts/audit_metadata_authority_contract.py`.",
        "",
        "## Summary",
        "",
        f"- Instruments scanned: **{summary['instruments_scanned']}**",
        f"- Operative instruments: **{summary['operative_instruments']}**",
        f"- Draft instruments: **{summary['draft_instruments']}**",
        f"- Instruments with one or more exceptions: **{summary['instruments_with_issues']}**",
        f"- Total exceptions: **{summary['total_issues']}**",
        "",
        "## Exception counts",
        "",
        "| Code | Count |",
        "|---|---:|",
    ]
    for code, count in summary["issues_by_code"].items():
        lines.append(f"| `{code}` | {count} |")

    lines.extend(["", "## Observed values", ""])
    for field, values in summary["observed_values"].items():
        lines.append(f"### {field}")
        lines.append("")
        lines.append("| Value | Count | Controlled |")
        lines.append("|---|---:|---|")
        for value, count in values.items():
            controlled = "yes" if value in ALLOWED[field] else "no"
            lines.append(f"| `{value or '[missing]'}` | {count} | {controlled} |")
        lines.append("")

    lines.extend(["## Instrument exceptions", "", "| Instrument | Field | Value | Exception |", "|---|---|---|---|"])
    for issue in issues:
        lines.append(f"| `{issue['path']}` | {issue['field']} | `{issue['value'] or '[missing]'}` | `{issue['code']}` |")

    lines.extend([
        "",
        "## Migration rule",
        "",
        "No exception in this register is automatically proof that the underlying doctrine or authority claim is valid. Semantically exact mappings may be automated; ambiguous authority claims require instrument-level review.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path, required=True)
    parser.add_argument("--md-out", type=Path, required=True)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    records = []
    issues = []
    observed: dict[str, Counter] = {field: Counter() for field in ALLOWED}
    operative = drafts = 0

    found = files()
    known_ids = known_instrument_ids(found)

    for path, is_draft in found:
        meta = parse(path)
        operative += int(not is_draft)
        drafts += int(is_draft)
        for field in ALLOWED:
            observed[field][meta.get(field, "")] += 1
        current = evaluate(path, is_draft, meta, known_ids)
        records.append({"path": path.relative_to(ROOT).as_posix(), "draft": is_draft, "metadata": meta, "issues": current})
        issues.extend(current)

    add_circular_lineage_issues(records, issues)

    issue_counts = Counter(issue["code"] for issue in issues)
    summary = {
        "instruments_scanned": len(records),
        "operative_instruments": operative,
        "draft_instruments": drafts,
        "instruments_with_issues": sum(bool(record["issues"]) for record in records),
        "total_issues": len(issues),
        "issues_by_code": dict(sorted(issue_counts.items())),
        "observed_values": {field: dict(sorted(counter.items(), key=lambda item: (-item[1], item[0]))) for field, counter in observed.items()},
    }

    payload = {"summary": summary, "records": records, "issues": issues}
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.md_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.md_out.write_text(render_md(summary, records, issues) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2, ensure_ascii=False))
    if args.strict and issues:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
