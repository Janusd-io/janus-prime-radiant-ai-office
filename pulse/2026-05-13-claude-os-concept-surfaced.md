---
type: pulse
title: Claude OS concept — Hostinger-hosted vault files behind purpose-built APIs/MCPs
slug: 2026-05-13-claude-os-concept-surfaced
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office, engineering]
confidence: low
sources: [2026-05-13-aio-it-meeting]
related: [janus-prime-radiant-build, hostinger, claude, jehad-altoutou]
---

# Claude OS concept — Hostinger-hosted vault files behind purpose-built APIs/MCPs

[[jehad-altoutou|Jehad]] surfaced a new architectural direction in the [[2026-05-13-aio-it-meeting|13 May AIO-IT standup]]: instead of Claude reaching into vault files directly via filesystem or Drive APIs, host the vault on [[hostinger]] and front it with **purpose-built APIs / MCP servers** that expose structured operations (read entity, append decision, lint, query by department, etc.) rather than raw file access. Working title "Claude OS" — the connector layer becomes the *operating-system surface* between Claude and the institutional knowledge base.

## Why this is worth tracking

- **Naturalises the abstraction we keep paying for at the ingest layer.** Today, every ingest pass re-derives "what does this Monday item have to do with that decision page" through filesystem scans and frontmatter parsing. If the vault sat behind a typed API, those joins move to the data layer.
- **Decouples Claude's harness from the storage backend.** Whether the vault lives on Drive, GitHub, or Hostinger becomes a back-end choice the agent doesn't see — only the API contract matters. Aligns with the *decoupling-the-brain-from-the-hands* framing emerging in Claude Managed Agents.
- **Concrete trigger:** the Drive webhooks investigation (2912592197) is a tactical improvement over polling, but a webhook still delivers raw file events. The Claude OS direction asks whether we should be receiving *semantic* events ("decision X was logged") rather than file events ("decisions/foo.md was modified").

## Status

- Approved for **research only** in the standup — architecture exploration, not commitment.
- Monday research item created under Engage data architecture (2912590122).
- **Depends on Drive webhooks API research outcome** (2912592197); if Drive webhooks resolve the event-driven ingest problem cheaply, Claude OS gets deprioritised. If they reveal further friction, Claude OS gets a real evaluation.

## Open questions

- Where does this sit relative to [[janus-prime-radiant-build]]'s GitHub-as-substrate decision? Does Hostinger become an *additional* surface, or a *replacement* if/when adopted?
- Does the API surface look more like a REST/GraphQL layer or a curated MCP toolset? The latter is Claude-native; the former is more portable across agent platforms.
- Cost / operational complexity of running purpose-built APIs over the current "Claude reads markdown directly" baseline — what's the actual win?
