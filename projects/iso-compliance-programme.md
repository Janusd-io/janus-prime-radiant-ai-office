---
type: project
title: ISO Compliance Programme
slug: iso-compliance-programme
created: 2026-05-07
updated: 2026-05-13
departments: [iso, it-ops, ai-office, office-of-ceo]
status: active
owner: michael-bruck
sources: [aio-2026-05-01, aio-2026-05-04, aio-2026-05-05, aio-2026-05-06, simon-iso-programme-discovery-2026-04, bonaventure-reframe-analysis-2026-04-20, 2026-05-11-aio-standup-with-jehad, 2026-05-12-bonaventure-ai-native-call, jehad-vault-iso-compliance-programme]
related: [iso, simon-tarskih, bonaventure-wong, michael-bruck, jehad-altoutou, ai-tool-evaluation, standup, wispr-flow, 2026-05-01-iso-compliance-gate-before-automation, 2026-04-20-iso-first-stack-architectural-pivot, ai-native-janus-positioning]
---

# ISO Compliance Programme

Hub for Janus's ISO compliance work. Top priority for [[bonaventure-wong]]; working partnership between [[michael-bruck]] (programme owner) and [[simon-tarskih]] (ISO programme facilitator). Multi-process scope — not just documentation, but aligning the AI Office's existing process stack against ISO standards.

## Why this is its own project hub

ISO compliance has been showing up across the wiki as a *gate* on other work — automation projects blocked behind it, the standup skill iterating toward ISO alignment, `ai-tool-evaluation` needing ISO-compliance work. That cross-cutting role means it earns a dedicated narrative hub rather than being scattered across decision pages and Monday items.

Per [[2026-04-20-iso-first-stack-architectural-pivot]], Bonaventure reordered the executive-management-system architecture so ISO-compliant workflows come first. That reframe is the upstream constraint on much of Janus's 2026 build work.

## Scope

Multi-track programme:

| Track | What | Owner | Status |
|---|---|---|---|
| **ISO documentation foundation** | Input → activities → output template captured for Janus's processes (the work Simon facilitates). | [[simon-tarskih]] | Recurring blocker — Michael following up across multiple AIO standups. |
| **AI Tool Evaluation framework ISO alignment** | Make [[ai-tool-evaluation]]'s gates and dossier requirements ISO-compliant. | [[michael-bruck]] + Simon Tarskih | Active. |
| **Standup skill v3.x ISO alignment** | Skill v3.x continues iterating until ISO-aligned; v2.1 stays in production until v3 ships. | [[jehad-altoutou]] | Active. |
| **ISO facilitation skill build** | New Claude skill scaffolding Simon's facilitated sessions; candidate consumer of [[wispr-flow]] for voice capture. | [[jehad-altoutou]] | In definition. |
| **ISO compliance gate enforcement** | Per [[2026-05-01-iso-compliance-gate-before-automation]] — automation projects can't begin until ISO documentation for the relevant scope is complete. | [[michael-bruck]] | Policy active. |

## Roles

- **Sponsor:** [[bonaventure-wong]] — top priority; sets bar alongside Simon for ISO interpretation.
- **Programme owner:** [[michael-bruck]] — coordinates across tracks; recurring follow-up with Simon.
- **Working partner / ISO facilitator:** [[simon-tarskih]] — facilitates documentation sessions.
- **Engineering:** [[jehad-altoutou]] — builds the ISO facilitation skill, advances standup skill v3.x toward ISO alignment.

## Cross-references

