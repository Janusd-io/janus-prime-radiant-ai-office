---
title: "Level Up Your Agents: Announcing Google's Official Skills Repository"
source: "https://cloud.google.com/blog/topics/developers-practitioners/level-up-your-agents-announcing-googles-official-skills-repository"
author:
  - "[[Megan O'Keefe]]"
published: 2026-04-22
created: 2026-05-06
description: "Announcing Google's official Agent Skills repository, launched at Cloud Next 2026. Equip your AI agents with condensed, real-time expertise for Google Cloud products like BigQuery, GKE, and the Gemini API, avoiding context bloat."
tags:
  - "clippings"
---
Developers & Practitioners

##### Megan O'Keefe

Senior Staff Developer Advocate

As AI models improve, technical practitioners are increasingly turning to agentic AI tools to build with Google Cloud products, from Firebase and the Gemini API, to BigQuery and GKE. But how can you ensure that the model is equipped with **accurate, up-to-date information** about these technologies?

One way to do this is to plug your AI agent into a grounded, real-time information source. For instance, [Google offers a Model Context Protocol (MCP) server for its developer documentation](https://developers.google.com/knowledge/mcp). But heavily using MCP servers can cause a problem called “context bloat,” where huge amounts of context are loaded into the context window, confusing the model and racking up token costs.

We need a way to equip agents with additional, condensed expertise — and we can do this with [**Agent Skills.**](https://agentskills.io/home)

[Skills](https://agentskills.io/home) are “a simple, open format for giving agents new capabilities and expertise.” Think of a skill as compact, agent-first documentation for a specific technology or task. Skills are written in Markdown and can contain reference files, code snippets, and other assets. Agents load in skill information [only as-needed,](https://agentskills.io/what-are-skills#how-skills-work) reducing the risk of context bloat.

Today, on Day 1 of [Google Cloud Next 2026,](https://www.googlecloudevents.com/next-vegas/) we’re excited to announce the launch of Google’s official Agent Skills repository:

[**github.com/google/skills**](https://github.com/google/skills)

This repository is starting off with thirteen skills, focused on Google Cloud technologies:

- A selection of products**:** AlloyDB, BigQuery, Cloud Run, Cloud SQL, Firebase, Gemini API, and Google Kubernetes Engine (GKE).
- Three [**Well-Architected Pillar**](https://docs.cloud.google.com/architecture/framework) skills: Security, Reliability, and Cost Optimization
- “Recipe” skills for Google Cloud Onboarding, Authentication, and Network Observability.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/image_1_BwwkF6A.max-2200x2200.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/image_1_BwwkF6A.max-2200x2200.png)

Use `npx skills install ` [`github.com/google/skills`](http://github.com/google/skills) to install these skills to your agents of choice, including [Antigravity](https://antigravity.google/), [Gemini CLI](https://geminicli.com/), and third-party agents.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/agent_skills-2.max-2200x2200.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/agent_skills-2.max-2200x2200.png)

Stay tuned as we launch additional skills in this repo in the coming weeks and months!

Now get building!

Posted in