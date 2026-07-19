from pathlib import Path

root = Path(__file__).resolve().parents[2]
for transient in (
    root / ".github/trigger-identity-finalisation-pr.txt",
    root / ".github/scripts/remove-second-trigger-marker.py",
):
    if transient.exists():
        transient.unlink()
