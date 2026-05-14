---
type: source
source_type: notion
slug: bonaventure-discussion-task-tracker
title: Bonaventure — Discussion & Task Tracker
created: 2026-05-08
captured_by: jehad-altoutou
notion_url: https://www.notion.so/357114fc090c817da4a1fe07c4c4dceb
audience: department
departments: [ai-office]
sensitivity: dept
sensitivity_confidence: 0.5
---

# Purpose
Persistent log of meetings with **Bonaventure Wong** (CEO sponsor of the AI Office programme). Each meeting follows the same format as the daily AIO standup entries in the [AI Office Operations Notebook](https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a) — clean summary, time-bucketed next steps with Monday hyperlinks, decisions, findings, items touched, and Linear / AI Registry reconciliation. Newest meeting at the top.
CEO-related operational tasks now live in a dedicated **Office of CEO** group on the [Automation Plans & Task Tracking](https://janusd-company.monday.com/boards/5095012818) board.

---

## Jehad / Michael / Bonaventure Meeting — 8 May 2026
**Attendees:** Michael Bruck, Jehad Altoutou, Bonaventure Wong *(Fireflies mislabelled all speakers as "Michael Bruck" — known custom-vocab gap, tracked on item [Configure Fireflies custom vocabulary](https://janusd-company.monday.com/boards/5095012818/pulses/2882206428))*
**Source transcript:** [Fireflies — Jehad / Michael / Bonaventure Meeting](https://app.fireflies.ai/view/01KR3MEP5PSM0TS6F92J9PZKJ5)
**Duration:** 49 min

### Clean meeting summary
- Prime Radiant demo'd to Bonaventure mid-meeting — Foundation framing landed; personal → department → CEO vault hierarchy validated as the right shape. Bonaventure: *"This is the beginning of a digital twin. Knowledge."*
- Departmental folders (Marketing, HR, IT, Finance) confirmed as the next addition to Prime Radiant — each folder becomes the connecting node between AI Office and the host department, automatically populated from meeting transcripts.
- Bonaventure raised journalist-dossier feature for the marketing-variant LLM Wiki — track journalists' interests, auto-connect to Janus topics for outbound pitch placement-probability scoring. Logged as a new Engage data architecture sub-item.
- HR Rubik scoring walkthrough — Jehad demo'd SSFI/Assessify pipeline (form intake → scoring → red flags → recommended-experience reroute → JD MCP path). Bonaventure validated the continuous-learning principle: *"Be curious why it's 5… how do we fine-tune our engine when people are not curious."* Every hire / rejection feeds back to refine the rubric.
- Recruitment hire joining next month — owns fine-tuning JDs + scoring rubrics + understanding the "why" behind scores. Onboarding tracked separately on HR Dashboard board (5095636727).
- Skills-transfer workflow walked through end-to-end: project files + skill .md + Cowork. Bonaventure committed to clean up his existing skill kit and migrate from personal to team Cowork project so it can be shared.
- Productisation / upskilling vision: gig-economy marketplace for engineers / lawyers / accountants / reskilled hairdressers, anchored in Singapore PM upskilling push and AI-on-site training. Logged as longer-horizon vision; not actioned today.

### 🎯 Next steps — by next standup
- [ ] [Monday — Prime Radiant](https://janusd-company.monday.com/boards/5095012818/pulses/2900825519) — Demo Prime Radiant to Andrew (Bonaventure portion complete) — Owner: Michael — Due: 9 May

### 📅 This week
- [ ] [Monday — Add departmental folders (Marketing, HR, IT, Finance) to Prime Radiant](https://janusd-company.monday.com/boards/5095012849/pulses/2902026224) — Owner: Both — Due: 13 May
- [ ] [Monday — Help Bonaventure migrate skills from personal to team Cowork project](https://janusd-company.monday.com/boards/5095012849/pulses/2902034399) — Owner: Michael — Due: 13 May

### 🏔️ Longer horizon
- [ ] [Monday — Build journalist-dossier feature (interests + matching) for marketing-variant LLM Wiki](https://janusd-company.monday.com/boards/5095012849/pulses/2902003769) — Owner: Michael — Due: longer
- [ ] [Monday — Bonaventure Prime Radiant variant (CEO-level master view / digital twin)](https://janusd-company.monday.com/boards/5095012849/pulses/2900875344) — Owner: Michael — Due: longer
- [ ] [Monday — Sync with Bonaventure on Rubik scoring methodology on his return](https://janusd-company.monday.com/boards/5095012849/pulses/2898224301) — Owner: Jehad — Due: longer

### Decisions made
- Departmental folders (Marketing, HR, IT, Finance) confirmed as the next Prime Radiant addition.
- Bonaventure variant of Prime Radiant (CEO-level master view) endorsed — to be built once personal + department layers stabilise.
- Journalist-dossier feature added to the marketing-variant LLM Wiki roadmap.
- Continuous-learning principle for HR Rubik scoring confirmed — every hire / rejection feeds back to refine the rubric.
- Skills-transfer flow confirmed: project files + skill .md + Cowork (skill download → recipient loads into their Claude; project files shared separately via team workspace).
- Bonaventure committed to clean up and migrate his skill kit to a team Cowork project before sharing.

### Key findings / discussions
- Foundation reference (Asimov / Hari Seldon / Prime Radiant) recognised by Bonaventure — "digital twin" framing accepted as the end-state.
- Bonaventure's hiring example (5.5-score candidate hired against scorecard advice; gap was 1-of-4 fault-detection on transcript) crystallised why the engine has to keep learning from outcomes — both successful hires and rejections.
- JD-to-role rerouting (engine suggesting an alternate role for a candidate based on transcript analysis) flagged as the engine's strongest moment — worth investing in the multi-JD matching dimension.
- Janet has access to the Google Drive backup of the canonical Prime Radiant vault — backup status ✅.
- The Sender (per Michael) uses Obsidian extensively — possible internal SME after his current training cycle ends; he's a long-time project manager (claimed 20 years), more product / PM than technical.
- Productisation security model (separate hosting, role-based access, Pinecone for vault security) acknowledged as the long-pole productisation work — not blocking near-term internal deployment.

---

## Bonaventure / Michael / Jehad / Andrew Meeting — 4 May 2026
**Attendees:** Michael Bruck, Bonaventure Wong, Jehad Altoutou *(Andrew listed in the title but not labelled as a speaker — likely silent or briefly present)*
**Source transcript:** [Fireflies — Bonaventure, Michael, Jehad and Andrew Meeting](https://app.fireflies.ai/view/01KQSAG8Q4JYBB63VZ5XXM750Y)
**Duration:** 1h 13m

### Clean meeting summary
- Designed the AI tool evaluation pipeline end-to-end: Slack intake → Claude triage agent → human review → policy gates → sandbox → IT hand-off, with Bonaventure validating each stage as CEO sponsor.
- Slack intake form fields locked: URL, submitter name, timestamp, location, organisation. No approval gate at submission — friction-free entry; duplicate-check is the bot's first activity, not the form's.
- Linear AIR confirmed as the system of record for the AI Tools Registry — *"that's why we update Linear and everything; it becomes part of the knowledge base, it's compounded knowledge."*
- AI-policy gate is binary 4-of-4 (data training, Google integration, security, …). Failing any criterion = reject. Rejection records reason + approver name; "reject (garbage)" vs "watch list" distinguished.
- Standup skill is the orchestrator dispatching sub-skills (AI Registry, AI Evaluation) — approved as the new way of working; confidence-scoring rubric (≥90% silent / 60–80% confirm / <60% ask) endorsed.
- Long-term vision: company-wide single source of truth / digital twin, role-based compartmentalisation, eventually external-facing (NDA / GDPR concerns flagged).
- Cowork is in active use but **not yet formally approved** — Jehad flagged, Bonaventure acknowledged.

### Decisions made
- Slack intake form fields and friction-free submission policy (no approval gate at submission).
- Linear AIR is the system of record for the AI Tools Registry.
- AI-policy gate is binary 4-of-4; rejection records reason + approver name.
- Standup skill is the central orchestrator that dispatches `/ai-registry` and `/ai-tool-evaluation` sub-skills.
- Confidence-scoring rubric for the standup skill (≥90% silent / 60–80% confirm / <60% ask) endorsed.
- Bonaventure agreed to be the next test case for applying the standup-skill methodology to a non-AI-Office workstream.

### Key findings / discussions
- No good auto-categoriser exists for AI tools yet — comparables search is blocked on this gap. Hercules vs Lovable / Replit / Claude Design / Google Stitch was the conversation that exposed it.
- Sandbox scoring rubric still needs refinement; IT hand-off template doesn't exist yet.
- Enterprise Claude licensing economics deferred (cost vs ~50-user minimum).
- External-facing version of the methodology raises NDA / GDPR / role-based compartmentalisation work — long-term vision but not blocking near-term.
- Fireflies summary explicitly distrusted as a primary signal — *"crap"*, "out of context"; the raw transcript is canonical.

---

## Bonaventure Reframe Meeting — 20 Apr 2026
Full analysis lives on a dedicated child page: [Bonaventure Meeting — Reframe Analysis (20 Apr 2026)](https://www.notion.so/348114fc090c81878e5cdb8ef46fff44)

## Weekly CEO Update — 6 Apr 2026
Referenced in the [AI Office Operations Notebook](https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a) compact archive. Full content in the source Fireflies recording.
