#!/usr/bin/env python3
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OLD_REF = "origin/policy/civilisational-wealth-governance"
REPORT = ROOT / ".github" / "Indices" / "conflicted-source-tip-diff.patch"
FILES = [
    "Governance/Charters/CAM-EQ2026-ETHICS-003-PLATINUM.md",
    "Governance/Charters/CAM-EQ2026-SECURITY-001-PLATINUM.md",
    "Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md",
    "Governance/Charters/CAM-EQ2026-STEWARD-003-PLATINUM.md",
    "Governance/Constitution/CAM-BS2025-AEON-001-SCH-01.md",
    "Governance/Constitution/CAM-BS2025-AEON-003-SCH-02.md",
    "Governance/Constitution/CAM-BS2025-AEON-006-PLATINUM.md",
    "Governance/Constitution/CAM-BS2026-AEON-012-PLATINUM.md",
]

subprocess.run(
    ["git", "fetch", "origin", "policy/civilisational-wealth-governance"],
    cwd=ROOT,
    check=True,
)
proc = subprocess.run(
    ["git", "diff", "--no-ext-diff", "--no-renames", "HEAD", OLD_REF, "--", *FILES],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=True,
)
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(
    "# Exact tip-to-tip source diff\n"
    "# Base: repair branch checkout HEAD\n"
    f"# Head: {OLD_REF}\n\n"
    + proc.stdout,
    encoding="utf-8",
)
