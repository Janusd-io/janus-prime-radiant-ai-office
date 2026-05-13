---
type: source
notion_url: https://www.notion.so/358114fc090c81c8b2a2cce22a03b53e
notion_id: 358114fc-090c-81c8-b2a2-cce22a03b53e
title: IT — Discussion & Task Tracker
source_type: notion-page
fetched: 2026-05-06
---

# IT — Discussion & Task Tracker

Persistent log of meetings between **AI Office** (Michael Bruck, Jehad Altoutou) and **IT Department** (Euclid, Andre, incoming engineer Tia/Dhya joining w/c 11 May 2026). Follows standup format.

## Latest: AI ↔ IT Department Meeting — 6 May 2026

**Attendees:** Michael Bruck, Jehad Altoutou (AI Office), Euclid, Andre (IT Department)
**Duration:** 55m
**Source:** Fireflies

### Summary highlights

- **Cloud (incl. Cowork) + Cloud Code added to IT approved-tools list v3** — listed separately because Cloud Code/Codex is different domain.
- **Cloud browser-mode access restricted; app-only enforcement** (token-spike control: $13–$30 spikes observed for non-app users).
- **IT department adopts standup-skill + Monday + Notion stack** — Andre is IT-side pilot lead (sibling pilot to Andrew's marketing pilot).
- **Sandbox→IT handoff procedure formalised:** SOP / README / sign-off / formal-test requirements still to define. Andre's distinction: AI projects need *testing*, productivity tools need *deployment* only. ISO remains gating blocker.
- **AI registry scope clarified:** Monday / Notion / Deel / Xero / Airwallex are NOT AI tools — should not be in AIR. Cleanup pending.
- **AI agent for IT helpdesk approved** — symmetric Slack→triage→Zendesk pattern to AI Internal Hub bot, replaces passthrough integration.
- **Monday.com Javin call locked for 7 May, 3pm** — Andre sending Zoom link; multi-workspace structure + corporate discount on agenda.
- **New IT engineer (Tia/Dhya E-Y-A) joins w/c 11 May** — bootstrap via Entra Google Workspace + Notion + Claude markdown-extract.

### Key decisions

- Cloud + Cloud Code added to IT approved-tools v3 (separate entries).
- Cloud browser-mode restricted; app-only enforcement.
- IT adopts standup-skill + Monday + Notion — Andre leads IT side.
- AI registry scope: Monday / Notion / Deel / Xero / Airwallex are NOT AI tools.
- IT helpdesk gets symmetric agentic-feedback-loop bot (Slack triage → Zendesk) replacing passthrough integration.
- Software procurement: no individual cards; all new tools require prior approval (Andre owns IT-side approvals).
- Test-vs-deployment distinction (Andre): AI-built projects require sandbox testing; vendor productivity tools require deployment only.

### Key findings

- IT pilot is *second* cross-department test of standup methodology (after Andrew). Generalisability claim begins to hold.
- Test-vs-deployment branching prevents ceremony on tools that don't need it (Monday, Gmail) while preserving rigour where it matters.
- Cloud token-spike behaviour confirms app-only as only practical control surface.
- Notion-as-KB scaling concerns reinforced; Obsidian / Karpathy LLM Wiki tracked separately.
- **Asana phase-out signal noted:** *"Asana's gonna go away. We only did Asana for Singapore. It shouldn't be used for anything else."* (Euclid). Borderline registry trigger; not dispatched today.

### Monday items created/touched

- Created **IT Department** group on board 5095012818.
- **Apply standup-skill methodology to IT department workstream** — In Definition, High.
- **AI agent for IT helpdesk (Slack triage → Zendesk)** — In Definition, Medium.
- **Onboard new IT engineer (Tia/Dhya — w/c 11 May)** — In Definition, High.
- Updated 7 existing items (Source bumped to AI/IT Mtg 6 May).

### Linear AIP reconciliation

- No AIP-N references. AIP-21 conflict still carried (4 standups consecutive across AIO 4/5/6 May) — recommend manual review.

### AI Registry outcomes

- **None this round.** All mentions gated out except **Asana (borderline deprecation signal, flagged for user confirmation, not dispatched).**

---

## Standing context

**IT Department roster:** Euclid (lead), Andre (engineer), Tia/Dhya (engineer joining w/c 11 May).

**No Monday accounts yet** — Euclid and Andre have no Monday accounts; task attribution narrative-only. Will revisit once they're set up.

**Cadence:** Ad-hoc working sessions; first formally tracked meeting is 6 May 2026. May move to weekly once IT pilot of standup skill is running.

**Recurring themes:**
- Sandbox → IT-production handoff (formal SOP, sign-off, test acceptance)
- AI tool approval list governance (what counts as AI tool, browser-vs-app restrictions)
- IT helpdesk automation (Slack triage → Zendesk replacement)
- Standup methodology rolled out to IT (Andre as pilot lead)

---

## How to maintain

For each new AI-Office ↔ IT-Department meeting:
1. Add new `## <title> — DD Mon YYYY` section at top.
2. Use standup template: Attendees, Source, Summary, 🎯 / 📅 / 🏔️ next steps, Decisions, Findings, Monday items, Linear AIP, AIR outcomes.
3. IT tasks live in **IT Department** group on board 5095012818. Cross-cutting items in Operations/Office of CEO.
4. Per Step 3G of standup skill, every new Monday item gets Description Update immediately.
