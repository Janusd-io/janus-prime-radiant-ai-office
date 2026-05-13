---
type: question
slug: update-fireflies
title: Proposed update to entities/vendors/fireflies.md
created: 2026-05-11
updated: 2026-05-11
status: active
owner: jehad-altoutou
audience: [department]
departments: [ai-office]
captured_by: jehad-altoutou
target_page: entities/vendors/fireflies.md
---

# Proposed update to entities/vendors/fireflies.md

**Reason:** Personal fireflies.md is solid but misses two concrete operational details from the AI Office Brain: AIP-13 (speaker diarisation improvement) and Monday Automations item #56 (`2882206428`, custom vocabulary configuration). Both are useful cross-references when transcripts surface diarisation or vocabulary issues.

**Patch block** (append to existing canonical page):

---


## Operational improvement items

From AI Office Brain `Systems-of-Record/Fireflies.md` (4 May 2026). Source: [[aio-brain-sor-fireflies]].

- **Speaker diarisation** is variable quality. Sometimes correctly named (Michael Bruck, Jehad Altoutou); sometimes appears as `Speaker 1`, `Speaker 2`. **AIP-13** ("Speaker diarisation for Fireflies") is in Backlog as an improvement project.
- **Custom vocabulary** for Janus-specific terms (team names, tool names like Wispr Flow vs Whisper Flow, product names, internal acronyms AIO/AIR/AIP/ISO) tracked on Monday Automations as item `2882206428` (#56 "Configure Fireflies custom vocabulary for team-name transcription").
- **Title convention for standup search:** `AIO DD Mon` (e.g. "AIO 1 May"). `/standup` searches with ±1 day window; typos degrade matching, fallback is `keyword:"standup"`.

