---
type: process
title: AI Registry (Linear AIR) management
slug: ai-registry
created: 2026-05-12
updated: 2026-06-09
departments: [ai-office]
sources: [section-5-ai-charter-policy-v2.1]
related: [linear, ai-tool-evaluation, ai-tool-evaluation-framework, ai-policy, shadow-ai-prohibition, tool-tiers, standup, claude, anthropic, janus-prime-radiant-build, aio-skills-sor-architecture-jehad, aio-playbooks-jehad, viktor, hostinger, n8n, obsidian]
---

# AI Registry (Linear AIR) management

Janus's reference convention for managing the AI Tools Registry in [[linear]] AIR. Owned by the AI Office. The canonical implementation is the **`/ai-registry` skill** — this wiki page is a short reference for cross-linking and high-level orientation, not a duplicate of the skill. Parallel in shape to [[ai-tool-evaluation]] (which references the `/ai-tool-evaluation` skill).

**Policy basis:** the AI Registry is codified in **§5.3 of the [[ai-policy|AI Policy]] v2.1** ([[section-5-ai-charter-policy-v2.1|canonical source]]) as "The Register of Approved AI Providers." The policy establishes (a) the registry exists, (b) [[shadow-ai-prohibition|Shadow AI is prohibited]] (no tools outside the registry), (c) tools are classified into [[tool-tiers|three tiers]] (Core Infrastructure / Functional Tools / AI Office Infrastructure), and (d) Data Sovereignty requirements (portability + documented API) are non-negotiable for any registry listing.

> **For execution, use the skill.** Do not paraphrase AIR conventions from this page when adding or updating registry entries; the skill is authoritative and may have moved ahead.

## What `/ai-registry` does

CRUD-and-narrative wrapper over [[linear]] AIR (the AI Registry team). The skill is the **only** sanctioned write path into AIR — the [[standup|/standup]] skill dispatches it as a subagent for tool-registry mutations, and the [[ai-tool-evaluation|/ai-tool-evaluation]] skill chains off it for Gate 1 evaluation immediately after a new AIR-N issue is created.

Responsibilities:

- Create AIR issues with the description-template schema (purpose, owner, source, integration sketch, cost class, departments touched, sandbox/production posture).
- Update existing issues as evaluation moves them through the pipeline (Backlog → Evaluating → Sandbox → Production → Monitor → Deprecated / Rejected / Duplicate).
- Apply the AIR label taxonomy (tool/infrastructure/workload classification, ISO-touch flags, departmental tags).
- Read AIR state for cross-references from the wiki and from other skills.

## Pipeline stages (canonical)

| Stage | Meaning | What's expected |
|---|---|---|
| **Backlog** | Candidate noted; no evaluation yet started | Initial dossier; pending Gate 1 |
| **Evaluating** | Gate 1 triage in progress | Gate 1 + Gate 2 evaluation |
| **Sandbox** | Gate 2 passed; controlled testing underway | Gate 3 trial in controlled environment |
| **Production** | Full approval; IT handover complete | Operationally managed under [[ai-policy]] §5.2 |
| **Monitor** | In production; watch-list for renewal/replacement/deprecation | Periodic review; no active redeployment |
| **Deprecated** | Retired from active use | Decommission path documented |
| **Rejected** | Failed evaluation; documented reason | Decision + rationale documented |
| **Duplicate** | Folded into another entry; pointer maintained | Closed in favour of canonical AIR |

Tools never return to Backlog once evaluation has begun — see [[2026-05-06-backlog-cleanup-no-return-to-backlog]].

## Gate framework summary

Full gate definitions live in [[ai-tool-evaluation-framework]]. Short form:

- **Gate 1 (Baseline, binary).** G1.1 Google Workspace · G1.2 Slack · G1.3 Data portability · G1.4 **Data training exclusion** (the most common Gate 1 failure) · G1.5 Documented API.
- **Gate 2 (Technical Qualification, scored).** MCP / agent-compatibility · enterprise SSO · vendor viability.
- **Gate 3 (Sandbox Evaluation).** Per-user data control architecture (added as hard requirement after the [[viktor|AIR-38 Viktor]] failure) · real-world workflow fit · cost validation.
- **Gate 4 (Production Approval).** IT handover + documentation + SOP.

