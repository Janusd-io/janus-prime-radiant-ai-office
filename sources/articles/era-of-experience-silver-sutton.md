---
title: "Welcome to the Era of Experience"
source: "https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf"
authors: ["David Silver", "Richard S. Sutton"]
affiliation: "Google DeepMind"
published: 2026
note: "Preprint of a chapter to appear in the book Designing an Intelligence, published by MIT Press."
created: 2026-06-05
description: "Silver & Sutton argue AI is entering an era of experience: agents will achieve superhuman capability by learning from their own streams of experience rather than from static human data. Four defining properties: streams (continuous, not episodic), grounded actions/observations, grounded rewards, and non-human reasoning."
tags:
  - "research-paper"
  - "reinforcement-learning"
  - "experiential-ai"
---

# Welcome to the Era of Experience

**Authors:** David Silver, Richard S. Sutton (Google DeepMind)  
**Note:** Preprint; chapter to appear in *Designing an Intelligence* (MIT Press)

## Abstract (paraphrased)

We stand on the threshold of a new AI era. A new generation of agents will acquire superhuman capabilities by learning predominantly from experience — not from human-generated data. This note explores the key characteristics of this era.

## The Era of Human Data — and its limits

LLMs achieved broad generality by training on massive human data and fine-tuning with human preferences. But:
- The approach can reproduce human competence, not superhuman intelligence.
- High-quality training data is nearly exhausted across key domains.
- Progress from supervised human-data learning is demonstrably slowing.
- Genuinely new insights (new theorems, scientific breakthroughs) lie beyond existing human knowledge.

## The Era of Experience — four defining properties

The solution is agents that **learn continually from their own experience**:

1. **Streams.** Agents inhabit ongoing streams of experience (years-long) rather than short, isolated episodes. Goals can stretch far into the future; information carries across the entire stream.

2. **Grounded actions and observations.** Rather than interacting via human dialogue alone, agents act autonomously in the real world — sensorimotor interaction, code execution, APIs, computer interfaces. This enables exploration and discovery beyond human instruction.

3. **Grounded rewards.** Rewards come from the environment — cost, error rates, health metrics, productivity measures, empirical observations — not from human expert pre-judgement. The reward function can be adapted through experience in a user-guided manner (bi-level optimisation over grounded signals).

4. **Non-human reasoning.** Human language is unlikely to be the optimal internal representation for computation. Self-learning systems can discover or improve their own reasoning mechanisms. AlphaProof as example: proved theorems via methods quite different from human mathematicians. Agents trained only on human thought inherit human fallacies; grounded experience provides the feedback loop to test and overturn them.

## Reconciling experiential RL with LLM generality

The era of simulation (RL in closed domains) produced superhuman agents in narrow domains. The era of human data achieved breadth but discarded self-discovery. The era of experience reconciles both: autonomous interaction with complex, real-world action spaces + RL methods that can solve open-ended problems in rich reasoning spaces.

AlphaProof (IMO silver-medal level) and DeepSeek-R1's reinforcement learning are early signals that the transition is underway.

## Safety considerations

Experiential agents introduce heightened risks: fewer natural intervention points, non-human reasoning is harder to interpret. But also safety benefits:
- Experiential agents can observe when behaviour triggers human concern and adaptively modify it.
- Misaligned reward functions can be incrementally corrected through trial and error (bi-level optimisation).
- Physical-world constraints impose real-time limits on how fast agents can act.

## Connection to Letta / token-space learning

Silver & Sutton's framing is about experience as the *training signal*. Letta's Context Constitution and "Continual Learning in Token Space" blog post are about *token-space context management* as the learning mechanism. The two are complementary: Silver/Sutton describe what agents should learn from; Letta describes how agents should represent what they've learned without updating weights. Together they sketch the architecture of experiential AI: streams of experience → token-space representations as the persistent output of that learning.

## References

Full reference list on pages 9–11 of the PDF. Key citations:
- AlphaProof: Masoom et al. (2024) — silver-medal level IMO
- MemGPT: Packer et al. (arxiv 2310.08560)
- Sleep-time Compute: arxiv 2504.13171
- DeepSeek-R1: arxiv 2501.12948
