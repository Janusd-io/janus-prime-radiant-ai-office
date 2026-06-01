---
type: question
title: Should the Coordination Leverage Model ratify a 10th principle — "The Framer Stays In The Room"?
slug: 2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room
created: 2026-05-22
updated: 2026-05-22
departments: [ai-office, office-of-ceo]
status: active
owner: michael-bruck
sources: [2026-04-coordination-leverage-model-v0.3]
related: [coordination-leverage-model, coordination-three-layer-model, organisational-digital-twin, pre-ship-confidence-and-frame-check, singapore-monitoring-frame-audit-2026-05, pilot-in-command, builders-sellers-measurers, ai-native-mandate]
---

# Should the Coordination Leverage Model ratify a 10th principle — "The Framer Stays In The Room"?

## Where the question came from

Surfaced 2026-05-22 from a stress-test of the [[coordination-leverage-model]] against Dan Shipper's *After Automation* (Every, 2026). Specifically Claims 6 and 7 from `claims.md`:

- **Claim 6** — *A benchmark score measures how well a model performs inside a task, prompt, scoring rubric, and evaluation frame someone created. When a model saturates one frame, the human work often moves one level up.*
- **Claim 7** — *Even if a model can choose and re-choose frames, it is still acting in pursuit of a goal, reward, or signal that someone decided should count as progress. The model can climb frames, but the framer is still in contact with the whole live situation the frame leaves out.*

The Coordination Leverage Model's Layer 3 promise — agents maintain institutional context, translate between regulatory frameworks, aggregate cross-market intelligence, route decisions to the right human authority — is **frame-climbing work** that the framework currently treats as automation. Principle 2 (Automate Coordination, Not Judgment) is the closest existing safeguard, but it conflates *judgment* (what to do given a frame) with *framing* (what frame applies). The gap is real.

## The proposed principle

**Principle 10 — The Framer Stays In The Room.**

> Every Layer-3 agentic workflow has a named *Framer of Record* — a human who owns not just the workflow's output but the **frame the output is produced inside**. The Framer's specific job: ask *"is this still the right question?"* on a defined cadence, with authority to retire a frame even when the agent is performing well inside it.

Distinguishes from [[pilot-in-command|Pilot in Command]] (AI Policy §5.9): PIC owns the *output*; Framer owns the *frame the output is produced inside*. PIC says *"this answer is correct."* Framer says *"this is still the right question."* Both can be the same person (often are, at small scale). The point of naming the role distinctly is to make the frame audit a discrete review event distinct from output review.

Schema implication: add a `framed_by:` frontmatter field for Layer-3 artefacts, in addition to the existing `decided_by:` / `captured_by:` / `owner:`.

## Why this isn't already covered

Quick map against the existing 9 principles to confirm the gap:

| Existing principle | Adjacent? | Why it doesn't fully cover |
|---|---|---|
| 1. Layer Sequence Is Not Optional | No | About build-order, not frame ownership. |
| 2. Automate Coordination, Not Judgment | Closest | Names *judgment* as the human-owned activity. *Framing* is upstream of judgment and the principle doesn't distinguish them. |
| 3. Structured Data Is Capital | No | About output format, not frame validity. |
| 4. Calibrate Autonomy Per Task | Closest | Names per-task autonomy calibration. But "task" is itself a frame; the calibration happens inside a chosen frame, not over it. |
| 5. Systems of Record Are the Sensor Network | No | About the input layer. |
| 6. Capture Before You Coordinate | No | About sensor density. |
| 7. Portability Over Optimisation | No | About cross-geography replicability. |
| 8. The Effectiveness Gate | Closest | "Should this activity exist at all?" is a framing question. But Principle 8 is fired at workflow *creation* time, not at standing-workflow operation time. Principle 10 would name the *ongoing* framing discipline. |
| 9. Identity Is the Perimeter | No | About IAM and access control. |

Principle 8 is the most overlapping existing principle. Worth considering whether Principle 10 is best ratified as a *separate principle* or as an *extension of Principle 8* (e.g., 8.1 The Effectiveness Gate at creation; 8.2 The Frame Audit at operation). My instinct: separate principle, because the *cadence* and *named role* are operationally distinct from the creation-time effectiveness check.

