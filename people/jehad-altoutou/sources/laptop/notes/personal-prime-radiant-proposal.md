---
type: source
source_type: laptop
title: personal-prime-radiant-proposal
slug: personal-prime-radiant-proposal
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/briefs/personal-prime-radiant-proposal.md
original_size: 8072
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "Strategic brief proposing the Personal Prime Radiant tier to Michael; AIO-internal content, no PII or credentials"
project: janus-brain-bootstrap

---

# personal-prime-radiant-proposal

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/briefs/personal-prime-radiant-proposal.md` on 2026-05-14._

---
type: brief
title: Personal [[prime-radiant|Prime Radiant]] — why per-employee instances are the missing tier
slug: personal-prime-radiant-proposal
created: 2026-05-11
updated: 2026-05-11
departments: [ai-office, hr, it-ops, marketing, finance, office-of-ceo, engineering, training]
confidence: medium
status: active
owner: jehad-altoutou
audience: [departments:ai-office]
captured_by: jehad-altoutou
sources: [janus-prime-radiant-build, 2026-05-08-andrew-marketing-prime-radiant, llm-wiki, 2026-05-08-marketing-prime-radiant-as-separate-vault]
related: [janus-prime-radiant-build, ai-office, marketing-prime-radiant, standup, llm-wiki]
---

# Personal Prime Radiant — why per-employee instances are the missing tier

The Prime Radiant pattern federates from a department instance up toward a Janus-wide knowledge twin via the `entities/departments/` layer (per [[janus-prime-radiant-build]] and [[2026-05-08-marketing-prime-radiant-as-separate-vault]]). What it doesn't yet have is a **per-employee tier below the department instance** — the signal-capture layer that turns each person's laptop, [[fireflies|Fireflies]] meetings, and curated reading into a contributing source for their department's Prime Radiant.

This brief proposes filling that gap with a **Personal Prime Radiant** per employee — same CLAUDE.md schema (derived from AIO v0.8), [[federation|federation]] flowing up via the locked `departments:` vocabulary, scaffolded and maintained by a [[claude-code|Claude Code]] skill (`/janus-brain`). The proposal is escalated to AIO for Michael's review before any roll-out beyond Jehad's own laptop.

## Why this matters to AIO

The AIO Prime Radiant currently ingests **what Michael curates** — Slack bookmarks, Web Clipper articles, Fireflies meetings he attends, standup-skill output. That's high-signal but it's one person's perception of the AIO. As Prime Radiant rolls out to other departments (Marketing live since 2026-05-08; HR/Finance/IT-Ops/Office-of-CEO/Engineering/Training queued), each department curator (Andrew for Marketing, Theresa for HR, etc.) will face the same scaling problem: they can curate their own bookmarks, but they can't see what their team members are reading, deciding, and learning in private.

A Personal Prime Radiant tier fixes this:

- Each employee's laptop becomes a sensor (per the §1 Signals-layer framing) — articles read, decisions made in personal notes, meetings they attended that the department curator didn't
- Their per-person `audience:` frontmatter routes notes up to the right department instance(s)
- Cross-departmental meetings (e.g. an HR + IT-Ops 1:1) flow into both instances simultaneously
- The CEO instance, when it spins up, federates everything — the long-promised digital knowledge twin becomes mechanically buildable, not just architecturally described

The bet this supports: that **institutional knowledge is currently lost on every person's local machine** and that capturing it at the personal tier, sanitised, and federating up, is what makes the multi-instance Prime Radiant compound at organisation scale instead of stalling at the curator bottleneck.

## What's proposed

A new tier, below department, called **Personal Prime Radiant**:

- **Same schema as AIO CLAUDE.md v0.8**, with two additions:
  - `audience:` frontmatter required on every wiki page (values: `personal | department | departments:<a>,<b> | org | ceo-only`). Drives federation routing.
  - `captured_by:` frontmatter required on every wiki page (kebab-case person slug). Liability anchor; never strippable during sanitisation.
- **Folder structure identical to AIO** plus one extra: `sources/laptop/` for files captured from `$HOME` by the skill's walker.
- **Locked department vocabulary unchanged.** Personal instances cannot invent new departments. New entity creation remains high-stakes per AIO §5.1 — the skill escalates to `questions/ingest-*.md` instead of writing silently.
- **Federation always goes through the target's `inbox/`.** Never write directly to a department instance's wiki pages. This preserves the curator boundary — Michael (or Andrew, or any future curator) applies their own ingest discipline to inbound personal-tier contributions.
- **Privacy default = department** (per user preference 2026-05-11). The bootstrap biases toward dept-level sharing; only explicit personal markers (salary, performance, medical, legal) downgrade to `[personal]`.

## How federation works in practice

Example flows:

| Page in personal vault | `audience:` | `departments:` | Federates to |
|---|---|---|---|
| Notes from an AIO 1:1 with Jehad | `[department]` | `[ai-office]` | `AIO/inbox/personal-jehad-altoutou-<slug>.md` |
| Cross-dept meeting with HR + IT-Ops attendees | `[departments:hr,it-ops]` | `[hr, it-ops]` | HR `inbox/` AND IT-Ops `inbox/` |
| Article: [[anthropic|Anthropic]] Claude Skills GA | `[org]` | `[ai-office]` | AIO + every other dept instance + Org instance (when it exists) |
| Personal performance review | `[personal]` | `[]` | Nowhere — stays local |
| 1:1 with CEO about confidential strategy | `[ceo-only]` | `[]` | CEO instance only (when it exists) |

The personal instance never sees inside a department instance's wiki pages — federation is push-only, upward, via inbox.

## What gets ingested

The `/janus-brain` skill walks `$HOME` excluding hidden + Library, applies a five-layer privacy filter (see skill `references/privacy-filter.md`), classifies files, and queues each into the personal vault's `inbox/`. The ingest pass — parallel general-purpose subagents reading AIO §5.1 discipline — files sources into `sources/laptop/` and updates wiki pages low-stakes or escalates high-stakes.

Fireflies meetings pull nightly via per-user API key (per [[2026-05-04-centralised-fireflies-webhook-for-interviews]] adjacent decision — the personal tier uses each user's own Fireflies key, gated to meetings they attended). Recurring 1:1s and team standups are skipped by default — the [[standup]] skill owns those.

## Open questions for Michael

1. **Naming.** Should this be "Personal Prime Radiant · `<Person>`" (matches AIO precedent) or something narrower like "Prime Radiant — `<Person>` Personal"? Current skill uses `[[janus-prime-radiant|Janus Prime Radiant]] · <Person> (Personal)` — happy to align with whatever convention you set.

2. **Federation cadence.** Skill currently federates after every ingest pass (so nightly). Alternative: weekly batch federation so personal instances have time to settle before contributing. Trade-off: nightly is fresher, weekly gives the personal curator a chance to review/edit before federating.

3. **Escalation routing.** When a personal-tier ingest creates a high-stakes `questions/ingest-*.md` page, does it stay in the personal instance for the person to resolve, or also escalate to AIO/dept? Current default: stays personal. Alternative: cross-post to dept if `audience` is `department`+.

4. **Schema deviations.** The personal tier adds `audience:` and `captured_by:` as required. The AIO instance has `audience:` optional and no `captured_by:`. Do you want these promoted to AIO required for cross-tier consistency, or kept optional at department level?

5. **Roll-out gate.** Until you OK this, the skill operates in **personal-only mode** — no federation. Suggested gate: I run it on my own laptop for ~2 weeks, you review the personal vault output, then we decide whether to enable federation and roll to other employees.

## What I'm asking for

A decision (or a deferral with a `questions/` page) on whether to add Personal Prime Radiant as the per-employee tier under each department instance. Concrete deliverable already exists: the `/janus-brain` skill is installed in my Claude Desktop today, ready to scaffold a Personal PR for me. I'll run it on my own laptop in personal-only mode this week, hand you the vault to inspect, and we can decide from there whether to flip the federation switch.

The brief itself is the escalation per AIO §5.1 high-stakes discipline — a new tier in a curated program belongs in `questions/` or `briefs/`, not silently asserted.
