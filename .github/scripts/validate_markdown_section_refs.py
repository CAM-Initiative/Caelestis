#!/usr/bin/env python3
import argparse
import difflib
import pathlib
import re
import sys
from dataclasses import dataclass

HEADING_NUMBER_RE = re.compile(r"^(?:#+\s+)?(?P<section>\d+(?:\.\d+)*)\b")
SECTION_REF_RE = re.compile(r"§(?P<section>\d+(?:\.\d+)*)")
INSTRUMENT_NEARBY_RE = re.compile(
    r"\b(?:CAM-[A-Z]{2}\d{4}-[A-Z]+-\d{3}(?:-[A-Z0-9]+-\d{2,3}|-[A-Z]+)?|"
    r"AEON-\d{3}(?:-SCH-\d{2})?|"
    r"LAW-\d{3}|"
    r"SCH-\d{2}|"
    r"Constitution|Charter|Law|Annex)\b",
    re.IGNORECASE,
)


@dataclass
class Finding:
    file_path: str
    line_number: int
    reference: str
    status: str
    target_exists: str
    closest_section: str


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
    return sections


def closest_section(target: str, section_map: set[str]) -> str:
    if not section_map:
        return ""
    close = difflib.get_close_matches(target, sorted(section_map), n=1, cutoff=0.0)
    return close[0] if close else ""


def scan_file(path: pathlib.Path) -> list[Finding]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    sections = extract_sections(lines)
    findings: list[Finding] = []

    for idx, line in enumerate(lines, start=1):
        for match in SECTION_REF_RE.finditer(line):
            ref = match.group("section")
            ref_token = f"§{ref}"

            left = max(0, match.start() - 80)
            right = min(len(line), match.end() + 80)
            context = line[left:right]

            if INSTRUMENT_NEARBY_RE.search(context):
                findings.append(
                    Finding(
                        file_path=str(path),
                        line_number=idx,
                        reference=ref_token,
                        status="manual review required",
                        target_exists="n/a",
                        closest_section="",
                    )
                )
                continue

            exists = ref in sections
            findings.append(
                Finding(
                    file_path=str(path),
                    line_number=idx,
                    reference=ref_token,
                    status="pass" if exists else "fail",
                    target_exists="yes" if exists else "no",
                    closest_section="" if exists else closest_section(ref, sections),
                )
            )

    return findings


def run(root: pathlib.Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in sorted(root.glob("**/*.md")):
        findings.extend(scan_file(path))
    return findings


def print_report(findings: list[Finding]) -> None:
    print("file path\tline number\treference found\ttarget exists\tclosest matching section\tstatus")
    for f in findings:
        print(
            f"{f.file_path}\t{f.line_number}\t{f.reference}\t{f.target_exists}\t{f.closest_section}\t{f.status}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate intra-document Markdown section references (e.g., §1.2.3)."
    )
    parser.add_argument(
        "--root",
        default="Governance",
        help="Root directory containing Markdown files (default: Governance)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Reserved for explicit fixes; this validator does not rewrite files.",
    )
    args = parser.parse_args()

    if args.fix:
        print("--fix specified: no automatic rewrites are implemented by this validator.")

    root = pathlib.Path(args.root)
    findings = run(root)
    print_report(findings)

    unresolved = [f for f in findings if f.status == "fail"]
    print(f"TOTAL_REFERENCES={len(findings)}")
    print(f"UNRESOLVED_INTRA_DOC_REFERENCES={len(unresolved)}")

    return 1 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main())
