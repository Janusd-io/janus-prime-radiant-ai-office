---
type: source
source_type: meeting
title: Data Management System Overhaul Meeting
slug: 2026-05-14-data-management-system-overhaul-meeting
created: 2026-05-14
captured_by: jehad-altoutou
attendees: [unknown-speaker-1, michael-bruck, jehad-altoutou, unknown-speaker-4]
duration_min: 63
fireflies_id: 01KRJHC7PHQWWJH66T3DBB13K4
audience: department
departments: [ai-office]
dept_scope: [ai-office]
sensitivity: dept
task_tracker: monday
parsed_at: 2026-05-15T09:25:59Z
parser_version: 3
summary: Jehad and Michael worked through the next phase of the Janus Prime Radiant / Obsidian rollout
topics: [janus-prime-radiant, obsidian-git, vault-architecture, federation, meeting-ingest, lint-queue, github-org-setup, department-rollout]
decisions: [2026-05-14-collapse-personal-vault-into-department-vault, 2026-05-14-adopt-obsidian-git-plugin-drop-github-desktop-and-cli, 2026-05-14-substrate-is-github-not-google-shared-drive, 2026-05-14-one-repo-per-department-not-subfolders, 2026-05-14-andrew-marketing-instance-is-next-rollout-target, 2026-05-14-defer-personal-vault-question-until-bonaventure-returns, 2026-05-14-drop-notion-as-standup-target]
action_items_count: 6
confidence_overall: medium
---

# Data Management System Overhaul Meeting

