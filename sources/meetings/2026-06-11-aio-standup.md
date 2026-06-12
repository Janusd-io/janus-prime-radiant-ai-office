---
type: source
source_type: meeting
title: AIO Standup 11 Jun 2026
slug: 2026-06-11-aio-standup
created: 2026-06-11
captured_by: jehad-altoutou
fireflies_id: 01KTTJW2RSYJJE0ZXPWV34WETX
fireflies_url: https://app.fireflies.ai/view/01KTTJW2RSYJJE0ZXPWV34WETX
attendees: [Michael Bruck, Jehad Altoutou]
duration_min: 33
audience: department
departments: [ai-office]
standup_skill_version: v3.24
parser_version: 3
related: [2882205554, 2939688504, 2988245235, 2988239191, AIR-60, AIR-56, AIR-18, AIR-104, AIR-26, AIR-99, AIR-162, AIR-95, AIR-22, AIR-32, AIR-155, AIR-149, AIR-110, AIR-118, AIR-111, AIR-92, AIR-156, AIR-164, AIR-165, AIR-166, AIR-97]
---

## Clean Meeting Summary

Michael and Jehad held a short, dense standup dominated by a live audit of the Linear AIR registry. They found the "ledger" had drifted from reality — in-use tools sitting in Backlog, parked tools in Sandbox, duplicates and MCP noise — and made roughly twenty-five explicit status decisions on the spot, while agreeing the systematic fix is a periodic lint/verification process. Michael set out his plan to re-run the marketing CRM requirements assessment, this time grounded in the Prime Radiant operational knowledge base, and the pair firmed up the dual-mode (UI-to-headless "autonomy slider") requirement and the decision to run their own AI harness (Agent SDK + Slack bot) rather than rely on any CRM's built-in AI. The senior engineer hiring direction was confirmed around product-hardening experience, with Michael interviewing CTO candidate Jun later today. Obsidian sync issues (Jehad disabled sync yesterday after clashes) and standup-skill noise/lag were flagged for diagnosis.

## 🎯 Next steps — by next standup

