---
type: question
slug: update-iso-compliance-programme
title: Proposed update to projects/iso-compliance-programme.md
created: 2026-05-11
updated: 2026-05-11
status: active
owner: jehad-altoutou
audience: [department]
departments: [ai-office]
captured_by: jehad-altoutou
target_page: projects/iso-compliance-programme.md
---

# Proposed update to projects/iso-compliance-programme.md

**Reason:** Existing AIO project hub for the ISO programme. New material in this chunk: PULS branding and its concrete deliverables (20 process docs + dashboard + template-per-entity), Jehad's proposed C1/C2/S2 ownership, the 11-item Open Questions for Simon tracker, the janus-puls-onboarding GitHub repo, the /ims-enrolment skill, and the full Process Owners Map. None of this contradicts the existing hub; it enriches the Scope and Open/pending sections. Recommend appending a dated section rather than rewriting existing content.

**Patch block** (append to existing canonical page):

---

## 2026-05-11 — PULS programme detail and Jehad's onboarding deliverables

*Source notes ingested 2026-05-11 from Jehad's `07 ISO IMS PULS/` Obsidian section.*

**PULS = Predictive Unified Live System.** The programme deliverable concretises to three things: (1) **20 IMS process documents** in Notion — Core 10, Support 3, Management 5, Additional 2 — plus 11 IMS Manual policy documents above them; (2) the **PULS dashboard** showing real-time status of every process; (3) the **whole system deployable as a template** to every new entity (10 entities this year, 20/yr from 2027). See `iso-ims-puls-programme` and `iso-ims-20-process-documents`.

**Standards.** ISO 9001:2015 (quality) + ISO/IEC 27001:2022 (information security) + ISO/IEC 42001:2023 (AI governance — brand new). Integrated: one IMS, one audit, one certificate. Per `iso-ims-three-iso-standards`, Janus already evidences the bulk of 42001 today: Linear AIR is the AI Systems Register, `/ai-tool-evaluation` runs the Impact Assessments (Gates 1-4), and `/standup` v3.10+ auto-chains evaluation when a new tool is registered — "no AI tool enters use without an Impact Assessment."

**Process Owners Map.** [[jehad-altoutou]] is proposed Process Owner for **C1 — AI System Design & Development**, **C2 — Software Development & Release**, and **S2 — IT Infrastructure & Data Governance**. Awaiting [[michael-bruck]]'s formal sign-off per `iso-ims-process-owners-map`. M1 and M5 likely Michael / Top Management. C3-C10 (except C9), S1, S3, M2-M4, A1, A2 have no obvious owner from the current org chart — Jehad's recommended next move is a half-day with Michael to lock 60% of these.

**Open Questions for Simon (11 live items, last reviewed 2026-05-11, unchanged since 2026-05-08).** Q1 ownership of C1/C2/S2; Q2 form codes F1-F8 physical vs digital; Q3 Stage 4 approval authority delegation; Q4 re-evaluation cadence (Stage 9); Q5 HR architecture (Option 1 Integrated + migration trigger vs Option 2 Decentralized); Q6 Appendix A naming; Q7 does Linear AIR satisfy 42001 §6 AI Systems Register or is a Notion mirror needed; Q8 is Obsidian acceptable as §7.5 documented information; Q9 Gates 1-4 criteria alignment with `/ai-tool-evaluation`; Q10 tool sunset/decommission stage; Q11 Path B Slack-webhook intake pre or post certification. Full tracker in `iso-ims-open-questions-for-simon`. Three items have been blocked on Jehad for 3 days as of 2026-05-11: send the gap-analysis reply, ping Michael for ownership conversation, send First Voice form.

**Deliverables-as-code.** All procedural documents live in a private GitHub repo, [`Jehada-Janusd/janus-puls-onboarding`](https://github.com/Jehada-Janusd/janus-puls-onboarding), cloned locally at `/Users/jehad/Documents/janus-puls-onboarding`. 11 documents (README + files 01-10) covering plain-English overview, the 3-sentence email to Simon, the 5-task breakdown, the formal AI Ops Engineer response (covers C1, C2, S2 at activity level), jargon decoder, send-ready First Voice answers, Meeting → Task → Build workflow (implements Activity 1 of the AI Ops process; underlying skill `/standup` v3.11), Tool Evaluation Procedure v0.4 (maps to Simon's IMS-PRC-AI-001; needs v0.5 alignment), Platform Development Process (9 stages; Assessify worked example), and a Gap Analysis vs Simon's v0.4 (10 specific gaps, ~3 dev-days to close). Word doc exports via pandoc on Desktop. See `iso-ims-external-repo-janus-puls-onboarding`.

**IMS Enrolment skill.** Jehad built `/ims-enrolment` — a Claude Desktop skill that walks any Janus department through ISO 9001 Figure 1 documentation, producing a parent process doc, sub-process docs per activity, First Voice questionnaire, and Word-doc handover bundle for Simon. Output drops on the Desktop (`~/Desktop/<Department> - IMS Enrolment/`) so any team member can find a dept's bundle without knowing internal paths. AI Department ships as the worked example. New AIO process page proposed: [[ims-enrolment]]. Skill bundle is 20 files / ~3500 lines at v1.1, distributable to other dept heads from the same GitHub repo (`skills/ims-enrolment/`).

**Tracks update.** The earlier table's tracks all remain active. Two clarifications: (a) the "ISO facilitation skill build" mentioned in the original Tracks table is the same artefact as the `/ims-enrolment` skill now shipping; (b) the four documents in the AI Ops Engineer's repo (07, 08, 09 + the formal response 04) cover the activity-level content for C1, C2, and S2 — what's missing is the full seven-section structure with Controls + Monitoring + Resources + Outputs filled in formally.

Load-bearing supporting concept also added in this chunk: [[iso-9001-figure-1-schematic]] — the shape every IMS process document follows.

