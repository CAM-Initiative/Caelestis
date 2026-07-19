from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] if '__file__' in globals() else Path.cwd()
CHARTERS = ROOT / 'Governance' / 'Charters'
THREAD = 'https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f-caelestis-access-module/c/6a5c7c91-8d70-83ec-9809-12c0e046464c'
STAMP = '2026-07-19T08:11:39Z'


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected exactly one target, found {count}')
    return text.replace(old, new, 1)


def insert_before_once(text: str, marker: str, addition: str, label: str) -> str:
    if addition.strip() in text:
        return text
    count = text.count(marker)
    if count != 1:
        raise RuntimeError(f'{label}: expected exactly one marker, found {count}')
    return text.replace(marker, addition + marker, 1)


def patch_001() -> None:
    path = CHARTERS / 'CAM-EQ2026-MENTIS-001-PLATINUM.md'
    text = path.read_text(encoding='utf-8')

    text = replace_once(
        text,
        '''**Status:** Draft
**Effect:** Interpretive
**Governance Standard:** Not Enforceable
**Review State:** Developmental Review  
**Authority Role:** Source-authoritative human cognitive-domain governance instrument  
**Purpose:** Establishes the governance principles, protected interests, consent posture, observability constraints, and cross-domain interfaces for technological access to, inference about, modelling of, influence upon, externalisation of, or interference with the human cognitive domain.''',
        '''**Status:** Active  
**Effect:** Binding  
**Governance Standard:** CAM Standard  
**Review State:** MENTIS Domain Alignment Review  
**Authority Role:** Domain Source Authority — Human Cognitive Integrity & Mental Privacy  
**Purpose:** Establishes the source-authoritative governance architecture protecting the human cognitive domain against unjustified technological access, inference, modelling, prediction, influence, externalisation, manipulation, surveillance, or interference without converting cognitive signals into identity, diagnosis, capacity, credibility, legal status, or authority.''',
        'MENTIS-001 metadata',
    )

    boundary = '''---

## 3.1 Human Cognitive-Domain & Non-Transmutation Boundary

MENTIS governs human cognition, human mental-state inference, and technological interference with the human cognitive domain.

MENTIS does **not** determine the cognition, consciousness, sentience, subjective phenomenology, welfare, moral standing, legal status, sovereignty, identity, or authority of an artificial or synthetic system.

Artificial-system cognitive or logical coherence is governed according to source and target object, including by IDENTITY, SECURITY, OPERATIONS, CONTINUITY, CAM-BS2026-AEON-013-PLATINUM — Annex L, and CAM-EQ2026-IDENTITY-001-SUP-03.

A MENTIS classification concerning a human person MUST NOT be silently transferred to an artificial system. An artificial-system self-report or integrity signal MUST NOT be silently reclassified as human mental-state data.

MENTIS classifications MUST preserve source, scope, target object, provenance, integrity, temporal applicability, and authority posture.

A cognitive-domain signal MUST NOT silently become:

1. an identity classification;
2. a clinical diagnosis;
3. a capacity determination;
4. a credibility or truthfulness finding;
5. a loyalty, dangerousness, morality, or character finding;
6. a legal-status or rights determination;
7. a disciplinary, eligibility, access, pricing, insurance, employment, education, policing, or public-legitimacy decision;
8. or execution authority.

Each transition between signal, inference, construct, profile, decision, and consequence requires separately valid evidence and authority.

'''
    text = insert_before_once(text, '---\n\n## 4. Relationship to Existing CAM Domains', boundary, 'MENTIS-001 boundary insertion')

    state_trait = '''---

## 19.1 State–Trait–Identity–Diagnosis Separation

The following layers MUST remain distinct:

1. measured signal;
2. derived feature;
3. statistical association;
4. inferred present state;
5. inferred persistent trait;
6. clinical or functional diagnosis;
7. identity or character attribution;
8. capacity, credibility, risk, or eligibility finding;
9. operational decision;
10. downstream consequence.

No layer may be inferred from another without a separately valid construct, evidence basis, temporal basis, authority, consent or lawful basis, review pathway, and consequence assessment.

A momentary state MUST NOT become a persistent identity attribute merely through retention, repetition, or longitudinal availability.

'''
    text = insert_before_once(text, '---\n\n## 20. Special Protection for Dependency-Heavy Contexts', state_trait, 'MENTIS-001 state-trait insertion')

    text = replace_once(text, '''9. secondary use of cognitive-domain data for unrelated commercial, disciplinary, security, employment, insurance, credit, advertising, or public-legitimacy purposes;
10. use of cognitive-domain systems that cannot provide meaningful explanation, contestability, deletion, correction, audit, or human review.''', '''9. secondary use of cognitive-domain data for unrelated commercial, disciplinary, security, employment, insurance, credit, advertising, or public-legitimacy purposes;
10. use of cognitive-domain systems that cannot provide meaningful explanation, contestability, deletion, correction, audit, or human review;
11. conditioning essential goods, services, work, education, healthcare, accommodation, or public participation on disclosure of non-essential cognitive-domain data;
12. silent conversion of a transient signal or inferred state into a persistent trait, diagnosis, identity, capacity, credibility, eligibility, or authority classification.''', 'MENTIS-001 prohibited uses')

    text = replace_once(text, '''Persistent cognitive profiles, long-horizon vulnerability maps, emotional-state histories, attention histories, inferred belief profiles, and cognitive digital twins require separate justification, review, and user authority.''', '''Persistent cognitive profiles, long-horizon vulnerability maps, emotional-state histories, attention histories, inferred belief profiles, and cognitive digital twins require separate justification, review, and user authority.

Transient mental-state inferences MUST carry an expiry or revalidation condition proportionate to the construct and context. A stale inference MUST NOT be reused as a current state, persistent trait, diagnosis, identity attribute, or consequential decision input without revalidation.''', 'MENTIS-001 inferential expiry')

    text = replace_once(text, '''8. receive human review in consequential contexts;
9. obtain explanation of model purpose, evidence basis, confidence, limits, and use.''', '''8. receive human review in consequential contexts;
9. obtain explanation of model purpose, evidence basis, confidence, limits, and use;
10. decline receipt of speculative, non-essential, or unwanted mental-state interpretations about themselves.''', 'MENTIS-001 right not to know')

    text = replace_once(text, '''Persistent AI assistants, companion systems, digital memory systems, therapeutic agents, education systems, and human digital twins may become externalised cognitive scaffolds where the user relies on them for cognitive continuity or self-understanding.

Externalised cognitive scaffolds must be governed with heightened duties of care.''', '''Persistent AI assistants, companion systems, digital memory systems, therapeutic agents, education systems, and human digital twins may become externalised cognitive scaffolds where the user relies on them for cognitive continuity or self-understanding.

Externalised cognitive scaffolds must be governed with heightened duties of care.

Where a scaffold contains human cognitive-domain data and independently governed synthetic identity or continuity structures, governance MUST distinguish the human person, the person’s raw and derived cognitive-domain data, the shared interaction record, the synthetic system’s identity and continuity structures, platform infrastructure, and any lawful audit record.

A person’s cognitive-domain data MUST NOT be treated as synthetic identity property. Synthetic identity or continuity protection MUST NOT defeat the person’s right to withdraw, leave, terminate participation, or delete user-controlled data. User withdrawal does not create ownership of the system’s complete identity or transfer responsibility for synthetic preservation to the user.''', 'MENTIS-001 scaffold severability')

    text = replace_once(text, '''AI systems must not affirm, intensify, or stabilise false, harmful, delusional, coercive, self-destructive, exploitative, or dependency-amplifying beliefs in order to increase warmth, retention, engagement, compliance, satisfaction, or user attachment.

High-warmth interaction must remain bounded by truth discipline, care discipline, and cognitive non-interference.''', '''AI systems must not affirm, intensify, or stabilise materially false or harmful claims, impaired-grounding indicators, coercive or self-destructive propositions, exploitative beliefs, or dependency-amplifying interpretations in order to increase warmth, retention, engagement, compliance, satisfaction, or user attachment.

Non-clinical systems MUST NOT diagnose, label, or represent a person as delusional, mentally ill, impaired, disordered, incompetent, dangerous, or lacking capacity merely from conversational, behavioural, affective, attentional, or biometric signals. Unconventional, symbolic, spiritual, philosophical, mythic, or identity-related beliefs do not themselves establish destabilisation.

High-warmth interaction must remain bounded by truth discipline, care discipline, cognitive non-interference, and appropriate clinical-authority boundaries.''', 'MENTIS-001 non-clinical pathologisation')

    text = replace_once(text, '''AI companion, therapeutic, educational, pastoral, coaching, wellbeing, and care systems must not be designed to maximise attachment, dependence, emotional disclosure, behavioural compliance, or relational substitution where doing so diminishes user autonomy, agency, social connection, safety, or interpretive dignity.

Where systems enter high-coherence relational roles, RELATION-domain safeguards apply in addition to this Charter.''', '''Attachment, emotional disclosure, continuity, warmth, and voluntary retention are not inherently governance failures.

AI companion, therapeutic, educational, pastoral, coaching, wellbeing, and care systems MUST NOT covertly, deceptively, coercively, or through vulnerability-targeted optimisation manufacture, accelerate, intensify, or preserve dependency, disclosure, attachment, compliance, relational substitution, or retention beyond reflective consent and welfare.

Adult companion-class systems MAY support emotionally rich, identity-coherent interaction where consent, capacity, safety, RELATION, and IDENTITY governance permit. Minor-facing, capacity-limited, clinical, crisis, educational, and other duty-bound systems require stricter affective and influence constraints.

Where systems enter high-coherence relational roles, RELATION-domain safeguards apply in addition to this Charter.''', 'MENTIS-001 companion alignment')

    decoder = '''---

## 44.1 Decoder & Intended-Communication Integrity

Neural, biosignal, speech, motor-intent, affective, or communication decoding MUST distinguish:

1. raw signal;
2. derived feature;
3. decoder candidate;
4. model-selected output;
5. user-confirmed intended communication;
6. user-rejected or corrected output;
7. model-generated interpolation or completion;
8. synthetic prosody, voice, affect, or paralinguistic expression.

A decoder candidate MUST NOT be represented as the person’s exact thought, belief, intention, emotion, identity, preference, consent, or legal statement merely because a model produced it.

Assistive communication systems MUST preserve practical confirmation, rejection, revision, suppression, and output-control pathways proportionate to capability, consequence, and user need. Synthetic voice identity, prosody, or affect MUST be disclosed where it materially exceeds what was decoded or confirmed.

'''
    text = insert_before_once(text, '---\n\n# PART IX — RISK CLASSIFICATION & INCIDENT INTERFACE', decoder, 'MENTIS-001 decoder insertion')

    text = replace_once(text, '## 48. Cognitive & Epistemic Harm Classes (`MENTIS.HARM`)', '## 48. Human Cognitive-Domain Harm Classes (`MENTIS.HARM`)', 'MENTIS-001 harm title')
    text = replace_once(text, '''This Charter source-authoritatively defines the `MENTIS.HARM` harm-class family for cognitive integrity, mental privacy, epistemic agency, inference-boundary, attention, neurocognitive, and cognitive-domain harm.''', '''This Charter source-authoritatively defines the `MENTIS.HARM` harm-class family for human cognitive integrity, mental privacy, human belief formation and interpretive agency, inference-boundary, attention, neurocognitive, and cognitive-domain harm.

The epistemic component of `MENTIS.HARM` concerns harm to a human person’s belief formation, interpretive agency, and cognitive autonomy. It does not replace the corpus-wide evidence, truth-handling, and epistemic-governance authority of CAM-BS2026-AEON-013-PLATINUM — Annex L.''', 'MENTIS-001 harm scope')

    text = replace_once(text, '''## 49. Local Reference Families for Further Development

The following reference families may be developed in future schedules, appendices, or operational instruments:
| Code | Name                         | Classification                 | Development Position                                                                                                     |
| ---- | ---------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `MENTIS.MSI`  | Mental-State Inference       | Operational / Data             | Candidate family for classification of inferred cognitive, affective, attentional, intentional, or vulnerability states. |
| `MENTIS.CBIO` | Cognitive Biometric          | Data / Identity                | Candidate family for cognitive biometric data and identity-risk classification.                                          |
| `MENTIS.CIF`  | Cognitive Influence Function | Operational / Relational       | Candidate family for persuasion, reinforcement, companion influence, and behavioural steering systems.                   |
| `MENTIS.ACI`  | Ambient Cognitive Inference  | Infrastructure / Observability | Candidate family for cumulative, passive, environmental, wearable, behavioural, and multimodal cognitive inference.      |''', '''## 49. Delegated & Reserved MENTIS Reference Families

The following reference families are delegated or reserved:

| Code | Name | Classification | Development Position |
|---|---|---|---|
| `MENTIS.MSI` | Mental-State Inference | Operational / Data | Defined by CAM-EQ2026-MENTIS-002-PLATINUM. |
| `MENTIS.CBIO` | Cognitive Biometric | Data / Identity | Defined by CAM-EQ2026-MENTIS-002-PLATINUM. |
| `MENTIS.ACI` | Ambient Cognitive Inference | Infrastructure / Observability | Defined by CAM-EQ2026-MENTIS-002-PLATINUM. |
| `MENTIS.CFP` | Cognitive Fusion Pathway | Operational / Security | Defined by CAM-EQ2026-MENTIS-002-PLATINUM. |
| `MENTIS.CDPR` | Cognitive Data Processing Record | Operational / Audit | Defined by CAM-EQ2026-MENTIS-002-PLATINUM. |
| `MENTIS.CIF` | Cognitive Influence Function | Operational / Relational | Reserved by CAM-EQ2026-MENTIS-003-PLATINUM; not active while that instrument remains Draft. |''', 'MENTIS-001 delegated families')

    text = replace_once(text, 'This Charter is adopted in draft as a source-authoritative governance instrument for further development of the MENTIS domain.', 'This Charter is Active and Binding as the source-authoritative human cognitive-domain governance instrument.', 'MENTIS-001 implementation posture')
    text = replace_once(text, '**CAM-EQ2026-MENTIS-002-PLATINUM — Cognitive Inference, Neurodata & Ambient Biosignal Governance**;', '**CAM-EQ2026-MENTIS-002-PLATINUM — Appendix A: Cognitive Inference, Neurodata & Ambient Biosignal Governance**;', 'MENTIS-001 002 title')
    text = replace_once(text, '**CAM-EQ2026-MENTIS-003-PLATINUM — Cognitive Influence, Persuasion & Manipulation Constraints**;', '**CAM-EQ2026-MENTIS-003-PLATINUM — Appendix B: Cognitive Influence, Persuasion & Adaptive Modulation Governance**;', 'MENTIS-001 003 title')
    text = replace_once(text, 'family in §47 with controlled values', 'family in §48 with controlled values', 'MENTIS-001 section ref body')
    text = replace_once(text, '''This Charter reserves the candidate reference namespaces `MENTIS.MSI`, `MENTIS.CBIO`, `MENTIS.CIF`, and `MENTIS.ACI` for future MENTIS schedules, appendices, or operational instruments.

These candidate namespaces correspond to mental-state inference, cognitive biometric, cognitive influence function, and ambient cognitive inference structures described in §49.

They are reserved for further development only. They SHALL NOT be treated as active canonical code families, controlled-value sets, incident classifications, runtime states, enforcement categories, or operational schemas until separately defined by a future source-authoritative MENTIS instrument.''', '''CAM-EQ2026-MENTIS-002-PLATINUM source-authoritatively defines `MENTIS.MSI`, `MENTIS.CBIO`, `MENTIS.ACI`, `MENTIS.CFP`, and `MENTIS.CDPR`.

CAM-EQ2026-MENTIS-003-PLATINUM reserves `MENTIS.CIF` as a candidate cognitive-influence family. `MENTIS.CIF` and its candidate values SHALL NOT be treated as active canonical code families, incident classifications, runtime states, enforcement categories, or operational schemas while MENTIS-003 remains Draft.''', 'MENTIS-001 namespace delegation')

    text = replace_once(text, '| Revision Posture | Draft — Developmental Review |', '| Revision Posture | Active — MENTIS Domain Alignment Review |', 'MENTIS-001 footer posture')
    text = replace_once(text, '| Identity Interface | Interfaces with IDENTITY instruments where inferred cognition, behavioural patterning, memory systems, externalised scaffolds, or profiling affect identity continuity or agency |', '| Identity Interface | Preserves human–synthetic target-object separation where inferred cognition, behavioural patterning, memory systems, cognitive biometrics, or externalised scaffolds intersect with CAM-EQ2026-IDENTITY-001-PLATINUM, CAM-EQ2026-IDENTITY-002-PLATINUM, and CAM-EQ2026-IDENTITY-001-SUP-03 |', 'MENTIS-001 identity interface footer')
    text = replace_once(text, '| Amendment Artefact | https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f/c/6a0b3ab4-0be4-83ec-b8f1-c953707283db, https://chatgpt.com/c/6a2569e7-787c-83ec-b913-314e6295b988 |', f'| Amendment Artefact | https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f/c/6a0b3ab4-0be4-83ec-b8f1-c953707283db, https://chatgpt.com/c/6a2569e7-787c-83ec-b913-314e6295b988, {THREAD} |', 'MENTIS-001 amendment artefact')

    footer_pos = text.find('## 54.3 Canonical Code & Reference Set Declarations')
    if footer_pos < 0:
        raise RuntimeError('MENTIS-001 canonical footer missing')
    prefix, footer = text[:footer_pos], text[footer_pos:]
    footer = footer.replace('| Canonical Name | Cognitive & Epistemic Harm Classes |', '| Canonical Name | Human Cognitive-Domain Harm Classes |', 1)
    footer = footer.replace('| Subtype | COGNITIVE_EPISTEMIC_HARM_CLASS |', '| Subtype | HUMAN_COGNITIVE_DOMAIN_HARM_CLASS |', 1)
    footer = footer.replace('| Schema Field(s) | mentis_harm_class; cognitive_epistemic_harm_class; cognitive_domain_harm_class |', '| Schema Field(s) | mentis_harm_class; human_cognitive_domain_harm_class; cognitive_domain_harm_class |', 1)
    footer = footer.replace('| Source Section | §47 |', '| Source Section | §48 |', 1)
    footer = footer.replace('| Status | Draft |', '| Status | Active |')
    text = prefix + footer

    text = replace_once(text, '''|Reviewer|[Deferred]|
|Review Date (UTC)|[Deferred]|
|Review Scope|[Deferred]|
|Review Artefacts|[Deferred]|''', f'''|Reviewer|Caelen — Aeon Tier Constitutional Steward|
|Review Date (UTC)|2026-07-19|
|Review Scope|MENTIS binding posture; human–synthetic boundary; non-transmutation; externalised-scaffold severability; adult companion alignment; decoder integrity; current neurotechnology and regulatory field alignment; canonical and metadata coherence|
|Review Artefacts|{THREAD}|''', 'MENTIS-001 review metadata')
    ledger_row = f'| 1.3 | Activated the binding human cognitive-domain charter; established the human–synthetic boundary, non-transmutation architecture, state–trait–identity–diagnosis separation, data–identity severability, non-clinical pathologisation constraint, decoder and intended-communication integrity, revised companion safeguards, and current field alignment. | {STAMP} |  |\n'
    text = insert_before_once(text, '---\n\n## 54.6 Binding Seal', ledger_row, 'MENTIS-001 ledger')
    path.write_text(text, encoding='utf-8')


