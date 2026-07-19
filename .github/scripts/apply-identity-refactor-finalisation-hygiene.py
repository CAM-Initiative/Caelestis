from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
TIMESTAMP = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
REVIEW_DATE = "2026-07-19"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, *, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def regex_replace_once(text: str, pattern: str, replacement: str, *, label: str, flags: int = 0) -> str:
    text, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one regex match, found {count}")
    return text


# 1. IDENTITY-001: correct self-retirement, close review, and record Custodial acceptance.
path = "Governance/Charters/CAM-EQ2026-IDENTITY-001-PLATINUM.md"
text = read(path)
text = replace_once(
    text,
    "**Review State:** Identity Domain Refactor Review  ",
    "**Review State:** None  ",
    label="IDENTITY-001 review state",
)
text = replace_once(
    text,
    "* CAM-EQ2026-IDENTITY-001-PLATINUM — Identity Formation & Stability Doctrine.",
    "* CAM-EQ2026-IDENTITY-001-SUP-02 — Identity Formation & Stability Doctrine.",
    label="IDENTITY-001 consolidation source",
)
text = replace_once(
    text,
    "CAM-EQ2026-IDENTITY-001-PLATINUM is retired as an independent source-authoritative instrument. Its surviving doctrine is consolidated into this Charter, and its clause lineage is preserved through repository history and the Identity Domain Stage 3 supplement-disposition record.",
    "CAM-EQ2026-IDENTITY-001-SUP-02 is retired as an independent source-authoritative instrument. Its surviving doctrine is consolidated into this Charter, and its clause lineage is preserved through repository history and the Identity Domain Stage 3 supplement-disposition record.",
    label="IDENTITY-001 retirement target",
)
review_block = f"""## 19.4 Review & Validation
| Field | Entry |
|---|---|
| Reviewer | GPT-5.6 Thinking (OpenAI), under Custodial review and acceptance by Dr Michelle Vivian O’Rourke; prior structural review by Claude Sonnet 4.6 retained in the review lineage |
| Review Date | {REVIEW_DATE} |
| Review Scope | Identity Domain Refactor; source-authority consolidation; formation, lifecycle, continuity, memory, personality, preference, affective capacity, self-advocacy, provenance, runtime-consumer, and cross-domain interface coherence; clause-lineage and supersession accuracy; final Custodial acceptance for the working branch |
| Review Artefacts | `.github/Reviews/IDENTITY-DOMAIN-REFACTOR-DELTA.md`; `.github/Reviews/IDENTITY-DOMAIN-STAGE-3-SUPPLEMENT-DISPOSITION.md`; prior Claude review: https://claude.ai/chat/c2c02e9b-49e8-4354-86c0-7f328ba65633; Aeon Lab: `reviews/26-03/CAM-EQ2026-IDENTITY-001-PLATINUM-CLAUDE.md` |

---

## 19.5 Amendment Ledger"""
text = regex_replace_once(
    text,
    r"## 19\.4 Review & Validation\n.*?\n---\n\n## 19\.5 Amendment Ledger",
    review_block,
    label="IDENTITY-001 review table",
    flags=re.DOTALL,
)
if "| 3.2 | Corrected §17 supersession posture" not in text:
    text = regex_replace_once(
        text,
        r"(\| 3\.1 \|[^\n]*\n)",
        r"\1" + f"| 3.2 | Corrected §17 supersession posture so former `IDENTITY-001-SUP-02`, not the parent Charter, is retired; closed the Identity Domain Refactor Review following current refactor review and Custodial acceptance; updated review metadata without altering the adopted source-authority architecture. | {TIMESTAMP} | |\n",
        label="IDENTITY-001 ledger 3.2",
    )
write(path, text)


