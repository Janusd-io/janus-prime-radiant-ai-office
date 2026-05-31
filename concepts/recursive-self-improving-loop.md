---
type: concept
title: Recursive self-improving loop
slug: recursive-self-improving-loop
created: 2026-05-31
updated: 2026-05-31
departments: [ai-office, engineering, office-of-ceo]
status: active
confidence: high
sources: [2026-04-24-yc-diana-hu-ai-native-company-from-ground-up, 2026-05-21-yc-blomfield-self-improving-company, 2026-03-31-block-from-hierarchy-to-intelligence]
related: [organisational-digital-twin, coordination-leverage-model, ai-native-enterprise-restructuring, ralph-loop-pattern, builders-sellers-measurers, ai-native-mandate, agentic-pipeline, sandbox-environment]
---

# Recursive self-improving loop

A canonical architectural primitive for AI-native operations: a closed-loop control system applied to a single business process, where the loop itself learns from its own failures and gets better over time without human intervention. Surfaced into a teachable founder-grade vocabulary in Q2 2026 via two Y Combinator batch talks ([[2026-04-24-yc-diana-hu-ai-native-company-from-ground-up|Diana Hu, 2026-04-24]] and [[2026-05-21-yc-blomfield-self-improving-company|Tom Blomfield, 2026-05-21]]). Diana Hu framed it in **control-theory** language (open-loop vs closed-loop); Blomfield framed it as a **five-part loop** with an explicit failure-fed-back-into-the-loop step.

## The five-part loop (Blomfield framing)

Every effective AI-native process follows this cycle:

1. **Sensor** — captures signals from the outside world (customer emails, support tickets, code changes, subscription cancellations, product telemetry, transcripts, system-of-record events).
2. **Policy** — defines what the system can do autonomously, what must escalate to a human, what must be logged.
3. **Tools** — deterministic APIs the AI can call (query the database, look up the calendar, post to Slack, file a Linear issue). Code; not LLM judgement.
4. **Quality gate** — evals, filters, safety checks, human review for high-risk actions.
5. **Learning** — when a step fails, the failure is captured and fed back into the loop so the next iteration is smarter. **This is the compounding step.** Without it, the loop is automation; with it, the loop self-improves.

Run every step with minimal human intervention and the loop *"gets better and better while you're sleeping"* (Blomfield).

## Closed-loop framing (Diana Hu)

Equivalent decomposition under control-theory vocabulary:

- **Open-loop system** — controlled but no feedback. Decision → execute → don't systematically measure outcome → don't adjust. *"Open loops are inherently lossy."*
- **Closed-loop system** — continuously monitors output, adjusts process to better meet the stated goal. *"Closed loops are extremely powerful for correctness and stability."*

Diana's anchoring claim: **with self-improving agents, your company should run as a closed loop.** Every important process gets a feedback mechanism; the "intelligence layer" at the centre of the company absorbs each iteration's outcome and tunes the next.

The two framings are isomorphic. The five-part loop is the implementation; closed-loop is the control-theory abstraction.

## YC's canonical worked example (Blomfield)

The proof point Blomfield gave for the recursive-self-improvement step:

1. YC has an internal agent with deterministic tools to query the YC database (e.g. *"who did I last meet from this batch?"*).
2. A **monitoring agent** sits on top of it and watches every query every YC employee runs.
3. When the original agent fails or produces a suboptimal result, the monitor asks *"why not — different tools? skills file update? database view? new index?"*
4. The monitor writes the fix, opens a merge request, a second review agent reviews and merges it overnight.
5. By the next morning, the same query that failed yesterday now succeeds.

*"That's not just AI making you 20 or 30% more valuable. It is the AI going through this loop to figure out how to self-improve."*

A second, longer-arc YC example: regenerating the **YC user manual** ([[2026-05-21-yc-blomfield-self-improving-company]]). 2,000 hours of office-hour recordings → diarised → categorised (fundraising, hiring, co-founder disputes, etc.) → synthesised into a fresh 150-page user manual in a weekend. Auto-updates monthly: every new piece of advice is compared with the existing manual and either incorporated or thrown away. The artefact is *both* the documentation and the context-injection for an AI advisor that gives founders *"the combined wisdom of 16 YC partners in one."*

## How this maps onto Janus AIO patterns

The five-part loop is a clean recognition of patterns the AIO is already running, named at the right level of abstraction to teach to other departments:

