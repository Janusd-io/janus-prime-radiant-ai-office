---
type: source
source_type: meeting
title: AIO Standup 18 May 2026
slug: 2026-05-18-aio-standup
created: 2026-05-18
captured_by: jehad-altoutou
fireflies_id: 01KRA6FQZ2WEX5WJ3EX1W3E3G8
fireflies_url: https://app.fireflies.ai/view/AI-Native-CEO-c93c0577-2cb3
attendees: [Jehad Altoutou, Bonaventure Wong, Joyce Woo]
duration_min: 58
audience: department
departments: [ai-office]
standup_skill_version: v3.21
parser_version: 3
related: [2891609467, 2917841885, 2882088507, 2900825519, 2917860605, 2882088496, 2889202957, 2917860539, 2924305391, 2889155963, AIR-103, AIR-100, AIR-104, AIP-16, AIP-4, AIP-5]
---

# AIO Standup — 18 May 2026
**Meeting:** AI Native - CEO | 12:00 PM | ~58 min
**Attendees:** Jehad Altoutou, Bonaventure Wong (CEO), Joyce Woo (Singapore)
**Recorded:** Fireflies `01KRA6FQZ2WEX5WJ3EX1W3E3G8`

---

## Clean Meeting Summary

Today's CEO-level session covered four active workstreams and produced several important architectural and operational decisions.

**Platform architecture** — The Prime Radiant infrastructure (Obsidian + GitHub) was presented to Bonaventure and introduced to Joyce. The core decision: department-first rollout is the right approach; individual Prime Radiants are on hold until several departments are live and working well. Singapore is to be treated as a department-level function (solid line to global), not a standalone entity. The knowledge base architecture will be one big centralised repository with open access — no per-market siloing. How the user interface adapts context to a given market is separate from the data structure. A technical limitation was discovered: Obsidian can only connect to one GitHub repo per instance, which blocks multi-KB interconnection. This is deferred until a solution is engineered.

**Marketing / Andrew onboarding** — Andrew is fully set up (Obsidian installed, templates ready). The bulk import will happen today or tomorrow: all Fireflies meetings from previous sessions with Andrew + all markdown documents he has pre-saved. This gives his Prime Radiant a strong kickstart. In parallel, when the team plugged the existing static HTML website into Claude Code to add a Singapore landing page, they discovered it could do a full TypeScript/React redesign. Bonaventure approved proceeding with the full rebuild — MailChimp integration for Singapore lead capture + GDPR privacy popup are included in scope.

**Project Management discovery** — A meeting was held with Lysander, Spike, and Rosa. It was conducted in Chinese; the AI transcript was processed into a summary presentation and sent back to them for review. Lysander responded positively. Target: PM team live on their own Prime Radiant by next week (w/c 25 May). Key insight: stop over-architecting upfront; let the system learn as data comes in.

**ISO skill (Joyce)** — Almost finished. Joyce has sent the process outputs to Simon for review. Skill architecture: interactive Q&A that collects what process the user wants to create + data sources, then LLM generates the process. Blocked on Simon's confirmation. Once confirmed → deploy to everyone.

**Notion deprecation** — Explicit decision: stop using Notion. "Feed it straight into the prime radiant — Notion becomes redundant. It's one less tool to worry about." Prime Radiant (Obsidian + GitHub) is now the sole knowledge and meeting-output surface. Standup skill v3.21 deployed today reflects this: Notion removed entirely, Step 5 writes directly to `sources/meetings/`.

**Slack bot sprawl** — Bonaventure flagged that multiple Slack bots (Finance/Airwallex, HR, etc.) are overwhelming him and he's turning notifications off. The agreed vision: one chief-of-staff bot per person in their own dedicated Slack channel. nano Claude / NanoClaw (modelled after OpenClaude) was mentioned as a candidate architecture — smaller, more secure, tailored to Janus's needs. Bot sprawl is a short-term problem on the path to the consolidated architecture.

**Naming/branding** — "Prime Radiant" is acknowledged as geeky. Decision: let Andrew propose internal branding for the knowledge system. Guidance from Bonaventure: go back to the origin of what we're building and drive from there. Drop the "Janus" prefix.

