#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p validation-reports

printf '\n== Canonical header validation ==\n'
python .github/scripts/validate_canonical_headers.py

printf '\n== Markdown section reference validation ==\n'
python .github/scripts/validate_markdown_section_refs.py \
  --root Governance \
  --report-file validation-reports/section-reference-report.tsv

printf '\n== Canonical code index consistency check ==\n'
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
python .github/scripts/build-canonical-code-index.py \
  --root Governance \
  --md-out "$TMP_DIR/canonical-code-index.md" \
  --json-out "$TMP_DIR/canonical-code-index.json" \
  --check
cmp -s "$TMP_DIR/canonical-code-index.md" Governance/canonical-code-index.md
cmp -s "$TMP_DIR/canonical-code-index.json" Governance/canonical-code-index.json

printf '\n== Symbolic/index validation ==\n'
python .github/scripts/lint-symbolic-structures.py \
  --index Governance/canonical-code-index.json

printf '\nGovernance checks completed. Section-reference report: validation-reports/section-reference-report.tsv\n'
