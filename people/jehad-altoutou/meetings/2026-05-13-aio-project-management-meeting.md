---
type: source
source_type: meeting
title: "AIO, Project Management Meeting"
slug: 2026-05-13-aio-project-management-meeting
created: 2026-05-13
captured_by: jehad-altoutou
attendees: [euclid-wong, jehad-altoutou, michael-bruck, rosa]
duration_min: 97
fireflies_id: 01KRGKF94R785XZNVKGKTB840J
audience: "departments:ai-office,it-ops"
departments: [ai-office, it-ops]
dept_scope: [ai-office, it-ops]
sensitivity: dept
task_tracker: monday
parsed_at: 2026-05-15T09:25:59Z
parser_version: 3
summary: Michael and Jehad walked Euclid and Rosa (IT/Ops project-management side) through the Janus Prime Radiant — the Obsidian + Claude Code + GitHub knowledge brain the AI Office has been running for six weeks — to seed the third departmental instance after AI Office and Marketing
topics: [janus-prime-radiant, it-ops-onboarding, github-substrate, speaker-tagging, claude-code, obsidian, privacy-classification, notion-deprecation]
decisions: [2026-05-13-it-ops-prime-radiant-starts-with-project-management, 2026-05-13-github-replaces-google-share-drive-as-prime-radiant-substrate, 2026-05-13-let-claude-propose-vault-structure-not-architect-top-down, 2026-05-13-tomorrow-2pm-it-ops-scoping-meeting-in-chinese, 2026-05-13-deprecate-notion-from-aio-stack]
action_items_count: 7
confidence_overall: high
---

# AIO, Project Management Meeting

