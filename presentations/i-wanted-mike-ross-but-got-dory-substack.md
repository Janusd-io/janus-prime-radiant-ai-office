# I Wanted Mike Ross. I Got Dory.

*Why the most important thing you can do with AI isn't smarter inference. It's building a memory that compounds.*

---

There's a scene early in *Suits* where Harvey Specter tests Mike Ross for the first time. He throws a thick file across the desk and tells him to read it. Mike reads it once, cover to cover, and from that point on he can recall any clause, any footnote, any timestamp from that document on demand. Years later, he can still tell you what was on page 47. He's not just smart; he has total recall. He knows everything that's ever passed through his hands, and he can retrieve any of it, in context, instantly.

That's what organisations imagined they were getting when they first deployed AI for knowledge work.

What they got was Dory.

Dory, the blue tang from *Finding Nemo*, is genuinely capable in the moment — responsive, helpful, full of enthusiasm. But every few minutes, she resets. Ask her tomorrow what you talked about today and she'll have no idea. She's not malfunctioning. That's simply what she is.

And that is the deepest limitation of AI in organisations today. Not the quality of the responses. The absence of useful memory between them.

---

## The Stateless Trap

Today's AI systems do have some memory. Most major platforms offer conversation history, persistent project spaces, and ways to inject standing context at the start of a session. These are genuinely useful improvements. But they solve a shallow version of the problem, not the deep one.

Conversation history persists within a thread, not across your whole organisation's work. Project spaces let you attach some background documents, but they're typically siloed per user and hard to share or keep current. None of these mechanisms accumulate knowledge structurally: they don't cross-reference new information against old, they don't update existing conclusions when new evidence contradicts them, and they don't build the causal chain that lets you ask "why did we decide this?" and get a real answer.

The consequence is that institutional intelligence produced in one session stays trapped there. If you asked your AI to help analyse a vendor in March, and you're asking again in June, it has no idea the analysis happened. It cannot build on what it found. It starts from zero.

This is tolerable for one-off tasks. It is quietly devastating for knowledge work, where almost all the value is cumulative. The second decision is supposed to build on the first. The tenth brief should synthesise the previous nine. Institutional intelligence is precisely the web of connections between past choices, their outcomes, and the context that produced them. An AI whose memory is shallow, siloed, or structurally flat cannot participate in that compounding. It can only serve the moment.

The industry has spent three years improving inference quality. It has spent almost no time solving this. As a result, most organisations are using their AI in the most wasteful possible way: as a very fast amnesiac.

---

## Why Your Current Tools Don't Fix It

The natural objection is: we already have this. We have Notion. We have Slack. We have meeting transcripts. We have project management software, CRM notes, shared drives. The knowledge exists — it's just scattered.

But scattered is the problem. These tools are each authoritative within their own domain. Your meeting software captures what was said. Your project tracker captures what was decided. Your documentation platform captures what was planned. But none of them are connected, none are synthesised, and none are queryable across the whole.

Try asking your AI assistant: "Why did we make the decision we made in April?" Getting to the real answer requires pulling the meeting where it was discussed, the document where it was logged, the project ticket where it was evaluated, and the Slack thread where it was contested. The answer lives across four systems, zero of which talk to each other. The AI has to reconstruct the story every single time. It never knows it's told this story before.

More fundamentally: these tools weren't designed for AI-native accumulation. They're human knowledge tools that AI can query. They're not knowledge structures that get smarter as new information arrives. The gap isn't search quality. It's synthesis over time.

---

## What Continual Learning Actually Means

Continual learning memory changes the operating model from retrieval to accumulation. Instead of asking an AI to search for relevant content on demand, you build a system that continuously processes new signals — meeting notes, articles, decisions, evaluations — and integrates them into a persistent, structured knowledge base that grows more connected with each addition.

The properties that make this transformational rather than incremental:

**Persistence.** Knowledge doesn't evaporate between sessions. A decision recorded in April is queryable in September with full causal context: why it was made, what evidence supported it, what alternatives were rejected and on what grounds.

