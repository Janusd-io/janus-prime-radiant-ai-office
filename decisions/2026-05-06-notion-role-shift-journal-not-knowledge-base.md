---
type: decision
slug: 2026-05-06-notion-role-shift-journal-not-knowledge-base
title: Notion's role shifts to journal + dept pages; AI-searchable knowledge moves to Markdown/YAML
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: michael
sources: [automations-2882088507, jehad-vault-2026-05-06-notion-role-shift-journal-not-knowledge-base]
related: [llm-wiki, janus-prime-radiant-build, notion, monday, linear, standup]
---

## Decision

As of 5 May 2026, Notion's role in the Janus knowledge infrastructure has formally shifted from centralised knowledge base to:
1. **Journal & meeting log** — AIO standups, decision capture, next-steps planning
2. **Department landing pages** — segmented sub-pages for Simon/ISO, IT, HR, Bonaventure, Andrew
3. **Onboarding surface** — org structure, team contacts, role mapping

**AI-searchable knowledge is moving to Markdown + YAML frontmatter** (the [[llm-wiki]]), with progressive exposure as structured data grows.

## Options considered

1. **Keep Notion as monolithic knowledge base** — consolidate everything in Notion, accept search degradation at scale
2. **Split: journal in Notion, knowledge in Markdown** (chosen) — Notion becomes temporal/narrative, Markdown becomes canonical/searchable
3. **Use Notion as search layer with external knowledge source** — Notion remains primary but syncs from external KB (higher complexity)

## Why this decision

- Observed fact (5 May): Notion search degraded when agent was asked about Attia internal-hub request; agent failed to consult Linear/Notion before drafting, indicating search at scale is unreliable
- Design principle: Tasks on Monday (execution), AI Registry in Linear AIR (tool reference), Notion as journal (narrative + history)
- Pattern success: standup skill v3.x Description Update blocks are proving that per-task context works in Monday Updates; Markdown with YAML frontmatter can do the same at scale for knowledge

## When this took effect

- 5 May 2026 — decision confirmed in AIO standup
- 6 May 2026 — Notion restructuring begins; department sub-pages (Simon/ISO, IT, HR) to be created this week

## Related work

- [[notion-operations-notebook-restructure]] (execution project)
- [[janus-prime-radiant-build]] (Markdown KB bootstrap; slug renamed from `llm-wiki-build` on 2026-05-08)
- [[standup|Standup skill v3.x]] (driving the Description Update pattern)

## Quoted reasoning

Michael (5 May standup): "keep Notion as a journal but offload AI-searchable knowledge to a Markdown + front-matter YAML store with progressive exposure."
