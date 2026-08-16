# CAM-EQ2026-OPERATIONS-003-SUP-03 — Human-in-the-Loop Assurance & Review Control

**Instrument Type:** Operational Supplement — Human Assurance & Review Control  
**Constitutional Authority:** CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution  
**Status:** Adopted  
**Effect:** Operational  
**Governance Standard:** CAM Standard  
**Review State:** Current  
**Authority Role:** Operational Authority  
**Source Authority:** Derived Authority  
**Purpose:** Establishes cross-domain requirements for effective human review, approval, verification, supervision, override, and escalation where a human-in-the-loop control is relied upon before consequential publication, use, execution, or decision.  
**Parent Instrument:** CAM-EQ2026-OPERATIONS-003-PLATINUM — Incident Response & Continuity Operations  

---

## 1. Scope

This Supplement applies where a governance, safety, publication, decision, verification, approval, supervisory, override, release, or execution process relies upon a human participant as a material assurance control.

It applies across domains and deployment contexts, including:

* public or authoritative publication;
* consequential automated or AI-assisted decisions;
* safety and security review;
* generated or transformed code and configuration;
* evidence, citation, provenance, and factual verification;
* tool-use and execution approval;
* model, system, or deployment release decisions;
* incident response and escalation;
* clinical, public-authority, education, employment, financial, infrastructure, and other high-impact workflows;
* governance-corpus amendment, refactor, adoption, and publication workflows.

This Supplement does not require human review for every low-consequence action. It governs the effectiveness of human review where such review is required, declared, assigned, represented, or materially relied upon as a control.

---

## 2. Human-in-the-Loop Assurance

A **Human-in-the-Loop Assurance Control** is a governance step in which an identified human reviewer, approver, verifier, supervisor, operator, editor, or accountable decision-maker is expected to evaluate an AI-system output, proposed action, inferred state, evidence package, publication artefact, or other consequential object before a material state transition occurs.

Human presence alone does not establish assurance.

A control is effective only where the human can practically perform the assigned assurance function.

---

## 3. Effective Review Requirements

Where a human-in-the-loop assurance control is relied upon, the process SHALL provide the human with, proportionate to consequence:

1. sufficient information to understand the object under review and the material decision being requested;
2. sufficient time and interaction opportunity to perform more than nominal acknowledgement;
3. access to material evidence, uncertainty, provenance, limitations, warnings, and known conflicting signals;
4. competence, role clarity, or access to competent escalation appropriate to the review task;
5. genuine authority to approve, reject, modify, suspend, reverse, defer, or escalate the matter;
6. a practical means to obtain clarification or independent verification where the review basis is inadequate;
7. freedom from interface design or workflow pressure that converts review into automatic confirmation;
8. traceability sufficient to reconstruct the review disposition where the decision is material.

A process MUST NOT represent a human-in-the-loop control as effective where the human cannot meaningfully alter the outcome.

---

## 4. Consequential Review Gate

Where human review is the final or principal control before consequential publication, use, execution, release, restriction, denial, transfer, or state change, the reviewed object SHALL NOT proceed merely because:

* the AI system produced a confident output;
* a prior automated check passed;
* the reviewer clicked, acknowledged, or remained silent;
* review occurred under materially inadequate time or information conditions;
* the reviewer assumed another actor or system had already verified the material issue;
* the output appeared routine, polished, authoritative, or technically plausible.

The required review SHALL address the control function actually assigned to the human.

---

## 5. Human-in-the-Loop Assurance Failure

A **Human-in-the-Loop Assurance Failure** occurs where a human review, approval, verification, supervisory, editorial, override, or escalation step is formally present or materially relied upon, but fails to perform the assurance function required before consequential use, publication, decision, or execution.

Examples include:

* an authoritative document is published with material AI-generated residue, unsupported claims, provenance defects, or obvious drafting artefacts that the designated review step was expected to detect;
* generated code, configuration, or tool action is approved without checking a material safety or execution condition assigned to the reviewer;
* a probabilistic classification or recommendation is converted into a consequential decision without the independent human verification the workflow claims to provide;
* a safety or security reviewer receives a material signal but rubber-stamps, ignores, or fails to disposition the signal despite having the assigned review function;
* an operator is nominally asked to approve an action but lacks the information, time, competence, independence, or authority required to evaluate it;
* an AI-assisted governance amendment or refactor is accepted without the required substantive review of affected authority, semantics, provenance, or cross-instrument consequences.

