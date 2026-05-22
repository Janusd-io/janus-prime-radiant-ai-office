---
type: meeting
title: AIO Standup 22 May 2026
slug: 2026-05-22-aio-standup
created: 2026-05-22
updated: 2026-05-22
departments: [ai-office]
status: active
captured_by: jehad-altoutou
participants: [jehad-altoutou, michael-bruck]
sources: [2026-05-22-aio-standup]
related: [assessify, nanoclaw, gemini, 2026-05-21-aio-standup]
parser_version: 3
standup_skill_version: v3.23
fireflies_id: 01KS739PFR96MW7MT8EEN2XS79
---

## Clean Meeting Summary

AIO standup on 22 May 2026. Participants: Michael Bruck and Jehad Altoutou (~53 minutes). Attribution: Fireflies speaker labels confirmed as reliable for this recording (named speakers identified correctly).

**ISO documentation:** Jehad delivered a full ISO documentation package to Simon on 7 May (SSFI audit-ready package ~16 pages, IMS AI process elements table, AI tool evaluation process, platform/tool development process). Simon has not responded in 15 days. Bonaventure returns Monday 25 May and is expected to ask; the team needs to prep a status brief showing what's been done. AI tool evaluation skill has been updated to reflect Simon's ISO requirements and needs syncing with Michael's instance.

**Nanoclaw AI eval Slack bot:** Michael plans to prototype today. Architecture: NanoClaude added to AIO Slack channel; monitors for tool suggestions; runs first-pass evaluation using the AI eval framework (sourced from Prime Radiant via GitHub); replies to submitter with feedback; pings AIO team with evaluation + Monday task. Michael is impressed: "only scratching the surface of its capabilities." NanoClaude recently received a VC funding commitment. Deployment to Hostinger + Caddy (replacing Ngrok) is planned to remove the URL-instability issue.

**Gemini landscape:** Google's strategy is to inject Gemini everywhere in its consumer ecosystem (Maps, Travel, Docs, Drive, mobile). ~900 million active users, on par with or passing OpenAI. New video generator released. Gemini small model benchmarks very competitive. Michael's estimate: ~6 months before Gemini seriously challenges Claude in enterprise/developer tooling. Anthropic/Claude context: profitable, doubled revenue, signed 276K-employee deal with a major accounting firm. OpenAI may IPO. Janus posture: stay with Claude; Gemini flagged as API-cost fallback only if needed.

**Marketing / Andrew:** Decision confirmed — zoom into marketing/Andrew as the priority department; stop spreading across multiple departments. Michael coaching Andrew toward task-based AI agent architecture (decompose funnel into tasks + outcomes + tools, not job descriptions). Bonaventure said no to Bangalore hiring. Prime Radiant already migrated to Windows for Andrew; Cowork onboarding happening today. Rosa's marketing workflows reviewed at 11:45. Joyce (Singapore) flagged as potential task-cluster overseer.

**Assessify / SSFI HR:** ~80% built. Mariam actively using it (leave management, org hierarchy, employee DB). DLL confirmed NOT needed (Bonaventure: just a basic contact manager — Assessify already does more). Teresa demo planned for today. Leave views already built per Teresa's request. Outstanding: rubric/scoring metric for recruitment piece (waiting on HR). SSFI/Nomi name change: Andrew to propose internal names. HR ↔ Finance alignment meeting still needed. Fireflies-SSFI webhook for post-interview evaluation being planned (Jehad waiting for rubric and needs to resolve audio access issue first).

**Website LLM-friendliness:** Inspired by Every.to "Read with your agent" approach. Michael: website should be designed not just for human readers but for humans with LLMs — pre-built prompts, companion GitHub repos, LLM-parseable content. Jehad's idea: 3D AI icon / chat interface. Low priority — keep in mind during website redesign. AIO will drive feature direction; Andrew handles content.

**Fireflies audio access blocked:** Jehad is blocked on fetching audio files from Fireflies for voice-print processing (needed for SSFI post-interview evaluation pipeline). Contacting Fireflies support to resolve.

---

## 🎯 Today (22 May 2026)

