---
type: meeting
title: AIO, CEO, Emma Training, PM Meeting — 3 June 2026
slug: 2026-06-03-aio-ceo-pm-training-meeting
created: 2026-06-03
updated: 2026-06-03
departments: [ai-office, office-of-ceo, training]
status: active
captured_by: jehad-altoutou
participants: [bonaventure-wong, michael-bruck, emma-mccall, rosa-wu]
sources: [2026-06-03-aio-ceo-pm-training-meeting]
related: [2026-06-01-aio-ceo-meeting, janus-prime-radiant-build, emma-mccall, rosa-wu, lysander-liu]
parser_version: 3
standup_skill_version: v3.23
fireflies_id: 01KT6EV9F19AHFRQSCCZJDN805
---

## Attribution Note

Recorded on Michael Bruck's Fireflies account (`michaelb@janusd.com`). Jehad's recording was corrupted. Speaker attribution confirmed per Jehad Altoutou:
- **Bonaventure Wong** — CEO (confirmed by Fireflies name tag)
- **Michael Bruck** — AIO (confirmed by Fireflies name tag)
- **Speaker 3 = Emma McCall** — Head of Certification/Training (first day; new hire joining 29 June 2026)
- **Speaker 4 = Rosa Wu** — PM; head of project management knowledge base

---

## Clean Meeting Summary

First onboarding session for Emma McCall as Head of Certification/Training, 3 June 2026 (~78 minutes). Bonaventure Wong and Michael Bruck briefed Emma on the Janus AI vision and the certification programme; Rosa Wu presented the PM knowledge base. Michael gave a live demo of the Prime Radiant (Obsidian knowledge graph), querying it on certification programme design — the system correctly referenced the June 1 CEO meeting's decision to build the certification training, and surfaced Lysander's 28-phase workflow as the "canonical content backbone." Rosa showed her PM workflow spreadsheet (templates and manuals for all 28 phases) and the AWS simulation environment (fake BMS server with 1-year historical data) for hands-on training. The meeting confirmed: BMS engineers are the primary certification target; Singapore is the pilot; Emma and Rosa need a dedicated knowledge-transfer session before Emma designs modules; internal Janus staff also need an AI onboarding training package.

---

## 🎯 Today / This Week

