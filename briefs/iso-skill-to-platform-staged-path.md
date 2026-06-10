---
type: brief
title: ISO documentation — skill first, platform second: the staged path from 41 DRAFT docs to a productizable IMS platform
slug: iso-skill-to-platform-staged-path
created: 2026-06-10
updated: 2026-06-10
departments: [ai-office, iso]
captured_by: jehad-altoutou
owner: jehad-altoutou
status: active
confidence: high
sources: [ims-readiness-assessment-2026-06-08, tmpl-light-process-discovery, tmpl-unified-process-design, 2026-05-22-aio-project-management-iso-meeting, 2026-05-18-aio-iso-meeting]
related: [ims-digital-twin, ims-enrolment, puls-programme, iso-ims-puls, unified-process-design-template, ims-process-visualization-standard, ims-documentation-hierarchy, organisational-digital-twin, 2026-06-10-enrolment-approaches-converge-light-template-vs-ims-enrolment-skill, michael-bruck, simon-tarskih]
---
# ISO documentation — skill first, platform second: the staged path from 41 DRAFT docs to a productizable IMS platform

> **Status: discovery — for Michael's review.** Drafted 2026-06-10 by Jehad + Claude. Decision sought: endorse the staged sequence (and its framing for the Teresa conversation), or redirect.

## The lede

The ISO programme is blocked not by missing methodology but by an untested mechanism and an unstable interface between Simon and the departments. AIO can unblock it with a **three-stage build — skill → dashboard → interactive platform** — where each stage's output is the next stage's input, so effort survives even if the IMS de-emphasis decision (Teresa, 12 Jun) lands. The end state is not internal overhead: a properly built IMS platform is an **organisational-digital-twin product asset** in a category Gartner has just codified (DTO Platforms MQ, Sep 2026) — which is the framing that makes this fundable rather than "more ISO."

## Why this matters to AIO

1. **We become the unblocking party.** Simon's own [[ims-readiness-assessment-2026-06-08|readiness report]] names the #1 unproven milestone: the **Light→Technical AI translation** — exactly an AI-department deliverable. Proving it converts two months of mutual confusion (11 unshared template iterations; Jehad's diagram template never reviewed; parallel solutions built — see [[2026-06-10-enrolment-approaches-converge-light-template-vs-ims-enrolment-skill|the convergence pulse]]) into a clear division of labour: **Simon owns the data model, AIO owns the automation.**
2. **It de-risks the Teresa decision.** Stage 1 is days of effort and produces the certification-critical artefacts (the documents themselves) regardless of how the de-emphasis call lands. Nothing is bet on the platform until the model is proven and the strategic green light exists.
3. **It converts compliance spend into product R&D.** Janus sells digital-twin capability ([[organisational-digital-twin]]); the IMS digital twin is already register process **C12 — Internal AI Product**. An interactive IMS platform built on validated foundations is a candidate market entry in the DTO category, not just an internal tool.

## The problem, precisely

- All 7 IMS foundation documents are **DRAFT, none approved**; no document lifecycle exists yet.
- The core mechanism (process owner fills the plain-language **Light template** → AI translates to the **Technical v11** format) has **never been tested**.
- Departments experience ISO as "boring PDFs and forms"; enrolment friction is the scaling bottleneck for 41 processes across every department.
- Two enrolment approaches exist in parallel — Simon's Light template and AIO's `/ims-enrolment` interview skill — which are **the same concept independently designed** (both: zero ISO knowledge required from owners, AI carries the structure). They need merging, not competing.

## The staged path

### Stage 1 — the IMS factory skill (now; days of effort)

Upgrade `/ims-enrolment` to Simon's data model:

1. **Input** — AI-led conversational interview that populates the [[tmpl-light-process-discovery|Light template]] fields (or ingests an already-filled form).
2. **Translate** — emit the [[unified-process-design-template|Technical v11]] document, fully populated (the unproven milestone, proven).
3. **Diagram** — generate the Level-1 swimlane via Simon's own [[ims-process-visualization-standard|19-rule AI build prompt]].
4. **Deliver** — HTML tables (the confirmed audit format, per [[2026-05-22-aio-project-management-iso-meeting|22 May meeting]]: auditor checks existence, awareness, evidence — no platform required).
5. **Trace** — validate output against the clause-comparison matrix so every process shows its ISO 9001/27001/42001 coverage and missing fields.

**Design constraint that makes the path staged rather than three separate builds: the skill emits structured JSON alongside the HTML.** The JSON is the platform's database, from day one.

**Validation test (self-contained, ~1 day):** regenerate Simon's pilot process (AI Tool Evaluation & Approval) from a Light-template input and diff against his hand-made v0.1. If they match, the mechanism is proven — in his own format, so the result is not disputable.

### Stage 2 — thin review dashboard (after pilot validation; ~a week)

Read-only Next.js view over the Stage-1 JSON: all processes by department · status (draft / in review / approved) · missing-field and clause-gap flags computed automatically · a review queue for the ISO department. Delivers ~70% of the platform vision (ISO oversight, gap pinpointing, departments seeing what they're missing) with none of the interactive-editing complexity, while the template is still settling.

### Stage 3 — the interactive platform (= PULS MVP; after template stability + strategic green light)

The full vision: in-browser guided process creation/editing with embedded education ("ISO from boring PDF to immersive experience") · approve/reject workflow with structured feedback to the owning department · full cross-department process map · audit-ready export packs · eventually the predictive layer that gives [[puls-programme|PULS]] its name. Entry criteria: technical template survives 5–10 real processes without structural change, AND the post-Teresa mandate supports it.

## Why not platform-first

- **Unstable data model**: 11 template iterations in 5 weeks; a UI built now inherits every future change as a schema migration, and today's confusion gets baked into software.
- **Certification doesn't need it**: HTML tables already satisfy the auditor; the platform improves the *experience*, the skill produces the *documents*.
- **Timing**: committing platform effort 2 days before a possible de-emphasis decision is backwards; Stage 1 is cheap and valuable under every outcome.

## Open points for Michael

1. Endorse the staged sequence and the Stage-1 start (validation test against Simon's pilot)?
2. Framing for the 12 Jun Teresa conversation: "AIO unblocks ISO with days of effort + optional product upside" vs. de-emphasis?
3. When/how to bring Simon in — propose: after the validation test passes, show him his own pilot regenerated by AI from the Light template (evidence, not argument).
4. Does the Stage-3 product angle (DTO category) warrant its own track in the AI Projects portfolio, or stay latent until Stage 2 proves value?

## Cross-references

[[ims-digital-twin]] · [[2026-06-10-enrolment-approaches-converge-light-template-vs-ims-enrolment-skill]] · [[puls-programme]] · [[iso-ims-puls]] · [[ims-documentation-hierarchy]] · [[organisational-digital-twin]]
