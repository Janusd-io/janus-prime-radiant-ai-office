---
type: source
source_type: laptop
title: interview-activity-owner
slug: interview-activity-owner
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/prompts/interview-activity-owner.md
original_size: 6115
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Per-activity interview prompt template for IMS enrolment — public-internal process artefact."
project: janus-puls-onboarding

---

# interview-activity-owner

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/prompts/interview-activity-owner.md` on 2026-05-14._

# Interview Prompt — Phase 3 — Sub-Process (Activity Owner)

> Use this prompt once per activity from the parent process's Q3 list. Goal: produce one `sub-process-[slug].md` per activity. Interview the **activity owner** (may not be the department head).

## Opening

> "We're going to detail **[Activity Name]** — one of the activities you (or your department head) named in the parent process. Same 7-section structure as before, but scoped to this single activity. We'll spend about 20-30 minutes.
>
> Where the parent process said *what* your department does, this document says *how* this one activity gets done step by step. Other activities will get their own documents — stay focused on just this one."

## Pacing

- Total: ~20-30 minutes per sub-process
- If the activity is very simple, this can be 15 minutes
- If the activity has many steps or many stakeholders, can extend to 45 minutes
- Encourage drafts — perfection is the enemy of done; Simon will refine

---

## Q1 — Sources of inputs (for this activity specifically)

> "Who or what triggers **this activity**? Often this is narrower than the parent — e.g., the parent says 'requests come from many places', but this specific activity might only fire when an incident is reported."

**Probing follow-ups:**
- "When was the last time this activity ran? What kicked it off?"
- "Is this activity event-driven, scheduled, or on-demand?"
- "Does this activity ever fire from another sub-process inside the same department?"

**Map to sub-process template section 2.**

---

## Q2 — Inputs (for this activity)

> "Concretely — what arrives when this activity is triggered? Data, requests, prior-step outputs, signed-off artefacts."

**Probing follow-ups:**
- "What format does the trigger take — ticket, message, email, document?"
- "Does the activity require any artefacts already exist (e.g., a signed approval, a prior record)?"

**Map to sub-process template section 3.**

---

## Q3 — Activities — step by step (THE CORE OF THIS SUB-PROCESS)

> "Walk me through this activity step by step. What's the first thing that happens after the trigger? What's the second? What's the last? For each step, tell me: who does it, and how do you know it's done before moving to the next step?"

**Probing follow-ups:**
- "Can you describe a specific time you ran this activity recently? Tell me the steps in order."
- "Where in the steps do other people get involved?"
- "Are there decision points where you might go down a different path?"
- "What's the typical end state — what indicates 'done'?"

**Build out section 4 as a numbered table:**

| # | Step | Description | Owner | Control point on exit |
|---|---|---|---|---|

Push for 4-10 steps. If they say it's just one step, ask "what happens before, during, and after that one step?" Almost every activity has internal steps.

---

## Q4 — Outputs (of this activity)

> "What does this activity produce? Each output should have a form (document, record, decision, service), a receiver, and where it's retained."

**Probing follow-ups:**
- "What artefact proves this activity was done?"
- "What lands on someone else's desk because of this activity?"

**Map to section 5.**

---

## Q5 — Receivers of outputs

> "Who consumes what this activity produces? Often the next sub-process in the same department, sometimes another department, sometimes a client."

**Map to section 6.**

---

## Q6 — Controls and check points

> "Same question as the parent, but scoped to this activity. Where in the steps you described are the quality gates? What stops a step from proceeding until something's verified?"

**Probing follow-ups:**
- "Is there a step where someone has to approve before you proceed?"
- "Any required checks — security, AI Impact Assessment, peer review, automated tests?"
- "What's the *last* check before output is released?"

**Map to section 7. Cross-reference the control points listed in Q3's step table.**

---

## Q7 — Resources

> "What does this activity need? Tools, people, knowledge, budget."

**Probing follow-ups (cover each row):**
- "Who's the named activity owner?"
- "Who else gets involved in any of the steps?"
- "What tools and systems are used in each step?"
- "Any external vendors involved?"
- "What knowledge or training is required to run this activity?"
- "Per-execution cost or monthly run rate?"

**Map to section 8.**

---

## Q8 — KPIs

> "How do you know this activity ran well? What metrics matter — time, quality, cost, error rate?"

**Probing follow-ups:**
- "Is there a target time from trigger to completion?"
- "What error or defect rate is acceptable?"
- "What's a 'good' versus 'bad' execution of this activity?"

**Map to section 9.** Same as parent — proposed KPIs are fine if formal ones don't exist.

---

## Q9 — Open items

> "Any decisions or clarifications this sub-process needs from Simon?"

**Map to section 10.**

---

## Closing

> "[Activity Name] is now documented. Next we'll move to [next activity from the parent's list]. Want to continue or take a break?"

Save populated `sub-process-[slug].md`.

---

## Naming convention for the file

Use a short kebab-case slug from the activity name:

- "Meeting → Task → Build" → `sub-process-meeting-to-task-build.md`
- "Customer Onboarding" → `sub-process-customer-onboarding.md`
- "Payroll Run" → `sub-process-payroll-run.md`

---

## If the activity owner gets stuck

Show them the corresponding sub-process from `examples/ai-department/`:

- For something automation/workflow-heavy → `sub-process-meeting-to-task.md`
- For something vendor- or tool-evaluation-related → `sub-process-tool-evaluation.md`
- For something build/design/dev-related → `sub-process-platform-development.md`

These are full ISO-grade worked examples — the activity owner can pattern-match their answers against them.

---

## After all sub-processes are done

- Update the parent process's section 11 (Related sub-process documents) with the actual filenames
- Move to Phase 4 (First Voice questionnaires per person)
- Then Phase 5 (handover bundle)
