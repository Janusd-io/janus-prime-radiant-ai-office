---
type: concept
title: LLM Wiki
slug: llm-wiki
created: 2026-05-06
updated: 2026-06-08
departments: [ai-office]
confidence: high
sources: [karpathy-llm-wiki, greg-isenberg-obsidian-claude-code-os, elvis-saravia-personal-research-kb, arscontexta-claude-code-plugin, obsidian-knowledge-vault-auto-synthesis, prime-radiant-continual-learning-memory]
related: [andrej-karpathy, janus-prime-radiant-build, obsidian, agent-skills, prime-radiant, compounding-learning, agent-memory]
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

## The stateless AI trap — why the wiki is not optional

Every AI conversation starts cold. The model has no memory of what was discussed last week, last month, or last year. It doesn't know which vendors were rejected and why, which strategic bets are in flight, which decisions were made under which constraints. This is not a quirk of any platform — it is the default state of all current commercial AI.

The consequence is that intelligence produced in a session evaporates when it ends. The next session recomputes it from scratch. For one-off queries, tolerable. For strategic knowledge work — where almost all value comes from accumulation — fatal.

The instinct is to say "we already have Notion, Slack, Fireflies." But these systems are not connected, not synthesised, and not queryable across the whole. An AI that can search each independently cannot answer "why did we make the decision we made in April?" — the answer requires pulling the meeting transcript, the Notion log, the Linear evaluation, and the Slack thread where it was contested. No single system holds the synthesis. The wiki holds it, by design. See [[prime-radiant]] for the full argument.

## Why in-context learning beats fine-tuning for institutional knowledge

The alternative to the wiki approach — encoding institutional knowledge in model weights via fine-tuning — has superficial appeal but fails on the dimensions that matter most for organisational knowledge:

- **Updatability.** In-context knowledge changes by editing a file. In-weights knowledge requires a new training run. For knowledge that evolves weekly, this is not a marginal difference — it is the difference between a living record and a slowly degrading snapshot.
- **Inspectability.** Context is readable by anyone — human or AI. Weights are opaque. You cannot audit what a fine-tuned model "knows" or identify where it is wrong. A structured wiki page can be read, corrected, and version-controlled.
- **Vendor independence.** In-context knowledge travels across model generations and providers unchanged. Fine-tuned weights are locked to the model they were trained on.

The research grounding: Brown et al.'s 2020 GPT-3 work established that in-context learning is competitive with fine-tuning for knowledge retrieval tasks, and subsequent research has consistently found that well-structured, curated context outperforms large-volume raw injection. Quality and organisation of context matter more than volume — which is precisely what the wiki's curation discipline provides.

The wiki solves the remaining challenge of in-context learning — scale — by injecting only the relevant subset on each query. The multi-graph frontmatter (department, temporal, causal, semantic edges) makes targeted retrieval possible regardless of how large the vault grows. See [[prime-radiant]] for the multi-graph architecture and [[agent-memory]] for the broader memory-system research context.

## Related approaches surfaced post-Karpathy

- **"How to Build an Obsidian Knowledge Vault That Gets Smarter Every Day Without You Doing Anything"** ([[obsidian-knowledge-vault-auto-synthesis]]). Same pattern from individual knowledge-worker angle: ingest articles + tweets + voice notes, extract durable entities/concepts, auto-generate cross-links. Reinforces that the wiki pattern is portable across personal and organizational scales.
- **Greg Isenberg's "Obsidian + Claude Code as a 24/7 personal OS"** ([[greg-isenberg-obsidian-claude-code-os]]). Same primitives (Obsidian + LLM + markdown), framed for solo-founder workflows.
- **Elvis Saravia's tuned skill for research-paper curation** ([[elvis-saravia-personal-research-kb]]). Uses Tobi's `qmd` CLI for indexing; explicitly cites Karpathy. Notable for showing the pattern works at scale for research papers specifically.
- **arscontexta** ([[arscontexta-claude-code-plugin]]) — open-source Claude Code plugin that generates individualised knowledge systems from conversation. Not yet evaluated; potentially a tool to seed an LLM Wiki for someone starting from zero. Worth tracking.

These confirm the [[llm-wiki]] pattern is becoming a small-but-active practice rather than just Karpathy's idiosyncrasy.
