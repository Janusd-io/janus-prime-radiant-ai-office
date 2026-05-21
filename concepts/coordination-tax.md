---
type: concept
title: Coordination tax
slug: coordination-tax
created: 2026-05-21
updated: 2026-05-21
departments: [ai-office, office-of-ceo]
status: active
sources: [2026-04-coordination-leverage-model-v0.3, 2026-04-coordination-leverage-model-v0.1]
related: [coordination-leverage-model, coordination-three-layer-model, organisational-digital-twin, builders-sellers-measurers, ai-native-mandate, agentic-lean-marketing-stack]
---

# Coordination tax

The overhead that grows superlinearly with organisational complexity and has historically been the binding constraint on scalable growth. The central primitive of the [[coordination-leverage-model]].

## Definition

As organisations grow, they accumulate management layers, reporting structures, status meetings, approval chains, information-routing functions, and context-translation activities that exist not to produce value directly, but to enable value-producing work to happen at scale. Only a small fraction of any company's activity directly produces value — building products, serving clients, closing deals. Everything else is coordination: making sure the right people have the right information at the right time to do the right work. That overhead is the tax.

## Why it scales superlinearly

Communication paths in a team grow as `n(n−1)/2`. Every additional person creates communication overhead with every existing person. Traditional management addresses this through hierarchy — creating intermediate nodes (managers) who aggregate and route information — but hierarchy introduces its own costs:

- **Latency** — information is delayed as it traverses layers.
- **Distortion** — information is simplified or filtered at each handoff.
- **Rigidity** — the structure itself becomes resistant to reconfiguration.

Geographic expansion compounds the tax multiplicatively. Each new country adds language, regulatory, timezone, and cultural dimensions to every coordination channel. The tax does not merely grow — it *grows multiplicatively* with geographical complexity. For Janus, this is the load-bearing constraint behind any multi-country expansion strategy.

## Why agentic AI changes the economics

Previous automation (ERP, workflow tools, RPA) automated *transactions* — structured, repeatable actions. Agentic AI is the first technology that automates *coordination itself*: the interpretation of context, the routing of information, the translation between domains, the synthesis of multiple inputs into coherent outputs, and the maintenance of institutional context across interactions.

The inversion: rather than building management layers to handle coordination overhead, organisations can deploy agents to perform the coordination function directly. The firm's cost structure shifts — the coordination tax is no longer proportional to headcount and geography; it becomes proportional to the capability and orchestration of the agent infrastructure. **The question is no longer "how many managers do we need to coordinate this work?" but "what coordination functions can agents perform, and what must remain human?"**

## Theoretical lineage

- **Ronald Coase (1937)** — "The Nature of the Firm." Firms exist because the transaction cost of coordinating work through markets exceeds the cost of coordinating it inside a firm. The firm is a coordination mechanism whose existence is conditional on its coordination cost being lower than the market's.
- **Peter Drucker (1954)** — *The Practice of Management.* "Only marketing and innovation produce results; everything else is cost." The "everything else" is largely coordination.
- **Frederick Brooks (1975)** — *The Mythical Man-Month.* `n(n-1)/2` communication paths. A general law of organisational complexity, not just a software-team observation.
- **Andy Grove (1983)** — *High Output Management.* Manager's output = output of their organisation + output of neighbouring organisations under their influence. Leverage = activities where intervention disproportionately increases the output of others.

(These lineage citations are in [[2026-04-coordination-leverage-model-v0.1]]; the current v0.3 draft strips them for a more business-direct voice.)

## Companion lenses

- **[[builders-sellers-measurers]]** (Drucker 1954 / Prince 2026) — the role-taxonomy lens on the same restructuring. Builders and sellers create value; measurers are coordination overhead. AI is coming for the measurer-role population because that's where the coordination tax concentrates.
- **[[coordination-three-layer-model]]** — the architectural lens. Individual / Department / Organisation layers are *where* the coordination tax sits and *which layer's tooling* reduces it.

## Application to Janus

The coordination tax is the binding constraint on Janus's multi-country expansion. The conventional answer — multidivisional structure with semi-autonomous country units, each carrying its own management layer — exists precisely *because* the coordination tax made tight integration across geographies historically more expensive than local duplication. The [[coordination-leverage-model]] argues that agentic AI inverts this trade-off, making tight integration cheaper than local duplication, *provided* the Layer-2 substrate is portable and the Layer-3 [[organisational-digital-twin]] is populated. The [[janus-prime-radiant-build|Prime Radiant rollout]] is the operational expression of that bet at Janus.

## Watch for

- The diagnostic for whether the tax is actually being displaced (per §8 of the framework): does **revenue per employee** increase as the organisation scales? If yes, the tax is being displaced. If revenue-per-employee is flat or declining as headcount grows, the AI investment is producing the appearance of transformation rather than the substance — the anti-indicator.
- Whether the framework's core claim — that AI automates coordination, not just transactions — holds as agents take on more consequential decisions. The §5 "Calibrate Agent Autonomy Per Task" principle is the safety valve.
