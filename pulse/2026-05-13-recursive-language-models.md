---
type: pulse
title: Recursive Language Models — third paradigm for long context (after RAG and compaction)
slug: 2026-05-13-recursive-language-models
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office, engineering]
confidence: high
sources: [recursive-language-models]
related: [context-engineering, agentic-ai, post-rag-agent-data-stack, retrieval-augmented-generation, claude, openai, 2026-05-13-claude-os-concept-surfaced, standup]
---

# Recursive Language Models — third paradigm for long context

[[recursive-language-models|RLM]] (MIT CSAIL; Zhang, Kraska, Khattab; arxiv 2512.24601) proposes that long prompts should not be fed into the model directly. Instead, the LLM treats the prompt as a *variable inside a Python REPL environment* and writes code to inspect, decompose, and recursively call itself over snippets. Results: handles inputs >10× the model's context window; outperforms GPT-5 by a median of 26% over compaction, 130% over CodeAct-with-sub-calls, and 13% over [[claude|Claude]] Code across four long-context benchmarks. A small post-trained model (RLM-Qwen3-8B) gains 28% over its base and approaches vanilla GPT-5 on three of the four tasks. Code: `github.com/alexzhang13/rlm`.

## Why this matters now

The dominant industry framings for long context to date have been two:

1. **RAG / retrieval** — fetch relevant snippets at query time and inject. [[retrieval-augmented-generation|See concept page]].
2. **Compaction / summarisation** — keep recent turns verbatim, summarise older ones. [[claude]] Code and most agent harnesses do some form of this.

RLM is a third, distinct paradigm: **the LLM does its own context engineering at inference time** by writing code that reads the prompt as a data structure. This is conceptually *compilation-stage context engineering* (per [[context-engineering]]) applied at the inference layer — the agent decides what to look at, how to decompose, when to recurse, all through code rather than through a separately-engineered data pipeline.

The cost story is what makes this paradigm-changing rather than just clever: comparable cost to vanilla LLM calls on the same prompts, despite the recursion. Compaction is cheap but lossy; RAG is cheap but requires the upstream data work; RLM is cheap *and* expressive *and* doesn't require pre-processing the corpus.

## Janus implications

Three places this lands:

- **[[context-engineering|The context-engineering concept]] needs a third branch.** Currently the page distinguishes compilation-stage (pre-query data work) from in-session management (trimming / summarisation). RLM is *inference-time programmatic context engineering* — neither fits cleanly. Adding it as a third scale shifts the framing from "two scales" to "three modes."
- **The [[2026-05-13-claude-os-concept-surfaced|Claude OS research direction]] from this morning's standup is closely adjacent.** Jehad's framing — Claude interacts with a structured environment via APIs rather than reading files directly — and RLM's framing — LLM treats the prompt as a REPL variable and writes code over it — are the same intuition arriving from different angles. The Claude OS investigation should track RLM's framework as prior art.
- **[[standup|The standup skill]] could benefit operationally.** Today's Fireflies transcripts already strain context windows; today's 72-min meeting hit ~95KB. The current approach (read the whole transcript into the model) is exactly the failure mode RLM targets. Not a near-term swap-in — Claude doesn't natively support RLM-style recursion yet — but it's a future axis of improvement for any skill processing long sources.

## Open questions

- Does the RLM paradigm require a model post-trained for recursion, or do off-the-shelf frontier models (Claude Opus 4.6, GPT-5) work well enough zero-shot? The paper's small post-trained model (RLM-Qwen3-8B) hints that explicit training helps; the GPT-5 results suggest zero-shot is already strong.
- How does RLM compose with file-based agent memory (Claude Managed Agents, Mnemon)? In principle: RLM handles in-prompt reasoning; agent memory handles cross-session persistence. They're orthogonal.

## Watch for

- Anthropic / OpenAI shipping a first-class RLM-style recursion primitive in their agent SDKs.
- Whether Khattab's group at MIT (also behind DSPy) folds RLM into the DSPy framework.
- Cost-at-scale validation on real production workloads — paper's "comparable cost" claim is benchmark-bound.
