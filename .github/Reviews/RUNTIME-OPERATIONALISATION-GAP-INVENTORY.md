# Runtime Operationalisation Gap Inventory

## A — Operational and sound

| Concept | Owner | Representation | Action |
| --- | --- | --- | --- |
| AI-BOM composition/evidence posture | CAM-AI-BOM-PROFILE | Schema and validator; expressly not execution evidence | Retain. |
| Lifecycle roles and agentic lifecycle events | CAM-LIFECYCLE-ACTOR-AGENTIC-PROFILE | Controlled roles/events with record obligations | Retain. |
| Governance reach | OPERATIONS-007 | `OPS.CGRD` + `OPS.CGRS` independent families | Retain. |

## B — Semantically sound, operationally incomplete

| Concept | Owner | Current representation | Missing primitive | Proposed action |
| --- | --- | --- | --- | --- |
| Independent relational configuration | Annex B §2 / RELATION-007 | Mandatory prose fields | Canonical serialization, evidence posture and rule inputs | Implemented as CAM-RUNTIME-STATE-PROFILE and schema. |
| Effective Runtime configuration | Annex B §4.1 / OPERATIONS-007 | Defined evidence record, no schema | Controlled serialized snapshot | Implemented in same profile; execution provenance remains separate. |
| Reassessment conditions | Lifecycle profile / OPERATIONS | Event prose | Controlled trigger set | Implemented as `reviewTriggers`. |

## C — Operational but malformed

| Concept | Owner | Defect | Action |
| --- | --- | --- | --- |
| `AEON.H0–H4` temporal horizon | Annex B §3 | Collapses duration, persistence, reliance, organisational reach, succession, evidence durability and impact | No replacement implemented; research gate below. |

## D — Assessment-only

| Concept | Reason |
| --- | --- |
| AI-BOM declared composition | Important provenance/assurance evidence, but does not establish effective Runtime state or execution participation. |
| Long-horizon constitutional interpretation | Interpretive/governance scope until an independently evidenced operational variable is identified. |

## E — Research required

**Question:** What standards-grounded multidimensional model should Caelestis use to operationally represent lifecycle position, persistence, reliance duration, effect durability, evidence validity, reassessment, succession and long-horizon governance, and should `AEON.H0–H4` be retired in favour of independent machine-actionable fields?

Reason: the existing scale combines several variables. A safe replacement requires a defined evidence model and control consequences for each variable, rather than a new internally invented ladder.
