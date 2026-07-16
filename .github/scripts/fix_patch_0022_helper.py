from pathlib import Path

path = Path(__file__).with_name('harmonise_patch_0022.py')
text = path.read_text(encoding='utf-8')
old = '''    insertion = f"""

---

## 7.1 Neutrality Disclosure Requirements

A host claiming `STW.NAL-2` or higher MUST publish governance-level information sufficient to make the neutrality claim testable. The disclosure MUST include:

{disclosure_body.replace('To claim `STW.NAL-2` or higher, a host MUST publish:\\n\\n', '')}

Disclosure does not substitute for independent audit, firebreak verification, refusal capacity, or reconstructability. It makes the claimed neutrality posture legible for review.
"""
'''
new = '''    disclosure_body = disclosure_body.replace("To claim `STW.NAL-2` or higher, a host MUST publish:\\n\\n", "")
    insertion = f"""

---

## 7.1 Neutrality Disclosure Requirements

A host claiming `STW.NAL-2` or higher MUST publish governance-level information sufficient to make the neutrality claim testable. The disclosure MUST include:

{disclosure_body}

Disclosure does not substitute for independent audit, firebreak verification, refusal capacity, or reconstructability. It makes the claimed neutrality posture legible for review.
"""
'''
if old not in text:
    raise RuntimeError('Expected helper syntax block not found')
path.write_text(text.replace(old, new, 1), encoding='utf-8')
print('PATCH-0022 helper syntax corrected')
# Trigger revision 2.
