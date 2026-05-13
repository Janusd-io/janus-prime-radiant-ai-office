---
type: decision
title: KB direction — Markdown + front-matter YAML + progressive exposure; not RAG
slug: 2026-05-05-kb-direction-markdown-progressive-exposure-not-rag
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office]
status: resolved
owner: michael
sources: [aio-2026-05-05]
related: [llm-wiki, janus-prime-radiant-build, retrieval-augmented-generation, post-rag-agent-data-stack, andrej-karpathy]
---

# KB direction — Markdown + front-matter + progressive exposure; explicitly not RAG

**Decision date:** 2026-05-05
**Decided by:** Michael Bruck, Jehad Altoutou
**Source:** [[aio-2026-05-05]]

## What

Janus's company knowledge base will be built on a substrate of plain Markdown files with YAML front-matter and progressive (incremental) exposure. Derivative caches sit on top of a single canonical library. RAG (vector retrieval over chunked sources) is explicitly **rejected** as the primary architecture.

Michael was tasked with prototyping the [[llm-wiki|Karpathy LLM Wiki]] concept as the candidate KB pattern.

## Why

- Notion's search degrades at scale; large workspaces become expensive and slow to retrieve from. See [[2026-05-05-notion-degrades-as-ai-searchable-kb]] (the lesson that drives this decision).
- OpenClaw session-restart token cost reinforces the case for derivative caches (instead of re-loading full context) and progressive exposure (instead of indiscriminate retrieval).
- The [[post-rag-agent-data-stack]] industry brief frames this same shift at the vendor level: pre-shaped knowledge artefacts beat runtime retrieval over raw chunks for agent workloads.

## Implications

- This wiki ([[janus-prime-radiant-build]]) is the prototype implementation of the chosen direction.
- The schema lives in `CLAUDE.md` and disciplines the LLM into being a maintainer rather than a search index.
- Future Janus knowledge surfaces (operational runbooks, vendor intelligence, decision archives) are candidates to migrate to the same substrate once the prototype validates.
- RAG-based tools (vector DBs, embedding indexes) can still be evaluated for narrow workloads but are not the default architecture for the company KB.

## Related

- [[janus-prime-radiant-build]] — the project executing this direction.
- [[andrej-karpathy]] — author of the LLM Wiki gist that articulated the pattern.
- [[2026-05-05-notion-degrades-as-ai-searchable-kb]] — originating lesson.
