---
type: source
source_type: laptop
title: diagram-prompt-parent-process
slug: diagram-prompt-parent-process
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/examples/ai-department/diagram-prompt-parent-process.md
original_size: 4041
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "ISO/IMS process diagram prompt — AI Department parent process, work content"
project: janus-puls-onboarding

---

# diagram-prompt-parent-process

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/examples/ai-department/diagram-prompt-parent-process.md` on 2026-05-14._

# Diagram Prompt — AI Department Parent Process

> Filled-in example. Paste the prompt block into ChatGPT (GPT-5 or GPT-4o image gen) to generate a high-quality image of the AI Department's parent process diagram.
> See `templates/diagram-prompt.md` for the parametric template.
> Mermaid backup lives inside `parent-process.md` Section 1.

---PROMPT---

Generate a **high-resolution, ultra-wide professional business diagram** (aspect ratio 21:9 or wider, minimum 3840×1620 px) titled **"AI Department — Parent Process Schematic (per ISO 9001:2015 Figure 1)"**.

**Style:** Clean corporate / [[mckinsey|McKinsey]]-style. Flat design, soft drop shadows, rounded corners (8px). White background. Sans-serif typography (Inter / SF Pro). ISO palette: navy `#1A4480` on activity boxes, amber `#996600` on the controls box, deep red `#990000` on the resources box, green `#1B5E20` on the KPI box, mid-grey `#666` on neutral boxes. All arrows clean with arrowheads.

**Layout:** Controls box full width across the top. Below it: Sources → Inputs → Activities → Outputs → Receivers, left to right. Resources box full width across the bottom. KPI box attached to Activities with a dashed line.

**TOP BOX — CONTROLS:**
- Policies · Objectives · Requirements
- ISO 9001:2015 · ISO 27001:2022 · ISO 42001:2023
- UAE · Singapore · UK jurisdictional law

**LEFTMOST BOX — SOURCES OF INPUTS:**
- Internal — meetings (departments / teams)
- Internal — Slack channels
- Internal — [[michael-bruck|Michael Bruck]] (AI Projects lead)
- External vendors — [[anthropic|Anthropic]] · [[openai|OpenAI]] · Vercel · [[hostinger|Hostinger]] · Airwallex · n8n
- External regulators — UAE · SG · UK

**SECOND BOX — INPUTS:**
- Requirements (from meetings or Slack)
- Constraints (stack · infra · budget)
- Access (credentials · API keys · sandbox)
- Strategic direction & approvals

**CENTRAL BOX — ACTIVITIES:** Header "ACTIVITIES — 6-step flow with control points (CP) between each step". Render the six steps left to right with CP markers between them:

1. **Gather Requirements** — meetings or Slack until scope is complete
2. **Build in Sandbox** — develop in isolated environment
3. **Stress Test** — break it across functionality, UI/UX, security, APIs, stability
4. **Fix & Enrol** — patch what testing surfaced
5. **Document** — write SOP, README, implementation plan
6. **Handover to IT** — IT deploys company-wide

**FOURTH BOX — OUTPUTS:**
- Sandbox-tested software
- SOP document · README · Implementation plan
- Documented evidence (test logs · security checks · API records)

**RIGHTMOST BOX — RECEIVERS OF OUTPUTS:**
- Primary: IT Department (deploys company-wide)
- Secondary: End-users in requesting department
- Subsequent processes: C5 · M3 · M4 · M5
- External (when applicable): clients · partners · certification body

**BOTTOM BOX — RESOURCES — Process Owner: Jehad (AI Operations Engineer):**
Four columns:
- **AI Tools:** Claude AI · OpenAI · [[claude-code|Claude Code]] · Codex · Antigravity · AI Gateway
- **Dev Stack:** Next.js 15 · React · TypeScript · Drizzle · n8n · shadcn/ui
- **Infra:** Hostinger VPS · Vercel · Neon Postgres · [[github|GitHub]]
- **Productivity:** Notion · [[linear|Linear]] · Slack · [[obsidian|Obsidian]] Brain

**KPI BOX (dashed line to Activities) — MONITORING & MEASUREMENT:**
- Stress-test pass rate (target 5/5 for handover)
- Critical security findings at handover (target 0)
- Time from requirements to IT handover
- Post-handover defect rate (trended downward)
- AI Systems Register coverage (100% — verified by AI department)

**Footer (centered below diagram):**
"ISO 9001 §8.1 · §7.5 · §8.5.6 · ISO 27001 A.5 · A.8 · ISO 42001 §6.1 · §8.2 — Linear AIR maintained by AI Department as the AI Systems Register."

**Critical:** Render all text legibly. Do not invent or change wording. Wide landscape orientation. Output as a single high-resolution image.

---PROMPT---

**Mermaid backup:** see `parent-process.md` Section 1. Open on GitHub for native rendering or paste into [mermaid.live](https://mermaid.live).
