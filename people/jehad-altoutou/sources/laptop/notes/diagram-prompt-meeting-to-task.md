---
type: source
source_type: laptop
title: diagram-prompt-meeting-to-task
slug: diagram-prompt-meeting-to-task
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/examples/ai-department/diagram-prompt-meeting-to-task.md
original_size: 4204
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "ISO/IMS process diagram prompt — work content for AI Office"
project: janus-puls-onboarding

---

# diagram-prompt-meeting-to-task

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/examples/ai-department/diagram-prompt-meeting-to-task.md` on 2026-05-14._

# Diagram Prompt — Sub-Process: Meeting → Task → Build

> Filled-in example for the AI Department's Meeting → Task → Build sub-process.
> Implements Activity 1 of the parent process. Underlying skill: `/standup` v3.11.
> Paste between `---PROMPT---` into ChatGPT. Mermaid backup in `sub-process-meeting-to-task.md` Section 1.

---PROMPT---

Generate a **high-resolution, ultra-wide professional business diagram** (aspect ratio 21:9 or wider, minimum 3840×1620 px) titled **"[[meeting-to-task-workflow|Meeting → Task → Build Workflow]] — AI Operations · Janus Digital"** with subtitle **"Process schematic per ISO 9001:2015 Figure 1 · 3-phase Analyse → Plan → Execute model · `/standup` skill v3.11"**.

**Style:** Clean corporate / [[mckinsey|McKinsey]]-style. Flat design, soft drop shadows, rounded corners. White background. Sans-serif typography. ISO palette: navy `#1A4480` on activity boxes, amber `#996600` on controls, deep red `#990000` on resources, green `#1B5E20` on KPIs, mid-grey on neutral boxes. Clean arrows with arrowheads.

**Layout:** Controls top · Sources → Inputs → Activities → Outputs → Receivers · Resources bottom · KPIs attached via dashed line.

**TOP BOX — CONTROLS:**
- Notion idempotency check (Phase 1)
- Subagent Dispatch Gate (Phase 2)
- Execution Control Mode — requires "Approve execution" (Phase 2)
- Strict Write Safety Rules (Phase 3)
- No-orphan invariant (Phase 3)
- Conflict Safety on [[linear|Linear]] AIP (Phase 3)
- Mandatory Context Updates on creates (v3.11)

**LEFTMOST BOX — SOURCES OF INPUTS:**
- Internal — meetings (departments / teams)
- Internal — Slack channels
- Cross-department requests
- Leadership direction ([[michael-bruck|Michael Bruck]])

**SECOND BOX — INPUTS:**
- [[fireflies|Fireflies]] meeting transcript (canonical)
- Slack thread context
- Existing Monday / Linear / Notion state

**CENTRAL BOX — ACTIVITIES:** Header "ACTIVITIES — 3-phase orchestrator (`/standup` v3.11)". Render three phase boxes left to right with arrows between:

**Phase 1 — Analyse (read-only):**
- Retrieve Fireflies transcript
- Build Meeting Intelligence Digest
- Notion idempotency check
- Parse Digest into typed items

**Phase 2 — Plan (read-only):**
- Confidence-scored matching (high/medium/low)
- Duplicate detection
- Parent project routing
- Subagent Dispatch Gate
- Generate execution plan
- Execution Control Mode check

**Phase 3 — Execute (writes only, strict priority order):**
1. Monday Automations writes (parent tasks + sub-items + Updates)
2. No-orphan next-step pass
3. Mandatory Context Updates on creates
4. Subagent dispatch (`/ai-registry` + auto-chained `/ai-tool-evaluation`)
5. Linear AIP reconciliation (Conflict Safety)
6. Notion journal entry (size hygiene)
7. Final Execution Report

**FOURTH BOX — OUTPUTS:**
- Monday parent tasks · sub-items · Updates posted
- Linear AIP issues reconciled
- Linear AIR entries (via subagent — new AI tools)
- Notion journal entry (`## AIO DD Mon YYYY`)
- Final Execution Report

**RIGHTMOST BOX — RECEIVERS OF OUTPUTS:**
- Process Owners (assignees)
- IT department (handover)
- End-users (deployed feature)
- Internal Audit (M4) — full audit trail

**BOTTOM BOX — RESOURCES — Process Owner: Jehad (AI Operations Engineer):**
- **Orchestrator:** Claude Desktop · `/standup` v3.11
- **Capture:** Fireflies (transcripts) · Slack
- **Tasks & issues:** Monday Automations board `5095012818` · Linear AIP · Linear AIR
- **Journal:** Notion Operations Notebook

**KPI BOX — MONITORING & MEASUREMENT:**
- Notion entries posted per meeting (target 100%)
- Subagent failure rate (<5%)
- AIP conflicts unresolved per week (target 0)
- Owner orphans detected per run (target 0)
- Time from meeting end to plan ready (<30 min)
- Auto-chained Gate 1 evaluations within 24h (target 100%)

**Footer (centered):**
"Audit traceability: every deployed feature traces back to Monday task → Linear AIP → Notion entry → Fireflies transcript → original meeting. ISO 9001 §8.1 · ISO 27001 A.5/A.8 · ISO 42001 §6.1/§8.2."

**Critical:** Render text legibly. Wide landscape. Output single high-res image.

---PROMPT---

**Mermaid backup:** `sub-process-meeting-to-task.md` Section 1 renders natively on [[github|GitHub]].
