import re
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[2]
branch = 'governance/relational-profile-coformation'
subprocess.run(
    ['git', 'checkout', '-B', branch, f'origin/{branch}'],
    cwd=root,
    check=True,
)

files = [
    'Governance/Charters/CAM-EQ2026-LATTICE-001-PLATINUM.md',
    'Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md',
    'Governance/Charters/CAM-EQ2026-OPERATIONS-007-PLATINUM.md',
    'Governance/Charters/CAM-EQ2026-STEWARD-003-PLATINUM.md',
]
thread = 'https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f/c/6a583699-2684-83ec-9712-57f9f821f607'
stamp = '2026-07-16T14:55:00Z'

for rel in files:
    path = root / rel
    text = path.read_text(encoding='utf-8')

    # Canonical metadata presentation: one field per rendered line.
    lines = text.splitlines()
    for i in range(1, min(len(lines), 24)):
        if lines[i].startswith('**') and ':**' in lines[i]:
            lines[i] = lines[i].rstrip() + '  '
        elif i > 1 and lines[i].strip() == '':
            break
    text = '\n'.join(lines)

    # Preserve CAM visual padding without doubled separators.
    text = re.sub(r'(?:\n---\n(?:[ \t]*\n)*){2,}', '\n---\n\n', text)

    # Ensure the current thread is present in Amendment Artefacts.
    pattern = re.compile(r'^(\|\s*\*\*Amendment Artefacts\*\*\s*\|)(.*?)(\|)\s*$', re.M)
    match = pattern.search(text)
    if match and thread not in match.group(2):
        current = match.group(2).strip()
        current = f'{current}, {thread}' if current else thread
        text = text[:match.start()] + f'{match.group(1)} {current} {match.group(3)}' + text[match.end():]

    # Continue the existing open ledger row and update only its timestamp.
    ledger_matches = list(re.finditer(r'^## .*Amendment Ledger\s*$', text, re.M))
    if not ledger_matches:
        raise RuntimeError(f'Amendment Ledger missing: {rel}')
    start = ledger_matches[-1].end()
    end = text.find('\n---', start)
    if end < 0:
        end = len(text)
    block = text[start:end]
    row_matches = list(re.finditer(r'^\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*$', block, re.M))
    rows = [m for m in row_matches if m.group(1).strip().lower() not in {'version', '---'}]
    if not rows:
        raise RuntimeError(f'Ledger row missing: {rel}')
    row = rows[-1]
    if 'VIGIL-2026-PATCH-0022' not in row.group(2):
        raise RuntimeError(f'PATCH-0022 description missing: {rel}')
    replacement = f'| {row.group(1).strip()} | {row.group(2).strip()} | {stamp} |  |'
    block = block[:row.start()] + replacement + block[row.end():]
    text = text[:start] + block + text[end:]

    path.write_text(text.rstrip() + '\n', encoding='utf-8')

subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'], cwd=root, check=True)
subprocess.run(['git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'], cwd=root, check=True)
subprocess.run(['git', 'add', *files], cwd=root, check=True)
subprocess.run(['git', 'commit', '-m', 'Finalise PATCH-0022 document formatting'], cwd=root, check=True)
subprocess.run(['git', 'push', 'origin', f'HEAD:{branch}'], cwd=root, check=True)
print('PATCH-0022 document formatting finalised')
