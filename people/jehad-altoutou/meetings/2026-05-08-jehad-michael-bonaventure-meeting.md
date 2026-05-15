---
type: source
source_type: meeting
title: "Jehad, Michael, Bonaventure Meeting"
slug: 2026-05-08-jehad-michael-bonaventure-meeting
created: 2026-05-08
captured_by: jehad-altoutou
attendees: [michael-bruck, jehad-altoutou]
duration_min: 50
fireflies_id: 01KR3MEP5PSM0TS6F92J9PZKJ5
audience: department
departments: [ai-office]
dept_scope: [ai-office]
sensitivity: dept
task_tracker: monday
parsed_at: 2026-05-15T09:25:59Z
parser_version: 3
summary: "Jehad demoed an Obsidian-based knowledge graph ('Prime Radiant') he built in a day with Claude Cowork that ingests Fireflies transcripts, Monday tasks, Linear registry, Notion, and web-clipped articles, abstracting them into vendors, people, decisions, lessons, projects, trends, and briefs"
topics: [prime-radiant, obsidian-knowledge-graph, department-rollout, recruitment-pipeline, scoring-rubric, assessify-mcp, upskilling, digital-twin]
decisions: [2026-05-08-prime-radiant-per-department-rollout, 2026-05-08-share-prime-radiant-via-shared-google-drive, 2026-05-08-recruiter-owns-scoring-rubric-fine-tuning]
action_items_count: 7
confidence_overall: high
---

# Jehad, Michael, Bonaventure Meeting