## Why escalate rather than ratify directly

Two reasons:

1. **The framework is Michael's.** Adding principles is a strategic act, not a wiki edit. Even when the proposal lands cleanly, ratification belongs with the author.
2. **No empirical evidence yet.** The proposal is theoretically motivated (Dan Shipper's Claim 7) but hasn't been tested against a Janus workload. The [[singapore-monitoring-frame-audit-2026-05]] experiment is designed to produce that evidence. Ratification before the audit risks adopting an over-engineered rule; rejection before the audit risks missing a real gap.

## What the evidence base will look like

The [[singapore-monitoring-frame-audit-2026-05]] experiment produces one of three outcomes that map to ratification stances:

- **Outcome A (no material drift):** Principle 10 *as a discipline* is worth adopting (frame-audit cadence + Framer-of-Record naming) but doesn't need to be *architecture-level*. Adopt the discipline; defer hard codification.
- **Outcome B (material but recoverable drift):** Principle 10 ratified at the discipline level. Add `framed_by:` to frontmatter schema; require Framer-of-Record naming for new Layer-3 workflows; cadenced frame audits become AIO standard.
- **Outcome C (severe drift; workflow answering wrong question):** Principle 10 ratified at the architecture level. The frame-audit becomes a hard gate per [[pre-ship-confidence-and-frame-check]]; failure surfaces stop publication, not just revise it.

The audit timeline is ~1 working day this week; ratification decision should be feasible within 2026-W22.

## Operational rule under each outcome

| Outcome | Principle 10 ratified as | New operational rule |
|---|---|---|
| A | Discipline (not architecture) | Layer-3 workflow project hubs add a `## Frame audits` section; cadenced quarterly review by the named owner. |
| B | Architecture principle (light) | `framed_by:` frontmatter field becomes required for Layer-3 artefacts. Monthly frame-audit cadence as AIO standard. [[pre-ship-confidence-and-frame-check]] gate runs but frame-validity threshold doesn't block publication. |
| C | Architecture principle (hard) | All of B, plus: frame-validity < 0.8 on the pre-ship gate becomes a publication-blocker. Framer of Record is on the on-call rota for Layer-3 workflows. |

## Side question worth resolving alongside

If Principle 10 is ratified, two follow-up framework questions surface:

1. **Where does the framer come from at Layer 2?** Department-level pipelines have framers too (the standup pipeline's framer is implicitly Michael; the recruitment pipeline's framer is implicitly Rosa). Should the principle extend to Layer 2, or stay scoped to Layer 3 where frame-climbing is the named concern?
2. **What about the framer's framer?** A regress argument — the Framer of Record is operating inside *their own* frame, which is set by the next level up (department head, CEO, board, market reality). The Coordination Leverage Model doesn't currently address this. The pragmatic answer: stop the regress at the human in contact with the live situation the frame leaves out. Worth a footnote on the framework brief if the principle ratifies.

## Status

**Overdue (as of 2026-06-01).** Target was end of 2026-W22 (week of 26 May); we are now in W23. The [[singapore-monitoring-frame-audit-2026-05]] project file exists (created 2026-05-22) but the audit output — `pulse/2026-05-29-singapore-monitoring-frame-audit.md` — has not been filed. The experiment was a ~1 working day commitment from Michael.

**Next step:** Michael to run the audit (Steps 1–4 per the project brief) and file the pulse entry. Once that exists, the Principle 10 ratification decision (Outcome A/B/C) follows immediately. This question stays `active` until the pulse entry is filed and Michael makes the call.

## Related

- [[coordination-leverage-model]] — the framework being amended.
- [[coordination-three-layer-model]] — the Layer-3 distinction that triggers the proposal.
- [[pre-ship-confidence-and-frame-check]] — the proposed operational mechanism.
- [[singapore-monitoring-frame-audit-2026-05]] — the experiment producing the evidence.
- [[pilot-in-command]] — the existing accountability framing being distinguished from.
- [[builders-sellers-measurers]] — the companion role-taxonomy frame.
- *After Automation* (Dan Shipper, Every, 2026) — source for Claims 6 + 7.
