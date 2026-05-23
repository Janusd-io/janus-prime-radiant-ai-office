---
type: vendor
title: Claude Code
slug: claude-code
created: 2026-05-14
updated: 2026-05-23
departments: [ai-office, engineering]
status: active
confidence: high
sources: [2026-05-21-mit-tech-review-code-with-claude-london]
related: [claude, anthropic, agent-skills, agent-memory, janus-prime-radiant-build, ai-native-enterprise-restructuring]
---

# Claude Code

CLI / IDE coding agent built by [[anthropic|Anthropic]]; part of the [[claude|Claude product family]]. See the umbrella entry at [[claude]] for the full family and Janus's broader posture — this page exists as a thin pointer so `[[claude-code]]` references resolve cleanly without duplicating the umbrella content.

## Janus use

Active across engineering. The `/standup`, `/ai-registry`, and `/ai-tool-evaluation` skills run on Claude Code as their execution surface; the [[janus-prime-radiant-build]] tooling (template repos, scripted instance setup) leans on Claude Code for its scripting and file-manipulation primitives.

## Product trajectory — Q2 2026 (added 2026-05-23)

Sourced from MIT Technology Review coverage of **Code with Claude**, Anthropic's two-day developer event in London (kickoff 2026-05-19, same day as Google I/O; see [[2026-05-21-mit-tech-review-code-with-claude-london]]) and the [[2026-05-21-code-with-claude-london|pulse entry]] of the same event.

- **Model cadence accelerating.** Claude 4.6 (February 2026) and Claude 4.7 (April 2026) materially upgrade the coding agent. Anthropic engineering lead Katelyn Lesse: *"Claude is probably as good as a midlevel engineer at writing code"*; *"You still need expert engineers to design a system and troubleshoot harder problems."*
- **In-room adoption signal.** Boris Cherny (Claude Code lead, opening keynote) showed almost half the packed room had shipped a Claude-Code-written PR in the last week; most kept their hands up when he asked whether they had shipped one *without reading the code*. This is the strongest single anecdotal signal yet of how far the "let it cook" default has propagated.
- **"Dreaming" — new agent-memory feature** (announced 2026-05-07-ish, surfaced at the event). Claude Code agents write task-specific notes to themselves; later agents read the notes to get up to speed and avoid past errors. *Dreaming* itself is a consolidation pass over those notes — pattern-spotting and common-issue identification across tasks. Relevance for Janus: this is the [[agent-memory|agent-memory layer]] landing inside Claude Code natively, in the same multi-graph pattern surfaced by [[2026-05-13-magma-multi-graph-agentic-memory]] and Mnemon ([[2026-05-12-mnemon-llm-supervised-memory]]) earlier in May. Worth watching whether the dreaming-store becomes inspectable / portable (i.e., whether a Janus team can read another's accumulated notes).
- **"Let it cook" / Claude prompts itself.** The default operating mode pitched at the event: *"The default isn't 'I'm going to prompt Claude' — the default is now 'I'm going to have Claude prompt itself.'"* End-state Anthropic is targeting: developer doesn't see error messages; Claude tests-and-tweaks autonomously until everything runs. Product lead Angela Jiang: *"the absolute end state we're trying to get to is Claude basically being able to build itself."*
- **Customer showcases** (Code with Claude stage talks): Spotify, Delivery Hero, [[monday|Monday.com]], plus three startups (Lovable, Base44, Monday.com) "vibe-coding apps that help people vibe-code apps."

## Counter-signal — sustainability concerns to watch

The MIT TR piece counterweighs the in-room enthusiasm with skeptic-quotes from Hacker News / Reddit (developers reporting that AI tools push extra review burden upstream; complaints that coding skills atrophy as more is handed to AI; researcher warnings that AI-produced code is more vulnerable to attacks). Lesse's response: *"All of the old software development best practices still apply. They've applied this entire time. I think there are a lot of people and teams that may have lost sight of them in this moment."* This maps to the Janus posture of routing all coding-agent work through review, source-tracking, and the [[pre-ship-confidence-and-frame-check|pre-ship confidence + frame check]] gate — the *let-it-cook* default does not absolve the human of the framer-of-record role.

## See also

- [[claude]] — umbrella product-family page (preferred entry point).
- [[agent-skills]] — the abstraction Claude Code uses to package reusable workflows.
- [[agent-memory]] — concept page; the *dreaming* feature is Claude Code's instantiation of the agent-memory layer.
- [[ai-native-enterprise-restructuring]] — the strategic brief tying the Claude-Code adoption trajectory to the broader enterprise AI-native moment.
