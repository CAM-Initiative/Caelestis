#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess
import tempfile

REPO_ROOT = Path(__file__).resolve().parents[2]
OLD_REF = "origin/policy/civilisational-wealth-governance"
FIXED_TIMESTAMP = "2026-07-28T09:35:31Z"
INCORRECT_TIMESTAMP = "2026-07-26T00:00:00Z"
TOKEN = "<!-- CAM_AMENDMENT_LEDGER_RECONCILIATION_TOKEN -->"
DIAGNOSTIC = REPO_ROOT / ".github" / "Indices" / "source-reconciliation-diagnostic.txt"
EXCLUDED = {
    "Governance/Constitution/CAM-BS2025-AEON-003-SCH-01.md",
    "Governance/Constitution/CAM-BS2025-AEON-003-SCH-03.md",
    "Governance/Charters/CAM-EQ2026-OPERATIONS-008-PLATINUM.md",
}

HEADING_RE = re.compile(r"^##+\s+.*amendment\s+ledger", re.IGNORECASE | re.MULTILINE)
NEXT_HEADING_RE = re.compile(r"^##+\s+", re.MULTILINE)
VERSION_RE = re.compile(r"^\d+(?:\.\d+)+$")


def run(args, *, check=True):
    proc = subprocess.run(args, cwd=REPO_ROOT, text=True, capture_output=True)
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "Command failed: " + " ".join(args))
    return proc


def git_text(ref, path):
    proc = run(["git", "show", f"{ref}:{path}"], check=False)
    return proc.stdout if proc.returncode == 0 else None


def split_ledger(text):
    if text is None:
        return None, None, None
    match = HEADING_RE.search(text)
    if not match:
        return text, None, ""
    tail = text[match.end():]
    nxt = NEXT_HEADING_RE.search(tail)
    end = match.end() + nxt.start() if nxt else len(text)
    return text[:match.start()], text[match.start():end], text[end:]


def body_with_token(text):
    prefix, ledger, suffix = split_ledger(text)
    if ledger is None:
        return text, None
    return prefix + TOKEN + suffix, ledger


def row_cells(line):
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None
    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    if not cells or not VERSION_RE.match(cells[0]):
        return None
    while len(cells) < 4:
        cells.append("")
    return cells[:4]


def parse_rows(ledger):
    rows = []
    if ledger is None:
        return rows
    for idx, line in enumerate(ledger.splitlines(keepends=True)):
        cells = row_cells(line)
        if cells:
            rows.append({
                "index": idx,
                "version": cells[0],
                "description": cells[1],
                "timestamp": cells[2],
                "hash": cells[3],
            })
    return rows


def semver(value):
    return tuple(int(part) for part in value.split("."))


def next_minor(versions):
    parsed = [semver(value) for value in versions if VERSION_RE.match(value)]
    top = max(parsed)
    if len(top) == 2:
        return f"{top[0]}.{top[1] + 1}"
    return ".".join(str(part) for part in (*top[:-1], top[-1] + 1))


def canonical_row(version, description, timestamp, hash_value):
    return f"| {version} | {description} | {timestamp} | {hash_value} |\n"


def timestamp_key(value):
    return value or "9999"


def rebuild_sorted_rows(lines, additions):
    current = parse_rows("".join(lines))
    if not current and not additions:
        return lines
    start = min(row["index"] for row in current)
    end = max(row["index"] for row in current)
    combined = [
        {
            "version": row["version"],
            "description": row["description"],
            "timestamp": row["timestamp"],
            "hash": row["hash"],
        }
        for row in current
    ] + additions
    combined.sort(key=lambda row: (semver(row["version"]), timestamp_key(row["timestamp"]), row["description"]))
    lines[start:end + 1] = [
        canonical_row(row["version"], row["description"], row["timestamp"], row["hash"])
        for row in combined
    ]
    return lines


