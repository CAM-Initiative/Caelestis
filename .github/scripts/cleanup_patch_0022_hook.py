from pathlib import Path

root = Path(__file__).resolve().parents[2]
workflow = root / '.github/workflows/governance-rebuild.yml'
text = workflow.read_text(encoding='utf-8')
start = '      # PATCH-0022 TEMPORARY HOOK BEGIN\n'
end = '      # PATCH-0022 TEMPORARY HOOK END\n'
if start in text and end in text:
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    text = before + after
text = text.replace("      - '.github/workflows/governance-rebuild.yml'\n", '')
text = text.replace("        if: env.PATCH_0022_MODE != 'true'\n        run: python .github/scripts/verify-ledger-sha-coverage.py --strict-latest\n", "        run: python .github/scripts/verify-ledger-sha-coverage.py --strict-latest\n")
workflow.write_text(text, encoding='utf-8')

for rel in [
    '.github/workflows/apply-patch-0022-harmonisation.yml',
    '.github/scripts/harmonise_patch_0022.py',
    '.github/scripts/cleanup_patch_0022_hook.py',
]:
    p = root / rel
    if p.exists():
        p.unlink()

print('PATCH-0022 temporary workflow hooks removed')
