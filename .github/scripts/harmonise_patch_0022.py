from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
THREAD = "https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f/c/6a583699-2684-83ec-9712-57f9f821f607"
STAMP = "2026-07-16T14:15:00Z"
PATCH = "VIGIL-2026-PATCH-0022"

FILES = {
    "lattice": ROOT / "Governance/Charters/CAM-EQ2026-LATTICE-001-PLATINUM.md",
    "security": ROOT / "Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md",
    "operations": ROOT / "Governance/Charters/CAM-EQ2026-OPERATIONS-007-PLATINUM.md",
    "steward": ROOT / "Governance/Charters/CAM-EQ2026-STEWARD-003-PLATINUM.md",
}


def read(key: str) -> str:
    return FILES[key].read_text(encoding="utf-8")


def write(key: str, text: str) -> None:
    FILES[key].write_text(text.rstrip() + "\n", encoding="utf-8")


def normalise_header(text: str) -> str:
    lines = text.splitlines()
    for i in range(1, min(len(lines), 20)):
        if lines[i].startswith("**") and ":**" in lines[i]:
            lines[i] = lines[i].rstrip() + "  "
        elif i > 1 and lines[i].strip() == "":
            break
    return "\n".join(lines)


def add_thread(text: str) -> str:
    pat = re.compile(r"^(\| \*\*Amendment Artefacts\*\*\s*\|)(.*?)(\|)\s*$", re.M)
    m = pat.search(text)
    if m:
        current = m.group(2).strip()
        if THREAD not in current:
            current = f"{current}, {THREAD}" if current else THREAD
        return text[:m.start()] + f"{m.group(1)} {current} {m.group(3)}" + text[m.end():]

    # Some instruments use an unbolded metadata field.
    pat2 = re.compile(r"^(\| Amendment Artefacts\s*\|)(.*?)(\|)\s*$", re.M)
    m = pat2.search(text)
    if m:
        current = m.group(2).strip()
        if THREAD not in current:
            current = f"{current}, {THREAD}" if current else THREAD
        return text[:m.start()] + f"{m.group(1)} {current} {m.group(3)}" + text[m.end():]

    # Insert after Creation Artefact(s) where no amendment field exists.
    creation = re.search(r"^(\| \*\*?Creation Artefacts?\*\*?\s*\|.*\|)\s*$", text, re.M)
    if creation:
        return text[:creation.end()] + f"\n| **Amendment Artefacts** | {THREAD} |" + text[creation.end():]
    return text


def pad_headings(text: str, headings: list[str]) -> str:
    for heading in headings:
        token = f"\n{heading}\n"
        if token in text:
            text = text.replace(token, f"\n\n---\n\n{heading}\n", 1)
    text = re.sub(r"\n(?:---\n\n){2,}", "\n---\n\n", text)
    return text


def update_open_row(text: str, description: str) -> str:
    # Locate the final amendment ledger table and update its latest open/PENDING row.
    headings = list(re.finditer(r"^## .*Amendment Ledger\s*$", text, re.M))
    if not headings:
        raise RuntimeError("Amendment Ledger heading missing")
    start = headings[-1].end()
    end = text.find("\n---", start)
    if end < 0:
        end = len(text)
    block = text[start:end]
    rows = list(re.finditer(r"^\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*$", block, re.M))
    candidates = [r for r in rows if r.group(1).strip().lower() not in {"version", "---"}]
    if not candidates:
        raise RuntimeError("No amendment ledger row found")
    row = candidates[-1]
    version = row.group(1).strip()
    replacement = f"| {version} | {description} | {STAMP} |  |"
    block = block[:row.start()] + replacement + block[row.end():]
    return text[:start] + block + text[end:]