**Connection.** New information is automatically cross-referenced against existing knowledge. A new source doesn't just add a new fact; it updates the web of relationships around existing facts. A competitor signal might simultaneously inform a vendor evaluation, a strategic brief, and an open question from three months ago. Those connections get made on ingest, not on demand.

**Synthesis.** The AI doesn't just store inputs; it extracts meaning. What does this meeting decision imply for the vendor evaluation made six weeks earlier? What does this research paper mean for the architectural bet made last quarter? The synthesis lives in the system, not in someone's head.

**Compounding.** Each new piece of knowledge makes the existing knowledge more useful. A knowledge base with 500 entries answers questions that a 50-entry base cannot, not because of size, but because the connections between entries are denser, the contradictions are resolved, and the synthesis is deeper. The value is network-valued, not linear.

This is the gap between a searchable document store and genuine institutional memory. A document store gives you faster retrieval of things that already exist. Continual learning memory gives you a system that gets more intelligent over time.

---

## The Architecture Problem: Why Vector Search Isn't Enough

The standard response to "we need AI to query institutional knowledge" is a vector database: embed all documents, retrieve by semantic similarity, inject into context. This is the RAG (Retrieval-Augmented Generation) pattern, and it's genuinely useful for document search. It's not sufficient for institutional memory.

The core limitation: vector similarity captures one relationship type. Semantic closeness. Two documents are "related" because they discuss similar topics. But institutional knowledge runs on at least four relationship types simultaneously.

**Semantic** — conceptual similarity, same topic, same domain. Answers: "What do we know about agent frameworks?"

**Entity** — the organisational graph: who was involved, which team, which vendor. Answers: "Every decision Sarah has been part of."

**Temporal** — when things happened, what came before what, how positions evolved. Answers: "What changed between Q1 and Q2?"

**Causal** — what led to what: decisions, their rationale, their outcomes. Answers: "Why did we reject that vendor?"

A pure vector store handles semantic queries adequately. It handles entity, temporal, and causal queries poorly or not at all. "Why did we reject that vendor?" requires traversing a causal chain: the evaluation decision, the meeting where it was discussed, the principle it violated, the earlier lesson that established the principle. Semantic similarity to "vendor rejection" doesn't surface that chain. Graph traversal does.

In May 2026, two independent research groups published essentially the same insight within 48 hours of each other. Mnemon, an open-source agent memory project, proposed a four-graph knowledge store covering exactly these four dimensions. MAGMA, a peer-reviewed paper from researchers at UT Dallas and the University of Florida, independently proposed the same four-graph decomposition and validated it experimentally on established memory benchmarks, substantially outperforming vector-similarity approaches on complex multi-hop reasoning tasks.

When two groups deriving from different premises arrive at the same architecture in the same week, it suggests the decomposition reflects something real about the structure of knowledge, not an arbitrary design choice. Organisations building institutional memory should take the four-graph model seriously — not as a theoretical curiosity but as a validated engineering foundation.

---

## Fine-Tuning vs. Context: The Practical Tradeoff Teams Get Wrong

There are roughly four ways to give an AI system access to organisational knowledge. Most teams end up choosing the wrong one by default.

**Fine-tuning the model.** Training an LLM on institutional data so the knowledge is baked into model weights. The problems: retraining is expensive and slow, updates require a new training run, the knowledge is opaque (you cannot inspect or audit what the model "knows"), and the entire investment is lost if you change models. For knowledge that changes daily, sometimes hourly, this doesn't scale. Fine-tuning is a reasonable choice for durable domain vocabulary. It is a poor choice for living institutional knowledge.

**Long-context injection.** Maintaining institutional knowledge in a very long system prompt injected at the start of every session. This works for shallow depth (a few standing facts) but collapses as knowledge grows. Context windows are finite. Injecting everything means injecting noise alongside signal. More fundamentally, it's volatile: nothing persists once the session ends. You're not building memory; you're configuring a stateless machine.

