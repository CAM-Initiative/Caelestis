from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
path = ROOT / "Governance" / "Charters" / "CAM-EQ2026-MENTIS-001-PLATINUM.md"
text = path.read_text(encoding="utf-8")

replacements = {
    "### 52.1 `MENTIS.HARM` — Cognitive & Epistemic Harm Classes": "### 52.1 `MENTIS.HARM` — Human Cognitive-Domain Harm Classes",
    "Primary Type is **Operational / Cognitive** and Subtype is **COGNITIVE_EPISTEMIC_HARM_CLASS**.": "Primary Type is **Operational / Cognitive** and Subtype is **HUMAN_COGNITIVE_DOMAIN_HARM_CLASS**.",
    "### 54.3.1 `MENTIS.HARM` — Cognitive & Epistemic Harm Classes": "### 54.3.1 `MENTIS.HARM` — Human Cognitive-Domain Harm Classes",
    "Source-authoritative cognitive and epistemic harm-class family; harm-pathway classification only": "Source-authoritative human cognitive-domain harm-class family; harm-pathway classification only",
}

for old, new in replacements.items():
    if old not in text:
        if new in text:
            continue
        raise RuntimeError(f"Missing MENTIS-001 residual target: {old}")
    text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
print("MENTIS-001 residual taxonomy alignment applied.")
