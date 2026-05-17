#!/usr/bin/env python3
"""Validate §-style section references in Governance markdown.

This validator does not assume every `§x` reference is local. It first classifies
reference scope (local, cross-document, etc.) because CAM instruments frequently
mix local, cross-document, annex/schedule, and constitutional references.
"""
import argparse
import difflib
import pathlib
import re
import sys
from dataclasses import dataclass

HEADING_NUMBER_RE = re.compile(r"^(?:#+\s+)?(?P<section>\d+(?:\.\d+)*)\b")
SECTION_REF_RE = re.compile(r"§(?P<section>\d+(?:\.\d+)*)")
DOC_ID_RE = r"CAM-[A-Z0-9]+(?:-[A-Z0-9]+)+"
DOC_ID_WITH_EXT_RE = rf"(?P<doc_id>{DOC_ID_RE})(?:\.md)?"
CROSS_DOC_AFTER_RE = re.compile(rf"^\s+{DOC_ID_WITH_EXT_RE}")
DOC_BEFORE_SECTION_RE = re.compile(rf"{DOC_ID_WITH_EXT_RE}\s*(?:,|:|—|–|-)?\s*$")
DOC_ID_COMPILED_RE = re.compile(DOC_ID_WITH_EXT_RE)
PHRASE_DOC_SECTION_RE = re.compile(rf"(?:as defined in|under|pursuant to)\s+{DOC_ID_WITH_EXT_RE}\s+§(?P<section>\d+(?:\.\d+)*)", re.IGNORECASE)
INSTRUMENT_NEARBY_RE = re.compile(r"\b(?:AEON-\d{3}(?:-SCH-\d{2})?|LAW-\d{3}|SCH-\d{2}|Constitution|Charter|Law|Annex|Appendix|Schedule|Part)\b", re.IGNORECASE)
NAMED_INSTRUMENT_REF_RE = re.compile(r"\b(?P<label>(?:Annex\s+[A-Z]|Appendix\s+[A-Z]|Schedule\s+\d+|Part\s+[IVX]+))\s+§(?P<section>\d+(?:\.\d+)*)", re.IGNORECASE)
AMENDMENT_REGISTER_HEADING_MARKERS = (
    "amendment register",
    "amendment history",
    "register of amendments",
    "change register",
    "revision history",
    "amendment log",
    "amendment ledger",
    "amendments",
)
BLOCKING_STATUSES = {
    "fail_local",
    "fail_cross_document_section_missing",
    "fail_cross_document_target_missing",
}
MANUAL_REVIEW_STATUSES = {
    "manual_review_required",
    "ambiguous_named_instrument_reference",
}
IGNORED_STATUSES = {
    "ignored_amendment_register_reference",
}


@dataclass
class Finding:
    file_path: str
    line_number: int
    reference: str
    reference_class: str
    target_document: str
    target_exists: str
    target_section_exists: str
    closest_section: str
    status: str


def normalize_sections(raw: set[str]) -> set[str]:
    out = set(raw)
    for s in list(raw):
        if "." in s:
            out.add(s.rstrip(".0"))
        else:
            out.add(f"{s}.0")
    return out


def extract_sections(lines: list[str]) -> set[str]:
    sections: set[str] = set()
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("#"):
            continue
        heading_text = stripped.lstrip("#").strip()
        match = HEADING_NUMBER_RE.match(heading_text)
        if match:
            sections.add(match.group("section"))
    return normalize_sections(sections)


def closest_section(target: str, section_map: set[str]) -> str:
    close = difflib.get_close_matches(target, sorted(section_map), n=1, cutoff=0.0)
    return close[0] if close else ""


def build_doc_index(root: pathlib.Path) -> dict[str, pathlib.Path]:
    idx = {}
    for p in sorted(root.glob("**/*.md")):
        stem = p.stem
        if stem.startswith("CAM-"):
            idx[stem] = p
    return idx


def is_inside_amendment_register(lines: list[str], line_index: int) -> bool:
    for i in range(line_index, -1, -1):
        heading = lines[i].strip()
        if heading.startswith("#"):
            heading_lower = heading.lower()
            return any(marker in heading_lower for marker in AMENDMENT_REGISTER_HEADING_MARKERS)
    return False


