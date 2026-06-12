---
type: source
source_type: meeting
title: AIO Project Management Meeting 11 Jun 2026
slug: 2026-06-11-aio-project-management-meeting
created: 2026-06-11
captured_by: jehad-altoutou
fireflies_id: 01KTVAV9A7YDBK0K1QTQ9GQ1F1
fireflies_url: https://app.fireflies.ai/view/01KTVAV9A7YDBK0K1QTQ9GQ1F1
attendees: [Michael Bruck, Lysander Liu, Rosa Wu, Euclid Wong, Jehad Altoutou]
duration_min: 57
audience: department
departments: [ai-office]
standup_skill_version: v3.24
parser_version: 3
related: [2924305391, 2990749244, 2990747445, 2990758821, AIR-10, AIR-74]
---

## Clean Meeting Summary

The AI Office met with the Project Management team leads (Lysander, Rosa, Euclid) to kick off the PM-team Prime Radiant instance for delivery knowledge. The group decided to rebuild the knowledge base from the PM team's audited Google Drive documents rather than migrating Lysander's legacy Obsidian vault, whose content is two to three months stale. An empty skeleton structure was generated live during the session (running on Fable 5, Anthropic's newly released model); content lands once Lysander delivers his organised documents folder early next week. Scope was settled as delivery knowledge plus pre-sales documents, with product/solutions work explicitly excluded. Onboarding proceeds one person at a time — Lysander first, then Rosa and Spike once stable.

## 🎯 Next steps — by next standup

- **Transfer Prime Radiant setup to new laptop and sync Obsidian vault** — Owner: Jehad — due 15 Jun 2026 — [Monday sub-item](https://janusd-company.monday.com/boards/5095012849/pulses/2990749244)

## 📅 Next steps — this week

- **Lysander to organise and deliver the structured Google Drive documents folder** — Owner: Lysander Liu (PM team) — due Mon/Tue 15–16 Jun 2026 — Monday: excluded by AI Office Ownership Gate
- **Resume PM instance implementation in person; process the folder into the skeleton once received** — Owner: Jehad (with Michael) — next week — tracked on [parent item](https://janusd-company.monday.com/boards/5095012818/pulses/2924305391) (covered by existing sub-item "Upload Project Management team documents to Prime Radiant inbox folder", 2915304680 — approach superseded per this meeting's Update post)

## 🏔️ Next steps — longer horizon

- **Enable Anthropic APIs and finalise Fable 5 subscription setup** — Owner: Jehad — due by July 2026 — [Monday sub-item](https://janusd-company.monday.com/boards/5095012849/pulses/2990747445)
- **Connect Monday MCP and meeting-transcript ingest to PM Prime Radiant instance** — Owner: Jehad — post-initial phase, due ~26 Jun 2026 — [Monday sub-item](https://janusd-company.monday.com/boards/5095012849/pulses/2990758821)
- **Onboard Rosa and Spike once the instance is stable** — Owner: Jehad/Michael — covered by the [parent item](https://janusd-company.monday.com/boards/5095012818/pulses/2924305391) scope

## Decisions made

- Rebuild the PM delivery knowledge base from audited Google Drive documents; do not migrate Lysander's legacy Obsidian vault (stale, partially wrong content). Skeleton stays empty until the folder arrives.
- Scope: delivery knowledge only. Product design/coding is separate (future group; CTO scope under discussion is infrastructure/DevOps, not development). Pre-sales documents are included — the group agreed they are delivery-related.
- Adopt Fable 5 (Anthropic) for Prime Radiant / Cowork work; covered by subscription until July, then enable APIs.
- Onboarding sequence: one at a time — Lysander (curator) first, then Rosa and Spike.
- Per-person log attribution adopted in the enrolment (each contributor's additions identified, replacing the single shared log) — raised by Jehad, agreed.

## Findings / context

- Lysander's concern driving the rebuild decision: his old vault mixes outdated entries and non-delivery material (e.g. Synapse-system notes), risking wrong outcomes if ingested wholesale.
- Live skeleton build on Fable 5 surfaced field-vocabulary mismatches and date-format conflicts (Chinese-style YYYY-MM-DD) during categorisation — expected, handled by the rulebook.
- The PM team's audited Google Drive corpus is ~285 files — manageable size for a clean implementation pass.
- Jehad's laptop migration is a near-term dependency (security setup on the new machine; vault re-sync over the weekend).
- Workflow positioning restated for the PM team: Obsidian = index layer, markdown on disk = data, Claude Cowork + CLAUDE.md = intelligence/navigation; no RAG / vector DB needed; Fireflies summaries ignored in favour of raw transcripts.

## Monday items touched

- [PM team onboarding to Prime Radiant (Lysander / Spike / Rosa)](https://janusd-company.monday.com/boards/5095012818/pulses/2924305391) — source bump, decisions Update, next-step stub
- [Transfer Prime Radiant setup to Jehad's new laptop and sync Obsidian vault](https://janusd-company.monday.com/boards/5095012849/pulses/2990749244) — created
- [Enable Anthropic APIs and finalise Fable 5 subscription setup](https://janusd-company.monday.com/boards/5095012849/pulses/2990747445) — created
- [Connect Monday MCP and meeting-transcript ingest to PM Prime Radiant instance](https://janusd-company.monday.com/boards/5095012849/pulses/2990758821) — created

Coverage: ✅ 4 items, ⚠️ 0 backfilled, ➡️ 0 move-rationales, ❌ 0 coverage failures

## External / Other-Department Follow-ups

- **Organise and deliver structured Google Drive documents folder for the PM Prime Radiant rebuild** — Owner: Lysander Liu (PM team) — due Mon/Tue 15–16 Jun 2026 — Monday: excluded by AI Office Ownership Gate

## Linear AIP reconciliation

No AIP status changes authorised by the transcript — none applied.

## AI Registry / Tool Evaluation outcomes

- **AIR-10 Claude** — enriched: Fable 5 adoption for Prime Radiant/Cowork (decided this meeting); July 2026 subscription boundary + post-July API cost question added; status unchanged (Production). No Gate chain.
- **AIR-74 Obsidian** — enriched: PM/delivery-team instance adoption expansion, rebuild-from-Drive approach, onboarding sequence; status unchanged (Sandbox). No Gate chain.
- Skipped (registered, no new information): Fireflies (AIR-9), Google Drive (AIR-107), Monday.com (AIR-83), GitHub (AIR-109).
- Not registered (user decision): "Synapse" — Lysander's system, zero-context market/internal reference; revisit if it resurfaces with operational context.