| Loop component | AIO instance (current) |
|---|---|
| **Sensor** | [[fireflies]] transcripts; [[linear]] AIR / AIP events; [[monday]] task changes; [[notion]] standup logs; inbox/ drops in Prime Radiant |
| **Policy** | CLAUDE.md trust-line (§5.1 low-stakes vs high-stakes); [[ai-policy]] §5.x rules; [[tool-tiers]] |
| **Tools** | `/standup`, `/ai-registry`, `/ai-tool-evaluation`, `/ai-tool-evaluation` subagent dispatch, Monday/Linear/Notion MCP servers, Cowork connectors |
| **Quality gate** | `questions/` escalations; lint pass (§5.3); attribution-confidence rule (§5.1 Meetings) |
| **Learning** | `lessons/`; `decisions/` (supersession chains); CLAUDE.md version bumps; the lint workstream that turns recurring findings into rule changes |

Each AIO pipeline (the [[ai-registry|Linear AIR pipeline]], the [[standup]] flow, the wiki-ingest workflow this very page exists inside) is one instance of the pattern. **The thing the AIO has not yet automated is the *fifth* step — fully-automated learning.** Today's "learning" step still routes through Michael as curator. Closing the fifth step (e.g., a monitor agent that watches lint findings → proposes CLAUDE.md edits → another agent reviews and merges overnight) is what would convert AIO from an *assisted* loop into a *self-improving* one in the Blomfield sense.

## Relation to other concepts on this wiki

- **[[organisational-digital-twin]]** — the twin is the *substrate* the loop operates against. Closed loops without a queryable model of the company are blind; the twin without loops is inert. They co-evolve.
- **[[coordination-leverage-model]]** — the loop is the mechanism by which coordination cost decreases per cycle. Each loop iteration that runs without human intervention is a unit of measurer-work removed.
- **[[ralph-loop-pattern]]** — Ralph is a *runtime* loop pattern for single-agent execution (deliberate context rotation; failures evaporate). The recursive self-improving loop is a *business-process* loop pattern (multiple agents; failures captured + fed back). Different scope; complementary discipline.
- **[[builders-sellers-measurers]]** — Drucker's measurer work is what gets absorbed inside the loops. Builders and sellers operate *between* loops, designing them and supervising the failure cases the quality gate kicks out.
- **[[ai-native-mandate]]** — the loop is the operational expression of the mandate. "AI-native" without loops is a vibe; with loops, it's a process discipline.

## Operating-model implications surfaced by the YC talks

- **"Software is ephemeral, context is durable."** Blomfield's most contrarian framing. Internal dashboards / one-off tools should be treated as disposable; the durable artefact is the *context* — recordings, transcripts, structured operating instructions. When a stronger model lands (months later), regenerate the software against the same context.
- **"Burn tokens, not headcount."** Diana frames it as the API bill being *"uncomfortably high"* because it's replacing far-more-expensive headcount. Blomfield reports YC seeing ~5× more revenue per employee at demo day than 18 months ago. Operationally: the AIO should expect token spend to rise faster than payroll for the next 12-24 months and that's the intended shape.
- **"Make the entire organisation legible to AI."** Both talks converge here. *"If it didn't get recorded, it didn't happen to your intelligence."* Direct mandate to maximise the [[organisational-digital-twin|sensor network]] coverage — every meeting transcribed, every DM channelled, every decision artefact-producing.
- **IC + DRI** as the two roles that remain. Diana adds a third ("AI founder type" — the at-the-front founder dogfooding the tools); Blomfield drops it (*"I actually don't like the third one, so I deleted it"*). Either way, **middle management is the role that disappears.** See [[ai-native-enterprise-restructuring]] for the operating-model implications across the Janus organisation.

## Provenance — the Dorsey → Block → Diana → Blomfield chain

The vocabulary did not spring up at YC. The transcripts make the chain explicit:

- **Jack Dorsey** posted a series of tweets around late April / early May 2026 articulating the "company-as-intelligence-not-hierarchy" framing. Both YC talks name-check Dorsey directly.
- **Block / Sequoia, "From Hierarchy to Intelligence"** ([[2026-03-31-block-from-hierarchy-to-intelligence|essay]], 2026-03-31 publish date; surfaced via inbox 2026-05-31) is Dorsey's company's formal articulation of the architecture.
- **Diana Hu's YC talk** (2026-04-24, [[2026-04-24-yc-diana-hu-ai-native-company-from-ground-up]]) introduces the **closed-loop / queryable-organisation** framing and names Jack-at-Block as the canonical Fortune-500 instance.
- **Tom Blomfield's YC talk** (2026-05-21, [[2026-05-21-yc-blomfield-self-improving-company]]) *"based a little bit off a talk Diana gave"* + Dorsey's tweets, formalises the five-part loop and drops Diana's third role.

This is the canonical pattern of how Fortune-500-scale architectural framings become founder-grade playbooks: primary essay → tweet-thread distribution → accelerator distillation into a teachable batch talk. **YC's role is the propagation channel**, not the originator. Worth noting for [[ai-native-janus-positioning|Janus's positioning]] — the consensus is now propagating through founder networks, not just through enterprise-IT trade press.
