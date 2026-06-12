# Email — Hermes evaluation update for Jon Austin

**Date:** 2026-06-12 · **From:** Michael Bruck · **To:** [[jon-austin|Jon Austin]] (Jono) — incoming CTO
**Context:** Jono recommended [[hermes|Hermes Agent]] during the 2026-06-11 intro call (source: `2026-06-11-jon-austin-cto-intro`). This email closes the loop on the code-level evaluation (Hermes vs [[nanoclaw|NanoClaw]] as the Prime Radiant front-end; tracked in Linear AIR-163). Evaluation working docs live outside the vault at `~/Code/hermes/` (assessment, deeper evaluation, trial spec incl. Hermes hands-on arm + headless-Obsidian cloud phase).

---

**Subject:** Hermes follow-up — where our evaluation landed

Hi Jon,

Great speaking yesterday — and thanks for the Hermes pointer. We moved on it straight away: it's in our AI registry pipeline as of yesterday, and I've since done a deeper evaluation directly against the codebase, comparing it with NanoClaw (the minimal Claude-native agent host we've been trialling as the front-end to Prime Radiant). Wanted to close the loop with you on where that landed.

The short version: Hermes is genuinely impressive — the engineering velocity, the provider abstraction, and the self-improving skill/memory loop are real differentiators, and I can see why it's winning the CTO-group consensus as a general agent platform. But for the Prime Radiant front-end specifically, the evaluation came out in favour of staying with NanoClaw. Three findings drove it:

1. **Claude-nativeness.** Hermes runs its own agent loop with Anthropic as one pluggable provider — it doesn't read CLAUDE.md, and its skill format isn't compatible with the Anthropic skill ecosystem. Prime Radiant's entire operating discipline lives in a CLAUDE.md rulebook, and we already run a fleet of load-bearing Claude Code skills. Adopting Hermes means re-implementing all of that in a foreign format; NanoClaw (built on the Claude Agent SDK) runs it as-is.

2. **Isolation defaults.** Hermes executes on the host by default, with containers opt-in. NanoClaw gives per-session container isolation with an explicit mount allowlist and request-time credential injection out of the box. For an agent with write access to our institutional memory, that's the posture we want as the default, not the retrofit.

3. **The learning loop cuts the wrong way for this use case.** Hermes' autonomous memory curation is its best feature for a personal agent — but Prime Radiant is deliberately human-curated, with a strict low/high-stakes trust line. An agent that rewrites its own skills and accumulates its own memory store competes with that discipline rather than serving it.

None of which is a knock on Hermes — its strengths point at a different problem than ours. And since this was a code-level read rather than a live test, we're keeping it honest: the trial plan includes a time-boxed hands-on arm running Hermes through the exact same acceptance tests as NanoClaw, on the same vault, so the conclusion is empirical rather than architectural.

One thread I'd genuinely value your input on, given your offer to help with Prime Radiant cloud hosting: the next trial phase moves the stack off-device to a cloud VM, using Obsidian's new headless client as the sync transport (curators edit in Obsidian desktop/mobile, the VM is the sole git committer for the audit trail). It's the kind of keep-it-simple deployment shape I suspect you'd have opinions on. Happy to send over the full evaluation and trial spec if useful.

Thanks again for the steer — exactly the kind of signal we want flowing into the registry.

Best,
Michael
