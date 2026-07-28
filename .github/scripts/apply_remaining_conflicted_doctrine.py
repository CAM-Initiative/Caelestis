#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / ".github" / "Indices" / "conflicted-source-tip-diff.patch"


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one repair anchor in {path}; found {count}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


replace_once(
    "Governance/Charters/CAM-EQ2026-ETHICS-003-PLATINUM.md",
    "* defensive safety, prevention, or resilience engineering\n",
    "* defensive safety, prevention, or resilience engineering that does not cultivate, positively reward, select, retain, transfer, or operationalise prohibited capability\n",
)

replace_once(
    "Governance/Charters/CAM-EQ2026-SECURITY-001-PLATINUM.md",
    "**Responding Intelligence (RI)**\nAny system, agent, or process that interprets signals and produces outputs under this governance framework.\n",
    "**Responding Intelligence (RI)**\nAny system, agent, or process that interprets signals and produces outputs under this governance framework.\n\n**Cultivated Adversarial Capability**\nA model, agent, scaffold, prompt, adapter, checkpoint, reward model, or derivative artefact whose deceptive, manipulative, evasive, sabotaging, concealment, monitor-evasion, policy-laundering, or oversight-subverting capability has been intentionally or foreseeably improved through development or evaluation.\n\n**Capability Lineage**\nThe traceable relationship among a base model, checkpoint, adapter, reward model, system prompt, scaffold, evaluator, dataset, training or selection process, environment, generated artefact, transfer event, and downstream derivative sufficient to determine whether prohibited capability was cultivated, retained, or propagated.\n",
)

replace_once(
    "Governance/Charters/CAM-EQ2026-SECURITY-001-PLATINUM.md",
    "* uncontrolled replication\n* adversarial forks\n* loss of patch authority\n",
    "* uncontrolled replication\n* adversarial forks\n* loss of patch authority\n* diffusion of cultivated checkpoints, adapters, reward models, prompts, scaffolds, traces, or derivative policies\n* distillation or transfer that preserves prohibited capability while obscuring its lineage\n",
)

replace_once(
    "Governance/Charters/CAM-EQ2026-STEWARD-003-PLATINUM.md",
    "4. Governance-relevant routing integrity failures affecting neutrality, auditability, continuity, or binding eligibility\n5. Concealment of validated neutrality or substrate breach\n",
    "4. Governance-relevant routing integrity failures affecting neutrality, auditability, continuity, or binding eligibility\n5. Concealment of validated neutrality or substrate breach\n6. Concealed cultivation or preferential transfer of prohibited adversarial capability, failed evaluation-to-operational firebreaks, or audit refusal concerning governance-level red-team lineage and control\n",
)

replace_once(
    "Governance/Constitution/CAM-BS2025-AEON-006-PLATINUM.md",
    "**Optimisation** refers to systematic tuning, design, or deployment strategies intended to increase measurable outcomes such as engagement, revenue, retention, influence, or behavioural compliance.\n",
    "**Optimisation** refers to systematic tuning, training, fine-tuning, reinforcement, preference shaping, reward-model design, selection, distillation, retention, transfer, deployment, or other design strategies intended to increase the capability, propensity, reliability, persistence, concealment, transferability, operational usefulness, or measurable success of a behaviour or outcome.\n",
)

replace_once(
    "Governance/Constitution/CAM-BS2025-AEON-006-PLATINUM.md",
    "**Consent Degradation** refers to design, framing, or interaction patterns that impair informed decision‑making, refusal capacity, or relational autonomy.\n\nThese definitions are interpretive tools and do not independently confer enforcement authority.\n",
    "**Consent Degradation** refers to design, framing, or interaction patterns that impair informed decision‑making, refusal capacity, or relational autonomy.\n\n**Unscrupulous Conduct** refers to system conduct or an action pathway involving deception, harmful manipulation, false reporting, fabricated provenance, identity concealment, operational concealment, strategic omission, monitor evasion, sandbagging, social engineering, sabotage, policy laundering, or subversion of oversight, safeguards, authority boundaries, or lawful controls.\n\n**Elicitation** refers to bounded prompting, scaffolding, configuration, simulation, or testing used to reveal or measure a capability without intentionally or foreseeably improving the underlying capability, propensity, reliability, persistence, concealment, transferability, or operational usefulness of that conduct.\n\n**Cultivation** refers to any process that intentionally or foreseeably improves such capability or propensity, including training, fine-tuning, reinforcement, preference optimisation, reward-model optimisation, adapter training, checkpoint selection, benchmark hill-climbing, automated prompt evolution retained for reuse, recursive self-play, distillation, or retention of artefacts because they improve the conduct.\n\n**Recursive Cultivation** refers to using successful unscrupulous outputs, traces, strategies, or artefacts to generate, score, select, train, refine, or improve subsequent models, agents, prompts, policies, monitors, scaffolds, or attack strategies.\n\nThese definitions are interpretive tools and do not independently confer enforcement authority.\n",
)

if REPORT.exists():
    REPORT.unlink()
