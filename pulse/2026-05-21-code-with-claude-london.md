---
type: pulse
title: Code with Claude (London) — Anthropic's developer event signals "let it cook" as default
slug: 2026-05-21-code-with-claude-london
created: 2026-05-23
updated: 2026-05-23
departments: [ai-office, engineering]
confidence: high
sources: [2026-05-21-mit-tech-review-code-with-claude-london]
related: [claude, claude-code, anthropic, agent-memory, ai-native-enterprise-restructuring]
---

# Code with Claude (London) — Anthropic's developer event signals "let it cook" as default

Anthropic ran its two-day **Code with Claude** developer event in London on 2026-05-19/20 — deliberately scheduled the same day as Google's I/O keynote in Palo Alto (an Anthropic-staffer-disclaimed coincidence, per MIT Technology Review). Coverage at [[2026-05-21-mit-tech-review-code-with-claude-london]]. The event surfaces three signals worth tracking:

1. **"Let it cook" is the new default.** Boris Cherny (head of Claude Code) in the opening keynote: *"The default isn't 'I'm going to prompt Claude' — the default is now 'I'm going to have Claude prompt itself.'"* Anthropic's goal is full automation — Claude tests, tweaks, retries until everything runs, ideally without the developer seeing the error messages. The endpoint, per product lead Angela Jiang: *"Claude basically being able to build itself."*

2. **"Dreaming" — agent-memory landing inside Claude Code natively.** Announced ~2026-05-07, demoed by Ravi Trivedi at the event. Claude Code agents write task-specific notes; later agents read them to bootstrap context and avoid past errors. *Dreaming* itself is a consolidation pass — pattern-spotting across the accumulated notes. This is the [[agent-memory]] multi-graph pattern (per [[2026-05-13-magma-multi-graph-agentic-memory]], [[2026-05-12-mnemon-llm-supervised-memory]]) landing as a native Claude Code feature rather than as a third-party add-on. Worth watching whether the dreaming-store is inspectable / portable / multi-tenant.

3. **In-room adoption metric.** Cherny showed that almost half the packed room (developers, many coding live on knees during talks) had shipped a Claude-Code-written PR in the previous week; most of those hands stayed up when asked whether they'd shipped one *without reading the code*. Anecdotal but the strongest single in-room signal to date of the propagation of the "ship without reading" default. Customer showcases: Spotify, Delivery Hero, Monday.com, plus the vibe-code-tools-for-vibe-coders cluster (Lovable, Base44, Monday.com).

## Counter-signal

The MIT TR piece deliberately weighs the in-room enthusiasm against developer complaints (Hacker News / Reddit / 404 Media) that AI tooling pushes review burden upstream, atrophies skills, and produces less-secure code. Anthropic engineering lead Katelyn Lesse: *"All of the old software development best practices still apply. … I think there are a lot of people and teams that may have lost sight of them in this moment."* Implication for Janus: the *let it cook* default still requires the human as **framer of record** — see [[pre-ship-confidence-and-frame-check]] for the gate that operationalises this.

## Why this matters

Reinforces three working AIO theses already in the wiki:

- The [[claude-code]] surface keeps becoming more capable across short cadence (4.6 February, 4.7 April) — supports continuing to standardise the AIO's skills (`/standup`, `/ai-registry`, `/ai-tool-evaluation`) on Claude Code.
- The agent-memory layer is converging across vendors fast — Claude Code's *dreaming*, Mnemon's four-graph store, MAGMA's experimental validation. The Janus Prime Radiant pattern (file-based, four-axis frontmatter — see CLAUDE.md §4) sits in the same conceptual family.
- The "Claude as midlevel engineer" framing (Lesse) gives Bonaventure a clean handle for the [[ai-native-janus-positioning]] pitch: AI doesn't replace the senior engineer who frames the system — it replaces the junior who would have shipped the PR.

## Cross-reference

The Code-with-Claude event ran the same week as **Google I/O** ([[2026-05-19-google-io-2026-agents-as-product]]) and **Anthropic's Stainless acquisition** announcement (~$300M; surfaced in the same Every / Context Window write-up at [[2026-05-20-every-google-io-agents-agents-agents]]). The trio of events together makes 2026-W21 the most consequential single week of agent-platform competitive moves YTD — see [[ai-native-enterprise-restructuring]] for the strategic synthesis.