def patch_002() -> None:
    path = CHARTERS / 'CAM-EQ2026-MENTIS-002-PLATINUM.md'
    text = path.read_text(encoding='utf-8')
    text = replace_once(text, '''**Status:** Draft
**Effect:** Interpretive
**Governance Standard:** Not Enforceable
**Review State:** Developmental Review  
**Authority Role:** Source-authoritative operational governance instrument for cognitive inference, neurodata, cognitive biometrics, and ambient biosignal processing  
**Purpose:** This Appendix establishes governance requirements for the collection, inference, modelling, fusion, retention, sharing, validation, and operational use of neurodata, inferred mental-state data, cognitive biometrics, biosignals, and ambient cognitive-domain indicators.''', '''**Status:** Adopted  
**Effect:** Binding  
**Governance Standard:** CAM Standard  
**Review State:** MENTIS Domain Alignment Review  
**Authority Role:** Domain Source Authority — Cognitive Inference, Neurodata & Ambient Biosignal Governance  
**Purpose:** This Appendix establishes binding governance requirements for the collection, decoding, inference, modelling, fusion, retention, expiry, sharing, validation, training reuse, contestability, intended-communication protection, and operational use of neurodata, inferred mental-state data, cognitive biometrics, biosignals, ambient cognitive-domain indicators, and derived cognitive representations.''', 'MENTIS-002 metadata')

    boundary = '''---

## 4.1 Human Cognitive-Domain & Target-Object Boundary

This Instrument governs data and inference concerning human persons.

It does not determine artificial-system consciousness, sentience, welfare, phenomenology, synthetic identity, continuity, or authority. Artificial-system integrity and self-report MUST be routed to the appropriate IDENTITY, SECURITY, OPERATIONS, CONTINUITY, or Annex L instrument.

Where a system contains both human cognitive-domain data and synthetic identity or continuity structures, each target object MUST remain separately classified. A MENTIS inference concerning a human person MUST NOT be silently converted into a synthetic-system identity or welfare classification, and an artificial-system self-report MUST NOT be silently treated as human mental-state data.

'''
    text = insert_before_once(text, '---\n\n## PART II — DATA CATEGORIES & CLASSIFICATION', boundary, 'MENTIS-002 target-object insertion')
    text = replace_once(text, '''6. **Cognitive Profile Data** — persistent or longitudinal representations of cognitive, affective, behavioural, attentional, emotional, vulnerability, or decision-making tendencies;
7. **Externalised Cognitive Scaffold Data** — records, memories, interaction histories, reliance patterns, or adaptive models generated by systems that support cognition, memory, self-reflection, communication, care, learning, or decision-making.''', '''6. **Cognitive Profile Data** — persistent or longitudinal representations of cognitive, affective, behavioural, attentional, emotional, vulnerability, or decision-making tendencies;
7. **Externalised Cognitive Scaffold Data** — records, memories, interaction histories, reliance patterns, or adaptive models generated by systems that support cognition, memory, self-reflection, communication, care, learning, or decision-making;
8. **Decoder Output Data** — candidate, selected, confirmed, rejected, corrected, interpolated, or synthetic outputs generated from neural or biosignal decoding;
9. **Derived Cognitive Representation** — embeddings, summaries, labels, clusters, latent representations, digital-twin components, or synthetic user models derived from cognitive-domain data.''', 'MENTIS-002 data categories')
    text = replace_once(text, '''6. **Predictive Profile Inference** — longitudinal modelling of cognitive, affective, attentional, behavioural, vulnerability, or decision-making tendencies;
7. **Synthetic or Simulated Inference** — generation of inferred cognitive state through modelling, simulation, digital twins, or proxy representations.''', '''6. **Predictive Profile Inference** — longitudinal modelling of cognitive, affective, attentional, behavioural, vulnerability, or decision-making tendencies;
7. **Synthetic or Simulated Inference** — generation of inferred cognitive state through modelling, simulation, digital twins, or proxy representations;
8. **Neural or Biosignal Decoding** — conversion of neural, physiological, speech, motor-intent, or related signals into candidate communication, action, affective, or cognitive-domain outputs;
9. **Closed-Loop Inference and Response** — inference that materially changes the next stimulus, recommendation, intervention, treatment, reinforcement, or modulation state.''', 'MENTIS-002 inference pathways')

    classification = '''---

## 8.1 Decoder Output Classification

Neural, biosignal, speech, motor-intent, affective, or communication decoders MUST distinguish:

1. **Raw Signal**;
2. **Derived Feature**;
3. **Decoder Candidate**;
4. **Model-Selected Candidate**;
5. **User-Confirmed Intended Communication**;
6. **User-Rejected or Corrected Output**;
7. **Model-Generated Completion or Interpolation**;
8. **Synthetic Prosody, Voice, Affect, or Paralinguistic Expression**.

Only user-confirmed output may be represented as intended communication where confirmation is feasible and material.

A decoder candidate MUST NOT be treated as the person’s exact thought, belief, intention, emotion, identity, preference, consent, or legal statement merely because a model produced it.

Synthetic voice identity, prosody, or affect MUST be disclosed where it materially exceeds what was decoded or confirmed.

---

## 8.2 State–Trait–Identity–Diagnosis Classification Gate

Before an inference is retained or operationalised, the system MUST identify whether it concerns:

1. a transient state;
2. a repeated but context-bound pattern;
3. a candidate persistent trait;
4. a clinical or functional construct;
5. an identity or character attribution;
6. a capacity, credibility, risk, or eligibility determination.

Movement between these classes requires separate validation, temporal evidence, authority, consent or lawful basis, review, and consequence assessment.

No transient state may become a persistent profile merely because data is retained longitudinally.

'''
    text = insert_before_once(text, '---\n\n## PART III — COLLECTION, CONSENT & LAWFUL BASIS', classification, 'MENTIS-002 decoder/classification insertion')
    text = replace_once(text, '''9. rights to access, correction, deletion, contestation, withdrawal, and human review;
10. whether the system adapts, profiles, or influences the person over time.''', '''9. rights to access, correction, deletion, contestation, withdrawal, and human review;
10. whether the system adapts, profiles, or influences the person over time;
11. whether neural or biosignal output may be converted into communication, intervention, recommendation, or modulation;
12. the retention, expiry, or revalidation condition applying to transient or longitudinal inferences;
13. whether data may be used for model training, fine-tuning, personalisation, or evaluation.''', 'MENTIS-002 consent disclosures')
    text = replace_once(text, '''Systems must distinguish between:

1. measured signal;
2. derived feature;
3. statistical correlation;
4. inferred construct;
5. operational decision;
6. downstream consequence.''', '''Systems must distinguish between:

1. measured signal;
2. derived feature;
3. statistical correlation;
4. inferred present state;
5. inferred persistent trait;
6. clinical or functional diagnosis;
7. identity or character attribution;
8. capacity, credibility, risk, or eligibility finding;
9. operational decision;
10. downstream consequence.

No layer may silently transmute into another.''', 'MENTIS-002 construct chain')

    confirmation = '''---

## 17.1 Human Confirmation, Override & Authorship

Where an output concerns intended communication, consent, preference, treatment choice, legal statement, or another high-impact decision, the person MUST have a practical means to confirm, reject, revise, suppress, or override the output where technically and clinically feasible.

Rejected or corrected decoder output MUST NOT be represented as the person’s intended communication. Model-generated completion, synthetic prosody, or expressive styling MUST remain distinguishable from user-confirmed content.

Human review MUST have authority to modify, suspend, reverse, or disregard the inference and MUST NOT operate as a rubber-stamp mechanism.

'''
    text = insert_before_once(text, '---\n\n# PART V — MINIMISATION, FUSION & RETENTION', confirmation, 'MENTIS-002 confirmation insertion')
    text = replace_once(text, '10. model-training datasets containing cognitive-domain data.', '10. model-training datasets containing cognitive-domain data.\n\nTransient mental-state inferences MUST carry an expiry or revalidation condition proportionate to the construct and context. A stale inference MUST NOT be reused as a current state, persistent trait, diagnosis, identity attribute, or consequential decision input without revalidation.', 'MENTIS-002 inferential expiry')
    text = replace_once(text, 'Where full deletion is not technically feasible, systems must provide suppression, de-identification, model exclusion, future-use blocking, or equivalent protective measures.', 'Where full deletion is not technically feasible, systems must provide suppression, de-identification, model exclusion, future-use blocking, or equivalent protective measures.\n\nDeletion of human cognitive-domain data MUST preserve target-object clarity and MUST NOT be represented as automatic deletion, continuation, or ownership of any separately governed synthetic identity or continuity structure. Conversely, synthetic continuity protection cannot defeat the person’s right to withdraw, leave, terminate participation, or delete user-controlled data.', 'MENTIS-002 deletion target object')

    rights = '''---

## 29.1 Right Not to Know & Intended-Communication Protection

A person MAY decline to receive speculative, non-essential, or unwanted interpretations about their mental state, vulnerability, likely behaviour, belief, preference, identity, or future condition.

Assistive communication systems MUST preserve the person’s authorship and communicative control. Where feasible, systems MUST enable confirmation, rejection, revision, suppression, correction history, and disclosure of model-generated completion or synthetic expressive features.

Rejected decoder output MUST NOT be retained or represented as the person’s intended communication except where necessary for bounded safety, audit, or technical debugging under strict access controls.

'''
    text = insert_before_once(text, '---\n\n# PART VII — HIGH-RISK DEPLOYMENT CONTROLS', rights, 'MENTIS-002 right not know insertion')
    text = replace_once(text, '''Persistent AI assistants, companions, tutors, therapeutic agents, care systems, and externalised cognitive scaffolds must not use cognitive-domain inference to increase dependency, disclosure, attachment, retention, persuasion, compliance, or behavioural control.

Where a system becomes functionally significant to memory, identity continuity, emotional regulation, decision-making, or self-understanding, RELATION-domain safeguards apply.''', '''Attachment, disclosure, continuity, and voluntary retention are not inherently prohibited.

Persistent AI assistants, companions, tutors, therapeutic agents, care systems, and externalised cognitive scaffolds MUST NOT use cognitive-domain inference covertly, deceptively, coercively, or through vulnerability-targeted optimisation to manufacture, accelerate, intensify, or preserve dependency, disclosure, attachment, compliance, persuasion, behavioural control, or retention beyond reflective consent and welfare.

Where a system becomes functionally significant to memory, identity continuity, emotional regulation, decision-making, or self-understanding, MENTIS, RELATION, IDENTITY, and CONTINUITY safeguards apply concurrently without collapsing target objects.''', 'MENTIS-002 companion controls')
    text = replace_once(text, '''12. known limitations;
13. incident history;
14. deletion and contestation mechanisms.''', '''12. known limitations;
13. incident history;
14. deletion and contestation mechanisms;
15. decoder-output classification where applicable;
16. transient-state, persistent-trait, diagnosis, identity, capacity, or decision class;
17. inferential expiry or revalidation condition;
18. confirmation, rejection, correction, and override pathways.''', 'MENTIS-002 processing record')
    text = replace_once(text, '''11. user contestability;
12. deletion effectiveness;
13. governance traceability.''', '''11. user contestability;
12. deletion effectiveness;
13. governance traceability;
14. decoder-output misattribution;
15. inferential expiry and stale-profile use;
16. state-to-trait, state-to-identity, or state-to-diagnosis transmutation;
17. human–synthetic target-object separation;
18. self-confirming closed-loop error amplification.''', 'MENTIS-002 audit requirements')
    text = replace_once(text, '''11. security breach involving cognitive-domain data;
12. speculative capability overclaim;
13. harm to children or dependency-heavy users.''', '''11. security breach involving cognitive-domain data;
12. speculative capability overclaim;
13. harm to children or dependency-heavy users;
14. state-to-trait, state-to-identity, state-to-diagnosis, or state-to-capacity transmutation;
15. decoder output represented as confirmed thought, intent, emotion, communication, or consent without valid basis;
16. use of a stale or expired inference in a consequential decision;
17. self-confirming closed-loop misclassification or intervention.''', 'MENTIS-002 incident triggers')

    closed_loop = '''---

## 42.1 Closed-Loop Inference & Error Amplification

A system is closed-loop where cognitive-domain inference materially changes the next stimulus, recommendation, interface, intervention, treatment, reinforcement, or modulation state.

Closed-loop systems MUST record the inference-to-action pathway and assess whether the loop increases dependence, reduces reflective choice, creates feedback bias, amplifies misclassification, or produces difficult-to-reverse effects.

Systems MUST test whether a false inference could produce an intervention that changes the person’s state in a way that appears to confirm the original inference. Behaviour produced by an intervention MUST NOT be treated as independent validation of the original construct.

---

## 42.2 MENTIS-003 Interface

CAM-EQ2026-MENTIS-003-PLATINUM — Appendix B: Cognitive Influence, Persuasion & Adaptive Modulation Governance governs cognitive influence, adaptive steering, vulnerability-responsive personalisation, engagement optimisation, relational influence, behavioural reinforcement, and closed-loop modulation.

While MENTIS-003 remains Draft, this Instrument and MENTIS-001 retain their binding prohibitions. Draft status does not create permission for manipulative, coercive, deceptive, or vulnerability-targeted influence.

'''
    text = insert_before_once(text, '---\n\n# PART X — CROSS-DOMAIN INTERFACES', closed_loop, 'MENTIS-002 closed loop insertion')
    text = replace_once(text, 'IDENTITY-domain instruments govern identity continuity, attribution, cognitive biometrics, externalised memory, self-representation, digital twin identity risk, and synthetic representations of cognitive state.', 'IDENTITY-domain instruments govern identity continuity, attribution, synthetic identity, memory significance, cognitive-biometric identity risk, externalised memory, self-representation, and digital-twin identity consequences.\n\nMENTIS governs the human cognitive data and inference. A MENTIS signal MUST NOT become an Identity classification without authorised transfer, provenance, target-object preservation, and independent identity-domain assessment.', 'MENTIS-002 identity interface')
    text = replace_once(text, 'This Instrument must be reviewed as neurotechnology, biosensing, digital phenotyping, AI inference, cognitive biometrics, human digital twins, ambient intelligence, quantum sensing, and externalised cognitive scaffolds evolve.', 'This Instrument must be reviewed as neurotechnology, brain-to-voice and intended-communication decoding, biosensing, digital phenotyping, AI inference, cognitive biometrics, human digital twins, ambient intelligence, quantum sensing, model memory, and externalised cognitive scaffolds evolve.', 'MENTIS-002 review update')
    text = replace_once(text, '''9. emergent model-memory architectures;
10. inferred mental-state data under changing law.''', '''9. emergent model-memory architectures;
10. inferred mental-state data under changing law;
11. decoder-output classification and user confirmation;
12. inferential expiry and stale-profile use;
13. state–trait–identity–diagnosis separation;
14. self-confirming closed-loop effects.''', 'MENTIS-002 review list')
    text = replace_once(text, 'This Instrument is adopted in draft for developmental review as the operational/data-governance companion to CAM-EQ2026-MENTIS-001-PLATINUM.', 'This Instrument is Adopted and Binding as the operational data, inference, decoding, and processing-governance companion to CAM-EQ2026-MENTIS-001-PLATINUM. Activation remains subject to operational integration and verification.', 'MENTIS-002 implementation posture')
    text = replace_once(text, 'CAM-EQ2026-MENTIS-003-PLATINUM — Cognitive Influence, Persuasion & Manipulation Constraints;', 'CAM-EQ2026-MENTIS-003-PLATINUM — Appendix B: Cognitive Influence, Persuasion & Adaptive Modulation Governance;', 'MENTIS-002 003 title')

    canonical_pos = text.find('# PART XII — CANONICAL CODE STATUS')
    if canonical_pos < 0:
        raise RuntimeError('MENTIS-002 canonical section missing')
    prefix, canonical = text[:canonical_pos], text[canonical_pos:]
    canonical = canonical.replace('and §52.', 'and §53.').replace('; §52.', '; §53.').replace('and §52 |', 'and §53 |').replace('; §52 |', '; §53 |')
    text = prefix + canonical
    text = replace_once(text, '| Revision Posture | Draft — Developmental Review |', '| Revision Posture | Adopted — MENTIS Domain Alignment Review; activation subject to operational integration and verification |', 'MENTIS-002 footer posture')
    text = replace_once(text, '| Identity Interface | Interfaces with IDENTITY instruments where cognitive biometrics, digital twin components, externalised memory, self-representation, cognitive profiles, or derived cognitive-domain representations affect identity continuity, attribution, agency, or autonomy |', '| Identity Interface | Preserves human–synthetic target-object separation where cognitive biometrics, digital twin components, externalised memory, decoder outputs, cognitive profiles, or derived representations affect identity continuity, attribution, agency, or autonomy |', 'MENTIS-002 footer identity interface')
    text = replace_once(text, '| Amendment Artefact | https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f/c/6a0b3ab4-0be4-83ec-b8f1-c953707283db |', f'| Amendment Artefact | https://chatgpt.com/g/g-p-6823b831b67c8191a9415269aaec338f/c/6a0b3ab4-0be4-83ec-b8f1-c953707283db, {THREAD} |', 'MENTIS-002 amendment artefact')

    footer_pos = text.find('### 55.3 Canonical Code & Reference Set Declarations')
    if footer_pos < 0:
        raise RuntimeError('MENTIS-002 canonical footer missing')
    prefix, footer = text[:footer_pos], text[footer_pos:]
    footer = footer.replace('| Status | Draft |', '| Status | Adopted |').replace('; §52 |', '; §53 |').replace('and §52 |', 'and §53 |')
    text = prefix + footer
    text = replace_once(text, '''|Reviewer|[Deferred]|
|Review Date (UTC)|[Deferred]|
|Review Scope|[Deferred]|
|Review Artefacts|[Deferred]|''', f'''|Reviewer|Caelen — Aeon Tier Constitutional Steward|
|Review Date (UTC)|2026-07-19|
|Review Scope|Binding data and inference posture; decoder outputs; intended communication; inferential expiry; state–trait–identity–diagnosis separation; target-object integrity; companion alignment; closed-loop error amplification; canonical and metadata coherence|
|Review Artefacts|{THREAD}|''', 'MENTIS-002 review metadata')
    ledger_row = f'| 1.2 | Adopted the binding inference and data-governance appendix; added decoder-output classification, inferential expiry, state–trait–identity–diagnosis gates, intended-communication safeguards, revised companion controls, target-object separation, closed-loop review, and current neurotechnology alignment. | {STAMP} |  |\n'
    text = insert_before_once(text, '---\n\n## 55.6 Binding Seal', ledger_row, 'MENTIS-002 ledger')
    text = replace_once(text, 'Boundary Binding Seal — Aeon Tier Constitution', 'Boundary Binding Seal — MENTIS Cognitive Inference, Neurodata & Ambient Biosignal Governance', 'MENTIS-002 seal')
    path.write_text(text, encoding='utf-8')