**Joyce Prime Radiant setup** — Agreed to schedule a dedicated meeting to onboard Joyce to Obsidian/Prime Radiant. She's working solo in Singapore — different input source profile from Dubai standups. Singapore's knowledge should connect to global.

---

## Decisions

| # | Decision | Owner |
|---|----------|-------|
| 1 | **Notion deprecated** — all meeting output goes into Prime Radiant | Jehad + Bonaventure |
| 2 | **Department-first KB rollout** — individual Prime Radiants on hold | Jehad |
| 3 | **Singapore = department-level function** | Bonaventure |
| 4 | **One big centralised KB, open access** — no per-market siloing | Jehad + Bonaventure |
| 5 | **Website: full TypeScript/React rebuild** + MailChimp + GDPR popup | Jehad |
| 6 | **Joyce to get Prime Radiant setup** — separate meeting | Jehad |

---

## Next Steps — Time-bucketed

### TODAY / TOMORROW
- [ ] Andrew bulk import: load all Fireflies meetings + pre-saved markdown docs into his Prime Radiant (Monday sub-item `2924305246`)
- [ ] Begin full TypeScript/React website rebuild (Monday item `2917841885`)

### THIS WEEK
- [ ] Schedule dedicated Prime Radiant onboarding session for Joyce (Monday sub-item `2924307111`)
- [ ] ISO skill: await Simon confirmation — deploy to everyone once confirmed (Monday item `2889155963`)
- [ ] MailChimp AIR evaluation — AIR-100 is Backlog/Low priority, raise if Singapore campaign timeline demands it
- [ ] nano Claude / NanoClaw — Gate 1 evaluation underway (AIR-103, Evaluating)

### NEXT WEEK (w/c 25 May)
- [ ] PM team (Lysander/Spike/Rosa) live on Prime Radiant (Monday item `2924305391`)
- [ ] Andrew proposes internal branding for knowledge system (Monday sub-item `2924309863`)

### DEFERRED
- [ ] Obsidian single-GitHub-repo limitation — engineering solution for multi-KB interconnection
- [ ] Individual Prime Radiants (on hold until dept-level solid)
- [ ] Chief-of-staff bot consolidated architecture (depends on nano Claude / NanoClaw AIR Gate evaluation)

---

## Open Questions

- How do we build connective tissue between department KBs once they're all live? (Folders hierarchy? Tags? Federation?)
- Should daily standups be adopted by other departments (Sales, Training)? Bonaventure is not convinced for all contexts — valuable for AI Office (siloed workers), less so for front-office teams who already have meetings and calendars.
- When the revenue model platform is live, will it drive natural knowledge-capture behaviour? (Bonaventure thinks yes.)
- How do we capture knowledge from solo/remote workers like Joyce who don't have a standup partner?

---

## Blockers

| Blocker | Affects | Status |
|---------|---------|--------|
| Simon confirmation pending | ISO skill deploy | Active |
| Obsidian single-repo limitation | Multi-KB interconnection | Deferred |
| WeWork UAE↔Singapore WiFi degraded | Standup quality | Ongoing |

---

## AI Registry / Tool Mentions

| Tool | AIR Status | Action Taken |
|------|-----------|--------------|
| nano Claude / NanoClaw | AIR-103, Evaluating | Comment added with bot architecture context |
| Mailchimp | AIR-100, Backlog/Low | Found — no change, priority review recommended |
| Airwallex | AIR-104, Backlog/Medium | New entry created — bot-sprawl context captured |

---

## Linear AIP Notes

| Issue | Title | Action |
|-------|-------|--------|
| AIP-16 | Town Hall Transcript Processing | Comment: Notion deprecation affects output surface |
| AIP-4 | AI Internal Hub Bot | Comment: bot consolidation vision, nano Claude candidate |
| AIP-5 | Janus Spec | Comment: Prime Radiant architecture confirmed, Notion deprecated |

---

## Context Coverage (Monday)

13 items touched | 10/10 parent items have Description Updates | 4 sub-items created | 1 status change (Notion → Deprecated)
