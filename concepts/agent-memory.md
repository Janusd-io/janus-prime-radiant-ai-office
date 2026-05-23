---
type: concept
title: Agent Memory
slug: agent-memory
created: 2026-05-06
updated: 2026-05-23
departments: [ai-office]
confidence: high
sources: [agent-memory-engineering-nicbstme, your-harness-your-memory-hwchase17, mempalace-milla-jovovich, claude-managed-agents-memory, claude-managed-agents-memory-rlancemartin, himanshustwts-claude-code-memory-architecture, openai-agents-sdk-session-memory, mnemon-github-readme, jehad-vault-agent-memory, magma-multi-graph-agentic-memory, transformers-are-graph-neural-networks, 2026-05-22-marktechpost-gbrain-tutorial, 2026-05-21-mit-tech-review-code-with-claude-london]
related: [context-engineering, agentic-ai, agent-harness, retrieval-augmented-generation, 2026-05-13-magma-multi-graph-agentic-memory, 2026-05-13-transformers-are-graph-neural-networks, 2026-05-12-mnemon-llm-supervised-memory, 2026-05-22-gbrain-yc-tan-memory-layer, 2026-05-21-code-with-claude-london, gbrain]
---

# Agent Memory

The mechanisms by which AI agents persist and recall information across sessions, tasks, and users. As of 2026, this is one of the most actively contested areas of agent infrastructure — the dominant theme across the May 2026 article batch.

## Why it matters

Without memory, every agent session starts cold: re-loading context, re-deriving user preferences, re-discovering tools and constraints. With memory, agents accumulate competence over time. The interesting design questions:

- **What gets stored?** Verbatim transcripts, summaries, structured facts, relational graphs, or some combination.
- **Where does it live?** In the model's context window (volatile), in a vector store (retrieval-on-demand), as files (per [[anthropic|Anthropic]]'s [[claude|Claude]] Managed Agents approach), or in a structured graph.
- **Who owns it?** Embedded in the platform vs. portable across providers.

## Observable long-term patterns (as of 2026-05-12)

The original three patterns observed in early Q2 2026:

1. **Files-as-memory** — Anthropic's Claude Managed Agents stores memories as files; users can export, manage via API, retain control. See [[2026-04-08-claude-managed-agents-launch]] and [[claude-managed-agents-memory]].
2. **Harness-as-memory** — per Harrison Chase ([[your-harness-your-memory-hwchase17]]): agent harnesses (the orchestration layer around the model) are increasingly tied to specific memory implementations. The harness *is* the memory.
3. **Memory palace / structured indices** — MemPalace ([[mempalace-milla-jovovich]]) is an offline, palace-based system; alternative to model-heavy approaches. Niche but interesting as a portability/lock-in counterweight.

A finer-grained decomposition surfaced by the Mnemon project ([[mnemon-github-readme]], 2026-05-12) cuts the field along *LLM role* rather than *storage substrate* and is worth holding alongside the above:

| Pattern | LLM role | Representative |
|---|---|---|
| **LLM-Embedded** | Executor inside the memory pipeline | Mem0, Letta |
| **File Injection** | None — file read at session start | Claude Code Memory |
| **MCP Server** | Tool provider via [[model-context-protocol|MCP]] | claude-mem |
| **LLM-Supervised** | External supervisor of a standalone binary | Mnemon |

The two taxonomies are not redundant: the storage axis (where memory lives) and the LLM-role axis (who decides what to store) are orthogonal. Mnemon, for example, is "Files-as-memory" on the storage axis *and* "LLM-Supervised" on the role axis. Anthropic's Managed Agents are "Files-as-memory" on storage *and* effectively "LLM-Embedded" (the platform decides). The role axis is the better predictor of vendor lock-in; the storage axis is the better predictor of portability mechanics. See [[2026-05-12-mnemon-llm-supervised-memory]] for the surfacing pulse entry.

A third axis crystallised in mid-May 2026 with two independent surfacings of the same shape: **the relational-structure axis** — how memory items are *connected* to each other. The dominant pattern is monolithic semantic similarity (one big vector store, retrieve by cosine distance). The emerging pattern is **multi-graph**: four orthogonal graphs over the same memory items, one per relational dimension.

| Relational dimension | What it captures | Example query it unblocks |
|---|---|---|
| **Semantic** | Conceptual similarity / topic | "What did we say about CRM evaluation?" |
| **Temporal** | When things happened | "What changed between April and May?" |
| **Causal** | What led to what | "Why did we reject Viktor?" |
| **Entity** | Who/what was involved | "Every decision Bonaventure has touched" |

This decomposition was surfaced independently by Mnemon ([[mnemon-github-readme]], 2026-05-12 README) and MAGMA ([[magma-multi-graph-agentic-memory]], arxiv 2601, 2026-05-13) within 48 hours — same four dimensions, same architectural carve-up. MAGMA validates the approach experimentally on LoCoMo and LongMemEval, removing the single-data-point hedge that previously qualified the Mnemon entry. See [[2026-05-13-magma-multi-graph-agentic-memory]].

**Theoretical complement.** [[transformers-are-graph-neural-networks|Joshi 2026]] (arxiv 2506) argues that Transformers are mathematically GNNs operating on fully-connected token graphs — the dense-matrix implementation winning the "hardware lottery" over true sparse message-passing. Read together with the empirical multi-graph memory work: the agent-memory community is making *explicit and persistent* the same graph-structured representation the model uses implicitly during attention. Convergent or principled is an open question.