def merge_ledger(path, current_ledger, old_ledger):
    if current_ledger is None and old_ledger is None:
        return None
    if current_ledger is None:
        current_ledger = old_ledger

    lines = current_ledger.splitlines(keepends=True)
    rows = parse_rows(current_ledger)
    corrected_descriptions = set()

    # Correct placeholder-dated entries already present in the target ledger.
    version_descriptions = {}
    for row in rows:
        version_descriptions.setdefault(row["version"], set()).add(row["description"])
    for row in rows:
        if row["timestamp"] != INCORRECT_TIMESTAMP:
            continue
        if len(version_descriptions.get(row["version"], set())) > 1:
            if path != "Governance/Charters/CAM-EQ2026-OPERATIONS-007-PLATINUM.md":
                raise RuntimeError(f"Unresolved duplicate amendment version in {path}: {row['version']}")
            row["version"] = next_minor([candidate["version"] for candidate in rows])
        row["timestamp"] = FIXED_TIMESTAMP
        row["hash"] = ""
        corrected_descriptions.add(row["description"])
        lines[row["index"]] = canonical_row(row["version"], row["description"], row["timestamp"], row["hash"])

    additions = []
    for old_row in parse_rows(old_ledger):
        rows = parse_rows("".join(lines))
        is_red_team = old_row["timestamp"] == INCORRECT_TIMESTAMP

        if is_red_team:
            same_description = [row for row in rows if row["description"] == old_row["description"]]
            if len(same_description) == 1:
                target = same_description[0]
                lines[target["index"]] = canonical_row(
                    target["version"], target["description"], FIXED_TIMESTAMP, ""
                )
                corrected_descriptions.add(target["description"])
                continue
            if len(same_description) > 1:
                raise RuntimeError(f"Duplicate amendment descriptions in {path}: {old_row['description']}")

        rows = parse_rows("".join(lines))
        exact = [
            row for row in rows
            if row["version"] == old_row["version"] and row["description"] == old_row["description"]
        ]
        if exact:
            continue

        version = old_row["version"]
        description = old_row["description"]
        timestamp = FIXED_TIMESTAMP if is_red_team else old_row["timestamp"]
        hash_value = "" if is_red_team else old_row["hash"]
        collision = [row for row in rows if row["version"] == version and row["description"] != description]

        if collision:
            if len(collision) != 1:
                raise RuntimeError(f"Multiple amendment version collisions in {path}: {version}")
            target = collision[0]
            target_is_latest = target["index"] == max(row["index"] for row in rows)
            if timestamp_key(timestamp) < timestamp_key(target["timestamp"]):
                if not target_is_latest:
                    raise RuntimeError(f"Cannot renumber a non-latest collided entry in {path}: {version}")
                new_version = next_minor(
                    [row["version"] for row in rows] + [item["version"] for item in additions]
                )
                lines[target["index"]] = canonical_row(
                    new_version, target["description"], target["timestamp"], ""
                )
            else:
                version = next_minor(
                    [row["version"] for row in rows] + [item["version"] for item in additions]
                )

        additions.append({
            "version": version,
            "description": description,
            "timestamp": timestamp,
            "hash": hash_value,
        })
        if is_red_team:
            corrected_descriptions.add(description)

    lines = rebuild_sorted_rows(lines, additions)
    merged = "".join(lines)
    final_rows = parse_rows(merged)

    if corrected_descriptions:
        latest_description = final_rows[-1]["description"] if final_rows else None
        for description in corrected_descriptions:
            if description != latest_description:
                raise RuntimeError(
                    f"Corrected red-team entry is not the latest ledger row in {path}: {description}"
                )
    return merged


