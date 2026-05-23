---
type: concept
title: Observed exposure (Anthropic's AI-labor displacement measure)
slug: observed-exposure-ai-labor-measure
created: 2026-05-23
updated: 2026-05-23
departments: [ai-office, hr, marketing, office-of-ceo]
status: active
sources: [anthropic-labor-market-impacts-2026-03]
related: [builders-sellers-measurers, ai-native-enterprise-restructuring, anthropic, claude]
---

# Observed exposure (Anthropic's AI-labor displacement measure)

A new task-and-occupation-level measure of AI displacement risk, introduced by Anthropic in **Labor market impacts of AI: A new measure and early evidence** (Maxim Massenkoff & Peter McCrory; published 2026-03-05, corrections 2026-03-08). Source filed at [[anthropic-labor-market-impacts-2026-03]].

## What it is

A composite metric of *how exposed* an occupation is to AI displacement, built from three data sources:

1. **O\*NET task taxonomy** — ~800 occupations decomposed into tasks (US Labor Department database).
2. **Anthropic Economic Index usage data** — what Claude is actually being used for in production, broken down by task category. Drawn from the previous two Economic Index releases (August 2025, November 2025 usage).
3. **Eloundou et al. (2023) theoretical-capability scores (β)** — for each task, whether an LLM could *in theory* double its execution speed. β = 1 if LLM alone could do it; 0.5 if LLM with tools could; 0 otherwise.

A job's **observed exposure** is high if:
- Its tasks are theoretically capable for an LLM (high β).
- Its tasks see substantial usage in the Anthropic Economic Index.
- The usage is **work-related** (not recreational).
- The usage is **automated** (full weight) rather than **augmentative** (half weight).
- The AI-impacted tasks make up a *larger share of the overall role* (i.e., not just a 5% sliver).

Task-level coverage is then aggregated to the occupation level, weighted by share of time spent on each task. Mathematical details in the paper's [appendix](https://cdn.sanity.io/files/4zrzovbb/website/e5f77fc0e77c0185110b5e4b909602791ae76eae.pdf).

## Why the metric is different

Prior labor-impact measures (Eloundou et al. 2023; Brynjolfsson et al. 2025; Hampole et al. 2025) either:

- Measure *theoretical* AI capability without observed-usage validation (e.g., Eloundou), which historically over-estimates real-world disruption (the offshorability literature is the cautionary tale — Blinder 2009 estimated ~25% of US jobs were vulnerable, but a decade later most of those jobs had healthy employment growth).
- Measure *adoption-driven outcomes* (employment, postings, wages) without grounding in the technical capability boundary (e.g., Brynjolfsson, Hampole), which struggles to separate AI effects from business-cycle noise.

Observed exposure threads the needle: theoretical capability sets the upper bound, *actual platform usage* anchors the measure to what is happening *now*, and the weighting toward automation / work-related uses prioritises the displacement-relevant signal. The result is a measure that the authors claim will get *more* predictive over time as platform usage data accumulates.

## Key findings from the May 2026 release

- **AI is far from its theoretical capability.** For Computer & Math occupations (β = 94% of tasks theoretically feasible), Claude usage currently covers only 33% of those tasks. The blue area (theoretical) dwarfs the red area (observed) across most occupational categories. *The gap closes over time as adoption deepens.*
- **Top 10 most-exposed occupations:** Computer Programmers (75%), Customer Service Representatives, Data Entry Keyers (67%), Financial Analysts, and other clerical / programmable / routine-knowledge roles. This is the white-collar professional measurer-and-routine-builder mix — see [[builders-sellers-measurers]] for the related framing.
- **Zero-exposure population (~30% of US workers):** Cooks, Motorcycle Mechanics, Lifeguards, Bartenders, Dishwashers, Dressing Room Attendants. Physical/in-person service work.
- **BLS-projection validation:** Occupations with 10pp more coverage have 0.6pp lower BLS projected growth (2024-2034). Slight but *real*; importantly, the Eloundou theoretical measure alone shows *no* such correlation. The composite metric is doing predictive work neither input alone does.
- **Worker characteristics of the high-exposure group:** older, female, higher-paid (47% more on average), more educated (4.5× more likely to hold graduate degrees). The exposed population is the white-collar professional class.

## Key findings on unemployment & hiring

- **No systematic unemployment increase** in highly-exposed occupations since late 2022 (the ChatGPT release). The framework can detect differential unemployment increases of ~1 percentage point in the most-exposed quartile, and finds the post-ChatGPT change is *flat or slightly negative* (i.e., the exposed group's unemployment is not measurably higher). This holds across multiple cutoff variations and alternative data sources (Department of Labor UI claims).
- **Tentative young-worker hiring slowdown.** A 14% drop in job-finding rates for workers aged 22-25 entering exposed occupations, post-ChatGPT vs 2022 baseline. *Barely* statistically significant. No such decrease for workers older than 25. Echoes Brynjolfsson et al. (2025)'s 6-16% young-worker employment fall.

Implication: the soft-landing scenario (no aggregate displacement, but the *pipeline tightens at the entry point*) is the empirically-supported one as of mid-2026. This is consistent with the Drucker frame — incumbent measurers absorbed by natural attrition, junior measurer hires substituted by AI.

## Why this matters at Janus

1. **Empirical anchor for [[ai-native-enterprise-restructuring]].** The brief's thesis (AI restructures by displacing measurers, amplifying builders and sellers) gets a first-party-data backbone. Cite Anthropic's own paper rather than just CEO op-eds when explaining the position to risk-sensitive audiences.

2. **Operating-language for AIO positioning.** "Observed exposure" is a precise technical metric the AIO can reuse when discussing displacement risk inside Janus and with clients. Distinct from vague "AI is taking jobs" — gives a structured way to point at *which* jobs and *how much*.

3. **Direct application to per-department Prime Radiant rollouts.** When standing up a new instance (HR, Finance, IT/Ops, Engineering), the observed-exposure framework gives a methodology for *which roles in that department are most exposed* and therefore *where the measurer-replacement substrate has highest leverage*. The AIO can run a department-level exposure-mapping pass as part of the Infrastructure-layer setup for each new instance (per [[prime-radiant-three-layer-architecture]]).

4. **Vendor-side transparency posture is itself a Janus asset.** Anthropic chose to publish this analysis — using their own usage data — at a moment when other vendors are quiet on labor impact. For [[bonaventure-wong|Bonaventure]]'s [[ai-native-janus-positioning|three-pillar positioning]], the Society pillar gains a credible vendor-side ally: "we standardised on the vendor that publishes on the labor question, not the one that won't."

## Caveats and limits

- **US-only.** The CPS data and BLS projections are US-specific. Application to Janus's Singapore / UK contexts requires the methodology to be replicated against local labor-force surveys — feasible but not done in this paper.
- **The unemployment finding is null, not negative.** "No systematic increase" is not the same as "AI is not displacing jobs"; it means displacement has not yet shown up in unemployment statistics. Other channels (slowed hiring, exit to other industries, return-to-school) may be absorbing the impact.
- **The young-worker finding is barely significant.** 14% drop is a meaningful effect size but the confidence interval grazes zero; needs more time-series data to confirm.
- **The Eloundou capability measure is fixed at early 2023.** Capability has materially advanced since then (Claude 4.6/4.7, GPT-5.5, Gemini 3.5 Flash); the *theoretical* upper bound is now higher than the metric assumes. The authors flag this as a known update direction.
- **Anthropic-platform usage is not all-AI-usage.** The measure under-counts to the extent that other vendors (OpenAI, Google, Cohere, open-source) are being used for tasks Claude isn't. The trend may be more accurate than the level.

## Watch for

- **Updated releases.** Anthropic positions this as "a first step" and "easy to update as new data on employment and AI usage emerge." Expect refreshed exposure scores every Economic Index cycle.
- **Replication on other vendors' platforms.** Google, OpenAI, Microsoft could each publish equivalents using their usage data. Comparison would significantly sharpen the metric.
- **Methodology extension to non-US labour markets.** Particularly relevant for Janus given the [[singapore-launch]] and UK expansion.
- **The young-worker signal evolution.** If the 14% drop strengthens with more data, the entry-point-pipeline-tightening thesis becomes the dominant near-term AI-labor story; if it dissipates, the soft-landing narrative survives.
- **Whether other CEOs or labor economists cite *observed exposure* specifically.** Adoption as a vocabulary signal — see if BLS, Treasury, IMF, OECD pick it up.

## Related

- [[builders-sellers-measurers]] — Drucker's role frame; observed exposure provides the empirical reinforcement for which roles fall into which Drucker bucket.
- [[ai-native-enterprise-restructuring]] — the strategic brief synthesising the Q2 2026 enterprise-AI signals; observed exposure is the first-party empirical evidence supporting the brief's central claim.
- [[anthropic-labor-market-impacts-2026-03]] — the source paper.
- [[anthropic]] — vendor entity; the paper's publication is itself a posture signal worth tracking on the vendor page.
