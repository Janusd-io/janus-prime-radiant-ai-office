---
type: meeting
title: AIO, IT Meeting — 21 May 2026
slug: 2026-05-21-aio-it-meeting
created: 2026-05-21
updated: 2026-06-01
departments: [ai-office, it-ops, office-of-ceo]
status: active
captured_by: jehad-altoutou
participants: [michael-bruck, jehad-altoutou]
sources: [2026-05-21-aio-it-meeting]
related: [2026-05-21-aio-standup, nanoclaw, janus-prime-radiant-build, obsidian]
parser_version: 3
standup_skill_version: v3.23
fireflies_id: 01KS5413DKXPT58X77XQMRE629
---

## Clean Meeting Summary

Cross-functional AIO × IT meeting on 21 May 2026 (~54 minutes). Confirmed participants by name: Michael Bruck (AIO). Speaker 1 is Jehad Altoutou (high confidence — built the Slack bot + NanoClaw installation, manages GitHub scripts). Speaker 3 is an IT team member (likely Andre — discussed Monday, ticketing, asset tracking, mentioned giving the HTML presentation skill to "Andre"). Attribution note: Speaker 1 and Speaker 3 labels only from Fireflies; group attribution used where individual confirmation is absent.

**NanoClaw demo — Slack bot + AIO knowledge base:** Jehad (Speaker 1) demonstrated the Slack bot he built that queries the AIO Prime Radiant knowledge base ("I created a Slack bot that can talk to it. I can in Slack communicate with it, and it pulls up information. I asked Slack, 'What does Euclid do?' — and it answered from the knowledge base."). NanoClaw (AIR-103) was shown as the vehicle for this — running in Docker on Jehad's Mac, connected to Slack. The IT team saw the Prime Radiant knowledge graph visualization and were impressed. Michael: "It's our knowledge base. Completely assembled from all the meetings we've had, all the stuff in Linear and Monday."

**Monday.com company-wide evaluation:** Extended discussion on rolling Monday out beyond AIO and IT sandbox. Agreed target departments: PMO, ops/sender, production, IT. Admin: Google Tasks sufficient. Not all admin roles need Monday. Decision: extend subscription two weeks for full evaluation, then sign off on budget. Speaker 3 (Andre) confirmed he has used Monday for ticketing, asset tracking, and workflow automation. MCP/API coverage confirmed: 100% — "Every function you need to do manually can be done through the API."

**NanoClaw as AI layer for Zendesk IT help desk:** Michael proposed an AI agent between Slack and Zendesk for first-line IT support. Jehad confirmed NanoClaw fits: can connect to any Slack channel, runs in Docker (constrained, not full cowork access), can be configured to access a specific knowledge base or function. Plan: deploy NanoClaw to Hostinger VPS in Docker for company-wide availability (not on laptops).

**Meeting skill for AIO-IT meetings agreed:** Decision to apply the standup/meeting skill to all AIO-IT cross-functional meetings going forward. Monday as the shared coordination surface; IT team gets read visibility into AIO tasks. This 21 May meeting is retroactively processed as the first.

**Notion deprecated (confirmed in this meeting):** Michael confirmed Notion is gone ("So that, that's gone"). Reason: API failures with too much data, token-expensive, redundant with Obsidian. Obsidian + GitHub is the correct stack. Andre (Speaker 3) also suggested migrating his IT knowledge from Notion to Obsidian.

**Janus HTML presentation skill shared:** Speaker 3 (Andre) had polished the Janus HTML presentation skill. Skill shared to IT internal Slack group during this meeting. Michael: "At some point you should share it among the whole company. Anybody can do it."

**IT sandbox / staging environment:** Speaker 3 flagged the need for a dev/staging environment. Michael agreed: budget to be added to the 6-month template. "Any app already developed should go in the sandbox to verify before production."

**Marketing tool selection criteria presented:** Jehad briefed the IT team on AIO's approach to Andrew's marketing tool stack — minimize support overhead, prefer agent-friendly tools (Salesforce = too support-intensive; Cloudflare + Vercel = fully agent-manageable). "The more agent-friendly they are, the less people you need to run it."

