---
type: concept
title: Recursive self-improving loop
slug: recursive-self-improving-loop
created: 2026-05-31
updated: 2026-05-31
departments: [ai-office, engineering, office-of-ceo]
status: active
confidence: high
sources: [2026-04-24-yc-diana-hu-ai-native-company-from-ground-up, 2026-05-21-yc-blomfield-self-improving-company, 2026-03-31-block-from-hierarchy-to-intelligence, 2026-arxiv-harness-updating-not-harness-benefit]
related: [organisational-digital-twin, coordination-leverage-model, ai-native-enterprise-restructuring, ralph-loop-pattern, builders-sellers-measurers, ai-native-mandate, agentic-pipeline, sandbox-environment, agent-harness]
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

## Academic grounding — Harness Updating Is Not Harness Benefit (added 2026-06-02)

The academic literature on the **Learning** step of this loop is starting to formalise as *"harness self-evolution."* Lin, Wu, et al. (Penn State / UC Santa Cruz / Amazon / et al., 2026; [[2026-arxiv-harness-updating-not-harness-benefit]]) propose the disentangling vocabulary the engineering discussion has been missing:

- **Harness-updating capability** — a model's ability to produce *useful persistent harness updates* (skills, prompts, memories, tools) from execution evidence. Played by the **evolver** role in the loop. *"Surprisingly flat in base capability"* — Qwen3.5-9B's harness updates yield gains comparable to Claude Opus 4.6's.
- **Harness-benefit capability** — a model's ability to *benefit from updated harnesses* during task-solving. Played by the **task-solving agent** role. *"Non-monotonic in base capability"* — mid-tier models benefit most; weak-tier models benefit least (they fail to *invoke* harness artefacts or fail to *adhere* to them once loaded); strong-tier models hit the performance ceiling.

The paper's design guidance maps onto the YC five-part-loop architecture:

| Paper's recommendation | What it implies for the loop's Learning step |
|---|---|
| *"Allocate capability budget to the task-solving agent, not the evolver"* | The Quality-Gate + Sensor steps need the strongest model; the Learning step's evolver can be cheaper. Inverts the intuitive "use the best model for everything" default. |
| *"Bake harness invocation into agent training"* | Weak-tier models often fail to *load* the harness at all (25% load rate for Qwen3-32B vs ~96% for strong models). For AIO's purposes: the agents that *use* the AIO's skills (standup, ai-registry, ai-tool-evaluation) need strong harness-invocation discipline — not just strong base capability. |
| *"Strengthen long-horizon instruction following"* | Weak-tier adherence decays >4× more steeply across the trajectory than strong models. Long-running AIO loops (e.g., a closed lint workflow that runs overnight) need strong models or harnesses designed for adherence-recovery. |

**Implication for AIO's Learning-step build.** The proposed AIO closed-loop workflow (monitor agent watching `questions/` findings → proposes CLAUDE.md edits → review agent merges overnight) has a built-in role assignment that aligns with the paper's guidance:
- **Monitor / evolver** = mid-tier model is fine (harness-updating is flat in base capability). Cheap operating cost.
- **Review / task-solving agent** = strong-tier model required (harness-benefit needs ceiling-capacity for high-stakes wiki schema decisions). Higher operating cost, but justified.

This is also empirical support for the wiki's existing curator-pattern: Michael (strong-tier human reasoner) at the harness-benefit / task-solving role; the wiki's lint pass + standup skill (cheaper agentic execution) at the harness-updating role. The pattern Janus has been operating under is consistent with what the paper recommends — but now there's a citation. Worth carrying into outbound positioning when explaining why AIO's substrate works.

**Caveat.** The paper is preprint (2026, arxiv); evaluated on three benchmarks (SWE-bench Verified, MCP-Atlas, SkillsBench). Findings on Claude Opus 4.6 / Sonnet 4.6 / Haiku 4.5 specifically — directly relevant to Janus's stack. Treat as the strongest currently-available academic anchor for the AIO's loop-Learning-step design; expect follow-on work to refine the role-allocation guidance.