def build_amendment_register_mask(lines: list[str]) -> list[bool]:
    mask = [False] * len(lines)
    active = False
    active_heading_level = None
    for i, raw in enumerate(lines):
        line = raw.strip()
        heading_match = re.match(r"^(#+)\s+(.*)$", line)
        if heading_match:
            level = len(heading_match.group(1))
            heading_text = heading_match.group(2).lower()
            is_marker = any(marker in heading_text for marker in AMENDMENT_REGISTER_HEADING_MARKERS)
            if is_marker:
                active = True
                active_heading_level = level
            elif active and active_heading_level is not None and level <= active_heading_level:
                active = False
                active_heading_level = None
        elif any(marker in line.lower() for marker in AMENDMENT_REGISTER_HEADING_MARKERS):
            # Covers strong labels / block labels used before amendment tables.
            active = True
        mask[i] = active
    return mask


def classify_reference(line: str, match: re.Match) -> tuple[str, str, str]:
    # precedence A: doc id immediately before section (CAM-... §x)
    before = line[max(0, match.start()-120):match.start()]
    mb = DOC_BEFORE_SECTION_RE.search(before)
    if mb:
        return "cross_document", mb.group("doc_id"), ""

    # annex placeholders with explicit doc id become manual review (non-blocking)
    phrase = line[max(0, match.start()-220):match.end()+40]
    if re.search(rf"{DOC_ID_WITH_EXT_RE}\s*(?:,|:|—|–|-)?\s*Annex\s*\[[^\]]+\]\s*§{re.escape(match.group('section'))}", phrase, re.IGNORECASE):
        d = re.search(DOC_ID_WITH_EXT_RE, phrase)
        return "manual_review", d.group("doc_id") if d else "", "Annex [x]"

    # precedence A2: doc id before section with optional human-readable title
    # (CAM-... — Title §x), bounded to avoid over-binding.
    window_start = max(0, match.start() - 240)
    before_section = line[window_start:match.start()]
    # Choose the nearest CAM id before this section, with max same-line distance.
    doc_candidates = list(DOC_ID_COMPILED_RE.finditer(before_section))
    if doc_candidates:
        nearest = doc_candidates[-1]
        gap = before_section[nearest.end():]
        # Safe distance cap and same-line safeguard.
        if len(gap) <= 160 and "\n" not in gap:
            return "cross_document", nearest.group("doc_id"), ""

    # precedence B: section immediately before doc id (§x CAM-...)
    tail = line[match.end():]
    ma = CROSS_DOC_AFTER_RE.match(tail)
    if ma:
        return "cross_document", ma.group("doc_id"), ""

    # precedence C: explicit phrase forms near this match
    nearby = line[max(0, match.start()-80):match.end()+80]
    for pm in PHRASE_DOC_SECTION_RE.finditer(nearby):
        if pm.group("section") == match.group("section"):
            return "cross_document", pm.group("doc_id"), ""

    # avoid binding to later unrelated doc ids (e.g., subject to CAM-...)
    near = line[match.end(): match.end()+80]
    if INSTRUMENT_NEARBY_RE.search(near):
        return "manual_review", "", ""

    clause_start = max(line.rfind("(", 0, match.start()), line.rfind(";", 0, match.start()), line.rfind(".", 0, match.start()), line.rfind(":", 0, match.start()), line.rfind(",", 0, match.start()))
    clause_end_candidates = [x for x in [line.find(")", match.end()), line.find(";", match.end()), line.find(".", match.end())] if x != -1]
    clause_end = min(clause_end_candidates) if clause_end_candidates else len(line)
    clause = line[clause_start + 1:clause_end]
    named = NAMED_INSTRUMENT_REF_RE.search(clause)
    if named and named.group("section") == match.group("section") and not re.search(DOC_ID_RE, clause):
        return "manual_review", "", named.group("label")

    return "local", "", ""


