---
type: pulse
title: Enrolment approaches converge — Simon's Light template ≈ Jehad's /ims-enrolment skill
slug: 2026-06-10-enrolment-approaches-converge-light-template-vs-ims-enrolment-skill
created: 2026-06-10
updated: 2026-06-10
captured_by: jehad-altoutou
audience: department
departments: [ai-office, iso]
confidence: high
sources: [tmpl-light-process-discovery, ims-readiness-assessment-2026-06-08, 2026-05-22-aio-project-management-iso-meeting, 2026-05-18-aio-iso-meeting]
related: [ims-digital-twin, ims-enrolment, ims-enrolment-interview-flow, unified-process-design-template, ims-documentation-hierarchy, iso-ims-puls, simon-tarskih]
---
# Enrolment approaches converge — Simon's Light template ≈ Jehad's /ims-enrolment skill

Reviewing Simon's 2026-06-09 document set against Jehad's May recommendation on low-friction department enrolment surfaces a significant finding: **the two approaches are the same concept, independently designed.**

- **Jehad's `/ims-enrolment` skill** (May 2026, [[ims-enrolment-interview-flow]]): AI-led conversational interviews — parent process with the dept head, sub-processes with activity owners, First Voice per member — producing a Simon-ready handover bundle. Premise: process owners need zero ISO knowledge; the AI carries the structure.
- **Simon's Light Process Discovery Template** ([[tmpl-light-process-discovery]], v2.0): a plain-language form mirroring the technical template block-for-block, "so any process owner can fill it without ISO knowledge," with AI translating to the technical format. Premise: identical.

Both solve the same problem — enrol the 41 process owners without over-explaining ISO. The differences are delivery mechanics (interview vs. form) and data model (Jehad's ISO-9001-Figure-1 7-section shape vs. Simon's SIPOC + 4 registries + gates + KPIs).

## Why the confusion happened

Per [[2026-05-08-ims-prc-ai-001-gap-analysis-3-dev-days-to-align]], Jehad aligned to `IMS-PRC-AI-001 v0.4` in early May; Simon then iterated the Technical template through **11 versions** (May–June) without intermediate shares. The diagram template sent for sign-off was never reviewed; the format "evidence" Jehad was waiting for effectively arrived only on 2026-06-09 as the full doc set — by which point both sides had built parallel solutions. As of 2026-06-10 (AIO standup), Michael is raising IMS de-emphasis with Teresa to stop time-loss on blockers outside AIO control.

## The merge play (proposed)

Adopt **Simon's data model, Jehad's AI delivery**: update `/ims-enrolment` so its interview flow populates Simon's Light template fields, and have AI emit the Technical v11 format + a swimlane diagram via the [[ims-process-visualization-standard|19-rule AI build prompt]] + HTML-table delivery (the confirmed format, per [[2026-05-22-aio-project-management-iso-meeting]]). This directly executes the **#1 unproven milestone in Simon's own readiness report — the Light→Technical AI translation** — and turns two competing methodologies into one pipeline with clear division of labour: Simon owns the model, AIO owns the automation.