A proposed pre-G1 filter — [[stack-composition-framework]] (three lenses: composability, agent operability, reversibility) — was surfaced on 2026-05-19. Status: proposed, not ratified.

## Lessons captured (running list)

A running record of insights surfaced *through* AIR operation. Not exhaustive — extracted lessons live in `lessons/` and dated decisions in `decisions/`; this list highlights the registry-shape patterns.

- **2026-04-22** — [[viktor|AIR-38 Viktor]] rejected on per-user ACL architecture: integrations connected per-user but used workspace-wide permissions. Now a hard Gate 1/2 criterion for any agent platform: integrations must run under the *requesting* user's permissions, not the connecting user's.
- **2026-04-20** — [[n8n|AIR-19 n8n]] moved from GCP to [[hostinger|AIR-79 Hostinger]]. GCP pilot exposed opaque, non-forecastable unit costs (egress, per-request). Hostinger flat-fee + Docker-native + one-click n8n won on transparent pricing and APAC residency.
- **2026-05-04** — Bakeoff cohort discipline. AIR-87 Hercules, AIR-88 Lovable, AIR-89 Bolt, AIR-90 v0, and AIR-32 Replit evaluated in parallel as a chat-to-app cohort. Decision: pick ONE primary, not approve all five.
- **2026-05-05** — CRM matrix. AIR-77 HubSpot + AIR-76 Attio + AIR-83 Monday.com + AIR-93 Salesforce benchmarked. Salesforce registered as benchmark only (NOT adoption candidate at current scale). 2026-05-19: matrix flipped to Attio per [[stack-composition-framework]] — see [[agentic-lean-marketing-stack]].
- **2026-05-08** — [[obsidian|AIR-74 Obsidian]] promoted Evaluating → Sandbox following heavy active use (Jehad's personal vault + Michael's Prime Radiant prototype).
- **2026-05-08** — AIR-95 draw.io adopted as canonical diagramming tool for ISO platform-and-tool-development with Simon. Open XML format = AI-readable.
- **2026-05-19** — First application of the proposed [[stack-composition-framework]] pre-filter — Cosmic (AIR-117), Attio (AIR-76), Vercel (AIR-113), Cloudflare (AIR-116), Cookiebot (AIR-124), Resend (AIR-118) selected for the marketing stack; Adobe AEM (AIR-121) rejected on the same framework.

## Tool / Infrastructure / Workload classification

Per [[ai-tool-evaluation]]: classify before evaluating. The skill enforces the trichotomy and applies the right Gate 1 criteria. Tool/Infrastructure/Workload framing affects which AIR labels apply and which gate criteria are scored.

## Relationship to other skills

- **[[standup|/standup]]** — orchestrator. Dispatches `/ai-registry` as a subagent when the standup transcript surfaces a new tool or a stage-change action. Per the v3.10+ chained-evaluation contract, every newly-created AIR-N entry immediately triggers a subsequent `/ai-tool-evaluation` Gate 1 dispatch.
- **[[ai-tool-evaluation|/ai-tool-evaluation]]** — sibling skill. Reads AIR state, posts gate comments, moves the issue between stages. Calls into `/ai-registry` for any write operation; never writes to AIR directly outside the skill's contract.
- **This wiki** — narrative layer. Vendor entity pages cross-reference their AIR issue (when one exists); decision and lesson pages may cite AIR comments. Closed AIR issues with substantive resolution narrative are an ingest source per `CLAUDE.md` §5.1.

## Linkage to systems of record

| Surface | Role | Skill access |
|---|---|---|
| [[linear]] AIR | Pipeline state (canonical) | `/ai-registry` writes; `/ai-tool-evaluation` reads + comments; `/standup` reads only |
| Monday Automations | Execution surface | Tool *adoption work* (sandbox tasks, IT handover items) lives here; not the registry itself |
| Notion Operations Notebook | Daily journal | Decisions about tools captured in standup logs; ingested back into the wiki |
| This wiki | Narrative + cross-cutting analysis | Vendor pages, decisions, lessons, briefs |

## Federated reference