The relational-structure axis is orthogonal to the storage axis and the LLM-role axis. The Janus Prime Radiant wiki itself is a primitive multi-graph (`departments` = entity edges, `related` = semantic edges, dated decision/lesson links = causal/temporal edges) — operating the same shape MAGMA and Mnemon are validating at the agent-runtime layer, at the institutional-KB layer instead.

## Update — 2026-05-23: two more independent surfacings of the markdown-first multi-graph family

Two further surfacings within ~10 days extend the convergence pattern materially:

- **GBrain (Garry Tan / Y Combinator, surfaced 2026-05-22)** — markdown-first, PGLite + pgvector hybrid retrieval, MCP-native 74-tool surface, typed knowledge graph extracted via regex inference cascade with **zero LLM calls** (`FOUNDED → INVESTED → ADVISES → WORKS_AT → MENTIONS`). Production deployment of YC's CEO holds 146,646 pages / 24,585 people / 5,339 companies / 66 cron jobs. Each page follows a **compiled-truth-plus-timeline pattern** (current best-understanding on top, append-only evidence trail below) — strikingly close to Prime Radiant's vault-level append-only convention. See [[gbrain]] and [[2026-05-22-gbrain-yc-tan-memory-layer]].
- **Claude Code "dreaming" feature (Anthropic, announced ~2026-05-07; surfaced at the Code with Claude London event 2026-05-19)** — Claude Code agents write task-specific notes; a *dreaming* consolidation pass spots patterns across them; later agents read the dreamed-out summaries to bootstrap context. Same multi-graph pattern landing as a vendor-native feature inside Claude Code rather than as a third-party add-on. See [[claude-code]] and [[2026-05-21-code-with-claude-london]].

That brings the count to **four independent surfacings of the same architectural family within ~10 days** (Mnemon, MAGMA, GBrain, Claude Code dreaming), plus Anthropic's existing Managed Agents file-based memory. The pattern is now decisively the consensus shape of next-generation agent memory, not a single-vendor or single-project idiosyncrasy.

### What GBrain adds: the compiled-truth-plus-timeline sub-pattern

GBrain enforces the compiled-truth-plus-timeline discipline *at the per-page level*. Prime Radiant currently enforces it at the *vault* level (`log.md`, `decisions/`, `pulse/` are append-only; individual pages are edited in place with `updated:` frontmatter). The per-page variant is a finer-grained convention worth evaluating:

```markdown
---
type: person
title: Alice Chen
---

[current best-understanding paragraph — edited in place]

---

- 2024-03-12: Met at AI Engineer Summit.
- 2024-09-04: Announced $12M seed led by Sequoia.
- 2025-01-18: Shipped open-source inference router.
```

The trade-off: per-page timelines double the friction on every edit (every edit also requires a timeline entry) but produce a clean per-page causal/temporal trace without needing to grep dated decision slugs. Prime Radiant has not adopted this discipline; the question is whether the additional friction is worth the per-page traceability. Watch-for: whether GBrain's pattern produces qualitatively-better per-page retrieval results in practice.

### What Claude Code dreaming adds: vendor-native multi-graph memory

Claude Code's dreaming feature is the first vendor-shipped (not third-party / not OSS-side-project) instance of the multi-graph pattern. Implications for Janus:

- The agent-memory layer is no longer something Janus needs to "build" — vendors will increasingly ship it natively.
- The portability question gets harder: dreaming-store format, inspection, export are all unstated as of the 2026-05-19 surfacing. Janus's posture (markdown vault is the source of truth; agent dreaming-stores are derivative) preserves portability while letting Janus take advantage of the dreamed-out summaries when Claude Code is the consumer.

## Short-term vs long-term

The above patterns are about *long-term* memory — what survives across sessions. There's a separate short-term axis: what fits in the active context window during a single multi-turn run. Per [[openai-agents-sdk-session-memory|OpenAI's Agents SDK Cookbook]] (May 2026), short-term memory is managed via a `Session` primitive with two canonical techniques: **trimming** (keep last-N user turns verbatim, drop the rest — deterministic, low latency, weak long-range recall) and **summarisation** (compress older turns into a synthetic summary message — strong long-range recall, vulnerable to "context poisoning" if a bad fact enters the summary). See [[context-engineering]] for the broader discipline; the Session abstraction is what makes the in-session technique a first-class harness concern rather than ad-hoc prompt wrangling.

This makes [[openai|OpenAI]]'s memory story explicit: short-term context management is well-developed (the Cookbook lays out concrete patterns and code); long-term/portable memory is comparatively under-articulated. The opposite of [[anthropic|Anthropic]]'s position, where the Managed Agents file-based memory is the public surface and short-term in-session context management is comparatively implicit.

## Open question for Janus

How portable is agent memory? If Janus standardises on Claude Managed Agents memory, can those memories migrate to a different provider later? This is a load-bearing question for any tool evaluation involving memory features. See [[ai-tool-evaluation]] framework — memory portability should likely be a Stage 1 viability criterion going forward.

## Adjacent concepts

[[retrieval-augmented-generation]] — the predecessor pattern; memory was previously delegated to retrieval over an external store, now increasingly first-class in agent platforms.
[[context-engineering]] — the broader discipline of shaping what agents see; memory is one input.
[[agent-harness]] — the orchestration layer around the model; tightly coupled to memory in current architectures.
