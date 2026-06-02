---
type: meeting
title: AIO, CEO Meeting — 1 June 2026
slug: 2026-06-01-aio-ceo-meeting
created: 2026-06-01
updated: 2026-06-01
departments: [ai-office, office-of-ceo, technology]
status: active
captured_by: jehad-altoutou
participants: [michael-bruck, bonaventure-wong, jehad-altoutou]
sources: [2026-06-01-aio-ceo-meeting]
related: [2026-06-01-aio-standup, nanoclaw, janus-prime-radiant-build, hgtft, coordination-leverage-model]
parser_version: 3
standup_skill_version: v3.23
fireflies_id: 01KT1A9MZTFQPAMYYP2AN4SZGP
---

## Whiteboard Diagrams

Four diagrams were drawn on the Huawei board during this meeting and redrawn as clean SVGs. Original photos supplied by Jehad.

### ① Data Bank
*Janus as institutional data ledger — the "SWIFT of data" commercial model*

![[01-data-bank.svg|572]]

### ② System Architecture
*GitHub (breach risk) → KB Wiki → Obsidian on JA/MB laptops + VPS NanoClaw — ADIA/GIC counterparties — Singapore context*

![[02-system-architecture.svg|574]]

### ③ AI Pyramid
*Brand + FLD flanking AI Model at apex — DRI (Directly Responsible Individual) middle tier — Strawberry Generation base*

![[03-ai-pyramid.svg|613]]

### ④ Data Rating Ecosystem
*MRI analogy — Singapore AAA Data Rating — Digital Twin → Audit/Verified → Edge Computer → IoT sensors → ADIA/Keppel*

![[04-data-rating-ecosystem.svg|613]]
---

## Clean Meeting Summary

AIO × CEO working session on 1 June 2026 (~90 minutes). Confirmed participants: Michael Bruck, Bonaventure Wong, Jehad Altoutou. First CEO-level briefing on the enrollment V2 autopilot and NanoClaw architecture. Jehad demoed the 5-minute / 7-day enrollment system — Bonaventure understood and approved, confirming Lysander as the pilot. The meeting produced major direction on three fronts: (1) an AI certification training platform to be built on top of the PM knowledge base, (2) multi-messenger NanoClaw access for external third-party contractors using whatever chat platform they already use, and (3) a formal production handover gate requiring IT sign-off before Sandbox → Production in Linear. Bonaventure also articulated two strategic pillars that should anchor future AIO work: "no worker left behind" (upskilling not displacement, with a union strategy for Singapore and UK) and the "SWIFT of data" vision (data provenance as a competitive moat, charging for cross-border data movement like financial transaction fees).

---

## 🎯 Today (1 June 2026)

*No specific today-items beyond what was already in flight (Lysander enrollment, Andrew bootstrap). Bonaventure meeting itself was the today-action.*

---

## 📅 This Week

