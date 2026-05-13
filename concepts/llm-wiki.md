---
type: concept
title: LLM Wiki
slug: llm-wiki
created: 2026-05-06
updated: 2026-05-07
departments: [ai-office]
confidence: high
sources: [karpathy-llm-wiki, greg-isenberg-obsidian-claude-code-os, elvis-saravia-personal-research-kb, arscontexta-claude-code-plugin, obsidian-knowledge-vault-auto-synthesis]
related: [andrej-karpathy, janus-prime-radiant-build, obsidian, agent-skills]
---

# LLM Wiki

A pattern for building personal or organisational knowledge bases where an LLM maintains the wiki and humans direct it. Coined and articulated by [[andrej-karpathy]] in his 2026 gist.

## Core idea

Inverts the usual RAG pattern. Rather than re-retrieving raw sources on every query, the system maintains a **persistent, compounding wiki of LLM-written markdown** that gets updated as new sources arrive. Cross-references, contradictions, and synthesis are baked into the structure, not rediscovered each time.

Spiritually descended from Vannevar Bush's 1945 Memex vision — the maintenance burden that historically killed personal wikis is solved by handing it to the LLM.

## Architecture (three layers)

1. **Raw sources** — immutable inputs: articles, papers, transcripts, exports. The LLM reads, never modifies.
2. **The wiki** — directory of LLM-written markdown. Entity pages, concept pages, decisions, briefs. The LLM owns this and keeps it consistent.
3. **The schema** — a `CLAUDE.md`-style configuration document that tells the LLM the wiki's structure, naming conventions, and workflows. It is what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. Co-evolved with the human over time.

## Operations (three workflows)

- **Ingest** — drop a source in, LLM files it into `sources/`, updates affected entity/concept/project pages, logs the event.
- **Query** — ask questions against the wiki. Answers can be filed back as new pages, so explorations compound.
- **Lint** — periodic health check for contradictions, stale claims, orphan pages, missing references. Runs on a cadence or on demand.

## Why it works (per the gist)

- LLMs don't forget to update cross-references and can touch many pages in one pass — the maintenance burden goes near zero.
- The schema document keeps the LLM focused; without it the LLM produces generic output.
- Query results can become sources, so the wiki compounds twice: from external sources *and* from your own thinking.
- At ~100 sources / hundreds of pages, simple index + drill-down beats embeddings/vector search.

## Implementation in this wiki

See [[janus-prime-radiant-build]] for the project hub. Schema lives in `CLAUDE.md` at the wiki root. Source files live in `sources/`, intake queue in `inbox/`. The Janus implementation extends Karpathy's pattern with department and country tagging in frontmatter, and a low-stakes/high-stakes split in the ingest flow (LLM auto-writes routine updates; flags new entities and merges as `questions/` pages for review).

## Why "Janus Prime Radiant"

The Janus instance of this pattern is named **Janus Prime Radiant**, after Hari Seldon's living psychohistory instrument in Asimov's Foundation series. The metaphor was chosen deliberately over alternatives (e.g., Asimov's Multivac / AC lineage) because the *mechanic* of the Prime Radiant fits this pattern exactly:

- **Living and updating.** The Prime Radiant holds the equations of psychohistory and is updated as Speakers contribute refinements. The wiki is the same shape — each ingest adds pages, each lint adds cross-links, each decision/lesson refines the body of equations.
- **Authoritative, not omniscient.** It doesn't *know* the future; it represents the *current best understanding* of it. That matches the wiki's epistemic posture: confidence levels, dated claims, lessons revised when wrong.
- **Contributed-to by trained practitioners.** The Speakers each add to the Prime Radiant; here, humans curate sources and the LLM synthesises pages. It's a contributed-to instrument, not a black-box oracle.
- **Long-arc planning.** Foundation's project is a 1,000-year recovery from civilisational dark age. Janus's analog is durable institutional memory across vendor cycles, personnel changes, and platform migrations. Same shape: the Prime Radiant is the artifact that makes the long-arc thinkable.

By contrast, Asimov's Multivac / Galactic AC / Cosmic AC lineage are *computational* metaphors — black-box mainframes you query for answers. That's an oracle / search-engine model, which the wiki isn't. The wiki is closer to a guarded, contributed-to instrument than a giant computer in a basement.

The naming pattern: one Prime Radiant, many domain facets — *Janus Prime Radiant · AI Office* (this instance), *· Marketing*, *· HR*, etc., as the pattern extends to other departments.

## Related approaches surfaced post-Karpathy

- **"How to Build an Obsidian Knowledge Vault That Gets Smarter Every Day Without You Doing Anything"** ([[obsidian-knowledge-vault-auto-synthesis]]). Same pattern from individual knowledge-worker angle: ingest articles + tweets + voice notes, extract durable entities/concepts, auto-generate cross-links. Reinforces that the wiki pattern is portable across personal and organizational scales.
- **Greg Isenberg's "Obsidian + Claude Code as a 24/7 personal OS"** ([[greg-isenberg-obsidian-claude-code-os]]). Same primitives (Obsidian + LLM + markdown), framed for solo-founder workflows.
- **Elvis Saravia's tuned skill for research-paper curation** ([[elvis-saravia-personal-research-kb]]). Uses Tobi's `qmd` CLI for indexing; explicitly cites Karpathy. Notable for showing the pattern works at scale for research papers specifically.
- **arscontexta** ([[arscontexta-claude-code-plugin]]) — open-source Claude Code plugin that generates individualised knowledge systems from conversation. Not yet evaluated; potentially a tool to seed an LLM Wiki for someone starting from zero. Worth tracking.

These confirm the [[llm-wiki]] pattern is becoming a small-but-active practice rather than just Karpathy's idiosyncrasy.
