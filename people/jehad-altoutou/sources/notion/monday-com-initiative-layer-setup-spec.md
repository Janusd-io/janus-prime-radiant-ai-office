---
type: source
source_type: notion
slug: monday-com-initiative-layer-setup-spec
title: Monday.com Initiative Layer — Setup Spec
created: 2026-04-27
captured_by: jehad-altoutou
notion_url: https://www.notion.so/34f114fc090c80c1a680d87e30cd709e
audience: department
departments: [ai-office]
sensitivity: dept
sensitivity_confidence: 0.5
---

**Version:** 1.0 — 2026-04-27<br>**Author:** Michael Bruck (with Claude)<br>**Purpose:** Concrete configuration for replicating Linear's Initiatives behavior in Monday.com on the Pro tier, as part of the System of Record (SOR) evaluation.
---
## Plan Reality
<table header-row="true">
<tr>
<td>Tier</td>
<td>Cost (annual billing)</td>
<td>Native Portfolio?</td>
<td>Verdict</td>
</tr>
<tr>
<td>Free</td>
<td>\$0 (2 seats)</td>
<td>No</td>
<td>Insufficient for SOR</td>
</tr>
<tr>
<td>Basic</td>
<td>\$9/seat/mo</td>
<td>No</td>
<td>Limited automations</td>
</tr>
<tr>
<td>Standard</td>
<td>\$12/seat/mo</td>
<td>No</td>
<td>Workable but limited dashboards</td>
</tr>
<tr>
<td>**Pro**</td>
<td>**\$19/seat/mo**</td>
<td>**No (build it)**</td>
<td>**Recommended starting point**</td>
</tr>
<tr>
<td>Enterprise</td>
<td>Contact sales</td>
<td>Yes (native Portfolio Solution)</td>
<td>Re-evaluate after pilot</td>
</tr>
</table>
**Decision:** Spec for Pro tier. Enterprise upgrade is a downstream decision after the pilot proves the rhythm has value.
---
## Pre-Work: Workspace Cleanup
The trial workspace `janusd-company.monday.com` currently has test artifacts:
- `My first project`
- `MCP getting started`
- `Automation Plans & Task Tracking`
- `Subitems of Automation Plans & Task Tracking`
- Two `New Workflow` boards
- `Asana Task Import` (+ subitems board)
**Action:** Archive all of the above before standing up the real structure.
---
## Workspace Architecture
```plain text
janusd-company.monday.com
└── Main workspace
    ├── 📋 Strategic Operations (folder)
    │   ├── 🎯 Initiatives (board)         ← top-level "initiative" objects
    │   ├── 🛠️  Projects (board)           ← workstream-level objects
    │   └── 📊 Janus Strategic View (dashboard)
    ├── 🏢 Departmental Work (folder)
    │   ├── AI Office Work (board)
    │   ├── Finance Work (board)
    │   ├── HR Work (board)
    │   └── ...
    └── 📚 AI Registry (folder)
        └── AI Registry (board)            ← mirrors current Linear AIR
```
The folder structure mirrors the conceptual layers: strategic (initiatives + projects), operational (per-department work), reference (registry).
---
## Board Schemas
### Board: Initiatives
One row per initiative. This is the closest analog to Linear's Initiative object.
<table header-row="true">
<tr>
<td>Column</td>
<td>Type</td>
<td>Purpose</td>
</tr>
<tr>
<td>Name</td>
<td>Text</td>
<td>Initiative title</td>
</tr>
<tr>
<td>Owner</td>
<td>People</td>
<td>Single accountable owner</td>
</tr>
<tr>
<td>Health</td>
<td>Status (RAG)</td>
<td>`On Track` / `At Risk` / `Off Track` / `No Update Yet`</td>
</tr>
<tr>
<td>Status</td>
<td>Status</td>
<td>`Planned` / `Active` / `Completed` / `On Hold`</td>
</tr>
<tr>
<td>Timeline</td>
<td>Timeline</td>
<td>Start + target date</td>
</tr>
<tr>
<td>Last Update</td>
<td>Long Text</td>
<td>Auto-populated from latest update form submission</td>
</tr>
<tr>
<td>Last Update Date</td>
<td>Date</td>
<td>Auto-populated; drives staleness logic</td>
</tr>
<tr>
<td>Charter</td>
<td>Doc</td>
<td>Workdoc with full charter, scope, success criteria</td>
</tr>
<tr>
<td>Connected Projects</td>
<td>Connect Boards → Projects</td>
<td>Links to workstream rows</td>
</tr>
<tr>
<td>Project Health Rollup</td>
<td>Mirror</td>
<td>Worst-case Health from connected Projects</td>
</tr>
<tr>
<td>Slack Channel</td>
<td>Link</td>
<td>Default channel for this initiative's updates</td>
</tr>
<tr>
<td>Notion Link</td>
<td>Link</td>
<td>Pointer to long-form narrative in Notion</td>
</tr>
</table>
### Board: Projects
One row per workstream under an initiative.
<table header-row="true">
<tr>
<td>Column</td>
<td>Type</td>
<td>Purpose</td>
</tr>
<tr>
<td>Name</td>
<td>Text</td>
<td>Workstream/project title</td>
</tr>
<tr>
<td>Initiative</td>
<td>Connect Boards → Initiatives</td>
<td>Parent initiative</td>
</tr>
<tr>
<td>Owner</td>
<td>People</td>
<td>Workstream lead</td>
</tr>
<tr>
<td>Health</td>
<td>Status (RAG)</td>
<td>Same statuses as Initiatives</td>
</tr>
<tr>
<td>Status</td>
<td>Status</td>
<td>`Backlog` / `Planned` / `In Progress` / `Blocked` / `Done` / `Cancelled`</td>
</tr>
<tr>
<td>Timeline</td>
<td>Timeline</td>
<td>Start + target</td>
</tr>
<tr>
<td>Connected Items</td>
<td>Connect Boards → Departmental Work boards</td>
<td>Links to actual tasks</td>
</tr>
<tr>
<td>AIR References</td>
<td>Connect Boards → AI Registry</td>
<td>Links to relevant tools</td>
</tr>
<tr>
<td>Last Update</td>
<td>Long Text</td>
<td>Latest project-level note</td>
</tr>
</table>
### Board: Work Items (per department)
Standard task board with a `Project` connect-board column linking back upward. The schema you already use elsewhere — Status, Owner, Priority, Timeline, Description.
### Board: AI Registry
Mirror or migration of current Linear AIR. Same lifecycle states (`Backlog → Evaluating → Sandbox → Production → Monitor → Deprecated`), same per-tool fields (cost, departments, evaluator, gate scores). When Linear is decommissioned for AIR, this becomes the source of truth; until then, it's a mirror.
---
## Update Cadence — Automation Recipes
These five recipes replicate Linear's update flow:
### Recipe 1: Weekly reminder
> When the date arrives every **Wednesday at 9:00 AM Riyadh time**,<br>notify the **Owner** of each active initiative:<br>*"Time to post your weekly update for \[Initiative\]. Click here: \[Form URL\]"*
### Recipe 2: Form-driven update post
Build a Monday Form titled **"Post Initiative Update"** with these questions:
- Initiative (dropdown, populated from Initiatives board)
- Health (radio: On Track / At Risk / Off Track)
- Headline (short text — 1-line summary)
- What changed since last update (long text)
- Blockers (long text, optional)
- Next steps (long text)
On form submission:
- Append the response as an Update on the chosen Initiative item
- Set the Health column to the selected value
- Stamp Last Update Date to today
- Trigger Recipe 4 (Slack post)
### Recipe 3: Stale-update escalation
> When Last Update Date is **more than 10 days ago** AND Status is `Active`,<br>notify Owner: *"Update overdue for \[Initiative\] — last posted on \[date\]."*<br>If still not posted after 2 working days, escalate to Michael.
### Recipe 4: Slack cross-post on update
> When an Update is posted on an Initiative,<br>send a structured message to **#initiative-updates**:
	```plain text
[Health Emoji] [Initiative Name] — [Health Status]
Owner: [Name]
Headline: [...]

What changed: [...]
Blockers: [...]
Next: [...]

🔗 View in Monday | 📄 Charter
	```