**RAG over raw documents.** As discussed above, adequate for semantic search, but inadequate for multi-graph institutional memory. RAG has well-documented limitations beyond the four-graph problem: it struggles with multi-hop reasoning (questions that require connecting several documents in sequence), it retrieves based on surface similarity rather than logical relevance, and it has no mechanism for keeping retrieved content current as the underlying documents change. Most organisations that have deployed "AI over our knowledge base" are here. It's better than nothing, but not good enough.

**Structured, curated, LLM-maintained knowledge bases.** Flat files of machine-readable structured knowledge — markdown with YAML frontmatter encoding the four graph types — maintained by an LLM operating against a schema document, queryable by both humans and AI, version-controlled. This is the approach validated by the research literature on in-context learning.

The research case for the last approach is robust. The foundational finding, established since Brown et al.'s GPT-3 paper (2020) and reinforced by Min et al. (EMNLP 2022) and Yin et al. (EMNLP 2024), is that well-structured in-context knowledge is competitive with fine-tuning for knowledge retrieval, and outperforms it on the dimensions that matter most to organisations. Min et al. showed that what drives in-context learning performance is the structure and format of the provided knowledge, not just its presence — curated organisation matters as much as content. Yin et al. showed that for tasks requiring implicit pattern recognition across a knowledge base, in-context learning captures those patterns significantly better than fine-tuning does.

- **Updatability.** In-context knowledge changes when you edit a file. In-weights knowledge requires a new training run. Institutional knowledge evolves daily, sometimes hourly. That cadence makes fine-tuning a slowly degrading snapshot, not a living record.
- **Inspectability.** Context is readable by anyone — human or AI. You can audit it, correct it, and version-control it. Weights are opaque. You cannot identify where a fine-tuned model is wrong until it answers a question incorrectly.
- **Precision over volume.** Research has consistently shown that well-structured, curated context outperforms large-volume raw injection. Quality and organisation matter more than quantity. A curated 50-page knowledge base will outperform an uncurated 5,000-document corpus in most real-world tasks.
- **Vendor independence.** Knowledge stored in structured files travels across model generations and providers unchanged. Fine-tuned weights are locked to the model they were trained on. Your knowledge investment should survive your next model upgrade.

The practical implication: for most teams, the right architecture is not fine-tuning and not naive RAG. It's curated, structured, multi-graph knowledge that is injected into context with precision — pulling only the subset relevant to the current query, not the entire corpus.

---

## The Wiki as Delivery Construct

The most viable practical implementation of the above for most organisations is a structured wiki maintained by an LLM: a set of flat markdown files that together encode the four graph types, updated automatically as new information arrives, readable by both humans and AI, and version-controlled via Git.

This probably sounds underwhelming. It isn't.

The idea of an LLM-maintained wiki originates with Andrej Karpathy, who proposed it in the context of personal knowledge management. His core insight was that an LLM is uniquely well-suited to the maintenance burden that kills every personal wiki: keeping pages current, consistent, and cross-referenced as new information arrives. That insight scales directly to organisations, where the maintenance burden is larger by orders of magnitude and the cost of institutional knowledge degrading is far higher than any individual's.

**Markdown files are simultaneously human-readable and machine-queryable.** A Notion page requires Notion's API. A database table requires a query layer. A markdown file with YAML frontmatter can be opened in any text editor or searched programmatically via standard file operations. There's no translation layer, no API dependency, no schema negotiation. The file is the knowledge.

**Flat files are portable across AI vendor cycles.** If you move from one model to another (and you will, within the next few years), the knowledge base travels with you unchanged. A platform-managed memory store, opaque state maintained inside a vendor's infrastructure, cannot make this claim. This has become a live debate in the AI engineering community: Harrison Chase (LangChain CEO) and Sarah Wooders (Letta CTO) both argued in 2026 that your agent harness and your memory are inseparable — meaning that if your memory lives inside a closed harness, it leaves when you do. File-based memory sidesteps this entirely; the knowledge is yours regardless of which platform you run it through.