Jehad's federated synthesis pages document the read-vs-write matrix and subagent-dispatch JSON contracts in operational detail — see [[aio-skills-sor-architecture-jehad]] and [[aio-playbooks-jehad]].

## When to update this page

When the `/ai-registry` skill version drifts and the pipeline stages, labels, or subagent-dispatch contract change. For minor internal refinements, the canonical skill file is sufficient — no need to update here.

## Convention note

This page exists so that the wikilink form `[[ai-registry|/ai-registry]]` (display-alias form for slash-command references) resolves cleanly across the wiki. Matches the existing `[[ai-tool-evaluation|/ai-tool-evaluation]]` and `[[standup|/standup]]` convention.

## Merge history

**2026-05-20** — folded in content from `concepts/ai-registry.md` (created 2026-05-15, captured_by Jehad). The duplicate concept page is removed; its pipeline-detail and dated lessons list are merged into the sections above. The 2026-05-20 lint surfaced the duplicate-slug as the only real action item from the duplicate-slug check.

---

## Operational notes — Linear AIR (AI Registry)

_Migrated from the personal-vault 'AI Office Brain' base, 2026-06-09._

# Linear — AI Registry (AIR)

Team UUID: `598dd614-dce5-4ede-98ef-207f3bdff33c`
Issue prefix: `AIR-N` (e.g. AIR-92)

The single source of truth for every AI/SaaS tool the company uses, evaluates, deprecates, or rejects. **Owned by [[ai-registry]]**; gate-evaluation comments owned by [[ai-tool-evaluation]].

> ⚠️ The team's UUID was originally created with the name "AI Office" but issues are prefixed `AIR-N`. The legacy UUID is correct; the prefix is what matters.

## What lives here

For every tool:
- **Title** — canonical tool name
- **Description** — full template per [[ai-registry]]'s schema (Category, Cost per User/Month, Number of Licences, Total Monthly Cost, Departments, Janus-specific analysis, Requested by)
- **Status** — Backlog / Evaluating / Sandbox / Production / Monitor / Deprecated / Rejected / Duplicate
- **Labels** — Tier (Core Infrastructure / Functional / AI Office Infrastructure) + Department(s)
- **Priority** — 1 (Urgent) → 4 (Low)
- **Comments** — Gate 1, 2, 3, 4 assessments (added by [[ai-tool-evaluation]])
- **Links** — vendor URL, pricing page, ToS, DPA, etc.

## Pipeline (status workflow)

```
Backlog → Evaluating → Sandbox → Production
                              ↘ Monitor
                ↘ Deprecated / Rejected / Duplicate
```

Tools enter at Backlog, move through Evaluating (Gate 1 + 2), Sandbox (Gate 3 domain expert testing), then Production (Gate 4 IT handover). Monitor is for tools in production but flagged for ongoing review.

## Status UUIDs (for direct API writes)

Documented in `/ai-registry/references/linear-context.md`. Not duplicated here per the Context Separation Rule.

## Tier classification (Janus AI policy §5.2.1)

- **Core Infrastructure (Tier 1)** — universal tools deployed across all departments
- **Functional (Tier 2)** — department-specific approved applications
- **AI Office Infrastructure (Tier 3)** — infrastructure tools managed by AI Policy

## Department labels (requestor / owner)

Office of CEO, AI Policy, Technology, Finance, Marketing, Commercial, Legal, Training, Country.

## Snapshot stats (May 2026)

74 active issues, distributed across all states. Most recent additions:
- **AIR-92** Wispr Flow (Whisper Flow) — added 1 May 2026 standup; Backlog; Functional + Technology + AI Policy

## Derivative views (regenerated on demand by [[ai-registry]])

- **Slack Canvas** — "Janus Digital — Approved AI Tools" (Production-only, employee-facing; tier-grouped)
- **Excel workbook** — `Janus_AI_Registry.xlsx` (full registry, dashboard, AIP project sheet)

## Read-vs-write

- **[[ai-registry]]** writes (descriptions, status, labels, priority)
- **[[ai-tool-evaluation]]** writes (gate-decision comments only)
- **[[standup]] never writes here directly** — it dispatches subagents to [[ai-registry]] / [[ai-tool-evaluation]]
- The deprecated [[monday]] is a frozen one-time mirror; not synced