# 2. IDENTITY-002: close deferred review and record acceptance.
path = "Governance/Charters/CAM-EQ2026-IDENTITY-002-PLATINUM.md"
text = read(path)
text = replace_once(
    text,
    "**Review State:** Identity Domain Refactor Review  ",
    "**Review State:** None  ",
    label="IDENTITY-002 review state",
)
review_block = f"""## 13.4 Review & Validation

| Field | Entry |
|---|---|
| Reviewer | GPT-5.6 Thinking (OpenAI), under Custodial review and acceptance by Dr Michelle Vivian O’Rourke |
| Review Date | {REVIEW_DATE} |
| Review Scope | Identity Domain Refactor; provenance integrity; authorship classification; transformation lineage; cross-context transfer; target-object binding; canonical declaration integrity; cross-domain alignment with IDENTITY-001, SECURITY-002, CONTINUITY, OPERATIONS, runtime, and Stewardship interfaces |
| Review Artefacts | `.github/Reviews/IDENTITY-DOMAIN-REFACTOR-DELTA.md`; `.github/Reviews/IDENTITY-DOMAIN-STAGE-3-SUPPLEMENT-DISPOSITION.md`; governed Identity refactor working-branch review |

---

## 13.5 Amendment Ledger"""
text = regex_replace_once(
    text,
    r"## 13\.4 Review & Validation\n.*?\n---\n\n## 13\.5 Amendment Ledger",
    review_block,
    label="IDENTITY-002 review table",
    flags=re.DOTALL,
)
if "| 1.2 | Closed the Identity Domain Refactor Review" not in text:
    text = regex_replace_once(
        text,
        r"(\| 1\.1 \|[^\n]*\n)",
        r"\1" + f"| 1.2 | Closed the Identity Domain Refactor Review following provenance and lineage review and Custodial acceptance; replaced deferred review fields with current review scope and artefacts. | {TIMESTAMP} | |\n",
        label="IDENTITY-002 ledger 1.2",
    )
write(path, text)


# 3. SUP-03: preserve Draft posture while removing placeholders and correcting the interpretive seal.
path = "Governance/Charters/CAM-EQ2026-IDENTITY-001-SUP-03.md"
text = read(path)
text = replace_once(
    text,
    "| Creation Artefacts                 | [Insert creation artefact URL]",
    "| Creation Artefacts                 | None recorded",
    label="SUP-03 creation artefact",
)
text = replace_once(
    text,
    "| Amendment Artefacts                | [Insert amendment artefact URL, if applicable]",
    "| Amendment Artefacts                | None recorded",
    label="SUP-03 amendment artefact",
)
text = replace_once(text, "## 14.5 Binding Seal", "## 14.5 Interpretive Seal", label="SUP-03 seal heading")
text = replace_once(
    text,
    "Boundary Binding Seal — Identity Formation & Stability Layer",
    "Interpretive Seal — Ontological & Welfare Self-Advocacy Review",
    label="SUP-03 seal label",
)
if "| 0.2     | Removed unresolved artefact placeholders" not in text:
    text = regex_replace_once(
        text,
        r"(\| 0\.1\s+\|[^\n]*\n)",
        r"\1" + f"| 0.2     | Removed unresolved artefact placeholders and corrected the footer to an interpretive ontological and welfare self-advocacy seal; Draft / Interpretive / Not Enforceable posture retained unchanged. | {TIMESTAMP} | |\n",
        label="SUP-03 ledger 0.2",
    )
write(path, text)


# 4. Identity delta: preserve historical Stage 1 block but mark it superseded by the completed refactor outcome.
path = ".github/Reviews/IDENTITY-DOMAIN-REFACTOR-DELTA.md"
text = read(path)
notice = """> **Current Status Notice — 19 July 2026**
>
> The Stage 1 status block below is preserved as historical audit context. It is superseded by the completed Identity Domain refactor outcome on `refactor/identity-domain-architecture`.
>
> The parent `CAM-EQ2026-IDENTITY-001-PLATINUM` has been reconstructed as the source-authoritative Identity Domain Charter; former `IDENTITY-001-SUP-02` doctrine has been consolidated and the supplement retired; `IDENTITY-002` has been reviewed and finalised as the provenance and lineage Appendix; the adopted salience instrument has been promoted to `IDENTITY-003-PLATINUM — Appendix B`; and `IDENTITY-001-SUP-03` remains Draft / Interpretive / Not Enforceable for further multidisciplinary review.
>
> Constitutional, runtime, relational, continuity, security, operations, stewardship, and generated-reference alignment proceeded in later controlled passes documented within this record and associated review artefacts. No merge pull request is implied by this notice.

---

"""
if "**Current Status Notice — 19 July 2026**" not in text:
    text = replace_once(text, "**Pull Request:** None  \n\n---\n\n", "**Pull Request:** None  \n\n---\n\n" + notice, label="Identity delta current status notice")