**Version control gives you the audit trail, but only if you use Git.** Store the wiki in a Git repository and every change is tracked with author, timestamp, and message. The decision recorded in January, the meeting transcript from March that modified it, and the brief from June that synthesised it are all in the same version history, navigable by commit log and diff. That's not just good practice; it's the causal graph substrate made concrete and auditable.

**LLM maintenance eliminates the overhead that kills personal wikis.** The graveyard of personal knowledge management systems is enormous. Every ambitious Notion setup, every carefully structured Roam graph, every meticulously tagged Obsidian vault: most die the same death, abandoned when maintenance burden exceeds the benefit of having them. The LLM solves this. Every ingest is fully automated: a source arrives, the LLM reads it, identifies which existing pages it affects, updates them, creates new pages where needed, adds cross-references, logs the activity, updates the index. What would take a knowledge worker thirty minutes of careful curation takes two minutes of automated processing. And crucially: the LLM never falls behind.

The compounding mechanism is the cross-reference. Each ingest adds not just a new page but new edges — new connections between existing pages that only become visible when they're seen alongside the new source. It's those edges that make the system more intelligent over time, not just larger.

---

## The Schema Is the Strategy

One component the wiki approach requires that most organisations underestimate: a governing schema document.

An LLM without explicit operating rules applied to a knowledge base will produce inconsistent output. Idiosyncratic structure, broken cross-references, contradictory claims, naming collisions. The maintenance advantage disappears if the LLM is making different structural choices on each ingest.

The schema, a document that governs every write the LLM makes, is what turns a capable AI into a disciplined institutional curator. It specifies naming conventions, frontmatter fields, folder semantics, the distinction between low-stakes and high-stakes operations, attribution standards, the shape of a brief, and criteria for escalating to human review.

Think of it as an operating contract between the organisation and the AI. The schema is not documentation of how the system works; it is the mechanism by which the system works. Without it, knowledge accumulates chaotically. With it, knowledge accumulates as a coherent graph where any entry point leads reliably to every relevant connected page.

The schema also evolves. This is important. Each version should add discipline where practice revealed gaps. The right cadence is: start with a minimal viable schema, run it for several weeks of real ingest, surface the places where the LLM's choices were inconsistent or the output structure failed to support a real query, and amend. The schema is the accumulated lesson of operating the system.

This is one of the few AI implementation tasks where the human investment pays compounding returns: one good schema document, maintained over time, governs thousands of future ingest operations without further human intervention.

---

## The Three-Layer Model for Organisational Implementation

For teams trying to build this in practice, the architecture decomposes into three layers. The sequence matters.

**Layer 1 — Signals.** Everything the system is exposed to: meeting transcripts, Slack threads, system-of-record exports (your project tracker, CRM, documentation platform), articles, competitor intelligence, research. The discipline here is to throw the net wide. AI handles volume; under-collecting is the failure mode, not over-collecting. The system is only as smart as its sensor array is dense. If signals aren't flowing in, the knowledge base stagnates.

**Layer 2 — Infrastructure.** Domain-specific framing documents that define what relevance looks like from your organisation's vantage point: company mission, strategic priorities, ideal customer profile (for a marketing team), tool evaluation criteria (for an IT or AI team), policy frameworks. Without infrastructure, dense signals produce dense noise. With it, the same signals produce precise relevance flags and durable strategic context. This is the layer most organisations skip, and it's why their AI knowledge tools feel generic.

**Layer 3 — Outputs.** What the system produces back to the world: briefs, plans, decision records, positioning documents. The canonical output is the strategic brief — not a neutral industry summary, but an explicit connection between external signals and the organisation's specific bets. The brief is how the system thinks out loud.

Build in this order. Attempting to design outputs before infrastructure is documented produces brittle templates with no grounding. Attempting to stand up infrastructure before signals are flowing produces abstract frameworks with no evidence base. The order is fixed by the logic of the thing: you cannot synthesise what you haven't collected, and collection without context produces noise.

---

## Practical Steps for Teams Starting Now