- **Prototype NanoClaude AI eval Slack bot** (Michael) — add bot to AIO channel, test first-pass eval flow end-to-end | Monday: [2934256606](https://janusd-company.monday.com/boards/5095012849/pulses/2934256606) | Due: today
- **Onboard Andrew on Cowork** (Jehad) — Cowork setup, Prime Radiant walkthrough | Monday: [2928659254](https://janusd-company.monday.com/boards/5095012849/pulses/2928659254) | Due: today
- **Assessify demo for Teresa** (Jehad/Michael) — show leave views + employee DB, confirm no DLL needed | Monday: [2934266264](https://janusd-company.monday.com/boards/5095012849/pulses/2934266264) | Due: today
- **Rosa marketing workflows review** (Jehad) — 11:45 meeting, feed into funnel decomposition | no dedicated Monday item (sub-item of 2928683517)
- **Give Michael latest AI eval skill version** (Jehad) — ensure both instances in sync before Nanoclaw bot prototype

---

## 📅 This Week

- **Prep ISO documentation status brief for Bonaventure** (Jehad) — list all docs delivered to Simon, current status, what's outstanding | Monday: [2934252152](https://janusd-company.monday.com/boards/5095012849/pulses/2934252152) | Due: before Mon 25 May
- **Investigate Fireflies audio access blocked** (Jehad) — contact support, determine plan/permission requirements | Monday: [2934274933](https://janusd-company.monday.com/boards/5095012849/pulses/2934274933)
- **Decompose marketing funnel into task-based architecture** (Jehad + Andrew) — map tasks → outcomes → tools → agents | Monday: [2934252002](https://janusd-company.monday.com/boards/5095012849/pulses/2934252002)

---

## 🏔️ Horizon

- **NanoClaude Hostinger + Caddy deployment** — replace Ngrok for stable URL | Monday: [2931866304](https://janusd-company.monday.com/boards/5095012849/pulses/2931866304)
- **HR ↔ Finance alignment meeting** — define what Finance needs from HR for payroll data fields in Assessify
- **Assessify recruitment rubric** — waiting on HR to deliver scoring/rubric framework before Fireflies webhook can be finalised
- **LLM-friendly website concept brief** — research + brief for Andrew (low priority) | Monday: [2934278925](https://janusd-company.monday.com/boards/5095012849/pulses/2934278925)
- **ISO facilitation skill company-wide rollout** — gated on Simon's feedback (15-day wait as of today) | Monday: [2923830605](https://janusd-company.monday.com/boards/5095012849/pulses/2923830605)
- **NanoClaude rename** — Andrew to propose internal names (also for Nomi/SSFI) | Monday: [2931863368](https://janusd-company.monday.com/boards/5095012849/pulses/2931863368)

---

## Registry & Evaluation Outcomes

| Tool | AIR # | Action |
|---|---|---|
| Gemini (Google) | AIR-5 | Enriched — ecosystem strategy update (900M users, video gen, consumer saturation, 6-month enterprise horizon) |
| NanoClaude / Nanoclaw | AIR-103 | Enriched — AI eval Slack bot use case, VC round, Hostinger+Caddy deployment plan |
| Hostinger | AIR-79 | Enriched — confirmed as NanoClaude production deployment target |
| Caddy (web server) | AIR-133 | Created — open-source reverse proxy, NanoClaude infrastructure layer |

---

## Context Coverage (Step 3I)

- Items touched: 12 (6 source-bumped + 6 created)
- Description Updates present: 12/12
- Backfills required: 1 (2923830605 — Await Simon's ISO confirmation — no prior Description block)
- Backfills completed: 1
- Move-rationale Updates: 0
- **Coverage: 100% PASS ✓**

---

## Deduplication (Step 2B.1 + Step 3.0)

- Candidates scanned: 6
- HIGH blocks: 0
- MEDIUM flags resolved: 2 (Nanoclaw Slack bot vs. chief-of-staff sub-item; ISO brief vs. schema definition sub-item — both cleared after use-case analysis)
- Items created: 6

---

## Issues / Warnings

- **Fireflies audio access** (operational issue, not a tool): Jehad blocked on fetching audio for SSFI voice-print pipeline. Support contact in progress.
- **Simon ISO 15-day wait**: Not a meeting blocker, but flagged as a dependency risk ahead of Bonaventure's Monday return. Status brief being prepared.
- **AIO IT Meeting 21 May** (`01KS5413DKXPT58X77XQMRE629`, ~54 min): Previously identified in Fireflies, not yet processed. Requires a separate standup run.
- **Fireflies speaker attribution**: Recording opened with Michael's microphone not picking up audio initially. Speaker labels validated as reliable for the captured portion — Michael Bruck and Jehad Altoutou confirmed throughout transcript.
