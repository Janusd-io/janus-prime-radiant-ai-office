---
type: lesson
title: Notion degrades as an AI-searchable knowledge base at scale
slug: 2026-05-05-notion-degrades-as-ai-searchable-kb
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: michael-bruck
confidence: high
sources: [pr-backup-2026-05-11-1432-lesson-notion-degrades-as-ai-searchable-kb]
related: [notion, llm-wiki, janus-prime-radiant-build, retrieval-augmented-generation]
audience: [department]
captured_by: jehad-altoutou
---

# Notion degrades as an AI-searchable KB at scale

**Surfaced:** 2026-05-05. **Reinforced:** 2026-05-06.

## What we observed

Notion is excellent as a *journal* — the chronological surface for daily standups, decisions, and forward-looking notes. But once Notion volume grows, it degrades as a knowledge base for AI agents to search:

- Notion's search returns coarse, page-level results without reliable structural cues.
- Per the 2026-05-06 standup, Notion + MCP retrieval is too slow and too expensive at scale.
- Per the 2026-05-05 standup, Notion is good as a journal but degrades as an AI-searchable KB once volume grows.
- Symptom: agents fabricate context rather than consulting the source.

## Why it matters

This is the originating motivation for the [[janus-prime-radiant-build]] project. The 2026-05-05 standup explicitly chose Markdown + front-matter + progressive exposure over RAG-on-Notion as the company's KB direction. The lesson sits at a peculiar inflection: [[notion]] stays valuable for what it's good at (journal, chronological reporting, human-readable navigation) but loses to a Markdown-based wiki for what it's not (an indexable, agent-callable knowledge surface).

## Implications

- Notion is retained as the AIO Operations Notebook and remains authoritative for the daily journal.
- Knowledge that needs to be consulted by agents gets pulled into the [[llm-wiki|LLM Wiki]] in Markdown form rather than relying on Notion search to surface it.
- Consistent with the broader industry shift: pre-shaped knowledge artefacts beat runtime retrieval over raw chunks.

## Open questions

- How much of the Operations Notebook ultimately wants to live in Markdown vs. stay in Notion? Initial answer: standup logs stay in Notion (journal); decisions, lessons, vendor pages, concepts migrate to the wiki.
- Does Notion eventually fix this, or is the gap structural? Watch for Notion AI improvements vs. continuing to build the wiki regardless.
