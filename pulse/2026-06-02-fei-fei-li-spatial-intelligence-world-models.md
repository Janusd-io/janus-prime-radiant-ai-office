---
type: pulse
title: "Fei-Fei Li frames spatial intelligence + world models as AI's next frontier (World Labs / Marble)"
slug: 2026-06-02-fei-fei-li-spatial-intelligence-world-models
created: 2026-06-02
updated: 2026-06-02
departments: [ai-office, engineering]
confidence: medium
sources: [2025-11-10-fei-fei-li-spatial-intelligence-frontier]
related: [organisational-digital-twin, digital-twin, agent-memory, agentic-ai, post-rag-agent-data-stack]
---

# Fei-Fei Li frames spatial intelligence + world models as AI's next frontier

Fei-Fei Li (founder of ImageNet, Stanford SVL, World Labs) published *"From Words to Worlds: Spatial Intelligence is AI's Next Frontier"* on her Substack 2025-11-10 ([[2025-11-10-fei-fei-li-spatial-intelligence-frontier]]). Older piece than the rest of this batch — surfaced via the inbox 2026-06-02 — but worth a pulse because the framing maps cleanly onto Janus's own digital-twin work and because Fei-Fei is the most credentialed voice in the field placing this bet publicly.

## The thesis

LLMs are *"wordsmiths in the dark; eloquent but inexperienced, knowledgeable but ungrounded."* The next-decade frontier is **spatial intelligence** — the capability that links imagination, perception, and action through grounded representations of physical or virtual worlds. World models are the architectural class being built to deliver it.

Fei-Fei defines a world model through three essential capabilities:

1. **Generative** — generates simulated worlds (perceptually, geometrically, physically consistent) from semantic / multimodal prompts.
2. **Multimodal** — accepts images, video, depth maps, text, gestures, or actions; produces predicted world states.
3. **Interactive** — when given an action, outputs the *next state* of the world consistent with the previous state, physical laws, and dynamical behaviours.

World Labs (her current company, co-founded with Justin Johnson, Christoph Lassner, Ben Mildenhall) recently launched **Marble**, *"the first ever world model that can be prompted by multimodal inputs to generate and maintain consistent 3D environments for users and storytellers."*

## Why this matters to the AI Office

Two non-obvious connections to existing AIO concepts:

1. **The "world model" vocabulary is the bridge between Fei-Fei's spatial-intelligence research and Block's "company world model" framing.** [[organisational-digital-twin]] uses world-model vocabulary borrowed from Block; Block uses it for organisational state; Fei-Fei uses it for spatial / physical state. The architectural pattern is the same: a continuously-updated structured representation of an environment (physical or organisational), generative and interactive, that an agent operates against. **The wiki's organisational-digital-twin concept is a sibling of Fei-Fei's spatial-world-model concept**, applied to a different substrate. Worth carrying that framing into outbound positioning — it ties the AIO's institutional-knowledge bet to a recognised research-frontier vocabulary, not just to Block.

2. **Janus's HGTFT product is in this lineage.** HGTFT (Heterogeneous Graph Temporal Fusion Transformer — see [[organisational-digital-twin]] for the cross-reference) is a digital twin of physical building infrastructure: geometry + mechanical systems + sensor network + continuous update + queries / simulations / predictions. In Fei-Fei's vocabulary, that's a *spatial world model for a specific built environment*. The fact that Janus already ships HGTFT means the firm has engineering DNA in the spatial-world-model space — not just the organisational-world-model space. **For the deep-research competitive landscape on the AI-Native / digital-twin thesis (see `outputs/org-digital-twin-research-prompt.md`), Fei-Fei / World Labs / Marble is an adjacency worth tracking** because the architectural overlap with HGTFT is non-trivial and might be exploitable for positioning ("Janus is in the spatial-world-model business already").

## Practical implications (lower priority)

- World Labs / Marble could become a vendor of interest if Janus's engineering side investigates spatial-world-model tooling for HGTFT or future digital-twin products. Not an AIO concern today.
- Spatial intelligence will eventually intersect with robotics + healthcare + scientific simulation per Fei-Fei's piece. Not a near-term AIO concern; bookmarked as a horizon signal.
- The piece is principle-led, not benchmark-led. Treat the framing as direction-setting rather than as a measured capability claim.

## Watch for

- Whether Marble ships with public benchmarks or just creative-tool demos. Public benchmarks would let the AIO compare the spatial-world-model frontier against the organisational-world-model frontier on capability terms.
- Whether other foundation-model vendors (OpenAI, Google DeepMind, Anthropic) ship explicit "world model" products distinct from their main LLMs. Google's Genie line is the closest existing analogue; whether it gets repositioned as "world model" framing is the signal to watch.
- Whether the Janus engineering team has touched any of this internally — worth a follow-up question to [[jehad-altoutou|Jehad]] / engineering leads on whether HGTFT's evolution roadmap touches any "world model" framing or if it stays explicitly building-twin-focused.

## Cross-reference

This pulse should be linked from any future research output covering the digital-twin landscape (e.g., the `org-digital-twin-research-prompt.md` artefact at `outputs/`) — Fei-Fei + World Labs is one of the adjacencies the deep-research pass should test.
