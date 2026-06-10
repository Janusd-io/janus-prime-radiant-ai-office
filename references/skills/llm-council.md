---
type: skill
tags: [skill, decision-support, multi-agent, karpathy]
command: /council
path: ~/.claude/skills/llm-council/SKILL.md
source: https://github.com/aiwithremy/claude-skills-llm-council
---

# /llm-council

Run any high-stakes question, idea, or decision through a council of 5 AI advisors who independently analyze it, peer-review each other anonymously, and synthesize a final verdict. Based on Andrej Karpathy's LLM Council methodology — adapted to run inside Claude via subagents with distinct thinking lenses instead of distinct models.

## When to use
Use when a decision has genuine uncertainty, multiple options, and meaningful downside if you call it wrong. Bad fit for factual lookups or pure creation tasks.

## Trigger phrases
**Mandatory:** "council this", "run the council", "war room this", "pressure-test this", "stress-test this", "debate this".
**Strong (with a real tradeoff):** "should I X or Y", "which option", "what would you do", "is this the right move", "validate this", "get multiple perspectives", "I can't decide", "I'm torn between".

## How it works
1. Five advisor subagents independently analyze the question from different angles
2. They anonymously peer-review each other's reasoning
3. A chairman subagent synthesizes a final verdict — agreements, clashes, recommendation

## Related
- [[skill-create]]
- [[prompt-engineer]]
- [[skills]]