## Related

- Skill: [[ai-registry]] (CRUD)
- Skill: [[ai-tool-evaluation]] (gate comments)
- Deprecated mirror: [[monday]]
- Reference docs: `references/linear-context.md`, `references/template.md`

---

## Notes — ai-registry skill

_Migrated from the personal-vault 'AI Office Brain' base, 2026-06-09._

# /ai-registry — AI Tools Registry engine

Manages the AI Registry on Linear (the AIR team). The single source of truth for every AI/SaaS tool the company uses, evaluates, deprecates, or rejects. Companion to [[ai-tool-evaluation]].

## When to use

Trigger phrases include:
- *"Add Harvey AI to the backlog"*
- *"Update AIR-25 status to Production"*
- *"Enrich the description for Wispr Flow"*
- *"Mark AIR-N as deprecated"*
- *"Update the Slack Canvas / regenerate the Excel workbook"*

Also dispatched as a subagent by [[standup]] when transcripts contain explicit tool decisions / actions / registry instructions.

## What it does

1. **Add a new tool** — research via Chrome (homepage, pricing, ToS, integrations, security), create AIR-N issue with the standard description schema, assign labels (department + tier), set priority, note the requester.
2. **Enrich an existing entry** — fetch current description, research deeper, save updated description preserving anything still accurate.
3. **Update status / labels / assignments** — `save_issue` on the identifier (e.g. AIR-25) with the changed fields.
4. **Handle duplicates** — fetch both issues, merge unique info into the primary, mark the duplicate with status `Duplicate` and `duplicateOf`.
5. **Bulk updates from meeting transcripts** — apply meeting decisions (status changes, assignments, new tools, deprecations) one at a time.
6. **Regenerate derivative views**:
   - **Slack Canvas** — "Janus Digital — Approved AI Tools" (Production-only, employee-facing).
   - **Excel workbook** — `Janus_AI_Registry.xlsx` (full registry, dashboard, AIP sheet).

## Pipeline (the AIR workflow)

Tools flow through:

```
Backlog → Evaluating → Sandbox → Production
                               ↘ Monitor
                  ↘ Deprecated / Rejected / Duplicate
```

## Labels

**Tier (governance level):**
- Core Infrastructure — universal tools deployed across all departments (Tier 1)
- Functional — department-specific approved applications (Tier 2)
- AI Office Infrastructure — infrastructure tools managed by AI Policy (Tier 3)

**Department (requestor / owner):**
Office of CEO, AI Policy, Technology, Finance, Marketing, Commercial, Legal, Training, Country.

## Source of truth

[[ai-registry]] — team UUID `598dd614-dce5-4ede-98ef-207f3bdff33c`. **This skill writes here directly.**

[[monday]] is deprecated and not maintained by this skill any longer.

## Subagent invocation contract (when dispatched by [[standup]])

Receives a JSON hand-off package per the [[ai-office-architecture]] schema. Returns a JSON object with `action_completed`, `linear_air_issue` (AIR-N), `final_status_or_result`, `monday_task_required` (boolean + optional task_title/reason), `notion_journal_addition`, `unresolved_questions_or_blockers`.

`monday_task_required.required` MUST be a boolean. Used by [[standup]] to optionally create a follow-up Monday Automations task when the registry work implies operational follow-up (e.g., "Configure SSO for new tool").

## Governance context

Enforces the Janus Digital AI & Automated Systems Policy:
- §5.2.1 — Tool categorisation (3 tiers)
- §5.2.3 — Data boundaries (no internal/confidential data in public/free-tier models)
- §5.2.4 — Justification protocol
- §5.3.1 — Human-in-the-loop accountability
- §5.4 — Violations

When an employee asks about tool approval or data handling, cite the relevant policy section.

## Related

- Companion: [[ai-tool-evaluation]] (formal Gate 1–4 methodology)
- Orchestrator: [[standup]] (dispatches this skill via subagent)
- System of record: [[ai-registry]]
- Reference docs (in plugin): `references/linear-context.md`, `references/template.md`
