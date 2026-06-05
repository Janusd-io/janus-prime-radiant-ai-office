---
type: source
source_type: meeting
title: AIO Standup 5 Jun 2026
slug: 2026-06-05-aio-standup
created: 2026-06-05
updated: 2026-06-05
captured_by: jehad-altoutou
fireflies_id: 01KTB47JKRH6W4779155H1K4YN
fireflies_url: https://app.fireflies.ai/view/01KTB47JKRH6W4779155H1K4YN
attendees: [Michael Bruck, Jehad Altoutou]
duration_min: 57
audience: department
departments: [ai-office]
standup_skill_version: v3.24
parser_version: 3
related: [2928682913, 2956583393, 2969295918, 2969245116, 2969272627, 2969296209, 2969286293, 2969249413, AIR-35, AIR-107]
---

## Clean Meeting Summary

AIO standup on 5 June 2026 (~57 min). Bonaventure Wong's Prime Radiant is live and working — he queried "JLL strategy" and got useful results; he's now asking how to get more information in. Two formal decisions were taken: (1) **one-curator-per-group** is now policy — only the curator needs Obsidian, other users access via NanoClaw/Slack; (2) **cloud-based deployment** is the strategic direction — running on individual laptops is too complex to maintain at scale. The PM team (Lysander) Google Drive ingestion requires careful planning — Jehad to get read-only access first, clone the structure, study it before designing the ingest. Euclid handover confusion needs to be resolved today.

---

## 🎯 Today (5 June 2026)

- **Install latest Janus HTML presentation skill on Bonaventure's Cowork** (Jehad Altoutou): Bonaventure asked yesterday; Jehad doesn't have the latest version — get it from Andrew. | Monday: [2969295918](https://janusd-company.monday.com/boards/5095012849/pulses/2969295918)
- **Clarify AIO→IT handover criteria with Euclid** (Jehad Altoutou): HR is depending on the system. Euclid's team needs to define what they need for sign-off — not more from AIO. Michael: "Let's clarify today. I'm leaving in July." | Monday: [2969245116](https://janusd-company.monday.com/boards/5095012849/pulses/2969245116)

---

## 📅 This Week

- **Get read-only access to PM team Google Drive** (Jehad Altoutou): Ask Rosa or Lysander to share the PM Google Drive folder as view-only. Required before designing the ingestion pipeline. | Monday: [2969272627](https://janusd-company.monday.com/boards/5095012849/pulses/2969272627)
- **Clone PM spreadsheet + study Google Drive document structure** (Jehad Altoutou): Don't rush ingestion. Clone first, map structure and linkages, understand file types, then design. Preserve links to original source docs throughout. | Monday: [2969296209](https://janusd-company.monday.com/boards/5095012849/pulses/2969296209)
- **Document one-curator-per-group policy** (Michael Bruck + Jehad Altoutou): Draft the formal policy document + a one-page briefing for PM team (Lysander/Rosa/Euclid). Update CLAUDE.md with curator convention if not already there. | Monday: [2969286293](https://janusd-company.monday.com/boards/5095012849/pulses/2969286293)

---

## 🏔️ Horizon

- **Design Bonaventure calendar connector workflow** (Jehad Altoutou): When a calendar event is created → Prime Radiant auto-generates a briefing (background on attendees, objectives, talking points, optional presentation). | Monday: [2969249413](https://janusd-company.monday.com/boards/5095012849/pulses/2969249413)
- **PM team data ingestion** (Jehad Altoutou): After Google Drive access + structure study; run on Jehad's machine first, push to Lysander's GitHub when ready.
- **Cloud deployment architecture** (Both): Design the cloud-based infrastructure path — users via NanoClaw/Slack, curators only need Obsidian. Enables commercialisation at scale.

---

## Decisions Made

- **ONE CURATOR PER GROUP** (formal policy): Each Prime Radiant group has exactly one curator. Only the curator needs Obsidian. Other users access via NanoClaw/Slack. Backup curator allowed but cannot run simultaneously (race condition risk). Curator must be "rule-book fluent" — trained on CLAUDE.md.
- **Cloud-based deployment direction**: Running Obsidian on every employee's machine is too complex to maintain. Strategic direction: cloud-hosted system, users interface via Slack/NanoClaw. This also enables commercialisation.
- **PM Google Drive ingestion — go slow**: Clone + study structure first. Don't let Claude ingest before the linkage topology is understood.
- **Pre-approval consent technique**: For unattended Cowork ingestion runs, tell Claude: "You have my consent to do everything — don't ask for approval. If you ask, I'm not approving anything." Strict prompt required.
- **Bonaventure enrollment learnings filed**: Phone folder + OneDrive must be excluded from ingestion. Windows-specific lesson documented.

---

## Findings / Context

**Bonaventure enrollment working:** He queried "JLL strategy" and the system surfaced insights from prior meetings and research. He's now motivated to add more — wants to connect Slack, Monday.com (once Euclid gets accounts set up), and migrate chat history from Claude chat mode to Cowork.

**Lysander enrollment status:** Jehad can only see 1 meeting in the vault — enrollment may be incomplete. Needs investigation. He couldn't finish last session.

**Curator model rationale:** More than one curator → race conditions and file lock conflicts (Jehad + Michael have already experienced this). One curator per group eliminates this. Also simplifies cloud deployment since only the curator instance needs Obsidian. This is the same architectural discipline as having one primary in a leader-follower database setup.

**Asana → Monday:** Bonaventure asked to migrate Singapore Company-in-a-Box tracker from Asana to Monday.com. Asana (AIR-35) was a one-off for Singapore setup; Monday becomes the standard. Migration decision is Bonaventure's/IT's.

**Inbox shortcut for Bonaventure (Windows):** Jehad showed Bonaventure how to create a taskbar shortcut to the Inbox folder. He clipped a Singapore Business Times article about Anthropic's Singapore office — first real web clip.

---

## External / Other-Department Follow-ups

*(Excluded from Monday by AI Office Ownership Gate — Obsidian only)*

- **Assess Asana → Monday.com migration for Singapore project** — Owner: Bonaventure Wong + IT | `Monday: excluded by AI Office Ownership Gate`
- **Euclid/Rosa/Lysander read + adopt curator guidelines** — Owner: those individuals, once AIO documents the policy | `Monday: excluded by AI Office Ownership Gate`

---

## Registry Outcomes

| Tool | AIR # | Action |
|---|---|---|
| Asana | AIR-35 | Enriched — Bonaventure requested migration to Monday; migration decision pending Bonaventure/IT |
| Google Drive | AIR-107 | Enriched — PM team's primary doc repo; ingestion design approach decided (clone + study first) |

---

## Context Coverage (Step 3I)

- Items touched: 8 (2 source bumps + 6 creates)
- Description Updates: 8/8 ✓
- Step 3G creates: 6 | Step 3H backfills: 0 | Step 3E.1 moves: 0
- **Coverage: 100% PASS ✓**

---

## AI Office Ownership Gate

- Reviewed: 8 | Passed: 6 | Reframed: 0
- Excluded: 2 (Asana migration — Bonaventure/IT owns it; team reads curator guidelines — their work)
