---
type: person
title: Jehad Altoutou
slug: jehad-altoutou
created: 2026-05-06
updated: 2026-05-13
sources: [jehad-vault-jehad-altoutou]
departments: [ai-office]
related: [michael-bruck, janus-prime-radiant-build, fireflies, monday, peer-to-peer-mesh-federation-pattern, aio-skills-sor-architecture-jehad, aio-playbooks-jehad, iso-compliance-programme]
migrated_from: entities/internal/jehad-altoutou.md
---
# Jehad Altoutou

Janus AI Office. Author and owner of the `/standup` skill (currently v3.13, v3.14 pending). Frequent collaborator on every AIO standup recorded in this wiki — co-attendee on the 1, 4, 5, 6, 11 May 2026 standups.

Primary engineering owner of:
- the `/standup` skill (v3.x evolution, ISO alignment in progress; v3.14 dual-write-to-wiki-inbox spec pending per [[ingest-2026-05-11-standup-skill-dual-write-to-aio-inbox]])
- recruitment-pipeline implementation work on the [[monday]] HR Dashboard board
- the Fireflies webhook architecture for interview transcripts (see [[2026-05-04-centralised-fireflies-webhook-for-interviews]])
- the **`/ims-enrolment`** skill — Claude Desktop skill that walks any Janus department through ISO 9001 Figure 1 documentation; produces parent process docs, sub-process docs per activity, First Voice questionnaire, and Word-doc handover bundle for [[simon-tarskih|Simon]]. v1.1, 20 files / ~3500 lines; distributable via the `Jehada-Janusd/janus-puls-onboarding` GitHub repo. (This is the same artefact previously referred to in this wiki as "ISO facilitation skill"; renamed to its actual name.)
- the [[2026-05-05-recruitment-scoring-as-claude-skill|recruitment scoring Claude skill]]
- the [[2026-05-06-andrew-as-standup-skill-rollout-pilot|standup-skill rollout to Andrew]]
- the **PULS programme** branding and 11-doc onboarding repo (Predictive Unified Live System); proposed Process Owner for ISO 9001 sections C1 (AI System Design & Development), C2 (Software Development & Release), S2 (IT Infrastructure & Data Governance) — awaiting [[michael-bruck|Michael]]'s sign-off. See [[iso-compliance-programme]].

## Architecture contributions

- **[[peer-to-peer-mesh-federation-pattern|Peer-to-peer mesh federation pattern]]** (emerged from the 11 May 2026 AIO standup discussion) — the federation design for cross-vault Prime Radiant sharing: each department-to-department relationship gets its own shared `entities/departments/<other>/` subfolder visible to both vaults. Filesystem-level federation, not event-broker. Now the canonical federation pattern for the [[janus-prime-radiant-build|Prime Radiant rollout]].
- **[[aio-skills-sor-architecture-jehad|AIO skills + systems-of-record architecture]]** — the synthesis-level reference (authored by Jehad in his personal vault, federated into this wiki) for how `/standup`, `/ai-registry`, `/ai-tool-evaluation`, `/assessify-hr` interconnect, including subagent-dispatch JSON contracts and read-vs-write matrix per system.
- **[[aio-playbooks-jehad|AIO operational playbooks]]** — step-by-step recipes for the work that runs through the AI Office (authored by Jehad in his personal vault, federated in).

Working partner with [[michael-bruck]] on AIO architecture decisions; sub-skill orchestration design and dispatch-gate semantics are largely his work.
