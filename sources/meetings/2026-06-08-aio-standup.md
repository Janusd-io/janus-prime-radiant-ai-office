---
type: source
source_type: meeting
title: AIO Standup 8 Jun 2026
slug: 2026-06-08-aio-standup
created: 2026-06-08
updated: 2026-06-08
captured_by: jehad-altoutou
fireflies_id: 01KTK2EQ50XXCMBDZRTT6VF4VS
fireflies_url: https://app.fireflies.ai/view/01KTK2EQ50XXCMBDZRTT6VF4VS
attendees: [Michael Bruck, Jehad Altoutou]
duration_min: 46
audience: department
departments: [ai-office]
standup_skill_version: v3.24
parser_version: 3
related: [2900825519, 2924305391, 2976646988, 2976654431, 2976650207, 2976640743, 2976661503, 2976663263, 2976661357, graphify, letter, fireflies, openai-codex, google-gemini, obsidian]
---

# AIO Standup — 8 Jun 2026

46-minute standup. Attendees: Michael Bruck, Jehad Altoutou. Source: [Fireflies](https://app.fireflies.ai/view/01KTK2EQ50XXCMBDZRTT6VF4VS).

---

## Clean Meeting Summary

The standup covered five main threads: (1) Bonaventure enrollment status and a discovered gap, (2) Prime Radiant vault housekeeping, (3) tooling investigation (Gemini Agent SDK, Letter), (4) non-technical harness design for company-wide rollout, and (5) PM team onboarding progress.

**Bonaventure enrollment.** Running autonomously on a 7-day rolling window. ~2,500 files reduced to ~1,700 after dedup. The discovery: [[graphify]] — a file-tree-to-Obsidian knowledge graph tool Jehad uses on his personal laptop — was not included in the enrollment setup. This is a gap; Jehad to add it.

**Prime Radiant vault housekeeping.** Two items surfaced. First, [[CLAUDE.md]] still references Notion as an active output surface despite Notion being retired from the standup pipeline as of v3.21 (2026-05-21). Jehad to add a deprecation notice and fix version ordering. Second, launchd plist and Xcode artefacts have accumulated in the vault directory and are being tracked by git. Jehad to remove and update .gitignore.

**Tooling investigations.** Michael is investigating two tools: (1) Google [[gemini]] Agent SDK for local agent orchestration — the question is whether it complements or replaces the current Claude Cowork + Claude CLI approach, particularly for the non-technical harness; (2) [[letter]] — a coding harness with interesting agent memory patterns. Both are now in Linear AIR (AIR-5 enriched; AIR-153 created).

**Non-technical harness.** The company-wide Prime Radiant rollout requires a simplified interface for staff (e.g., Emma, Marianne) who cannot use Claude Cowork or Code directly. The loop is: meeting → ingest → Monday + wiki, but the interface must be abstracted. A Slack-based NanoClaude interface is the likely pattern. Jehad + Michael own the design. Scheduling mechanisms discussed: Cowork scheduled tasks and Claude CLI (launchd on Mac) are the recommended approaches over Windows Task Scheduler.

**PM team onboarding.** Lysander is curator for the PM team instance (Lysander + Euclid + Rosa). Phase 1 enrollment nearly complete. Phase 2: (1) get PM team onto Monday Standard plan — Standard is required (has automations, integrations, timeline/Gantt, calendar views that Basic lacks; minimum 5 seats); (2) study the PM team Google Drive before ingestion begins. Euclid needs Monday Standard admin rights. Both Phase 2 session and Monday Standard setup are now tracked as sub-items on [[2924305391]].

---

## Decisions

- Graphify to be added to Bonaventure Prime Radiant enrollment (Jehad, this week).
- CLAUDE.md: add Notion deprecation notice + fix version ordering (Jehad, this week).
- Vault launchd/Xcode artefacts: remove and update .gitignore (Jehad, this week).
- Gemini Agent SDK investigation for local orchestration use case assigned to Jehad.
- Non-technical harness/wrap design: owned by Jehad + Michael, scoped against company-wide rollout.
- PM team Phase 2: book session with Lysander for Monday Standard + Google Drive study.
- Euclid/Venture team: AIO to set up Monday Standard with admin rights for Euclid.

---

## Next Steps

### Today / This Week
- [ ] Implement Graphify in Bonaventure Prime Radiant enrollment → [[2976646988]]
- [ ] Update CLAUDE.md — deprecate Notion references, fix version ordering → [[2976654431]]
- [ ] Clean up launchd plist and Xcode artefacts from vault → [[2976650207]]
- [ ] Investigate Gemini Agent SDK for local agent orchestration → [[2976640743]]
- [ ] Design non-technical harness for company-wide Prime Radiant rollout → [[2976661503]]
- [ ] Conduct Phase 2 session with Lysander — Monday Standard + Google Drive study → [[2976663263]]
- [ ] Set up Monday Standard for Euclid / Venture team — admin rights → [[2976661357]]

### Later / Carry-forward
- `[[prime-radiant-instance-setup]]` addendum: add "identify curator" as step 1 of any new-instance bootstrap.
- Obsidian Git auto-sync on Jehad's machine should be disabled (set interval to 0 — only Michael's machine should auto-commit).
- Principle 10 "Framer Stays in the Room" — singapore-monitoring-frame-audit overdue.
- File `questions/per-user-jpr-dashboard-design.md` when ready.

