---
title: "The claude code tutorial level 2"
source: "https://x.com/eyad_khrais/status/2010810802023141688?s=12"
author:
  - "[[@eyad_khrais]]"
published: 2026-01-13
created: 2026-05-07
description: "This is the official Claude Code tutorial part 2, where I cover more advanced concepts that help you get even more out of Claude Code. If yo..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/G-fVmb6XEAE-TB7?format=jpg&name=large)

This is the official Claude Code tutorial part 2, where I cover more advanced concepts that help you get even more out of Claude Code. If you haven't read part one, I’d highly recommend it before you read this article. This builds directly on those fundamentals.

Part one went mega viral, but if you missed it, read it first here: [https://x.com/eyad\_khrais/status/2010076957938188661?s=20](https://x.com/eyad_khrais/status/2010076957938188661?s=20)

I've been a SWE for 7 years, between Amazon, Disney, and Capital One. The code I've shipped touches millions of users. Part one covered the basics that most people get wrong, but this post goes deeper into the systems underneath Claude Code that separate competent usage from exceptional usage.

There are 3 main capabilities that most people still don’t know how to use effectively, which are: skills, subagents, and MCP connectors. All of these capabilities are in the documentation, the only problem is that the documentation doesn't tell you how these pieces fit together in practice, or which configurations actually matter for real work.

What follows is everything I've learned about these systems after using them daily to build production software. Some of this took me weeks to figure out, while some through trial and error. Hopefully it saves you some time.

## The Context Window Problem

Before we get into the advanced features, there's something fundamental that affects everything else. If you're using multiple AI coding tools, you've probably assumed they all handle context the same way (spoiler alert: they don’t). According to a detailed comparison from Qodo's engineering team, Claude Code provides a "more dependable and explicit 200K-token context window," while Cursor's "practical usage often falls short of the theoretical 200K limit" due to "internal truncation for performance or cost management." The system applies internal safeguards that silently reduce your effective context. I cover why context is so important in part 1.

While you could get pissed at Cursor for having these limitations, you have to understand that different tools are optimized for different workflows. If you're working on large, interconnected codebases where you need the model to understand how your authentication system connects to your API routes and how that connects to your database schema, that context matters. So for larger projects I would recommend using Claude Code directly. Claude Code delivers the full 200K consistently.

This is also why the features I'm about to cover work so well in Claude Code specifically. Skills, subagents, and MCP connections all benefit from having predictable context to work with.

## Skills: Teaching Claude Your Specific Workflows

A skill is a markdown file that teaches Claude how to do something specific to your work. When you ask Claude something that matches a skill's purpose, it automatically applies it. The structure is dead simple.

1. Create a folder with a SKILL.md file: ~/.claude/skills/your-skill-name/[SKILL.md](http://skill.md/)
2. Or for project-specific skills that you want to share with your team: .claude/skills/your-skill-name/SKILL.md

Every SKILL.md starts with YAML frontmatter:

name: code-review-standards

description: Apply our team's code review standards when reviewing PRs or suggesting improvements. Use when reviewing code, discussing best practices, or when the user asks for feedback on implementation.

The description is critical. Claude uses it to decide when to apply the skill. Be specific about the trigger conditions. You can also explicitly tell Claude to “utilize x skill” and it will do so. But the goal is for Claude to recognize when it needs to utilize the skill on its own accord.

Below the frontmatter, write the actual instructions in markdown. Here's a minimal example:

\---

name: commit-messages

description: Generate commit messages following our team's conventions. Use when creating commits or when the user asks for help with commit messages.

\---

\# Commit Message Format

All commits follow conventional commits: - feat: new feature - fix: bug fix - refactor: code change that neither fixes nor adds - docs: documentation only - test: adding or updating tests

Format: \`type(scope): description\`

Example: \`feat(auth): add password reset flow\`

Keep the description under 50 characters. If more context is needed, add a blank line and then the body. It’s awkward to write in this format at first (since writing normally-sounding English sentences is your usual), but the difference in quality is noticeable.

The key architectural principle is progressive disclosure. Claude pre-loads only the name and description of every installed skill at startup (roughly 100 tokens each). The full instructions only load when Claude determines the skill that is relevant, which means that you can have dozens of skills available without bloating your context.

You can add supporting files to your skill folder. If you have extensive reference material, put it in a separate file and reference it in SKILL.md. Claude will read it only when needed.

Also important to note that skills aren't limited to just code. I've seen engineers build skills for:

- Database query patterns specific to their schema
- API documentation formats their company uses
- Meeting notes templates
- Even personal workflows like meal planning or travel booking

The pattern works for anything where you find yourself repeatedly explaining the same context or preferences to Claude.

To see what skills are currently loaded, ask Claude directly: "What skills do you have available?" It will list them (or go settings → capabilities → scroll down and you’ll see skills)

## Subagents: Parallel Processing With Isolated Context

A subagent is a separate Claude instance with its own context window, system prompt, and tool permissions. This is where Claude Code's architecture really differentiates itself. When Claude delegates to a subagent, that subagent operates independently and returns a summary to the main conversation.

It’s important to remember that context degradation happens around 45% of your context window. Subagents let you offload complex research or implementation tasks to a fresh context, then bring back only the relevant results, which means your main conversation stays clean.

Claude Code includes three built-in subagents:

**Explore**: A fast, read-only agent for searching and analyzing codebases. Claude delegates here when it needs to understand your code without making changes. When used correctly, Claude specifies thoroughness: quick, medium, or very thorough.

**Plan**: A research agent used during plan mode to gather context before presenting a plan. It investigates your codebase and returns findings so Claude can make informed architectural decisions.

**General-purpose**: A capable agent for complex, multi-step tasks requiring both exploration and action. Claude delegates here when the task needs multiple dependent steps or complex reasoning.

**Creating Custom Subagents**

Just like you need a custom skill, I would highly recommend creating your own custom subagents. Run /agents in Claude Code to see all available subagents and create new ones.

To create one manually, add a markdown file to ~/.claude/agents/ (user-level, available in all projects) or .claude/agents/ (project-level, shared with your team).

An exemplar structure:

\---

name: security-reviewer

description: Reviews code for security vulnerabilities. Invoke when checking for auth issues, injection risks, or data exposure.

tools: Read, Grep, Glob

\---

You are a security-focused code reviewer. When analyzing code:

1\. Check for authentication and authorization gaps 2. Look for injection vulnerabilities (SQL, command, XSS) 3. Identify sensitive data exposure risks 4. Flag insecure dependencies

Provide specific file and line references for each finding. Categorize by severity: critical, high, medium, low.

The tools field controls what the subagent can do. For a read-only reviewer, restrict to read, grep and glob commands. For an implementation agent, include write, edit, and bash commands.

**How Subagents Communicate**

This is the part most people miss. Subagents don't share context directly with each other, since they’re operating in isolation. Communication happens through the delegation and return pattern:

1. Main agent identifies a task suitable for delegation
2. Main agent invokes subagent with a specific prompt describing the task
3. Subagent executes in its own context window
4. Subagent returns a summary of findings/actions to main agent
5. Main agent incorporates the summary and continues

The summary is the key. A well-designed subagent doesn't dump its entire context back. This is why subagent descriptions and system prompts need to be explicit about output format.

For complex workflows, you can chain subagents. The main agent orchestrates:

Main Agent

|── Delegates research to Explore subagent │ └── Returns: "Found 3 relevant files: [auth.py](https://auth.py/), [middleware.py](https://middleware.py/), [routes.py](https://routes.py/)" |── Delegates implementation to custom implementer subagent │ └── Returns: "Added password reset endpoint, updated 2 files" └── Delegates testing to custom test-runner subagent └── Returns: "All 12 tests passing, coverage at 94%"

Each subagent gets fresh context for its specific task. The main agent only holds the summaries, not the full exploration history. This prevents the context pollution that kills long coding sessions.

One important constraint: subagents cannot spawn other subagents. This prevents infinite nesting and keeps the architecture predictable.

**Practical Subagent Patterns**

**Large refactoring**: Have the main agent identify all files that need changes, then spin up a subagent for each logical group. Each subagent handles its scope and returns a summary. The main agent never needs to hold the full context of every file simultaneously.

**Code review pipeline**: Create three subagents: style-checker, security-scanner, test-coverage and run them in parallel against a PR. Each returns findings in a consistent format → main agent synthesizes into a single review.

**Research tasks**: When you need to understand an unfamiliar part of the codebase, delegate to Explore with specific questions. It returns a distilled map of relevant files and patterns, keeping your main context focused on the actual implementation work.

## MCP Connectors: Never Leave Claude

MCP (Model Context Protocol) is a standardized way for AI models to call external tools and data sources through a unified interface instead of custom integrations for each one. You don’t have to go into github, you don’t have to go into slack, gmail, drive, etc.. You can get AI to “talk” to all of those through the Claude interface via an MCP server.

The command to add a connector:

\# HTTP transport (recommended for remote servers)

claude mcp add --transport http <name> <url>

\# Example: Connect to Notion

claude mcp add --transport http notion [https://mcp.notion.com/mcp](https://mcp.notion.com/mcp)

\# With authentication

claude mcp add --transport http github [https://api.github.com/mcp](https://api.github.com/mcp) \\

\--header "Authorization: Bearer your-token"

Or if you want the super simple route in the web app, you go settings → connectors → find your server → configure → give permissions and you’re set.

Some examples of what MCP servers have done for me in the last 6 months:

- Implement features from issue trackers: "Add the feature described in JIRA issue ENG-4521"
- Query databases: "Find users who signed up in the last week from our PostgreSQL database"
- Integrate designs: "Update our email template based on the new Figma designs"
- Automate workflows: "Create Gmail drafts inviting these users to a feedback session"
- Summarize Slack threads: "What did the team decide in the [#engineering](https://x.com/search?q=%23engineering&src=hashtag_click) channel about the API redesign?"

The power isn't any single integration.

A workflow that used to require five context switches (check the issue tracker, look at the design, review the Slack discussion, implement the code, update the ticket), now happens in one continuous session. You’re in flow state 24/7.

I’d recommend connecting the following MCP servers:

- **GitHub**: Repository management, issues, PRs, code search
- **Slack**: Channel history, thread summaries, message search
- **Google Drive**: Document access for reference during implementation
- **PostgreSQL/databases**: Direct queries without leaving Claude
- **Linear/Jira**: Issue tracking integration

To see your current MCP connections, run /mcp in Claude Code.

Third-party MCP servers aren't verified by Anthropic, so be careful. For sensitive integrations, review the server's source code or use official connectors from the service providers.

## The Compound Effect

Here's where this all comes together. A skill that knows your codebase patterns + a subagent that handles testing + MCP connections to your issue tracker = a system that is unmatched.

The skill encodes your team's conventions. You don’t need to worry about context. The subagents keep your main conversation clean while handling complex subtasks. The MCP connections eliminate the context switching that fragments your attention.

The engineers I've watched who get the most from Claude Code aren't using it for one-off tasks, but they’re treating it as a system to multiply their work capabilities. They invest time configuring skills, defining subagents, connecting services. That investment then rightfully pays dividends on every subsequent task.

If you’re scared of where to start, just start with one skill for something you explain repeatedly. Or create just a singular agent. Then test and go from there. No need to overwhelm yourself with trying everything at once.

## TLDR

**Context windows aren't equal.** Claude Code delivers consistent 200K tokens. Cursor often truncates to 70-120K in practice due to internal safeguards. This matters for large codebases.

**Skills teach Claude your specific workflows.** Create ~/.claude/skills/skill-name/SKILL.md with YAML frontmatter (name, description) and markdown instructions. Claude applies them automatically when relevant.

**Subagents provide isolated context for complex tasks.** Each gets its own 200K window. Built-in: Explore, Plan, general-purpose. Create custom ones in ~/.claude/agents/. They communicate through delegation and summary, not shared context.

**MCP connectors eliminate context switching.** Connect to GitHub, Slack, databases, issue trackers. Chain workflows that would normally require five tabs into one continuous session. Command: claude mcp add --transport http <name> <url>

**These compound.** Skills encode patterns, subagents handle subtasks, MCP connects services. Together, they build a system that improves with use.

If you're building with Claude Code and want more tactical breakdowns like this, subscribe to my weekly AI newsletter: [https://varickagents.com/newsletter](https://varickagents.com/newsletter)