The research and architectural arguments above point toward a concrete starting position for any organisation that hasn't done this yet.

**Start with one domain, not the whole organisation.** Pick the team with the most to gain from accumulated institutional memory — usually the one that deals with the most recurring knowledge work: vendor evaluations, strategic decisions, client intelligence, competitive analysis. Stand up a minimal knowledge base for that team and run it for a quarter before expanding.

**Build the schema before you build the vault.** Spend a week writing the operating contract for your knowledge base: what types of content go in, what metadata fields each type carries, what naming conventions apply, what the LLM should do when it encounters a new entity versus an update to an existing one. A minimal schema can be a single document of a few hundred words. A bad schema (or no schema) produces a knowledge base that degrades rather than compounds.

**Let the LLM do the maintenance, not the creation.** The human role in this system is curation and judgment: deciding what enters the inbox, resolving escalations, reviewing outputs, updating the schema when gaps appear. The LLM's role is everything else: ingesting, cross-referencing, updating, synthesising. If humans are doing the maintenance, the system doesn't scale. If the LLM is making the judgment calls, the system makes mistakes it shouldn't.

**Treat the output as a new input.** Every time the system produces a brief or a synthesis that earns its keep, file it back in. The best knowledge base is one where the system's own conclusions become part of its context for future reasoning. This is the query-back compounding mechanism, and it's where the most dramatic improvements in output quality come from over time.

**Run periodic health checks.** Lint the knowledge base every few weeks: surface pages that contradict each other, claims that have gone stale, entities mentioned across multiple pages that don't have their own dedicated page, cross-references that point to non-existent targets. Each lint pass tightens the graph and resolves inconsistencies. The knowledge base should become more accurate over time, not less. If it's degrading, something is wrong with the schema or the ingest discipline.

---

## Why This Matters More Than Model Quality

Here is the uncomfortable implication of everything above.

In the near term, model quality (the raw inference capability of the underlying AI) will continue to improve rapidly and will continue to commoditise rapidly. The gap between the best model and the third-best model, for most knowledge work tasks, is shrinking. In 18 to 24 months, every organisation will have access to capable AI inference. It will be like electricity: infrastructure-level, essentially free, universally available.

The organisations that will benefit disproportionately from that world are not the ones that found the best model. They are the ones that built the best memory.

Institutional memory is not a commodity. It cannot be purchased; it can only be built, over time, through accumulated ingest and disciplined curation. A knowledge base with two years of structured, cross-referenced institutional history is worth something qualitatively different from a knowledge base with two weeks. The gap is not a function of model quality. It is a function of how long you started.

This is the practical import of the Dory problem. The answer to "we wanted Mike Ross but got Dory" is not "find a better Dory." It is to build the memory system that turns Dory into something else: a system that accumulates what every conversation produces and makes it available to every future conversation, permanently, with context intact.

The organisations that start building that system now will have a meaningful advantage that no future model upgrade can close, because the advantage is not the AI's intelligence. It's the organisation's accumulated knowledge of itself.

---

*References:*

*Multi-graph memory architecture: [MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents](https://arxiv.org/abs/2601.03236) (accepted ACL 2026); [Mnemon: LLM-supervised persistent memory for AI agents](https://mnemon.dev/).*

*In-context learning: [Brown et al., "Language Models are Few-Shot Learners," NeurIPS 2020](https://arxiv.org/abs/2005.14165); [Min et al., "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?", EMNLP 2022](https://arxiv.org/abs/2202.12837); [Yin et al., "Deeper Insights Without Updates: The Power of In-Context Learning Over Fine-Tuning," EMNLP 2024](https://arxiv.org/abs/2410.04691).*

*Karpathy LLM Wiki: [Original gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).*

*Harness/memory lock-in: Harrison Chase, ["Your harness, your memory"](https://blog.langchain.com/your-harness-your-memory/) (LangChain, April 2026); Sarah Wooders (Letta CTO), as cited in Chase's analysis — the full Wooders framing: "Asking to plug memory into an agent harness is like asking to plug driving into a car."*