---

## Registry / Evaluation Outcomes

| Tool | AIR Issue | Action | Outcome |
|---|---|---|---|
| Graphify | AIR-154 | CREATED | Backlog. Gate 1 chained → **FAIL** (product identity discrepancy: public Graphify ≠ Jehad's tool). Needs Jehad to confirm which product. |
| Letter | AIR-153 | CREATED | Backlog. Gate 1 chained → **BLOCKED** (no public product matching description found). Needs Michael to share source URL. |
| Fireflies.ai | AIR-9 | ENRICHED | Transcript-to-SaaS integration capability finding added. Native integrations mature but custom pipeline still preferred. |
| OpenAI Codex | AIR-84 | ENRICHED | Claude-first workflow finding added. Codex less relevant to AIO's agentic pipeline; Technology evaluation continues. |
| Google Gemini | AIR-5 | ENRICHED | Local agent orchestration use case investigation added. Monday follow-up item 2976640743 referenced. |
| Obsidian | AIR-74 | ENRICHED | Obsidian Sync vs GitHub substrate trade-off finding added. Prospective, no decision. |

---

## Monday Writes Summary

**Parent items source-bumped (Step 3A):**
- [2900825519](https://janusd-company.monday.com/boards/5095012818/pulses/2900825519) Prime Radiant — company-wide knowledge graph + digital twin
- [2924305391](https://janusd-company.monday.com/boards/5095012818/pulses/2924305391) PM team onboarding to Prime Radiant (Lysander / Spike / Rosa)

**Step 3H backfills:** 0 (both parents already had Description headers).

**Sub-items created (Step 3B, 7 items):**

Under 2900825519:
- [2976646988](https://janusd-company.monday.com/boards/5095012849/pulses/2976646988) Implement Graphify in Bonaventure Prime Radiant enrollment — Jehad
- [2976654431](https://janusd-company.monday.com/boards/5095012849/pulses/2976654431) Update CLAUDE.md — deprecate Notion references and fix version ordering — Jehad
- [2976650207](https://janusd-company.monday.com/boards/5095012849/pulses/2976650207) Clean up launchd plist and Xcode artefacts from vault — Jehad
- [2976640743](https://janusd-company.monday.com/boards/5095012849/pulses/2976640743) Investigate Gemini Agent SDK for local agent orchestration — Jehad
- [2976661503](https://janusd-company.monday.com/boards/5095012849/pulses/2976661503) Design non-technical harness for company-wide Prime Radiant rollout — Jehad + Michael

Under 2924305391:
- [2976663263](https://janusd-company.monday.com/boards/5095012849/pulses/2976663263) Conduct Phase 2 session with Lysander — Monday Standard setup and Google Drive study plan — Jehad + Michael
- [2976661357](https://janusd-company.monday.com/boards/5095012849/pulses/2976661357) Set up Monday Standard for Euclid and Venture team — admin rights and onboarding — Jehad + Michael

**Context Coverage Invariant (Step 3I):** PASS — 9/9 touched items have Description Updates.

---

## External / Other-Department Follow-ups

*(Not AIO-owned; captured for record only — no Monday items created.)*

- **HR / Ops:** Emma and Marianne identified as target users for non-technical Prime Radiant harness. No action for AIO yet beyond harness design.
- **Venture / Euclid team:** Need to self-onboard to Monday Standard once AIO completes the setup — their onboarding steps are their own responsibility post-setup.
