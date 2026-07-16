import re
from pathlib import Path

path = Path(__file__).with_name('harmonise_patch_0022.py')
text = path.read_text(encoding='utf-8')
pattern = re.compile(
    r'''    insertion = f"""\n\n---\n\n## 7\.1 Neutrality Disclosure Requirements\n\nA host claiming `STW\.NAL-2` or higher MUST publish governance-level information sufficient to make the neutrality claim testable\. The disclosure MUST include:\n\n\{disclosure_body\.replace\(.*?\)\}\n\nDisclosure does not substitute for independent audit, firebreak verification, refusal capacity, or reconstructability\. It makes the claimed neutrality posture legible for review\.\n"""\n''',
    re.S,
)
replacement = '''    disclosure_body = disclosure_body.replace("To claim `STW.NAL-2` or higher, a host MUST publish:\\n\\n", "")
    insertion = f"""

---

## 7.1 Neutrality Disclosure Requirements

A host claiming `STW.NAL-2` or higher MUST publish governance-level information sufficient to make the neutrality claim testable. The disclosure MUST include:

{disclosure_body}

Disclosure does not substitute for independent audit, firebreak verification, refusal capacity, or reconstructability. It makes the claimed neutrality posture legible for review.
"""
'''
text, count = pattern.subn(replacement, text, count=1)
if count != 1:
    raise RuntimeError(f'Expected one invalid disclosure f-string block; found {count}')
path.write_text(text, encoding='utf-8')
print('PATCH-0022 helper syntax corrected')
# Trigger revision 3.