**Date:** 2026-05-14
**Attendees:** [[unknown-speaker-1]], [[michael-bruck]], [[jehad-altoutou]], [[unknown-speaker-4]]
**Duration:** 63 min
**Fireflies:** [original meeting](https://app.fireflies.ai/view/01KRJHC7PHQWWJH66T3DBB13K4)

---

## Summary

Jehad and Michael worked through the next phase of the Janus Prime Radiant / Obsidian rollout. Key reframe: drop the personal-vs-department two-tier model and run a single department-level vault per dept (marketing, AI office, PM, IT) — the personal tier added confusion without adding content, and federation between personal and dept was not working. They diagnosed why yesterday's AIO meetings (PM team, IT, Andrew onboarding) had landed in Jehad's personal vault instead of the AIO vault and why the meeting parser differed in quality between the standup skill (good) and the janus-brain enrolment dump (raw). They confirmed the Obsidian Git community plugin replaces the need for the GitHub Desktop app and CLI for sync, but Jehad still has to run pushes manually because of stored-credentials errors; a daily cron job covers the rest. They agreed to land Andrew's marketing instance next as the smallest test case, defer further personal-vault work until Bonaventure is back, and add a curator/dashboard surface later to expose pending questions and lint findings.

## Decisions

- [[2026-05-14-collapse-personal-vault-into-department-vault]] — Collapse personal vault into department vault
- [[2026-05-14-adopt-obsidian-git-plugin-drop-github-desktop-and-cli]] — Adopt Obsidian Git community plugin as the sync mechanism; drop GitHub Desktop app and CLI
- [[2026-05-14-substrate-is-github-not-google-shared-drive]] — Substrate is GitHub, not Google Shared Drive
- [[2026-05-14-one-repo-per-department-not-subfolders]] — One GitHub repo per department, not subfolders inside one repo
- [[2026-05-14-andrew-marketing-instance-is-next-rollout-target]] — Andrew's marketing instance is the next rollout target
- [[2026-05-14-defer-personal-vault-question-until-bonaventure-returns]] — Defer personal-vault question until Bonaventure returns
- [[2026-05-14-drop-notion-as-standup-target]] — Drop Notion as a standup target; transcripts go straight into Obsidian

## Action items

- [ ] @jehad-altoutou Reconcile the janus-brain enrolment parser with the standup skill's meeting-parser logic so enrolment-imported transcripts get the same structured shape as standup-imported ones (rather than dumping raw transcript). — Monday
- [ ] @jehad-altoutou Re-run janus-brain enrolment to land Andrew Soane's marketing Prime Radiant vault on GitHub end-to-end (repo, group, permissions, Obsidian Git plugin). (raised by @michael-bruck) — Monday
- [ ] @michael-bruck Review the bash automation script Jehad shared in Slack for end-to-end department-repo provisioning and clean up anything Claude missed. (due: 2026-05-14; raised by @jehad-altoutou) — Monday
- [ ] @jehad-altoutou Install and configure the Obsidian Git community plugin on the personal-vault Obsidian instance so it stops sitting at the local-only state and matches the AIO vault's auto-commit interval (5 min). (raised by @michael-bruck) — Monday
- [ ] @michael-bruck Work through the backlog of escalated ingest questions in questions/ (Vivian Balakrishnan, FactSet, OpenAI vendor page, Niman, Pinecone) and either approve or defer each. — Monday
- [ ] @unknown-speaker-4 Generate an HTML-rendered presentation for the afternoon meeting with Rosalind and Lysandra describing the onboarding process (step 1 / step 2 / step 3, what's needed, what's provided), driven from the Prime Radiant knowledge base. (due: 2026-05-14) — Monday

## 🎯 This week

- @jehad-altoutou Stabilise the Obsidian Git sync flow end-to-end (resolve the stored-credentials / 'another Git process' errors and the manual-push fallback) so Andrew's vault and onward rollouts don't inherit them.
- @team Focus the week on getting the department-level vaults reliable; do not deploy the PM-team instance until Andrew's marketing instance is fully working. (raised by @jehad-altoutou)
- @michael-bruck Use the daily standup slot to triage outstanding questions/ escalations as they accumulate, instead of letting them age.

## 🏔️ Long horizon

- Build a 'wiki of wikis' surface that reads across every department's GitHub-backed Prime Radiant repo and gives Bonaventure (and other leadership) a roll-up view. (owner: @michael-bruck; horizon: quarter)
- Add a curation / dashboard layer on top of the vaults so end users see what needs their attention (open questions, lint findings) without driving everything through a Claude chat — solving the 'blank prompt' problem. (owner: @michael-bruck; horizon: weeks)
- Treat the Prime Radiant as a third team member / chief-of-staff that recommends, organises, and surfaces patterns — not just a passive document store. (owner: @michael-bruck)
- Eventually recreate cross-departmental 'cross-pollinisation' (Bell Labs / Pixar pattern) by letting one department's wiki surface ideas into another department's instance. (owner: @michael-bruck; horizon: year)
- Once a department vault is stable, run a second-phase conversation with each department head asking what outputs they want (dashboard pages, attention surfaces, dynamic views) rather than expecting them to navigate raw Obsidian. (owner: @michael-bruck; horizon: weeks)

## Findings

- The janus-brain enrolment skill currently dumps raw Fireflies transcripts into the vault, whereas the standup skill produces a structured, parsed meeting page; the two should converge on the standup skill's parsing shape. (stated by @jehad-altoutou)
- Yesterday's AIO meetings (PM team, IT, Andrew onboarding) landed in Jehad's personal vault rather than the AIO vault — likely because the active Claude Code project was pointed at the personal vault directory, illustrating that one Claude project per vault is the right discipline. (stated by @michael-bruck)
- The wiki's questions/ escalation queue is accumulating multi-day-old items (Vivian Balakrishnan, FactSet, OpenAI, Niman) that need explicit human disposition — the system is intentionally not autonomous on entity creation. (stated by @michael-bruck)
- The wiki uses prior decisions as precedent — e.g. it recommended 'defer, match the Q2 OpenAI deferral precedent' for a new vendor escalation, demonstrating compounding institutional memory in action. (stated by @michael-bruck)
- Obsidian struggles with discoverability — Jehad had to hunt to find where transcripts live (sources/meetings/); this confirms the need for a navigation/dashboard layer over the raw vault. (stated by @jehad-altoutou)
- The Obsidian Git community plugin (by Vinzent03) is sufficient for end-to-end sync; the GitHub Desktop app and a separate CLI workflow are both unnecessary. (stated by @michael-bruck)
- Two Obsidian vault instances cannot run their Obsidian-Git plugins simultaneously on the same machine — the plugin reports 'another Git process is running' when both are active. (stated by @michael-bruck; confidence: medium)
- GitHub repo permissioning needs a group-plus-admin layering: department members get a group with write/commit/pull only, while Jehad and Michael hold individual admin roles per repo. (stated by @jehad-altoutou)
- Personal-vault Obsidian had auto-commit interval set to 0 and so was never actually pushing — the AIO vault was at 5 minutes; this gap explained why some 'syncing' messages were misleading. (stated by @michael-bruck)

## Open questions

- How do we keep multiple users' Obsidian-Git instances in sync on the same machine when only one Git process can run at a time per plugin? (raised by @michael-bruck)
- Should the substrate be janusd.io or janusd.com for the department repos — and which subset of people goes where given the IO vs com organisational split? (raised by @jehad-altoutou)
- What does federation actually look like between department vaults once the personal tier is dropped — bidirectional, one-way, or via a leadership-only 'wiki of wikis' reader? (raised by @michael-bruck)
- Should the wiki be authorised to autonomously create entity / vendor pages once confidence is high enough, instead of always escalating to questions/? (raised by @michael-bruck)
- Do we need a real navigation UI / dashboard layer over the vault for non-technical users, or can plain Obsidian + chat be made to surface 'what needs your attention' adequately? (raised by @michael-bruck)

## Blockers

- Obsidian-Git plugin cannot read the GitHub personal access token from the macOS Keychain (sandbox-limited), forcing Jehad to push manually until a long-term credential-storage fix is in place. (blocks: [[janus-prime-radiant]]; owner: @jehad-altoutou)
- Two Obsidian vaults running the Git plugin simultaneously produce 'another Git process' errors, blocking real-time multi-vault sync on a single laptop. (blocks: [[obsidian-git]]; owner: @jehad-altoutou)
- Bonaventure is on holiday, blocking final resolution of the personal-vs-department vault question. (blocks: [[2026-05-14-collapse-personal-vault-into-department-vault]]; owner: @bonaventure-wong)

## Tool mentions

- [[obsidian]] — primary vault UI for every Prime Radiant instance
- [[obsidian-git]] — Vinzent03's community plugin chosen as the sync mechanism replacing GitHub Desktop / CLI
- [[github]] — substrate for all department Prime Radiant repos, replacing Google Shared Drive
- [[google-shared-drive]] — previous substrate being abandoned
- [[notion]] — being dropped as a standup target because of recurring API issues
- [[fireflies]] — transcript source feeding the meeting-parser; the enrolment skill currently dumps Fireflies output raw
- [[claude-code]] — engine running the enrolment + standup skills; needs the right per-project default directory to write to the correct vault
- [[cowork]] — Cowork project workspace Jehad set up; first attempt to wire it failed and is to be redone
- [[monday]] — noted as already being summarised inside the wiki ('it even did Monday') — staying as the execution surface
- [[linear]] — system of record the wiki ingest can also pull from via connector

## Topics

- janus-prime-radiant
- obsidian-git
- vault-architecture
- federation
- meeting-ingest
- lint-queue
- github-org-setup
- department-rollout

## Related

- Project: [[janus-prime-radiant]] — the entire programme being stood up — primary subject of the meeting
- Project: [[janus-brain-bootstrap]] — the enrolment skill whose parser needs to converge with the standup skill
- Project: [[standup-skill]] — reference implementation for meeting parsing; called out as 'way better understanding of structure'
- Vendor: [[obsidian-git]] — chosen sync mechanism — discussed materially
- Vendor: [[github]] — substrate decision
- Vendor: [[notion]] — explicitly dropped as a standup target
- Vendor: [[fireflies]] — transcript source feeding ingest
- Vendor: [[openai]] — queued questions/ escalation to create a vendor page
- Vendor: [[factset]] — queued questions/ escalation to create a vendor page
- Vendor: [[pinecone]] — mentioned as backlog item alongside the new vendor under consideration
- Person: [[bonaventure-wong]] — on holiday; awaited for personal-vault decision and as 'wiki of wikis' consumer
- Person: [[andrew-soane]] — next rollout target — marketing instance
- Person: [[vivian-balakrishnan]] — queued questions/ escalation for an entity page (Singapore politician)
- Person: [[rosalind]] — afternoon meeting attendee for whom Speaker 4 wants an onboarding presentation
- Person: [[lysandra]] — afternoon meeting attendee for whom Speaker 4 wants an onboarding presentation
- Concept: [[cross-pollinisation]] — long-horizon framing — Bell Labs / Pixar / Steve Jobs anecdote for why cross-vault federation eventually matters
- Concept: [[curator-pattern]] — Michael invokes the curator role and 'nanny' framing for ongoing wiki upkeep
- Concept: [[ingest-vs-sync-vocabulary]] — Michael argues 'ingest' is the right term, not 'sync', for inbox processing
- Decision: [[2026-05-13-rewrite-spec-single-vault]] — today's single-vault decision operationalises the 2026-05-13 REWRITE-SPEC direction

---

## Transcript

Raw transcript stays in Fireflies — fetch via MCP when needed.
Fireflies: [original meeting](https://app.fireflies.ai/view/01KRJHC7PHQWWJH66T3DBB13K4)