def scan_file(path: pathlib.Path, doc_idx: dict[str, pathlib.Path], sections_cache: dict[pathlib.Path, set[str]]) -> list[Finding]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    amendment_mask = build_amendment_register_mask(lines)
    sections = sections_cache.setdefault(path, extract_sections(lines))
    findings: list[Finding] = []

    for idx, line in enumerate(lines, start=1):
        for match in SECTION_REF_RE.finditer(line):
            ref = match.group("section")
            ref_token = f"§{ref}"
            if amendment_mask[idx - 1]:
                findings.append(Finding(str(path), idx, ref_token, "ignored", path.stem, "n/a", "n/a", "", "ignored_amendment_register_reference"))
                continue
            ref_class, doc_id, named_label = classify_reference(line, match)

            if ref_class == "cross_document":
                target_path = doc_idx.get(doc_id)
                if not target_path:
                    findings.append(Finding(str(path), idx, ref_token, ref_class, doc_id, "no", "n/a", "", "fail_cross_document_target_missing"))
                    continue
                target_sections = sections_cache.get(target_path)
                if target_sections is None:
                    target_sections = extract_sections(target_path.read_text(encoding="utf-8", errors="ignore").splitlines())
                    sections_cache[target_path] = target_sections
                exists = ref in target_sections
                if exists:
                    status = "pass_cross_document"
                else:
                    status = "fail_cross_document_section_missing"
                findings.append(Finding(str(path), idx, ref_token, ref_class, doc_id, "yes", "yes" if exists else "no", "" if exists else closest_section(ref, target_sections), status))
                continue

            if ref_class == "manual_review":
                status = "ambiguous_named_instrument_reference" if named_label else "manual_review_required"
                target = f"{path.stem}:{named_label}" if named_label else ""
                findings.append(Finding(str(path), idx, ref_token, ref_class, target, "n/a", "n/a", "", status))
                continue

            exists = ref in sections
            if exists:
                status = "pass_local"
            else:
                status = "fail_local"
            findings.append(Finding(str(path), idx, ref_token, "local", path.stem, "yes", "yes" if exists else "no", "" if exists else closest_section(ref, sections), status))

    return findings


def run(root: pathlib.Path) -> list[Finding]:
    findings: list[Finding] = []
    doc_idx = build_doc_index(root)
    sections_cache: dict[pathlib.Path, set[str]] = {}
    for path in sorted(root.glob("**/*.md")):
        findings.extend(scan_file(path, doc_idx, sections_cache))
    return findings


def filter_display_findings(findings: list[Finding], show_passes: bool, show_ignored: bool=False) -> list[Finding]:
    out = findings
    if not show_passes:
        out = [f for f in out if not f.status.startswith("pass_")]
    if not show_ignored:
        out = [f for f in out if f.status not in IGNORED_STATUSES]
    return out


def print_report(findings: list[Finding]) -> None:
    print("file path\tline number\treference found\treference class\ttarget document\ttarget exists\ttarget section exists\tclosest matching section\tstatus")
    for f in findings:
        print(f"{f.file_path}\t{f.line_number}\t{f.reference}\t{f.reference_class}\t{f.target_document}\t{f.target_exists}\t{f.target_section_exists}\t{f.closest_section}\t{f.status}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate local and cross-document Markdown section references.")
    parser.add_argument("--root", default="Governance")
    parser.add_argument("--fix", action="store_true", help="No-op: validator does not rewrite files.")
    parser.add_argument("--show-passes", action="store_true", help="Include pass_* rows in the printed report output.")
    parser.add_argument("--show-ignored", action="store_true", help="Include ignored_amendment_register_reference rows in table output.")
    args = parser.parse_args()

    if args.fix:
        print("--fix specified: no automatic rewrites are implemented by this validator.")

    findings = run(pathlib.Path(args.root))
    display_findings = filter_display_findings(findings, show_passes=args.show_passes, show_ignored=args.show_ignored)
    print_report(display_findings)
    statuses = {}
    for f in findings:
        statuses[f.status] = statuses.get(f.status, 0) + 1
    for k in sorted(statuses):
        print(f"STATUS_{k.upper()}={statuses[k]}")
    unresolved = [f for f in findings if f.status in BLOCKING_STATUSES]
    passes = [f for f in findings if f.status.startswith("pass_")]
    manual = [f for f in findings if f.status in MANUAL_REVIEW_STATUSES]
    ignored = [f for f in findings if f.status in IGNORED_STATUSES]
    print(f"TOTAL_REFERENCES={len(findings)}")
    print(f"PASSED_REFERENCES={len(passes)}")
    print(f"HARD_FAILURE_REFERENCES={len(unresolved)}")
    print(f"MANUAL_REVIEW_REFERENCES={len(manual)}")
    print(f"IGNORED_REFERENCES={len(ignored)}")
    if not args.show_ignored and ignored:
        print(f"SUPPRESSED_IGNORED_ROWS={len(ignored)} (use --show-ignored to display)")
    return 1 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main())