- **Action:** Diagnose standup-skill Linear sync lag and backlog noise. **Owner:** Jehad. **Time horizon:** by next standup. **Due:** 12 Jun 2026. **Monday:** [sub-item 2988239191](https://janusd-company.monday.com/boards/5095012849/pulses/2988239191)
- **Action:** Re-run CRM requirements assessment via Prime Radiant KB (existing sub-item "Prime Radiant CRM comparison analysis"). **Owner:** Michael. **Time horizon:** by next standup. **Due:** 12 Jun 2026. **Monday:** [parent 2882205554](https://janusd-company.monday.com/boards/5095012818/pulses/2882205554)

## 📅 Next steps — this week

- **Action:** Define the Linear AIR lint/verification process (scope, triggers, comparison sources). **Owner:** Michael + Jehad. **Time horizon:** this week. **Due:** 17 Jun 2026. **Monday:** [item 2988245235](https://janusd-company.monday.com/boards/5095012818/pulses/2988245235)
- **Action:** Progress senior-engineer search (candidates shortlisted) alongside Jun/Austin CTO interviews. **Owner:** Michael. **Time horizon:** this week. **Due:** 17 Jun 2026. **Monday:** [item 2939688504](https://janusd-company.monday.com/boards/5095012818/pulses/2939688504)

## 🏔️ Next steps — longer horizon

- **Action:** Build the AI harness (Agent SDK headless + Slack bot + UI widgets) as the standard interface to CRM/Martech tooling. **Owner:** Michael + Jehad. **Time horizon:** post-CRM-selection. **Due:** TBD. **Monday:** [parent 2882205554](https://janusd-company.monday.com/boards/5095012818/pulses/2882205554) (architecture captured in 11 Jun Update)

## Decisions made

- Re-run the CRM assessment with Prime Radiant operational knowledge (not the pre-Andrew requirements-list-only version).
- Selected CRM must support the full autonomy slider — legacy UI through fully headless; Janus runs its own LLM harness, CRM built-in AI reserved for non-Cowork users/geographies.
- Registry audit status calls (executed in Linear same-day): Nemo Claw → Rejected; Run Bear → Deprecated; Perplexity → Deprecated; Airwallex → Production; Gamma → Sandbox; Canva → Sandbox (evaluation bypass flagged — chat with Euclid); Slack → Sandbox (G1.4 opt-out still pending); Draw.io, Dify, Replit, Gmail MCP, WeChat, Nomi, Google Calendar MCP → Rejected; Resend and Mailchimp duplicates merged; "Whisper flow" corrected to Wispr Flow.
- New CEO-suggested tools registered: Gong, Twelve Labs, VAPI (Solace already existed — enriched).
- Build a periodic Linear AIR lint/verification process; skill should move tool statuses when transcripts say so.
- Senior engineer hire: product-hardening/shipped-product profile confirmed over raw coding skill.

## Findings / context

- Linear drift root cause: the team works through agents and rarely opens Linear — drift accumulates invisibly. Michael frames Linear as the company "ledger" (banking analogy); systems of record must be lint-checked.
- Standup skill "acting weird" since a recent update — backlog noise (stray MCPs), sync lag. Jehad to diagnose.
- Obsidian sync: Jehad disabled sync yesterday to avoid clashes; Michael's pushes weren't landing. Needs re-enable + conflict resolution (journal-only; no Monday item per Jehad's call).
- Twenty open question for Felix follow-up: external LLM API key handling / bring-your-own-LLM; MCP from Cowork as alternative path.
- Registry enrichment quality notably improved since Prime Radiant access ("it even tells you where it came from — May 19th").
- Prime Radiant won Andrew over; he retains UI attachment — validates dual-mode requirement.
- Boris Cherny (Claude Code) no longer opens an IDE — manages loops end-to-end; reinforces pace-of-change and the hardening-skills hire rationale.
- Today: Lysander meeting 16:00–17:00; "budget stuff" for Ann/Andrea evaluation pending.

## Monday items touched

- [Marketing automation / CRM evaluation (2882205554)](https://janusd-company.monday.com/boards/5095012818/pulses/2882205554) — source bump, assessment/harness Update, next-step stub
- [AIO engineering hire (2939688504)](https://janusd-company.monday.com/boards/5095012818/pulses/2939688504) — source bump, senior-direction Update, next-step stub
- [Linear AIR registry lint — periodic status verification process (2988245235)](https://janusd-company.monday.com/boards/5095012818/pulses/2988245235) — created (Michael + Jehad, In Definition)
- [Diagnose standup-skill Linear sync lag and backlog noise (2988239191)](https://janusd-company.monday.com/boards/5095012849/pulses/2988239191) — created (Jehad; dedup-flagged, user-confirmed)

Coverage: ✅ 4/4 items, ⚠️ 0 backfilled, ➡️ 0 move-rationales, ❌ 0 coverage failures

## External / Other-Department Follow-ups

- **Action:** CTO candidate process (Jun interview today; Austin in frame). **Owner:** Michael / CEO office. **Time horizon:** this week. **Monday:** excluded by AI Office Ownership Gate
- **Action:** Budget evaluation items for Ann/Andrea. **Owner:** Finance/Ann. **Time horizon:** unclear. **Monday:** excluded by AI Office Ownership Gate
- **Action:** Chat with Euclid about Canva bypassing the evaluation process. **Owner:** Michael (governance conversation). **Time horizon:** this week. **Monday:** excluded by AI Office Ownership Gate (logged on AIR-99)
- **Action:** Slack global ML model opt-out email to feedback@slack.com. **Owner:** Org/Workspace Owner (IT/Michael). **Time horizon:** this week. **Monday:** excluded by AI Office Ownership Gate (blocker logged on AIR-162)

## Linear AIP reconciliation

- No AIP issues matched this standup's content. 0 applied, 0 conflicts.

## AI Registry / Tool Evaluation outcomes

- **Audit batch (19 actions):** statuses, rejections, merges and corrections per Decisions above. Notables: Resend canonical = AIR-118 (AIR-101 → Duplicate); Mailchimp canonical = AIR-111 (AIR-100 → Duplicate); only one Canva entry existed (no merge needed); Nomi rejected as internal product (suggest AIP tracking); Google Calendar MCP rejected as noise (conservative scope).
- **New entries + chained Gate 1:** Gong AIR-164 — **BLOCKED** (G1.4 conditional: MSA/DPA training clause unsighted; Fireflies overlap + Salesforce dependency noted). Twelve Labs AIR-165 — **BLOCKED** (ToS training licence would fail G1.4; Bedrock-only route viable; parked pending use case). VAPI AIR-166 — **BLOCKED** (4/5 pass; gating item = capture Bonaventure's use case, owner Jehad; ZDR ~$1k/mo for training exclusion). Solace AIR-97 — **Gate 1 PASS** → Evaluating; Stage 2 = zero-cost desk review of open-source Solace Agent Mesh vs alternatives for Prime Radiant federation.
- **Registry gaps flagged for next review:** Grok has NO AIR entry despite sandbox use; Gemini Code Assist has no dedicated entry; Attio appears twice (AIR-76 / AIR-94) — likely unmerged duplicate; Jules (AIR-33) and Kimi (AIR-82) need owner decisions.
