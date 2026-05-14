---
type: source
source_type: laptop
title: diagram-prompt-platform-development
slug: diagram-prompt-platform-development
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/examples/ai-department/diagram-prompt-platform-development.md
original_size: 6272
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "ISO/IMS process diagram prompt — Platform Development workflow, work content"
project: janus-puls-onboarding

---
<!-- jb:project-callout -->
> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — automatically linked by /janus-brain.


# diagram-prompt-platform-development

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/examples/ai-department/diagram-prompt-platform-development.md` on 2026-05-14._

# Diagram Prompt — Sub-Process: Platform & Tool Development

> Filled-in example for the AI Department's platform development process.
> 9 stages from pain point to live. Worked example: [[assessify|Assessify]].
> Paste between `---PROMPT---` into ChatGPT. Mermaid backup in `sub-process-platform-development.md` Section 2.

---PROMPT---

Generate a **high-resolution, ultra-wide professional business diagram** (aspect ratio 21:9 or wider, minimum 3840×1620 px) titled **"[[platform-development-process|Platform & Tool Development Process]] — Janus Digital"** with subtitle **"From pain point to live · 9 stages · [[obsidian|Obsidian]] as the living spine · Worked example: Assessify"**.

**Style:** Clean corporate / [[mckinsey|McKinsey]]-style. Flat design, soft drop shadows, rounded corners. White background. Sans-serif typography. ISO palette:
- Process stage boxes: light blue `#E6F0FF` with navy `#1A4480` border
- Controls (top): soft yellow `#FFF8D6` with amber `#996600` border
- Resources (bottom): soft pink `#FFE8E8` with deep red `#990000` border
- KPIs: light green `#E8F5E9` with green `#1B5E20` border
- Sources / Inputs / Outputs / Receivers: light grey `#F5F5F5` with mid-grey `#666` border
- **Obsidian spine accent (purple):** `#EDE7F6` with violet `#4527A0` border for any box that calls out an Obsidian artifact

**Layout:** Controls top · Sources → Inputs → Activities (9 stages, 2 rows) → Outputs → Receivers · Resources bottom · KPI box below attached via dashed line.

**TOP BOX — CONTROLS:**
- Build-vs-buy gate (run Tool Evaluation Procedure first)
- Strategic approval gate (Michael) — no code before sign-off
- Stack alignment with Janus standard tech stacks
- Phased build with control points between phases
- Sandbox isolation — no production data
- Standing rule: never `docker compose down -v` unless schema changed
- Graphify before review (AI agents read the graph, not raw source)
- [[5-area-stress-test|5-area stress test]] (functionality · UI/UX · security · APIs · stability)
- Requester sign-off + IT acceptance gates
- Documentation triad mandatory (README · SOP · implementation plan)
- Obsidian-as-living-docs invariant (stale notes = process failure)

**LEFTMOST BOX — SOURCES OF INPUTS:**
- Pain point from a department
- Strategic priority (Michael)
- Gap left by Tool Evaluation (no third-party fit)
- Regulatory or audit driver

**SECOND BOX — INPUTS:**
- Use case · stakeholders · success criteria
- Existing tools surveyed (Tool Eval result)
- Tech stack constraints
- Budget · timeline

**CENTRAL BOX — ACTIVITIES:** Header "ACTIVITIES — 9 stages from pain point to live platform". Two horizontal rows linked by arrows:

**Row 1:**
1. **Identify need** — pain point captured · build-vs-buy decided
2. **Scope & approval** — one-pager · Michael signs off · Obsidian project note created
3. **Stack selection** — pick from `05 Tech Stacks/` (SaaS Default · AI App · Creative Dev)
4. **Sandbox build (phased)** — Phase 1A → 1B → 2A → ... · isolated Docker · ngrok exposure
5. **Graphify + Obsidian sync** — `/graphify --update --obsidian` · graph dump per major change

**Row 2:**
6. **AI / [[agentic-layer|agentic layer]]** — n8n workflows · MCP skills · [[claude-code|Claude Code]] skills · auto-chained 42001 Gate 1
7. **Stress test + internal demo** — 5-area test · requester runs real use case in sandbox
8. **Documentation** — README + SOP + implementation plan (all three required)
9. **IT handover + go-live** — handover package · IT accepts · production deployment · status → Active

Add a small purple-border callout near stages 2 and 5: **"Obsidian project note updated at every stage"**.

**FOURTH BOX — OUTPUTS:**
- Live platform (production URL)
- [[github|GitHub]] repo
- Obsidian project note (living)
- Graphify dump (`_COMMUNITY_*.md` notes)
- README · SOP · implementation plan
- n8n workflows · MCP skills

**RIGHTMOST BOX — RECEIVERS OF OUTPUTS:**
- Requesting department (end-users)
- IT department (operates and runs it)
- All employees (eventual access)
- Internal Audit (full trail)
- AI agents (via Graphify + MCP skills)

**BOTTOM BOX — RESOURCES — Process Owner: Jehad (AI Operations Engineer):**
Four columns:
- **Knowledge spine (purple):** Obsidian Vault (`03 Projects/` · `02 Skills/` · `05 Tech Stacks/` · `99 Graphify/`) · `/brain` skill · per-project auto-memory
- **Graphify (purple):** `~/.local/bin/graphify` · `--obsidian-dir` flag · ~2400× token efficiency
- **Stacks & AI:** Next.js · Prisma · Drizzle · Postgres · Tailwind · shadcn · n8n · Claude · [[openai|OpenAI]] · Codex · Antigravity · AI Gateway
- **Infra:** [[hostinger|Hostinger]] VPS · Vercel · Neon · Docker · [[linear|Linear]] AIP / AIR · Monday board `5095012818`

**KPI BOX (dashed line):** Header "MONITORING & MEASUREMENT":
- Time pain-point → live (target ≤ 3 months)
- Phase completion vs plan (≥ 90% on time)
- 5-area stress test pass rate (100% at handover)
- Defect rate post-IT-handover (trended downward)
- Adoption rate by requester (≥ 80% within 30 days)
- AI components Gate 1 evaluated (100%)
- Obsidian note freshness (≤ 14 days for active projects)
- Graphify dump freshness (refreshed within 1 week of major code change)

**Worked example inset box (bottom-right, smaller, subordinate):**
Header: "Worked example — Assessify (HR assessment platform)"
- Stage 1: HR pain — manual assessments, no analytics
- Stage 4: Phases 1-2D · CRUD · scoring · RBAC · production hardening (10-17 Apr 2026)
- Stage 5: Graph 451→611 notes; communities mapped
- Stage 6: n8n Bank/Personal/Error workflows · `assessify-hr` MCP skill
- Stage 7: 5-area stress test passed · DB cleaned for demo
- Stage 8: README v2 · SOP v1.1
- Stage 9: **In flight — awaiting IT for custom domain + HTTPS**

**Footer (centered):**
"ISO 9001 §8.3 (design and development) · §8.5 · §7.5 · §9.1.3 · ISO 27001 A.5.7 · A.8 · A.8.25-A.8.34 · ISO 42001 §6.1 · §8.2."

**Critical:** Render all text legibly. Use **purple borders** for Obsidian-artifact elements (the project-note callout, Knowledge spine column, Graphify column). Worked example callout should be visually subordinate to the main diagram. Wide landscape. Output single high-res image.

---PROMPT---

**Mermaid backup:** `sub-process-platform-development.md` Section 2 renders natively on GitHub.