def reconcile():
    if DIAGNOSTIC.exists():
        DIAGNOSTIC.unlink()
    run(["git", "fetch", "origin", "main", "policy/civilisational-wealth-governance"])
    base_ref = run(["git", "merge-base", "HEAD", OLD_REF]).stdout.strip()
    diff = run([
        "git", "diff", "--name-only", "--diff-filter=ACMR", f"{base_ref}..{OLD_REF}", "--",
        ":(glob)Governance/Charters/*.md", ":(glob)Governance/Constitution/*.md",
    ]).stdout.splitlines()

    candidates = []
    skipped = []
    for path in sorted(set(line.strip() for line in diff if line.strip())):
        if path in EXCLUDED or path.endswith("Index.md"):
            skipped.append(path)
            continue
        old_text = git_text(OLD_REF, path)
        if old_text is None:
            continue
        base_text = git_text(base_ref, path)
        _bp, base_ledger, _bs = split_ledger(base_text)
        _op, old_ledger, _os = split_ledger(old_text)
        current_exists = (REPO_ROOT / path).exists()
        if base_text is not None and old_ledger == base_ledger:
            continue
        if not current_exists and base_text is None:
            candidates.append(path)
        elif old_ledger is not None:
            candidates.append(path)

    conflicts = []
    changed = []
    for path in candidates:
        old_text = git_text(OLD_REF, path)
        base_text = git_text(base_ref, path)
        target_path = REPO_ROOT / path
        current_text = target_path.read_text(encoding="utf-8") if target_path.exists() else None

        if current_text is None:
            merged_body, _ = body_with_token(old_text)
            _op, old_ledger, _os = split_ledger(old_text)
            merged_ledger = merge_ledger(path, old_ledger, old_ledger)
        else:
            current_body, current_ledger = body_with_token(current_text)
            old_body, old_ledger = body_with_token(old_text)
            if base_text is None:
                if current_body == old_body:
                    merged_body = current_body
                else:
                    conflicts.append(f"{path}: independently added on both branches")
                    continue
            else:
                base_body, _base_ledger = body_with_token(base_text)
                with tempfile.TemporaryDirectory() as tmpdir:
                    cur = Path(tmpdir) / "current"
                    base = Path(tmpdir) / "base"
                    old = Path(tmpdir) / "old"
                    cur.write_text(current_body, encoding="utf-8")
                    base.write_text(base_body, encoding="utf-8")
                    old.write_text(old_body, encoding="utf-8")
                    proc = run(["git", "merge-file", "-p", str(cur), str(base), str(old)], check=False)
                    if proc.returncode != 0:
                        conflicts.append(f"{path}: three-way source conflict")
                        continue
                    merged_body = proc.stdout
            merged_ledger = merge_ledger(path, current_ledger, old_ledger)

        if merged_ledger is not None:
            if merged_body.count(TOKEN) != 1:
                conflicts.append(f"{path}: amendment ledger token count was {merged_body.count(TOKEN)}")
                continue
            merged_text = merged_body.replace(TOKEN, merged_ledger)
        else:
            merged_text = merged_body

        if current_text != merged_text:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(merged_text, encoding="utf-8")
            changed.append(path)

    print("SOURCE_RECONCILIATION_CANDIDATES_BEGIN")
    for path in candidates:
        print(path)
    print("SOURCE_RECONCILIATION_CANDIDATES_END")
    print("SOURCE_RECONCILIATION_CHANGED_BEGIN")
    for path in changed:
        print(path)
    print("SOURCE_RECONCILIATION_CHANGED_END")
    print("SOURCE_RECONCILIATION_SKIPPED_BEGIN")
    for path in skipped:
        print(path)
    print("SOURCE_RECONCILIATION_SKIPPED_END")

    if conflicts:
        print("SOURCE_RECONCILIATION_CONFLICTS_BEGIN")
        for conflict in conflicts:
            print(conflict)
        print("SOURCE_RECONCILIATION_CONFLICTS_END")
        raise SystemExit(1)

    if changed:
        run(["git", "add", *changed])
        run([
            "python", ".github/scripts/lint_amendment_ledger.py",
            "--staged", "--fix", "--stage", "fix",
        ])
        run([
            "python", ".github/scripts/lint_amendment_ledger.py",
            "--staged", "--strict", "--stage", "post_fix",
        ])
        run(["git", "reset"])

    remaining = run([
        "grep", "-R", "--line-number", "--fixed-strings", INCORRECT_TIMESTAMP,
        "Governance/Charters", "Governance/Constitution",
    ], check=False)
    if remaining.returncode == 0:
        print(remaining.stdout)
        raise RuntimeError("Incorrect 2026-07-26 placeholder timestamp remains in source doctrine")


if __name__ == "__main__":
    reconcile()
