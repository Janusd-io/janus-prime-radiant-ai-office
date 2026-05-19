---
type: source
source_type: meeting
title: AIO, ISO Meeting 18 May 2026
slug: 2026-05-18-aio-iso-meeting
created: 2026-05-18
captured_by: jehad-altoutou
fireflies_id: 01KRXFH61964G4BA18K1QX3P3V
fireflies_url: https://app.fireflies.ai/view/01KRXFH61964G4BA18K1QX3P3V
attendees: [Michael Bruck, Simon Tarskih, Jehad Altoutou]
duration_min: 64
audience: department
departments: [ai-office, iso]
standup_skill_version: v3.21
parser_version: 3
related: [2882088503, 2889155963, 2924556146, 2924562376, 2924513833, 2924559320, 2924557920, 2924559454, AIR-30, AIR-81, AIR-5, AIR-105, AIR-106, AIR-107, AIR-108]
---

## Clean Meeting Summary

Michael Bruck, Simon Tarskih, and Jehad Altoutou held a 64-minute working session on 18 May 2026 to align on the Janus ISO management system. Michael walked through the 41 identified management system processes mapped across four categories and three ISO standards (9001, 27001, 42001). After months of the ISO documentation work being blocked on Simon's foundation documents, the session produced a concrete phased-rollout plan: work on AIO as the pilot department first, freeze existing policies as ISO-compliant baselines, build one replicable AI skill, and then deploy to other departments. Michael committed to documenting 1–5 of his own processes as worked examples by Wednesday 20 May. A side discussion on AI-efficient file formats (Markdown over docx, HTML over PDF) and the Claude in Excel plugin led to actionable adoption steps for Simon.

---

## 🎯 Next steps — by next standup (20 May 2026)

