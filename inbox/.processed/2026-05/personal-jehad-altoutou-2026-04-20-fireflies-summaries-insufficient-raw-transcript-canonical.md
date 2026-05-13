---
type: lesson
title: Fireflies summaries are insufficient — raw transcript must be canonical
slug: 2026-04-20-fireflies-summaries-insufficient-raw-transcript-canonical
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office]
countries: [sg, gb, us]
status: resolved
owner: michael-bruck
confidence: high
sources: [pr-backup-2026-05-11-1432-lesson-fireflies-summaries-insufficient]
related: [fireflies, standup]
audience: [department]
captured_by: jehad-altoutou
---

# Fireflies summaries are insufficient — raw transcript canonical

**Date:** 20–24 April 2026. **Owner:** Michael Bruck. **Status:** Resolved.

## What happened

The AI Office and Janus leadership have been relying on Fireflies' auto-generated summaries to extract decisions and context from recorded meetings. During the week of 20–24 April, across multiple meetings (Bonaventure on 20 Apr, Simon on 22 Apr, Weekly Status review, Bonaventure again on 4 May, IT on 6 May), it became consistently apparent that **Fireflies summaries are too shallow, miss nuance, and sometimes misattribute speaker labels or lose load-bearing context.**

## Why it matters

- **Decisions and nuance get lost:** Bonaventure's reframe on 20 Apr was explicit and load-bearing but Fireflies summaries flattened it into generic CEO-meeting context.
- **Transcripts drive automation:** The `/standup` skill and Claude's processing of meeting context depend on accurate input. Shallow or inaccurate summaries feed poor decision signals downstream.
- **Speaker attribution errors:** The IT meeting on 6 May had notable mis-attributions between Michael Bruck and Euclid.
- **Context loss compounds:** When meetings are chained, loss of nuance in earlier meetings means later meetings lack foundation.

## What we changed

1. **Raw transcripts are now canonical.** Fireflies summaries are reference only. All decision extraction begins from the raw transcript.
2. **Speaker-verification step added:** When attribution is ambiguous, content-based re-attribution is applied before processing.
3. **Standup skill updated** to privilege raw transcript content over Fireflies "Summary" field.
4. **Meeting notes are human-extracted** from raw transcript, not Fireflies summaries.

## Going forward

- [[fireflies]] is a **recording and storage system**, not a summary system.
- Raw transcripts are the canonical input to all downstream processing.
- Human extraction (via the `/standup` skill or manual review) produces the authoritative meeting notes.
- Fireflies summaries may be useful as a starting point for skimming, but never as the basis for decision-making, wiki ingestion, or automation dispatch.
