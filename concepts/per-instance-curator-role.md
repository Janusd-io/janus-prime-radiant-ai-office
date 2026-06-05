---
type: concept
title: Per-Instance Curator Role
slug: per-instance-curator-role
created: 2026-06-05
updated: 2026-06-05
departments: [ai-office]
status: active
confidence: high
sources: [per-instance-curator-role, 2026-06-05-aio-standup]
related: [janus-prime-radiant-build, prime-radiant-instance-setup, nanoclaw, claude-md-v0.14-schema-bump-proposal]
---

# Per-Instance Curator Role

## One sentence

Each Prime Radiant instance has **one designated curator** who runs Obsidian locally and owns the vault's discipline. Everyone else is a contributor who accesses the instance through NanoClaude (Slack) — no local Obsidian required.

## Why this matters

The curator pattern solves three problems that surface as Prime Radiant rolls out to multi-person teams:

1. **Race conditions.** If more than one person runs Obsidian against the same vault, git `index.lock` conflicts and divergent edits accumulate. One curator = one writer = no contention.
2. **Deployment complexity.** Obsidian + Obsidian Git + CLAUDE.md fluency is non-trivial to install and maintain on every employee's machine. One curator per instance — not one per user.
3. **Judgment consistency.** The CLAUDE.md rulebook requires human judgment: which contradiction to flag, which orphan to archive, when attribution needs softening. A single curator develops this judgment steadily; distributed curation dilutes it.

## Curator vs contributor

| | Curator (one per instance) | Contributor / user (everyone else) |
|---|---|---|
| **Interface** | Obsidian (local clone) + NanoClaude | NanoClaude via Slack DM only |
| **Write access** | Push rights to canonical remote | Drop content into `inbox/` via Slack; curator triages |
| **Responsibilities** | Daily triage, weekly lint, questions/ review, CLAUDE.md judgment calls, log.md + index.md maintenance | Ask questions, surface decisions, drop content |
| **Obsidian required** | Yes | No |
| **Rulebook fluency** | Required — must be trained on CLAUDE.md and lint discipline | Not required |
| **Docker / NanoClaude install** | Optional (curator may also run NanoClaude locally during early deployment) | Not required |

## Curator responsibilities

**Daily (or on each ingest cycle):** triage NanoClaude-surfaced drafts — `inbox/` deposits, chat replies, PRs. File what warrants filing; edit what needs tightening; drop what doesn't earn its keep. Update `log.md` and `index.md` in lockstep.

**Weekly (or per the §5.3 10-ingest threshold):** run lint. Resolve judgment calls: which contradiction to flag, which orphan to archive, when to file a `questions/` escalation, when attribution needs softening.

**As triggered:** review open `questions/` for items ready to promote to brief or decision. Review `pulse/` for converging themes that warrant a brief.

**As-needed:** propose CLAUDE.md edits via `questions/` pages; coordinate with adjacent-instance curators for cross-vault federation.

## Curator ≠ team lead

The PM-team instance (2026-06-05) established this precedent explicitly: **[[lysander-liu]] holds the curator role** while **[[euclid-wong]] and [[rosa-wu]] remain the team leads**. The curator is the person best-positioned to do the work — by skill, inclination, and bandwidth — regardless of org-chart position. This matters for scale: leadership roles and vault-maintenance roles should be assignable independently.

## Selection criteria

A good curator has all three:
- **Inclination** — they want to do this kind of work (triage, lint, judgment calls, knowledge organisation)
- **AI/tooling fluency** — comfortable with Obsidian, git, CLAUDE.md, and NanoClaude; not afraid of the rulebook
- **Domain fluency** — understands the team's content well enough to make good filing and attribution decisions

## Deputy policy

Deputies are recommended where headcount allows. The deputy can step in during PTO/illness/busy periods. Operating rule: **only the primary or the deputy runs Obsidian at any given time** — not both simultaneously (race condition). Single-person instances (Marketing, Bonaventure's) accept the queue during unavailability.

Confirmed deputies per instance (as of 2026-06-05):
- **AIO:** primary = Michael Bruck; deputy = Jehad Altoutou
- **PM team:** primary = Lysander Liu; deputy = Rosa Wu or Spike Zhao (to be confirmed with PM team)
- **Marketing:** primary = Andrew Soane; deputy = none (single-person instance)
- **Bonaventure:** primary = Bonaventure Wong; deputy = none (single-person instance)

## Current instances

| Instance | Curator | Contributors | Notes |
|---|---|---|---|
| **AIO** | [[michael-bruck]] | [[jehad-altoutou]] | Implicit; Jehad is highly rulebook-fluent |
| **Marketing** | [[andrew-soane]] | (none yet) | Single-person; curator = contributor |
| **Bonaventure** | [[bonaventure-wong]] | (none) | CEO personal vault |
| **PM team** | [[lysander-liu]] | [[rosa-wu]], [[spike-zhao]] | First explicit curator ≠ team lead separation |

## Handoff protocol

When a curator rotates out: two-week pair-curate with the incoming curator. CLAUDE.md is the manual; [[prime-radiant-instance-setup]] is the runbook. A `processes/curator-handoff.md` page will be written when the first handoff occurs.

## NanoClaude and the curator pattern

NanoClaude is the **contributors' read interface** and the **curator's draft-staging assistant**. It is not a second autonomous curator. The human curator reviews NanoClaude-surfaced drafts before they enter the canonical vault. This keeps the curator in the loop without burdening contributors with Obsidian access.

## Source

Ratified in AIO Standup, 5 June 2026. Jehad Altoutou: *"Take the decisions. This just makes sense. Let's go for it. New policy. Make it formal."* See [[per-instance-curator-role]] (questions/) for the full design rationale and open sub-questions.