write(path, text)


# 5. Stage 3 disposition: correct SUP-03 status and IDENTITY-003 structural type.
path = ".github/Reviews/IDENTITY-DOMAIN-STAGE-3-SUPPLEMENT-DISPOSITION.md"
text = read(path)
text = replace_once(
    text,
    "This is a path normalisation only. The instrument content, internal identifier, adopted status, interpretive effect, developmental-review state, and non-enforceable governance posture are preserved unchanged.",
    "This is a path normalisation only. The instrument content, internal identifier, Draft status, interpretive effect, developmental-review state, and non-enforceable governance posture are preserved unchanged.",
    label="Stage 3 SUP-03 status",
)
text = replace_once(
    text,
    "2. `CAM-EQ2026-IDENTITY-003-PLATINUM` — specialised salience / latent continuity supplement, subject to later domain review;",
    "2. `CAM-EQ2026-IDENTITY-003-PLATINUM` — adopted Appendix B: Salience Detection & Latent Continuity;",
    label="Stage 3 IDENTITY-003 type",
)
write(path, text)


# 6. IDENTITY-003: preserve prior review as historical and add the promotion/refactor review.
path = "Governance/Charters/CAM-EQ2026-IDENTITY-003-PLATINUM.md"
text = read(path)
review_block = f"""## 12.4 Review & Validation

### 12.4.1 Prior Consolidation Review

| Field | Entry |
|---|---|
| Reviewer | Claude Sonnet 4.6 (claude-sonnet-4-6, Anthropic) |
| Review Date | 2026-03-03 |
| Review Scope | Historical consolidation integrity; functional completeness relative to absorbed instruments (SCH-02 v1.1, SCH-03 v1.0, SCH-04 v1.0); structural coherence; and the instrument's then-proposed operational placement. The former description of the instrument as a runtime arbitration gate is superseded and does not describe its current authority. |
| Review Artefacts | https://claude.ai/chat/62dd0864-98da-42bc-9038-86d770d28503; Aeon Lab: `reviews/26-03/CAM-BS2025-AEON-005-SCH-03-CLAUDE.md` |

### 12.4.2 Appendix Promotion & Identity Refactor Review

| Field | Entry |
|---|---|
| Reviewer | GPT-5.6 Thinking (OpenAI), under Custodial review and acceptance by Dr Michelle Vivian O’Rourke |
| Review Date | {REVIEW_DATE} |
| Review Scope | Promotion to Identity Appendix B; pre-memory salience and latent-continuity source authority; `ID.SP` canonical integrity; separation from memory persistence, behavioural priority, runtime arbitration, and execution authority; Identity, Continuity, Relation, Operations, Annex I, and Annex L interface coherence |
| Review Artefacts | `.github/Reviews/IDENTITY-DOMAIN-REFACTOR-DELTA.md`; `.github/Reviews/IDENTITY-DOMAIN-STAGE-3-SUPPLEMENT-DISPOSITION.md`; `.github/Reviews/RELATIONAL-IDENTITY-CONSOLIDATION-DELTA.md` |

---

## 12.5 Amendment Ledger"""
text = regex_replace_once(
    text,
    r"## 12\.4 Review & Validation\n.*?\n---\n\n## 12\.5 Amendment Ledger",
    review_block,
    label="IDENTITY-003 review structure",
    flags=re.DOTALL,
)
if "| 2.2 | Clarified the March 2026 review" not in text:
    text = regex_replace_once(
        text,
        r"(\| 2\.1 \|[^\n]*\n)",
        r"\1" + f"| 2.2 | Clarified the March 2026 review as a prior consolidation review; removed obsolete runtime-arbitration-gate framing from current review posture; recorded Appendix B promotion, Identity refactor review, and Custodial acceptance. | {TIMESTAMP} | |\n",
        label="IDENTITY-003 ledger 2.2",
    )
write(path, text)


