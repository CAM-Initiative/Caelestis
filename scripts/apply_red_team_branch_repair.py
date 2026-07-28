from __future__ import annotations

import re
import subprocess
from pathlib import Path

POLICY_REF = "origin/policy/civilisational-wealth-governance"

TARGETS = [
    (
        "Governance/Constitution/CAM-BS2025-AEON-006-PLATINUM.md",
        "## 3.13 Prohibition on Operationalising Unscrupulous Conduct",
        None,
    ),
    (
        "Governance/Charters/CAM-EQ2026-ETHICS-003-PLATINUM.md",
        "## 1.5.1 Defensive-Purpose Non-Transferability",
        None,
    ),
    (
        "Governance/Charters/CAM-EQ2026-SECURITY-001-PLATINUM.md",
        "### 4.8.1 Internally Cultivated Adversarial Capability",
        None,
    ),
    (
        "Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md",
        "### 2.2.14 Adversarial Evaluation Capability Lineage Boundary",
        None,
    ),
    (
        "Governance/Constitution/CAM-BS2026-AEON-012-PLATINUM.md",
        "### 2.4.4 Adversarial Evaluation Boundary Signals",
        None,
    ),
    (
        "Governance/Charters/CAM-EQ2026-STEWARD-003-PLATINUM.md",
        "## 12.1 Adversarial Capability Programme Neutrality & Dual-Use Firebreak",
        None,
    ),
    (
        "Governance/Charters/CAM-EQ2026-OPERATIONS-008-PLATINUM.md",
        "# CAM-EQ2026-OPERATIONS-008-PLATINUM — Appendix G: Adversarial Evaluation & Red-Team Governance",
        "Adversarial Evaluation & Red-Team Governance Charter",
    ),
    (
        "Governance/Constitution/CAM-BS2025-AEON-003-SCH-02.md",
        "### 13.12 Adversarial Evaluation Execution-Boundary Gate",
        None,
    ),
    (
        "Governance/Constitution/CAM-BS2025-AEON-001-SCH-01.md",
        "### 3.2.3 Adversarial Evaluation Pause Signals",
        None,
    ),
]

HEADING_RE = re.compile(r"^(#{1,6})\s+.+$")


def git_show(path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"{POLICY_REF}:{path}"],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout


def heading_level(line: str) -> int:
    match = HEADING_RE.match(line)
    if not match:
        raise ValueError(f"Not a markdown heading: {line!r}")
    return len(match.group(1))


def section_bounds(lines: list[str], heading: str) -> tuple[int, int]:
    try:
        start = lines.index(heading)
    except ValueError as exc:
        raise RuntimeError(f"Source heading missing: {heading}") from exc
    level = heading_level(heading)
    end = len(lines)
    for index in range(start + 1, len(lines)):
        match = HEADING_RE.match(lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break
    return start, end


def find_insertion_index(source_lines: list[str], current_lines: list[str], start: int, end: int) -> int:
    source_level = heading_level(source_lines[start])

    # Prefer the first following peer-or-parent heading that still exists in current.
    for index in range(end, len(source_lines)):
        match = HEADING_RE.match(source_lines[index])
        if match and len(match.group(1)) <= source_level and source_lines[index] in current_lines:
            return current_lines.index(source_lines[index])

    # Otherwise insert after the nearest preceding peer-or-parent section present in current.
    for index in range(start - 1, -1, -1):
        match = HEADING_RE.match(source_lines[index])
        if not match or len(match.group(1)) > source_level:
            continue
        heading = source_lines[index]
        if heading not in current_lines:
            continue
        current_start = current_lines.index(heading)
        current_heading_level = len(match.group(1))
        current_end = len(current_lines)
        for cursor in range(current_start + 1, len(current_lines)):
            next_match = HEADING_RE.match(current_lines[cursor])
            if next_match and len(next_match.group(1)) <= current_heading_level:
                current_end = cursor
                break
        return current_end

    raise RuntimeError(f"No safe insertion anchor found for {source_lines[start]}")


def normalise_block(lines: list[str]) -> list[str]:
    block = list(lines)
    while block and block[0] == "":
        block.pop(0)
    while block and block[-1] == "":
        block.pop()
    return [""] + block + [""]


def apply_target(path: str, heading: str, alternate_presence: str | None) -> bool:
    destination = Path(path)
    current_text = destination.read_text(encoding="utf-8")
    if heading in current_text or (alternate_presence and alternate_presence in current_text):
        print(f"PRESENT: {path}: {heading}")
        return False

    source_text = git_show(path)
    source_lines = source_text.splitlines()
    current_lines = current_text.splitlines()
    start, end = section_bounds(source_lines, heading)
    insertion = find_insertion_index(source_lines, current_lines, start, end)
    block = normalise_block(source_lines[start:end])
    merged = current_lines[:insertion] + block + current_lines[insertion:]
    destination.write_text("\n".join(merged).rstrip() + "\n", encoding="utf-8")
    print(f"INSERTED: {path}: {heading}")
    return True


def main() -> None:
    changed = []
    for path, heading, alternate_presence in TARGETS:
        if apply_target(path, heading, alternate_presence):
            changed.append(path)

    print("Changed files:")
    for path in changed:
        print(f"- {path}")

    # Validate substantive presence without requiring stale ledger reconciliation.
    for path, heading, alternate_presence in TARGETS:
        text = Path(path).read_text(encoding="utf-8")
        if heading not in text and not (alternate_presence and alternate_presence in text):
            raise SystemExit(f"Missing required doctrine marker after repair: {path}: {heading}")


if __name__ == "__main__":
    main()
