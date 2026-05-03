#!/usr/bin/env python3
import json
import re
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GOVERNANCE_ROOT = REPO_ROOT / "Governance"
INDICES_ROOT = REPO_ROOT / ".github" / "Indices"
INDEX_JSON_PATH = INDICES_ROOT / "CAM.Governance.Symbolic-Structures.Index.json"
INDEX_MD_PATH = INDICES_ROOT / "CAM.Governance.Symbolic-Structures.Index.md"
REGISTRY_PATH = INDICES_ROOT / "CAM.Governance.Symbolic-Structures.Registry.json"
BASE_CANONICAL_URL = "https://github.com/CAM-Initiative/Registry/blob/main/"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
VALUE_RE = re.compile(r"\b([A-Z]{1,4}(?:-(?:\d+(?:\.\d+)?|[A-Z])|(?:\d+(?:\.\d+)?)))\b")
SECTION_PREFIX_RE = re.compile(r"^\s*(?:(?:\d+(?:\.\d+)*)|(?:[IVXLCDM]+))\.?\s+", re.IGNORECASE)

SCALE_KEYWORDS = {"scale", "taxonomy", "matrix", "classification", "level", "registry", "tier", "mode", "signal"}
COLUMN_TERMS = {"level", "tier", "scale", "category", "classification", "signal", "trigger", "domain", "runtime layer", "authority", "status", "mode"}
REDEFINITION_HINTS = {"means", "defined", "definition", "classified", "class", "tier", "level", "taxonomy", "matrix"}


def normalize_space(v: str) -> str:
    return re.sub(r"\s+", " ", v.strip())


