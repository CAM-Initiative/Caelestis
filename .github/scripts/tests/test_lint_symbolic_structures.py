import pathlib
import subprocess
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
SCRIPT = REPO_ROOT / ".github" / "scripts" / "lint-symbolic-structures.py"


def run_lint(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_missing_deprecated_index_is_non_fatal_when_not_required():
    result = run_lint(
        "--index",
        ".github/Indices/CAM.Governance.Symbolic-Structures.Index.json",
        "--registry",
        ".github/Indices/CAM.Governance.Symbolic-Structures.Registry.json",
    )
    assert result.returncode == 0
    assert "skipping legacy symbolic index checks" in result.stdout


def test_missing_deprecated_index_fails_when_explicitly_required():
    result = run_lint(
        "--index",
        ".github/Indices/CAM.Governance.Symbolic-Structures.Index.json",
        "--require-index",
    )
    assert result.returncode == 1
    assert "Required index file not found" in result.stdout