- **Schedule Emma McCall × Rosa Wu knowledge transfer** (Emma + Rosa + Michael): Rosa presents PM workflow + Emma presents certification design methodology — mutual exchange before module design begins | Monday: [2966076290](https://janusd-company.monday.com/boards/5095012849/pulses/2966076290) | Before Emma's start date (29 June)

---

## 📅 This Month (before Emma starts 29 June)

- **Create internal Janus staff AI onboarding training** (Michael Bruck + Emma McCall): Gemini/Claude effective use, HTML presentations, prompt engineering, context engineering, agents vs chat distinction. "Big missing piece in our own onboarding" — Bonaventure. | Monday: [2966148396](https://janusd-company.monday.com/boards/5095012849/pulses/2966148396)

---

## 🏔️ Horizon

- **Design modular certification programme for BMS engineers** (Emma McCall, with AIO support): Based on Emma × Rosa knowledge transfer. Singapore pilot first; UK second. Train-the-trainer model. LinkedIn badges + gamification. On-demand + structured learning dual-mode.
- **Ingest Rosa's PM knowledge base into PM Prime Radiant** (Rosa Wu + Jehad): Google Drive folder, 28-phase spreadsheet index, phase-by-phase templates and manuals. Currently all translated to English.
- **Build virtual BMS training sandbox** (Rosa Wu + AIO): AWS simulation environment (already exists with 1-year fake building data). Needs to be integrated into the certification platform for hands-on labs.
- **Enroll Emma McCall on Cowork + Prime Radiant** (Jehad): Emma starts 29 June. Add to GitHub, Obsidian, Monday, Claude Cowork. Her meetings with the team will auto-ingest into the knowledge base from day 1.

---

## Decisions Made

- **"Training" → "Certification"**: Renamed to avoid displacement narrative — certifying existing engineers to connect with Janus tools, not retraining them for new roles
- **BMS engineers = primary target group** confirmed for Singapore pilot
- **Singapore pilot** → UK second lighthouse → 10 countries by year-end
- **Train the trainer model**: Senior engineers certified first; they train the younger ones
- **Build bespoke system** (not buy LMS): AI makes coding easy enough; commercial platforms 1-2 generations behind
- **Internal staff AI training gap identified**: Missing from current Janus onboarding; Emma and Michael to build it
- **Emma McCall start date: 29 June 2026**

---

## Key Insights — Certification Design (Emma McCall's framework)

1. **Start from what they know.** Adult learning principle: known → unknown. Don't drop engineers into brand-new concepts. Start with the pipes they already know, then show how Janus connects to them.
2. **Mixed abilities require tailored paths.** Senior tenured vs junior; technical vs non-technical. AI enables personalised learning at scale — "same end result, different paths."
3. **On-demand learning vs structured courses.** Quick queries before a client meeting = on-demand. Skill acquisition = structured course. Both are needed; different tools for different modes.
4. **Continuous assessment.** Not a single final exam — checkpoints throughout. Rosa confirmed: some roles already have practice-based certification (build a floor to get certified).
5. **Overcoming psychological barriers.** Fear vs excitement spectrum. Trust-building through familiar starting points reduces resistance.
6. **Labs are critical.** Michael's Intel/Azure course experience: reading and videos are OK; hands-on lab on a real (or simulated) system is the most effective. Rosa's AWS simulation environment addresses this.

---

## Key Insights — Strategic Vision (Bonaventure)

- **"They feel part of us because they know as much as we know."** The goal of the knowledge base is to give certified engineers on-demand access to the same institutional knowledge Janus has — ask any question, get the answer from the combined knowledge of Rosa/Lysander/Spike/all meetings.
- **Build vs Buy: Build is coming back.** AI makes bespoke development cost-competitive with SaaS. Commercial LMS platforms are 1-2 generations behind what Janus can build. "Go to a tailor, have a bespoke suit made."
- **Agent-as-a-service** is the longer-term product: demonstrate internally first, then deploy externally as a product offering.
- **Data provenance flywheel**: Engineers using the tools → their work interactions feed back into the knowledge base → the next engineer gets better answers → better certification outcomes → tighter feedback loop.

---

## Key Insights — Rosa Wu's PM Knowledge Base

- **28-phase PM delivery workflow** is the primary content backbone for the certification programme. Lysander walked through all phases in earlier meetings; this content is now in the Prime Radiant.
- **Simulation environment**: AWS-hosted fake BMS server with 1-year historical building data. Engineers can practice installation, configuration, and sensor reading on a system that behaves exactly like a real building without any risk.
- **Python/TypeScript tools**: Rosa has built data collection automation for the PM workflow. Also building TypeScript tools that eliminate the need for AI inference for routine regional data collection (regions don't need AI to use them — AI was used to build them, not to run them).
- **Deep Talk** mentioned: a Slack-connected agent that searches developer/product documentation to answer engineer questions. Check AIR.

---

## Registry Outcomes

| Tool/Entity | Action |
|---|---|
| Emma McCall | Entity page created: `entities/people/emma-mccall.md` |
| Rosa Wu | Entity page already exists (created May 2026) |
| Deep Talk | FLAG — check AIR; mentioned by Rosa as Slack agent for product docs search |
| Kaggle | SKIP — Jehad's personal interest, mentioned in passing, no operational context |
| AWS | AIR-150 (Backlog) — simulation environment confirmed as running on AWS |

---

## Context Coverage

- Items touched: 3 (source bump on 2960121648 + 2 creates)
- Description Updates: 3/3 ✓
- **Coverage: 100% PASS ✓**
