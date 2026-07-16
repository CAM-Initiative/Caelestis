import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[2]
branch = 'governance/relational-profile-coformation'
subprocess.run(
    ['git', 'checkout', '-B', branch, f'origin/{branch}'],
    cwd=root,
    check=True,
)

cleanup = root / '.github/scripts/cleanup_patch_0022_hook.py'
subprocess.run(['python', str(cleanup)], cwd=root, check=True)

subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'], cwd=root, check=True)
subprocess.run(['git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'], cwd=root, check=True)
subprocess.run(
    ['git', 'add', '-A', '.github/workflows', '.github/scripts'],
    cwd=root,
    check=True,
)
subprocess.run(
    ['git', 'commit', '-m', 'Remove temporary PATCH-0022 tooling'],
    cwd=root,
    check=True,
)
subprocess.run(
    ['git', 'push', 'origin', f'HEAD:{branch}'],
    cwd=root,
    check=True,
)
print('Temporary PATCH-0022 tooling removed and standard workflow restored')
