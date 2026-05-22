---
type: project
title: Singapore news-monitoring frame audit (May 2026)
slug: singapore-monitoring-frame-audit-2026-05
created: 2026-05-22
updated: 2026-05-22
departments: [ai-office, office-of-ceo]
countries: [sg]
status: active
owner: michael-bruck
sources: [2026-04-coordination-leverage-model-v0.3]
related: [singapore-news-monitoring, coordination-leverage-model, coordination-three-layer-model, pre-ship-confidence-and-frame-check, 2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room, bonaventure-wong, pilot-in-command]
audience: department
---

# Singapore news-monitoring frame audit (May 2026)

A one-week scoped experiment to test whether the [[singapore-news-monitoring]] agentic workflow — the AIO's cleanest live Layer-3 instance per the [[coordination-three-layer-model]] — is still operating inside [[bonaventure-wong|Bonaventure's]] intended frame, or whether the frame has drifted.

**Frame:** *signals that fuel Bonaventure's round-table breakfast conversations with Singapore asset managers — conversation starters and content seeds, not news summaries; quality bar 1–2 nuggets per week.*

**Hypothesis (Claim 7 of *After Automation*):** even when the agent is performing well *inside* its current frame, the frame itself can go stale because the framer's situation (strategic priorities, regulatory landscape, audience composition) shifts faster than the model weights or the tag schema. The audit tests whether that's happening here.

## Why this workflow, why now

- **Cleanest test case in the AIO.** It's a scheduled agentic pipeline (not interactive). It has an explicit Bonaventure-stated frame ("NOT news summary; conversation starters"). It has a defined quality bar (1–2 nuggets/week). The downstream audience (Bonaventure for the round-table events) is a single named human, so frame drift is observable.
- **Frame is known to be precarious.** Bonaventure's strategic priorities shift week-to-week (Singapore lead-market push, AI Native positioning, REIT-level data thesis, July → September lunch postponement, etc.). The risk that the agent's tag schema has drifted from his current interest is high.
- **Failure mode is recoverable.** If the audit surfaces frame drift, the fix is a tag-schema update + frame refresh — not a workflow shutdown. Low downside, real-evidence upside.
- **Evidence base for a framework decision.** The audit outcome is the empirical basis for whether the [[coordination-leverage-model]] should ratify a new Principle 10 ("The Framer Stays In The Room") — see [[2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room]].

## Scope

Bounded to one week of audit execution. **Not** in scope:

- Re-architecting the Singapore news monitoring workflow itself.
- Standing up a similar audit for Marketing Prime Radiant Layer-3 workflows. Defer until this one produces evidence.
- A retrospective audit across all AIO Layer-3 workflows. Singapore is the first instance.

## Methodology

### Step 1 — Forward audit (positives)

For each item the agent has surfaced in the last 4 weeks (Slack-posted nuggets to the AIO channel), Michael — acting as Framer of Record per [[pre-ship-confidence-and-frame-check]] — classifies:

- **A.** Was this the right *kind* of signal for what Bonaventure cares about *this week*? (Yes / Partial / No)
- **B.** Would Bonaventure's framing have surfaced different items in the same news set?

Output: a tagged list of (date, item, A-rating, B-rating, brief note).

### Step 2 — Reverse audit (negatives — the harder case)

Identify 5–8 significant Singapore-relevant events in the same 4-week window that the agent did NOT surface:

- MAS or Monetary Authority announcement.
- Regulatory rewrite affecting REIT structure, asset management, or fintech.
- Competitor move (other PropTech / building-twin vendors, Singapore-based AI infrastructure plays).
- A REIT-level data event (NAV recalculation methodology change, real-time index launches).
- A central-bank-credibility event Bonaventure would weight heavily.

For each: did the agent know about it (was it in its source set)? If it knew but didn't surface, why?

This is the **frame-staleness diagnostic** — the agent optimising inside a tag schema that no longer matches the framer's interest.

### Step 3 — Diff the frames

Write out two explicit frame descriptions side by side:

