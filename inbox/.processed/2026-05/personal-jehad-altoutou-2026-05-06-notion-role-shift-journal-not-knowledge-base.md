---
type: decision
title: Notion's role shifts to journal + dept pages; AI-searchable knowledge moves to Markdown/YAML
slug: 2026-05-06-notion-role-shift-journal-not-knowledge-base
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: michael-bruck
confidence: high
sources: [pr-backup-2026-05-11-decision-notion-role-shift-journal]
related: [llm-wiki, janus-prime-radiant, notion, monday, linear, standup-skill, 2026-05-05-kb-direction-markdown-progressive-exposure-not-rag]
audience: [department]
captured_by: jehad-altoutou
---

# Notion's role shifts to journal + dept pages; AI-searchable knowledge moves to Markdown/YAML

**Decision date:** 5 May 2026 (confirmed in AIO standup). **Owner:** [[michael-bruck]]. Source: `automations-2882088507`.

## Decision

[[notion]]'s role in the Janus knowledge infrastructure has formally shifted from centralised knowledge base to:
1. **Journal & meeting log** — AIO standups, decision capture, next-steps planning.
2. **Department landing pages** — segmented sub-pages for Simon/ISO, IT, HR, Bonaventure, Andrew.
3. **Onboarding surface** — org structure, team contacts, role mapping.

**AI-searchable knowledge is moving to Markdown + YAML frontmatter** (the [[llm-wiki]]), with progressive exposure as structured data grows.

## Options considered

1. Keep Notion as monolithic knowledge base — accept search degradation at scale.
2. **Split: journal in Notion, knowledge in Markdown** (chosen) — Notion temporal/narrative, Markdown canonical/searchable.
3. Use Notion as search layer with external knowledge source — higher complexity, rejected.

## Why

- Observed fact (5 May): Notion search degraded when agent was asked about Attia internal-hub request; agent failed to consult [[linear]]/[[notion]] before drafting, indicating search at scale is unreliable.
- Design principle: Tasks on [[monday]] (execution), AI Registry in [[linear]] AIR (tool reference), Notion as journal (narrative + history).
- Pattern success: standup skill v3.x Description Update blocks are proving that per-task context works in Monday Updates; Markdown with YAML frontmatter can do the same at scale for knowledge.

## When this took effect

- 5 May 2026 — decision confirmed in AIO standup.
- 6 May 2026 — Notion restructuring begins; department sub-pages (Simon/ISO, IT, HR) created this week.

## Quoted reasoning

[[michael-bruck]] (5 May standup): *"keep Notion as a journal but offload AI-searchable knowledge to a Markdown + front-matter YAML store with progressive exposure."*
