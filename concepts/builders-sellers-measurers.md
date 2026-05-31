---
type: concept
title: Builders, sellers, measurers (Drucker's role trichotomy applied to AI restructuring)
slug: builders-sellers-measurers
created: 2026-05-21
updated: 2026-05-31
departments: [ai-office, marketing, hr, office-of-ceo]
status: active
sources: [2026-05-21-prince-cloudflare-measurers-replaced, anthropic-labor-market-impacts-2026-03, 2026-03-31-block-from-hierarchy-to-intelligence, 2026-04-24-yc-diana-hu-ai-native-company-from-ground-up, 2026-05-21-yc-blomfield-self-improving-company]
related: [ai-native-mandate, ai-native-enterprise-restructuring, agentic-lean-marketing-stack, ai-native-janus-positioning, stack-composition-framework, andrew-soane, observed-exposure-ai-labor-measure, recursive-self-improving-loop]
---

# Builders, sellers, measurers

Peter Drucker's three-role decomposition from *The Practice of Management* (1954), reinvigorated in 2026 by Matthew Prince's Cloudflare layoff-and-grow piece ([[2026-05-21-prince-cloudflare-measurers-replaced]]) as the operating lens for *which* enterprise roles AI displaces vs *which* roles it amplifies.

## The trichotomy

- **Builders** — create products. Engineers, designers, content creators, anyone whose output is a thing the company sells or uses. Output is *measurable in itself*.
- **Sellers** — sell those products. Account executives, business development, partner managers, customer-facing reps. Output is *revenue*.
- **Measurers** — everything else: internal audit, revenue recognition, finance, legal, compliance, middle management, operations. Output is *information about the business*.

## Parallel role taxonomy — IC + DRI (added 2026-05-31)

Two adjacent role taxonomies surfaced in 2026 land on a similar shape, and the YC consolidation is converging on **IC + DRI** as the two non-negotiable roles in an AI-native company:

| Source | Role taxonomy | Notes |
|---|---|---|
| **Drucker / Cloudflare-Prince** (this concept) | Builders / Sellers / Measurers | The work-shape decomposition. Says *what* AI absorbs (measurer work) vs *what* AI amplifies (builder/seller). |
| **Block "From Hierarchy to Intelligence"** ([[2026-03-31-block-from-hierarchy-to-intelligence]]) | ICs / DRIs / Player-coaches | The headcount-shape decomposition that *follows* once measurer work is absorbed. |
| **Diana Hu / YC** ([[2026-04-24-yc-diana-hu-ai-native-company-from-ground-up]]) | IC / DRI / AI-founder-type | Same as Block + an "AI-founder-type" archetype for the dogfooding founder. |
| **Tom Blomfield / YC** ([[2026-05-21-yc-blomfield-self-improving-company]]) | IC + DRI | Drops Diana's third role explicitly: *"Jack Dorsey has three. I actually don't like the third one, so I deleted it."* |

The two taxonomies answer different questions and pair cleanly. **Drucker says which work AI absorbs; IC + DRI says which roles remain.** Operationally:

- **Builders ↔ ICs.** Every retained IC is a builder. The IC role in AI-native vocabulary is *"a builder, an operator"* (Blomfield) who *"comes to meetings with working prototypes, not pitch decks"* (Diana Hu).
- **Sellers ↔ ICs (with edge-case judgement).** Sellers also remain — Diana and Blomfield both keep human salespeople for trust-building / high-stakes conversations. In the IC + DRI vocabulary, sellers are ICs operating on the **edge** where the company makes contact with reality (Block's framing). The role doesn't have a dedicated name in the YC vocabulary; it's an IC variant.
- **Measurers → absorbed into the loops.** The work the measurer role used to do (status rollups, audit, revenue recognition, compliance reporting, coordination) is precisely the work the [[recursive-self-improving-loop]] absorbs. *"Status, decisions, and outcomes are continuously captured and fed back into this intelligence layer"* (Diana Hu) is the literal description of measurer-replacement.
- **DRI is the non-substitutable role.** Each outcome has one named human responsible. Diana: *"One person, one outcome, no hiding."* Blomfield: *"a named human, not a committee."* This is the accountability layer the loops cannot generate on their own — they need a designated edge-position human to hold the can if the loop produces a bad result.

Three independent landings of **"DRI"** as a role name in 60 days (Block, Diana Hu, Blomfield — and the lineage is Apple-heritage via Block, propagating through YC). Strong evidence the vocabulary is stabilising. Worth absorbing into Janus operating language alongside or instead of bespoke owner-naming ([[ai-native-enterprise-restructuring]] flags this as an operational implication).

All three are critical to a functioning business. The question is which scales linearly with revenue and which scales sub-linearly when AI is introduced into the workflow.

## The 2026 update

Prince's claim (Cloudflare, 2026-05-21):

> "AI isn't coming for builders or sellers, but it is coming for measurers. Tireless, independent, efficient and available, AI systems can now measure an organization with a level of objective detail and precision that was previously impossible even for the best employees."

Cloudflare laid off >20% of staff *while* growing >30% in revenue. Per Prince, the vast majority of the layoffs were measurers — middle managers, ops consolidated into a single AI-supported group, marketing measurers, finance automation. No reduction in builders or sellers; in fact, record open positions for those roles plus 1,111 paid internships (1M applicants), all builders or sellers.

The structural argument: builders' marginal productivity *increases* with AI ("if an engineer can be 10× as productive, I'll hire as many as I can find"); sellers' marginal value *also increases* because the bottleneck is human-trust-building, which AI doesn't substitute for; measurers' marginal value *decreases* because their core function — observe, audit, report — is exactly what tireless, independent, available AI is best at.

## Why this matters at Janus

The frame validates and clarifies the [[ai-native-mandate|AI-native operating mandate]]:

1. **Headcount mix moves toward builders + sellers.** Andrew's 2026 hiring plan ([[andrew-soane]]) — 8-9 hires, "nearly all marketing roles, not technical" — *is* a builder-and-seller-weighted hire plan. The marketing team's output is the campaigns / content / positioning that creates demand (sellers + builders); the operational measurement of that demand is increasingly run by [[agentic-lean-marketing-stack|MCP-native tooling operated by one engineer]].
2. **The AIO itself is the measurer-replacement layer.** The systems the AI Office is building — Linear AIR for tool registry, Monday for execution tracking, [[janus-prime-radiant-build|Janus Prime Radiant]] for institutional knowledge, the [[standup]] pipeline for daily auditability — are precisely the *organisational measurement* surfaces Drucker described. Janus is not eliminating measurement; it's eliminating the human-measurer headcount that previously was the only way to do it.
3. **Cross-domain Prime Radiant rollouts apply the same logic per department.** Each Prime Radiant instance (Marketing, HR, Finance, IT/Ops, Office-of-CEO, Engineering, Training, ISO) is the measurer-replacement substrate for its domain. The federation layer ([[entities/departments/]] + the [[peer-to-peer-mesh-federation-pattern]]) is what makes the measurer-replacement *coherent across* the organisation rather than per-silo.
4. **Stack-composition decisions inherit the lens.** The [[stack-composition-framework]]'s "agent operability" lens is the *how* — agent-operable tools let one engineer support the surface that previously needed a multi-person ops team. That engineer is a builder; the team-they-replace was measurers.

## The cross-industry signal

By Q2 2026 the same frame is being articulated across enterprise:

- **JPMorgan (Dimon, 2026-05-21)** — "more AI people and fewer bankers" delivered through natural turnover (10% annual attrition = 25,000-30,000 departures/year is the manageable substrate). Backed by McKinsey estimate that ~30% of finance-and-insurance hours could be automated by 2030; Citi research showing >50% of banking jobs high-potential for replacement or augmentation. ([[2026-05-21-dimon-jpmorgan-more-ai-fewer-bankers]])
- **Standard Chartered (Winters)** — eliminating 8,000 "lower-value human capital" roles over 4 years. ([[2026-05-21-dimon-jpmorgan-more-ai-fewer-bankers]] context)
- **HSBC (Elhedery)** — AI will "destroy" certain roles while creating others; staff must adapt.
- **Goldman Sachs (Waldron)** — back-office operations as "a human assembly line" ripe for automation.
- **KPMG (Thomas, 2026-05-19)** — 276,000+ employees getting Claude access, Digital Gateway gets Cowork + Managed Agents; KPMG's *own* tax-agent build that used to take weeks now takes minutes. ([[2026-05-19-kpmg-claude-alliance]])

These are not isolated decisions; they're an industry-wide structural rebalance. The Drucker framing surfaced by Prince is now the most credible single explanation for *which jobs go and which jobs grow*.

## Empirical reinforcement — Anthropic's labor market paper (added 2026-05-23)

Anthropic's own *Labor market impacts of AI: A new measure and early evidence* ([[anthropic-labor-market-impacts-2026-03]]; Massenkoff & McCrory; 2026-03-05) provides empirical reinforcement that maps cleanly onto the Drucker frame. The paper's new *[[observed-exposure-ai-labor-measure|observed exposure]]* metric — combining theoretical LLM capability with actual Claude usage data — identifies the top 10 most-exposed occupations: **Computer Programmers (75%)**, **Customer Service Representatives**, **Financial Analysts**, **Data Entry Keyers (67%)**, and other roles that are largely the measurer-and-routine-builder mix Prince's frame predicts. At zero exposure: Cooks, Motorcycle Mechanics, Lifeguards, Bartenders, Dishwashers — physical / in-person service work, exactly the category the Drucker frame doesn't claim.

Three findings sharpen the frame:

1. **The BLS regression validates the directional claim.** A 10 percentage point increase in occupational AI coverage maps to a 0.6 pp drop in BLS-projected employment growth (2024-2034). The relationship is slight but exists — *and crucially, there is no such correlation using the Eloundou et al. theoretical-capability measure alone*. Theoretical capability and actual usage together are predictive in a way that either alone is not. This is empirical support for the proposition that the Drucker reset is happening at the job-task level, not as theatre.

2. **The high-exposure population skews older, female, higher-paid, more educated.** Workers in the top quartile of exposure earn 47% more on average, are 4.5× more likely to hold graduate degrees. This is *not* the population that gets sympathetic press in "AI takes jobs" narratives — these are the white-collar measurers Prince names directly. Operational use for Janus positioning: when Andrew or Bonaventure are asked about AI-driven labor displacement, the answer is that the affected population is the white-collar professional class, not the gig economy or the trades — and the AIO substrate is precisely the layer that re-routes that population's value into builder/seller-adjacent roles inside the firm rather than out of it.

3. **The young-worker hiring slowdown is the early canary.** No systematic unemployment increase in highly-exposed occupations since late 2022 — but a statistically marginal 14% drop in job-finding rates for **workers aged 22-25** entering exposed occupations. Echoes Brynjolfsson et al. (2025)'s 6-16% young-worker employment-fall finding. The Drucker frame predicts exactly this shape: incumbent measurers absorbed by natural attrition (Dimon's 10%/yr framing), but pipeline tightens at the entry point because junior measurer hires are the first to get substituted by AI. For Janus, this maps onto the [[andrew-soane|Andrew's]] hiring choice — explicitly biasing toward builder/seller roles instead of measurer-junior hires.

The empirical caveats matter: the relationships are statistically modest, the time horizon (2.5 years post-ChatGPT) is short, the data is US-only. But this is *Anthropic publishing on their own usage data* — a vendor-side transparency choice that gives the frame credibility independent of the Drucker-citing CEO class. Treat as the strongest first-party empirical evidence supporting the frame to date.

## Caveats and counter-considerations

- **Drucker's categories are leaky.** Some roles are partly builder, partly measurer (a senior engineer who also runs sprint planning; a senior marketer who also runs attribution). The frame is a *gradient*, not a binary classification. Edge cases will need judgment.
- **"Measurer" is not a value judgment.** Drucker himself argued measurement is critical to business; the question is *who* (or what) does the measurement, not whether to do it. A tireless AI auditor that audits *every* business risk continuously is doing the measurer's job *better*, not eliminating the function.
- **Builder-and-seller multiplication assumes a market that absorbs the extra output.** If Cloudflare doubles its builder count but the market can't absorb the additional product / customer acquisition, the marginal builder hire stops scaling. The frame holds for now because demand for AI-shaped products is the bottleneck-of-the-decade, not supply.
- **Political and social fallout.** Dimon explicitly warned "if it happens too fast" — accelerated transitions create labour-market dislocation, regulatory blowback, and the political backlash that bank execs (Winters, HSBC) are already navigating. Janus is small enough to sidestep most of this directly; the macroeconomic signal still shapes the policy environment any vendor operates in.

## Watch for

- Other CEO-level articulations of the same frame in Q2-Q3 2026; tracks whether builders-sellers-measurers becomes the standing executive-class vocabulary or stays a Prince-specific idiom.
- McKinsey, BCG, or Bain operationalising the frame into a service offering ("which of your roles are measurers, and how do we replace them?"). High likelihood given KPMG's preferred-partner-for-PE move with Anthropic.
- Pushback from the operations / finance professional communities (CPAs, internal auditors, MBA programs) — the frame is *threatening* to those constituencies and they'll articulate counter-positions worth tracking.
- Specific applications inside Janus: when each Prime Radiant instance is stood up, who does it free up *time-wise*, and what does that person now do (build / sell / something else)?

## Related

- [[ai-native-enterprise-restructuring]] — the strategic brief synthesising the 2026 Q2 cross-industry signal.
- [[ai-native-mandate]] — Janus's internal mandate; the Drucker frame is the *why* behind it.
- [[ai-native-janus-positioning]] — three-pillar positioning brief; the Society / Business / Individual spine maps onto Drucker's role frame (the Business pillar = builders + sellers retained, measurer-substrate AI-shaped).
- [[agentic-lean-marketing-stack]] — concrete instance of the frame applied to a single function (marketing).
