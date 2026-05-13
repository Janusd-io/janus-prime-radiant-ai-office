---
type: linear-issue
linear_id: AIR-38
linear_url: https://linear.app/janusd/issue/AIR-38/viktor
title: Viktor
status: Rejected
fetched: 2026-05-07
source_type: linear-issue
---

# AIR-38: Viktor

**Issue:** AIR-38  
**Title:** Viktor  
**Status:** Rejected (2026-04-22), account deleted 2026-05-04  
**Category:** AI Agent Platform (In-Slack Coworker)  

## Description

**Category:** AI Agent Platform (In-Slack Coworker)
**Cost per User/Month:** Free Tier | $50 (Pro) | ~$250 (Enterprise)
**Number of Licences:** N/A — account deleted 2026-05-04
**Total Monthly Cost:** $0 (rejected)
**Departments:** Technology, AI Policy, Commercial
**Final Status:** Rejected (2026-04-22) → account deleted (2026-05-04)

## Evaluation Dossier Summary

* **Gate 1 (Baseline):** PASS (G1.1–G1.5). Confirmed no-training policy and native GCP/Slack fit.
* **Gate 2 (Technical):** PASS (Score: 23/25).
* **Gate 3 (Sandbox):** Initiated; failed on per-user data-control architecture (see below).

## Reason for Rejection

Sandbox evaluation in the `#viktor-evaluation` Slack channel (2026-04-03, with Michael Bruck, Jehad Altoutou, Andrey Timokhov) surfaced a structural data-control issue that ruled Viktor out for Janus use:

* **Integrations are connected per-user but used workspace-wide.** A single user (e.g., Michael) connects Google Drive, Notion, Linear, etc. to Viktor; once connected, *every* authorised Slack channel member can invoke those integrations through Viktor.
* **Integration runs under the connecting user's permissions, not the requesting user's.** Viktor explicitly does not enforce the access boundaries of the connected platform. If User C is in the Slack channel but has no Notion account, they can still pull Notion data through Viktor because the Notion integration was authorised by another user.
* **First-line defence is a workspace allow-list (Team Settings), not per-tool ACLs.** The only finer-grained control is requiring per-call approval on sensitive tools — manual, breaks at scale, and still doesn't enforce the source platform's own access model.

This is the wrong shape of access control for a multi-user, multi-jurisdiction consultancy where Notion / Drive / Linear access boundaries are deliberately differentiated by team and project. Approving Viktor would have meant collapsing those boundaries every time someone asked Viktor a question in a shared channel.

When asked directly ("does User C get access to Notion through Viktor even if they're not a Notion user?"), Viktor's own response was: *"Short answer: yes, User C could access Notion data through me."*

## Account Deletion

Account deleted on **2026-05-04**, triggered by the $50 Pro-tier payment coming due against a tool we were not using post-rejection. Deletion form completed with reasons:

* *Main reason for leaving:* Does not fit in with our company's requirements.
* *What would need to change:* Requires more role-based account controls to data sources.

## Lessons Captured for Future Evaluations

Per-user, source-platform-faithful access control is a **hard requirement** for any AI agent / integration platform used at Janus. Specifically:

1. The integration must run under the *requesting* user's permissions, not the connecting user's.
2. Source-platform access boundaries (Notion page permissions, Drive file ACLs, Linear team membership, etc.) must be honoured in full when the agent reads or writes on a user's behalf.
3. A workspace-level allow-list and per-tool approval workflows are *not* substitutes for proper per-user data-source ACLs.

This is now a Gate 1 / Gate 2 criterion and should be checked early in any future agent-platform evaluation.

---

*Originally requested by: Michael Bruck. Cancelled 2026-04-22; account deleted 2026-05-04.*

## Comments

### Comment 1: Jehad Altoutou (2026-04-03 07:05)

### Gate 2 Matrix
# Janus Digital — Gate 2 Technical & Strategic Fit Matrix: Viktor

| Tool Name | Viktor (getviktor.com) |
| :--- | :--- |
| Date | 2026-04-03 |
| Evaluator | Jehad Altoutou |

## 🛡️ Must Have (Binary Screen)

*All criteria must be "PASS" for the candidate to progress to Stage 3.*

| Criterion | Result | Evidence / Notes |
| :--- | :--- | :--- |
| **G2.1 — MCP Compatibility** | ✅ PASS | Highly extensible via API/function patterns for AI orchestration. |
| **G2.2 — SSO Auth** | ✅ PASS | SSO documentation for enterprise Workspace accounts. |
| **G2.3 — Vendor Viability** | ✅ PASS | Funded by top-tier VCs; built by former Google engineers. |

---

## 📈 Should Have (Scored 0–5)

*Pass Threshold: ≥ 15/25*

| Criterion | Score | Rationale & Evidence |
| :--- | :---: | :--- |
| **G2.4 — Efficiency Gain** | 5 | Automates complete cross-platform workflows (Ads -> Sheets -> Slack). |
| **G2.5 — Ease of Adoption** | 5 | In-Slack onboarding is intuitive for all skill levels. |
| **G2.6 — Multi-Platform** | 4 | Primarily Slack/Teams; web interface for configuration. |
| **G2.7 — Audit Trail** | 4 | Robust execution logging for each agent action. |
| **G2.8 — Gemini Integration** | 5 | Native Google Cloud pedigree ensures baseline performance. |

**Should Have Score Total:** **23 / 25**

---

## ✨ Nice to Have (Scored 0–5)

| Criterion | Score | Rationale & Evidence |
| :--- | :---: | :--- |
| **G2.9 — Automation Support** | 5 | Native builder for conditional logic / 3,000+ connectors. |
| **G2.10 — Differentiation** | 5 | First true "AI coworker" rather than just a chatbot. |
| **G2.11 — Cost Efficiency** | 4 | Professional pricing tiers align with high ROI. |

---

## 🏁 Gate 2 Decision: PASS

**Next Action:** Proceed to **Stage 3 Sandbox Pilot**. Conduct deeper testing of Dialogflow compatibility as requested.

### Comment 2: Jehad Altoutou (2026-04-03 07:05)

### Gate 1 Report
# Janus Digital — Gate 1 Assessment Report: Viktor

| Tool Name | Viktor (getviktor.com) |
| :--- | :--- |
| Date | 2026-04-03 |
| Evaluator | Jehad Altoutou |

## 🛡️ Technical & Security Baseline (Binary Screen)

*All criteria must be "PASS" for the candidate to progress to Stage 2.*

| Criterion | Result | Evidence / Notes |
| :--- | :--- | :--- |
| **G1.1 — Google Integration** | ✅ PASS | Deep native integrations with Google Ads, GA4, GSheets, and GCalendar. Built by ex-Googlers. |
| **G1.2 — Slack Integration** | ✅ PASS | Slack is the primary deployment interface for Viktor agents. |
| **G1.3 — Data Portability** | ✅ PASS | Connects directly to Google ecosystem; data and outputs are accessible via integrated Sheets/Docs. |
| **G1.4 — Data Training Exclusion** | ✅ PASS | **Explicit Guarantee**: "Your data never trains AI models. Conversations, files, and business data are never used to train third-party models." |
| **G1.5 — Documented API** | ✅ PASS | While a "ready-to-use" agent, it documents full extensibility with 3,000+ third-party APIs. |

---

## 🏁 Gate 1 Decision: PASS

**Next Action:** Proceed to Stage 2 Technical Qualification & Scoring.