**Date:** 2026-05-13
**Attendees:** [[euclid-wong]], [[jehad-altoutou]], [[michael-bruck]], [[rosa]]
**Duration:** 97 min
**Fireflies:** [original meeting](https://app.fireflies.ai/view/01KRGKF94R785XZNVKGKTB840J)

---

## Summary

Michael and Jehad walked Euclid and Rosa (IT/Ops project-management side) through the Janus Prime Radiant — the Obsidian + Claude Code + GitHub knowledge brain the AI Office has been running for six weeks — to seed the third departmental instance after AI Office and Marketing. The session covered the architecture (markdown files as the data store, kebab-case slugs, frontmatter, the inbox-as-single-entry-point discipline, Claude.md as the per-vault rulebook), the recent substrate decision to abandon Google Shared Drive in favour of GitHub for cross-user sync, and the speaker-tagging discipline Fireflies requires for the brain to capture entity edges correctly. Rosa pushed for IT/Ops to be split into a separate identity covering both product and project management work (internal standardised procedures + external client delivery), distinct from the existing 'operations' (support) scope, and the call was made to start with the project-management facet first and let Claude propose the structure rather than architecting it top-down. A live ingest demo on Michael's laptop processed 122 inbox files end-to-end, surfacing duplicate handling, orphan files, OCR for images, and the privacy/sensitivity classifier as concrete next-build items. A scoping meeting was scheduled for tomorrow 2-3pm where Rosa and Lysander will explain — in Chinese, with Fireflies transcribing — what they do, what their inputs and outputs are, so Claude can seed the IT/Ops project-management vault. Notion was flagged as a likely casualty of the new stack.

## Decisions

- [[2026-05-13-it-ops-prime-radiant-starts-with-project-management]] — IT/Ops Prime Radiant scopes to project-management first, separate from 'operations'
- [[2026-05-13-github-replaces-google-share-drive-as-prime-radiant-substrate]] — GitHub replaces Google Shared Drive as the Prime Radiant sync substrate
- [[2026-05-13-let-claude-propose-vault-structure-not-architect-top-down]] — Each new departmental Prime Radiant lets Claude propose its directory structure from transcripts,...
- [[2026-05-13-tomorrow-2pm-it-ops-scoping-meeting-in-chinese]] — Schedule an IT/Ops scoping meeting tomorrow 2-3pm, conducted in Chinese, Fireflies-transcribed
- [[2026-05-13-deprecate-notion-from-aio-stack]] — Likely deprecation of Notion from the AIO operating stack

## Action items

- [ ] @michael-bruck Accept the pending Janusd-io GitHub organisation invitation (check .io vs .com — invite sent to the .io org). (due: 2026-05-14; raised by @euclid-wong) — Monday
- [ ] @rosa Tag every speaker in the Fireflies transcript of this meeting before sharing it onward — only the recording's owner can do this in Fireflies. (due: 2026-05-13; raised by @michael-bruck) — Monday
- [ ] @rosa Share the tagged Fireflies recording of this meeting with Euclid / the AIO team (or grant Fireflies access so Claude can pull it via MCP). (due: 2026-05-14; raised by @euclid-wong) — Monday
- [ ] @rosa Run a Chinese-language scoping meeting tomorrow 2-3pm with Lysander, explaining IT/Ops project-management work (inputs, outputs, goals, procedures) as if onboarding a new joiner; Fireflies transcribes. (due: 2026-05-14; raised by @euclid-wong) — Monday
- [ ] @euclid-wong Create a starter Prime Radiant template repository for the IT/Ops project-management instance (analogous to the marketing template he built with Andrew). (due: 2026-05-14) — Monday
- [ ] @euclid-wong Ingest tomorrow's Chinese scoping transcript and use it to propose the initial IT/Ops project-management vault directory structure via Claude. (due: 2026-05-15) — Monday
- [ ] @rosa Provide both the Chinese-language source documents and any existing internal procedure documents (the DOC files Rosa mentioned, including ones with embedded screenshots) for ingest into the IT/Ops vault. (due: 2026-05-15; raised by @euclid-wong) — Monday

## 🎯 This week

- @euclid-wong Stand up the IT/Ops project-management Prime Radiant from a template, seed it from the Chinese scoping transcript, and iterate the directory vocabulary with Rosa and Lysander.
- @team Continue the AIO/IT-Ops collaboration on a privacy/sensitivity classifier that marks files private vs shareable in the front-matter and routes private items so they never sync to GitHub. (raised by @michael-bruck)
- @jehad-altoutou Continue working on duplicate-detection inside the Prime Radiant ingest pipeline (Jehad flagged he is actively on dupes during the live demo).

## 🏔️ Long horizon

- Every Janus employee and every department gets a Prime Radiant, federating into a company-wide digital twin where decisions, lessons, vendor intelligence and synthesis are durably captured and queryable. (owner: @michael-bruck; horizon: year)
- Rollout sequence after AIO + Marketing: IT/Ops (now), then ISO, then HR, then Finance — each as its own Prime Radiant with a shared schema but emergent per-department directory vocabulary. (owner: @michael-bruck; horizon: quarter)
- Migrate off Notion entirely once the Prime Radiant has absorbed its synthesis-layer use cases; treat the Claude-to-Notion MCP latency and token cost as evidence the architecture is wrong. (owner: @michael-bruck; horizon: weeks)
- Find a durable solution for image-heavy and multimodal content (screenshots, PDFs, block diagrams) inside a markdown-first Prime Radiant — store images in an indexable side store and link from markdown via OCR / metadata. (owner: @euclid-wong; horizon: weeks)
- Move the brand of the system from 'Prime Radiant' to whatever cross-product naming methodology Andrew (Marketing) eventually proposes — Nomi, Mios, and Prime Radiant all currently coexist without one umbrella. (owner: @andrew-soane)
- Treat the Prime Radiant as a 10-50x productivity substrate rather than a 10-20% productivity tool; the whole-company digital twin is what the architecture is pointed at. (owner: @michael-bruck; horizon: year)

## Findings

- Google Shared Drive is incompatible with the Claude Code + Obsidian vault model — when pointed at a Shared Drive the integration 'just broke'; Drive works for opening individual Word/JPEG/video files but not for database-style directory access. (stated by @euclid-wong)
- LLMs generate good-looking HTML far more cheaply (in tokens) than they generate PowerPoint — HTML is the right output format for AI-generated decks. (stated by @michael-bruck)
- Fireflies cannot reliably auto-identify speakers in in-person meetings (no voice prints; legal restrictions on capturing them); accurate speaker tags require manual tagging by the recording owner after the call. (stated by @michael-bruck)
- Otter.ai handles speaker recognition well but is unusable in every other way; Granola does not do it either — there is no single 'good at everything' transcription tool today. (stated by @euclid-wong; confidence: medium)
- The Prime Radiant + Claude.md + inbox pattern processed 122 inbox files end-to-end in a single live ingest, with the system auto-classifying as 58 duplicates / 64 new + flagging 120 high-stakes escalations correctly per its own Section-5.1 ingest rules. (stated by @euclid-wong)
- Letting humans hand-place files into the vault outside the inbox produces broken links and orphan pages — the inbox-as-single-entry-point discipline is load-bearing for system integrity. (stated by @euclid-wong)
- Speaker-tagged transcripts are far higher-signal than untagged ones for the Prime Radiant because the entity-edge layer (who-said-what) is most of the synthesis value — untagged transcripts lose the cross-references the brain depends on. (stated by @michael-bruck)
- Karpathy's LLM-Wiki idea (LLMs are very good at the housekeeping/organising of personal knowledge, not at collecting it) is the design inspiration for Prime Radiant; the original Karpathy framing is preserved in the AIO concepts/ folder. (stated by @michael-bruck)
- Fireflies records Chinese natively with selectable input language — making it viable to run the IT/Ops scoping meeting in Chinese without an English-translation step gate. (stated by @rosa)
- Six weeks of AIO Prime Radiant usage produced organic emergence of higher-order categories Michael did not seed (concepts/, briefs/, the LLM-Wiki concept itself, the AI-native-positioning brief) — the LLM proposes the taxonomy once it has enough content. (stated by @euclid-wong)

## Open questions

- How should the Prime Radiant store and index image-heavy / screenshot-heavy documents (Rosa's product DOCs, internal procedure decks with many screenshots) given that the brain is markdown-first? (raised by @rosa)
- Should IT/Ops's Prime Radiant be one combined instance covering both 'product' and 'project management', or two separate facets? (raised by @euclid-wong)
- How does the company arrive at one umbrella name covering Prime Radiant, Nomi, Mios and the other AI-systems sub-brands? (raised by @michael-bruck)
- Can voice-print speaker identification be self-built on top of Fireflies' raw audio (since Fireflies cannot do it for legal reasons), and is the effort worth it vs the 1-minute manual tagging habit? (raised by @michael-bruck)

## Blockers

- Michael cannot use the Janusd-io GitHub org (and therefore cannot pull/push the shared vault) until he accepts the pending org invitation — the .io invite appears to have timed out and may need re-sending. (blocks: [[michael-bruck]]; owner: @michael-bruck)
- Rosa's product / project-management materials are screenshot-heavy DOC files, which the current markdown-only ingest pipeline cannot fully absorb until the image-storage strategy is settled. (blocks: [[it-ops-prime-radiant]]; owner: @euclid-wong)

## Tool mentions

- [[github]] — newly chosen sync substrate for Prime Radiant vaults, replacing Google Shared Drive
- [[google-drive]] — incompatible with Claude Code + Obsidian; being retired as the Prime Radiant substrate
- [[obsidian]] — the Prime Radiant's UI / database manager on top of markdown files
- [[obsidian-git]] — third-party Obsidian plugin used to auto-commit and pull every five minutes against GitHub
- [[claude-code]] — the agentic engine reading Claude.md and running the ingest pipeline on the vault
- [[claude-cowork]] — shared-directory mode of Claude that operates on the same folder as Obsidian
- [[fireflies]] — primary meeting-capture source for the Prime Radiant; MCP-connected so Claude can pull transcripts directly
- [[notion]] — likely deprecation candidate — Prime Radiant replaces its synthesis role and MCP integration is slow
- [[linear]] — system of record for the AI Tools Registry and AI Projects; referenced by Claude.md as an ingest source
- [[monday-com]] — execution surface for AI Office projects and standup task tracking
- [[obsidian-web-clipper]] — primary intake mechanism for articles into the Prime Radiant inbox
- [[otter-ai]] — compared as the one transcription tool with good speaker recognition but otherwise poor
- [[granola]] — compared and ruled out for speaker identification
- [[openai-codex]] — alternative agentic stack the team chose against because cross-LLM portability is hard once a vault is committed to one model family
- [[visual-studio-code]] — IDE editor pointed at the same vault directory as Obsidian + Claude for editing markdown

## Topics

- janus-prime-radiant
- it-ops-onboarding
- github-substrate
- speaker-tagging
- claude-code
- obsidian
- privacy-classification
- notion-deprecation

## Related

- Project: [[janus-prime-radiant-build]] — the meeting is a working session of this programme — onboarding the IT/Ops department into the Prime Radiant pattern
- Project: [[it-ops-prime-radiant]] — the new departmental instance being scoped in this meeting
- Project: [[marketing-prime-radiant]] — cited throughout as the prior playbook (Andrew's instance) the IT/Ops rollout is copying
- Concept: [[llm-wiki]] — the design inspiration (Karpathy) cited by Michael as the genesis of the Prime Radiant
- Concept: [[prime-radiant]] — named brand of the system; discussed at length including the Asimov Foundation reference
- Concept: [[digital-twin]] — Michael frames the company-wide vision as a digital twin built from per-department brains as sensors
- Vendor: [[github]] — newly chosen substrate; Michael's pending org invite was the bottleneck discussed
- Vendor: [[google-drive]] — being retired from the Prime Radiant substrate role
- Vendor: [[notion]] — flagged as likely deprecation
- Vendor: [[fireflies]] — raw transcript source; speaker-tagging discipline discussed at length
- Vendor: [[obsidian]] — the vault UI on top of markdown
- Person: [[andrew-soane]] — his marketing Prime Radiant is the template for the IT/Ops rollout; will own future brand naming
- Person: [[bonaventure-wong]] — Michael references using the Prime Radiant to prep for weekly Bonaventure meetings and Bonaventure's three-pillar messaging brief surfaced by the system
- Person: [[andrey-timokhov]] — Michael recalls the prior Fireflies Lisbon-office conversation he and Andrey had about speaker identification
- Person: [[andrej-karpathy]] — named source of the LLM-Wiki idea
- Person: [[lysander]] — Rosa's IT/Ops project-management colleague; co-presenter at tomorrow's Chinese scoping meeting (not on roster — may need stub)
- Decision: [[2026-05-13-andrew-soane-first-cross-dept-prime-radiant-rollout]] — prior decision this meeting builds on — IT/Ops is the third departmental rollout after Andrew's
- Concept: [[kebab-case]] — naming convention discussed at length as a load-bearing piece of the schema
- Concept: [[inbox-as-single-entry-point]] — ingest discipline explained as the rule that prevents broken links
- Concept: [[claude-md-rulebook]] — per-vault rulebook discussed as the per-department customisation surface

---

## Transcript

Raw transcript stays in Fireflies — fetch via MCP when needed.
Fireflies: [original meeting](https://app.fireflies.ai/view/01KRGKF94R785XZNVKGKTB840J)
