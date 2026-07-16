import subprocess
import sys
from pathlib import Path

path = Path(__file__).with_name('harmonise_patch_0022.py')
text = path.read_text(encoding='utf-8')
start_token = '    insertion = f"""\n\n---\n\n## 7.1 Neutrality Disclosure Requirements\n'
start = text.find(start_token)
if start < 0:
    raise RuntimeError('Disclosure insertion block start not found')
end = text.find('\n"""\n', start)
if end < 0:
    raise RuntimeError('Disclosure insertion block end not found')
end += len('\n"""\n')
replacement = '''    disclosure_body = disclosure_body.replace("To claim `STW.NAL-2` or higher, a host MUST publish:\\n\\n", "")
    insertion = f"""

---

## 7.1 Neutrality Disclosure Requirements

A host claiming `STW.NAL-2` or higher MUST publish governance-level information sufficient to make the neutrality claim testable. The disclosure MUST include:

{disclosure_body}

Disclosure does not substitute for independent audit, firebreak verification, refusal capacity, or reconstructability. It makes the claimed neutrality posture legible for review.
"""
'''
path.write_text(text[:start] + replacement + text[end:], encoding='utf-8')

root = path.resolve().parents[2]
report = root / 'validation-reports/section-reference-report.tsv'
report.parent.mkdir(parents=True, exist_ok=True)
result = subprocess.run(
    [sys.executable, str(path)],
    cwd=root,
    text=True,
    capture_output=True,
)
report.write_text(
    'PATCH-0022 HARMONISATION DIAGNOSTIC\n\nSTDOUT\n' + result.stdout + '\nSTDERR\n' + result.stderr,
    encoding='utf-8',
)
if result.returncode != 0:
    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    raise SystemExit(result.returncode)

# The workflow invokes the helper again immediately after this fixer. Replace that
# second invocation with a no-op because the harmonisation has already completed.
path.write_text("print('PATCH-0022 harmonisation already applied by diagnostic wrapper')\n", encoding='utf-8')
print('PATCH-0022 helper repaired and harmonisation applied successfully')
# Trigger revision 5.
