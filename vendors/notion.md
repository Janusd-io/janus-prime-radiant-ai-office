---
type: vendor
title: Notion
slug: notion
created: 2026-05-06
updated: 2026-06-09
departments: [ai-office, it-ops, office-of-ceo]
status: deprecating
confidence: high
sources: [2026-05-13-aio-it-meeting, 2026-05-18-ai-native-ceo]
related: [michael-bruck, janus-prime-radiant-build, 2026-05-11-notion-restricted-to-aio-no-broad-rollout]
migrated_from: entities/vendors/notion.md
---
# Notion

Workspace, wiki, and docs platform. At Janus, primary use was the **Operations Notebook** — the forward-looking journal / reporting surface for AIO operations.

## Deprecation (as of 2026-05-13, reconfirmed 2026-05-18)

**Notion deprecation target: end of May 2026.** Confirmed in [[2026-05-13-aio-it-meeting]]. Reconfirmed by Bonaventure Wong in the [[2026-05-18-ai-native-ceo|18 May 2026 CEO meeting]] — "one fewer tool in the stack." The transition path is dual-write: the `/standup` skill (v3.15+) writes standup logs both to Notion (legacy) and to the Prime Radiant vault inbox via MCP connector (Step 5G). After end of May, Notion-side writes stop and Prime Radiant becomes the sole journal surface. This aligns with [[2026-05-11-notion-restricted-to-aio-no-broad-rollout|Bonaventure's no-broad-Notion-rollout decision]] and the [[janus-prime-radiant-build]] program direction.

## Scope at Janus (historical)

The Operations Notebook is where the `/standup` skill writes daily standup logs (`## AIO DD Mon YYYY` entries) consolidating decisions, next-step planning, and registry/evaluation outcomes from each day. Beyond the standup journal, Notion also hosts project documentation tied to active Monday projects and ad-hoc internal documentation.

## Relationship to this wiki

Notion was authoritative for the daily operations narrative — what was discussed, what was decided, what's queued next. This wiki ingests Notion pages selectively, focused on the standup-log entries which are the densest carrier of decisions and rationale. Per `CLAUDE.md` §5.1.

The wiki is the **synthesis layer over Notion**, not a replacement for it — until end of May 2026, when Prime Radiant absorbs the journal role and Notion exits the operational stack.

---

## Operational notes — Notion Operations Notebook

_Migrated from the personal-vault 'AI Office Brain' base, 2026-06-09._

# Notion — AI Office Operations Notebook

Page ID: `335114fc-090c-8191-9a6e-cd2f2cacc64a`
URL: https://www.notion.so/335114fc090c81919a6ecd2f2cacc64a

The chronological journal for the AI Office. Standup logs, decisions, key findings, time-bucketed next steps. **Written by [[standup]]** (Step 5).

## Structure (post-cleanup, 4 May 2026)

```
# Purpose
  ↳ Sources of truth table
  ↳ Format conventions (## AIO DD Mon YYYY)
  ↳ Cleanup note (4 May 2026)

## Compact archive — pre-30 Apr standups
  ↳ 20 dated bullets (2026-04-01 → 2026-04-28)
  ↳ Full content of each entry lives in Fireflies transcripts only

## AIO 1 May 2026
  ↳ Clean meeting summary
  ↳ 🎯 / 📅 / 🏔️ next steps
  ↳ Decisions / Findings / Items touched / AIP reconciliation / Outcomes

## AIO 4 May 2026
  ↳ same structure

[Child page references — preserved]
  ↳ Completed Action Items — Archive (deprecated)
  ↳ SOR Tooling Analysis (Notion vs Monday)
  ↳ Simon Meeting — ISO Programme Discovery
  ↳ Bonaventure Meeting — Reframe Analysis
  ↳ Weekly Status (20-24 Apr 2026)
  ↳ Vibe-Coding & Vibe-Design Bakeoff
```

## Standup entry template (mandatory, v3.8.1+)

```markdown
## AIO DD Mon YYYY

**Attendees:** Michael Bruck, Jehad Altoutou
**Source transcript:** [Fireflies — AIO DD Mon](URL)

---

### Clean meeting summary
- (5–7 bullets max — high-signal only, no transcript quotes, no fluff)

---

### 🎯 Next steps — by next standup
- [ ] [Monday — <task>](URL) — <Verb + object + context> — Owner: <name> — Due: <date>

### 📅 This week
- [ ] ...

### 🏔️ Longer horizon
- [ ] ...

---

### Decisions made
- ...

### Key findings / discussions
- ...

### Monday items touched
- ✏️ updated / ➕ created / 🧬 sub-item added / 💬 update posted

### Linear AIP reconciliation
- AIP-N: <old> → <new> (rationale)
- Or: "No mismatches detected."

### AI Registry / Tool Evaluation Outcomes
- [ai-registry] AIR-N <tool> — <action completed> — Result: <status>
- [ai-tool-evaluation] AIR-N <tool> — Gate <N> — Result: <pass/fail/needs more>
```

## Size hygiene (v3.9)

[[standup]] keeps this page bounded:

| Threshold | Behaviour |
|---|---|
| <60KB | Healthy |
| 60–80KB | Warn; queue archival |
| >80KB | Mandatory archival before append |
| >100KB | Block live append; fall back to outputs file |

**Retention window:** default 14 days of full content on this page. Older entries auto-archive to monthly `Standup Log Archive — <Month YYYY>` child pages with one-line summaries replacing them on the master page.

The 4 May 2026 cleanup was a manual one-shot (page was 106KB). Going forward, archival is automatic per [[standup]] Step 5F.

## What does NOT live here (v3.7+ source-of-truth boundaries)

- Active action item tables (🟡 In Progress / 🟢 Open / ⏸️ Parked) — **migrated to [[monday]]**, removed from this page on 4 May 2026
- AI tool registry entries — live on [[ai-registry]]
- Recruitment / leave dashboard items — live on [[monday]]
- Daily standup transcripts — live on [[fireflies]]

This page is journal-only. Forward-looking. Decisions and next-step plans only.

## Read-vs-write

- **[[standup]]** writes (Step 5 each run; Step 5F archival when triggered)
- Anyone reads (it's leadership-readable by design)

## Related

- Skill: [[standup]] (Step 5)
- Backup: `outputs/notion-operations-notebook-backup-2026-05-04.md` (durable pre-cleanup snapshot)
- Source transcripts: [[fireflies]]
