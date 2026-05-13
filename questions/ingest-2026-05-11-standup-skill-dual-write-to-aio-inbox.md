---
type: question
title: Standup skill dual-write — add markdown-to-AIO-inbox alongside Notion
slug: ingest-2026-05-11-standup-skill-dual-write-to-aio-inbox
created: 2026-05-11
updated: 2026-05-11
departments: [ai-office]
status: active
owner: jehad-altoutou
sources: [2026-05-11-aio-standup-with-jehad]
related: [standup, notion, janus-prime-radiant-build, michael-bruck, jehad-altoutou]
audience: [department]
captured_by: jehad-altoutou
---

# Standup skill dual-write — add markdown-to-AIO-inbox alongside Notion

Escalation per AIO CLAUDE.md §5.1 high-stakes ("anything where confidence is low or rumor and the change is durable"). The decision was discussed and provisionally agreed in the **AIO 11 May 2026 standup** (Jehad + Michael, Fireflies ID `01KRAZJ9RN9TSNASHPCPD8NS9S`). Filing here so it lands as a `decisions/` page on Michael's next ingest pass rather than relying on the standup transcript getting ingested (which is normally skipped per §5.1).

## Proposed action

Extend the `/standup` skill (currently v3.13) so that — **in addition to** writing the daily standup journal entry to Notion — it also writes a markdown version of the same content to `<AIO Prime Radiant>/inbox/<YYYY-MM-DD>-aio-standup.md`.

Notion writes stay alive (existing flow unchanged). The new inbox write runs in parallel. The AIO ingest pass then processes the markdown per §5.1 — extracting decisions, lessons, action items into the wiki structure.

## Exact transcript evidence

> **Note:** the transcript these quotes come from had Fireflies-misattributed speakers; specific attribution to Jehad or Michael in the quote blocks below should not be relied on. The substance of the exchange is accurate; who said what is not.

> **Jehad:** "Tweak our skill for the standup — in addition to writing to Notion, also write a markdown to the inbox. On the shared one… within the standup skill, whatever it writes to Notion, write a markdown version of that. To the inbox."
>
> **Michael:** "Okay. Yeah. But we need to keep it as a — I'm thinking what kind of section we need to create for that specific thing… if you push the our standup into we need to push it to the cloud."
>
> **Jehad:** "Push it into inbox. Inbox, it's empty, except what's been processed."

## Reasoning

The standup is the AIO's most decision-dense daily artefact. Today, its decisions live in Notion (Operations Notebook, daily AIO entries) and only land in the AIO Prime Radiant when Michael explicitly clips or references them. The dual-write turns every standup into a first-class wiki source — no manual curation required, no "I should remember to bring that into the wiki later" lag.

The AIO CLAUDE.md §5.1 currently has a default rule: *"Skip recurring 1:1s and team standups by default. The standup skill already handles standups separately; double-ingesting wastes effort."* The dual-write doesn't violate this — it changes WHERE the standup skill writes (Notion + AIO inbox), and the inbox ingest replaces what would have been a separate Fireflies ingest. Net effect: less duplication, not more.

## Open questions for Michael (raised in the meeting)

1. **Section routing.** The meeting raised the question "what kind of section we need to create for that specific thing." Three options:
   - **(a) Goes straight to `sources/meetings/`** — treat the standup markdown as a meeting source like any other Fireflies-ingested transcript; the §5.1 pass extracts decisions/lessons into the right folders.
   - **(b) Dedicated `sources/standups/` subfolder** — standups get their own section because they're a distinct artefact type (synthesised, not raw transcript).
   - **(c) Both** — standup writes to a new `sources/standups/<date>-aio-standup.md` AND mirrors the structured content as decision/lesson candidates that ingest extracts.

   Recommendation: **(b)** — dedicated subfolder. The standup output is already a synthesised, structured artefact (Final Execution Report + Notion entry). It's not a raw transcript and shouldn't sit alongside `2026-05-08-andrew-marketing-prime-radiant.md` in `sources/meetings/`.

2. **What gets written.** Two options:
   - **(i) The Notion entry verbatim** (formatted as markdown).
   - **(ii) A structured wiki-ready summary** — frontmatter + sections for Decisions, Action Items, Tool Mentions, Subagent Activity, AIP Conflicts.

   Recommendation: **(ii)** — write a structured markdown that the §5.1 ingest pass can consume directly. The Notion entry stays as the journal; the inbox file is the wiki-ready synthesis. Both derived from the same Meeting Intelligence Digest.

3. **Order.** Should the inbox write happen before or after the Notion write? Recommendation: **after**, mirroring the existing Phase 3 priority (Monday → Linear AIP → Notion → Inbox Markdown → Final Report).

4. **Failure mode.** If the inbox write fails (Drive offline, path missing), should it block the run? Recommendation: **no** — log under Final Execution Report and continue. Existing Notion-failure pattern in §5.1 applies.

## What would resolve this

A short note from Michael on (1) routing, (2) what-gets-written, and any objections to (3)/(4). Then I update the `/standup` skill — likely a new Phase 3 step between Notion write and Final Report — and ship as v3.14.

## Source

AIO 11 May 2026 standup transcript (Fireflies). Full transcript available via Fireflies ID `01KRAZJ9RN9TSNASHPCPD8NS9S`. The transcript itself is **not** being ingested per §5.1 default (standups are skipped); this escalation captures only the standup-skill-modification decision.
