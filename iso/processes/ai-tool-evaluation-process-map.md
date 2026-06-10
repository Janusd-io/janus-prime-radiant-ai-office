---
type: process
title: AI Tool Evaluation & Approval — IMS Process Map (pilot)
slug: ai-tool-evaluation-process-map
created: 2026-06-09
updated: 2026-06-09
departments: [ai-office, ims-compliance]
captured_by: jehad-altoutou
audience: [department]
confidence: high
sources: [proc-ims-ai-tool-evaluation, ai-tool-evaluation-diagram]
related: [ims-digital-twin, unified-process-design-template, ai-tool-evaluation-framework, ai-tool-evaluation, ai-registry, ims-process-register, michael-bruck, iso-ims-puls]
---

# AI Tool Evaluation & Approval — IMS Process Map (pilot)

The **first fully-documented IMS process** (PROC-IMS-AIToolEvaluation v0.1, DRAFT) — the pilot that validated the [[unified-process-design-template|technical template]]. It is the ISO-grade process map for the same gate captured operationally in [[ai-tool-evaluation-framework]] / [[ai-tool-evaluation]] and feeding the [[ai-registry|AI Registry]]; register code **G12 (AI Tools Approval for Use)**. Process owner: Head of AI Office ([[michael-bruck|Michael]]). ISO 9001 cl.6.1/7.5/9.1 · ISO 27001 A.5.9/A.5.12 · ISO 42001 §8.2. Full map verbatim: [[proc-ims-ai-tool-evaluation]]; swimlane diagram: [[ai-tool-evaluation-diagram]].

## Actors (5 swimlanes + 1 AI agent)
Requester (any employee) · AI Evaluator (AI & Technology Office) · Domain Expert (relevant dept) · IT Department · Head of AI Office (approval authority). AI agent **AI-03 = Fireflies** captures tool mentions from meetings.

## Triggers
(A) Request via Slack `#ai-tool-requests`; (B) tool mention in a meeting (Fireflies, AI-03). Records on **Form 1A1 (AI Tool Intake Log)** and **Form 1A2 (AI Tool Evaluation Report)**.

## Four-stage gated flow
1. **Stage 1 — Intake & Triage**: log candidate, classify Tool vs Infrastructure, rapid desk review → **Gate G1.1–G1.5** (all must pass).
2. **Stage 2 — Technical Qualification**: detailed review, score against **G2.1–G2.11** matrix → pass if all Must-Have + Should-Have ≥15/25; **Conditional Approval** by Head of AI Office if Should-Have 10–14/25.
3. **Stage 3 — Sandbox (Tier 3, no production data)**: provision sandbox, Domain Expert executes a 3–5 day test brief, completes structured evaluation → **Gate G3** (majority recommend + no critical defects).
4. **Stage 4 — Compilation & Approval**: compile dossier (Form 1A2) → Head of AI Office approves → **4B IT Handover** (security review, SSO, deployment) → **4C Announcement** (Slack) → add to [[ai-registry|AI Registry]] (tier, use cases, data boundary, IT contact). Rejections at any gate notify the requester.

## Status / next
DRAFT pilot — not yet validated by its process owner (a gap flagged in the [[ims-readiness-assessment-2026-06-08|readiness report]]). Validating this pilot + proving the Light→Technical translation are the two milestones before the [[ims-digital-twin]] scales to the other 40 [[ims-process-register|processes]].
