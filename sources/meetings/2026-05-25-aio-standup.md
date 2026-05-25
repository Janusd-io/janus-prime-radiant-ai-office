---
type: meeting
title: AIO Standup — 25 May 2026
slug: 2026-05-25-aio-standup
created: 2026-05-25
updated: 2026-05-25
departments: [ai-office, technology]
status: active
captured_by: jehad-altoutou
participants: [jehad-altoutou, michael-bruck]
sources: [2026-05-25-aio-standup]
related: [2026-05-22-aio-standup, 2026-05-22-aio-marketing-meeting, nanoclaw, janus-prime-radiant-build, assessify]
parser_version: 3
standup_skill_version: v3.23
fireflies_id: 01KSF0QM16YB2JW8ZFQ7PG7VG6
---

## Clean Meeting Summary

AIO working session on 25 May 2026 (~87 minutes). Confirmed participants by name: Michael Bruck and Jehad Altoutou. Speaker attribution confirmed via Fireflies name tags.

**Nanoclaw Slack integration demo:** Michael Bruck demonstrated the live Nanoclaw instance running in Docker/VM on his MacBook. Architecture: GitHub read-only access pulls the Prime Radiant vault into a container-local vault. Skills (standup, tool evaluation) are visible and accessible. Slack integration is installed in the Janus workspace — Jehad found it via search — but interactive responses are not yet working (interactive URL not configured in app settings). Michael: "these are the little things we need to get working."

