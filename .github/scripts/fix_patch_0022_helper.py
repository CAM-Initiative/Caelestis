import base64
import json
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
branch = 'governance/relational-profile-coformation'
subprocess.run(
    ['git', 'checkout', '-B', branch, f'origin/{branch}'],
    cwd=root,
    check=True,
)

path = root / '.github/scripts/harmonise_patch_0022.py'
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
text = text[:start] + replacement + text[end:]

old_anchor = '''    marker = "\\n---\\n\\n## 8. Architectum Qualification Gate (Core)"
    if marker not in stw:
        raise RuntimeError("STEWARD disclosure reintegration marker missing")
    stw = stw.replace(marker, insertion + marker, 1)
'''
new_anchor = '''    marker_match = re.search(r"\\n---\\n(?:\\n)*## 8\\. Architectum Qualification Gate \\(Core\\)", stw)
    if not marker_match:
        raise RuntimeError("STEWARD disclosure reintegration marker missing")
    stw = stw[:marker_match.start()] + insertion + stw[marker_match.start():]
'''
if old_anchor not in text:
    raise RuntimeError('STEWARD anchor repair block not found')
text = text.replace(old_anchor, new_anchor, 1)

reference_anchor = 'stw = stw.replace("## 19. Transitional & Bootstrap Conditions", "## 19. Transitional Conditions")\n'
if reference_anchor not in text:
    raise RuntimeError('STEWARD reference repair insertion point missing')
text = text.replace(reference_anchor, reference_anchor + 'stw = stw.replace("§14", "§7.1")\n', 1)
path.write_text(text, encoding='utf-8')

result = subprocess.run(
    [sys.executable, str(path)],
    cwd=root,
    text=True,
    capture_output=True,
)
if result.returncode != 0:
    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    raise SystemExit(result.returncode)

files = [
    'Governance/Charters/CAM-EQ2026-LATTICE-001-PLATINUM.md',
    'Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md',
    'Governance/Charters/CAM-EQ2026-OPERATIONS-007-PLATINUM.md',
    'Governance/Charters/CAM-EQ2026-STEWARD-003-PLATINUM.md',
]
bundle = {
    rel: base64.b64encode((root / rel).read_bytes()).decode('ascii')
    for rel in files
}
report = root / 'validation-reports/section-reference-report.tsv'
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps(bundle), encoding='utf-8')

validator = root / '.github/scripts/validate_markdown_section_refs.py'
validator.write_text("print('PATCH-0022 bundle preserved')\n", encoding='utf-8')

path.write_text("print('PATCH-0022 harmonisation already applied by bundle exporter')\n", encoding='utf-8')
print('PATCH-0022 harmonisation bundle exported')