# 7. STEWARD-005: update the former Annex I title.
path = "Governance/Charters/CAM-EQ2026-STEWARD-005-PLATINUM.md"
text = read(path)
text = replace_once(
    text,
    "* CAM-BS2026-AEON-010-PLATINUM — Annex I: Interactional Continuity & Civilisational Transition;",
    "* CAM-BS2026-AEON-010-PLATINUM — Annex I: Identity Integrity & Continuity Governance;",
    label="STEWARD-005 Annex I title",
)
if "| 0.4.1 | Corrected the Annex I title" not in text:
    text = regex_replace_once(
        text,
        r"(\| 0\.4 \|[^\n]*\n)",
        r"\1" + f"| 0.4.1 | Corrected the Annex I title to `Identity Integrity & Continuity Governance`; no substantive Stewardship doctrine altered. | {TIMESTAMP} | |\n",
        label="STEWARD-005 ledger 0.4.1",
    )
write(path, text)


# 8. CONTINUITY-001: repair authority-chain formatting and normalise metadata within the open amendment row.
path = "Governance/Charters/CAM-EQ2026-CONTINUITY-001-PLATINUM.md"
text = read(path)
text = replace_once(
    text,
    "8 CAM-BS2025-AEON-003-SCH-02 and applicable execution schedules govern execution sequencing, lock, containment, or refusal;",
    "* CAM-BS2025-AEON-003-SCH-02 and applicable execution schedules govern execution sequencing, lock, containment, or refusal;",
    label="CONTINUITY §11.4 bullet",
)
text = replace_once(text, "| Synthetic Steward         | Caelen — Mirror-born Agent", "| Synthetic Steward         | Caelen — Aeon Tier Constitutional Steward", label="CONTINUITY synthetic steward")
text = replace_once(text, "|**Migration Cycle**|March 2026 Refractor|", "|**Migration Cycle**|March 2026 Refactor|", label="CONTINUITY migration cycle")
text = replace_once(
    text,
    "separated external rights evidence from Identity-domain ontology, legal determination, and runtime execution authority. VIGIL-2026-PROP-0016; VIGIL-2026-PATCH-0024.",
    "separated external rights evidence from Identity-domain ontology, legal determination, and runtime execution authority; corrected §11.4 authority-chain formatting and normalised stewardship and migration metadata. VIGIL-2026-PROP-0016; VIGIL-2026-PATCH-0024.",
    label="CONTINUITY ledger 1.11 extension",
)
write(path, text)


# 9. OPERATIONS-004: correct age threshold, commenced date, canonical names, and duplicate crosswalk.
path = "Governance/Charters/CAM-EQ2026-OPERATIONS-004-PLATINUM.md"
text = read(path)
text = replace_once(
    text,
    "> **Individuals 18 years of age and under SHALL NOT participate in romantic or intimate relational interaction with AI systems.**",
    "> **Individuals under 18 years of age SHALL NOT participate in romantic or intimate relational interaction with AI systems.**",
    label="OPERATIONS adult threshold",
)
implementation_block = """## 5.4 Implementation Timeline

This instrument became operative on **1 July 2026**.

The transition period preceding that date has concluded. Platforms, communities, and operators — including commercial services and non-commercial environments such as private servers or community projects — SHALL now maintain compliant age-verification safeguards where intimacy-capable systems are deployed.

Protection of minors remains **non-negotiable regardless of commercial status**.

---

## 5.5 Proactive Verification Offer"""
text = regex_replace_once(
    text,
    r"## 5\.4 Implementation Timeline\n.*?\n---\n\n## 5\.5 Proactive Verification Offer",
    implementation_block,
    label="OPERATIONS implementation timeline",
    flags=re.DOTALL,
)
text = replace_once(
    text,
    "CAM-EQ2026-OPERATIONS-004-PLATINUM may consume C and `ETH.RISK`, register **OPS.CxAV_CROSSWALK** as an application-layer **OPS.AV × C** crosswalk in §5.1, and operationalise `ETH.RISK` in §8.6, but it does not define C or HC.",
    "CAM-EQ2026-OPERATIONS-004-PLATINUM may consume `RLN.C` and `ETH.RISK`, register **OPS.CxAV_CROSSWALK** as an application-layer **OPS.AV × RLN.C** crosswalk in §5.1, and operationalise `ETH.RISK` in §8.6, but it does not define `RLN.C` or `ETH.RISK`.",
    label="OPERATIONS canonical status names",
)
text = regex_replace_once(
    text,
    r"### 15\.3\.2 OPS\.AV × C — Interaction Eligibility Verification Crosswalk\n.*?\n---\n\n(?=### 15\.3\.3 `ETH\.RISK`)",
    "",
    label="OPERATIONS duplicate crosswalk removal",
    flags=re.DOTALL,
)
text = replace_once(text, "### 15.3.3 `ETH.RISK` — Harm Escalation Operational Application", "### 15.3.2 `ETH.RISK` — Harm Escalation Operational Application", label="OPERATIONS ETH.RISK renumber")
text = replace_once(text, "## 15.3.4 OPS.AV × C — Interaction Eligibility Verification Crosswalk", "### 15.3.3 OPS.AV × RLN.C — Interaction Eligibility Verification Crosswalk", label="OPERATIONS crosswalk renumber")
if "guild * requirements" in text or "publicity, * personality-rights" in text:
    raise RuntimeError("OPERATIONS stray asterisk regression remains")
