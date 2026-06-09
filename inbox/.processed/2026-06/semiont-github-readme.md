---
title: "The-AI-Alliance/semiont: Semiont supports human+ai collaborative knowledge work.  Use it as: a Wiki, Knowledge Base, Context Graph, Semantic Layer, or Agentic Memory."
source: "https://github.com/The-AI-Alliance/semiont"
author:
published:
created: 2026-06-08
description: "Semiont supports human+ai collaborative knowledge work.  Use it as: a Wiki, Knowledge Base, Context Graph, Semantic Layer, or Agentic Memory. - The-AI-Alliance/semiont"
tags:
  - "clippings"
---
## Semiont

**Semiont is an open, source-grounded semantic knowledge platform for building and maintaining trusted AI knowledge bases and context layers. It gives humans and AI agents a shared workspace and architecture to annotate, connect, enrich, and govern domain knowledge for accurate applications, agents, and workflows.**

[![Semiont screenshot](https://github.com/The-AI-Alliance/semiont/raw/main/website/assets/images/semiont-2026-03-10.png)](https://github.com/The-AI-Alliance/semiont/blob/main/website/assets/images/semiont-2026-03-10.png)

## Quick Start

### Start the browser

Install one of [Apple Container](https://github.com/apple/container), [Docker](https://www.docker.com/), or [Podman](https://podman.io/) if you don't already have one.

Run the published browser container image (substitute `docker` or `podman` for `container` as needed):

```
container run --publish 3000:3000 -it ghcr.io/the-ai-alliance/semiont-frontend:latest
```

Then open **[http://localhost:3000](http://localhost:3000/)** in your web browser.

For local-network access notes, supply-chain verification, the native [desktop app](https://github.com/The-AI-Alliance/semiont/releases) alternative, and frontend dev setup, see **[docs/browser/](https://github.com/The-AI-Alliance/semiont/blob/main/docs/browser/README.md)**.

### Start a knowledge base

Clone a knowledge base and follow its README. Each KB repo contains configuration, container definitions, and startup scripts under `.semiont/`.

#### Starting from scratch

| Template | Description |
| --- | --- |
| **[semiont-template-kb](https://github.com/The-AI-Alliance/semiont-template-kb)** | Empty template — start here for a new project |

#### Demo KBs

These ship a small corpus and a layered set of skills (ingest → mark → canonicalize → wire-edges → compose-aggregates) that demonstrate the SDK in a particular domain. The value is the *skills*, not the data — the skills are corpus-generic and work on any corpus dropped into the same directory layout.

| Knowledge Base | Domain |
| --- | --- |
| **[semiont-gutenberg-kb](https://github.com/The-AI-Alliance/semiont-gutenberg-kb)** | Public-domain literature from Project Gutenberg |
| **[semiont-arxiv-kb](https://github.com/The-AI-Alliance/semiont-arxiv-kb)** | Research papers from arXiv |
| **[semiont-legal-kb](https://github.com/The-AI-Alliance/semiont-legal-kb)** | Synthetic legal documents — contracts, attorney correspondence, internal memos |
| **[semiont-caselaw-kb](https://github.com/The-AI-Alliance/semiont-caselaw-kb)** | U.S. case law — Supreme Court opinions and state appellate cases |
| **[semiont-clinical-evidence-kb](https://github.com/The-AI-Alliance/semiont-clinical-evidence-kb)** | Synthetic clinical evidence — trials, observational studies, treatment guidelines, drug-safety reports |
| **[semiont-newsroom-kb](https://github.com/The-AI-Alliance/semiont-newsroom-kb)** | Synthetic investigative-journalism documents — interview transcripts, FOIA responses, public statements |
| **[semiont-household-kb](https://github.com/The-AI-Alliance/semiont-household-kb)** | Synthetic home-property records — service receipts, contractor emails, manuals, mortgage / insurance, HOA notices |

#### Community

| Knowledge Base | Domain |
| --- | --- |
| **[synthetic-family](https://github.com/pingel-org/synthetic-family)** | Synthetic family history and genealogy |

### Connect browser to knowledge base

In the Semiont browser's Knowledge Bases panel, enter host `localhost`, port `4000`, and the email and password you provided when starting the backend.

[![Connect to knowledge base](https://github.com/The-AI-Alliance/semiont/raw/main/website/assets/images/connect-kb.png)](https://github.com/The-AI-Alliance/semiont/blob/main/website/assets/images/connect-kb.png)

## Automate

Every operation in the GUI is available programmatically through three surfaces:

- **[Semiont SDK](https://github.com/The-AI-Alliance/semiont/blob/main/packages/sdk/README.md)** — type-safe TypeScript client (`@semiont/sdk`) for scripts, embeddings, and apps.
- **[Semiont CLI](https://github.com/The-AI-Alliance/semiont/blob/main/apps/cli/README.md)** — drive Semiont from the terminal.
- **[Agent Skills](https://github.com/The-AI-Alliance/semiont/blob/main/docs/protocol/skills)** — ready-made skill definitions for agentic coding assistants like Claude Code.

All three are organized around **[eight composable flows](https://github.com/The-AI-Alliance/semiont/blob/main/docs/protocol/flows/README.md)** — frame, yield, mark, match, bind, gather, browse, beckon — the same verbs whether driven by a human, a script, or an AI agent. See **[docs/protocol/](https://github.com/The-AI-Alliance/semiont/blob/main/docs/protocol/README.md)** for the protocol overview, design tenets, and value proposition.

## Contributing

> ⚠️
> 
> **Alpha.** API and package surface are not yet stable; breaking changes between 0.x releases are expected.

- **[Development docs](https://github.com/The-AI-Alliance/semiont/blob/main/docs/development/README.md)** — codebase layout, build status badges, Codespaces shortcut, where to read next.
- **[System architecture](https://github.com/The-AI-Alliance/semiont/blob/main/docs/system/README.md)** — actor model, knowledge system, container topology, package architecture.
- **[CONTRIBUTING.md](https://github.com/The-AI-Alliance/semiont/blob/main/CONTRIBUTING.md)** — branch/PR workflow, commit conventions, platform-contribution playbook.