- Decisions driving this programme: [[2026-04-20-iso-first-stack-architectural-pivot]], [[2026-05-01-iso-compliance-gate-before-automation]].
- Tools / vendors implicated: [[wispr-flow]] (voice capture for facilitation), [[claude]] (skill substrate), [[notion]] (Operations Notebook journal where Simon's framings live), [[fireflies]] (transcripts of facilitated sessions).
- Adjacent process: [[ai-policy-gate-approval]] — separate but adjacent governance gate; ISO is foundational, AI Policy gate is operational.

## Open / pending

- Get the ISO documentation references from Simon (recurring blocker on AIO standups).
- Confirm Wispr Flow Gate 1 outcome — voice-capture readiness for the ISO facilitation skill.
- Scope which Janus processes need ISO-aligned documentation first; surface order from Simon + Bonaventure agreement.

## Watch for

- Bonaventure's expectations on ISO interpretation alignment with Simon's interpretation — divergence here is the key risk.
- ai-tool-evaluation framework version that incorporates ISO-aligned dossier requirements.
- Standup skill v3.x reaching ISO-aligned production state (will trigger broader rollout per [[it-department-standup-pilot]] and [[2026-05-06-andrew-as-standup-skill-rollout-pilot]]).

## 2026-05-11 — PULS programme detail and Jehad's onboarding deliverables

*Source notes ingested 2026-05-11 from [[jehad-altoutou|Jehad]]'s `07 ISO IMS PULS/` Obsidian section (federated personal-vault content authored by Jehad) and the AIO 11 May standup transcript.*

**PULS = Predictive Unified Live System.** The programme deliverable concretises to three things: (1) **20 IMS process documents** in [[notion]] — Core 10, Support 3, Management 5, Additional 2 — plus 11 IMS Manual policy documents above them; (2) the **PULS dashboard** showing real-time status of every process; (3) the **whole system deployable as a template** to every new entity (10 entities this year, 20/yr from 2027).

**Standards.** ISO 9001:2015 (quality) + ISO/IEC 27001:2022 (information security) + ISO/IEC 42001:2023 (AI governance — brand new). Integrated: one IMS, one audit, one certificate. Janus already evidences the bulk of 42001 today: [[linear]] AIR is the AI Systems Register, [[ai-tool-evaluation|/ai-tool-evaluation]] runs the Impact Assessments (Gates 1-4), and [[standup|/standup]] v3.10+ auto-chains evaluation when a new tool is registered — "no AI tool enters use without an Impact Assessment."

**Process Owners Map.** [[jehad-altoutou]] is proposed Process Owner for **C1 — AI System Design & Development**, **C2 — Software Development & Release**, and **S2 — IT Infrastructure & Data Governance**. Awaiting [[michael-bruck]]'s formal sign-off. M1 and M5 likely Michael / Top Management. C3–C10 (except C9), S1, S3, M2–M4, A1, A2 have no obvious owner from the current org chart — Jehad's recommended next move is a half-day with Michael to lock 60% of these.

**Open Questions for Simon (11 live items, last reviewed 2026-05-11, unchanged since 2026-05-08).** Q1 ownership of C1/C2/S2; Q2 form codes F1–F8 physical vs digital; Q3 Stage 4 approval authority delegation; Q4 re-evaluation cadence (Stage 9); Q5 HR architecture (Option 1 Integrated + migration trigger vs Option 2 Decentralized); Q6 Appendix A naming; Q7 does Linear AIR satisfy 42001 §6 AI Systems Register or is a Notion mirror needed; Q8 is Obsidian acceptable as §7.5 documented information; Q9 Gates 1–4 criteria alignment with [[ai-tool-evaluation|/ai-tool-evaluation]]; Q10 tool sunset/decommission stage; Q11 Path B Slack-webhook intake pre or post certification. Three items have been blocked on Jehad for 3 days as of 2026-05-11: send the gap-analysis reply, ping Michael for ownership conversation, send First Voice form.

**Deliverables-as-code.** All procedural documents live in a private GitHub repo, [`Jehada-Janusd/janus-puls-onboarding`](https://github.com/Jehada-Janusd/janus-puls-onboarding), cloned locally at `/Users/jehad/Documents/janus-puls-onboarding`. 11 documents (README + files 01–10) covering plain-English overview, the 3-sentence email to Simon, the 5-task breakdown, the formal AI Ops Engineer response (covers C1, C2, S2 at activity level), jargon decoder, send-ready First Voice answers, Meeting → Task → Build workflow (implements Activity 1 of the AI Ops process; underlying skill [[standup|/standup]] v3.11), Tool Evaluation Procedure v0.4 (maps to Simon's IMS-PRC-AI-001; needs v0.5 alignment), Platform Development Process (9 stages; [[assessify]] worked example), and a Gap Analysis vs Simon's v0.4 (10 specific gaps, ~3 dev-days to close). Word doc exports via pandoc on Desktop.

**IMS Enrolment skill.** Jehad built `/ims-enrolment` — a Claude Desktop skill that walks any Janus department through ISO 9001 Figure 1 documentation, producing a parent process doc, sub-process docs per activity, First Voice questionnaire, and Word-doc handover bundle for Simon. Output drops on the Desktop (`~/Desktop/<Department> - IMS Enrolment/`) so any team member can find a dept's bundle without knowing internal paths. AI Department ships as the worked example. Skill bundle is 20 files / ~3500 lines at v1.1, distributable to other dept heads from the same GitHub repo (`skills/ims-enrolment/`). See proposed AIO process page `ims-enrolment` (to be created).

**Tracks update.** The earlier table's tracks all remain active. Two clarifications: (a) the "ISO facilitation skill build" mentioned in the original Tracks table is the same artefact as the `/ims-enrolment` skill now shipping; (b) the four documents in the AI Ops Engineer's repo (07, 08, 09 + the formal response 04) cover the activity-level content for C1, C2, and S2 — what's missing is the full seven-section structure with Controls + Monitoring + Resources + Outputs filled in formally.

**Janus Pulse onboarding skill (Michael's complementary build).** Per the 11 May standup, the `/janus-pulse` (working title) onboarding skill owned by [[michael-bruck]] is in progress — 22 references; GitHub backend; goal: a person installs the skill, it asks dept + name, creates a GitHub repo, runs a daily cron, fetches sources, builds a personal vault. Designed to expand beyond Cowork users (regular Claude chat). Sits alongside (not in place of) the `/ims-enrolment` skill owned by [[jehad-altoutou]] — `/ims-enrolment` onboards a department to ISO documentation; `/janus-pulse` onboards an individual to the personal-vault pattern that feeds the department [[janus-prime-radiant-build|Prime Radiant]] instance.

**Simon's enrolment deferred.** The 11 May standup discussed whether to enrol [[simon-tarskih|Simon]] in the personal-vault pattern today; the meeting concluded: hold off until Simon has a clear use case. [[andrew-soane|Andrew]] is the active test case; [[euclid-wong|Euclid]]'s project-management team is the next pilot (Wednesday meeting). The standup-methodology-rollout planning that initially lived as an empty placeholder at vault root has been retired — that content properly belongs in the Marketing vault per the federation pattern. See [[it-department-standup-pilot]] for the IT-Ops sibling pilot and [[marketing-prime-radiant]] for Andrew's instance.

## 2026-05-12 — Bonaventure check-in on the AI Native call

Bonaventure asked about ISO programme progress at end of the 12 May call ([[2026-05-12-bonaventure-ai-native-call]]): *"How are you guys doing for your department? I'm going to have a call with Simon later but I want to make sure that it kind of coming through clearly with regards to the evaluation side and how quickly can we adopt this across everywhere. The key thing is what do we need for every department to prepare for that journey?"*

- **`/ims-enrolment` skill explained on the call** — Jehad's skill (currently at v1.1, 22 reference documents, GitHub-distributable) walks any department through ISO 9001 documentation: parent process doc, sub-process docs per activity, First Voice questionnaire, Word handover bundle for Simon. Bonaventure's response: *"All right, let's start with that and see how that works out for all the departments. I'm sure we're not the only ones that solving this problem, there must be people touching on this."* — i.e., proceed with current track.
- **"Encapsulation" as the visual framing.** Bonaventure: *"I keep thinking about encapsulation because it kind of gives a lot of people visual on the sense of this is how we manage the task. And it's control task. It's not like it's all over the place... that way people kind of understand. Okay, I understand what you're talking about."* This framing is worth threading through the ISO programme's external comms — encapsulation as the visual metaphor for the ISO control discipline.
- **Bonaventure 1:1 with Simon today.** Following on from this call. Worth aligning with Simon afterwards on what Bonaventure asked / committed to.
- **AI Native positioning ties in.** Per [[ai-native-janus-positioning]], the ISO compliance evidence trail is now part of the trust layer under the [[ai-native-janus-positioning|three-pillar pitch]]. Externalisability of the compliance evidence is a sales-asset consideration, not just a regulatory hedge.
- **Bonaventure's longer-term direction:** *"the next thing I think what we need to move towards is how do we create the AI agents on top of that... the brain, if we're adding this and it's organising it by itself, that alone is already the beginning of your AI native."* Strong signal that the Prime Radiant + ISO programme + agent-on-top stack is what he sees as the path to Janus's "AI Native" identity.
