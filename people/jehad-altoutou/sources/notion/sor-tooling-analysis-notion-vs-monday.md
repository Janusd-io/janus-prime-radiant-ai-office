---
type: source
source_type: notion
slug: sor-tooling-analysis-notion-vs-monday
title: SOR Tooling Analysis — Notion vs Monday.com (for CEO Executive Management System)
created: 2026-04-21
captured_by: jehad-altoutou
notion_url: https://www.notion.so/348114fc090c81d79220ef9b4e001c7f
audience: department
departments: [ai-office]
sensitivity: dept
sensitivity_confidence: 0.5
---

> **For:** Jehad Altoutou
> **From:** Michael Bruck (analysis framing by Claude)
> **Date:** 20 April 2026
> **Related:** [AIR-83 ](https://linear.app/janusd/issue/AIR-83/mondaycom)[Monday.com](http://Monday.com) · [AIR-44 ClickUp](https://linear.app/janusd/issue/AIR-44/clickup)
> **Status:** Analysis in progress — not a decision. Waiting on Simon's ISO requirements before closing.
## Why this page exists
Jehad, you raised [Monday.com](http://Monday.com) as a candidate in the meeting with Bonaventure today, and the team's been developing the framing for the CEO Executive Management System. This page captures where the analysis currently sits so you're in the loop on how we're thinking about the tooling decision — especially because your [Monday.com](http://Monday.com) recommendation genuinely reshaped the trade-off. Your input on the head-to-head below is wanted before we close the decision.
## What changed after the Bonaventure meeting
Going in, the working assumption was **Notion as the single SOR**, based on a design centred on strategic initiatives → quarterly objectives → measurable outputs → weekly status. Bonaventure reframed several things:
- He explicitly chose **task-based, bottom-up rollup** — not OKR/objectives. Direct quote: "I think I'm more on task right now on the project level. Seeing where everyone is right now, that's really it."
- The CEO weekly meeting was **deprioritised**. He said "don't worry about me at this time — worry about applying this for everyone to see what you've done."
- He moved **ISO-compliant workflow documentation** (under Simon) to the top of the stack. Workflows per department → automation → cross-departmental agents → real-time compliance → eventual "Janus standard."
- He confirmed **Asana is out**, and was open to [Monday.com](http://Monday.com) when you brought it up.
The net effect is that the tooling criteria rebalance. The original pitch leaned toward Notion's flexibility and documentation-plane strengths. Bonaventure's reframe pulls weight back toward **task/workflow maturity and dashboard visualisation** — which is [Monday.com](http://Monday.com)'s territory.
## The decision, sharpened
The real question is no longer "Notion or [Monday.com](http://Monday.com) for the CEO management system." It's:
> What tool(s) best support task-based, bottom-up work capture per department, with documentation of ISO-compliant workflows sitting alongside, such that an AI agent can read meeting transcripts and write structured state into the right place?
## Head-to-head against Bonaventure's actual criteria
<table header-row="true">
<tr>
<td>Criterion</td>
<td>Winner</td>
<td>Notes</td>
</tr>
<tr>
<td>Task-based, bottom-up rollup with CEO pull-up visibility</td>
<td>[**Monday.com**](http://Monday.com)</td>
<td>Boards → workspaces → dashboards is the product's core metaphor. 50-board dashboard ceiling on Enterprise covers 12 functions with headroom. Notion requires schema work to achieve the same shape.</td>
</tr>
<tr>
<td>ISO-compliant workflow documentation</td>
<td>**Notion**</td>
<td>Workflow documentation, policies, procedures, evidence artefacts — Notion's native territory. [Monday.com](http://Monday.com) Docs is a secondary feature, not a knowledge system.</td>
</tr>
<tr>
<td>Agent writability (Fireflies → SOR pipeline)</td>
<td>[**Monday.com**](http://Monday.com)** (slight edge)**</td>
<td>Both capable. [Monday.com](http://Monday.com) has mature REST + GraphQL APIs with good item CRUD semantics and webhooks. Notion's API is clean but less task-idiomatic. For writing tasks with status/assignee/date/commitment fields, [Monday.com](http://Monday.com) edges ahead. For writing narrative pages, Notion does.</td>
</tr>
<tr>
<td>Security, IAM, audit</td>
<td>**Tie (slight edge **[**Monday.com**](http://Monday.com)** at top end)**</td>
<td>Both: SOC 2 Type II, ISO 27001, SAML SSO, SCIM, audit logs on Enterprise. [Monday.com](http://Monday.com) additionally: ISO 27032, ISO 27701, DORA alignment, Guardian add-on (BYOK, TLE, DLP).</td>
</tr>
<tr>
<td>Pricing transparency</td>
<td>**Tie**</td>
<td>Both publish mid-tier pricing; both are custom at Enterprise. [Monday.com](http://Monday.com) has a 3-seat minimum and bucket pricing in multiples of 5 — inflates small-team costs.</td>
</tr>
<tr>
<td>Multi-country playbook model</td>
<td>[**Monday.com**](http://Monday.com)** (slight edge)**</td>
<td>Template + board-duplication workflow is built for this. Notion can do it via templates, less natively.</td>
</tr>
<tr>
<td>Third-party-first philosophy</td>
<td>**Tie**</td>
<td>Both mature, VC-scale, publicly traded or equivalent. Both fit.</td>
</tr>
</table>
## Three realistic paths
### Path 1 — [Monday.com](http://Monday.com) as SOR + Notion as documentation/knowledge plane (two-tool)
Each tool does what it's best at. Agent writes tasks to [Monday.com](http://Monday.com), writes narrative and decisions to Notion, cross-links by ID. Costs more (two Enterprise contracts eventually) and adds an integration seam — but the seam is managed by agents rather than humans, which makes it less painful than it sounds. Matches Bonaventure's reframe most cleanly.
### Path 2 — Notion for everything (Notion-primary, single tool)
Works, but task/dashboard UX is noticeably weaker than [Monday.com](http://Monday.com) and we invest significant schema effort up-front. Cheaper and architecturally cleaner. A bet that Notion's 2026 roadmap keeps closing the gap — not a certainty.
### Path 3 — [Monday.com](http://Monday.com) for everything (Monday-primary, single tool)
Works for task-heavy functions, but ISO documentation and knowledge base live in a tool not designed for them. Risk: the documentation plane gets neglected because the tool makes it feel second-class.
## Current lean
**Path 1 (two-tool) is the current lean** — because Bonaventure's reframe genuinely pulls in both directions and picking one tool forces a compromise on whichever side loses. It keeps Linear intact for engineering / AI Projects, meaning the end state is:
- **Linear** — engineering + AI project tracking (current)
- [**Monday.com**](http://Monday.com) — operations & CEO management system SOR (new)
- **Notion** — documentation, ISO artefacts, knowledge base (current, deepened)
Three tools, three clear roles, each best-in-class for its lane.
This is a lean, not a decision. It's subject to what Simon says about ISO requirements — specifically whether his ISO programme has a preferred documentation tool, and how tightly workflow documentation needs to sit against the tasks it governs.
## Why we're not closing yet
Simon's ISO requirements are the critical path this week. Possible outcomes that would shift the lean:
- If Simon has a preferred specialist ISO tool (e.g., Greenlight Guru, MasterControl, Qualio), the documentation plane moves out of Notion and the case for a simpler SOR ([Monday.com](http://Monday.com) alone, or Notion alone) strengthens.
- If Simon says "just give me Notion and we'll structure it properly," Path 2 (Notion-primary) becomes more viable.
- If Simon wants ISO workflow docs to sit directly against the tasks they govern, Path 1 (two-tool with strong cross-linking) holds.
## What I'd like from you, Jehad
1. **Is the **[**Monday.com**](http://Monday.com)** capability picture above accurate?** You've worked with it more than I have. Anything wrong, understated, or missed?
2. **The agent-driven task creation pattern on **[**Monday.com**](http://Monday.com) — any gotchas you've seen with the API at scale (rate limits, webhook reliability, status transition semantics) that would change the integration picture?
3. **ClickUp (AIR-44) closure** — OK to mark ClickUp as Duplicate once we lock in [Monday.com](http://Monday.com) vs Notion, or do you see a reason to keep it live?
4. **Your instinct on the path** — given Bonaventure's reframe, do you still lean [Monday.com](http://Monday.com)-primary, or has the documentation-plane weight shifted your view toward the two-tool model?
Drop comments inline or pull me / the Claude session into a thread — whichever is easier.
---
*This page is a working document, not a final decision. v3 of the CEO Executive Management System design document will be produced after Simon's meeting closes out the ISO requirements.*
<empty-block/>
