# Wiki Index

_Updated: 2026-05-20 (**Marketing stack batch ingest + lint + lint-followup.** Michael's technical writeup (Michael → Jehad, 2026-05-19) filed alongside the 2026-05-19 AIO-Marketing meeting transcript. Locks the marketing stack on Cosmic CMS, Attio CRM, Vercel hosting, Cloudflare edge/DNS, Resend transactional, Cookiebot consent — Mailchimp held open (Rejected → Backlog) pending Andrew's post-launch decision. **Singapore lunch postponed July → September 2026** per Bonaventure / Joyce — campaign continues on original timeline. **Two net-new wiki pages**: [[stack-composition-framework]] (concept) — three lenses (composability, agent operability, reversibility) proposed as **pre-G1 filter** to the formal [[ai-tool-evaluation-framework]]; [[agentic-lean-marketing-stack]] (brief) — the strategic aha tying the framework + tool picks to AIO's agentic-lean operating thesis. Updates: [[resend]], [[mailchimp]], [[monday]] (explicit not-a-CRM), [[janus-website-cms]] (Cosmic locked), [[janus-crm-selection]] (Attio locked, flipped from HubSpot-leaning), [[singapore-launch]] (10-day operational plan + Sept postponement), [[janus-website]] (Hostinger → Vercel+Cloudflare delta), [[crm-evaluation-and-selection]] (flip recorded), [[ai-tool-evaluation-framework]] (pre-G1 proposal noted). 1 escalation: [[ingest-2026-05-20-1145-create-marketing-stack-vendor-pages]] proposing vendor stubs for Cosmic, Attio, Vercel, Cloudflare, Cookiebot. Lint pass run after — see [[2026-05-20-lint]]. **Lint-followup same day (Michael-driven):** (1) merged duplicate `ai-registry` slug — folded `concepts/ai-registry.md` content (gate framework + lessons list) into `processes/ai-registry.md` then deleted the duplicate; (2) **CLAUDE.md v0.12** — new attribution-discipline rule in §5.1 Meetings: Fireflies speaker labels are unreliable due to shared-mic and untagged-speaker artefacts; downstream attribution requires corroboration (curator confirmation, non-Fireflies source, or prior `decided_by:` field); (3) promoted 3 recurring-lint-missing-page slugs to substantive stubs at `projects/notion-operations-notebook-restructure.md`, `projects/build-categorisation-taxonomy-for-ai-tools.md`, `projects/apply-standup-methodology-to-andrew-work-stream.md`. 7 ingests since last lint cleared; counter reset.)_

> Content catalog for **Janus Prime Radiant · AI Office**. One line per page, grouped by category. See `CLAUDE.md` for the schema and update rules.

## Vendors

- [anthropic](entities/vendors/anthropic.md) — AI safety/research company; parent of the Claude product family. [active, high]
- [anthropic-claude](entities/vendors/anthropic-claude.md) — legacy slug for the Claude product family; thin redirect to [[claude]]. [superseded]
- [assessify](entities/vendors/assessify.md) — HR/candidate-assessment platform; bridge for Janus recruitment automation pipeline. [active, medium]
- [claude](entities/vendors/claude.md) — Anthropic product family: Claude models, Claude Code, Claude Managed Agents, Cowork, Claude in Chrome. [active, high]
- [canva](entities/vendors/canva.md) — web-based graphic design platform; Marketing candidate (AIO-99, Backlog, Gate 1 BLOCKED). [active, low]
- [claude-code](entities/vendors/claude-code.md) — Anthropic's CLI/IDE coding agent; thin pointer to umbrella [[claude]] entry. [active, high]
- [deel](entities/vendors/deel.md) — HR/payroll platform; used as headless backend at Janus. [active, medium]
- [fireflies](entities/vendors/fireflies.md) — meeting transcription; system of record for "what was said" at Janus. [active, high]
- [github](entities/vendors/github.md) — code hosting + version control; confirmed substrate for Prime Radiant vault sync as of 2026-05-13. [active, high]
- [google-cloud](entities/vendors/google-cloud.md) — GCP arm; Agentic Data Cloud, Skills Repo, A2A protocol push. [active, high]
- [hostinger](entities/vendors/hostinger.md) — hosting/infrastructure; Sandbox in Linear AIR. [active, medium]
- [linear](entities/vendors/linear.md) — issue tracker; system of record for the AI Tool Registry (AIR). [active, high]
- [linkedin-marketing-solutions](entities/vendors/linkedin-marketing-solutions.md) — B2B advertising and lead generation suite; Marketing/Commercial candidate (AIO-98, Backlog, Gate 1 BLOCKED). [active, low]
- [mailchimp](entities/vendors/mailchimp.md) — email marketing platform (Intuit); AIR-111 Backlog (hold-open) pending Andrew's broadcast-email decision post-Singapore. [active, medium]
- [marketo](entities/vendors/marketo.md) — Adobe Marketo Engage; marketing automation candidate signal source. [monitored, low]
- [marp](entities/vendors/marp.md) — markdown-based slide/presentation tool. [active, high]
- [microsoft-clarity](entities/vendors/microsoft-clarity.md) — website analytics and heatmapping tool (Microsoft, free); Marketing/Technology candidate (AIO-102, Backlog, Gate 1 BLOCKED). [active, low]
- [monday](entities/vendors/monday.md) — work management; primary execution surface for Janus tasks/projects. [active, high]
- [n8n](entities/vendors/n8n.md) — open-source workflow automation; self-hosted on Hostinger; operational plumbing for AIO ingestion pipelines. [active, medium]
- [nanoclaw](entities/vendors/nanoclaw.md) — open-source self-hosted AI agent orchestration framework (NanocoAI); MIT licence; Docker isolation per agent; Anthropic Agent SDK native; native Slack Socket Mode; identified as personal AI chief-of-staff candidate (AIR-103, Gate 1 PASS, Evaluating). [active, medium]
- [nemoclaw](entities/vendors/nemoclaw.md) — NVIDIA enterprise-hardened OpenClaw derivative; production tier-1 agent infrastructure (AIR-39). [active, medium]
- [notebooklm](entities/vendors/notebooklm.md) — Google's note-taking+Q&A product; retired 2026-05-11 in favour of HTML outputs. [archived, medium]
- [notion](entities/vendors/notion.md) — workspace and docs; Operations Notebook journal/reporting surface. [active, high]
- [resend](entities/vendors/resend.md) — developer-focused transactional email API; **confirmed for marketing stack** AIR-118, 3/3 on Stack Composition Framework; Broadcasts feature may obsolete the need for Mailchimp. [active, high]
- [obsidian](entities/vendors/obsidian.md) — markdown editor; the wiki interface. [high]
- [openai](entities/vendors/openai.md) — frontier model / agent-platform vendor; Janus posture: monitor, not adopt as primary. [monitored, high]
- [openclaw](entities/vendors/openclaw.md) — open-source AI agent framework; OSS baseline for [[nemoclaw]]. [active, medium]
- [pinecone](entities/vendors/pinecone.md) — vector DB pivoting to "knowledge engine" with Nexus. [active, high]
- [slack](entities/vendors/slack.md) — real-time messaging; AI Hub channel + AI Internal Hub agentic workflow target. [active, high]
- [viktor](entities/vendors/viktor.md) — agent/integration platform rejected at AIR-38; precedent for per-user access policy. [archived, medium]
- [vs-code](entities/vendors/vs-code.md) — Microsoft's code editor; one of Michael's two primary editors. [active, high]
- [wispr-flow](entities/vendors/wispr-flow.md) — voice dictation; Linear AIR-92 (Backlog) for ISO facilitation. [active, medium]
- [zed](entities/vendors/zed.md) — Rust-based code editor; one of Michael's two primary editors. [active, high]

## Clients

_(none yet)_

## People (external)

- [andrej-karpathy](entities/people/andrej-karpathy.md) — AI researcher; authored the LLM Wiki gist that inspired this wiki. [high]
- [vivian-balakrishnan](entities/people/vivian-balakrishnan.md) — SG Foreign Minister; runs personal LLM wiki on Raspberry Pi; potential SG-government advocate for Prime Radiant pattern (relationship via Bonaventure). [high]
- [yusuf-apple-dubai](entities/people/yusuf-apple-dubai.md) — Apple Store Dubai sales associate; 3rd-year CS student at AUD; potential internship candidate for non-technical-AIO-rollout interface role. [active, low]

## People (internal)

- [andrew-soane](entities/internal/andrew-soane.md) — CMO; standup-skill rollout pilot; recurring weekly cadence with Michael.
- [andrey-timokhov](entities/internal/andrey-timokhov.md) — IT/Operations team; reports to Euclid; co-designs the IT standup pilot and helpdesk triage bot.
- [dhyey-mehta](entities/internal/dhyey-mehta.md) — IT team, recent joiner under Euclid; first wiki touchpoint = 2026-05-15 Singapore strategy alignment session; role detail TBD.
- [ann-greed](entities/internal/ann-greed.md) — Financial Controller; finance-touching tool decisions and procurement approval.
- [bonaventure-wong](entities/internal/bonaventure-wong.md) — CEO; sponsor of ISO programme + Singapore news bot; strict-policy holder.
- [euclid-wong](entities/internal/euclid-wong.md) — Head of three teams (IT, Project Management, Operations); IT approved-tools list owner; CRM lock-in stakeholder; sponsor on the Project Management Prime Radiant rollout.
- [jehad-altoutou](entities/internal/jehad-altoutou.md) — AI Office; owner of the `/standup` skill; engineering lead on most active projects.
- [joyce-woo](entities/internal/joyce-woo.md) — CEO Janus Digital Singapore; co-signed author of the Janus SG white paper; BW/JW direct-outreach pairing on the SG launch campaign; 40+ years SG banking (DBS Finance → Merrill Lynch → OCBC Private Bank → Citi/UBS/MS/BoS → Jachin Capital → Leo Wealth → Janus).
- [lysander-liu](entities/internal/lysander-liu.md) — Head of Project Management (operational lead); authored the 28-phase digital delivery workflow; curator candidate for the Project Management Prime Radiant.
- [mariam-mahmood](entities/internal/mariam-mahmood.md) — HR; sample-data provider for the recruitment-automation pipeline.
- [michael-bruck](entities/internal/michael-bruck.md) — AI Office; owner of this wiki.
- [rosa-wu](entities/internal/rosa-wu.md) — Co-head of Project Management (with Euclid); dashboard track owner on the Project Management Prime Radiant.
- [simon-tarskih](entities/internal/simon-tarskih.md) — ISO programme facilitator; working partner on the [[iso-compliance-programme]].
- [spike-zhao](entities/internal/spike-zhao.md) — Digital modeling engineer; Project Management delivery side; works in Phases 16–18 of the workflow.
- [theresa-wong](entities/internal/theresa-wong.md) — Head of HR; sponsor of the recruitment-automation pipeline.

## Departments

- [ai-office](entities/departments/ai-office.md) — AI strategy, tools, adoption; Michael curator; canonical Prime Radiant instance live (this wiki).
- [engineering](entities/departments/engineering.md) — stub; vocabulary placeholder; routes through ai-office and it-ops for now.
- [finance](entities/departments/finance.md) — Financial Controller seat (Ann Greed); Prime Radiant instance queued; CFO seat open question.
- [hr](entities/departments/hr.md) — Theresa head, Mariam operator; recruitment-automation pipeline; instance queued.
- [iso](entities/departments/iso.md) — Simon programme lead; ISO 9001/27001/42001 compliance function; cross-cutting across every department; instance queued (added to vocabulary 2026-05-11).
- [it-ops](entities/departments/it-ops.md) — Euclid head (three teams: IT, Project Management, Operations); Andrey on IT; production handover from AIO. Project Management instance is pilot #2 after Marketing (Rosa, Lysander, Spike, Euclid).
- [marketing](entities/departments/marketing.md) — Andrew CMO; Prime Radiant instance kicking off 2026-05-08; Andrew confirmed active test case (2026-05-11); ICP/Personas pending.
- [office-of-ceo](entities/departments/office-of-ceo.md) — Bonaventure; ISO programme; will be the digital-knowledge-twin federation endpoint.
- [training](entities/departments/training.md) — stub; newly added vocabulary; instance queued.

## Concepts

- [agent-harness](concepts/agent-harness.md) — orchestration layer around an LLM; locus of memory, tools, retries, optimisation. [medium]
- [agent-memory](concepts/agent-memory.md) — how agents persist and recall across sessions; dominant 2026 theme. [high]
- [agent-skills](concepts/agent-skills.md) — packaged, condensed expertise loaded on demand; multi-vendor pattern. [high]
- [agent-to-agent-protocol](concepts/agent-to-agent-protocol.md) — A2A; horizontal protocol for agent-agent communication. [medium]
- [agentic-ai](concepts/agentic-ai.md) — umbrella term for autonomous, tool-using AI systems; broad framing. [high]
- [context-engineering](concepts/context-engineering.md) — discipline of pre-shaping data into agent-usable knowledge. [high]
- [gist-pattern-as-template-replacement](concepts/gist-pattern-as-template-replacement.md) — Karpathy gist pattern as a replacement for rigid templates; adaptable starting points expanded by LLM under local context. [high]
- [knowledge-compilation](concepts/knowledge-compilation.md) — pre-compiled knowledge artefacts beat runtime retrieval; the architectural pattern behind Prime Radiant, Pinecone Nexus, Google Knowledge Catalog. [high]
- [llm-wiki](concepts/llm-wiki.md) — methodology for LLM-maintained personal/organisational knowledge bases. [high]
- [model-context-protocol](concepts/model-context-protocol.md) — MCP; vertical protocol for LLM-to-tools integration. [high]
- [peer-to-peer-mesh-federation-pattern](concepts/peer-to-peer-mesh-federation-pattern.md) — mesh federation for the Prime Radiant rollout; each department-to-department relationship gets its own shared subfolder; filesystem-level federation, not event-broker. [high]
- [prime-radiant-three-layer-architecture](concepts/prime-radiant-three-layer-architecture.md) — Signals / Infrastructure / Outputs decomposition for any Prime Radiant instance; canonical architecture. [high]
- [ralph-loop-pattern](concepts/ralph-loop-pattern.md) — naive-persistence iteration pattern; unsanitized failure feedback drives convergence. [high]
- [retrieval-augmented-generation](concepts/retrieval-augmented-generation.md) — RAG pattern; predecessor to compilation-stage knowledge layers. [high]
- [stack-composition-framework](concepts/stack-composition-framework.md) — three-lens evaluation layer (composability, agent operability, reversibility) proposed as pre-G1 filter to the formal AI Tool Evaluation Framework. First applied 2026-05-19 to the marketing stack. [high]

## Processes

- [ai-policy-gate-approval](processes/ai-policy-gate-approval.md) — reusable governance process for moving an AI tool from active use to formal approval; 4-of-4 gate, 8-step flow, 4-system coordination.
- [ai-registry](processes/ai-registry.md) — Linear AIR management conventions; pipeline stages + gate framework summary + running lessons list; reference page pointing at the canonical `/ai-registry` skill. Concept-folder duplicate folded in 2026-05-20.
- [ai-tool-evaluation](processes/ai-tool-evaluation.md) — Janus's gate-based AI tool evaluation framework; reference page pointing at the canonical `/ai-tool-evaluation` skill.
- [janus-html-deck-brand-guideline](processes/janus-html-deck-brand-guideline.md) — v1.0 brand guideline for HTML decks (derived from the official Janus brand book): brand orange #FCB745, navy #013A7D, blue #028CDC, Montserrat, official SVG logo. Scoped to logos / fonts / colour palette — verbal brand being refreshed by Andrew's agency.
- [project-management-digital-delivery-workflow](processes/project-management-digital-delivery-workflow.md) — Janus PM's end-to-end project delivery workflow (28 phases); the canonical reference the PM Prime Radiant initialises against.
- [prime-radiant-instance-setup](processes/prime-radiant-instance-setup.md) — curator-side runbook for standing up a new Prime Radiant instance end-to-end; embedded bash script automates repo + local-vault + initial-commit-and-push; GUI sequence for branch protection, Obsidian, Cowork.
- [standup](processes/standup.md) — AIO daily standup workflow (Fireflies → Monday → Linear AIP → Notion); reference page pointing at the canonical `/standup` skill (v3.13).

## Projects

- [april-2026-aio-transcripts-recovery](projects/april-2026-aio-transcripts-recovery.md) — recover the ~22 April 2026 AIO standup entries lost from Notion by re-running raw Fireflies transcripts through synthesis. [active]
- [assessify-hr-assessment-platform](projects/assessify-hr-assessment-platform.md) — Assessify — HR Assessment Platform. [active]
- [crm-evaluation-and-selection](projects/crm-evaluation-and-selection.md) — locking down Janus's CRM platform choice (HubSpot / Attio / Salesforce / Pipedrive); 2–3 year architectural commitment. [active]
- [iso-compliance-programme](projects/iso-compliance-programme.md) — multi-track ISO compliance work (documentation foundation + ai-tool-eval ISO alignment + standup skill ISO alignment + /ims-enrolment skill + PULS programme detail); top priority for Bonaventure. [active]
- [it-department-standup-pilot](projects/it-department-standup-pilot.md) — rolling out the AIO standup methodology to IT; sibling to Andrew's Marketing pilot. [active]
- [it-helpdesk-triage-bot](projects/it-helpdesk-triage-bot.md) — Slack→triage→Zendesk agentic workflow for IT support requests. [active]
- [janus-prime-radiant-build](projects/janus-prime-radiant-build.md) — program-level hub: rolling out Janus Prime Radiant instances across departments toward a company-wide digital knowledge twin. CEO-level validation received 2026-05-18; program now explicitly scoped toward a company-wide unified KB per CEO direction. [active]
- [marketing-prime-radiant](projects/marketing-prime-radiant.md) — Marketing-domain Prime Radiant instance; pilot kicked off 2026-05-08 with Andrew Soane. [active]
- [recruitment-automation-pipeline](projects/recruitment-automation-pipeline.md) — full CV-to-hire pipeline; HR Dashboard board (28 items). [active]
- [singapore-news-monitoring](projects/singapore-news-monitoring.md) — market-intelligence agent for the Singapore office; Bonaventure-driven. [active]

## Decisions

- [2026-05-18-ceo-global-kb-unified-market-ui](decisions/2026-05-18-ceo-global-kb-unified-market-ui.md) — CEO Bonaventure Wong: one unified global knowledge base, market-specific UI layer, open access. Singapore two-layer model (read-access to global + local vault feeds back). Obsidian single-repo limitation deferred. [active]
- [2026-05-18-nanoclaw-as-personal-ai-coa-candidate](decisions/2026-05-18-nanoclaw-as-personal-ai-coa-candidate.md) — NanoClaw identified as personal AI chief-of-staff candidate for Slack bot sprawl resolution; one bot per person; AIR-103 Gate 1 PASS; Gate 2 pending. [active]
- [2026-05-18-website-react-typescript-full-rebuild](decisions/2026-05-18-website-react-typescript-full-rebuild.md) — website scope expanded from landing-page to full React/TypeScript rebuild; GDPR consent popup + Mailchimp integration required for Singapore campaign compliance. [active]
- [2026-05-13-prefer-html-over-powerpoint-for-claude-generated-decks](decisions/2026-05-13-prefer-html-over-powerpoint-for-claude-generated-decks.md) — Prefer HTML over PowerPoint for Claude-generated decks. [resolved]
- [2026-05-13-migrate-prime-radiant-vaults-from-google-drive-to-github](decisions/2026-05-13-migrate-prime-radiant-vaults-from-google-drive-to-github.md) — Migrate Prime Radiant vaults from Google Shared Drive to GitHub. [resolved]
- [2026-05-13-defer-paid-github-org-pending-bonaventure-approval](decisions/2026-05-13-defer-paid-github-org-pending-bonaventure-approval.md) — "Defer paid GitHub org upgrade pending Bonaventure's approval". [resolved]
- [2026-05-13-andrew-soane-first-cross-dept-prime-radiant-rollout](decisions/2026-05-13-andrew-soane-first-cross-dept-prime-radiant-rollout.md) — Andrew Soane is the first cross-department Prime Radiant rollout. [resolved]
- [2026-05-12-three-messaging-pillars](decisions/2026-05-12-three-messaging-pillars.md) — "Three messaging pillars: SG sustainability, AI as growth engine, individual augmentation". [resolved]
- [2026-05-12-start-marketing-prime-radiant-without-waiting-for-crm](decisions/2026-05-12-start-marketing-prime-radiant-without-waiting-for-crm.md) — Start the marketing Prime Radiant rollout this week without waiting for the CRM. [resolved]
- [2026-05-12-single-domain-gems-com-with-country-paths](decisions/2026-05-12-single-domain-gems-com-with-country-paths.md) — "Single gems.com domain with country sub-paths, not standalone country sites". [resolved]
- [2026-05-14-personal-vaults-shelved-pending-federation-redesign](decisions/2026-05-14-personal-vaults-shelved-pending-federation-redesign.md) — personal vaults deferred from rollout; team brains only for Project Management + future departments; revisit after federation-architecture redesign on the GitHub substrate. [resolved]
- [2026-05-14-windows-as-first-non-mac-deployment](decisions/2026-05-14-windows-as-first-non-mac-deployment.md) — Project Management rollout is also Janus's first Windows deployment of Prime Radiant; controlled platform-test framing for all subsequent Windows-team rollouts. [resolved]
- [2026-05-12-singapore-as-lead-market](decisions/2026-05-12-singapore-as-lead-market.md) — Singapore confirmed as Janus's lead commercial market for AI Native products; UAE deprioritised for streaming-economy products on banking-infrastructure grounds. [resolved]
- [2026-05-12-reorder-deck-outputs](decisions/2026-05-12-reorder-deck-outputs.md) — "Reorder the deck's 'outputs' section: plans/campaigns first, then briefs/positioning, then POVs/white papers/assets". [resolved]
- [2026-05-12-marketing-pr-outputs-reordered](decisions/2026-05-12-marketing-pr-outputs-reordered.md) — Marketing PR Outputs reordered: plans / campaigns first, briefs / positioning second, POVs / white papers third. Counters Bonaventure white-paper-centric framing. [resolved]
- [2026-05-12-interim-lead-capture-via-google-form-sheet](decisions/2026-05-12-interim-lead-capture-via-google-form-sheet.md) — "Interim Singapore lead capture via Google Form into Google Sheets, pre-CRM". [resolved]
- [2026-05-12-html-as-presentation-format-adopted](decisions/2026-05-12-html-as-presentation-format-adopted.md) — HTML adopted as default presentation output format; CEO-endorsed; PowerPoint exception, not rule. [resolved]
- [2026-05-12-generalise-factset-to-news-sources](decisions/2026-05-12-generalise-factset-to-news-sources.md) — "Drop FactSet name from the deck; generalise to 'news sources / information gathering'". [resolved]
- [2026-05-11-notion-restricted-to-aio-no-broad-rollout](decisions/2026-05-11-notion-restricted-to-aio-no-broad-rollout.md) — Bonaventure: no additional Notion seats beyond AIO; non-AIO users use Drive + Prime Radiant; validates the wiki-as-substitute pattern. [resolved]
- [2026-05-11-notebooklm-retirement-html-over-image-outputs](decisions/2026-05-11-notebooklm-retirement-html-over-image-outputs.md) — retire NotebookLM for org-chart / presentation outputs; use HTML instead (editable, version-controllable, browser-native, cheaper). [resolved]
- [2026-05-08-prime-radiant-storage-on-shared-drive](decisions/2026-05-08-prime-radiant-storage-on-shared-drive.md) — "Prime Radiant vault lives on Janus Google Shared Drive, not personal Drive". [resolved]
- [2026-05-08-per-department-prime-radiant-instances](decisions/2026-05-08-per-department-prime-radiant-instances.md) — Each Janus department gets its own Prime Radiant instance. [resolved]
- [2026-05-08-package-iso-template-as-skill](decisions/2026-05-08-package-iso-template-as-skill.md) — Package the ISO process generator as a reusable Claude skill for other departments. [resolved]
- [2026-05-08-obsidian-as-personal-and-dept-brain](decisions/2026-05-08-obsidian-as-personal-and-dept-brain.md) — Adopt Obsidian as the substrate for personal and department-level Janus brains with shared-folder federation. [resolved]
- [2026-05-08-new-recruiter-owns-rubric-fine-tuning](decisions/2026-05-08-new-recruiter-owns-rubric-fine-tuning.md) — Incoming recruiter (starts next month) will own scorecard and JD fine-tuning. [resolved]
- [2026-05-08-marketing-prime-radiant-greenlit-with-andrew](decisions/2026-05-08-marketing-prime-radiant-greenlit-with-andrew.md) — Marketing Prime Radiant pilot greenlit; Karpathy-gist incremental build with Andrew as engaged stakeholder; runs in parallel with continued AIO honing. [resolved]
- [2026-05-08-marketing-prime-radiant-as-separate-vault](decisions/2026-05-08-marketing-prime-radiant-as-separate-vault.md) — Marketing Prime Radiant gets its own Google Shared Drive folder + own CLAUDE.md derived from AIO; sets the federation precedent for all subsequent department instances; pre-CRM design and architecture work proceeds immediately. [resolved]
- [2026-05-08-iso-process-template-shape](decisions/2026-05-08-iso-process-template-shape.md) — "ISO/IMS process documents follow Simon's standard structure: source, receiver, inputs, activities, controls, resources". [resolved]
- [2026-05-08-fireflies-summaries-rejected-use-raw-transcript](decisions/2026-05-08-fireflies-summaries-rejected-use-raw-transcript.md) — Reject Fireflies summaries; ingest only raw transcripts. [resolved]
- [2026-05-08-assessify-mcp-as-hr-claude-surface](decisions/2026-05-08-assessify-mcp-as-hr-claude-surface.md) — Assessify exposes recruitment pipeline to Claude via MCP. [resolved]
- [2026-05-08-ai-ops-three-phase-orchestration](decisions/2026-05-08-ai-ops-three-phase-orchestration.md) — "AI Ops task pipeline structured as three-phase orchestration (Analyze, Plan, Execute)". [resolved]
- [2026-05-07-rubric-scoring-as-claude-skill](decisions/2026-05-07-rubric-scoring-as-claude-skill.md) — Rubric scoring rebuilt as a Claude skill; API direct for production, MCP for low-volume rubric creation; $1.12/CV economics. [resolved]
- [2026-05-07-public-restricted-folder-split-per-department](decisions/2026-05-07-public-restricted-folder-split-per-department.md) — Each department Shared Drive splits into a public and a restricted folder. [resolved]
- [2026-05-07-per-workstream-api-keys-cost-monitoring](decisions/2026-05-07-per-workstream-api-keys-cost-monitoring.md) — per-workstream Claude API keys + weekly cost reports to HR + finance. [resolved]
- [2026-05-07-llm-wiki-extends-to-marketing-domain](decisions/2026-05-07-llm-wiki-extends-to-marketing-domain.md) — Janus Prime Radiant prototype validated; sibling marketing-domain instance to be built for Andrew. [resolved]
- [2026-05-07-google-shared-drives-as-company-doc-store](decisions/2026-05-07-google-shared-drives-as-company-doc-store.md) — Google Shared Drives are the company-wide document store. [resolved]
- [2026-05-07-google-groups-drive-permissions](decisions/2026-05-07-google-groups-drive-permissions.md) — "Drive permissions are managed via Google Groups, not per-user grants". [resolved]
- [2026-05-07-department-head-owns-contributors](decisions/2026-05-07-department-head-owns-contributors.md) — "Department heads, not IT, manage contributor membership on their drives". [resolved]
- [2026-05-07-ai-office-knowledge-stack-stays-internal](decisions/2026-05-07-ai-office-knowledge-stack-stays-internal.md) — "AI Office's Linear/Monday/Notion/Fireflies/Claude stack stays AI-Office-internal". [resolved]
- [2026-05-07-ai-office-and-it-pilot-drive-structure](decisions/2026-05-07-ai-office-and-it-pilot-drive-structure.md) — AI Office and IT pilot the Shared Drive + groups structure first. [resolved]
- [2026-05-06-standup-skill-v3-12-self-correcting-behavior](decisions/2026-05-06-standup-skill-v3-12-self-correcting-behavior.md) — v3.12 sub-skill orchestration validated by self-correction in Linear AIR. [resolved]
- [2026-05-06-slack-tool-intake-as-agentic-workflow-not-bot](decisions/2026-05-06-slack-tool-intake-as-agentic-workflow-not-bot.md) — internal hub Slack intake reframed as agentic workflow with SLA + status loop. [resolved]
- [2026-05-06-skills-stay-as-skills-not-plugins](decisions/2026-05-06-skills-stay-as-skills-not-plugins.md) — AIO tooling stays as Claude Skills, not Cowork plugins. [resolved]
- [2026-05-06-pilot-knowledge-pipeline-with-it](decisions/2026-05-06-pilot-knowledge-pipeline-with-it.md) — Pilot the Fireflies-to-Monday-Notion-Linear knowledge pipeline with IT Ops first. [resolved]
- [2026-05-06-notion-role-shift-journal-not-knowledge-base](decisions/2026-05-06-notion-role-shift-journal-not-knowledge-base.md) — Notion shifts to journal + dept pages; durable knowledge moves to Markdown wiki. [resolved]
- [2026-05-06-monday-rollout-standard-issue](decisions/2026-05-06-monday-rollout-standard-issue.md) — Monday.com will be rolled out company-wide as standard issue. [resolved]
- [2026-05-06-monday-not-an-ai-tool](decisions/2026-05-06-monday-not-an-ai-tool.md) — Monday.com is not an AI tool and stays out of the AI registry. [resolved]
- [2026-05-06-monday-com-to-production-this-week](decisions/2026-05-06-monday-com-to-production-this-week.md) — promote Monday.com sandbox→production this week; CRM lock-in same window. [resolved]
- [2026-05-06-backlog-cleanup-no-return-to-backlog](decisions/2026-05-06-backlog-cleanup-no-return-to-backlog.md) — post-evaluation tools never return to Linear AIR Backlog. [resolved]
- [2026-05-06-andrew-as-standup-skill-rollout-pilot](decisions/2026-05-06-andrew-as-standup-skill-rollout-pilot.md) — Andrew is the formal first external rollout target. [resolved]
- [2026-05-06-ai-tool-taxonomy-scope-policy](decisions/2026-05-06-ai-tool-taxonomy-scope-policy.md) — Monday/Notion/Deel/Xero/Airwallex are not AI tools; scope policy locks the AIR boundary. [resolved]
- [2026-05-06-add-claude-cowork-to-approved-tools](decisions/2026-05-06-add-claude-cowork-to-approved-tools.md) — Add Claude Cowork to the v3 approved-tools list. [resolved]
- [2026-05-05-website-build-in-house-not-agency](decisions/2026-05-05-website-build-in-house-not-agency.md) — "Build the new Janus website in-house with Lovable + Claude, not an agency". [resolved]
- [2026-05-05-start-with-source-and-input-only](decisions/2026-05-05-start-with-source-and-input-only.md) — "Document only source and input first, defer activity/output". [resolved]
- [2026-05-05-stand-up-ai-marketing-workspace](decisions/2026-05-05-stand-up-ai-marketing-workspace.md) — Stand up dedicated AI-marketing workspace (Claude project + Drive folder + Slack channel). [resolved]
- [2026-05-05-slack-is-canonical-source-of-tool-requests](decisions/2026-05-05-slack-is-canonical-source-of-tool-requests.md) — Slack is the canonical source for AI tool-evaluation requests. [resolved]
- [2026-05-05-skills-follow-input-activity-output-structure](decisions/2026-05-05-skills-follow-input-activity-output-structure.md) — Skills will be written in input/activity/output ISO structure. [resolved]
- [2026-05-05-recruitment-scoring-as-claude-skill](decisions/2026-05-05-recruitment-scoring-as-claude-skill.md) — recruitment scoring rebuilt from Bonaventure project + thread to a reusable Claude skill. [resolved]
- [2026-05-05-policy-baked-into-skill-not-separate-input](decisions/2026-05-05-policy-baked-into-skill-not-separate-input.md) — "AI policy is baked into the skill, not passed as a separate input". [resolved]
- [2026-05-05-move-eval-table-to-shared-google-doc](decisions/2026-05-05-move-eval-table-to-shared-google-doc.md) — Move the evaluation framework table from Word to a shared Google Doc. [resolved]
- [2026-05-05-markdown-as-canonical-format](decisions/2026-05-05-markdown-as-canonical-format.md) — Markdown is the canonical interchange format for AI-marketing source material. [resolved]
- [2026-05-05-kb-direction-markdown-progressive-exposure-not-rag](decisions/2026-05-05-kb-direction-markdown-progressive-exposure-not-rag.md) — KB direction = Markdown + front-matter + progressive exposure; not RAG. [resolved]
- [2026-05-05-janus-needs-a-crm](decisions/2026-05-05-janus-needs-a-crm.md) — Janus must adopt a CRM despite the long-term SaaS-replacement vision. [resolved]
- [2026-05-05-github-as-skill-library](decisions/2026-05-05-github-as-skill-library.md) — "GitHub is the skill library, treated as source code". [resolved]
- [2026-05-05-flow-first-skill-later](decisions/2026-05-05-flow-first-skill-later.md) — Document the evaluation flow first; convert to a Claude skill later. [resolved]
- [2026-05-05-five-marketing-capabilities-scoped](decisions/2026-05-05-five-marketing-capabilities-scoped.md) — Scope five core marketing capabilities for AI build-out. [resolved]
- [2026-05-05-defer-finance-and-legal-from-tool-eval-pipeline](decisions/2026-05-05-defer-finance-and-legal-from-tool-eval-pipeline.md) — Finance/contracts/legal are not part of the tool-evaluation pipeline. [resolved]
- [2026-05-05-crm-shortlist-for-evaluation](decisions/2026-05-05-crm-shortlist-for-evaluation.md) — "CRM shortlist for AI Registry evaluation: HubSpot, Attio, Monday CRM, Salesforce". [resolved]
- [2026-05-04-tool-intake-form-fields](decisions/2026-05-04-tool-intake-form-fields.md) — Lock the Slack intake form fields for new AI tool requests. [resolved]
- [2026-05-04-standup-confidence-bands](decisions/2026-05-04-standup-confidence-bands.md) — Use three confidence bands for standup-skill auto-updates. [resolved]
- [2026-05-04-reject-vs-watchlist-rejection-paths](decisions/2026-05-04-reject-vs-watchlist-rejection-paths.md) — Split rejection into hard-reject and watch-list with documented rationale. [resolved]
- [2026-05-04-recruitment-execution-on-hr-dashboard-board](decisions/2026-05-04-recruitment-execution-on-hr-dashboard-board.md) — recruitment automation execution on dedicated HR Dashboard Monday board. [resolved]
- [2026-05-04-monday-for-projects-linear-for-registry](decisions/2026-05-04-monday-for-projects-linear-for-registry.md) — "Split tool tracking from project tracking: Linear for AI Registry, Monday for projects". [resolved]
- [2026-05-04-iso-source-input-activity-output-template](decisions/2026-05-04-iso-source-input-activity-output-template.md) — Adopt Source/Input/Activity/Output as the standard ISO-style template for every pipeline stage. [resolved]
- [2026-05-04-discard-fireflies-summary](decisions/2026-05-04-discard-fireflies-summary.md) — "Ignore Fireflies' own summary; use only the raw transcript". [resolved]
- [2026-05-04-centralised-fireflies-webhook-for-interviews](decisions/2026-05-04-centralised-fireflies-webhook-for-interviews.md) — interview transcript capture via centralised Fireflies invitee + webhook. [resolved]
- [2026-05-04-ai-policy-gate-is-binary-four-of-four](decisions/2026-05-04-ai-policy-gate-is-binary-four-of-four.md) — AI policy evaluation gate is a 4-of-4 hard binary check. [resolved]
- [2026-05-01-wait-for-bonaventure-hr-template-before-finalising](decisions/2026-05-01-wait-for-bonaventure-hr-template-before-finalising.md) — "Wait for Bonaventure's HR Claude template before finalising assessment format". [resolved]
- [2026-05-01-slack-front-end-deel-back-end-for-leave](decisions/2026-05-01-slack-front-end-deel-back-end-for-leave.md) — Slack remains leave-request front-end; Deel.com is back-end. [resolved]
- [2026-05-01-remove-emergency-maternity-paid-from-leave-types](decisions/2026-05-01-remove-emergency-maternity-paid-from-leave-types.md) — Remove Emergency and Maternity-Paid from current leave types. [resolved]
- [2026-05-01-park-easter-egg-critical-thinking-assessment](decisions/2026-05-01-park-easter-egg-critical-thinking-assessment.md) — Park the Easter-egg critical-thinking assessment. [resolved]
- [2026-05-01-iso-compliance-gate-before-automation](decisions/2026-05-01-iso-compliance-gate-before-automation.md) — ISO compliance becomes a gate before automation projects begin. [resolved]
- [2026-05-01-google-drive-folder-structure-for-cvs](decisions/2026-05-01-google-drive-folder-structure-for-cvs.md) — Google Drive folder structure for CV storage. [resolved]
- [2026-05-01-fireflies-webhooks-for-post-interview-scoring](decisions/2026-05-01-fireflies-webhooks-for-post-interview-scoring.md) — Use Fireflies webhooks to feed post-interview scoring. [resolved]
- [2026-05-01-build-recruitment-tracker-in-hr-dashboard](decisions/2026-05-01-build-recruitment-tracker-in-hr-dashboard.md) — Add a recruitment tracker module to the HR dashboard. [resolved]
- [2026-05-01-ai-registry-source-of-truth-stays-in-linear-air](decisions/2026-05-01-ai-registry-source-of-truth-stays-in-linear-air.md) — AI Tools Registry SoR stays in Linear AIR; Monday AITR deprecated. [resolved]
- [2026-04-23-monday-hostinger-notion-stack-adopted](decisions/2026-04-23-monday-hostinger-notion-stack-adopted.md) — three-tool stack adopted: Monday (ops SoR) + Hostinger (self-host) + Notion (docs). [resolved]
- [2026-04-22-self-host-n8n-on-hostinger](decisions/2026-04-22-self-host-n8n-on-hostinger.md) — Self-host n8n on Hostinger instead of GCP. [resolved]
- [2026-04-22-reject-victor-slack-agent](decisions/2026-04-22-reject-victor-slack-agent.md) — Reject Victor Slack agent over RBAC failure. [resolved]
- [2026-04-22-per-user-data-control-hard-requirement-agent-platforms](decisions/2026-04-22-per-user-data-control-hard-requirement-agent-platforms.md) — per-user, source-platform-faithful access control is a Gate 1/2 hard requirement (Viktor precedent). [resolved]
- [2026-04-22-move-obsidian-to-sandbox](decisions/2026-04-22-move-obsidian-to-sandbox.md) — Move Obsidian from production to sandbox. [resolved]
- [2026-04-22-evaluate-openai-codex-as-claude-fallback](decisions/2026-04-22-evaluate-openai-codex-as-claude-fallback.md) — Evaluate OpenAI Codex as a Claude Code fallback. [resolved]
- [2026-04-22-decommission-signature-hound](decisions/2026-04-22-decommission-signature-hound.md) — Decommission Signature Hound dependency. [resolved]
- [2026-04-20-iso-first-stack-architectural-pivot](decisions/2026-04-20-iso-first-stack-architectural-pivot.md) — Bonaventure-driven pivot: ISO-compliant workflows come first, executive dashboard second. [resolved]

## Lessons

- [2026-05-14-ai-bounded-role-in-project-management](lessons/2026-05-14-ai-bounded-role-in-project-management.md) — Lysander: AI handles 30–60% of PM prep as first drafts only; PM stays in the loop. Maps onto AI-Native Pillar 3 (augment, not replace). [active]
- [2026-05-14-project-management-document-management-gap](lessons/2026-05-14-project-management-document-management-gap.md) — PM document/version management is ad-hoc per PM today; ISO problem. Michael's IBM-ECO probe + three-layer knowledge model frames Prime Radiant as the operational answer. [active]
- [2026-05-12-anti-ai-washing-as-content-discipline](lessons/2026-05-12-anti-ai-washing-as-content-discipline.md) — "name three things that make it AI" — content-discipline pattern that filters cosmetic AI-washing; first Janus social post on the angle going out today. [active]
- [2026-05-11-privacy-vs-personal-vault-content-taxonomy](lessons/2026-05-11-privacy-vs-personal-vault-content-taxonomy.md) — public / private / personal are three different things in Prime Radiant federation; personal is pre-promotion workflow staging (Janus contracts forbid non-work personal content). [active]
- [2026-05-11-html-over-powerpoint-for-read-only-content](lessons/2026-05-11-html-over-powerpoint-for-read-only-content.md) — HTML, not PowerPoint, for read-only content; token cost + editability + downstream value all favour HTML. [active]
- [2026-05-08-signals-sensors-inferences-input-architecture](lessons/2026-05-08-signals-sensors-inferences-input-architecture.md) — design the sensor array, the AI does the rest; pre-specifying outputs is the failure mode, under-specifying inputs is the second one. [active]
- [2026-05-08-wiki-vs-brain-metaphor-by-audience](lessons/2026-05-08-wiki-vs-brain-metaphor-by-audience.md) — system name is fixed (Janus Prime Radiant); supporting metaphor varies by audience ("brain" for non-technical, "wiki" for engineers). [active]
- [2026-05-07-llm-wiki-validates-capture-everything](lessons/2026-05-07-llm-wiki-validates-capture-everything.md) — "all this knowledge came out of these meetings" — the Janus Prime Radiant demo validates the capture-everything thesis. [resolved]
- [2026-05-05-notion-degrades-as-ai-searchable-kb](lessons/2026-05-05-notion-degrades-as-ai-searchable-kb.md) — Notion is excellent as a journal but degrades as an AI-searchable KB at scale; originating context for the LLM Wiki project. [resolved]
- [2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins](lessons/2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins.md) — GCP metering complexity drove Hostinger adoption ($920–1,020 vs $4,290–5,000). [resolved]
- [2026-04-20-fireflies-summaries-insufficient-raw-transcript-canonical](lessons/2026-04-20-fireflies-summaries-insufficient-raw-transcript-canonical.md) — Fireflies summaries too shallow; raw transcripts must be canonical for decision extraction. [resolved]

## Questions (open)

- [ingest-2026-05-20-1145-create-marketing-stack-vendor-pages](questions/ingest-2026-05-20-1145-create-marketing-stack-vendor-pages.md) — propose creating vendor pages for Cosmic, Attio, Vercel, Cloudflare, Cookiebot (5 adopted/in-flight tools from the 2026-05-19 marketing stack lock-in). [active]
- [2026-05-12-website-architecture-one-site-vs-country-sites](questions/2026-05-12-website-architecture-one-site-vs-country-sites.md) — one `janusd.com` site with country sub-paths (Andrew + Michael) vs standalone country sites (anticipated Bonaventure). Sequenced ahead of the Singapore landing-page work; status update 2026-05-15 — v1 campaign plan operationally uses both `janusd.com` + `janusdg.com`. [active]
- [ingest-2026-05-12-1730-vivian-balakrishnan-and-factset](questions/ingest-2026-05-12-1730-vivian-balakrishnan-and-factset.md) — propose creating Vivian Balakrishnan (Singapore Foreign Minister, LLM-wiki advocate) in entities/people/ + FactSet (financial data, AI-integrated) in entities/vendors/; both have ≥2 inbound references from today's ingest. [active]
- [ingest-2026-05-12-1545-openai](questions/ingest-2026-05-12-1545-openai.md) — lint-driven escalation to create `entities/vendors/openai.md`; 4-source threshold decisively met; recommendation = promote (confidence:medium). [active]
- [ingest-2026-05-12-1530-mnemon](questions/ingest-2026-05-12-1530-mnemon.md) — propose creating `entities/vendors/mnemon.md` for Mnemon (open-source LLM-supervised agent memory); recommendation = defer per single-source rule. [active]
- [ingest-2026-05-11-standup-skill-dual-write-to-aio-inbox](questions/ingest-2026-05-11-standup-skill-dual-write-to-aio-inbox.md) — Jehad's proposal to extend `/standup` (v3.13 → v3.14) to dual-write to Notion AND a markdown in the AIO Prime Radiant inbox; provisionally agreed; routing / what-gets-written / order / failure-mode questions awaiting Michael's sign-off. [active]
- [2026-05-11-internal-branding-prime-radiant-vs-nomi-vs-brain](questions/2026-05-11-internal-branding-prime-radiant-vs-nomi-vs-brain.md) — multiple names in circulation (Prime Radiant, Nomi, brain, wiki, Pulse, PULS) need consolidation conversation with Andrew. [active]
- [2026-05-11-bonaventure-friday-meeting-audio-recovery](questions/2026-05-11-bonaventure-friday-meeting-audio-recovery.md) — Fireflies failed to pick up Bonaventure's voice on a Friday post-ISO meeting; needs MP3 download + Whisper rerun. [active]

## Questions (resolved)

- [ingest-2026-05-15-joyce-woo](questions/ingest-2026-05-15-joyce-woo.md) — entity page promoted to [[joyce-woo|entities/internal/joyce-woo.md]] 2026-05-15 after the Janus Singapore white paper confirmed her title (CEO, Singapore) and supplied wiki-grade 4-decade-banking bio. [resolved]
- [ingest-2026-05-14-lysander-liu-and-spike-zhao](questions/ingest-2026-05-14-lysander-liu-and-spike-zhao.md) — escalation closed 2026-05-14; all three Project Management entity pages created ([[lysander-liu]], [[rosa-wu]], [[spike-zhao]]); Rosa upgraded from "referenced-only" to first-class entity per Michael's clarification that she co-heads Project Management with Euclid. [resolved]

- [ingest-2026-05-06-2300-new-project-hubs-from-monday](questions/ingest-2026-05-06-2300-new-project-hubs-from-monday.md) — all 5 Monday project-hub candidates approved and created. [resolved]
- [ingest-2026-05-06-2301-cowork-approval-governance-process](questions/ingest-2026-05-06-2301-cowork-approval-governance-process.md) — Cowork approval becomes a reusable [[ai-policy-gate-approval]] process page. [resolved]
- [2026-05-07-linear-air-ingest-new-vendor-candidates](questions/2026-05-07-linear-air-ingest-new-vendor-candidates.md) — NemoClaw + Viktor approved and created; Make/Lindy/Dify deferred. [resolved]
- [2026-05-06-notion-ingest-phase-1-new-entity-candidates](questions/2026-05-06-notion-ingest-phase-1-new-entity-candidates.md) — 7 vendors + 4 internal people approved and created. [resolved]
- [2026-05-06-mivory-batch-1-new-entity-candidates](questions/2026-05-06-mivory-batch-1-new-entity-candidates.md) — Anthropic / Marp / OpenClaw approved; Claude Code + Managed Agents fold under [[claude]] umbrella. [resolved]
- [2026-05-06-three-article-ingest-new-vendor-candidates](questions/2026-05-06-three-article-ingest-new-vendor-candidates.md) — Pinecone + Google Cloud approved; Andi Gutmans deferred. [resolved]
- [2026-05-06-karpathy-gist-new-vendor-candidates](questions/2026-05-06-karpathy-gist-new-vendor-candidates.md) — Cursor rejected (Janus uses VS Code + Zed); Claude approved; Marp/qmd deferred. [resolved]

## Pulse

- [2026-05-20-lint](pulse/2026-05-20-lint.md) — 393 wiki pages + 143 sources scanned; structural health OK; 4 meeting-source backfills (5-16 inbound refs each), 1 duplicate-slug supersession (`ai-registry`), 3 concept candidates, and 7 aging questions are the actionable items. [high]
- [2026-05-13-lint](pulse/2026-05-13-lint.md) — post v0.10 schema bump; 46 fm violations auto-fixed (owner normalisation + decided_by); 13 slug-alias rewrites; remediations deferred: concepts-folder migration, 8 missing-page stubs, ~10 unresolved meeting refs.
- [2026-05-13-transformers-are-graph-neural-networks](pulse/2026-05-13-transformers-are-graph-neural-networks.md) — Cambridge; foundational framing — Transformers ≡ GNNs on fully-connected token graphs winning the hardware lottery. [high]
- [2026-05-13-recursive-language-models](pulse/2026-05-13-recursive-language-models.md) — MIT CSAIL; third paradigm for long context (after RAG and compaction): LLM treats prompt as REPL variable, recursively self-calls. [high]
- [2026-05-13-magma-multi-graph-agentic-memory](pulse/2026-05-13-magma-multi-graph-agentic-memory.md) — UT Dallas / U. Florida; multi-graph (semantic/temporal/causal/entity) agentic memory; same four-graph shape as Mnemon — independent convergence. [high]
- [2026-05-13-claude-os-concept-surfaced](pulse/2026-05-13-claude-os-concept-surfaced.md) — Jehad's Hostinger+APIs/MCPs research direction; depends on Drive webhooks outcome. [low]
- [2026-05-12-vivian-balakrishnan-llm-wiki-government](pulse/2026-05-12-vivian-balakrishnan-llm-wiki-government.md) — Singapore Foreign Minister running personal LLM wiki on Raspberry Pi; keynoting AI Engineering Conference 16–17 May; Bonaventure knows him personally; potential advocate inside SG government. [high]
- [2026-05-12-mnemon-llm-supervised-memory](pulse/2026-05-12-mnemon-llm-supervised-memory.md) — Mnemon (open-source, Go binary, four-graph store) surfaces as the LLM-supervised pattern; closest external system to the Prime Radiant discipline applied at agent-runtime layer. [medium]
- [2026-05-12-lint](pulse/2026-05-12-lint.md) — first lint pass on the live Shared Drive vault; clean structural health; 3 inline fixes; `openai` vendor-page promotion now top recommendation.
- [2026-05-11-bonaventure-prime-radiant-shoutout](pulse/2026-05-11-bonaventure-prime-radiant-shoutout.md) — Bonaventure positive shout-out on the company-wide knowledge-base work; impressed it's happening sooner than expected; validates rollout pacing. [high]
- [2026-05-07-lint-evening](pulse/2026-05-07-lint-evening.md) — third lint pass (post 15-article batch); 4 slug-mismatches + 8 stale-updated bumps fixed inline; 7 persistent deferred-entity broken refs unchanged; no new breakage. Hyperproductivity cluster on watch.
- [2026-05-07-lint](pulse/2026-05-07-lint.md) — second lint pass; 3 broken wikilinks fixed, 10 persistent across 3 known patterns (skill references, Monday tracking items, deferred entities); recommends skill-reference convention.
- [2026-05-06-lint](pulse/2026-05-06-lint.md) — first wiki health check; 3 broken wikilinks, 1 missing-page candidate (ai-tool-evaluation), 2 ready briefs flagged.
- [2026-05-04-pinecone-nexus-launch](pulse/2026-05-04-pinecone-nexus-launch.md) — Pinecone reframes from vector DB to "knowledge engine"; introduces context compiler + KnowQL. [high]
- [2026-04-22-google-skills-repository](pulse/2026-04-22-google-skills-repository.md) — Google launches Official Agent Skills Repository at Cloud Next 2026. [high]
- [2026-04-22-google-agentic-data-cloud](pulse/2026-04-22-google-agentic-data-cloud.md) — Google rewires BigQuery + data catalog around autonomous agents at Cloud Next 2026. [high]
- [2026-04-14-claude-code-routines](pulse/2026-04-14-claude-code-routines.md) — Claude Code introduces routines (research preview): scheduled / event-driven automations. [high]
- [2026-04-08-claude-managed-agents-launch](pulse/2026-04-08-claude-managed-agents-launch.md) — Anthropic launches Claude Managed Agents; cloud-hosted agent execution platform. [high]
## Briefs

- [agentic-lean-marketing-stack](briefs/agentic-lean-marketing-stack.md) — why MCP-native tooling collapses SaaS sprawl risk for Janus; first concrete validation of the [[stack-composition-framework]]; locks Cosmic / Attio / Vercel / Cloudflare / Resend / Cookiebot for the marketing stack; September 2026 Singapore lunch (postponed from July). [active, high]
- [prime-radiant-storage-substrate](briefs/prime-radiant-storage-substrate.md) — Prime Radiant moves off Google Drive to Git as the canonical substrate; resolves Drive's stream-on-demand + cross-Workspace identity failure modes; Jehad-specific setup runbook for AIO migration; Marketing follows from-scratch on Git. [active, high]
- [ai-native-janus-positioning](briefs/ai-native-janus-positioning.md) — Bonaventure's three-pillar messaging spine (capital → companies → workers) reframes the AIO's infrastructure work as Janus's commercial differentiator. Third foundational aha. [high]
- [agent-memory-2026-q2](briefs/agent-memory-2026-q2.md) — Q2 2026 synthesis: file-based vs harness-coupled vs palace patterns; vendor moves; portability open questions. [high]
- [aio-playbooks-jehad](briefs/aio-playbooks-jehad.md) — Jehad's federated step-by-step playbooks for AIO operational work (standup, registry add, gate evaluation, assessify invite, AIP reconciliation, notebook cleanup). [medium]
- [aio-skills-sor-architecture-jehad](briefs/aio-skills-sor-architecture-jehad.md) — Jehad's federated synthesis of how `/standup`, `/ai-registry`, `/ai-tool-evaluation`, `/assessify-hr` interconnect; subagent-dispatch JSON contracts; read-vs-write matrix per SoR. [medium]
- [post-rag-agent-data-stack](briefs/post-rag-agent-data-stack.md) — the architectural shift from runtime RAG to compilation-stage knowledge layers; Pinecone Nexus + Google Agentic Data Cloud. [high]
