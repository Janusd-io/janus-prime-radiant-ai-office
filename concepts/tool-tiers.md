---
type: concept
title: Tool tiers (Core Infrastructure / Functional Tools / AI Office Infrastructure)
slug: tool-tiers
created: 2026-05-22
updated: 2026-05-22
departments: [ai-office, it-ops, iso]
status: active
sources: [section-5-ai-charter-policy-v2.1]
related: [ai-policy, ai-registry, ai-tool-evaluation-framework, shadow-ai-prohibition, fireflies, organisational-digital-twin]
---

# Tool tiers

The three-tier classification for every AI tool in the [[ai-registry|AI Registry]], codified in §5.3.1 of the [[ai-policy|AI Policy v2.1]]. Determines scope of deployment, who can access, and which evaluation criteria apply.

## The three tiers

| Tier | Scope | Description |
|---|---|---|
| **Core Infrastructure** | Universal — all staff | Mandatory platforms integrated into the Janus Digital operating environment. Vetted for maximum security and compliance. Deployed organisation-wide. |
| **Functional Tools** | Department-specific | Specialised applications approved for specific use cases or departments. Access granted by department and role. |
| **AI Office Infrastructure** | AI Office managed | Platforms and services operating below the employee-facing layer — development infrastructure, model APIs, internal tooling. Employees do not interact with these directly. |

## Tool vs Infrastructure — orthogonal to tier

A separate but related classification (§5.3.2) determines *which evaluation criteria apply*:

- **Tool** — a user-facing application that employees interact with directly.
- **Infrastructure** — a platform or service operating below the user-facing layer.

Tier (scope of deployment) and Tool/Infrastructure (interaction surface) intersect: a Core Infrastructure tool like [[fireflies|Fireflies]] is a *Tool* (employees interact with it) deployed at *Core Infrastructure* tier (universal). A model API like Anthropic's Claude API is *Infrastructure* deployed at *AI Office Infrastructure* tier (employees don't interact with it directly).

## Example classifications (as of 2026-05-22)

| Tool | Tier | Tool/Infra | Rationale |
|---|---|---|---|
| [[fireflies]] | Core Infrastructure | Tool | Foundational capture layer of the [[organisational-digital-twin|organisational twin]] per the [[coordination-leverage-model]] §4.2. Universal-staff scope. |
| [[claude]] (Cowork, Claude Code, chat) | Core Infrastructure | Tool | Janus-wide AI-Native operating layer. |
| [[monday]] | Core Infrastructure | Tool | Primary execution surface across departments. |
| [[linear]] | Core Infrastructure | Tool | AI Tools Registry system-of-record + AI Projects tracking. |
| [[notion]] | Core Infrastructure | Tool | Operations Notebook journal surface. (Deprecation in progress for non-AIO seats — see [[2026-05-11-notion-restricted-to-aio-no-broad-rollout]].) |
| Anthropic Claude API | AI Office Infrastructure | Infrastructure | Model API; employees don't interact directly; powers downstream surfaces. |
| [[hostinger]] | AI Office Infrastructure | Infrastructure | Hosting layer; sub-employee-facing. |
| Marketing stack (Cosmic, Attio, Vercel, Cloudflare, Resend, Cookiebot) | Functional Tools | Tool | Marketing-department scope; see [[agentic-lean-marketing-stack]]. |
| [[assessify]] | Functional Tools | Tool | HR department scope (recruitment assessment). |

## Why the classification matters

- **Gate criteria applicability.** Different tiers + Tool/Infrastructure splits trigger different Gate 1–4 criteria. A Core Infrastructure tool faces the most scrutiny (universal deployment = universal risk surface). AI Office Infrastructure faces different scrutiny (no employee-facing surface, but high blast radius if it fails). [[ai-tool-evaluation-framework]] documents the per-classification criteria.
- **Access provisioning.** Functional Tools require department-and-role-scoped access; Core Infrastructure is provisioned organisation-wide; AI Office Infrastructure is generally invisible to most employees and managed under separate IT processes.
- **Review cadence.** Core Infrastructure tools are reviewed most frequently (highest exposure). AI Office Infrastructure is reviewed against operational reliability rather than employee-facing risk. Functional Tools sit between.
- **Procurement implications.** Core Infrastructure procurement typically includes enterprise SSO + data-residency + audit-trail requirements; Functional Tools may be approved with narrower compliance surface. The [[stack-composition-framework]]'s three lenses (composability, agent operability, reversibility) apply across tiers but with different weight per tier.

## Relationship to the [[shadow-ai-prohibition]]

The tier classification doesn't determine whether a tool is permitted — that's the AI Registry's job. *Every* AI tool used at Janus must be in the registry at *some* tier; tools outside the registry are Shadow AI regardless of tier they would have been classified at.

## Watch for

- **Tier-misclassification risk.** A Functional Tool used informally across multiple departments (e.g., a marketing-only tool spreading into Operations / HR) needs reclassification to Core Infrastructure with corresponding re-evaluation. The AIO surveillance pass catches these drifts.
- **Sub-tier within Functional Tools.** As Janus scales, "Marketing-only" and "HR-only" and "Finance-only" Functional Tools may need finer-grained tier breakdown by department + role.
- **The "Embedded AI" classification gap.** AI features inside non-AI tools (Notion AI, Slack AI, Linear AI) don't fit cleanly into the three tiers — they ride on a Tool but are themselves a separable AI capability. Worth a §5.3.x clarification at next policy iteration.
