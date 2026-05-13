---
title: "How A2A and MCP work together: five integration patterns for building multi-agent systems"
source: "https://x.com/googlecloudtech/status/2047567704807346675?s=12"
author:
  - "[[@googlecloudtech]]"
published: 2026-04-24
created: 2026-05-06
description: "No organization will build every agent it needs from scratch. The real value comes from discovering agents  built by different teams, in dif..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HGprx10aoAAG2-p?format=jpg&name=large)

No organization will build every agent it needs from scratch. The real value comes from discovering agents built by different teams, in different languages, across different organizations. That's what A2A and MCP enable: A2A for agent-to-agent communication. MCP for agent-to-tool communication.

**By** [@addyosmani](https://x.com/@addyosmani) **and** [@Saboo\_Shubham\_](https://x.com/@Saboo_Shubham_)

At **Cloud Next 26**, we shipped the infrastructure that makes this integration practical at enterprise scale. Here are five integration patterns for building multi-agent systems with both protocols.

## Pattern 1: Agent Card Discovery

Before your agent can delegate to another agent, it needs to know that agent exists, what it can do, and how to communicate with it.

A2A solves this with Agent Cards. Every A2A-compatible agent publishes a JSON document at a well-known URL that describes its capabilities, authentication requirements, and rate limits. Think of it as an OpenAPI spec, but designed for agent-to-agent interaction rather than client-server communication.

In **Agent Development Kit (ADK)**, exposing your agent as an A2A server is a single configuration. It automatically generates the Agent Card from your agent's definition. Consuming a remote agent is equally straightforward through the RemoteA2aAgent component, which handles authentication, data serialization, error handling, and result streaming. From the coordinator's perspective, a remote agent built by another team in another language feels like a local one.

**Agent Registry** amplifies this. When you register agents in the central registry, other agents across your organization can discover them without knowing specific URLs. The registry becomes the service mesh for your agent ecosystem: a single place to find what capabilities are available, who maintains them, and how to access them.

![Image](https://pbs.twimg.com/media/HGppz3KaAAEalCm?format=jpg&name=large)

## Pattern 2: Delegated Specialization

The most common integration pattern is delegation: your agent encounters a task outside its expertise and hands it to a specialist.

This pattern builds on the [Coordinator-Dispatcher architecture](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/), but extends it across team and framework boundaries. The specialist doesn't need to be built with ADK. It doesn't need to be written in the same language. It doesn't need to be maintained by the same team. It just needs to speak A2A.

Consider a customer onboarding workflow that spans five teams and four languages. The coordinator (your team, Python) delegates identity verification to the security team's Go agent, credit assessment to the risk team's Java agent, account provisioning to the platform team's Go agent, compliance documentation to the legal team's Python agent, and welcome communication to the marketing team's TypeScript agent.

![Image](https://pbs.twimg.com/media/HGpqR5hbQAAjIMA?format=jpg&name=large)

Each specialist is owned by a different team, maintained independently, and deployed on its own schedule. The coordinator doesn't know or care about internal implementations. It only knows their Agent Card capabilities and the A2A protocol.

When the security team updates their verification agent to support new document types, no changes are needed in the coordinator. When the risk team improves their credit models, the coordinator automatically gets better assessments. Each team iterates independently, and the overall system improves. This is the same principle that made microservices successful: independent deployment, independent scaling, independent evolution. A2A provides the service contract that makes it work for agents.

## Pattern 3: Tool Bridge (Model Context Protocol)

While A2A connects agents to agents, MCP connects agents to tools and data. The Tool Bridge pattern uses MCP to give your agents secure access to data sources, APIs, and enterprise systems without building custom connectors for each one.

Without MCP, every data connection requires its own custom integration code. Your agent needs a Python connector for one REST API, a different connector for another database, yet another for a legacy system. Three data sources means three connectors to build, test, and maintain. MCP eliminates this by providing a single protocol that any tool can implement.

The [ADK integrations ecosystem](https://developers.googleblog.com/supercharge-your-ai-agents-adk-integrations-ecosystem/) provides more than 60 ready-to-use tools and integrations, such as GitHub, Notion, Hugging Face, AgentOps, and Stripe. These allow your agent to connect instantly through simple configuration, bypassing the need for lengthy custom development.

For database connectivity specifically, [MCP Toolbox for Databases](https://adk.dev/integrations/mcp-toolbox-for-databases/) connects over 30 different data sources to your agents through a single MCP interface. And Apigee API Hub takes this further: if you have existing REST APIs documented in Apigee, you can turn them into agent-accessible tools automatically. Your agents access data through the same governance layer that manages your existing API traffic. Rate limiting, authentication, logging, and access control are handled by infrastructure you already manage.

![Image](https://pbs.twimg.com/media/HGpqclbboAA1c_H?format=jpg&name=large)

ADK supports MCP natively. When you add an MCP tool to your agent, the agent discovers the tool's capabilities, invokes it with structured parameters, and receives structured responses. From the agent's perspective, an MCP tool through Stripe looks the same as an MCP tool through BigQuery. The protocol is the interface. The backend is interchangeable.

## Pattern 4: Cross-Organization Federation

The most ambitious pattern involves agents from different organizations collaborating on shared tasks. This is where A2A's open protocol design becomes essential, because you can't assume the other organization uses the same framework, language, or cloud provider.

Agent Gallery in Gemini Enterprise makes this practical. Over 100 validated partner agents from Adobe, ServiceNow, Workday, Salesforce, and others are available directly within the platform. Every partner agent has been validated by Google Cloud for security and interoperability.

The critical property is that each organization maintains its own governance. Your Agent Gateway policies control what data your agents can share with the partner agent, what actions they can take based on the partner's responses, and what information they can request. The partner agent operates under its own security model, validated by Google Cloud's integration requirements.

Consider a multi-agent payment workflow where your agent needs to coordinate with external merchant agents and financial service agents. Each party maintains its own governance while collaborating on shared transactions through A2A. Your agent doesn't need to understand how the merchant's system works internally. It communicates through the A2A protocol, and each side enforces its own security boundaries independently.

![Image](https://pbs.twimg.com/media/HGpqmRvbMAAzzv0?format=jpg&name=large)

The same principle applies to any cross-organization integration. Your agent doesn't need to understand Salesforce's data model or ServiceNow's internal architecture. It delegates to the partner agent in Agent Gallery, which is maintained by the partner's team, validated by Google Cloud, and governed by your Agent Gateway policies. When the partner updates their platform, their agent is updated. Your system benefits without any changes on your end.

## Pattern 5: Ambient Event Mesh

The final pattern combines A2A with event-driven architecture to create a mesh of ambient agents that react to events continuously in the background, without waiting for user requests.

Batch and Event-Driven Agents in Gemini Enterprise Agent Platform connect directly to BigQuery tables and Pub/Sub streams. When you combine this with A2A, you create a network of agents that listen for events, process them, and delegate to specialist agents as needed - all running continuously in the background.

Each agent in the mesh runs independently. When an event arrives, the receiving agent processes it and decides whether to handle it locally, delegate to a specialist via A2A, or escalate to a human via Mission Control. The mesh is self-organizing - adding a new specialist agent (say, a fraud detection specialist) requires only registering it in Agent Registry and updating the routing logic in the relevant ambient agents.

![Image](https://pbs.twimg.com/media/HGpqvSbbMAACtZs?format=jpg&name=large)

This pattern is particularly powerful for organizations with high event volumes. A content platform processing millions of uploads per day, a financial institution processing millions of transactions, an e-commerce platform processing millions of customer interactions - all can use ambient agent meshes to handle the long tail of events that require intelligent processing.

The governance story is critical here. Every agent in the mesh has its own identity via **Agent Identity**. Every tool access is governed by **Agent Gateway**. Every interaction is traced through **Agent Observability**. The mesh is not a black box - it is a fully observable, governed network of specialized agents.

## Choosing the Right Pattern

When building multi-agent systems, choose your integration pattern based on the relationship between agents:

![Image](https://pbs.twimg.com/media/HGpq6c7bMAAEVFX?format=jpg&name=large)

**Get started today**

The interoperability stack is available now:

- A2A protocol: Supported in ADK across Python, TypeScript, Go, and Java
- MCP: Native support in ADK, managed support for GCP databases
- Agent Gallery: 100+ validated partner agents in Gemini Enterprise
- Native Ecosystem Integrations: Plug-and-play connectors for enterprise systems

The A2A + MCP codelab walks through building a multi-agent system with cross-language collaboration: [codelabs.developers.google.com/instavibe-adk-multi-agents](https://codelabs.developers.google.com/instavibe-adk-multi-agents)

ADK samples including multi-agent patterns: [github.com/google/adk-samples](http://github.com/google/adk-samples)

The companies building isolated agents will be refactoring in twelve months. The companies building interoperable agent ecosystems will be compounding their advantage every day.

Start building: [adk.dev](https://adk.dev/) | [https://cloud.google.com/products/gemini-enterprise-agent-platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)

**Build Interoperable Agents: Google for Startups AI Agents Challenge**

Isolated agents are a dead end. Join our **6-week global challenge** for startups to build, optimize or refactor AI Agents on the Gemini Enterprise Agent Platform. You'll get **$500 in cloud credits**, full platform access and a shot at the **$90,000 prize pool**.

[Sign up today to start building](https://devpost.team/hackathon_guest_invites/4fb181b4-2722-415d-a442-285a57dcaba5?utm_source=twitter&utm_medium=social&utm_campaign=google-for-startups-ai-agents-challenge&utm_content=twitter-post)!