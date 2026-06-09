---
type: source
title: "Building AI agents for the enterprise"
slug: anthropic-building-ai-agents-enterprise
created: 2026-06-08
updated: 2026-06-08
departments: [ai-office]
publisher: Anthropic
related: [anthropic, compounding-learning, agentic-ai, claude]
---

# Building AI agents for the enterprise

Anthropic. 23-page enterprise guide. Published 2026 (specific date not stated in document; estimated H1 2026 based on case-study data and product references). PDF distributed via Anthropic.

## Summary

A practical guide for enterprise AI transformation framed around three organisational pillars (employees, processes, products) plus a dedicated section on Claude Cowork deployment. Argues that "agentic thinking" — deploying AI systems that reason, plan, and execute multi-step workflows — is the divide between organisations that get incremental gains vs. transformation.

Defines the "agentic thinking divide": organisations treating AI as a chatbot (answers questions in isolation) vs. organisations embracing agentic AI (reasons through complex tasks, executes multi-step workflows, applies domain expertise). Concludes with an explicit compounding-advantage thesis: organisations that start earliest accumulate the largest advantage through trained teams, proven workflows, and encoded institutional knowledge.

## Key terms defined

- **Agent**: AI that plans, makes decisions, uses tools across multiple steps; selects the right tools; adjusts approach based on learning
- **Chatbot**: single-turn interactions; does not plan or follow through on multi-step tasks
- **Claude Cowork**: Anthropic's collaborative AI interface for non-technical knowledge workers; agent capabilities without custom build; local execution; produces finished deliverables (Word, Excel, slide decks)
- **Plugins**: packages of skills + context + connectors giving Claude role-specific expertise; built once, shared across org
- **Skills**: reusable predefined workflows; anyone can create custom skills

## Chapter 1: Upskilling employees

Core argument: the real gain comes when AI reflects how the organisation actually works — standards, terminology, tools, institutional knowledge. Generic AI produces generic output.

Key pattern: encode organisational context into plugins → any employee gets output that "feels like it came from an experienced colleague." Two companies using the same model get dramatically different results depending on how much context they give it.

**L'Oréal case study** (source: Thomas Menard, Head of Agentic Platform and LAB):
- Problem: employees needed custom dashboards for every data question; specialist bottleneck
- Solution: Claude-based multi-agent system (15+ specialised agents) transforms natural language queries into data insights + visualisations
- Results: 44,000 monthly users; 2.5M messages/month; 15,000 daily active users; conversational analytics accuracy 90% → **99.9%** with Claude
- Key metric: 99.9% accuracy on conversational analytics

## Chapter 2: Accelerating processes

Core argument: process automation is only as impactful as the context behind it. General-purpose output is not faster — it requires the same review cycles. The differential comes from building standards + institutional knowledge directly into the system.

**Compounding accuracy mechanism** (the most operationally relevant frame): organisations achieving the most dramatic gains build systems where human expertise feeds back into the AI's knowledge base. Each new process starts from the same baseline; but in a compounding AI system, every expert review makes every future process better. First-mover advantage compounds over time.

**Lyft case study:**
- Problem: riders/drivers waited 30–40 minutes for support; agents juggled 3–4 customers simultaneously; rigid workflows; agent burnout rising
- Solution: Claude-powered support AI for driver onboarding (region-specific requirements) + rider support (charge disputes, ride issues). Claude greets customers by name, investigates specific situation, resolves in seconds; escalates to agent with AI-generated conversation summary
- Results: support resolution time reduced **87%**; decision-making accuracy improved **30%+**; millions in savings reinvested into agent programmes; Lyft Silver (dedicated 1:1 support for older riders) launched

## Chapter 3: Transforming product development

Core argument: combine frontier model + proprietary data + existing trust relationships + domain expertise = product that competitors can't replicate. Defensibility comes from everything around the model, not the model itself.

**Trust boundary as first design constraint** (particularly for regulated industries): products that require client data to leave the firm's security perimeter stall in compliance review indefinitely. The trust boundary must be solved first, not as an afterthought.

