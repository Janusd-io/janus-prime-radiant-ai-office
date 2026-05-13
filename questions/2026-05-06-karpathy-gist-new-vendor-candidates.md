---
type: question
title: Which tools mentioned in the Karpathy gist warrant their own entity pages?
slug: 2026-05-06-karpathy-gist-new-vendor-candidates
created: 2026-05-06
updated: 2026-05-06
status: resolved
owner: michael-bruck
sources: [karpathy-llm-wiki]
related: [llm-wiki, janus-prime-radiant-build, claude, vs-code, zed]
---

# Karpathy gist — new entity candidates (resolved)

Escalation from the inaugural ingest of `sources/articles/karpathy-llm-wiki.md`. Per `CLAUDE.md` §5.1, creating new entity pages is a high-stakes action; flagged for Michael's review rather than auto-created.

## Resolutions

| Candidate | Recommendation | Decision | Notes |
|---|---|---|---|
| Cursor | Create | **Rejected** | Michael uses [[vs-code]] and [[zed]] for editing, not Cursor. Karpathy may be habituated to Cursor; no reason to mirror that choice in this wiki. Reconsider only if Cursor is later adopted. |
| Claude | Create | **Approved** | Created as `entities/vendors/claude.md`. Foundational — powers this wiki's maintenance. |
| Marp | Defer | **Deferred** | Niche. Create on first real use at Janus. |
| qmd | Defer | **Deferred** | Optional infra; we explicitly chose index-based browsing for v1. |
| Dataview | Don't create standalone | **Confirmed** | Covered in [[obsidian]]. |
| Eureka Labs | Don't create standalone | **Confirmed** | Mention in [[andrej-karpathy]] is sufficient. |

## Additional pages created from this resolution

- [[vs-code]] — Michael-named as actual editor; created as a vendor page.
- [[zed]] — same.

## Closeout

`status: resolved` 2026-05-06. The Cursor rejection is a useful precedent: the wiki should reflect the Janus tool stack, not the source author's stack. Future ingests should respect this when proposing new vendor pages from articles.
