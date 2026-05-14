---
type: source
source_type: laptop
title: prime-radiant-personal
slug: prime-radiant-personal
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/references/prime-radiant-personal.md
original_size: 6429
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "Design rationale for the janus-brain skill — internal dept documentation, no PII / secrets / personal content."
---

# prime-radiant-personal

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/references/prime-radiant-personal.md` on 2026-05-14._

# Personal [[prime-radiant|Prime Radiant]] — the pattern

The personal-tier instance of [[[janus-prime-radiant|Janus Prime Radiant]]](https://drive.google.com/drive/folders/1GWBIIo1gsextmEgJv9fx2fJDWv9ABpuD). One vault per Janus employee, derived from the AIO CLAUDE.md v0.8 schema, federating up to the relevant Department Prime Radiant via `departments:` + `audience:` frontmatter.

This document is the design rationale and the canonical reference for the skill's behaviour. The user-facing rulebook lives in `templates/personal-claude-md.md` (gets copied into the user's vault as `CLAUDE.md` on scaffold).

## Why personal-tier

The AIO Prime Radiant captures **what Michael curates** — high-signal but one perspective. As Prime Radiant scales to Marketing, HR, Finance, etc., each curator faces the same bottleneck. The personal tier turns every employee's laptop and [[fireflies|Fireflies]] attendance into a contributing sensor array that feeds the department instance.

Without the personal tier:
- Knowledge stays trapped on individual laptops
- Curators can only ingest what they personally encounter
- Cross-departmental meetings get logged in one curator's vault but not the other's
- The CEO-level twin is architectural, not mechanical — there's no actual flow to it

With the personal tier:
- Every employee's signals layer feeds the department's synthesis layer
- Cross-dept meetings naturally federate to both instances
- The CEO twin is mechanically realisable — federate everything up
- Liability is traceable via `captured_by:` from any wiki page back to a person and a source

## Tier model

```
Personal (per employee)
  └── audience routing via departments: + audience:
      ↓
Department (per dept; AIO live, Marketing scaffolding, others queued)
  └── curator-owned ingest discipline applies
      ↓
Org (when it exists; cross-dept public synthesis)
  └── federation of audience: org notes
      ↓
CEO (Bonaventure; superset read-only)
```

[[federation|Federation]] is push-only and upward. A department instance never writes back to a personal instance. The Org instance never writes to a department instance.

## Schema additions vs AIO v0.8

Two frontmatter fields are **required** at the personal tier (optional or absent at department tier today):

### `audience:`

Values:
| Value | Federation behaviour |
|---|---|
| `personal` | Never federates. Stays in personal vault only. |
| `department` | Federates to each instance listed in `departments:`. |
| `departments:<a>,<b>` | Only the listed instances. Use for cross-dept meetings where the audience set is narrower than the union of attendee depts. |
| `org` | Every department instance + the Org instance. |
| `ceo-only` | CEO instance only. |

Default when subagent is uncertain: `department` (per user preference 2026-05-11).

### `captured_by:`

The kebab-case slug of the person whose laptop produced the page. Never strippable during sanitisation. Chain-of-custody for federated content.

## Privacy boundary

Three layers of privacy protection in order:

1. **Capture filter** (`config/exclude-*.txt`) — many files never reach the personal vault. Five-layer model documented in `references/privacy-filter.md`.
2. **Ingest classification** — every page that makes it into the personal vault is auto-classified into an `audience` band. Subagent biases toward `[personal]` when in doubt about personal/financial/medical/legal markers.
3. **Federation sanitisation** — even after classification, the federation script strips `original_path`, any `personal_*` frontmatter, and refuses to push `audience: personal` notes anywhere.

## Failure modes and mitigations

| Failure | Mitigation |
|---|---|
| Subagent miscategorises a private note as `[department]` and federates it | Federation goes via target `inbox/`, not direct write. Department curator catches it before it lands in their wiki. |
| Subagent invents a new entity that conflicts with an existing AIO one | Per AIO §5.1, new entities are high-stakes → escalates to `questions/ingest-*.md` in the personal vault. Personal owner reviews and decides before federation. |
| Two people in a cross-dept meeting capture the same transcript twice | Federation filename is `personal-<person-slug>-<original-slug>.md`. Department curator sees both and dedups during their ingest. |
| Fireflies pull picks up a recurring 1:1 the `/standup` skill is already processing | Default skip rules in `fetch-fireflies.py` — title heuristics for "standup", "1:1", "one on one". Override with `--no-skip-recurring`. |
| Personal vault grows unbounded | Five-layer privacy filter caps capture. Walker hard-stops at 5k files / 5M words and asks for scope reduction. Oversized files (>2 MB text) get stub notes only. |
| Personal CLAUDE.md drifts from AIO CLAUDE.md | Personal CLAUDE.md is generated from `templates/personal-claude-md.md` each install. Manual edits survive subsequent runs but drift is detectable by comparing version markers. |

## Cron, logs, audit

- Nightly cron at `0 3 * * *` runs `claude -p "/janus-brain sync"` non-interactively
- Every action appends to `<vault>/log.md` (ingest, federate, lint, scaffold)
- Every chunk's actions written to `<skill>/state/ingest/chunk_NN.json` for renderer validation
- Federation state in `<skill>/state/federation.json` (hashes for delta computation)
- Sync log in `<skill>/state/nightly.log`

## What's NOT done by this skill

- **Org-level synthesis** — that's a department curator's job, not the personal tier's
- **Cross-tier graphify** — the personal vault gets its own graphify pass; cross-tier graphify is a future Org-instance concern
- **Slack ingest** — out of scope for v0.1; the AIO instance does this via Web Clipper and bookmarks
- **Real-time capture** — the cron is the cadence. Real-time would require file-system watching and is a future addition
- **Multi-person same-machine** — assumes one Personal PR per laptop. Shared machines aren't supported

## See also

- `templates/personal-claude-md.md` — the rulebook that lands in each personal vault
- `prompts/enrichment-subagent.md` — the contract subagents follow during ingest
- `references/privacy-filter.md` — five-layer capture filter
- `briefs/personal-prime-radiant-proposal.md` — the proposal escalated to Michael for AIO review
- AIO CLAUDE.md at `<Drive>/Shared drives/Janus AI Office/Janus Prime Radiant — AI Office/CLAUDE.md` — the canonical pattern this derives from