- **Document 1–5 AIO processes as worked examples** (policy mgmt + change mgmt, with inputs, outputs, sources) — Owner: Michael Bruck — Due: 20 May 2026 — [Monday: 2924556146](https://janusd-company.monday.com/boards/5095012849/pulses/2924556146)
- **Review Simon's process docs and provide specific written feedback** (tool eval framework + task mgmt) — Owner: Michael Bruck — Due: 20 May 2026 — [Monday: 2924562376](https://janusd-company.monday.com/boards/5095012849/pulses/2924562376)
- **Discard current skill files; wait for Michael's policy examples** — Owner: Simon Tarskih — Due: 19 May 2026 — [Monday: 2924513833](https://janusd-company.monday.com/boards/5095012849/pulses/2924513833)

---

## 📅 Next steps — this week (by 22 May 2026)

- **Set up Claude in Excel plugin on Simon's machine** — Owner: Simon Tarskih — Due: 22 May 2026 — [Monday: 2924559320](https://janusd-company.monday.com/boards/5095012849/pulses/2924559320)

---

## 🏔️ Next steps — longer horizon

- **Research UAE/Singapore legal requirements for ISO management system** — Owner: Simon Tarskih — Due: TBD (after process mapping stable) — [Monday: 2924557920](https://janusd-company.monday.com/boards/5095012849/pulses/2924557920)
- **Design and build AI auditor skill for ISO compliance self-assessment** — Owner: Jehad Altoutou — Due: TBD (post process-doc stabilisation) — [Monday: 2924559454](https://janusd-company.monday.com/boards/5095012849/pulses/2924559454)

---

## Decisions made

1. **Phased rollout adopted**: AIO is the pilot department. Fully document AIO's process hierarchy and build one replicable AI skill before expanding to other departments — not all at once.
2. **Baseline-freeze strategy**: take existing AIO policies and processes at whatever completeness level they're at (20–80%), freeze them as ISO-compliant baselines, and iterate continuously.
3. **Michael to produce worked examples by Wednesday 20 May**: 1–5 processes starting with policy management and change management, with full inputs, outputs, proposed owners, and ISO clause references.
4. **Financial processes out of scope**: GAAP/IFRS standards handle finance separately; expense approval and budget may be added later.
5. **ISO 14001 (environmental) and 45001 (health & safety) deferred**: ISO 9001, 27001, 42001 in scope now.
6. **Document format recommendations adopted**: docx → Markdown; keep Excel only for comparison tables with formulas; HTML/SVG for diagrams; avoid PDF for LLM interaction.
7. **Next meeting: Wednesday 20 May 2026.**
8. **Status of ISO parent item (`2882088503`) changed: Postponed → In Definition** — concrete plan + explicit commitments authorise the move.

---

## Findings / context

**The 41-process management system.** Michael has mapped 41 management system processes across four categories — governance/board processes, internal/product processes, support processes (asset control, legal compliance), and management processes. The 41 span ISO 9001 (quality), 27001 (information security), and 42001 (AI management). The real count will likely grow when sub-processes are included (could reach 400+). Each process has inputs and outputs; some outputs are single documents, others are ten or more.

**AI-powered management system vision.** Rather than paper documents that people are asked to read, Michael's vision is 41 AI skills or agents — one per process — that operationalise each process directly. An "auditor agent" (see sub-item `2924559454`) would check compliance by asking deep audit questions against a defined document checklist. Michael: "I want to build like an auditor… ask ask ask — deeper deeper deeper." This is distinct from Joyce's nearly-complete facilitation skill (`2889155963`), which creates process documents interactively; the auditor skill checks whether the required documents exist and meet criteria.

**Joyce's facilitation skill is nearly done.** Per the earlier AI Native CEO meeting today (separate from this session), Joyce has almost finished the ISO facilitation skill. It references all relevant Simon documents and works as an interactive Q&A (what process, where does data come from → LLM generates the ISO process). Blocker: Simon's confirmation on the outputs before company-wide distribution. This is tracked on `2889155963`.

**Why AIO as pilot.** Jehad: "If we're gonna just send everything to the other departments they're not gonna understand anything — nor know how to start or where to start. So as long as we finish one department… create one skill and send the skill to the other departments. Let the skill work for them." This framing was accepted. AIO is the only department that has already written anything ISO-related; starting there produces the template other departments replicate.

**Document format discussion.** Simon currently uses .docx and .xlsx. Recommendations agreed:
- Switch Word docs to Markdown: cheaper token consumption, portable between Claude and Gemini, easier for LLMs to read and write.
- Keep Excel for complex comparisons with formulas; for pure table text, prefer HTML or CSV.
- Avoid PDF — Michael: "For LLMs PDF is really bad."
- Claude in Excel plugin: Michael demonstrated live — syncs with Cowork, allows incremental edits inside Excel rather than regenerating the full file from scratch, saving tokens. Claude in Word plugin similarly available.

**Legal requirements are next.** Simon plans to research UAE (UIE) and Singapore legal requirements once process mapping is stable. Janus has no CLO — this falls to Simon and Michael. Financial accounting standards (GAAP/IFRS) are explicitly excluded.

**Blockers.**
- No CLO — legal requirements research falls to Simon and Michael.
- Process documentation incomplete — Michael needs ~1–2 days to produce worked examples.
- Some process owners still undefined in the 41-process table (notably customer-facing processes with no current owner assigned).

**Open questions.**
- Final process count: 41 today, likely grows to 400+ when sub-processes are fully mapped.
- Best AI skill architecture: 41 individual skills, 41 agents, or one unified skill with process context?
- Ownership of customer-facing processes (no "head of AI native" equivalent currently assigned).

---

## Monday items touched

- [2882088503 — ISO officer process documentation](https://janusd-company.monday.com/boards/5095012818/pulses/2882088503) — Status: Postponed → In Definition, Source bumped ✅
- [2889155963 — Build ISO facilitation skill for Simon](https://janusd-company.monday.com/boards/5095012818/pulses/2889155963) — Next-step stub added ✅
- [2924556146 — Document AIO process examples](https://janusd-company.monday.com/boards/5095012849/pulses/2924556146) — Created ✅
- [2924562376 — Review Simon's process docs](https://janusd-company.monday.com/boards/5095012849/pulses/2924562376) — Created ✅
- [2924513833 — Discard current skill files](https://janusd-company.monday.com/boards/5095012849/pulses/2924513833) — Created ✅
- [2924559320 — Set up Claude in Excel plugin](https://janusd-company.monday.com/boards/5095012849/pulses/2924559320) — Created ✅
- [2924557920 — Research legal requirements](https://janusd-company.monday.com/boards/5095012849/pulses/2924557920) — Created ✅
- [2924559454 — AI auditor skill](https://janusd-company.monday.com/boards/5095012849/pulses/2924559454) — Created ✅

**Coverage: ✅ 8/8 items covered (6 Step 3G creates, 2 already covered, 0 backfills, 0 failures)**

---

## Linear AIP reconciliation

No AIP issues referenced in this meeting. No reconciliation changes applied.

---

## AI Registry / Tool Evaluation outcomes

| Tool | AIR | Action | Gate 1 |
|---|---|---|---|
| Claude in Excel plugin | AIR-30 | Enriched — ISO meeting demo context, Simon as new target user | Skipped (already in Sandbox) |
| Claude in Word plugin | AIR-81 | Enriched — Simon as new target user, ISO docs use case | Skipped (already Evaluating) |
| Gemini (Google) | AIR-5 | Enriched — Claude-backup role formalised, Sheets-native AI noted | Skipped (already Production) |
| ChatGPT (OpenAI) | AIR-41 | Already registered, no new context — skipped | — |
| Microsoft Excel | AIR-105 | Created (Backlog) — commodity office tool, Claude plugin anchor | Not required |
| Microsoft Word | AIR-106 | Created (Backlog) — commodity office tool, Claude plugin anchor | Not required |
| Google Drive | AIR-107 | Created (Backlog) — Simon's active file storage, Cowork-connected | Not required |
| Google Sheets | AIR-108 | Created (Backlog) — Gemini-native alternative, tooling decision context | Not required |