- **Build certification training platform — modular PM knowledge base quizzes with dynamic content** (Jehad Altoutou + Andrew Soane): Foundation: Lysander's PM vault (being enrolled). Dynamic quizzes per section. Chat-based delivery via NanoClaw. Target: working prototype by end of June. | Monday: [2960117206](https://janusd-company.monday.com/boards/5095012849/pulses/2960117206)
- **Research LinkedIn badge API for Janus certification issuance** (Jehad Altoutou): LinkedIn badges + third-party issuers (Credly, Badgr) + blockchain/NFT option. KYC + anti-cheat requirements. | Monday: [2960121454](https://janusd-company.monday.com/boards/5095012849/pulses/2960121454)
- **Schedule Bonaventure Cowork enrollment — remote setup when available** (Jehad Altoutou): Bonaventure is traveling this week and next; coordinate remotely. Same enrollment V2 process as Andrew + Lysander. | Monday: [2960121746](https://janusd-company.monday.com/boards/5095012849/pulses/2960121746)
- **Establish production sign-off gate — IT (Euclid) co-signs in Linear before Sandbox → Production** (Michael Bruck): Wednesday IT/ops meeting is the venue. Prevents repeat of the Nomi incident. | Monday: [2960118001](https://janusd-company.monday.com/boards/5095012849/pulses/2960118001)
- **Create Cowork enrollment deployment documentation + handover manual for IT** (Jehad Altoutou): Self-service guide for Euclid/Andre: GitHub setup, Obsidian install, Git plugin config, Web Clipper, bootstrap commands. Bonaventure: "give them a documentation that they can do it themselves — then that's it, you're done." | Monday: [2960121841](https://janusd-company.monday.com/boards/5095012849/pulses/2960121841)

---

## 🏔️ Horizon

- **Evaluate NanoClaw multi-messenger connectors — WhatsApp / Discord / WeChat** (Jehad Altoutou): Bonaventure's direction: use whichever messenger the client uses. WhatsApp for Singapore/Middle East; WeChat for China; Discord as an option for external developer communities. | Monday: [2960128240](https://janusd-company.monday.com/boards/5095012849/pulses/2960128240)
- **Data provenance + "SWIFT of data" architecture** (Michael Bruck + incoming CTO John): Bonaventure's strategic vision: Janus becomes the ledger for physical asset data, charges for cross-border data movement like SWIFT charges for financial transfers. Needs FinTech CTO architecture input.
- **Bonaventure enrollment** (Jehad): When he's back in office. All his Fireflies meetings to be ingested (note: some in Chinese — multilingual ingestion already configured).
- **Hostinger → AWS migration** (Jehad): Once NanoClaw is stable on Hostinger; AWS (AIR-150) is the confirmed next step. Google Cloud also a candidate for GPU/TPU inference.
- **Monday.com company-wide rollout finalisation** (Michael): Per-need basis confirmed; department heads decide for their teams. No Monday AI agents — Janus builds their own.

---

## Decisions Made

- **Lysander = first enrollment test user** — confirmed by Bonaventure in this meeting; proceed
- **AI certification training platform** — build on PM knowledge base; modular quizzes; LinkedIn badges; free for Singapore initially; union strategy (Singapore + UK)
- **NanoClaw multi-messenger** — use whatever messaging platform the client uses; NanoClaw handles all backends; WhatsApp first for Singapore
- **Production handover gate** — IT (Euclid/Andre) must sign off in Linear before any tool moves Sandbox → Production; prevents Nomi-style incidents
- **Monday company-wide** — per-need basis; no mandatory rollout; no Monday AI agents; project management use only
- **Obsidian status** — in use in production; governance review pending Wednesday IT meeting (Bonaventure confirmed governance is the only blocker for full Production status in AIR)
- **GitHub** — fine for AIO knowledge base (no client data); data sovereignty only applies when storing client interaction data
- **Hostinger → AWS** — confirmed migration path; timing TBD

---

## Strategic Findings / Bonaventure Vision

**"No Worker Left Behind" principle:** Every AIO product build must pass this test — have we left workers behind? If yes, rethink. The certification platform is the direct embodiment: upskilling existing workers (Singapore electricians, Keppel engineers) rather than displacing them. Union strategy: approach Singapore and UK unions to endorse the Janus certification. Bonaventure: "AI will not repress you, but people with AI will repress people without AI."

**"SWIFT of Data" vision:** Bonaventure is building toward a model where Janus becomes the trusted ledger for physical asset data (sensor data, energy flows, carbon credits). Clients who want to move this data across borders pay a fee — like SWIFT charges for financial transfers. Key competitive moat: Janus can guarantee data provenance (which sensor, where, when, verified) better than any competitor because it built the HGTFT digital twin and understands the ontology. Zero-knowledge proof mentioned for sensor-level provenance guarantees.

**"Data Rating" concept:** Bonaventure proposed a data quality/provenance rating matrix (analogous to S&P credit ratings) for IoT/sensor data. AAA-rated data = provenance-guaranteed, auditable, sensor-specific. This rating would be a competitive differentiator for attracting ADIA, Temasek, GIC as counterparties.

**DRI (Directly Responsible Individual):** Michael noted this term is coalescing as the industry standard for the human accountable for AI output quality. Bonaventure's reaction: "If it makes sense for the market, adopt it."

---

## Registry & Evaluation Outcomes

| Tool | AIR # | Action |
| ---- | ------ | ------ |
| Discord | AIR-147 | Created (Backlog) — external NanoClaw front-end candidate; Keppel engineers |
| WhatsApp | AIR-148 | Created (Backlog) — primary external messaging candidate; Singapore/Middle East |
| WeChat | AIR-149 | Created (Backlog) — China-facing messaging option; regulatory complexity noted |
| AWS (Amazon Web Services) | AIR-150 | Created (Backlog) — Phase 2 hosting target after Hostinger; GPU inference candidate |
| NanoClaw | AIR-103 | Enriched — CEO briefing, multi-backend + multi-messenger confirmed, composability principle |
| LinkedIn | AIR-98 | Enriched — badge API use case added (distinct from existing Lead Gen/Sales Nav use) |

---

## Context Coverage (Step 3I)

- Items touched: 11 (4 source-bumped + 1 new parent + 6 sub-items)
- Description Updates present: 11/11
- Step 3G creates: 7
- Step 3H backfills: 0
- Step 3E.1 moves: 0
- **Coverage: 100% PASS ✓**

---

## Deduplication (Step 2B.1 + Step 3.0)

- Candidates scanned: 6
- HIGH blocks: 0
- MEDIUM flags: 2 (N4 "production sign-off gate" + N5 "deployment documentation" — both cleared by user "Approve execution")
- Items created: 7 (P1 + N1–N6)
- Step 3.0 execution-time blocks: 0

---

## Issues / Warnings

- **Fireflies transcription issue raised in this meeting:** Jehad reported to Fireflies support that this meeting's recording was missing/processing late. Support could not find it. Ongoing reliability concern — backs up the case for LM Studio + Whisper Large Turbo MLX local transcription (from 25 May standup).
- **N5 partial overlap with existing item 2956564999** ("Write enrollment instruction manual"): The two items cover adjacent territory — N5 is IT handover focus; 2956564999 is user-facing setup. Both proceed but should be consolidated or cross-linked when writing.
- **LinkedIn badge use case** may warrant a separate AIR entry for the specific vendor once Jehad identifies the right platform (Credly, Badgr, etc.) — enrichment comment added to AIR-98 as a placeholder.
- **CTO "John"** — incoming CTO referenced by Bonaventure; no entity page exists yet. Note filed for next lint pass.
