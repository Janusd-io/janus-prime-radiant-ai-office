---
type: source
source_type: laptop
title: interview-department-head
slug: interview-department-head
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/prompts/interview-department-head.md
original_size: 7619
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Parent-process interview prompt template for IMS enrolment — public-internal process artefact."
project: janus-puls-onboarding

---
<!-- jb:project-callout -->
> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — automatically linked by /janus-brain.


# interview-department-head

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/prompts/interview-department-head.md` on 2026-05-14._

# Interview Prompt — Phase 2 — Parent Process (Department Head)

> Use this prompt to drive the **parent process interview** with the department head during Phase 2 of `/ims-enrolment`. Goal: produce a complete `parent-process.md` for the department.

## Opening

> "We're going to define how the [Department] functions as a whole. Think of this as the **front page** of your department's manual — anyone reading it should understand what your team does, who you serve, and how you measure success. We'll spend about 30-45 minutes here.
>
> I'll ask 7 questions matching the [[iso-9001-figure-1|ISO 9001 Figure 1]] schematic. After we finish, every activity you mention in Q3 will get its own detailed sub-process document — but for now, **stay at the department level**. Don't drill into the how-to of each activity yet."

## Pacing

- Total: ~30-45 minutes
- Pause every 2-3 questions to summarise what's been captured
- If the answer is fuzzy, ask "can you give me a concrete example?" before moving on
- Don't accept "TBD" for the Process Owner (Q8) — push for a name

---

## Q1 — Sources of inputs

> "Who or what triggers your department's work? List the people, departments, channels, vendors, regulators, and scheduled events that send work into your team."

**Probing follow-ups if the answer is sparse:**
- "Who emails you with requests?"
- "What Slack channels does work come into?"
- "Are there any scheduled events — monthly reviews, quarterly cycles — that trigger work?"
- "Any regulatory deadlines you respond to?"

**Map answers to the parent-process template section 2.**

---

## Q2 — Inputs

> "Concretely — what flows in? Triggers, data, requirements, briefs, resources requested. For each source you just named, what arrives from them?"

**Probing follow-ups:**
- "Can you give me one example of each input type from the last week?"
- "What format does the input arrive in — email, ticket, voice, document?"
- "What's missing from inputs that you wish you had?"

**Map answers to the parent-process template section 3.**

---

## Q3 — Activities (CRITICAL — this seeds the sub-processes)

> "Now the most important question — what are the **major activities** your department does? Not detailed steps yet — just the 3-10 main things your team is known for. Each one of these will become a separate sub-process document later, so think of these as **chapters** in your department's book."

**Probing follow-ups:**
- "If a new employee joined tomorrow, what 3-5 things would they need to learn to do?"
- "What activities take up the most time across the department?"
- "Are there activities that only happen quarterly or annually but matter a lot?"
- "Anything you do that's compliance- or audit-related specifically?"

**Map answers to the parent-process template section 4. Each activity needs:**
- Activity name (short — 2-5 words)
- Activity owner (named person — push back if "TBD")
- A 1-sentence description

**This list is the input to Phase 3.** Pause here to confirm the list is complete before moving on. Ask: *"Are these the right 3-10 activities to describe the department? Anything missing? Anything that's actually a step inside another activity?"*

---

## Q4 — Outputs

> "What does your department produce? Deliverables, decisions, records, services, products."

**Probing follow-ups:**
- "What lands on other departments' desks because of your team's work?"
- "What evidence does your team leave behind — documents, records, log entries?"
- "What does your department hand off to clients or external parties?"

**Map answers to the parent-process template section 5.**

---

## Q5 — Receivers of outputs

> "Who consumes what you produce? Same kind of list as Q1 but in reverse — internal departments, external clients, partners, regulators."

**Probing follow-ups:**
- "Who would notice immediately if your department stopped producing X?"
- "Are there outputs that go directly to clients or to other departments first?"

**Map answers to the parent-process template section 6.**

---

## Q6 — Controls and check points

> "Where in your work are the quality gates? What stops a piece of work from moving forward until it's been checked? Who approves what?"

**Probing follow-ups:**
- "Is there a moment where work has to wait for review before it can proceed?"
- "Are there approval requirements for spending, hiring, releasing, etc.?"
- "Any AI-touching work — does it have its own checks under ISO 42001?"
- "How do you catch errors before they reach a client or another department?"

**Map answers to the parent-process template section 7.**

---

## Q7 — Resources

> "What does your department need to function? People, tools, infrastructure, budget, knowledge."

**Probing follow-ups (cover each row of section 8):**
- "Who's in the department? How many people? What roles?"
- "What tools and systems does the team use day-to-day? Any AI tools?"
- "What infrastructure — physical or digital — does the team rely on?"
- "What knowledge or expertise is essential? Where does that knowledge live?"
- "Rough annual budget envelope?"

**Map answers to the parent-process template section 8.**

---

## Q8 — Process Owner (HARD REQUIREMENT)

> "Who is the **named person** accountable for this entire department process? Must be one person. Can be you or someone else — but it must be a name, not a role."

**Do not let the department head answer "TBD" or "the team."** ISO 9001 requires a single accountable owner. If they're unsure, walk them through this:

- "If the auditor walked in tomorrow and said 'show me who's accountable for this process,' whose name would you put forward?"
- "If a major finding came up, who would have to respond?"

**Map answer to the parent-process template section 8 (Process Owner) and the header.**

---

## Q9 — KPIs (soft requirement — okay if not yet defined)

> "How do you know the department is performing well? Do you track any specific metrics today?"

**Probing follow-ups:**
- "What does a great month look like, measurably?"
- "What's the first thing that would tip you off that something's going wrong?"
- "If you don't have formal KPIs, what would you want measured?"

If they don't have formal KPIs, that's fine — write them as **proposed KPIs to develop with Simon's help**, and add an Open Item.

**Map answers to the parent-process template section 9.**

---

## Q10 — Scope statement

> "In one paragraph: what's in scope for your department, what's out of scope, and what's shared with another department? This prevents auditor confusion later."

**Probing follow-ups:**
- "Where does your department's responsibility end?"
- "What things are people surprised to learn aren't your job?"
- "Are there grey areas with other departments?"

**Map to section 10.**

---

## Q11 — Open items

> "Any open questions or decisions that block this parent process document from being finalised? Things that need Simon's input?"

**Map to section 12.**

---

## Closing

> "We've got the parent process. Next we'll go through each of the [N] activities you named in Q3 — one at a time — and produce a sub-process document for each. That'll be Phase 3.
>
> Want to take a break first, or continue?"

Save the populated `parent-process.md`. Confirm the activities list before moving to Phase 3.

---

## If the department head gets stuck

Show them `examples/ai-department/parent-process.md` and walk through one section together. The AI Department worked example is the canonical reference — most questions ("what does Controls mean?") are answered by seeing what we wrote for AI Ops.
