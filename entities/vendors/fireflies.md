---
type: vendor
title: Fireflies
slug: fireflies
created: 2026-05-06
updated: 2026-05-21
departments: [ai-office, hr]
status: active
confidence: high
sources: [aio-2026-05-04, aio-2026-05-05, aio-2026-05-06, 2026-05-11-aio-standup-with-jehad, 2026-04-coordination-leverage-model-v0.3]
related: [michael-bruck, jehad-altoutou, claude, 2026-05-04-centralised-fireflies-webhook-for-interviews, aio-skills-sor-architecture-jehad, 2026-04-20-fireflies-summaries-insufficient-raw-transcript-canonical, april-2026-aio-transcripts-recovery, coordination-leverage-model, organisational-digital-twin, feedback-attribution-from-fireflies]
---

# Fireflies

Meeting transcription and recording platform. Janus's authoritative system of record for "what was said" in meetings — first-class in the `CLAUDE.md` system-of-record map.

**Classification — Core Infrastructure (per [[coordination-leverage-model]] v0.3, §4.2).** Not a productivity tool. Fireflies is the *foundational capture layer* of the [[organisational-digital-twin|organisational digital twin's]] sensor network — it converts tacit-knowledge meeting context (reasoning, alternatives considered, constraints acknowledged, commitments made) into structured queryable data that no transactional system of record can reach. **Every meeting that is not recorded is a sensor that was never installed** — knowledge generated in that room is invisible to the twin and lost to the compounding mechanism. This classification has procurement / SSO / data-residency implications distinct from a Tier-1 SaaS productivity tool.

## Use at Janus

- **AIO daily standups** — every standup is recorded; the transcript becomes the source for the `/standup` skill which writes the consolidated entry to the [[notion]] Operations Notebook.
- **Interview transcripts** — per [[2026-05-04-centralised-fireflies-webhook-for-interviews]], a centralised Fireflies invitee email auto-records recruitment interviews and triggers the post-assessment scoring skill via webhook.
- **Strategic / cross-team meetings** — Bonaventure reframes, Simon ISO discovery, customer/vendor calls — captured for later reference.

## Janus conventions

- **Naming convention:** First-name + First-letter (Microsoft-style), adopted 2026-05-06 — replaces prior less-consistent naming.
- **Custom vocabulary** is configured for Janus-specific terms (per a queued Monday item).
- **Voice-print augmentation** under consideration via [[wispr-flow]] adjacency.

## Relationship to this wiki

Fireflies transcripts are an ingest source for `sources/meetings/` per `CLAUDE.md` §5.1. Default policy: skip recurring 1:1s and team standups (the standup skill already produces the load-bearing summary). Manual override available for transcripts where strategic content sits outside the standup flow.

**Why raw transcripts are canonical, not Fireflies summaries:** see [[2026-04-20-fireflies-summaries-insufficient-raw-transcript-canonical]] — the lesson that drove the wiki's "always use the raw transcript" rule in `CLAUDE.md` §5.1. Fireflies' own summaries are too shallow for decision extraction; they consistently miss the substance Jehad and Michael actually act on.

**Recovery backstop:** Fireflies transcripts are also the source-of-truth fallback when downstream surfaces fail. The [[april-2026-aio-transcripts-recovery]] project is recovering ~22 April 2026 standup entries lost from Notion by re-running raw transcripts through synthesis — a live validation of the Fireflies-as-durable-backstop pattern.

## Watch for

- Webhook reliability once the recruitment-interview pipeline goes live.
- Whether the centralised-invitee pattern generalises beyond interviews (vendor demos, customer interviews).

## Operational improvement items

From Jehad's federated view ([[aio-skills-sor-architecture-jehad]], 2026-05-11) and the AI Office Brain `Systems-of-Record/Fireflies.md` (4 May 2026):

- **Speaker diarisation** is variable quality. Sometimes correctly named ([[michael-bruck|Michael]], [[jehad-altoutou|Jehad]]); sometimes appears as `Speaker 1`, `Speaker 2`. **AIP-13** ("Speaker diarisation for Fireflies") is in Backlog as an improvement project.
- **Custom vocabulary** for Janus-specific terms (team names, tool names like [[wispr-flow|Wispr Flow]] vs Whisper Flow, product names, internal acronyms AIO/AIR/AIP/ISO) tracked on Monday Automations as item `2882206428` (#56 "Configure Fireflies custom vocabulary for team-name transcription").
- **Title convention for standup search:** `AIO DD Mon` (e.g. "AIO 1 May"). `/standup` searches with ±1 day window; typos degrade matching, fallback is `keyword:"standup"`.
- **Quiet-voice capture failure mode** — observed 2026-05-08 Bonaventure meeting transcript missed [[bonaventure-wong|Bonaventure]]'s audio entirely (flagged in the 11 May standup). Mitigation: download the MP3 from Fireflies and rerun through Whisper to recover the missing channel.
