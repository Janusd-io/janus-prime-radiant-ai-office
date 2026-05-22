---
type: process
title: Pre-ship confidence-and-frame check (two-axis gate for Layer-3 agentic workflows)
slug: pre-ship-confidence-and-frame-check
created: 2026-05-22
updated: 2026-05-22
departments: [ai-office]
status: active
owner: michael-bruck
sources: [2026-04-coordination-leverage-model-v0.3]
related: [coordination-leverage-model, coordination-three-layer-model, organisational-digital-twin, pilot-in-command, ai-tool-evaluation-framework, ai-policy, singapore-monitoring-frame-audit-2026-05, 2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room]
---

# Pre-ship confidence-and-frame check

A reusable pre-publication gate for any Layer-3 agentic workflow at Janus. **Two axes** — *output quality* and *frame validity* — each scored independently, each with an explicit threshold, each surfaced before anything ships.

Derived from Every's *"Ask for confidence before shipping"* pattern (case-studies/every-ai-native-workflows.md, pattern #6) plus the **frame-vs-framer** distinction in Dan Shipper's *After Automation* (Claim 7). The Every pattern asks the agent to score one axis (confidence in the output). This process extends it to ask the agent to score two — because Layer-3 workflows produce outputs *inside a frame*, and the frame can go stale even when the agent is performing well inside it.

## Why two axes, not one

A single-axis confidence score lets a sharp agent pass a stale frame unchallenged. Concrete failure mode at Janus:

- An agent ([[singapore-news-monitoring]], say) is asked to surface signals for *Bonaventure's round-table breakfast conversations* — the frame.
- Bonaventure's strategic priorities shift week-to-week. The frame the agent is operating in is *last week's* frame.
- The agent's output is high-quality *inside that frame* — it confidently surfaces excellent items that match the obsolete tag schema. Output-confidence is 0.9.
- The framer ([[michael-bruck|Michael]] or [[bonaventure-wong|Bonaventure]]) would now describe the relevant frame differently. Frame-validity is 0.5.
- A one-axis gate ships the item. A two-axis gate surfaces the frame question.

The two-axis gate operationalises the proposed [[2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room|Principle 10 — The Framer Stays In The Room]] addition to the [[coordination-leverage-model]] design principles.

## Scope — when to use this gate

**Required** for every Layer-3 agentic workflow per the [[coordination-three-layer-model]]:

- Cross-market intelligence aggregation ([[singapore-news-monitoring]] and successors).
- Cross-domain decision routing (where the agent decides *which* department / human owns a decision).
- Long-horizon agent runs that produce output without standing human review.
- Any agentic workflow whose success metric is itself a frame ("revenue per employee," "AI adoption state in Finance," "which workflows will bottleneck at 3× headcount") rather than a measurement *inside* a stable frame.

**Optional but recommended** for Layer-2 workflows whose frame depends on a fast-moving external context (regulatory, competitive, customer-segment).

**Not required** for Layer-1 force-multiplier work — drafting, code generation, research synthesis — where the frame is stable (a draft is a draft; a function is a function).

## The two axes

### Axis 1 — Output quality confidence (the existing Every pattern)

The agent self-scores how confident it is that *the output it produced answers the question well inside the current frame*. Score 0.0–1.0 with explicit justification.

Sample agent self-prompt:

```
Before shipping, score your confidence in this output (0.0–1.0):

- 0.9–1.0: I am confident this output is high-quality. The evidence is solid,
  the reasoning is sound, the format fits the audience.
- 0.7–0.9: Output is solid but has a named risk (cite it).
- 0.5–0.7: Output is plausible but has unresolved questions. Surface them.
- < 0.5: I cannot ship this confidently. Surface what's missing.

Score: _____
Justification: _____
Unresolved risks: _____
```

**Threshold:** below 0.7 = revise or surface. Above 0.7 = proceeds to Axis 2.

### Axis 2 — Frame validity confidence (the new extension)

The agent self-scores how confident it is that *the frame the output is being produced inside is still the right frame for the framer's current situation*. Different question. Different score. Different threshold.

Sample agent self-prompt:

```
Now score the frame this output operates inside (0.0–1.0):

What's the frame?
- The question this workflow is answering: _____
- The success metric it's optimising: _____
- The audience this output is for: _____
- The strategic context it presumes: _____

Frame-validity check:
- Has anything material changed in the framer's situation since this frame
  was set? (regulatory shift / strategic pivot / new evidence / changed
  audience priorities)
- Are there events I know about that the current frame would NOT surface
  but the framer would now consider relevant?
- Could I describe what the framer would say if I asked them today
  "is this still the right question to be answering?"

Score: _____
Justification: _____
Frame-shift signals I observed: _____
```

