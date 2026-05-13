---
type: source
notion_url: https://www.notion.so/357114fc090c817da4a1fe07c4c4dceb
notion_id: 357114fc-090c-817d-a4a1-fe07c4c4dceb
title: Bonaventure — Discussion & Task Tracker
source_type: notion-page
fetched: 2026-05-06
---

# Bonaventure — Discussion & Task Tracker

Persistent log of meetings with **Bonaventure Wong** (CEO sponsor of AI Office programme). Each meeting follows standup format — clean summary, time-bucketed next steps, decisions, findings, Monday hyperlinks, Linear/AIR reconciliation.

## Latest: Bonaventure / Michael / Jehad / Andrew Meeting — 4 May 2026

**Attendees:** Michael Bruck, Bonaventure Wong, Jehad Altoutou
**Duration:** 1h 13m
**Source:** Fireflies

### Summary highlights

- **Designed AI tool evaluation pipeline end-to-end:** Slack intake → Claude triage agent → human review → policy gates → sandbox → IT hand-off. Bonaventure validating each stage.
- **Slack intake form locked:** URL, submitter name, timestamp, location, organisation. No approval gate at submission — friction-free entry.
- **Linear AIR confirmed as system of record** for AI Tools Registry — *"that's why we update Linear and everything; it becomes part of the knowledge base, it's compounded knowledge."*
- **AI-policy gate is binary 4-of-4** (data training, Google integration, security, etc.). Failing any = reject. Rejection records reason + approver name.
- **Standup skill is orchestrator,** dispatching sub-skills (`/ai-registry`, `/ai-tool-evaluation`). Confidence-scoring rubric endorsed (≥90% silent / 60–80% confirm / <60% ask).
- **Long-term vision:** company-wide digital twin, role-based compartmentalisation, eventually external-facing.
- **Cowork in active use but NOT YET FORMALLY APPROVED** — flagged by Jehad; Bonaventure acknowledged.

### Key decisions

- Slack intake form fields and friction-free submission (no approval gate at submission).
- Linear AIR is SoR for AI Tools Registry.
- AI-policy gate is binary 4-of-4; rejection records reason + approver.
- Standup skill as central orchestrator dispatching sub-skills.
- Bonaventure agreed to be next test case for applying standup methodology to non-AI-Office workstream.

### Key findings

- No auto-categoriser exists for AI tools — comparables search blocked. Hercules vs Lovable/Replit/Claude Design/Stitch exposed the gap.
- Fireflies summary explicitly distrusted as primary signal — *"crap"*, "out of context"; raw transcript is canonical.
- Sandbox scoring rubric needs refinement; IT hand-off template doesn't exist yet.

### Items created

- **Office of CEO group** on Monday board 5095012818.
- Several high-priority Monday items: Apply standup-skill to Bonaventure's workstream, Cowork formal approval, Define IT hand-off template, Build categorisation taxonomy.

## Earlier: Bonaventure Reframe Meeting — 20 Apr 2026

Full analysis on separate child page. Key outcome: **ISO-driven workflow foundation becomes primary deliverable**, not CEO weekly meeting. Task-based, bottom-up rollup. Simon is critical path.

---

## How to maintain

For each new Bonaventure meeting:
1. Add new `## <title> — DD Mon YYYY` section at top (newest first).
2. Use standup template: Attendees, Source, Summary, 🎯 / 📅 / 🏔️ next steps (with Monday hyperlinks), Decisions, Findings, Monday items, Linear AIP reconciliation, AIR / evaluation outcomes.
3. Tasks → **Office of CEO** group on board 5095012818.
4. Older entries fade into one-line cross-references with links to canonical Fireflies recording.
