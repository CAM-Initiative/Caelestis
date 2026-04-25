#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

import argparse
import pathlib
import re

PATTERNS = {
    'annex_shorthand': re.compile(r'\bAnnex\s+[A-Z]\b'),
    'sch_shorthand': re.compile(r'\bSCH-[0-9]{2}\b'),
    'domain_short_id': re.compile(r'\b(ARBITRATION|RELATION|ETHICS|OPERATIONS|IDENTITY|STEWARD|SECURITY|LATTICE|ECONOMICS)-[0-9]{3}\b'),
    'aeon_short_schedule': re.compile(r'\bAEON-[0-9]{3}-SCH-[0-9]{2}\b'),
    'normative_lowercase': re.compile(r'\b(must not|must|shall|should)\b'),
}

ALLOWLIST = re.compile(r'CAM-[A-Z]{2}[0-9]{4}-[A-Z]+-[0-9]{3}(?:-[A-Z0-9]+-[0-9]{2,3}|-[A-Z]+)?')


NORMATIVE_FIX_PATTERNS = [
    (re.compile(r'\bmust not\b'), 'MUST NOT'),
    (re.compile(r'\bmust\b'), 'MUST'),
    (re.compile(r'\bshall\b'), 'SHALL'),
    (re.compile(r'\bshould\b'), 'SHOULD'),
]


def lint(root: pathlib.Path) -> list[tuple[str, int, str, str]]:
    findings = []
    for path in sorted(root.rglob('*.md')):
        text = path.read_text(encoding='utf-8', errors='ignore').splitlines()
        for ln, line in enumerate(text, 1):
            if ALLOWLIST.search(line):
                # still check for additional shorthand fragments in same line
                pass
            for name, pat in PATTERNS.items():
                for m in pat.finditer(line):
                    findings.append((str(path), ln, name, m.group(0)))
    return findings


def apply_normative_case_fix(root: pathlib.Path) -> list[str]:
    changed: list[str] = []
    for path in sorted(root.rglob('*.md')):
        original = path.read_text(encoding='utf-8', errors='ignore')
        updated = original
        for pat, repl in NORMATIVE_FIX_PATTERNS:
            updated = pat.sub(repl, updated)
        if updated != original:
            path.write_text(updated, encoding='utf-8')
            changed.append(str(path))
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description='Lint governance docs for shorthand reference constructs.')
    parser.add_argument('--root', default='Governance', help='Root path to lint')
    parser.add_argument('--output', default='', help='Optional output file path')
    parser.add_argument('--fix-normative-case', action='store_true', help='Auto-capitalize lowercase normative terms (must/shall/should/must not).')
    args = parser.parse_args()

    root = pathlib.Path(args.root)
    changed: list[str] = []
    if args.fix_normative_case:
        changed = apply_normative_case_fix(root)

    findings = lint(root)
    lines = [f"{p}:{ln}:{kind}:{tok}" for p, ln, kind, tok in findings]

    if args.output:
        out = pathlib.Path(args.output)
        out.write_text('\n'.join(lines) + ('\n' if lines else ''), encoding='utf-8')

    for line in lines[:5000]:
        print(line)

    if changed:
        print(f"NORMATIVE_CASE_FILES_UPDATED={len(changed)}")

    print(f"TOTAL_FINDINGS={len(findings)}")
    return 1 if findings else 0


if __name__ == '__main__':
    raise SystemExit(main())
