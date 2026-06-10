---
type: source
source_type: meeting
title: AIO Standup 9 Jun 2026
slug: 2026-06-09-aio-standup
created: 2026-06-09
updated: 2026-06-09
captured_by: jehad-altoutou
fireflies_id: 01KTNDS2DWB0H1KZ30RZWDYGDG
fireflies_url: https://app.fireflies.ai/view/01KTNDS2DWB0H1KZ30RZWDYGDG
attendees: [Michael Bruck, Jehad Altoutou]
duration_min: 53
audience: department
departments: [ai-office]
standup_skill_version: v3.24
parser_version: 3
related: [2939688504, 2882205554, 2978750463, 2978784424, 2978814400, 2978814295, 2882206287, AIR-159, AIR-77, AIR-93, AIR-76]
---

# AIO Standup — 9 Jun 2026

53-minute standup. Attendees: Michael Bruck, Jehad Altoutou. Source: [Fireflies](https://app.fireflies.ai/view/01KTNDS2DWB0H1KZ30RZWDYGDG).

---

## Clean Meeting Summary

The standup ran along two main threads plus several housekeeping items. First, Michael and Jehad reviewed the revised **AI Software Engineer job description** — reworked through Prime Radiant from Bonaventure's original draft — and agreed a final set of changes before it goes to Bonaventure for sign-off. Second, on opening the Monday board they recognised it has **drifted**: orphaned and aging tasks, deeply nested subtasks, and items actually owned by other departments (IT, ISO) filed under the AI Office. They agreed to reorganise the board into clean per-department dashboards, using Michael's HR dashboard as the template, before loading the rest of the company. Alongside: Twenty (20) open-source CRM was auto-added to Linear AIR (AIR-159) and is being studied; adding Bonaventure to Monday with pre-meeting query access; and getting AI to surface a post-standup status/blocker digest. One blocker was noted — Nomi taken down by IT — flagged explicitly as an Obsidian/wiki item rather than a task.

---

## Decisions

- **AI Software Engineer JD** — take one more revision turn, then route via Marianne to Bonaventure for sign-off. Agreed changes: lead with memory & knowledge systems (no RAG/vector-DB framing); emphasise microservices / modular composable architecture and squad-style ownership; add team collaboration (not a solo role); **remove Terraform** as a requirement (CTO-owned infra — familiarity only); keep Kubernetes, Docker, AWS + GCP; reframe as a full-stack AI software engineer with shipped-in-volume systems-architecture experience.
- **Role is full-stack** — the team is too small to split backend/front-end into separate hires.
- **Tool registry/evaluation work stays with Michael** — self-contained, not enough work to need extra resources.
- **Clean up the AI Office Monday board before loading the rest of the company** — reorganise into per-department dashboards using the HR dashboard as the template; create Training and PM/PMO groupings.
- **Twenty (20) CRM Stage-2 criteria** — data-training exclusion and Slack integration both judged non-blockers (open-source/self-hosted, own LLMs); evaluation to proceed alongside Andrew.
- **Keep the product team meeting at its slot** — Anne and Salesforce can be moved if scheduling gets tight.

---

## Next Steps

### Today / This Week
- [ ] Revise AI Software Engineer JD per 9 Jun feedback and route to Bonaventure for sign-off — Jehad → tracked on [[2939688504]] (existing sub-items "Draft job description…" and "Revise AIO engineering hire profile…")
- [ ] Prepare department names, IDs & assignments for Monday reorganisation — Michael → [[2978814400]]
- [ ] Begin AI Office Monday board reorganisation into per-department dashboards — Michael + Jehad → [[2978750463]]
- [ ] Review Simon's tool evaluation template and share with Michael — Jehad → tracked on existing sub-item [[2924562376]] ("Review Simon's process docs — tool eval framework…")

### Longer Horizon
- [ ] Add Bonaventure to Monday + pre-meeting status query — resolve .io vs .com and access level — Michael → [[2978814295]]
- [ ] Build AI-assisted post-standup Monday status & blocker digest — Jehad → [[2978784424]]
- [ ] Discuss IT hand-off template at tomorrow's IT meeting → existing item [[2891603501]]
- [ ] Publish the memory-system Substack/LinkedIn article (thought-leadership) — Jehad *(not Monday-tracked; confirm if it should be)*

---

## Registry / Evaluation Outcomes

| Tool | AIR Issue | Action | Outcome |
|---|---|---|---|
| Twenty (20 CRM) | AIR-159 | ENRICHED → Gate 2 | Enriched with 9 Jun findings; Gate 1 cleared on self-hosted path (Slack + data-training criteria non-blockers). Chained **Gate 2 PASS** (all Must-Haves met; Should-Have 17/25). Status moved Evaluating → **Sandbox**. Residual risk is operational (self-hosting ownership, build-it-ourselves Slack), not technical. Linked to sibling CRM issues AIR-77/93/76/94. |

*Other tools mentioned (already registered, no new info, no dispatch): Salesforce (AIR-93 — demo today), HubSpot (AIR-77), Attio (AIR-76/94), Monday.com (AIR-83), Obsidian, Slack, GitHub, Claude/Claude Code. Dev-tooling references in the JD (Codex, Antigravity) not dispatched — reference mentions only; Antigravity already tracked via sub-item 2956565232.*

---

## Monday Writes Summary

**Items touched (Step 3A — source bump to `AIO 9 Jun 2026`):**
- [2939688504](https://janusd-company.monday.com/boards/5095012818/pulses/2939688504) AIO engineering hire — + substantive Update (JD revisions, route to Bonaventure)
- [2882205554](https://janusd-company.monday.com/boards/5095012818/pulses/2882205554) CRM evaluation — + substantive Update (Twenty/20 findings, Stage-2 criteria resolved)
- [2882206287](https://janusd-company.monday.com/boards/5095012818/pulses/2882206287) Executive Management System for Bonaventure — sub-item added

**New parent items (Step 3D, both with Step 3G Description Updates):**
- [2978750463](https://janusd-company.monday.com/boards/5095012818/pulses/2978750463) AI Office Monday board reorganisation — per-department dashboards + orphan cleanup — Michael + Jehad
- [2978784424](https://janusd-company.monday.com/boards/5095012818/pulses/2978784424) AI-assisted post-standup Monday status & blocker digest — Jehad

**Sub-items created (Step 3B, both with Step 3G Description Updates):**
- [2978814400](https://janusd-company.monday.com/boards/5095012849/pulses/2978814400) Prepare department names, IDs & assignments for Monday reorganisation — Michael (under 2978750463)
- [2978814295](https://janusd-company.monday.com/boards/5095012849/pulses/2978814295) Add Bonaventure to Monday + pre-meeting status query (resolve .io vs .com + access level) — Michael (under 2882206287)

**Deduplication (Step 2B.1 / Step 3.0) — blocked:**
- "Revise AI Software Engineer JD…" sub-item — blocked, high-confidence duplicate of existing 2962726356 ("Revise AIO engineering hire profile…") and 2939705098 ("Draft job description…"). Captured via parent Update instead.
- "Review Simon's tool evaluation template…" sub-item — blocked, high-confidence duplicate of existing 2924562376 ("Review Simon's process docs — tool eval framework…"). Captured as next-step against the existing sub-item.

**Step 3H backfills:** 0 (all touched existing items already had Description headers).

**Context Coverage Invariant (Step 3I):** PASS — 7/7 touched items have Description Updates. No group moves (Step 3E.1 n/a).

---

## External / Other-Department Follow-ups

*(Not AIO-owned; captured for record only — no Monday items created.)*

- **IT — Nomi taken down.** Nomi was taken down by IT, creating a blocker. Explicitly flagged by Michael as an Obsidian/wiki item, not a Monday task ("it's not something we need to work on… we just mentioned it"). Relates to IT hand-off and the LinkedIn conversation.
- **Finance — Anne's approval box / budgets.** Anne requested budget input (via email) and an approval box for finance. Finance-owned; surfaces the need for a Finance grouping in the board reorg.
- **ISO — misfiled item.** "Send Jehad ISO process diagram to sign" is an ISO item currently sitting in the AI Office area; to be reassigned during the board reorganisation.

---

## Notes

- Attribution is reliable for this transcript: a genuine two-person back-and-forth between Michael Bruck and Jehad Altoutou, both clearly identified throughout.
- Linear AIP reconciliation: no AIP items referenced this standup — none performed.
