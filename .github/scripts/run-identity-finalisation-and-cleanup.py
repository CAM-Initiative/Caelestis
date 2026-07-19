from pathlib import Path
import runpy

root = Path(__file__).resolve().parents[2]
runpy.run_path(str(root / ".github/scripts/apply-identity-refactor-finalisation-hygiene.py"), run_name="__main__")

for transient in (
    root / ".github/automation-trigger-identity-finalisation-20260719.txt",
    root / ".github/trigger-identity-finalisation-pr.txt",
    root / ".github/THIS_SHOULD_NOT_EXIST.txt",
    root / ".github/NOPE.txt",
    root / ".github/scripts/remove-second-trigger-marker.py",
    root / ".github/scripts/run-identity-finalisation-and-cleanup.py",
):
    if transient.exists():
        transient.unlink()
