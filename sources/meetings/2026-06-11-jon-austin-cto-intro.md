---
type: meeting
title: Introduction call — Jon Austin (CTO candidate) + Michael Bruck + Bonaventure Wong
slug: 2026-06-11-jon-austin-cto-intro
date: 2026-06-11
created: 2026-06-11
participants: [michael-bruck, bonaventure-wong, jon-austin]
departments: [ai-office, office-of-ceo]
attribution: confirmed
attribution_sources: []
---

# Introduction call — Jon Austin + Michael Bruck + Bonaventure Wong

**Date:** 11 June 2026, 10:49 AM  
**Participants:** Michael Bruck (in conference room `jdg-cr02 DXB Office`), Bonaventure Wong (named directly), Jon Austin / Jono Austin (remote).

**Attribution note:** `jdg-cr02 DXB Office` is the Janus Dubai conference room system account. **Michael Bruck confirmed he was the person in the conference room** — all `jdg-cr02 DXB Office` utterances are attributed to Michael Bruck. Note: Michael referred to "cr01" when confirming attribution; the Fireflies label shows "cr02 DXB Office" — treated as the same person regardless. Jon Austin is unambiguously the remote participant. Bonaventure Wong is named directly.

## Context

Bonaventure arranged this intro. Jon Austin will join Janus as CTO. Connection pathway: Chris Ash (Mocks/Mox fintech network) → "Ned" → Bonaventure → Jon Austin.

## Jon Austin background (from transcript)

Australian. Started as engineer (hardware/software), went into management ("the dark side"), now back in the weeds — describes this as a maturity/joy thing. Key career markers:
- AWS principal architect (first principal hire in Singapore, ~2019); pre-sales experience for large clients; found AWS infra complex and over-engineered
- Fintech background; worked with/around Mox (Standard Chartered virtual bank Hong Kong), Vacuum Labs team
- Has experimented with: Hermes (agentic framework), Claude, Open Interpreter ("too dangerous"), Claude Fable (released ~Jun 9-10 2026, very excited about it)
- CTO WhatsApp groups where Hermes is being heavily discussed
- Recently deployed a multilingual website entirely with Claude; ranked #1 on Google in 6 weeks
- Involved in deploying a fintech startup (cloud agnostic, custom auth — acknowledges this was over-engineered)
- "Build vs buy pendulum has massively swung to build in the last few months" — credits Opus 4.5 (December last year) and Claude Fable this week as step-change moments

## Key technical discussion

### Prime Radiant architecture (Michael's explanation)
Michael gave Jon a detailed walkthrough:
- LLM wiki / continual learning loop: not RAG (which "is like Dory the fish"), but progressive index + grep + CLAUDE.md rulebook enabling context assembly
- GitHub-backed markdown files; Obsidian Git sync; several thousand files; "gets better the more you use it"
- Referenced David Haber (a16z) piece about verbal vs written companies; companies where knowledge evaporates after meetings vs companies where it's captured
- Brittleness acknowledged: lock file issues, runs on device, needs to move to cloud/containerized

Jon's validation: *"It's a continual distillation. Right. It just gets tighter and tighter."* — and compared it to ASCII's return ("Markdown is the same for LLM"). Discussed SQLite apps that scale to a million users on one file as an analogy for simplicity-at-scale.

### Hermes framework (Jon's recommendation)
Jon recommended **Hermes** as an agent orchestration framework. Description from transcript:
- Open source; commercial hosted model (like Supabase)
- "Pulls you back from the API and provider-specific integrations"
- Abstracts whether the data source is RAG, markdown directory, SQL database
- Implements guardrails
- Developers love it; growing in CTO circles
- Jon is currently experimenting with it

Michael: Hermes is on his tracker but hasn't tried it. Will evaluate. Sees Hermes as potentially plugging into the Claude Agent SDK to provide a less Cowork-dependent runtime.

### Claude Fable
Released in the past 48 hours (per Jon, so ~Jun 9-10 2026). Jon: *"With Fable, it's another step change again."* Heavy buzz in CTO WhatsApp groups. Jon planning to dive in that evening.

### Australian bank anecdote (Jon)
Top-4 Australian bank spending 250–280M/year on Anthropic (trailing 12 months). Access model: non-technical staff gated through Microsoft Teams interface; technical staff have unfettered Claude access. Got temporary access to Claude Mythos Preview — ran it across internal/external codebase, found 9,000 vulnerabilities. Caused internal panic.

### Infrastructure discussion
Michael's frustration: Claude cannot reliably provision cloud infrastructure (CloudFront, Vercel, complex stacks). Jon validated this and suggested Cloudflare Workers as much simpler alternative. Jon: *"I've had 100% success with Cloudflare Workers — just deploy on free tier."* Also mentioned Terraform with Claude Code as workable (with human follow-up cleanup).

Jon's principle: "Trending from over-engineering to keeping it simple" — don't need multi-AZ EC2 + RDS for an internal tool.

### Build vs buy
Jon closing thought: *"The needle on build versus buy has just massively swung to build in the last few months."* Open source + extend + maintain > buying enterprise SaaS for internal tools. Twenty CRM example resonated with Jon ("I've been using Odoo — interesting").

### Temporal (mentioned by Jon)
Temporal — durable workflow engine originally from Uber (Cadence); founder forked it after leaving Uber. Just valued at $5.5B. Mentioned as example of successful commercial open source model ("the commercial open source model I'm a big proponent of").

## Relationship / next steps

- Bonaventure: Janus scaling to 10 countries by end of year; satellite offices; knowledge base connectivity is the proving point
- Jon offered to give a hand on website/infra work
- Michael to share Hermes evaluation with Jon; will add Hermes to Linear tracker
- Jon's email exchanged; Michael to follow up
