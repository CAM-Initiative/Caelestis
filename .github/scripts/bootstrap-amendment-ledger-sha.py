#!/usr/bin/env python3
import os
import sys
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import lint_amendment_ledger as ledger_lint


def main() -> int:
    updated: list[str] = []
    skipped: list[str] = []
    updated_rows = 0
    failures: list[str] = []

    for rel_path in ledger_lint.list_scoped_markdown_files():
        full_path = REPO_ROOT / rel_path
        text = full_path.read_text(encoding="utf-8")

        if not ledger_lint.has_amendment_ledger(text):
            skipped.append(f"{rel_path}: no amendment ledger")
            continue

        if ledger_lint.has_malformed_ledger_row(text):
            failures.append(f"{rel_path}: malformed amendment ledger row")
            continue

        row_info = ledger_lint.get_last_ledger_row_info(text)
        if not row_info:
            failures.append(f"{rel_path}: amendment ledger table missing parseable version rows")
            continue

        _, _, stored_hash = row_info
        if stored_hash != "":
            skipped.append(f"{rel_path}: latest-row SHA already populated")
            continue

        computed_hash, _ = ledger_lint.compute_hash_with_last_row_hash_blank(text)
        lines = text.splitlines(keepends=True)
        last_idx, last_line, _ = row_info
        lines[last_idx] = ledger_lint.replace_last_table_cell(last_line, computed_hash)
        updated_text = "".join(lines)
        if updated_text != text:
            full_path.write_text(updated_text, encoding="utf-8")
            updated.append(rel_path)
            updated_rows += 1

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1

    print(f"Updated rows: {updated_rows}")
    print(f"Files updated: {len(updated)}")
    if updated:
        print("Updated instruments:")
        for path in updated:
            print(f"- {path}")
    if skipped:
        print("Skipped:")
        for item in skipped:
            print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
