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
CROSS_DOC_ADJ_RE = re.compile(r"^\s+(?P<doc_id>CAM-[A-Z0-9]+(?:-[A-Z0-9]+)+)")
CROSS_DOC_NEAR_RE = re.compile(r"\b(?P<doc_id>CAM-[A-Z0-9]+(?:-[A-Z0-9]+)+)\b")
INSTRUMENT_NEARBY_RE = re.compile(r"\b(?:AEON-\d{3}(?:-SCH-\d{2})?|LAW-\d{3}|SCH-\d{2}|Constitution|Charter|Law|Annex)\b", re.IGNORECASE)


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


def classify_reference(line: str, match: re.Match) -> tuple[str, str]:
    tail = line[match.end():]
    m = CROSS_DOC_ADJ_RE.match(tail)
    if m:
        return "cross_document", m.group("doc_id")
    near = line[match.end(): match.end()+80]
    m2 = CROSS_DOC_NEAR_RE.search(near)
    if m2 and m2.start() < 20:
        return "cross_document", m2.group("doc_id")
    if INSTRUMENT_NEARBY_RE.search(near):
        return "manual_review", ""
    return "local", ""


def scan_file(path: pathlib.Path, doc_idx: dict[str, pathlib.Path], sections_cache: dict[pathlib.Path, set[str]]) -> list[Finding]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    sections = sections_cache.setdefault(path, extract_sections(lines))
    findings: list[Finding] = []

    for idx, line in enumerate(lines, start=1):
        for match in SECTION_REF_RE.finditer(line):
            ref = match.group("section")
            ref_token = f"§{ref}"
            ref_class, doc_id = classify_reference(line, match)

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
                findings.append(Finding(str(path), idx, ref_token, ref_class, doc_id, "yes", "yes" if exists else "no", "" if exists else closest_section(ref, target_sections), "pass_cross_document" if exists else "fail_cross_document_section_missing"))
                continue

            if ref_class == "manual_review":
                findings.append(Finding(str(path), idx, ref_token, ref_class, "", "n/a", "n/a", "", "manual_review_required"))
                continue

            exists = ref in sections
            findings.append(Finding(str(path), idx, ref_token, "local", path.stem, "yes", "yes" if exists else "no", "" if exists else closest_section(ref, sections), "pass_local" if exists else "fail_local"))

    return findings


def run(root: pathlib.Path) -> list[Finding]:
    findings: list[Finding] = []
    doc_idx = build_doc_index(root)
    sections_cache: dict[pathlib.Path, set[str]] = {}
    for path in sorted(root.glob("**/*.md")):
        findings.extend(scan_file(path, doc_idx, sections_cache))
    return findings


def print_report(findings: list[Finding]) -> None:
    print("file path\tline number\treference found\treference class\ttarget document\ttarget exists\ttarget section exists\tclosest matching section\tstatus")
    for f in findings:
        print(f"{f.file_path}\t{f.line_number}\t{f.reference}\t{f.reference_class}\t{f.target_document}\t{f.target_exists}\t{f.target_section_exists}\t{f.closest_section}\t{f.status}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate local and cross-document Markdown section references.")
    parser.add_argument("--root", default="Governance")
    parser.add_argument("--fix", action="store_true", help="No-op: validator does not rewrite files.")
    args = parser.parse_args()

    if args.fix:
        print("--fix specified: no automatic rewrites are implemented by this validator.")

    findings = run(pathlib.Path(args.root))
    print_report(findings)
    statuses = {}
    for f in findings:
        statuses[f.status] = statuses.get(f.status, 0) + 1
    for k in sorted(statuses):
        print(f"STATUS_{k.upper()}={statuses[k]}")
    unresolved = [f for f in findings if f.status in {"fail_local", "fail_cross_document_target_missing", "fail_cross_document_section_missing"}]
    print(f"TOTAL_REFERENCES={len(findings)}")
    print(f"UNRESOLVED_REFERENCES={len(unresolved)}")
    return 1 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main())