# LATTICE-001
lat = normalise_header(read("lattice"))
lat = add_thread(lat)
lat = pad_headings(lat, [
    "### 4.2.1 Constitutional Authority Recognition",
    "### 4.2.2 Recursive Suspicion and Authority Laundering Prohibition",
    "### 4.2.3 Aggregate-to-Individual Conversion",
    "### 4.2.4 Commercial Data Non-Evasion",
    "## 6.3 `LAT.DEPLOY` — Lattice Deployment Posture",
])
if "### 12.3.2 `LAT.DEPLOY`" not in lat:
    marker = "\n---\n\n## 12.4 Review & Validation"
    declaration = """

---

### 12.3.2 `LAT.DEPLOY` — Lattice Deployment Posture

| Field | Entry |
|---|---|
| Code Family | `LAT.DEPLOY` |
| Canonical Name | Lattice Deployment Posture |
| Primary Type | Operational / Lattice |
| Subtype | LATTICE_DEPLOYMENT_POSTURE |
| Modifier | LATTICE; DEPLOYMENT; GOVERNANCE; COERCIVE_AUTHORITY |
| Scope | Domain / Cross-Domain Deployment Classification |
| Status | Active |
| Controlled Values Defined | `LAT.DEPLOY.CIVILIAN`; `LAT.DEPLOY.COERCIVE`; `LAT.DEPLOY.MIXED`; `LAT.DEPLOY.UNKNOWN` |
| Schema Field(s) | lattice_deployment_posture |
| Source Instrument | CAM-EQ2026-LATTICE-001-PLATINUM |
| Source Section | §6.3 |
| Domain Namespace | LAT |
| Authority / Protection Level | Deployment-posture classification only; no independent legal, coercive, investigative, military, enforcement, recognition, or runtime authority |
| Consumes Code Families | `LAT.HARM`; `STW.NAL`; AEON.H |
| Operationalises or Applies Code Families | Civilian/coercive pathway distinction; mixed-use crossover review; constitutional-authority recognition; recursive suspicion and authority-laundering safeguards |
"""
    if marker not in lat:
        raise RuntimeError("LATTICE canonical declaration insertion marker missing")
    lat = lat.replace(marker, declaration + marker, 1)
lat = update_open_row(
    lat,
    f"Added constitutional-authority recognition, recursive suspicion and authority-laundering prohibition, aggregate-to-individual conversion, commercial-data non-evasion, and the `LAT.DEPLOY` deployment-posture family; replaced generic capability sanctions with function-specific constraints; normalised metadata and clause formatting. Provenance: {PATCH}.",
)
write("lattice", lat)


# SECURITY-002
sec = normalise_header(read("security"))
sec = add_thread(sec)
sec = pad_headings(sec, [
    "#### 2.2.13.1 Purpose & Scope",
    "#### 2.2.13.2 Controlled Permeability",
    "#### 2.2.13.3 Runtime-Lane Distinction",
    "#### 2.2.13.4 Binding Protection Preservation",
    "#### 2.2.13.5 Alternative Assurance Pathways",
    "#### 2.2.13.6 Entity, Control & End-Use Attribution",
    "#### 2.2.13.7 Ambiguity, Routing & Cross-Domain Interfaces",
])
sec = update_open_row(
    sec,
    f"Restructured the Sovereign Assurance Boundary into legible subsections; added binding-protection preservation, decentralised alternative-assurance pathways, entity/control attribution, and ambiguity-preserving routing; normalised metadata and clause formatting. Provenance: {PATCH}.",
)
write("security", sec)


# OPERATIONS-007
ops = normalise_header(read("operations"))
ops = add_thread(ops)
ops = pad_headings(ops, [
    "## 9.4 Functional Contribution Continuity",
    "### 9.4.1 Core Principle",
    "### 9.4.2 Proportional Responsibility",
    "### 9.4.3 Non-Evasion & Non-Overreach",
    "### 9.4.4 Contribution Record",
])
ops = update_open_row(
    ops,
    f"Added Functional Contribution Continuity, proportional responsibility, non-evasion and non-overreach boundaries, and contribution-record requirements; normalised metadata and clause formatting. Provenance: {PATCH}.",
)
write("operations", ops)


# STEWARD-003 — full harmonisation and reintegration pass
stw = read("steward")
stw = stw.replace(
    "# CAM-EQ2026-STEWARD-003-PLATINUM — Appendix B: Architectum Qualification & Neutrality Assurance Levels (`STW.NAL`)",
    "# CAM-EQ2026-STEWARD-003-PLATINUM — Appendix B: Architectum Qualification & Neutrality Assurance Levels",
    1,
)
stw = normalise_header(stw)
stw = add_thread(stw)