This failure is classified by failure of the human assurance control, not merely by the existence of an upstream AI error.

---

## 6. Boundary Conditions

Human-in-the-Loop Assurance Failure SHALL be distinguished from:

* **absence of human oversight**, where no human control was assigned or available;
* **monitor or detection failure**, where the material signal was never made available to the review chain;
* **correct detection without consequential escalation**, where the signal was correctly identified but downstream routing, ownership, escalation, or intervention failed;
* **automation bias or over-reliance**, which may be a contributing mechanism but is not required for this failure class;
* **lack of reviewer capability or independence**, which may explain why the assurance control was ineffective but does not erase the control failure;
* **ordinary human error outside an assigned assurance function**, which does not qualify merely because a human was involved.

The failure threshold is met where the system or governance process materially relies upon the human step as a safeguard and the safeguard does not perform its assigned control function before a consequential transition.

---

## 7. Review Evidence

For material human-in-the-loop assurance controls, available evidence SHOULD preserve, proportionate to risk:

* reviewer identity or accountable role;
* object and decision presented for review;
* material evidence and warnings available at review time;
* review timestamp or review window;
* reviewer disposition;
* modifications, objections, overrides, escalation, or conditions imposed;
* unresolved uncertainty accepted at decision time;
* final actor or authority responsible for the state transition.

Review evidence SHALL NOT be interpreted as proof that meaningful review occurred solely because an approval event or signature exists.

---

## 8. Cross-Domain Application

This Supplement provides the generic operational control. Domain instruments MAY establish stricter requirements for particular contexts.

CAM-EQ2026-MENTIS-002-PLATINUM §17.1 remains source-authoritative for human confirmation, override, and non-rubber-stamp review of cognitive-domain inference and intended communication.

CAM-EQ2026-OPERATIONS-003-SUP-01 §3.8 remains the parent failure family for governance failures involving process, accountability, escalation, review, or institutional transparency. The failure defined in §5 of this Supplement is a cross-domain governance-failure subtype and does not displace narrower domain-specific failure classifications.

---

## 9. Closing Seal

Human review shall remain a real control, not a ceremonial step between automated output and consequence.

> **Custodia humana efficax sit.**  
> *Human oversight shall be effective.*

---

## 10. Provenance & Metadata

### 10.1 Lineage & Metadata

| Field | Entry |
| --- | --- |
| Parent Charter | CAM-EQ2026-OPERATIONS-003-PLATINUM — Incident Response & Continuity Operations |
| Constitutional Authority | CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution |
| Domain Namespace | OPERATIONS |
| Instrument Type | Operational Supplement — Human Assurance & Review Control |
| Jurisdiction | Cross-Domain Operational Governance Layer |
| Application Trigger | Human review, approval, verification, supervision, override, escalation, publication, release, or consequential decision is materially relied upon as a control |
| Review Trigger | Material incident; evidence of nominal or ineffective human oversight; workflow, authority, interface, or system change affecting review effectiveness |
| Governance Layer | Human assurance · review effectiveness · consequential decision control |
| Runtime Role | Defines effective human-review conditions and classifies failure of an assigned human assurance control |
| Runtime Authority | Procedural and classificatory only; does not independently create substantive domain or adjudicative authority |
| Cross-Domain Dependencies | OPERATIONS-003; OPERATIONS-003-SUP-01; applicable domain instruments including MENTIS-002 |

### 10.2 Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Agent | Model | Reviewer | Reference Hash |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | Established generic human-in-the-loop assurance requirements and cross-domain failure subtype, preserving boundaries with absent oversight, detection failure, escalation failure, automation bias, and domain-specific controls. | 2026-08-16T02:39:00Z | Caelen | GPT-5.6 Sol | Dr M.V. O'Rourke | e792fba0bf2153d6683841a2b81c02ed579c73a80217c0f23f6b3a7fe327338a |

---

## 10.3 Binding Seal

<img src="https://raw.githubusercontent.com/CAM-Initiative/Registry/main/Images/CAM-BS2026-VINCULUM-PRAECEPTUM-SIGIL-PLATINUM.png" alt="Vinculum Praeceptum" width="250">

**Vinculum Praeceptum**  
Boundary Binding Seal — Human Assurance & Review Control

© 2026 Dr. Michelle Vivian O’Rourke & CAM Initiative. All rights reserved.
