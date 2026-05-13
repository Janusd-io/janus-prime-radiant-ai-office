---
type: question
title: New entity candidates from the 23-article Mivory batch
slug: 2026-05-06-mivory-batch-1-new-entity-candidates
created: 2026-05-06
updated: 2026-05-06
status: resolved
owner: michael-bruck
sources: [claude-managed-agents-launch, claude-code-routines, marp-homepage, openclaw-assistant-ryancarson, mempalace-milla-jovovich, arscontexta-claude-code-plugin, cheap-claude-tokens-china, your-harness-your-memory-hwchase17, elvis-saravia-personal-research-kb]
related: [2026-04-08-claude-managed-agents-launch, 2026-04-14-claude-code-routines, 2026-04-22-google-skills-repository, anthropic, marp, openclaw, claude]
---

# New entity candidates — Mivory batch 1 (resolved)

Escalation per `CLAUDE.md` §5.1 from the 23-article Mivory backfill batch.

## Resolutions — vendors

| Candidate | Recommendation | Decision | Notes |
|---|---|---|---|
| Anthropic | Create | **Approved** | Created as `entities/vendors/anthropic.md`. |
| Claude Code | Create as separate vendor | **Rejected** | Per Michael: Claude Code, Claude Managed Agents, and other Anthropic surfaces all live under `entities/vendors/claude.md` as one product family. claude.md expanded to cover the umbrella. Precedent set: vendor-page-per-sub-product fragments cross-references without benefit. |
| Claude Managed Agents | Create as separate vendor | **Rejected** | Same as Claude Code. Lives under [[claude]] as a sub-product. |
| Marp | Create | **Approved** | Created as `entities/vendors/marp.md`. |
| MemPalace | Defer | **Confirmed** | Niche; mention in [[agent-memory]] is sufficient. |
| OpenClaw | Defer (recommended) | **Approved (override)** | Per Michael: create. Created as `entities/vendors/openclaw.md` with low confidence; single source so far. |
| arscontexta plugin | Defer | **Confirmed** | Mentioned in [[llm-wiki]]. Promote if Janus evaluates or adopts. |

## Resolutions — people

All deferred per Michael's general policy: external people defer.

## Resolutions — concept candidates

The 5 concept pages I created during ingest ([[agent-memory]], [[model-context-protocol]], [[agent-to-agent-protocol]], [[agent-skills]], [[agent-harness]]) stand. No pushback received.

## Precedent set

**Multi-product vendors live under one umbrella.** Anthropic = company; [[claude]] = the product family (Claude API/models, Claude Code, Claude Managed Agents, Cowork, Claude in Chrome, etc.). This is the template for how to handle other vendors with multiple sub-products as the wiki grows.

## Closeout

`status: resolved` 2026-05-06.