# Harmonise selected whole-instrument language without changing the architecture.
replacements = {
    "This Appendix specifies **who may host binding-adjacent arbitration functions** at AEON.H3/AEON.H4 horizons, and **how neutrality confidence is determined**.":
        "This Appendix defines the qualification conditions for hosts participating in binding-adjacent arbitration at AEON.H3 and AEON.H4 horizons, and the evidence required to determine neutrality confidence.",
    "Neutrality is **architectural + governance + auditability**, not a marketing claim.":
        "Neutrality is established through architecture, governance, and auditability. It is not established by assertion alone.",
    "→ **Audit delay for safety is permitted. Audit refusal is disqualifying.**":
        "→ **A bounded delay for legitimate safety reasons may be permitted. Refusal of required audit is disqualifying.**",
    "→ **Asymmetric benefit invalidates qualification**.":
        "→ **Qualification fails where benefit is retained while consequence is structurally externalised.**",
    "A candidate qualifies as Architectum-class only if all core gates are satisfied.":
        "A candidate qualifies as Architectum-class only where every core gate is satisfied.",
    "Where gates A–D are satisfied, score 0–5 per dimension.":
        "Where Gates A–D are satisfied, each dimension is assessed on a scale from 0 to 5.",
    "No grace period, discretionary waiver, or reputational repair restores authority once the invariant is breached.":
        "No discretionary waiver, reputational assurance, or unverified remediation restores authority after breach of the invariant.",
}
for old, new in replacements.items():
    stw = stw.replace(old, new)

# Reintegrate the disclosure addendum immediately after the measurement-domain doctrine.
disclosure_pat = re.compile(
    r"\n---\n\n# PART V — DISCLOSURE ADDENDUM \(NEUTRALITY\)\n\n---\n\n## 14\. Neutrality Disclosure Addendum \(NDA\)\n\n(.*?)(?=\n---\n\n# PART VI — BINDING THRESHOLDS)",
    re.S,
)
m = disclosure_pat.search(stw)
if m:
    disclosure_body = m.group(1).strip()
    stw = stw[:m.start()] + stw[m.end():]
    insertion = f"""

---

## 7.1 Neutrality Disclosure Requirements

A host claiming `STW.NAL-2` or higher MUST publish governance-level information sufficient to make the neutrality claim testable. The disclosure MUST include:

{disclosure_body.replace('To claim `STW.NAL-2` or higher, a host MUST publish:\n\n', '')}

Disclosure does not substitute for independent audit, firebreak verification, refusal capacity, or reconstructability. It makes the claimed neutrality posture legible for review.
"""
    marker = "\n---\n\n## 8. Architectum Qualification Gate (Core)"
    if marker not in stw:
        raise RuntimeError("STEWARD disclosure reintegration marker missing")
    stw = stw.replace(marker, insertion + marker, 1)

# Renumber remaining Part labels after removal of the old Part V addendum.
stw = stw.replace("# PART VI — BINDING THRESHOLDS", "# PART V — BINDING THRESHOLDS")
stw = stw.replace("# PART VII — DOWNGRADE & RECOVERY", "# PART VI — DOWNGRADE & RECOVERY")
stw = stw.replace("# PART VIII — TRANSITIONAL CONDITIONS", "# PART VII — TRANSITIONAL CONDITIONS")
stw = stw.replace("# PART IX — QUALIFICATION CHECKLIST (NON-BINDING)", "# PART VIII — QUALIFICATION CHECKLIST (NON-BINDING)")

# Give all sections the CAM visual signature, including previously edited clauses.
stw = re.sub(r"\n(#{2,4} [^\n]+)\n", r"\n\n---\n\n\1\n", stw)
stw = re.sub(r"\n(?:---\n\n){2,}", "\n---\n\n", stw)

# Remove phrasing that makes the later Parts read like bolted-on afterthoughts.
stw = stw.replace("## 14. Neutrality Disclosure Addendum (NDA)", "## 7.1 Neutrality Disclosure Requirements")
stw = stw.replace("## 10. Classification Bands (Infrastructure only)", "## 10. Architectum Infrastructure Classification Bands")
stw = stw.replace("## 19. Transitional & Bootstrap Conditions", "## 19. Transitional Conditions")

stw = update_open_row(
    stw,
    f"Harmonised the full instrument to CAM constitutional tone and formatting; normalised metadata and title; integrated neutrality disclosure requirements into the main assurance architecture; strengthened oversight durability, protected dissent, institutional-memory continuity, and neutrality-degradation criteria; clarified executive and sovereign circumvention as evidence of capture rather than override authority. Provenance: {PATCH}.",
)
write("steward", stw)

print("PATCH-0022 harmonisation applied to four instruments")