**Multi-tenant Nanoclaw architecture:** Jehad Altoutou proposed deploying Nanoclaw on Hostinger as a multi-tenant system with per-tenant isolation and access control. Michael Bruck raised data isolation concerns (the Viktor/RBAC parallel — don't want everyone sharing the same backend). Resolution: fix and stabilise the current single-user instance first, then evaluate multi-tenant. Jehad: "working on access control is not an issue for me" — ready to build it when the time comes.

**LM Studio + Whisper Large Turbo MLX:** Michael Bruck introduced LM Studio (local LLM runner) and demonstrated Whisper Large Turbo MLX — an MLX-optimised Whisper model for Apple Silicon that runs on GPU and Neural Engine entirely on-device. Michael directed Jehad to install and test it as a potential local transcription alternative to Fireflies for sensitive meetings.

**Engineering hire:** Jehad Altoutou raised the need for engineering support ("two minds is better than one"). Michael Bruck confirmed Bonaventure has approved 2 headcounts for AIO. Profile agreed: junior to mid-level, AI-pilled, fast learner, some full-stack/SaaS coding experience (actual code written, not just vibe-coded), can do code reviews, excited about agentic systems. Michael has Slovak engineering company contacts (Vacuum Labs-type, pre-vetted). Jehad will draft the JD with Claude; Michael will also propose building an AI assessment test for candidate screening (Jehad: "I can build one. It's not an issue.").

**Marketing CLAUDE.md:** Michael Bruck identified that Andrew Soane's marketing Prime Radiant CLAUDE.md is bare-bones (top-level structure only, missing lint/ingest/query workflows, folder schema, high/low-stakes rules). Michael directed Jehad to create a marketing-adapted version based on the AIO CLAUDE.md — remove Linear, Monday, standup skill references; preserve general schema rules — and push it to Andrew's GitHub. Once Andrew runs it on his Mac, the system will build correctly from his transcripts. Jehad: "I'll work on this one. I'll send it to his GitHub."

**Euclid enrollment:** Jehad raised Euclid's Cowork enrollment. Michael said can't proceed without department assignment clarity for Euclid. Blocker owner: Michael to clarify Euclid's department.

**Bonaventure 3pm meeting:** Michael created a multi-agent architecture picture and was presenting it to Bonaventure at 3pm — aligning on the federated knowledge / middle-management coordination vision. Key framing Michael articulated: "What we're building here, nobody as far as I can tell has built anything like this... We're about 12 to 18 months ahead of the industry on this concept." The Prime Radiant pattern (federated institutional knowledge, department-level and corporate-wide) is the first step toward replacing the coordination/communications overhead of middle management with AI agents.

**Tool mentions:** LM Studio (new; AIR-142), Whisper Large Turbo MLX (new; AIR-143), Nanoclaw (enriched; AIR-103), "anti-gravity" (referenced ~10 times as an AI product/IDE; name uncertain from transcript — flagged for confirmation before AIR entry).

---

## 🎯 Today (25 May 2026)

- **Write marketing CLAUDE.md (from AIO template) and push to Andrew's GitHub** (Jehad Altoutou) — Michael directed; Jehad confirmed; unblocks Andrew's Prime Radiant from building correctly | Monday: [2939694038](https://janusd-company.monday.com/boards/5095012849/pulses/2939694038) | Due: Today

---

## 📅 This Week

- **Install LM Studio + test Whisper Large Turbo MLX for local transcription on Mac** (Jehad Altoutou) — Michael introduced + demonstrated; directive to Jehad; evaluate as Fireflies alternative for sensitive meetings | Monday: [2939694488](https://janusd-company.monday.com/boards/5095012849/pulses/2939694488)
- **Fix Nanoclaw Slack interactive responses — configure interactive URL in app settings** (Michael Bruck) — interactive URL not set; blocking Jehad from full Slack interaction with Nanoclaw | Monday: [2939690487](https://janusd-company.monday.com/boards/5095012849/pulses/2939690487)
- **Draft JD for AIO engineering hire (junior, AI-pilled, full-stack)** (Jehad Altoutou + Michael Bruck) — Michael directed; Jehad drafts with Claude; Michael reviews + adds sourcing contacts | Monday: [2939705098](https://janusd-company.monday.com/boards/5095012849/pulses/2939705098)
- **Nanoclaw multi-tenant architecture — review codebase viability + Hostinger deployment plan** (Jehad Altoutou) — Jehad proposed; Michael flagged complexity; agreed to investigate after current instance stabilised | Monday: [2939696937](https://janusd-company.monday.com/boards/5095012849/pulses/2939696937)

---

## 🏔️ Horizon

- **Build AI assessment test for engineering hire candidates** (Jehad Altoutou) — Michael proposed; Jehad confirmed; profile: AI-native skills screen, coding ability, agentic systems reasoning | Monday: [2939696889](https://janusd-company.monday.com/boards/5095012849/pulses/2939696889)
- **Engineering candidate sourcing — reach out to Slovak engineering network** (Michael Bruck) — Michael has contacts at Slovak engineering firm (Vacuum Labs-type, pre-vetted senior/lead engineers on contract) | Monday: [2939694741](https://janusd-company.monday.com/boards/5095012849/pulses/2939694741)
- **Enroll Euclid on Cowork — awaiting department clarification from Michael** (Jehad Altoutou — BLOCKED) — Jehad raised; Michael needs to confirm Euclid's department before enrollment can proceed | Monday: [2939694490](https://janusd-company.monday.com/boards/5095012849/pulses/2939694490)

---

## Registry & Evaluation Outcomes

| Tool | AIR # | Action |
| ---- | ------ | ------ |
| LM Studio | AIR-142 | Created — local LLM/Whisper runner for Mac; Michael introduced; Jehad to test |
| Whisper Large Turbo MLX | AIR-143 | Created — MLX-optimized Whisper for Apple Silicon; runs in LM Studio; local transcription candidate |
| NanoClaw | AIR-103 | Enriched — Slack integration status, Docker/VM architecture, multi-tenant discussion added as comment |
| "Anti-gravity" | — | Name uncertain from transcript (Fireflies artifact likely); flagged — no AIR entry created pending name confirmation |

---

## Context Coverage (Step 3I)

- Items touched: 12 (3 source-bumped + 1 new parent + 8 sub-items)
- Description Updates present: 12/12
- Backfills required: 0
- Move-rationale Updates: 0
- **Coverage: 100% PASS ✓**

---

## Deduplication (Step 2B.1 + Step 3.0)

- Candidates scanned: 8 new sub-items
- HIGH blocks: 0
- MEDIUM flags resolved: 0 (N3 Slack fix distinct from 2934256606 "Build Nanoclaw Slack bot"; N5 multi-tenant distinct from 2931866304 "Deploy to Hostinger")
- Items created: 8

---

## Issues / Warnings

- **"Anti-gravity" tool name uncertain:** Referenced ~10 times in transcript as an AI product/IDE compared to Cowork. Name is likely a Fireflies transcription artefact of another product. No AIR entry created — flagged for Michael to confirm the actual product name before registry entry.
- **Engineering hire parent item:** Created as new parent `2939688504` on the Planned Automations group since no existing hiring-related AIO parent existed.
- **Bonaventure 3pm meeting:** This was a same-day meeting (3pm 25 May). No Monday item created since it was a scheduled meeting, not a trackable task — outcome to be captured in next standup.
- **AIO IT Meeting 21 May** (`01KS5413DKXPT58X77XQMRE629`, ~54 min): Flagged as unprocessed across multiple standup files. Separate standup run required.
