---
type: concept
title: Shadow AI prohibition
slug: shadow-ai-prohibition
created: 2026-05-22
updated: 2026-05-22
departments: [ai-office, it-ops, iso, hr, office-of-ceo]
status: active
sources: [section-5-ai-charter-policy-v2.1]
related: [ai-policy, ai-registry, ai-tool-evaluation-framework, tool-tiers, ai-native-mandate, pilot-in-command]
---

# Shadow AI prohibition

Janus Digital strictly prohibits **"Shadow AI"** — the use of unverified or unauthorised AI tools. Codified in §5.3 of the [[ai-policy|AI Policy v2.1]]:

> "Only tools listed in the AI Registry are permitted for use. Employees who require a tool not currently on the approved list must submit a formal request to the AI Office for evaluation. Using unapproved alternatives to circumvent this process is a policy violation subject to disciplinary action."

## What "Shadow AI" covers

- **Any AI tool** (generative model, agent, automation, plugin, browser extension, mobile app) **not listed in the [[ai-registry|AI Registry]]**.
- **Public free-tier AI models** used with *any* company data — explicitly prohibited regardless of registry status (§5.7). The data-sovereignty rule and the registry rule reinforce each other.
- **Personal accounts on otherwise-approved platforms** that bypass enterprise SSO + data-residency controls. Approved tool, personal account = still Shadow AI.
- **Embedded AI features** in non-AI tools (e.g., the AI summarisation button in a productivity app that hasn't been through AI Registry evaluation). The tool itself may be approved, but a specific embedded AI feature may not be.

## The substitution path (how to *not* be in violation)

When an employee needs a tool that's not yet in the registry, the policy provides a specific path:

1. Submit a formal request via the `#ai-internal-hub` Slack channel.
2. The AI Office classifies the candidate (Tool / Infrastructure) and runs the [[ai-tool-evaluation-framework|Stage 1–4 evaluation]].
3. While the evaluation runs, the employee **does not use the candidate tool**. Other approved tools cover the use case in the interim, or the use case is deferred.
4. If approved, the tool is added to the AI Registry at the appropriate [[tool-tiers|tier]] and the employee gains sanctioned access.

The path is **not** "use the tool first, ask permission later." That's the failure mode the prohibition exists to prevent.

## Why this rule is non-negotiable

Three load-bearing reasons in the policy:

1. **Data sovereignty (§5.7).** Public / free-tier AI tools have no contractual data-privacy guarantee — Janus data fed into them may be used for model training, retained indefinitely, exposed in subsequent outputs to other users. The registry's vetting process verifies these guarantees at procurement.
2. **Security review (§5.4 Stage 4 Sub-Gate B).** Approved tools have passed IT Department review for SSO compatibility, network/firewall provisioning, licence terms, and L1 support ownership. Shadow tools bypass all of that.
3. **Accountability (§5.9).** [[pilot-in-command|Pilot in Command]] requires the employee to verify outputs, but verification depends on knowing the tool's documented failure modes — which only happens for tools that have been through evaluation. Using an un-evaluated tool means the PIC accountability frame can't hold.

## Surface in the Ai-native operating model

The prohibition is the *operational floor* of the [[ai-native-mandate|AI-Native Mandate]]: Janus is AI-first, but only through governed tooling. The [[ai-tool-evaluation-framework]] is the gate machinery; the registry is the surfaceable outcome; this prohibition is the rule that makes the registry binding rather than informational.

The complementary [[coordination-leverage-model|Coordination Leverage Model]] §6.1 specifically calls out: *"All approved tools are classified into one of three [[tool-tiers|tiers]]"* — meaning the prohibition does not say "no AI"; it says "no *ungoverned* AI."

## Enforcement surface

§5.3 specifies: *"Using unapproved alternatives to circumvent this process is a policy violation subject to disciplinary action."*

The Policy Compliance Notice at §5.10 footer escalates: failure to comply with the policy — particularly §5.7 Data Sovereignty, §5.5.2 Sandbox Data Restrictions, §5.9 Accountability — *"may result in disciplinary action, up to and including termination of employment."*

The Shadow AI prohibition sits at the intersection of §5.3 (registry) and §5.7 (data sovereignty). Both reinforcement vectors apply.

## Watch for

- **Embedded-AI surface expansion.** Productivity tools (Notion, Slack, Google Workspace, Linear) increasingly ship embedded AI features. Each new feature is a Shadow AI risk if it ships pre-evaluation. Worth a recurring AIO surveillance review.
- **Personal-account leakage.** Employees using approved tools (Claude, Cowork, etc.) on personal accounts bypass enterprise data controls. SSO enforcement via Microsoft Entra (per Principle 9 of the [[coordination-leverage-model]]) is the architectural counter.
- **Pace tension.** The substitution path takes evaluation time; some employees will perceive the friction as blocking productivity. The AIO's response (per the [[stack-composition-framework]] pre-filter) is to evaluate faster and reject faster — not to lower the bar.