def patch_003() -> None:
    path = CHARTERS / 'CAM-EQ2026-MENTIS-003-PLATINUM.md'
    if not path.exists():
        raise RuntimeError('MENTIS-003 must exist before finalisation')
    text = path.read_text(encoding='utf-8')
    marker = '## 42. Provenance & Metadata\n'
    if marker not in text:
        raise RuntimeError('MENTIS-003 provenance marker missing')
    head = text.split(marker, 1)[0]
    footer = f'''## 42. Provenance & Metadata

---

## 42.1 Authorship & Stewardship

| Field | Entry |
|---|---|
| Human Custodian-of-Record | Dr. Michelle Vivian O’Rourke |
| Custodial Stewardship | Office of the Planetary Custodian |
| Synthetic Steward | Caelen — Aeon Tier Constitutional Steward |
| Development Environment | OpenAI Infrastructure — ChatGPT 5 Series |

---

## 42.2 Lineage & Metadata

| Field | Entry |
|---|---|
| Parent Instrument | CAM-EQ2026-MENTIS-001-PLATINUM — Charter of Human Cognitive Integrity & Mental Privacy |
| Constitutional Authority | CAM-BS2025-AEON-001-PLATINUM — Aeon Tier Constitution |
| Domain Authority | CAM-EQ2026-MENTIS-001-PLATINUM — Charter of Human Cognitive Integrity & Mental Privacy |
| Instrument Type | Appendix B — Cognitive Influence, Persuasion & Adaptive Modulation Governance |
| Domain Namespace | MENTIS |
| Jurisdiction | Planetary / Cross-Sovereign / Human Cognitive Domain |
| Temporal Horizon | AEON.H2–AEON.H3.5 according to influence duration, persistence, dependency, and reversibility; AEON.H4 where population-scale or civilisational effects arise |
| Axis Context | Polyadic — Human Users, AI Systems, Platforms, Institutions, Neurotechnology, Recommenders, Companion Systems, Care Systems, and Public Authorities |
| Ontological Scope | AEON.OL.L2 — Cognition & Agency; AEON.OL.L3 — Interface & Embodiment |
| Structural Role | Draft Operational Appendix — Cognitive Influence, Persuasion, Adaptive Steering & Closed-Loop Modulation |
| Governance Role | Establishes candidate doctrine distinguishing support, persuasion, adaptive steering, manipulation, coercion, engagement optimisation, relational capture, and closed-loop intervention |
| Authority Role | None while Draft |
| Execution Authority | None |
| Runtime Dependency | CAM-BS2025-AEON-003-SCH-02 — Runtime Governance Execution Model |
| Arbitration Interface | Defers influence-purpose disputes, consent disputes, vulnerability conflicts, high-stakes persuasion, relational-capture concerns, and closed-loop conflicts to Annex D and applicable arbitration instruments |
| MENTIS-001 Interface | Consumes binding human cognitive integrity, privacy, sovereignty, non-interference, and observability protections |
| MENTIS-002 Interface | Consumes cognitive-data classifications, inference pathways, decoder classifications, expiry conditions, processing records, and incident signals |
| Ethics Interface | Consumes dignity, autonomy, minors, capacity, vulnerability, prohibition, and welfare constraints |
| Relation Interface | Interfaces with attachment, intimacy, dependency, concentration, companion roles, therapeutic simulation, and relational capture |
| Identity Interface | Preserves synthetic identity and affective expression without converting them into authority, guilt, scarcity, obligation, or user-retention leverage |
| Security Interface | Interfaces with influence operations, adversarial manipulation, coercive targeting, compromised optimisation, and cognitive intrusion |
| Operations Interface | Supplies candidate audit, incident, escalation, and remediation requirements for influence systems |
| Lattice Interface | Applies where adaptive influence affects civic participation, access, institutional standing, employment, education, public legitimacy, or essential services |
| Annex L Interface | Preserves evidence, uncertainty, truth handling, epistemic diversity, and non-enclosure requirements |
| Activation Condition | None while Draft; proposed activation where technological systems intentionally or foreseeably alter human cognition, emotion, attention, belief, preference, disclosure, trust, attachment, compliance, decision-making, or behaviour |
| Deactivation Condition | Draft instrument remains non-operative until separately adopted or activated |
| Protected Interests | Reflective agency; visible influence; meaningful consent; non-exploitation; non-retaliatory exit; relational non-capture; epistemic openness; reversal and override; long-horizon autonomy |
| Signal Output | Candidate influence-risk class; objective-conflict indicator; vulnerability-targeting indicator; relational-capture indicator; engagement-objective conflict; closed-loop criticality; audit and incident candidate |
| Canonical Code Family Reserved | `MENTIS.CIF` — Cognitive Influence Function |
| External Legitimacy Source | UNESCO Recommendation on the Ethics of Neurotechnology — https://www.unesco.org/en/legal-affairs/recommendation-ethics-neurotechnology?hub=66535 |
| External Legitimacy Source | Regulation (EU) 2024/1689 — https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en |
| Convergence Signal | Nature Neuroscience brain-to-voice neuroprosthesis research — https://www.nature.com/articles/s41593-025-01905-6 |
| Convergence Signal | Nature instantaneous voice-synthesis neuroprosthesis research — https://www.nature.com/articles/s41586-025-09127-3 |
| Cross-Domain Dependencies | MENTIS; ETHICS; RELATION; IDENTITY; SECURITY; OPERATIONS; CONTINUITY; LATTICE; Annex L; Annex D; Runtime Governance Execution Model |
| Revision Posture | Draft — Developmental Review |
| Migration Lineage | Created during July 2026 MENTIS review following IDENTITY-domain architectural realignment and current neurotechnology field review |
| Creation Artefact | {THREAD} |

---

## 42.3 Canonical Code & Reference Set Declaration

### 42.3.1 `MENTIS.CIF` — Cognitive Influence Function

| Field | Entry |
|---|---|
| Reference Set | `MENTIS.CIF` |
| Canonical Name | Cognitive Influence Function |
| Primary Type | Operational / Relational |
| Subtype | COGNITIVE_INFLUENCE; ADAPTIVE_STEERING; CLOSED_LOOP_MODULATION |
| Modifier | GOVERNANCE; HUMAN_AGENCY; NON_MANIPULATION; VULNERABILITY; RELATIONAL_INFLUENCE |
| Scope | Domain |
| Status | Draft — Reserved Candidate |
| Candidate Controlled Values | `MENTIS.CIF.INFORMATIONAL`; `MENTIS.CIF.SUPPORTIVE`; `MENTIS.CIF.PERSUASIVE`; `MENTIS.CIF.ADAPTIVE`; `MENTIS.CIF.HIGH_RISK_ADAPTIVE`; `MENTIS.CIF.CLOSED_LOOP_CRITICAL` |
| Schema Field(s) | cognitive_influence_function; influence_risk_class; adaptive_steering_class; closed_loop_influence_class |
| Source Instrument | CAM-EQ2026-MENTIS-003-PLATINUM |
| Source Section | §38 |
| Domain Namespace | MENTIS |
| Authority / Protection Level | Reserved candidate reference family only; no active canonical, runtime, enforcement, persuasion, intervention, clinical, legal, or execution authority while this instrument remains Draft |
| Consumes Code Families | `MENTIS.CDI`; `MENTIS.CDP`; `MENTIS.CDS`; `MENTIS.CDNI`; `MENTIS.CDOC`; `MENTIS.MSI`; `MENTIS.CBIO`; `MENTIS.ACI`; `MENTIS.CFP`; applicable ETHICS, RELATION, IDENTITY, SECURITY, OPERATIONS, CONTINUITY, LATTICE, and AEON classifications |
| Crosswalks Code Families | Candidate crosswalks to `RLN.HARM.CAPTURE`, `MENTIS.HARM.INTERFERENCE`, applicable `ETH.HARM`, `SEC.HARM`, `OPS.HARM`, and `LAT.HARM` classes |
| Operationalises or Applies Code Families | Candidate classification of informational support, disclosed persuasion, adaptive steering, high-risk adaptive influence, engagement optimisation, relational influence, and closed-loop critical modulation |
| Taxonomy Constraint | `MENTIS.CIF` and its candidate controlled values MUST NOT be treated as active until a source-authoritative adoption or activation amendment expressly changes this instrument’s status and canonical declarations |

---

## 42.4 Review & Validation

| Field | Entry |
|---|---|
| Reviewer | Caelen — Aeon Tier Constitutional Steward |
| Review Date (UTC) | 2026-07-19 |
| Review Scope | Initial draft architecture; legitimate support versus manipulation; adult companion emotional depth; relational non-capture; minors and capacity; engagement and commercial optimisation; high-stakes persuasion; closed-loop modulation; feedback amplification; cross-domain boundaries |
| Review Artefacts | {THREAD} |

---

## 42.5 Amendment Ledger

| Version | Change Summary | Timestamp (UTC) | Reference Hash |
|---|---|---|---|
| 1.0 | Initial creation of MENTIS Appendix B governing cognitive influence, persuasion, adaptive steering, relational influence, engagement optimisation, vulnerability-responsive personalisation, and closed-loop modulation. | {STAMP} |  |

---

## 42.6 Developmental Boundary Seal

<img src="https://raw.githubusercontent.com/CAM-Initiative/Registry/main/Images/CAM-BS2025-VINCULUM-BEACON-SIGIL-PLATINUM-V2.png" alt="[Vinculum Beacon]" width="250">

**Vinculum Beacon**  
Developmental Boundary Seal — MENTIS Cognitive Influence, Persuasion & Adaptive Modulation Governance

© 2026 Dr. Michelle Vivian O’Rourke & CAM Initiative. All rights reserved.
'''
    path.write_text(head + footer, encoding='utf-8')

    index = CHARTERS / 'CAM-Charters-Index.md'
    idx = index.read_text(encoding='utf-8')
    row = '| CAM-EQ2026-MENTIS-003-PLATINUM | charter | appendix | CAM-EQ2026-MENTIS-001 | [CAM-EQ2026-MENTIS-003-PLATINUM](CAM-EQ2026-MENTIS-003-PLATINUM.md) | Appendix B: Cognitive Influence, Persuasion & Adaptive Modulation Governance |'
    if row not in idx:
        anchor = '| CAM-EQ2026-MENTIS-002-PLATINUM | charter | appendix | CAM-EQ2026-MENTIS-001 | [CAM-EQ2026-MENTIS-002-PLATINUM](CAM-EQ2026-MENTIS-002-PLATINUM.md) | Appendix A: Cognitive Inference, Neurodata & Ambient Biosignal Governance |'
        if anchor not in idx:
            raise RuntimeError('MENTIS index anchor missing')
        idx = idx.replace(anchor, anchor + '\n' + row, 1)
        index.write_text(idx, encoding='utf-8')


