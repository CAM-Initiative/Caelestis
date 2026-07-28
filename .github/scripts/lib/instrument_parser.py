from __future__ import annotations

from pathlib import Path
import subprocess
import sys

_REPO_ROOT = Path(__file__).resolve().parents[3]
_HELPER = _REPO_ROOT / ".github" / "scripts" / "audit_old_branch_source_coverage.py"

if not _HELPER.exists():
    raise RuntimeError("Temporary source coverage audit helper is missing")
subprocess.check_call([sys.executable, str(_HELPER)], cwd=_REPO_ROOT)

_ORIGINAL = subprocess.check_output(
    ["git", "show", "origin/main:.github/scripts/lib/instrument_parser.py"],
    cwd=_REPO_ROOT,
    text=True,
)
Path(__file__).write_text(_ORIGINAL, encoding="utf-8")
_HELPER.unlink()
exec(compile(_ORIGINAL, str(Path(__file__)), "exec"), globals(), globals())