---

## 🎯 Today (21 May 2026)

*No immediate Today actions captured — meeting occurred mid-morning; broader actions are this-week or horizon.*

---

## 📅 This Week

- **Confirm Monday.com company-wide rollout scope — PMO, ops, production, IT — budget sign-off** (Michael Bruck): Decision from meeting; extend subscription; add to 6-month budget template. | Monday: [2956596446](https://janusd-company.monday.com/boards/5095012849/pulses/2956596446)
- **Deploy NanoClaw to Hostinger Docker for IT help desk integration** (Jehad Altoutou): Move from Jehad's laptop to Hostinger VPS; wire up Slack → NanoClaw → Zendesk ticket flow. (Note: existing Monday item 2931866304 already tracks this.) | Monday: [2931866304](https://janusd-company.monday.com/boards/5095012849/pulses/2931866304)

---

## 🏔️ Horizon

- **AI agent for IT helpdesk — Slack triage → Zendesk** (Jehad Altoutou): NanoClaw as first-line support layer. After Hostinger deployment. | Monday: [2896117600](https://janusd-company.monday.com/boards/5095012818/pulses/2896117600)
- **Re-assign IT handover sub-items — disaster recovery, access control, SSO, enterprise security** (IT team / Andre): Speaker 3 flagged these need IT ownership and budget. Michael to add sandbox budget to 6-month template. | Monday: [2882218645](https://janusd-company.monday.com/boards/5095012818/pulses/2882218645), [2882216721](https://janusd-company.monday.com/boards/5095012818/pulses/2882216721)

---

## Decisions Made

- Monday.com to be rolled out company-wide (PMO, ops, production, IT as first departments); admin optional
- NanoClaw = candidate AI layer for IT help desk (Slack → Zendesk)
- Meeting skill (standup pipeline) to be applied to all AIO-IT meetings going forward
- Notion deprecated — Obsidian + GitHub is the confirmed stack
- Marketing tool selection principle: agent-friendly, lightweight, minimal support overhead; avoid Salesforce-level complexity
- IT sandbox / staging environment to be budgeted

---

## Registry & Evaluation Outcomes

| Tool | AIR # | Action |
| ---- | ------ | ------ |
| Zendesk | AIR-146 | Created (Production) — IT team's active help desk; AI enhancement via NanoClaw under discussion |
| Monday.com | AIR-83 | Enriched — company-wide rollout discussion; PMO + ops + production + IT target scope |
| NanoClaw | AIR-103 | Existing (Sandbox as of 1 Jun) — demo shown to IT team; Zendesk integration proposed |
| Cloudflare | AIR-116 | Existing (Backlog) — agent-managed deployment confirmed by Michael |
| Vercel | AIR-113 | Existing (Backlog) — agent-managed deployment confirmed |
| Notion | — | Deprecated — confirmed dead in this meeting; no new AIR action |

---

## Context Coverage (Step 3I)

- Items touched: 6 (4 source-bumped + 1 new sub-item — Step 3G + 4 backfills Step 3H)
- Description Updates present: 6/6
- Step 3G creates: 1
- Step 3H backfills: 4 (all 4 source-bumped IT items predated coverage convention)
- Step 3E.1 moves: 0
- **Coverage: 100% PASS ✓**

---

## Issues / Warnings

- **Speaker attribution:** Fireflies returned 3-speaker labels (Speaker 1, Michael Bruck, Speaker 3). Speaker 1 = Jehad Altoutou (high confidence — built Slack bot + NanoClaw, manages GitHub). Speaker 3 = IT team member (likely Andre, given presentation skill context). Group attribution used for Speaker 3 decisions where confirmation is absent.
- **Retroactive processing:** This meeting occurred 21 May 2026 but was not processed until 1 June 2026 (flagged as unprocessed in 4 consecutive standup reports). Some action items from this meeting were already captured in subsequent standups (NanoClaw Hostinger deployment, Notion deprecation).
- **NanoClaw Hostinger deployment:** Existing Monday item 2931866304 already tracks this — not created as a duplicate.
