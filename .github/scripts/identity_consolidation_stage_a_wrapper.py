from pathlib import Path
import json
import runpy

ROOT = Path('.')
ORIGINAL = ROOT / '.github/scripts/identity_consolidation_stage_a.py'
CANONICAL_INDEX = ROOT / 'Governance/CAM.Canonical.Code.Index.json'
RETIRED_IDS = (
    'CAM-EQ2026-RELATION-009-SUP-01',
    'CAM-EQ2026-RELATION-009-PLATINUM',
    'CAM-BS2025-AEON-006-SCH-08',
)

try:
    runpy.run_path(str(ORIGINAL), run_name='__main__')
except SystemExit as exc:
    message = str(exc)
    expected = 'Governance/CAM.Canonical.Code.Index.json: retired IDENTITY-001-SUP-02'
    if expected not in message:
        raise

    def clean(value):
        if isinstance(value, str):
            return value.replace(
                'CAM-EQ2026-IDENTITY-001-SUP-02',
                'CAM-EQ2026-IDENTITY-001-PLATINUM',
            )
        if isinstance(value, list):
            return [clean(item) for item in value]
        if isinstance(value, dict):
            return {key: clean(item) for key, item in value.items()}
        return value

    data = json.loads(CANONICAL_INDEX.read_text(encoding='utf-8'))
    CANONICAL_INDEX.write_text(
        json.dumps(clean(data), indent=2, ensure_ascii=False) + '\n',
        encoding='utf-8',
    )

    hits = []
    for path in (ROOT / 'Governance').rglob('*'):
        if not path.is_file() or path.suffix.lower() not in {'.md', '.json', '.yml', '.yaml'}:
            continue
        text = path.read_text(encoding='utf-8', errors='ignore')
        for retired in RETIRED_IDS:
            if retired in text:
                hits.append(f'{path}: {retired}')
        if 'CAM-EQ2026-IDENTITY-001-SUP-02' in text:
            hits.append(f'{path}: retired IDENTITY-001-SUP-02')

    if hits:
        raise SystemExit('Active stale references remain after canonical-index repair:\n' + '\n'.join(hits[:100]))
