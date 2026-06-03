---
type: source
source_type: meeting
title: The Founder's Blueprint: Architecting Agentic AI on AWS
slug: 2026-06-02-founders-blueprint-agentic-ai-on-aws
created: 2026-06-02
captured_by: jehad-altoutou
fireflies_id: 01KT3GFTRPCK4BQMJD0H73VA56
fireflies_url: https://app.fireflies.ai/view/01KT3GFTRPCK4BQMJD0H73VA56
attendees: [Jehad Altoutou, Michael Bruck]
duration_min: 72
audience: department
departments: [ai-office]
standup_skill_version: v3.23
parser_version: 3
related: [agentic-ai, agentic-harness, agent-platform-evaluation, stack-composition-framework]
---

# The Founder's Blueprint: Architecting Agentic AI on AWS

## Source Context

Michael Bruck and Jehad Altoutou attended this AWS / SUDO Consultants / Ignyte event on 2 Jun 2026. The public event framing presented it as a founder-oriented session on architecting agentic AI on AWS, with a promised live demo rather than slide-only content. The Fireflies transcript shows the actual session was closer to a mixed AWS startup-programme briefing, partner-credit pitch, high-level AWS AI platform overview, and two generic agentic workflow demos.

Curator assessment from Jehad: low practical value. The speakers did not appear to have strong technical command of the subject, and the session should not be treated as authoritative architectural guidance. File this as a weak signal and vendor-positioning note, not as a design reference.

## Digest Summary

The session opened with AWS startup positioning: move quickly, avoid simple wrappers, use domain expertise as defensibility, manage model cost, and prefer Bedrock for model access before moving to SageMaker for custom model work. SUDO Consultants then presented AWS partner programmes for startups, including migration/build support, AI assessments, free or subsidised proofs of concept, DevOps support hours, architecture optimisation reviews, and AWS credits. The technical section positioned AWS AgentCore as infrastructure for running agent applications with identity, memory, policy controls, observability, API gateway abstraction, container deployment, and enterprise security. The demos covered resume-processing agents for recruitment and contract-analysis agents for legal documents.

The useful knowledge is mostly comparative: AWS is packaging "agent infrastructure" around the same concerns Janus has already identified in the Prime Radiant / agent-harness workstream - identity, gateway abstraction, observability, policy boundaries, model independence, deployment packaging, human-in-the-loop checkpoints, and cost control. The event did not materially change the AIO architecture direction.

## Claims Worth Preserving

- **Bedrock as model-router abstraction.** AWS positioned Bedrock as a single interface to multiple models, including Anthropic Claude and future OpenAI model availability, with model switching handled primarily by changing model selection rather than application logic.
- **Nova for cheaper basic tasks.** AWS positioned Amazon Nova as a lower-cost model family suitable for simpler tasks where latest frontier models are unnecessary.
- **SageMaker for deeper custom model work.** SageMaker was described as the next step when a startup needs to train, fine-tune, or build custom models rather than consume hosted foundation models.
- **AgentCore as packaged harness infrastructure.** The technical pitch described AgentCore as providing identity, memory, policies, observability, gateway controls, deployment support, security, and cost-performance optimisation around agents.
- **Gateway abstraction matters.** AgentCore Gateway was presented as an API abstraction layer: agents call the gateway instead of external APIs directly, which gives visibility, policy enforcement, and easier switching between downstream services.
- **Human-in-the-loop remains necessary.** The legal and payment examples both used human approval as a checkpoint for sensitive or critical actions.
- **AWS credits and partner support exist, but are conditional.** SUDO described startup access to AWS credits and services, including up to USD 100,000 in credits for eligible VC-backed startups, smaller distributor-linked credits, and migration/build support.

## Claims To Treat With Caution

- The transcript contains multiple garbled or imprecise technical statements, so do not rely on it for implementation detail.
- The speakers mixed marketing claims, AWS partner incentives, and architecture framing. Separate "AWS can help you build this" from "this is the right architecture."
- The AgentCore claims need verification against official AWS documentation before any Janus build decision.
- The cost and credit claims should be verified directly with AWS / SUDO / Redington before being used in procurement or planning.

## Relevance To Janus

### Agent harness / platform direction

The event reinforces, but does not originate, the need for an agent harness layer with:

- model routing
- tool/API gateway abstraction
- identity and access controls
- observability
- policy boundaries per agent
- human approval checkpoints
- deployment packaging
- cost controls

This maps to [[agentic-harness]], [[agentic-ai]], [[stack-composition-framework]], and the existing Monday parent "Agent Platform Evaluation".

### Prime Radiant / organisational digital twin

AWS's examples were generic, but the same pattern applies to Prime Radiant: agents should not call every system directly. A gateway or policy layer between agents and Monday, Linear, Fireflies, Slack, GitHub, and Obsidian would make actions observable, governable, and easier to swap later.

### Vendor evaluation posture

AWS should be treated as a potential infrastructure provider for agent deployment and orchestration, not as proof that Janus should move the agent stack onto AWS. The most important evaluation question is whether AgentCore materially reduces operational complexity without creating AWS lock-in or hiding the agent behaviour we need to inspect.

## Open Questions

- Is Amazon AgentCore generally available and mature enough for production use, or still primarily a partner/demo narrative?
- How does AgentCore compare with Janus's current lighter-weight stack: Prime Radiant, Codex/Claude skills, MCP connectors, Monday, Linear, and GitHub?
- Can AgentCore Gateway expose enough detail for audit, ISO, and governance requirements?
- Would AWS credits change the economics enough to justify a sandbox comparison?
- Does AWS's model-routing layer offer anything we cannot already get through existing model gateways and direct provider APIs?

## Proposed Follow-Up

No automatic Monday task is required. If AIO wants a formal comparison later, attach a sub-item to Agent Platform Evaluation: "Compare AWS AgentCore / Bedrock against Janus agent-platform requirements."