**Rakuten case study** ("AI-nization" strategy):
- Problem: engineering talent consumed building and maintaining agent infrastructure; agents needed persistent compute, memory, storage; innovation bottlenecked by platform team
- Solution: adopted Claude Managed Agents (Anthropic's pre-built configurable agent harness) to offload the execution layer; specialist agents deployed within a week across engineering/product/sales/marketing/finance; native mobile/voice support; long-running agents (hours) allow delegating goals, not tasks; **agent memory compounds results — agents remember what went wrong and avoid repeating mistakes; individual learning becomes organisational learning instantly**
- Results: major releases every **2 weeks** (was once per quarter); initial critical errors down **97%** in pilot; agent cost + latency down 30%+ with no loss in output quality; "Galileo" power users contribute across domains beyond primary roles — a product manager independently builds FinOps pipelines, sets up ambient monitoring agents

## Chapter 4: Bringing Claude to the rest of your organisation — Claude Cowork

### What Claude Cowork is

Claude Code capabilities (complex multi-step agent workflows) made available to non-technical knowledge workers without a custom build. Employees set goals, delegate work, receive finished deliverables. Distinguished from prior examples (L'Oréal, Novo Nordisk, RBC) by not requiring custom engineering.

**Plugins** are the mechanism: packages of skills + context + connectors giving role-specific expertise. Built once, shared across org. Encodes tribal knowledge as organisational infrastructure. Anthropic has open-sourced 11 plugins: productivity, sales, finance, data, legal, marketing, customer support, product management, enterprise search, biology research, plugin management.

### Governance and enterprise design

- **Admin marketplace**: org-specific plugin catalog; IT controls which plugins are available/pre-installed/approval-gated; no shadow AI sprawl; reactive governance becomes proactive curation
- **Local execution**: Claude processes files + documents on the employee's machine; no cloud upload; addresses most common compliance objection for regulated industries
- **Auditability**: OpenTelemetry-compatible observability; compliance team can see exactly how AI is being used; audit trail for AI's involvement in specific decisions
- **Integration**: works within existing systems (CRM, document management, compliance tools); no new workflow context-switching
- **Continuity**: work moves between Claude Cowork and Excel/PowerPoint without losing context

### Three-phase deployment model

1. **Weeks 1–4** — Evaluation + success criteria: identify 2–3 pilot teams with clear pain points; install/build plugins encoding team standards; define measurable success criteria (e.g., "call prep time reduced 50%"; "contract review from 5 days to 1")
2. **Months 2–3** — Champion pilot: 2–3 teams in production workflows (not sandboxed); measure adoption weekly; collect qualitative + quantitative feedback; goal is proof-of-value, not perfection
3. **Months 4–6** — Scale: deploy admin marketplace controls; establish plugin review/approval workflows; broader rollout using refined plugins. Second wave moves faster than the first; third faster still — **"this is the compounding dynamic in action"**

### Key design principles

- Start with specificity, not scale
- Choose pilots with a measurable finish line
- Build plugins for reuse from the beginning (marginal cost of sharing a plugin = zero; marginal value = enormous)
- Never underestimate the governance layer — prerequisites for broad rollout, not post-adoption additions

## Chapter 5: Compounding the AI advantage

Core thesis: *"Teams moving to centralise AI within their operations now (vs treating agentic AI as an add-on layer) have a compounding head start: trained teams, proven workflows, institutional knowledge encoded in plugins, and a governance infrastructure that can support rapid expansion."*

*"Your organisation doesn't need a perfect plan. It only needs a specific starting point, quantifiable success criteria, and the willingness to learn from what happens next."*

## AIO relevance

- Validates [[compounding-learning]] from the vendor's own positioning document — the first Anthropic-published articulation of the compounding thesis in enterprise deployment terms
- **Trust boundary** framing is new vocabulary for the IAM/compliance layer in [[organisational-digital-twin]]
- Plugin/skills architecture described here is the same architecture AIO uses (Prime Radiant + Cowork + skills); this guide is the formal enterprise deployment manual for the pattern we're already running
- Rakuten's "agent memory compounds results" note validates the core institutional-memory bet
- Novo Nordisk: clinical study report documentation reduced from "10+ weeks to 10 minutes" — extreme end of process-acceleration case studies; relevant to how to pitch the Prime Radiant build timeline to department heads
- RBC: "2,200 advisors managing $689 billion in assets" — scale signal; relevant to financial-services clients