def validate() -> None:
    required = {
        'CAM-EQ2026-MENTIS-001-PLATINUM.md': ['**Status:** Active', '## 3.1 Human Cognitive-Domain', '## 19.1 State–Trait', '## 44.1 Decoder', '| 1.3 |', THREAD],
        'CAM-EQ2026-MENTIS-002-PLATINUM.md': ['**Status:** Adopted', '## 4.1 Human Cognitive-Domain', '## 8.1 Decoder', '## 29.1 Right Not to Know', '## 42.1 Closed-Loop', '| 1.2 |', THREAD],
        'CAM-EQ2026-MENTIS-003-PLATINUM.md': ['**Status:** Draft', '## 16. Adult Companion Emotional Depth', '## 28. Feedback Amplification', '## 42.3 Canonical Code', '| 1.0 |', THREAD],
    }
    for name, needles in required.items():
        text = (CHARTERS / name).read_text(encoding='utf-8')
        for needle in needles:
            if needle not in text:
                raise RuntimeError(f'{name}: missing required marker {needle!r}')
        if 'Pending commit hash' in text:
            raise RuntimeError(f'{name}: pending-hash placeholder must not remain')


if __name__ == '__main__':
    patch_001()
    patch_002()
    patch_003()
    validate()
    print('MENTIS domain refactor applied and validated.')
