---
type: source
source_type: notion
slug: it-discussion-task-tracker
title: IT — Discussion & Task Tracker
created: 2026-05-07
captured_by: jehad-altoutou
notion_url: https://www.notion.so/358114fc090c81c8b2a2cce22a03b53e
audience: department
departments: [ai-office, it-ops]
sensitivity: dept
sensitivity_confidence: 0.5
---

# Purpose
Persistent log of meetings between the **AI Office** (Michael Bruck, Jehad Altoutou) and the **IT Department** (Euclid, Andre, and the incoming IT engineer Tia / Dhya — joining w/c 11 May 2026). Each meeting follows the same format as the daily AIO standup entries in the [AI Office Operations Notebook](https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a) — clean summary, time-bucketed next steps with Monday hyperlinks, decisions, findings, items touched, AIR / evaluation outcomes. Newest meeting at the top.
IT-driven operational tasks live in the new **IT Department** group on the [Automation Plans & Task Tracking](https://janusd-company.monday.com/boards/5095012818) board.

---

## Michael / Jehad / Euclid / Andre — IT Operations Working Session — 7 May 2026
**Attendees:** Michael Bruck, Jehad Altoutou (AI Office), Euclid C. Wong, Andre (IT Department)
**Source transcript:** [Fireflies — Michael, Jehad, Euclid, Andre IT Operations](https://app.fireflies.ai/view/01KR0J82186X2H5MHF1WH48NY6)
**Duration:** 46m

### Clean meeting summary
- Cross-department knowledge architecture decided: Google Shared Drives are the canonical document storage; one drive per department, two folders each (`<Dept>` company-readable + `<Dept> Restricted` department-private), optional third for vendor / project work.
- Permissions managed via Google Groups (`it@janusd.com`, `hr@janusd.com`, `everyone@janusd.com`); new hires inherit access via group membership; department heads are Managers, rest are Contributors.
- AI Office + IT pilot first, then roll out to HR / finance / marketing / ISO / training. Live setup of `IT` group and `IT Restricted` folder during the call.
- Knowledge layer (LLM-wiki / Karpathy-style overlay from yesterday) is a *separate* abstraction on top of the shared drives — not a replacement. File store and knowledge retrieval are distinct concerns.
- Workshop + documented guidelines + onboarding-procedure update queued; Google Sites flagged as the likely portal-as-index option but TBD vs custom Claude-Code build.
- Sync hazards (especially finance Excel on Windows) acknowledged as a known risk needing mitigation in the guidelines.

### Decisions made
- Google Shared Drives = canonical document storage; one per department.
- Two-folder pattern per drive: `<Dept>` (company-readable) + `<Dept> Restricted` (department-private). Optional third for vendor/project work.
- Permissions managed via Google Groups; new hires inherit via group membership.
- Department heads are Managers (Content-Manager in practice for testability); default new-hire role is Contributor.
- AI Office + IT are the pilot departments; rest follow post-workshop.
- Naming convention: "Restricted" preferred over "Private" or "External".
- Shared drives are file store, NOT the knowledge layer — knowledge retrieval is a separate overlay (LLM-wiki track).
- Onboarding procedure must include shared-drive walkthrough + Google Group setup.
- Country-vs-department split deferred — Janus is centrally managed globally; revisit on country growth or local-compliance trigger.

### Key findings / discussions
- Folder-permission UX gotcha in Google: Manager prevents managers being kicked → use Content-Manager for the role most people expect "manager" to mean.
- Sync hazards on Windows + large finance Excel files are a known risk; needs mitigation in the documented guidelines.
- Microsoft SharePoint compared and ruled out (Janus standardised on Google Workspace).
- Best-practice validation step (Gemini / Claude review) added before broad rollout — cheap insurance against a Google-specific gotcha.

---

## AI ↔ IT Department Meeting — 6 May 2026
**Attendees:** Michael Bruck, Jehad Altoutou (AI Office), Euclid, Andre (IT Department)
**Source transcript:** [Fireflies — Ai and IT department meeting](https://app.fireflies.ai/view/01KQYFN8G0DWZW8X8TKKXHQ5VB)
**Duration:** 55m
*Note: Fireflies appears to have mis-attributed many speaker labels between Michael Bruck and Euclid in this recording. Content-based attribution used in this entry — AI Office side = Michael + Jehad; IT Department side = Euclid + Andre.*

### Clean meeting summary
- Cloud (incl. Cowork) and Cloud Code to be added to IT's approved-tools list v3; browser-mode access restricted to enforce app-only usage (token-spike control: $13–$30 spikes observed for non-app users).
- IT department adopts the standup-skill + Monday + Notion stack — Andre is the IT-side pilot lead, mirroring Andrew's role on the marketing pilot. Sibling pilot to validate cross-department generalisability.
- Sandbox→IT handoff procedure formalised: SOP / README / sign-off / formal-test requirements still to define. Andre's important distinction landed — AI projects need *testing*, productivity tools need *deployment* only. ISO remains the gating blocker.
- AI registry scope clarified: Monday / Notion / Deel / Xero / Airwallex are not AI tools and should not be tracked in AIR. Cleanup decision pending.
- AI agent for IT helpdesk approved as a new build — symmetric Slack→triage→Zendesk pattern to the AI Internal Hub bot, replaces today's passthrough Zendesk integration.
- Monday.com Javin call locked for tomorrow at 3pm; Andre sending the Zoom link; multi-workspace structure (per department / per branch) and corporate licensing discount on the agenda.
- New IT engineer (first name Tia, surname spelled D-H-Y-A E-Y-A) joins w/c 11 May — bootstrap via Entra Google Workspace + Notion + Claude markdown-extract trick (Euclid's proven .com→.io migration pattern).

### Decisions made
- Cloud (incl. Cowork) + Cloud Code to be added to IT approved-tools list v3 — listed separately because Cloud Code/Codex is a different domain.
- Cloud browser-mode access restricted; app-only enforcement (token-spike control).
- IT department adopts the standup-skill + Monday + Notion stack — Andre leads IT side; sibling pilot to Andrew's marketing pilot.
- AI registry scope: Monday / Notion / Deel / Xero / Airwallex are not AI tools and should not live in AIR.
- IT helpdesk gets symmetric agentic-feedback-loop bot (Slack triage → Zendesk) replacing today's passthrough integration.
- Software procurement: no individual cards; all new tools require prior approval (Andre owns IT-side approvals).
- Test-vs-deployment distinction (Andre): AI-built projects require sandbox testing; vendor productivity tools require deployment only. Drives the IT-handoff template.

### Key findings / discussions
- IT pilot is the *second* cross-department test of standup methodology (after Andrew). Generalisability claim begins to hold.
- Test-vs-deployment branching prevents ceremony on tools that don't need it (Monday, Gmail) while preserving rigour where it matters (AI agents, integrations).
- Cloud token-spike behaviour confirms app-only as the only practical control surface; browser usage cannot be governed.
- Notion-as-KB scaling concerns reinforced; Obsidian / Karpathy LLM Wiki tracked separately on the data-architecture parent.
- Asana phase-out signal noted ("Asana's gonna go away. We only did Asana for Singapore. It shouldn't be used for anything else." — Euclid). Borderline registry trigger; not dispatched today, surfaced for user confirmation in the Final Execution Report.
- Singapore email setup (`inquiries@janusd.SG` or `.com.SG`) requested by Michael — handled as a side-conversation, not tracked as a Monday item.

---

# Standing context
**IT Department roster:** Euclid (lead), Andre (engineer), Tia / Dhya (engineer joining w/c 11 May 2026).
**No Monday accounts:** Euclid and Andre currently have no Monday accounts — task attribution is narrative only on Monday items. Will revisit once they're set up with Monday users.
**Cadence:** Ad-hoc working sessions between the AI Office and IT Department; first formally tracked meeting is 6 May 2026. Cadence may move to weekly once the IT pilot of the standup skill is running.
**Recurring themes:**
- Sandbox → IT-production handoff (formal SOP, sign-off, test acceptance)
- AI tool approval list governance (what counts as an AI tool, what gets browser-vs-app restrictions)
- IT helpdesk automation (Slack triage → Zendesk replacement)
- Standup methodology rolled out to IT (Andre as pilot lead)