def normalize_path(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def extract_prefix(value: str) -> str:
    m = re.match(r"^[A-Z]{1,4}", value)
    return m.group(0) if m else ""


def normalize_for_compare(v: str) -> str:
    s = normalize_space(v).lower()
    s = SECTION_PREFIX_RE.sub("", s)
    return re.sub(r"\s+", " ", s).strip(" .:-")


def normalize_title(v: str) -> str:
    out = normalize_space(v)
    while True:
        n = SECTION_PREFIX_RE.sub("", out)
        if n == out:
            return out.strip(" .:-")
        out = n


def extract_values(text: str) -> list[str]:
    return sorted(set(VALUE_RE.findall(text)))


def tokenize_row(line: str) -> list[str]:
    return [normalize_space(c) for c in line.strip().strip("|").split("|")]


def is_table_separator(line: str) -> bool:
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")):
        return False
    cols = [c.strip() for c in s.strip("|").split("|")]
    return bool(cols) and all(re.fullmatch(r":?-{3,}:?", c) for c in cols)


def load_registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def canonical_maps(registry: dict) -> tuple[dict[str, dict], dict[str, set[str]]]:
    by_prefix, allowed = {}, {}
    for row in registry.get("canonical_registered_structures", []):
        p = row.get("prefix", "")
        if not p:
            continue
        by_prefix[p] = row
        allowed[p] = set(row.get("canonical_codes", row.get("values", [])))
    return by_prefix, allowed


def classify_occurrence(occ: dict, canonical: dict, allowed_values: set[str]) -> str:
    value = occ["value"]
    context = occ["context_snippet"].lower()
    if "cam-" in context or "http" in context:
        return "metadata_reference"
    if canonical:
        canonical_src = canonical.get("canonical_source_instrument", "")
        in_source = canonical_src and canonical_src in occ["source_file"]
        value_allowed = (not allowed_values) or value in allowed_values
        if value_allowed and in_source:
            return "canonical_definition"
        if not value_allowed:
            if any(h in context for h in REDEFINITION_HINTS) or any(k in context for k in SCALE_KEYWORDS):
                return "noncanonical_value"
            return "unknown"
        if any(h in context for h in REDEFINITION_HINTS):
            return "possible_redefinition"
        if not any(k in context for k in SCALE_KEYWORDS):
            return "unrelated_use"
        return "reference"
    return "unknown"


def parse_file(path: Path, registry: dict) -> tuple[list[dict], list[dict]]:
    canonical_by_prefix, allowed_by_prefix = canonical_maps(registry)
    rel = normalize_path(path)
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    structures, occurrences = [], []
    heading_stack: list[str] = []
    i = 0

    def nearest_heading() -> str:
        return next((h for h in reversed(heading_stack) if h), "")

    while i < len(lines):
        line = lines[i]
        hm = HEADING_RE.match(line)
        if hm:
            level = len(hm.group(1))
            heading = normalize_space(hm.group(2))
            heading_stack = heading_stack[: level - 1]
            if len(heading_stack) < level - 1:
                heading_stack.extend([""] * (level - 1 - len(heading_stack)))
            heading_stack.append(heading)

            values = extract_values(heading)
            prefixes = sorted({extract_prefix(v) for v in values})
            has_heading_ctx = any(k in heading.lower() for k in SCALE_KEYWORDS)
            if has_heading_ctx or any(p in canonical_by_prefix for p in prefixes):
                structures.append({
                    "kind": "heading",
                    "source_file": rel,
                    "line_start": i + 1,
                    "heading": heading,
                    "nearest_heading": heading,
                    "detected_scale_values": values,
                    "detected_prefixes": prefixes,
                    "has_scale_like_heading": has_heading_ctx,
                    "has_scale_like_columns": False,
                    "has_repeated_numbered_sequence": len(values) >= 2,
                })
                for value in values:
                    prefix = extract_prefix(value)
                    can = canonical_by_prefix.get(prefix, {})
                    occ = {
                        "value": value,
                        "prefix": prefix,
                        "source_file": rel,
                        "line_number": i + 1,
                        "nearest_heading": heading,
                        "table_title": "",
                        "column_name": "",
                        "context_snippet": heading[:200],
                        "occurrence_type": "unknown",
                    }
                    occ["occurrence_type"] = classify_occurrence(occ, can, allowed_by_prefix.get(prefix, set()))
                    occurrences.append(occ)
            i += 1
            continue

        if line.strip().startswith("|") and i + 1 < len(lines) and is_table_separator(lines[i + 1]):
            start = i
            header = tokenize_row(lines[i])
            j = i + 2
            rows: list[tuple[int, list[str]]] = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append((j + 1, tokenize_row(lines[j])))
                j += 1

            head = nearest_heading()
            title = head
            for back in range(start - 1, -1, -1):
                cand = normalize_space(lines[back])
                if not cand or cand.startswith("|"):
                    continue
                title = normalize_space(cand.lstrip("#").strip("*_` "))
                break

            values = extract_values("\n".join([" | ".join(header)] + [" | ".join(r) for _, r in rows]))
            prefixes = sorted({extract_prefix(v) for v in values})
            has_cols = any(k in " | ".join(header).lower() for k in COLUMN_TERMS)
            has_head = any(k in f"{head} {title}".lower() for k in SCALE_KEYWORDS)
            structures.append({
                "kind": "table",
                "source_file": rel,
                "line_start": start + 1,
                "line_end": j,
                "table_title": title,
                "normalized_table_title": normalize_title(title),
                "nearest_heading": head,
                "columns": header,
                "row_count": len(rows),
                "detected_scale_values": values,
                "detected_prefixes": prefixes,
                "has_scale_like_heading": has_head,
                "has_scale_like_columns": has_cols,
                "has_repeated_numbered_sequence": len(values) >= 2,
            })

            for line_no, row in rows:
                for cidx, cell in enumerate(row):
                    if cell not in values:
                        continue
                    prefix = extract_prefix(cell)
                    can = canonical_by_prefix.get(prefix, {})
                    column_name = header[cidx] if cidx < len(header) else ""
                    snippet = " | ".join(row)[:200]
                    occ = {
                        "value": cell,
                        "prefix": prefix,
                        "source_file": rel,
                        "line_number": line_no,
                        "nearest_heading": head,
                        "table_title": title,
                        "column_name": column_name,
                        "context_snippet": snippet,
                        "occurrence_type": "unknown",
                    }
                    occ["occurrence_type"] = classify_occurrence(occ, can, allowed_by_prefix.get(prefix, set()))
                    occurrences.append(occ)
            i = j
            continue

        i += 1

    return structures, occurrences


def build_prefix_summary(structures: list[dict], occurrences: list[dict], registry: dict) -> tuple[list[dict], list[dict]]:
    canonical_by_prefix, allowed = canonical_maps(registry)
    protected = set(registry.get("protected_prefixes", {}).keys())
    by_prefix = defaultdict(list)
    for occ in occurrences:
        by_prefix[occ["prefix"]].append(occ)

    registered_rows, candidate_rows = [], []
    for prefix, items in sorted(by_prefix.items()):
        registered = prefix in canonical_by_prefix
        allowed_match = any(o["value"] in allowed.get(prefix, set()) for o in items)
        row = {
            "prefix": prefix,
            "occurrences": len(items),
            "confidence": "high" if registered and allowed_match else ("medium" if registered else "low"),
            "reason": "registered prefix with allowed values" if registered and allowed_match else ("registered prefix detected with partial value mismatch" if registered else "candidate structure with weak symbolic evidence"),
            "first_source_file": min(i["source_file"] for i in items),
            "protected": prefix in protected,
            "registered": registered,
            "registered_meaning": canonical_by_prefix.get(prefix, {}).get("canonical_name", ""),
            "expected_bucket": registry.get("protected_prefixes", {}).get(prefix, {}).get("expected_bucket", ""),
        }
        if registered:
            registered_rows.append(row)
        else:
            if row["occurrences"] >= 3:
                candidate_rows.append(row)
    return registered_rows, candidate_rows


def analyze_tables(structures: list[dict], registry: dict) -> tuple[list[dict], list[dict]]:
    allowlist = {normalize_for_compare(x) for x in registry.get("recurring_template_allowlist", [])}
    groups = defaultdict(list)
    for s in structures:
        if s.get("kind") == "table":
            groups[normalize_for_compare(s.get("normalized_table_title", ""))].append(s)

    recurring, dupes = [], []
    for norm, rows in sorted(groups.items()):
        if not norm:
            continue
        entry = {
            "normalized_title": rows[0].get("normalized_table_title", ""),
            "occurrences": len(rows),
            "confidence": "high" if any(r.get("detected_scale_values") for r in rows) else "low",
            "reason": "template table allowlisted" if norm in allowlist else "repeated non-template classification table",
            "examples": [{"source_file": r["source_file"], "line_start": r["line_start"], "canonical_url": BASE_CANONICAL_URL + r["source_file"]} for r in rows[:5]],
        }
        if norm in allowlist:
            recurring.append(entry)
        elif len(rows) > 1 and any(r.get("detected_scale_values") for r in rows):
            dupes.append(entry)
    recurring.sort(key=lambda x: (-x["occurrences"], x["normalized_title"].lower()))
    dupes.sort(key=lambda x: (-x["occurrences"], x["normalized_title"].lower()))
    return recurring, dupes


def build_noncanonical_and_collisions(occurrences: list[dict], registry: dict) -> tuple[list[dict], list[dict]]:
    canonical_by_prefix, allowed = canonical_maps(registry)
    protected = set(registry.get("protected_prefixes", {}).keys())

    grouped = defaultdict(list)
    for occ in occurrences:
        if occ["prefix"] not in canonical_by_prefix:
            continue
        reason = None
        severity = "warning"
        if occ["occurrence_type"] == "noncanonical_value":
            reason = "registered prefix used with non-canonical value"
            severity = "error" if occ["prefix"] in protected else "warning"
        elif occ["occurrence_type"] == "possible_redefinition":
            reason = "registered value appears as possible_redefinition"
        if reason is None:
            continue
        key = (occ["value"], occ["prefix"], occ["source_file"], occ["nearest_heading"], reason)
        grouped[key].append((severity, occ))

    noncanonical_rows, collision_rows = [], []
    for key, items in sorted(grouped.items()):
        sev = "error" if any(s == "error" for s, _ in items) else "warning"
        _, occ = items[0]
        row = {
            "value": occ["value"],
            "prefix": occ["prefix"],
            "severity": sev,
            "confidence": "high" if sev == "error" else "medium",
            "reason": key[4],
            "source_file": occ["source_file"],
            "line_number": occ["line_number"],
            "nearest_heading": occ["nearest_heading"],
            "context_snippet": occ["context_snippet"],
            "labels": [],
            "occurrences": len(items),
        }
        if occ["occurrence_type"] == "noncanonical_value":
            noncanonical_rows.append(row)
        collision_rows.append(row)

    return noncanonical_rows, collision_rows


def render_report(payload: dict) -> str:
    lines = [
        "# CAM Governance Symbolic Structures (Human Readable Index)",
        "",
        "## Corpus Summary",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Files scanned | {payload['files_scanned']} |",
        f"| Structures indexed | {payload['count']} |",
        f"| Canonical registered structures | {len(payload['canonical_registered_symbolic_structures'])} |",
        f"| Candidate prefixes | {len(payload['candidate_unregistered_prefixes'])} |",
        f"| Recurring template tables | {len(payload['recurring_governance_template_tables'])} |",
        f"| Potential duplicate symbolic structures | {len(payload['potential_duplicate_symbolic_structures'])} |",
        f"| Noncanonical registered prefix values | {len(payload['noncanonical_registered_prefix_values'])} |",
        f"| Possible collisions requiring review | {len(payload['possible_collisions_requiring_review'])} |",
        "",
        "## Canonical Registered Symbolic Structures",
        "",
        "| Code / Prefix | Canonical Name | Canonical Codes | Source Instrument | Protection Level | Status | Related Prefixes | Notes |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in payload["canonical_registered_symbolic_structures"]:
        lines.append(f"| {r.get('prefix','')} | {r.get('canonical_name','')} | {', '.join(r.get('canonical_codes', r.get('values',[])))} | {r.get('canonical_source_instrument','')} | {r.get('protection_level','')} | {r.get('status','')} | {', '.join(r.get('related_prefixes',[]))} | {r.get('notes','')} |")

    lines += ["", "## Candidate Unregistered Prefixes", "", "| Prefix | Occurrences | Confidence | Reason | First Source |", "|---|---:|---|---|---|"]
    for r in payload["candidate_unregistered_prefixes"]:
        lines.append(f"| {r['prefix']} | {r['occurrences']} | {r['confidence']} | {r['reason']} | {r['first_source_file']} |")

    lines += ["", "## Recurring Governance Template Tables", "", "| Normalized Title | Occurrences | Confidence | Reason | Example Canonical Instrument URL |", "|---|---:|---|---|---|"]
    for r in payload["recurring_governance_template_tables"]:
        ex = r["examples"][0] if r["examples"] else {"source_file": "", "canonical_url": ""}
        lines.append(f"| {r['normalized_title']} | {r['occurrences']} | {r['confidence']} | {r['reason']} | [{ex['source_file']}]({ex['canonical_url']}) |")

    lines += ["", "## Potential Duplicate Symbolic Structures", "", "| Normalized Title | Occurrences | Confidence | Reason | Example Canonical Instrument URL |", "|---|---:|---|---|---|"]
    for r in payload["potential_duplicate_symbolic_structures"]:
        ex = r["examples"][0] if r["examples"] else {"source_file": "", "canonical_url": ""}
        lines.append(f"| {r['normalized_title']} | {r['occurrences']} | {r['confidence']} | {r['reason']} | [{ex['source_file']}]({ex['canonical_url']}) |")

    lines += ["", "## Noncanonical Registered Prefix Values", "", "| Value | Prefix | Severity | Reason | Source File | Line | Nearest Heading | Context | Occurrences |", "|---|---|---|---|---|---:|---|---|---:|"]
    for r in payload["noncanonical_registered_prefix_values"]:
        lines.append(f"| {r['value']} | {r['prefix']} | {r['severity']} | {r['reason']} | {r['source_file']} | {r['line_number']} | {r['nearest_heading']} | {r['context_snippet']} | {r['occurrences']} |")
        lines.append(f"|  |  |  |  |  |  |  | `rg -n --glob 'Governance/**/*.md' '{r['value']}'` |  |")

    lines += ["", "## Possible Collisions Requiring Review", "", "| Scale Value | Prefix | Severity | Confidence | Reason | Source File | Line | Nearest Heading | Context | Labels | Occurrences |", "|---|---|---|---|---|---|---:|---|---|---|---:|"]
    for r in payload["possible_collisions_requiring_review"]:
        lines.append(f"| {r['value']} | {r['prefix']} | {r['severity']} | {r['confidence']} | {r['reason']} | {r['source_file']} | {r['line_number']} | {r['nearest_heading']} | {r['context_snippet']} | {', '.join(r.get('labels',[]))} | {r['occurrences']} |")

    return "\n".join(lines).rstrip() + "\n"


def build_index() -> dict:
    registry = load_registry()
    files = sorted([p for p in GOVERNANCE_ROOT.rglob("*.md") if p.name not in {"CAM.Governance.Index.md", "CAM.Governance.Symbolic-Structures.Index.md"} and not p.name.endswith("-Index.md")], key=normalize_path)

    structures, occurrences = [], []
    for p in files:
        s, o = parse_file(p, registry)
        structures.extend(s)
        occurrences.extend(o)

    structures.sort(key=lambda s: (s.get("source_file", ""), s.get("line_start", 0), s.get("kind", "")))
    occurrences.sort(key=lambda o: (o["source_file"], o["line_number"], o["value"], o["occurrence_type"]))

    registered_usage, candidates = build_prefix_summary(structures, occurrences, registry)
    recurring, dupes = analyze_tables(structures, registry)
    noncanonical, collisions = build_noncanonical_and_collisions(occurrences, registry)

    payload = {
        "schema_version": "4.0",
        "root": "Governance",
        "count": len(structures),
        "files_scanned": len(files),
        "detected_prefixes": sorted({o["prefix"] for o in occurrences}),
        "detected_scale_values": sorted({o["value"] for o in occurrences}),
        "canonical_registered_symbolic_structures": registry.get("canonical_registered_structures", []),
        "protected_scale_usage": registered_usage,
        "candidate_unregistered_prefixes": candidates,
        "recurring_governance_template_tables": recurring,
        "potential_duplicate_symbolic_structures": dupes,
        "noncanonical_registered_prefix_values": noncanonical,
        "possible_collisions_requiring_review": collisions,
        "value_occurrences": occurrences,
        "structures": structures,
    }
    return payload


def main() -> None:
    payload = build_index()
    INDICES_ROOT.mkdir(parents=True, exist_ok=True)
    INDEX_JSON_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    INDEX_MD_PATH.write_text(render_report(payload), encoding="utf-8")
    print(f"Wrote: {INDEX_JSON_PATH.relative_to(REPO_ROOT).as_posix()}")
    print(f"Wrote: {INDEX_MD_PATH.relative_to(REPO_ROOT).as_posix()}")
    print(f"Structures indexed: {payload['count']}")


if __name__ == "__main__":
    main()