**Date:** 2026-05-08
**Attendees:** [[michael-bruck]], [[jehad-altoutou]]
**Duration:** 50 min
**Fireflies:** [original meeting](https://app.fireflies.ai/view/01KR3MEP5PSM0TS6F92J9PZKJ5)

---

## Summary

Jehad demoed an Obsidian-based knowledge graph ('Prime Radiant') he built in a day with Claude Cowork that ingests Fireflies transcripts, Monday tasks, Linear registry, Notion, and web-clipped articles, abstracting them into vendors, people, decisions, lessons, projects, trends, and briefs. Michael agreed the pattern should be rolled out per department (starting with Andrew/Marketing, then Operations/IT/HR/Finance) with department folders acting as connecting nodes, eventually rolling up to a leadership/board view and a long-term digital twin. The group then pivoted to the HR recruitment pipeline: Jehad built an Assessify-backed front end with an MCP connector, a JD builder, an intake form, and an AI scoring rubric reverse-engineered from Maryam's prior results, with a new recruiter joining next month tasked with fine-tuning the rubric, weights, and JD process. Michael framed this as the foundation of an 'Uber for engineers' marketplace tied to Singapore upskilling, where the scoring engine compounds via continuous learning from hire outcomes and interview transcripts. Open items: how to productize the Prime Radiant securely (hosting the dashboard outside Claude, per-country/per-department instances), and Jehad still needs test cases (more candidates) to validate the scoring engine.

## Decisions

- [[2026-05-08-prime-radiant-per-department-rollout]] — Roll Prime Radiant out per department
- [[2026-05-08-share-prime-radiant-via-shared-google-drive]] — Host the AIO Prime Radiant on a Google Shared Drive
- [[2026-05-08-recruiter-owns-scoring-rubric-fine-tuning]] — New recruiter owns fine-tuning the HR scoring rubric and JDs

## Action items

- [ ] @jehad-altoutou Add a departments/ entity category to the Prime Radiant so each department folder federates between teams. (raised by @michael-bruck) — Monday
- [ ] @jehad-altoutou Build a Prime Radiant instance for Andrew/Marketing as the first cross-department rollout. (raised by @michael-bruck) — Monday
- [ ] @jehad-altoutou Move the Prime Radiant vault from Jehad's personal Google Drive to a Janus Shared Drive so Janet has access. (raised by @michael-bruck) — Monday
- [ ] @bonaventure-wong Retry building the HR skill using Claude Cowork now that the tooling has matured. (raised by @michael-bruck) — Monday
- [ ] @bonaventure-wong After building the recruitment project in a Claude personal project, convert it into a shareable skill via Cowork and hand off the skill plus project files to the team. (raised by @michael-bruck) — Monday
- [ ] @jehad-altoutou Generate test cases for the HR scoring engine by running existing Janus hires (pre- and post-interview) through the rubric. (raised by @michael-bruck) — Monday
- [ ] @jehad-altoutou Feed the signal that the recent candidate was actually hired back into the scoring engine as a positive training example. (raised by @michael-bruck) — Monday

## 🎯 This week

- @bonaventure-wong Clean up the personal Claude project (old files) before promoting it to the project-team workspace and converting to a skill.
- @jehad-altoutou Iterate the HR recruitment pipeline (JD builder, form intake, Assessify MCP connector, scoring rubric) with Theresa as the primary user.

## 🏔️ Long horizon

- Stand up a Prime Radiant / Obsidian-style knowledge graph per department (Marketing, Ops, IT, HR, Finance) and federate them via shared department folders rolling up to a Janus board / leadership view. (owner: @michael-bruck; horizon: quarter)
- Productize the Prime Radiant: host the dashboard outside Claude, address multi-country security, and ship per-country instances. (owner: @michael-bruck; horizon: year)
- Build the 'Uber for engineers' marketplace where the HR scoring engine compounds over hires, ties into Singapore upskilling, and eventually expands to lawyers, accountants, and other professionals. (owner: @michael-bruck; horizon: year)
- Position Janus's onsite AI training (with engineering certifications) as the applied-AI complement to the Singapore PM's upskilling initiative, used as a marketing/communication angle. (owner: @michael-bruck; horizon: year)
- Treat the Prime Radiant as the beginning of a Janus digital twin built on continuous learning from every meeting, decision, and hire. (owner: @michael-bruck)
- Use the Prime Radiant to build journalist dossiers and a Marketing opt-in engine that matches Janus content to publication interests for higher placement probability. (owner: @andrew-soane; horizon: quarter)

## Findings

- The Prime Radiant prototype was built end-to-end in roughly one day inside Claude Cowork, using Andrej Karpathy's 'LLM wiki gist' (description, not recipe) as the seed prompt. (stated by @michael-bruck)
- Fireflies summaries are insufficient; the wiki captures this as a lesson and uses raw transcripts as the source of truth. (stated by @michael-bruck)
- The wiki model is closer to a compiler than to RAG: data is compiled once into an Obsidian text/knowledge-graph store, so retrieval doesn't re-derive context every query. (stated by @michael-bruck)
- Memory engineering is reaching a tipping point: Pinecone, OpenAI, Google, and Anthropic are all working the problem, which is what makes the Prime Radiant pattern feasible now. (stated by @michael-bruck; confidence: medium)
- The HR scoring rubric was reverse-engineered from Maryam's prior candidate-score results because the source files she shared were insufficient. (stated by @jehad-altoutou)
- The recent candidate scored ~5.5 because the scoring engine detected from the transcript that he only produced one of four requested fault-detection examples; under normal scoring he would not have passed, but the team hired him anyway. (stated by @michael-bruck)
- The scoring engine, after ingesting all open JDs, recommended an alternate position better suited to a candidate, and that alternate offer was actually extended. (stated by @michael-bruck)
- Assessify exposes an MCP server, so JD creation, scoring, and pipeline operations can be driven directly from Claude as a connector alongside Figma and Fireflies. (stated by @jehad-altoutou)
- Obsidian Web Clipper converts clipped pages to markdown that drops into the inbox, becoming part of the knowledge base after the batch ingest pass. (stated by @michael-bruck)

## Open questions

- How do we productize the Prime Radiant securely (dashboard hosting outside Claude, multi-country security, per-country instances)? (raised by @michael-bruck)
- Can the AIO build something similar to the Prime Radiant for an executive roundtable so participants enter with full context on each other? (raised by @michael-bruck)
- What is the right way to share Claude skills and the underlying project files between teammates without manually re-uploading? (raised by @bonaventure-wong)

## Blockers

- HR scoring engine cannot be validated yet because Jehad only has one candidate with both pre- and post-interview data. (blocks: [[hr-scoring-engine]]; owner: @jehad-altoutou)

## Tool mentions

- [[obsidian]] — knowledge-graph substrate hosting the Prime Radiant vault
- [[claude-cowork]] — the build environment used to construct the Prime Radiant in a day
- [[fireflies]] — raw transcript source feeding the wiki; summaries explicitly rejected as insufficient
- [[linear]] — system of record contributing the AI tools registry into the wiki
- [[monday-com]] — system of record contributing tasks into the wiki
- [[notion]] — system of record contributing notes/operations entries into the wiki
- [[obsidian-web-clipper]] — manual article-clipping flow that becomes the Singapore news feed for Marketing
- [[google-drive]] — current substrate (Shared Drive) for the Prime Radiant vault
- [[pinecone]] — cited as one of several vendors pushing memory engineering to a tipping point
- [[assessify]] — backend platform for the HR recruitment pipeline, exposes an MCP server
- [[deel]] — treated as just a database in HR's target architecture, with the Prime Radiant as the front end
- [[remarkable]] — analogous bookmark-to-device flow compared to Obsidian's clipper

## Topics

- prime-radiant
- obsidian-knowledge-graph
- department-rollout
- recruitment-pipeline
- scoring-rubric
- assessify-mcp
- upskilling
- digital-twin

## Related

- Concept: [[prime-radiant]] — core artefact demoed in the meeting; named after Asimov's psychohistory device
- Concept: [[llm-wiki]] — Karpathy gist that seeded the Prime Radiant build
- Concept: [[agent-memory]] — framed as the industry trend making the Prime Radiant feasible
- Concept: [[knowledge-graph]] — Obsidian's underlying data structure cited as the differentiator vs RAG
- Concept: [[digital-twin]] — Bonaventure's framing of the long-term destination for the Prime Radiant
- Concept: [[compounding-learning]] — explicit framing for how the scoring engine and the wiki improve over time
- Concept: [[upskilling]] — tied to the Singapore PM's labour-force programme and Janus's onsite AI training pitch
- Project: [[janus-prime-radiant-build]] — the cross-department rollout programme owning this work
- Project: [[hr-recruitment-pipeline]] — Assessify-backed pipeline with JD builder, intake form, scoring rubric demoed in the meeting
- Project: [[uber-for-engineers]] — long-horizon marketplace tied to the HR scoring engine
- Vendor: [[obsidian]] — vault substrate for the Prime Radiant
- Vendor: [[claude-cowork]] — build environment for the prototype
- Vendor: [[assessify]] — HR pipeline backend with MCP connector
- Vendor: [[fireflies]] — raw transcript source
- Vendor: [[linear]] — AI registry SoR feeding the wiki
- Vendor: [[monday-com]] — task SoR feeding the wiki
- Vendor: [[notion]] — notes/ops SoR feeding the wiki
- Vendor: [[pinecone]] — industry signal cited in the agent-memory trend
- Vendor: [[deel]] — treated as backend database for HR in target architecture
- Person: [[andrew-soane]] — Marketing lead; named as first cross-dept Prime Radiant rollout target and journalist-dossier driver
- Person: [[theresa-wong]] — HR lead; primary user of the recruitment pipeline and source of intake requirements
- Person: [[andrej-karpathy]] — LLM-wiki gist that seeded the Prime Radiant
- Person: [[maryam]] — prior owner of the HR assessment files Jehad reverse-engineered the rubric from
- Person: [[janet]] — now has access to the shared-drive Prime Radiant vault
- Person: [[jenna]] — built the front end to the HR scoring system; collaborating with Bonaventure
- Person: [[the-sender]] — long-time Obsidian user inside Janus; product/PM background, finishing a training cycle

---

## Transcript

Raw transcript stays in Fireflies — fetch via MCP when needed.
Fireflies: [original meeting](https://app.fireflies.ai/view/01KR3MEP5PSM0TS6F92J9PZKJ5)
