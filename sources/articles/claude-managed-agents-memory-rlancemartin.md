---
title: "Memory in Claude Managed Agents"
source: "https://x.com/rlancemartin/status/2047720067107033525?s=12"
author:
  - "[[@rlancemartin]]"
published: 2026-04-24
created: 2026-05-06
description: "Claude Managed Agents (available on the Claude Platform) now has memory. Memories are stored as files and are accessible across sessions, al..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HGrseQmbEAACAWr?format=jpg&name=large)

**Claude Managed Agents (available on the Claude Platform) now has memory. Memories are stored as files and are accessible across sessions, allowing the agent to learn from experience. Memories can also be exported via the API.**

[@DavidSHershey](https://x.com/DavidSHershey) shared a story about agent memory with me: in his work on Claude Plays Pokémon, he gave Claude a tool to read and write memory files to a folder. These memory files were meant to help Claude navigate the game.

This didn’t work very well with earlier models. Sonnet 3.5 treated memory as a transcript, writing down what non-player characters said rather than what mattered. After 14,000 steps it had 31 memory files, but had not made much progress (it was stuck in the second town). Here’s an example of one file:

```json
caterpie_weedle_info:
- Caterpie and Weedle are both caterpillar Pokémon.
- Caterpie is a caterpillar Pokémon that does not have poison.
- Weedle is a caterpillar Pokémon that does have poison.
- This information is crucial for future encounters and battles.
- If our Pokémon get poisoned, we should seek healing at a Pokémon
 Center as soon as possible.
```

To overcome these limitations, many papers have proposed harnesses with tooling to manage memory. [@tedsumers](https://x.com/@tedsumers) [CoALA paper](https://arxiv.org/pdf/2309.02427) and the [memGPT work](https://arxiv.org/pdf/2310.08560) from [@sarahwooders](https://x.com/@sarahwooders) and [@charlespacker](https://x.com/@charlespacker) are two of my favorites. These use ideas from cognitive sciences and operating system to model agent memory.

But the Pokémon work showed an interesting result: later models learned to use the filesystem to organize memory much better. Opus 4.6, at the same step count, had 10 files organized into directories, three gym badges, and a learnings file distilled from its own failures:

```json
/gameplay/learnings.md:
- Bellsprout Sleep+Wrap combo: KO FAST with BITE before Sleep
 Powder lands. Don't let it set up!
- Gen 1 Bag Limit: 20 items max. Toss unneeded TMs before dungeons.
- Spin tile mazes: Different entry y-positions lead to DIFFERENT
 destinations. Try ALL entries and chain through multiple pockets.
- B1F y=16 wall CONFIRMED SOLID at ALL x=9-28 (step 14557)
```

This example highlights a trend, which I wrote about [here](https://claude.com/blog/harnessing-claudes-intelligence): give Claude general tools to manage its own context and actions. Claude can learn to use general tools to solve problems, like memory, with scaling intelligence.

With a general tool to manage files, we’ve seen Claude learn what to save and how to organize its own memories. [@Letta\_AI](https://x.com/@Letta_AI) [independently showed](https://www.letta.com/blog/benchmarking-ai-agent-memory) that a filesystem can outperform specialized memory tools.

This story explains why we use the filesystem for memory in [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) (available on the Claude Platform). Files can be organized however Claude wants, [using](https://platform.claude.com/docs/en/managed-agents/memory#how-the-agent-accesses-memory) its standard [file tools](https://platform.claude.com/docs/en/managed-agents/tools#available-tools). The platform just persists files between sessions using memory stores, which are workspace-scoped collections of text documents that outlive any single session.

![Image](https://pbs.twimg.com/media/HGrvh1dbYAIL7G5?format=png&name=large)

When you attach a memory store to a session, it's mounted into the container as a directory at /mnt/memory/<store-name>/. A short note about the mount is automatically injected into the system prompt so Claude knows it's there.

Multiple agents can access the same memory store and the platform will sync memories in real time: if one agent makes an edit, that edit will be reflected in the filesystem of all other agents that have the memory store mounted. It also will handle concurrency to make sure one agent doesn't overwrite the memory updates made by another agent.

Files have an additional benefit - they are interpretable and sharable. In the Pokémon example, [@DavidSHershey](https://x.com/DavidSHershey) was able to just download and share the memory folders. With Managed Agents you can also export memories:

```python
client.beta.memory_stores.memories.list(store_id, view="full")
```

This sets up a simple way to think about context in Managed Agents: there is a session log and a memory store. As [@mc\_anthropic](https://x.com/@mc_anthropic), [@gcemaj](https://x.com/@gcemaj), and I wrote about [here](https://www.anthropic.com/engineering/managed-agents), Claude can fetch and transform session context over the course of a task. The session lives outside the context window, which has benefits that [@a1zhang](https://x.com/@a1zhang) and [@lateinteraction](https://x.com/@lateinteraction) have nicely outlined [here](https://arxiv.org/abs/2512.24601). Claude can write files to the memory store if it wants to persist context across sessions.

**To get started, see our** [docs](https://platform.claude.com/docs/en/managed-agents/memory) **or use our** [claude-api skill](https://github.com/anthropics/skills/tree/main/skills/claude-api)**. This skill is built into Claude Code, and can be triggered by running "/claude-api". You can then ask questions about Claude Managed Agents or other API features.**