**Threshold:** below 0.8 = **surface to the Framer of Record, do not ship**. Frame-validity is held to a higher bar than output-quality because the cost of shipping confidently inside a stale frame is higher than the cost of shipping a noisy output inside the right frame.

## Mechanics

### Who's the Framer of Record?

A named human, declared in the workflow's project hub. Defaults:

- AIO-owned Layer-3 workflows: **Michael Bruck** unless otherwise specified.
- Marketing instance Layer-3 workflows: **Andrew Soane**.
- Each new Layer-3 workflow declares its Framer of Record at design time. Captured in the project's `framed_by:` frontmatter field (proposed schema extension; see [[2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room]]).

### Where the gate sits

For pipelines like [[standup]]: the gate runs as a final step before the structured output is written to Notion / Linear AIP / the Prime Radiant inbox. For scheduled monitoring agents (Singapore news, etc.): the gate runs before each scheduled publish.

### What happens below threshold

| Axis | Below threshold | Action |
|---|---|---|
| Output-quality (< 0.7) | Agent revises with the named risks addressed. If still below, surfaces to the PIC ([[pilot-in-command]]) for verification. |
| Frame-validity (< 0.8) | Agent **stops**, does not revise. Surfaces to the Framer of Record with: the current frame, the observed shift signals, and a proposed alternative frame or framer prompt. Framer either ratifies the existing frame, updates it, or retires the workflow. |

The asymmetry is the point: revising for output quality stays inside the loop; revising for frame validity has to escape the loop.

### Logging

Every gate pass produces a log entry:

```
[YYYY-MM-DD HH:MM] pre-ship-gate | <workflow-slug>
- output-confidence: 0.XX
- frame-validity: 0.XX
- decision: ship / revise / surface-to-framer
- framer-of-record: <slug>
- notes: <one line>
```

Logs accumulate in the per-workflow project hub. Frame-validity scores below 0.8 trigger an entry in the workflow's "Frame audits" running section regardless of decision — even when the framer ratifies the existing frame, the *frame question* is part of the audit trail.

## Why this strengthens Pilot in Command, not duplicates it

[[pilot-in-command|Pilot in Command]] (AI Policy §5.9) names the named human who is *accountable for the output*. The PIC's question is *"is this answer correct?"*

The Framer of Record's question is *"is this still the right question to be answering?"*

Both can be the same person (often are, at small scale). The point of separating the *roles* is to make the frame audit a discrete review event distinct from the output review. A PIC who has already approved 50 outputs inside a frame is exactly the person *least* likely to surface that the frame has gone stale — they're invested in the frame. Naming the Framer role explicitly lets the same person hold both responsibilities while distinguishing the two questions.

## First instance — Singapore news monitoring

The first agentic workflow to run this gate is documented in [[singapore-monitoring-frame-audit-2026-05]]. The audit is also the empirical evidence base for whether the [[coordination-leverage-model]] should ratify a new Principle 10 — see [[2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room]].

## Watch for

- **False-positive frame-shift signals.** An agent that surfaces "the frame might have shifted" every week becomes noise. Calibration data will come from the first 4–6 weeks of running the gate; if frame-validity scores cluster at 0.85–0.95 with rare drops below 0.8, the gate is calibrated. If they cluster low, either the workflows are genuinely operating in unstable frames (good signal) or the prompt is over-flagging (recalibrate).
- **Framer fatigue.** A Framer of Record who is constantly being asked to ratify frames will start rubber-stamping. The monthly frame-audit cadence (separate from per-publish gate events) is the structural counter — the framer reviews accumulated gate logs once per month and decides whether to refresh the frame, retire the workflow, or keep the schedule.
- **Compound-agent failure mode.** If the gate itself becomes an agentic workflow (which it will at some point — auto-scoring confidence + frame-validity from inside the agent stack), it becomes another Layer-3 workflow that needs its own framer. Infinite regress is avoided by keeping the gate *self-scoring by the producing agent*, with the Framer of Record as the named human at the bottom of the stack.

## Related

- [[coordination-leverage-model]] — the framework this gate operationalises.
- [[coordination-three-layer-model]] — the layer-3 distinction that triggers gate applicability.
- [[pilot-in-command]] — the existing accountability framing this strengthens.
- [[ai-tool-evaluation-framework]] — the gate-based discipline this gate fits inside (downstream of G4 ongoing review).
- [[singapore-monitoring-frame-audit-2026-05]] — first instance + experimental evidence.
- [[2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room]] — proposed framework principle this gate is the mechanism for.
- *After Automation* — Dan Shipper (Every, 2026); the frame-vs-framer distinction (Claim 7) is the source for the second axis.
- Every case-studies pattern #6 — "Ask for confidence before shipping"; source for the first axis.
