---
type: source
source_type: laptop
title: diagram-prompt-tool-evaluation
slug: diagram-prompt-tool-evaluation
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/examples/ai-department/diagram-prompt-tool-evaluation.md
original_size: 4691
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "ISO/IMS diagram prompt — Tool Evaluation procedure; work content"
---

# diagram-prompt-tool-evaluation

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/examples/ai-department/diagram-prompt-tool-evaluation.md` on 2026-05-14._

# Diagram Prompt — Sub-Process: AI Tool Evaluation & Onboarding

> Filled-in example for the AI Department's tool evaluation procedure.
> Two intake paths converging at one gate-driven pipeline.
> Paste between `---PROMPT---` into ChatGPT. Mermaid backup in `sub-process-tool-evaluation.md` Section 1.

---PROMPT---

Generate a **high-resolution, ultra-wide professional business diagram** (aspect ratio 21:9 or wider, minimum 3840×1620 px) titled **"AI Tool Evaluation & Onboarding Procedure — Janus Digital"** with subtitle **"Two intake paths · gate-driven evaluation · sandbox validation · IT handover"**.

**Style:** Clean corporate / McKinsey-style. Flat design, soft drop shadows, rounded corners. White background. Sans-serif typography. Color palette:
- Intake Path A (live): light blue `#E6F0FF` with navy `#1A4480` border
- Intake Path B (to be built): light orange `#FFF3E0` with orange `#E65100` border (signals "not yet built")
- Gate / decision diamonds: yellow `#FFF8D6` with amber `#996600` border
- Pass / approval boxes: light green `#E8F5E9` with green `#1B5E20` border
- Reject boxes: light red `#FFEBEE` with deep red `#B71C1C` border
- Neutral process boxes: light grey `#F5F5F5` with mid-grey `#666` border
- Decision points as **diamond shapes** with two labelled exits

**Layout:** Two intake boxes top-left, vertically stacked, converging into Intake → Registry Check (diamond) → Gates 1-4 → Sandbox (diamond) → Sign-off → IT Handover → Live. Rejection branches off the diamonds.

**TWO INTAKE BOXES:**

**Path A — Meeting mention** (light blue, "LIVE" badge):
- Fireflies transcript captures tool name
- `/standup` skill (v3.11) dispatches `/ai-registry`
- Auto-chains `/ai-tool-evaluation` Gate 1

**Path B — Slack request** (light orange, "TO BE BUILT" badge):
- User posts in `#ai-tool-requests` channel
- Webhook fires to AI agent
- Agent invokes `/ai-registry` + `/ai-tool-evaluation`

**INTAKE BOX (after merge):** "Capture: tool name · vendor · use case · requester · jurisdiction"

**REGISTRY CHECK (diamond):** "Already in Linear AIR?" — Two exits: "Yes — existing" → link to existing entry; "No — new" → create AIR-N issue.

**EXISTING TOOL BOX:** Link requester · notify status (Active / Rejected / In-Eval) · procedure ends here for duplicates.

**NEW TOOL BOX:** `/ai-registry` creates AIR-N · related-tools check populates "Suggested Alternatives" · notify requester "In evaluation — AIR-N#X".

**GATES BOX (central):** Header "Gates 1-4 — `/ai-tool-evaluation`". Sub-header "Each gate has documented pass/fail criteria · stored as comments on AIR-N". Four gates left to right with arrows between:

1. **Gate 1 — Initial fitness** (Cost · vendor reputation · capability · TOS)
2. **Gate 2 — Security & data** (Posture · residency · encryption · audit logs)
3. **Gate 3 — AI governance (ISO 42001)** (Impact assessment · model card · bias · oversight)
4. **Gate 4 — Operational fit** (Stack integration · SSO · API · SLA · exit strategy)

Two exits from Gates block:
- **All 4 pass** → Sandbox
- **Any gate fails** → Rejected (red)

**REJECTED — GATE FAILURE (red):** Failure reason as AIR-N comment · status → Rejected · Slack notification with reason.

**SANDBOX BOX:** Provision in isolated environment (no production data) · requester runs actual use case · 5-area stress test (functionality · UI/UX · security · APIs · stability) · findings documented on AIR-N.

**SANDBOX VALIDATION (diamond):** "Use case satisfied?" — Yes → Sign-off; No → Rejected.

**REJECTED — SANDBOX (red):** Use case not met OR critical stress-test issues · status → Rejected — Sandbox · requester notified.

**REQUESTER SIGN-OFF (green):** Requester confirms in writing on AIR-N or Slack · tool meets original need.

**IT HANDOVER:** Handover package: SOP · README · Implementation plan · IT reviews and accepts (recorded on AIR-N) · IT deploys company-wide (provisioning · SSO · access policies · cost allocation).

**LIVE BOX (deep green):** AIR status → Active · all eligible employees have access · requester receives final notification · loop closed.

**Footer (centered):**
"ISO 42001 §8.2 satisfied: Gates 1-4 collectively constitute the AI System Impact Assessment for every tool entering use. ISO 27001 A.5.21 / A.5.22 / A.8 · ISO 9001 §8.4 · Linear AIR is the sole source of truth for the AI Systems Register."

**Critical:** Render text legibly. Use diamonds for the three decision points. Wide landscape. Output single high-res image.

---PROMPT---

**Mermaid backup:** `sub-process-tool-evaluation.md` Section 1 renders natively on GitHub.