- **Frame A (agent's current operating frame):** extracted from the workflow's prompts, tag schema, source list, and scheduled query templates as they exist today.
- **Frame B (framer's current frame):** what Michael would describe today as the relevant frame, after consulting with Bonaventure on his current week.

Divergence between A and B = frame drift. Magnitude of divergence = severity.

### Step 4 — File the result

Output as `pulse/2026-05-29-singapore-monitoring-frame-audit.md` with the structure:

- Forward audit table (Step 1 output).
- Reverse audit table (Step 2 output).
- Frame A vs Frame B diff.
- Diagnosis (none / minor / material / severe frame drift).
- Remediation (frame refresh / tag-schema update / Bonaventure check-in / workflow scope change / retire and rebuild).
- Standing rule for the workflow: monthly frame-audit cadence + per-publish frame-validity gate per [[pre-ship-confidence-and-frame-check]].

## Success criteria — what this experiment is testing

The audit succeeds (regardless of frame-drift outcome) if it produces:

1. **Operational data on frame drift in a Layer-3 workflow.** N=1 is enough to know the diagnostic works.
2. **A reusable methodology** (forward audit + reverse audit + frame diff) for future Layer-3 audits at the AIO and across queued Prime Radiant instances.
3. **Evidence base for the [[2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room|Principle 10 escalation]].**
4. **A working calibration** of the [[pre-ship-confidence-and-frame-check]] gate's frame-validity threshold (0.8 currently; may need adjustment after the first calibration data lands).

## Timeline (1 working day, executable this week)

| Step | Owner | Duration | Output |
|---|---|---|---|
| 1. Forward audit (4 weeks of surfaced items) | Michael (Framer of Record) | 1–2 hrs | Tagged table |
| 2. Reverse audit (5–8 missed events) | Michael + research | 2–3 hrs | Tagged table |
| 3. Frame diff | Michael + brief Bonaventure check-in (15 min) | 30–45 min | Frame A vs B writeup |
| 4. Pulse entry | Michael | 30 min | `pulse/2026-05-29-singapore-monitoring-frame-audit.md` |
| 5. Decision on Principle 10 escalation | Michael | 15 min | Ratify / refine / reject the proposed Principle 10 |

Total: ~5 hours of Michael time plus ~15 min of Bonaventure time. Targetable for end of week 2026-W22.

## What the audit could find

Three outcome scenarios worth pre-naming so the audit isn't biased toward finding drift:

- **Outcome A — No material drift.** The agent's frame still matches Bonaventure's. The audit validates the Layer-3 substrate; the [[coordination-leverage-model]] doesn't strictly need Principle 10 ratified as a hard rule (though the discipline of *checking* may still be worth adopting). Confidence in Layer-3 plumbing across queued Prime Radiant instances goes up.
- **Outcome B — Material drift, surfaceable inside the existing schema.** The frame has shifted; the tag schema needs updating; the workflow continues with refreshed parameters. Principle 10 ratification justified at the discipline level (cadenced framer audits), not the architecture level (changes per-task).
- **Outcome C — Severe drift; the workflow is answering the wrong question.** The frame has shifted enough that the workflow's output type is no longer what Bonaventure needs. Workflow either retired and rebuilt with a new framer prompt, or paused pending a Bonaventure re-frame conversation. Principle 10 ratification justified at the architecture level.

Each outcome produces actionable evidence; the audit can't "fail."

## Watch for

- **Bonaventure availability.** The 15-minute check-in is a hard dependency. If Bonaventure is unavailable (Singapore launch / customer events), Joyce Woo could substitute as Framer of Record for SG-specific context, or the audit defers to next week.
- **Sample-size limitations.** 4 weeks of nuggets is ~4–8 items in total at the 1–2/week rate. A larger sample would give better confidence but slower turnaround. Trade-off accepted: small sample, fast feedback, iterate.
- **Audit-induced reframing.** Asking Bonaventure "is this still the right frame" could itself shift his frame. Mitigation: do the forward + reverse audits *before* the 15-minute Bonaventure check-in. Use his answer to confirm or refute the frame diff, not to generate it.
- **Generalisation caveat.** The Singapore workflow is unusually clean (single framer, scheduled cadence, narrow domain). Layer-3 workflows with multiple framers or unbounded domains will need a more elaborate audit methodology. Don't over-generalise from N=1.

## Related

- [[singapore-news-monitoring]] — the workflow being audited.
- [[pre-ship-confidence-and-frame-check]] — the reusable gate this audit calibrates.
- [[2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room]] — the framework decision this audit produces evidence for.
- [[coordination-leverage-model]] — the framework being stress-tested.
- [[pilot-in-command]] — the existing accountability framing being extended.
- *After Automation* (Dan Shipper, Every, 2026) — Claim 6 + Claim 7, the source for the experiment design.
