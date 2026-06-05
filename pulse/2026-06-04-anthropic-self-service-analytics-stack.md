---
type: pulse
title: "Anthropic's self-service analytics stack — production proof that structure beats retrieval"
slug: 2026-06-04-anthropic-self-service-analytics-stack
created: 2026-06-04
updated: 2026-06-04
departments: [ai-office, engineering]
confidence: high
sources: [anthropic-self-service-data-analytics]
related: [knowledge-compilation, post-rag-agent-data-stack, agent-skills, curator-pattern, recursive-self-improving-loop, retrieval-augmented-generation, 2026-06-02-rag-obituary-bustamante-post-retrieval-age, claude-md-rulebook]
---

# Anthropic's self-service analytics stack — production proof that structure beats retrieval

Anthropic's data team published *How Anthropic enables self-service data analytics with Claude* (claude.com blog; Chang, Peng, Leder, Jiao, Cherry; [[anthropic-self-service-data-analytics]]). At Anthropic, **95% of business-analytics queries are automated via Claude at ~95% aggregate accuracy** — but only because of a specific architecture, not by pointing an agent at a warehouse. The piece is the cleanest in-production validation yet of the compilation-stage-knowledge thesis behind [[janus-prime-radiant-build|Janus Prime Radiant]], and it doubles as an adoptable playbook.

## The core argument

Analytics accuracy is *"a context and verification problem, not a code generation issue."* Three failure modes account for most errors:

1. **Concept↔entity ambiguity** — the agent can't map "revenue for product X" to the one correct table/column/metric among many plausible candidates.
2. **Data staleness** — schemas/definitions/docs rot; agent knowledge silently goes wrong.
3. **Retrieval failure** — the right info exists and is annotated, but the agent doesn't find it in a vast search space.

The four-layer stack each attacks one or more: **data foundations** (canonical, governed datasets — collapse ambiguity *before* search), **sources of truth** (semantic layer first, then lineage, then query corpus, then business context), **skills** (the agent's *procedural* knowledge — which sources to consult in what order), and **validation** (offline evals + ablation + online adversarial review).

## The load-bearing result: structure beats access

The most important finding is a **negative ablation**. They gave the agent raw grep access to *thousands* of dashboard/transform/notebook SQL files, verified in transcripts that it read them — and **accuracy moved <1 point**. The answer was present in the corpus ~80% of the time for questions it got wrong, but "answer present" didn't predict "now correct." Conclusion: *"our bottleneck wasn't access to prior work, it was structure"* — mapping a question to the right entity. That single experiment redirected months of roadmap.

Skills were the multiplier: without skills, accuracy didn't exceed **21%**; with skills, consistently **>95%**, ~99% in some domains.

## Why this matters to the AI Office

This is external, first-party, numbers-backed validation of three things the AIO already bets on — and a concrete playbook for the parts it hasn't built yet.

1. **"Structure beats retrieval" *is* the Prime Radiant bet, now with an ablation behind it.** The wiki deliberately uses curated, governed pages + `[[wikilinks]]` + grep over a vector store (see [[post-rag-agent-data-stack]], [[2026-06-02-rag-obituary-bustamante-post-retrieval-age|the RAG obituary]]). Anthropic's null result — raw grep over everything barely moved accuracy; *structure* was the bottleneck — is the strongest evidence yet that the wiki's effort should go into **canonical pages + schema discipline + cross-links**, not into bolting on retrieval. The wiki's canonical-page-per-concept rule is Anthropic's "canonical datasets, aggressively deprecate near-duplicates"; the [[curator-pattern|curator]] enforcing one governed page is the analogue of "fewer, more heavily governed logical models."

2. **Skills as *procedural* knowledge maps onto CLAUDE.md and the AIO skills.** Anthropic's split — *sources of truth* = declarative (what a metric means), *skills* = procedural (which sources, in what order, what "done" looks like) — is exactly the [[claude-md-rulebook|CLAUDE.md rulebook]] / [[agent-skills|skills]] split the AIO runs. Their warehouse-skill skeleton (a thin "knowledge" router skill + an "unbook" process skill bundling reusable analysis patterns + adversarial-review sub-agents) is a near-mirror of CLAUDE.md's §5 workflows + trust-line + lint. Worth reading the appendix skeleton directly against CLAUDE.md the next time the rulebook is revised.

3. **"Active correction harvesting" is a worked example of the closed Learning step.** Their loop: a scheduled agent scans stakeholder channels for correction language ("wrong table," "missing the fraud filter"), drafts a one-line reference-doc fix, opens a PR tagged to the domain owner; the same corrections feed the offline eval set. This is precisely the fifth, still-unautomated step of the [[recursive-self-improving-loop]] (monitor → propose edit → review/merge → smarter next time) — running in production. It's the most concrete template the AIO has seen for closing its own Learning step (lint findings → proposed CLAUDE.md edits → review/merge), and it confirms the "boring fix path" design (edit a markdown file, merge, auto-sync) the AIO already uses.

## Other adoptable specifics

- **Generate docs with Claude, but a human owns the *definition*.** Auto-generating the semantic layer from raw tables/query logs was net-negative on evals — it encoded the very ambiguities they were eliminating. Same as the AIO's curator-owns-the-schema discipline.
- **Provenance footer** on every answer (source tier › semantic layer / governed table / raw exploration · freshness · owner). The wiki's `sources:` frontmatter + inline "Per `<slug>`" citations are the institutional-KB analogue; the freshness/tier framing is worth borrowing for query answers filed back as briefs.
- **Skill maintenance is a first-class engineering problem.** Offline accuracy drifted ~95%→~65% over a month without maintenance; the fix was colocating skill markdown in the same repo as the data models so the PR that changes a model updates the doc, with a CI hook flagging un-updated skills. The wiki's git-backed substrate + lint cadence is the same discipline; the CI-hook idea is a candidate for the AIO's eventual automated lint.
- **Design for null results; keep a short list of what didn't work.** Their "what didn't work" list (LLM-authored definitions; over-refining docs past 3 net-negative iterations; cheaper adversarial reviewer losing the accuracy wins) is the same function as the wiki's `lessons/` folder.

## Watch for

- Whether Anthropic ships any of this as a reusable skill/plugin (the post says skills sync to a marketplace + MCP resources). If it does, it's a direct Stage-1 eval candidate for AIO analytics needs.
- Whether the "semantic layer first, raw SQL as fallback" discipline generalises to the wiki: i.e., should AIO query-answering be *structurally required* to consult `index.md` + frontmatter slices before grepping bodies, mirroring "consult the semantic layer before raw SQL"? Candidate refinement to CLAUDE.md §5.2.