### Recipe 5: At-Risk alert
> When Health changes to `At Risk` or `Off Track`,<br>post to **#initiative-updates** with `@here`:<br>*"⚠️ \[Initiative\] is now \[status\]. Latest update: \[latest update text excerpt\]"*
---
## Slack Integration — Honest Limitations
Monday's Slack integration is **board/item-level**, not initiative-update-level the way Linear's is. Specifically:
**Works well:** Posting structured update messages to a channel (Recipe 4 above), notifying owners on automation triggers, mentioning teammates from Monday into Slack.
**Workable but rougher:** Bidirectional comment sync. Monday syncs item conversation to Slack threads, but the polish of Linear's "reply in Slack thread, see it in the Initiative Update" is not 1:1. You'll see Slack thread replies appear as item conversation entries, but the UX is less native.
**Worth testing in pilot:** Whether Bonaventure (or any consumer) can react and discuss in Slack and have it feel as integrated as Linear does. This is the single biggest UX-comparison datapoint between the two tools.
---
## Narrative Layer (Notion Boundary)
Per the standup decision (#80) — Notion is the **narrative home**, no mirroring of operational state.
**Inside Monday (Workdoc per Initiative):**
- Charter (1-2 paragraphs of why this exists)
- Scope (what's in, what's out)
- Success criteria (what "done" looks like)
- Decision log (operational decisions made along the way)
**Inside Notion (linked from the Initiative item):**
- Long-form strategic context
- Departmental themes / OKR rationale
- External-stakeholder narratives
- Anything that needs months/years of edit history
**Rule of thumb:** If it changes weekly, Workdoc. If it changes quarterly or less, Notion. Cross-link both directions.
---
## Dashboard: Janus Strategic View
Pro tier supports 20-board dashboards. Build one with these widgets:
1. **Initiative Health Card View** — all initiatives, color-coded by Health, sorted by stale-time
2. **Timeline View** — Gantt of initiative target dates
3. **Workload by Owner** — who's responsible for what
4. **Stale Update Flag** — initiatives where Last Update Date \> 10 days ago
5. **Project Rollup** — all Projects across all Initiatives, grouped by parent
6. **At-Risk Cluster** — projects + initiatives currently flagged
This is the surface Bonaventure would visit. Goal: glance at it, understand company state in 30 seconds.
---
## Worked Example: Finance Automation v1
This is one of the two pilot initiatives proposed for the Linear test. Setting it up in Monday in parallel:
**Initiatives board row:**
<table header-row="true">
<tr>
<td>Field</td>
<td>Value</td>
</tr>
<tr>
<td>Name</td>
<td>Finance Automation v1</td>
</tr>
<tr>
<td>Owner</td>
<td>Jehad Altoutou</td>
</tr>
<tr>
<td>Health</td>
<td>On Track</td>
</tr>
<tr>
<td>Status</td>
<td>Active</td>
</tr>
<tr>
<td>Timeline</td>
<td>2026-04-27 → 2026-08-31</td>
</tr>
<tr>
<td>Charter</td>
<td>\[Workdoc\] FAv1 — End-to-end finance workflow for Ann Greed</td>
</tr>
<tr>
<td>Connected Projects</td>
<td>Invoice Bot v3/v4, Airwallex Spend integration, Finance Dashboard, Deel API assessment</td>
</tr>
<tr>
<td>AIR References</td>
<td>Claude in Excel (AIR-30), Shortcut AI (AIR-28)</td>
</tr>
<tr>
<td>Slack Channel</td>
<td>#initiative-updates</td>
</tr>
<tr>
<td>Notion Link</td>
<td>\[Notion narrative page\]</td>
</tr>
</table>
**Connected Projects (rows in Projects board):**
<table header-row="true">
<tr>
<td>Project</td>
<td>Owner</td>
<td>Health</td>
<td>Status</td>
</tr>
<tr>
<td>Invoice Bot v3</td>
<td>Jehad</td>
<td>On Track</td>
<td>Done</td>
</tr>
<tr>
<td>Invoice Bot v4</td>
<td>Michael</td>
<td>On Track</td>
<td>In Progress</td>
</tr>
<tr>
<td>Airwallex Spend integration</td>
<td>Jehad</td>
<td>At Risk</td>
<td>Planned</td>
</tr>
<tr>
<td>Finance Dashboard (NL query)</td>
<td>Jehad</td>
<td>On Track</td>
<td>Backlog</td>
</tr>
<tr>
<td>Deel API assessment</td>
<td>Michael</td>
<td>On Track</td>
<td>Planned</td>
</tr>
</table>
**Initiative Health rollup:** Pulls "At Risk" from Airwallex Spend, so Initiative shows At Risk overall. Recipe 5 fires, posts to #initiative-updates.
This is the same shape as the Linear pilot — same inputs, same expected outputs, different tool. Direct A/B comparison.
---
## Implementation Order (3-4 Day Job)
**Day 1 — Cleanup + Schema**
- Archive existing trial-experiment boards
- Create folder structure
- Build Initiatives, Projects, AI Office Work boards with schemas above
- Build the Update Form
**Day 2 — Automations + Slack**
- Wire 5 automation recipes
- Connect Monday Slack integration
- Create #initiative-updates channel if needed
- Test fire each recipe end-to-end
**Day 3 — Pilot Initiative Setup**
- Create Finance Automation v1 + Meeting Intelligence Layer rows in Initiatives
- Populate Projects rows for each
- Cross-link to AI Registry tools where relevant
- Write initial Charter Workdocs
**Days 4-21 — Run + Observe**
- Weekly Wednesday update cadence kicks in
- Side-by-side with Linear pilot
- Daily glance at the Strategic View dashboard
---
## Pilot Evaluation Criteria
Track these for both tools across the 3-week pilot:
1. **Time to post an update** (form open → submit). Lower wins.
2. **Subjective friction** — does the cadence feel like leverage or like nag? (Owner self-report at end of each week.)
3. **Reading the rollup** — can a leader (Michael as proxy for Bonaventure) understand current state in \<60 seconds from the dashboard / Initiatives view? Subjective 1-5 score.
4. **Slack thread quality** — when a stakeholder reacts to an update post, does the thread feel native or bolted-on?
5. **Maintenance overhead** — count any time spent fixing mirror columns, debugging automations, or re-explaining the model. Lower wins.
6. **Cost-per-cadence** — Linear free vs. Monday Pro per-seat × number of operators.
---
## Cost Comparison Snapshot
For decision context:
- **Linear Free** — \$0/mo for \~2 seats, \~250 issues. Hard cap when scaling beyond.
- **Linear Standard** — \$8/seat/mo. Janus-wide (\~150 seats hypothetical) = \~\$1,200/mo = \~\$14k/yr.
- **Monday Pro** — \$19/seat/mo. Janus-wide (\~150 seats) = \~\$2,850/mo = \~\$34k/yr.
- **Monday Enterprise** (with native Portfolio) — Contact sales; meaningfully higher.
- **Notion** — Existing spend, already paid.
The "use both" near-term answer: keep Linear free for AI Office (it's the right tool for our specific operational shape), use Monday Pro company-wide for ops (it's the right tool for finance/HR/marketing/etc. who need flexibility, not opinionated execution). The Initiatives layer lives in whichever tool the leadership consumer prefers — that's the question the pilot answers.
---
## Open Questions To Resolve During Trial
1. **Confirm Pro plan capabilities on the trial.** The current trial may be auto-upgraded to Enterprise features for evaluation; need to verify what we'd actually have post-purchase.
2. **Test Monday's Slack bidirectional sync** with a real conversation — measure friction vs. Linear's same flow.
3. **Test mirror column robustness.** Worst-case rollup logic (Health = max severity of children) is a common Monday pattern but requires explicit configuration. Confirm it doesn't lag or break.
4. **Confirm whether Monday's update form can be used by non-licensed users** (i.e., can department heads post updates without a paid seat?). Affects the cost model materially.
5. **Compare the "Bonaventure glance"** — show the dashboards side by side to him after week 2 and ask which surface he'd actually open every morning.
<file src="file://%7B%22source%22%3A%22attachment%3Ae37f5128-c050-4134-b600-7a72fe4a76d7%3Amonday-portfolio-initiative-setup.md%22%2C%22permissionRecord%22%3A%7B%22table%22%3A%22block%22%2C%22id%22%3A%2234f114fc-090c-8030-a577-f045902fb3f1%22%2C%22spaceId%22%3A%22ba9114fc-090c-817e-ab0d-0003877c27a7%22%7D%7D"></file>