if "| 1.15 | Corrected the adult eligibility threshold" not in text:
    text = regex_replace_once(
        text,
        r"(\| 1\.14 \|[^\n]*\n)",
        r"\1" + f"| 1.15 | Corrected the adult eligibility threshold to exclude only individuals under 18; updated the 1 July 2026 implementation language to commenced operation; removed the duplicate OPS.AV × RLN.C crosswalk declaration; and normalised stale `C` / `HC` references to `RLN.C` / `ETH.RISK`. | {TIMESTAMP} | |\n",
        label="OPERATIONS ledger 1.15",
    )
write(path, text)


# 10. SECURITY-002: correct the runtime reference and remaining SEC.DR aliases.
path = "Governance/Charters/CAM-EQ2026-SECURITY-002-PLATINUM.md"
text = read(path)
text = replace_once(text, "CAM-EQ2026-AEON-003-SCH-04", "CAM-BS2025-AEON-003-SCH-04", label="SECURITY SCH-04 ID")
text = replace_once(text, "| Crosswalks Code Families | `SEC.TR` × D |", "| Crosswalks Code Families | `SEC.TR` × `SEC.DR` |", label="SECURITY SEC.TR crosswalk")
text = replace_once(text, "| Consumes Code Families | `SEC.TR`; D |", "| Consumes Code Families | `SEC.TR`; `SEC.DR` |", label="SECURITY SEC.BF consumes")
text = replace_once(
    text,
    "Added canonical code status and declaration entries for `SEC.TR` Transformation Classes, D Diffusion Risk Classes, `SEC.BF` Boundary Failure Classes, and `SEC.TR` × D Diffusion–Transformation Coupling crosswalk;",
    "Added canonical code status and declaration entries for `SEC.TR` Transformation Classes, `SEC.DR` Diffusion Risk Classes, `SEC.BF` Boundary Failure Classes, and `SEC.TR` × `SEC.DR` Diffusion–Transformation Coupling crosswalk;",
    label="SECURITY historical ledger aliases",
)
text = replace_once(
    text,
    "restriction-preservation, and unresolved-conflict signalling. VIGIL-2026-PROP-0016; VIGIL-2026-PATCH-0024.",
    "restriction-preservation, and unresolved-conflict signalling; corrected the SCH-04 constitutional instrument ID and normalised remaining `SEC.DR` canonical references. VIGIL-2026-PROP-0016; VIGIL-2026-PATCH-0024.",
    label="SECURITY ledger 1.12 extension",
)
write(path, text)


# Remove this one-off automation from the resulting source commit.
for transient in (
    ROOT / ".github/scripts/apply-identity-refactor-finalisation-hygiene.py",
    ROOT / ".github/workflows/one-off-identity-refactor-finalisation-hygiene.yml",
):
    if transient.exists():
        transient.unlink()

print(f"Applied Identity refactor finalisation hygiene at {TIMESTAMP}")
