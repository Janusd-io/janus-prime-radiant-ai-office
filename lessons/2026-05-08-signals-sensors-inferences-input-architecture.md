---
type: lesson
title: Signals → sensors → inferences — design the input array, the AI does the rest
slug: 2026-05-08-signals-sensors-inferences-input-architecture
created: 2026-05-08
updated: 2026-05-08
departments: [marketing, ai-office]
status: active
owner: michael-bruck
sources: [2026-05-08-andrew-marketing-prime-radiant]
related: [andrew-soane, prime-radiant-three-layer-architecture, janus-prime-radiant-build, marketing-prime-radiant, agentic-ai, agent-memory]
---

# Signals → sensors → inferences — design the input array, the AI does the rest

## What happened

In the 2026-05-08 brainstorm with [[andrew-soane]], a real concern surfaced: would a Marketing Prime Radiant, fed only by *internal* signals (Janus meetings, Slack, projects, internal documents), be smart enough to recognise an externally-relevant pattern that hadn't been internally discussed yet? Andrew's example: a sustainability regulation hits retail; an internally-trained system has no internal data on retail or this specific regulation, so how would it surface relevance?

The reframe Michael landed on:

> "If you get the right signals, it will. Because here's the thing — how did you come up with that insight? You got that information through some conversation, some document that you read, somewhere. So if we identify what signals do you need to collect... I think of this as sensors. We've got building sensors. What are the sensors that need to pick up a variety of different signals? Because that's the way we'll get it automated."

Andrew's resolution: two infrastructure documents (ICP, target Personas, with topic taxonomy embedded) tell the system *what relevance looks like*. Combined with sensor coverage that includes external news, competitor intel, industry analyst pieces, and customer-side signals, the system can draw the inferences he was worried it couldn't.

## The lesson

**You cannot design a Prime Radiant for the questions you can predict. You can only design the sensor array — and let the AI find the patterns. Pre-specifying outputs is the failure mode; under-specifying inputs is the second failure mode.**

The shift in framing:
- *Old framing:* "What insights do we want the system to surface?" → leads to top-down design, narrow data, brittle outputs.
- *New framing:* "What signals do we need to capture? What strategic anchors define relevance?" → leads to dense sensor array + clear infrastructure layer → emergent insights.

This maps directly onto the [[prime-radiant-three-layer-architecture|three-layer architecture]]: Signals (raw inputs) + Infrastructure (the lens that defines relevance) → Outputs (inferences and synthesis emerge).

## The two complementary disciplines

1. **Throw the net wide on Signals.** Include voice/video transcripts, Slack, system-of-record exports, web inbound, emails, articles, news, competitor intel, industry analyst pieces. The discipline is *don't pre-filter for relevance at the sensor layer*. AI can handle volume; under-collecting starves the synthesis.

2. **Be precise on Infrastructure.** Document the strategic anchors (mission, ICP, Personas, country plans, topic taxonomy). The Infrastructure layer is what tells the system *what relevance looks like* — without it, dense Signals produce dense noise. With it, the same dense Signals produce precise relevance flags.

## Why this matters for instance design

Every department instance build sequence: **identify Signals → curate Infrastructure → let Outputs emerge.** Outputs cannot be designed top-down. The Marketing instance's outputs (briefs, POVs, campaign plans) are blocked on the Infrastructure layer being documented (ICP, Personas, country plans) — but the Signals layer can light up immediately (Fireflies, Slack, news scraping). This is why the AIO instance got good fast — its Infrastructure layer was implicit in CLAUDE.md and the SoR map; Signals lit up immediately on Web Clipper / Notion / Linear feeds; Outputs emerged after enough signal accumulated.

Andrew's intuition that "the AI won't know" was a top-down framing of the problem. The reframe — "what sensors does it need?" — is bottom-up and tractable.

## Cross-cutting application

This lesson is the foundational design principle for every subsequent Prime Radiant rollout. When standing up HR, Finance, IT-Ops, Office-of-CEO, Engineering, or Training instances, the build conversation is:
1. What sensors does this department already have or need? (Signals layer inventory.)
2. What strategic documents define what's relevant for this department? (Infrastructure layer.)
3. Stand up the Signals; document the Infrastructure; let Outputs emerge.

Resist the temptation to pre-specify what insights the instance "should" produce. That always produces narrow, brittle systems.

## Cross-references

This lesson is tightly bound to the [[prime-radiant-three-layer-architecture]] concept and was the conversational moment that made it crystallise. It also sharpens the [[agent-memory]] / [[llm-wiki]] / [[agentic-ai]] threads in the wiki — all of those rest on the same intuition: *give the agent the right perception, and inference is what it's good at.*
