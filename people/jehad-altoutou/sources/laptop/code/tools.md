---
type: source
source_type: laptop
title: tools
slug: tools
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/tools.ts
original_size: 151523
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# tools

_Extracted from `[[assessify|assessify]]/src/lib/mcp/tools.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import { auditLog } from "@/lib/audit";
import { sendAssessmentInviteEmail } from "@/lib/email";
import type { McpSession } from "./auth";
import {
  assertCompetencyIdsExist,
  assertThresholds,
  McpPermissionError,
  McpValidationError,
  requireAdmin,
} from "./validation";
import { updateAssessment as updateAssessmentOp } from "@/lib/operations/assessments";
import {
  addSection as addSectionOp,
  removeSection as removeSectionOp,
  reorderSections as reorderSectionsOp,
  setSectionWeights as setSectionWeightsOp,
  updateSection as updateSectionOp,
} from "@/lib/operations/sections";
import {
  addQuestion as addQuestionOp,
  attachQuestionToSection as attachQuestionOp,
  createBankQuestion as createBankQuestionOp,
  detachQuestionFromSection as detachQuestionOp,
  reorderQuestions as reorderQuestionsOp,
  updateQuestion as updateQuestionOp,
} from "@/lib/operations/questions";
import {
  exportSessions as exportSessionsOp,
  getSession as getSessionOp,
  getSessionResults as getSessionResultsOp,
  listSessions as listSessionsOp,
} from "@/lib/operations/sessions";
import {
  getAssessmentAnalytics as getAssessmentAnalyticsOp,
  getQuestionAnalytics as getQuestionAnalyticsOp,
} from "@/lib/operations/analytics";
import {
  createNewVersion as createNewVersionOp,
  getAssessmentVersion as getAssessmentVersionOp,
  listAssessmentVersions as listAssessmentVersionsOp,
  publishVersion as publishVersionOp,
  revertToVersion as revertToVersionOp,
} from "@/lib/operations/versions";
import {
  bulkCreateInvites as bulkCreateInvitesOp,
  createInvite as createInviteOp,
  extendInviteExpiry as extendInviteExpiryOp,
  getInvite as getInviteOp,
  listInvites as listInvitesOp,
  resendInvite as resendInviteOp,
  revokeInvite as revokeInviteOp,
  updateCandidate as updateCandidateOp,
} from "@/lib/operations/invites";
import {
  duplicateAssessment as duplicateAssessmentOp,
  duplicateQuestion as duplicateQuestionOp,
} from "@/lib/operations/duplicates";
import {
  archiveCompetency as archiveCompetencyOp,
  createCompetency as createCompetencyOp,
  updateCompetency as updateCompetencyOp,
} from "@/lib/operations/competencies";
import {
  archiveDepartment as archiveDepartmentOp,
  createDepartment as createDepartmentOp,
  updateDepartment as updateDepartmentOp,
} from "@/lib/operations/departments";
import {
  archiveJobRole as archiveJobRoleOp,
  updateJobRole as updateJobRoleOp,
} from "@/lib/operations/job-roles";
import {
  bulkDeleteQuestions as bulkDeleteQuestionsOp,
  bulkTagQuestions as bulkTagQuestionsOp,
  bulkToggleAssessmentActive as bulkToggleAssessmentActiveOp,
} from "@/lib/operations/bulk";
import {
  findByExternalId,
  lookupByExternalId,
  type ExternalIdType,
} from "@/lib/operations/external-id";
import { applyRecruitmentScope, applyOfficeScope } from "@/lib/auth-scope";

// ─── Type helpers ──────────────────────────────────────────────

type ToolResult = { content: Array<{ type: "text"; text: string }>; isError?: boolean };

function ok(data: unknown): ToolResult {
  return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
}
function fail(msg: string): ToolResult {
  return { content: [{ type: "text", text: `ERROR: ${msg}` }], isError: true };
}

function slugify(s: string): string {
  return s
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

// ─── Tool definitions (JSON Schema for Claude) ────────────────

export const TOOL_DEFINITIONS = [
  // ── READ / SEARCH ──
  {
    name: "list_departments",
    description: "List all departments (use before creating a job role to get departmentId).",
    inputSchema: { type: "object", properties: {}, required: [] },
  },
  {
    name: "search_job_roles",
    description: "Search job roles by title or department. ALWAYS call this before creating a new role to check for duplicates.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "Free-text match against title/slug/description" },
        departmentId: { type: "string" },
      },
    },
  },
  {
    name: "search_assessments",
    description: "Search assessments (templates) by title or job role. ALWAYS call before creating to avoid duplicates.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string" },
        jobRoleId: { type: "string" },
        activeOnly: { type: "boolean", default: false },
      },
    },
  },
  {
    name: "get_assessment",
    description: "Get full assessment details including its latest version, sections, and questions.",
    inputSchema: {
      type: "object",
      properties: { id: { type: "string" } },
      required: ["id"],
    },
  },
  {
    name: "search_questions",
    description: "Search the question bank by text. Use before adding new questions to dedupe.",
    inputSchema: {
      type: "object",
      properties: {
        text: { type: "string" },
        limit: { type: "integer", default: 20 },
      },
    },
  },
  {
    name: "search_candidates",
    description: "Find candidates (sessions + invites) by email or name. Use before inviting to avoid duplicate invites.",
    inputSchema: {
      type: "object",
      properties: { query: { type: "string" } },
      required: ["query"],
    },
  },
  {
    name: "list_competencies",
    description: "List all competencies — useful when tagging questions.",
    inputSchema: { type: "object", properties: {}, required: [] },
  },

  // ── WRITE ──
  {
    name: "create_job_role",
    description:
      "Create a new job role under a department. IMPORTANT: Call search_job_roles first to confirm no duplicate exists. Present the proposed role to the user for confirmation before calling this tool. Optional externalId makes the call idempotent.",
    inputSchema: {
      type: "object",
      properties: {
        departmentId: { type: "string", description: "Department ID (from list_departments)" },
        title: { type: "string" },
        description: { type: "string" },
        externalId: { type: "string", description: "Idempotency key" },
      },
      required: ["departmentId", "title"],
    },
  },
  {
    name: "create_assessment",
    description:
      "Create a new assessment template with its first version, sections, and questions — all atomically. Drafts are created with isActive=false; admin must review in the portal before activating. IMPORTANT: search_assessments first and present the full structure for user confirmation before calling. Optional: pass `thresholds` to set Strong Hire / Hire / Consider cutoffs and `competencyIds` per question to tag.",
    inputSchema: {
      type: "object",
      properties: {
        jobRoleId: { type: "string" },
        title: { type: "string" },
        description: { type: "string" },
        timeLimit: { type: "integer", default: 45, description: "Minutes. Null/0 means unlimited." },
        thresholds: {
          type: "object",
          description: "Recommendation cutoffs (normalized 0..1). Must satisfy strongHire > hire > consider.",
          properties: {
            strongHire: { type: "number" },
            hire: { type: "number" },
            consider: { type: "number" },
          },
          required: ["strongHire", "hire", "consider"],
        },
        sections: {
          type: "array",
          items: {
            type: "object",
            properties: {
              title: { type: "string" },
              slug: { type: "string" },
              weight: { type: "number", description: "0.0-1.0 — all section weights MUST sum to ~1.0" },
              description: { type: "string" },
            },
            required: ["title", "weight"],
          },
        },
        questions: {
          type: "array",
          description: "Flat list of questions; each references sectionIndex (0-based index into sections array).",
          items: {
            type: "object",
            properties: {
              sectionIndex: { type: "integer" },
              prompt: { type: "string", description: "Full question text shown to candidate" },
              title: { type: "string", description: "Short label (optional; derived from prompt if omitted)" },
              questionType: {
                type: "string",
                enum: [
                  "single_select",
                  "multi_select",
                  "scenario",
                  "short_text",
                  "situational_judgment",
                  "ranking",
                  "confidence_rating",
                ],
              },
              difficulty: { type: "string", enum: ["easy", "medium", "hard"], default: "medium" },
              maxPoints: { type: "number", default: 1 },
              options: {
                type: "array",
                description: "For single_select/multi_select: array of {label, points}. Correct options have points>0; distractors 0.",
                items: {
                  type: "object",
                  properties: { label: { type: "string" }, points: { type: "number" } },
                  required: ["label", "points"],
                },
              },
              competencyIds: {
                type: "array",
                description: "Competency IDs (from list_competencies) to tag this question with.",
                items: { type: "string" },
              },
            },
            required: ["sectionIndex", "prompt", "questionType"],
          },
        },
        externalId: { type: "string", description: "Idempotency key — repeat calls return the existing record" },
      },
      required: ["jobRoleId", "title", "sections", "questions"],
    },
  },
  {
    name: "toggle_assessment_active",
    description: "Activate or deactivate an assessment template. Only call when the user explicitly asks to publish or unpublish.",
    inputSchema: {
      type: "object",
      properties: {
        id: { type: "string" },
        isActive: { type: "boolean" },
      },
      required: ["id", "isActive"],
    },
  },
  {
    name: "update_assessment",
    description:
      "Update an existing assessment's metadata (title, description, jobRoleId) and the latest version's settings (timeLimit, passingScore, recommendation thresholds). Mutates in place — does not create a new version. Use create_new_version first if you need to preserve the previous published version. All fields except `id` are optional; only the provided fields change.",
    inputSchema: {
      type: "object",
      properties: {
        id: { type: "string", description: "AssessmentTemplate ID" },
        title: { type: "string" },
        description: { type: "string" },
        jobRoleId: { type: "string", description: "Reassign to a different role" },
        timeLimit: { type: "integer", description: "Minutes; 0 or null = unlimited" },
        passingScore: { type: "number", description: "0..1 normalized score required to pass" },
        thresholds: {
          type: "object",
          description: "Recommendation cutoffs (normalized 0..1). strongHire > hire > consider.",
          properties: {
            strongHire: { type: "number" },
            hire: { type: "number" },
            consider: { type: "number" },
          },
          required: ["strongHire", "hire", "consider"],
        },
        eggHuntEnabled: {
          type: "boolean",
          description: "When true, candidates who finish this assessment see the egg-hunt CTA on their result page.",
        },
      },
      required: ["id"],
    },
  },
  {
    name: "add_section",
    description:
      "Add a new section to an existing assessment's latest version. Section weights do NOT auto-rebalance — use set_section_weights afterwards to rebalance to sum=1.0 before activating.",
    inputSchema: {
      type: "object",
      properties: {
        assessmentId: { type: "string" },
        title: { type: "string" },
        weight: { type: "number", description: "0..1; rebalance other sections via set_section_weights after." },
        description: { type: "string" },
        introText: { type: "string" },
        sortOrder: { type: "integer", description: "0-based; defaults to end" },
      },
      required: ["assessmentId", "title", "weight"],
    },
  },
  {
    name: "update_section",
    description:
      "Update a section's metadata. Does NOT change weight — use set_section_weights for that (it validates sum=1.0 atomically).",
    inputSchema: {
      type: "object",
      properties: {
        sectionId: { type: "string" },
        title: { type: "string" },
        description: { type: "string" },
        introText: { type: "string" },
      },
      required: ["sectionId"],
    },
  },
  {
    name: "remove_section",
    description:
      "Delete a section and all its questions. Refuses if any candidate has answered. Rebalance remaining section weights with set_section_weights afterwards.",
    inputSchema: {
      type: "object",
      properties: { sectionId: { type: "string" } },
      required: ["sectionId"],
    },
  },
  {
    name: "reorder_sections",
    description:
      "Reorder sections within an assessment. Pass every section ID exactly once in the desired order.",
    inputSchema: {
      type: "object",
      properties: {
        assessmentId: { type: "string" },
        orderedSectionIds: { type: "array", items: { type: "string" } },
      },
      required: ["assessmentId", "orderedSectionIds"],
    },
  },
  {
    name: "set_section_weights",
    description:
      "Atomically set the weight on every section of an assessment. Validates that weights sum to 1.0. Pass every section in the latest version exactly once.",
    inputSchema: {
      type: "object",
      properties: {
        assessmentId: { type: "string" },
        weights: {
          type: "array",
          items: {
            type: "object",
            properties: {
              sectionId: { type: "string" },
              weight: { type: "number" },
            },
            required: ["sectionId", "weight"],
          },
        },
      },
      required: ["assessmentId", "weights"],
    },
  },
  {
    name: "add_question",
    description:
      "Add a question to a section. For single_select/multi_select, supply options where correct answers have points>0. Optional competencyIds tag the question for analytics.",
    inputSchema: {
      type: "object",
      properties: {
        sectionId: { type: "string" },
        prompt: { type: "string" },
        title: { type: "string" },
        questionType: {
          type: "string",
          enum: [
            "single_select",
            "multi_select",
            "scenario",
            "ranking",
            "situational_judgment",
            "short_text",
            "confidence_rating",
          ],
        },
        difficulty: { type: "string", enum: ["easy", "medium", "hard"] },
        maxPoints: { type: "number" },
        options: {
          type: "array",
          items: {
            type: "object",
            properties: { label: { type: "string" }, points: { type: "number" } },
            required: ["label", "points"],
          },
        },
        competencyIds: { type: "array", items: { type: "string" } },
        explanation: { type: "string" },
        externalId: { type: "string", description: "Idempotency key" },
      },
      required: ["sectionId", "prompt", "questionType"],
    },
  },
  {
    name: "update_question",
    description:
      "Update a question in place. If `options` is provided, ALL existing options are replaced. If `competencyIds` is provided, ALL competency tags are replaced. Omit fields to leave them unchanged.",
    inputSchema: {
      type: "object",
      properties: {
        questionId: { type: "string" },
        prompt: { type: "string" },
        title: { type: "string" },
        questionType: {
          type: "string",
          enum: [
            "single_select",
            "multi_select",
            "scenario",
            "ranking",
            "situational_judgment",
            "short_text",
            "confidence_rating",
          ],
        },
        difficulty: { type: "string", enum: ["easy", "medium", "hard"] },
        maxPoints: { type: "number" },
        options: {
          type: "array",
          items: {
            type: "object",
            properties: { label: { type: "string" }, points: { type: "number" } },
            required: ["label", "points"],
          },
        },
        competencyIds: { type: "array", items: { type: "string" } },
        explanation: { type: "string" },
      },
      required: ["questionId"],
    },
  },
  {
    name: "reorder_questions",
    description: "Reorder questions within a section. Pass every question ID exactly once in the desired order.",
    inputSchema: {
      type: "object",
      properties: {
        sectionId: { type: "string" },
        orderedQuestionIds: { type: "array", items: { type: "string" } },
      },
      required: ["sectionId", "orderedQuestionIds"],
    },
  },
  {
    name: "update_thresholds",
    description:
      "Set the Strong Hire / Hire / Consider recommendation cutoffs on an assessment's latest version. Thin wrapper over update_assessment for clarity.",
    inputSchema: {
      type: "object",
      properties: {
        assessmentId: { type: "string" },
        strongHire: { type: "number" },
        hire: { type: "number" },
        consider: { type: "number" },
      },
      required: ["assessmentId", "strongHire", "hire", "consider"],
    },
  },
  {
    name: "create_question",
    description:
      "Create a standalone Question Bank entry under a department's hidden library template. Reusable across assessments via attach_question_to_section. Use add_question instead if you want the question to live inside a specific assessment section.",
    inputSchema: {
      type: "object",
      properties: {
        departmentId: { type: "string" },
        bankSectionSlug: {
          type: "string",
          enum: ["cultural-fit", "ai-awareness", "department-specific", "general"],
          default: "general",
        },
        prompt: { type: "string" },
        title: { type: "string" },
        questionType: {
          type: "string",
          enum: [
            "single_select",
            "multi_select",
            "scenario",
            "ranking",
            "situational_judgment",
            "short_text",
            "confidence_rating",
          ],
        },
        difficulty: { type: "string", enum: ["easy", "medium", "hard"] },
        maxPoints: { type: "number" },
        options: {
          type: "array",
          items: {
            type: "object",
            properties: { label: { type: "string" }, points: { type: "number" } },
            required: ["label", "points"],
          },
        },
        competencyIds: { type: "array", items: { type: "string" } },
        explanation: { type: "string" },
        externalId: { type: "string", description: "Idempotency key" },
      },
      required: ["departmentId", "prompt", "questionType"],
    },
  },
  {
    name: "attach_question_to_section",
    description:
      "Clone a question (typically a Bank entry) into a target section, including its options and competency tags. Returns the new question's ID. The source question is unchanged.",
    inputSchema: {
      type: "object",
      properties: {
        questionId: { type: "string", description: "Source question (e.g. a Bank entry)" },
        sectionId: { type: "string", description: "Target section to copy into" },
      },
      required: ["questionId", "sectionId"],
    },
  },
  {
    name: "detach_question_from_section",
    description:
      "Remove a question from its section (hard delete). Refuses if any candidate has answered it. Equivalent to delete_question but named for the attach/detach pair.",
    inputSchema: {
      type: "object",
      properties: { questionId: { type: "string" } },
      required: ["questionId"],
    },
  },
  {
    name: "get_session",
    description:
      "Read full state of a candidate session — status, timestamps, per-section + per-competency scores, every response, and final recommendation. Admin role required (returns PII).",
    inputSchema: {
      type: "object",
      properties: { sessionId: { type: "string" } },
      required: ["sessionId"],
    },
  },
  {
    name: "list_sessions",
    description:
      "Paginated browse of candidate sessions. Optional filters: assessmentId, jobRoleId, status, recommendation tier, candidateEmail, dateFrom/dateTo. Returns summary rows (no per-question data — use get_session for that). Cursor-based pagination: pass `cursor` from the previous response's `nextCursor` to get the next page.",
    inputSchema: {
      type: "object",
      properties: {
        assessmentId: { type: "string" },
        jobRoleId: { type: "string" },
        candidateEmail: { type: "string" },
        status: {
          type: "string",
          enum: ["not_started", "in_progress", "paused", "completed", "expired", "disqualified"],
        },
        recommendation: {
          type: "string",
          enum: ["strong_hire", "hire", "consider", "weak_fit", "reject"],
        },
        dateFrom: { type: "string", description: "ISO date (inclusive)" },
        dateTo: { type: "string", description: "ISO date (inclusive)" },
        limit: { type: "integer", description: "1..100, default 25" },
        cursor: { type: "string", description: "Opaque cursor from previous nextCursor" },
      },
    },
  },
  {
    name: "get_session_results",
    description:
      "Scoring-only view of a completed session — total + per-section + per-competency scores, recommendation, duration. Refuses if the session has no result yet (still in-flight).",
    inputSchema: {
      type: "object",
      properties: { sessionId: { type: "string" } },
      required: ["sessionId"],
    },
  },
  {
    name: "get_assessment_analytics",
    description:
      "Aggregate stats for an assessment: invite/completion counts, completion rate, score histogram, recommendation breakdown, per-section averages, per-competency averages, per-question pctCorrect + avg time. Optional dateFrom/dateTo filters.",
    inputSchema: {
      type: "object",
      properties: {
        assessmentId: { type: "string" },
        dateFrom: { type: "string" },
        dateTo: { type: "string" },
      },
      required: ["assessmentId"],
    },
  },
  {
    name: "get_question_analytics",
    description:
      "Per-question stats: % correct, avg time, distractor selection rates, discrimination index (top-tercile vs bottom-tercile delta when sample size ≥ 6).",
    inputSchema: {
      type: "object",
      properties: { questionId: { type: "string" } },
      required: ["questionId"],
    },
  },
  {
    name: "export_sessions",
    description:
      "Export every session for an assessment. format=json returns an array; format=csv returns a CSV string. Optional dateFrom/dateTo. Returns inline (no file download).",
    inputSchema: {
      type: "object",
      properties: {
        assessmentId: { type: "string" },
        format: { type: "string", enum: ["json", "csv"], default: "json" },
        dateFrom: { type: "string" },
        dateTo: { type: "string" },
      },
      required: ["assessmentId"],
    },
  },
  {
    name: "create_new_version",
    description:
      "Snapshot the current latest (or a specified) version's full tree into a new draft. Use this BEFORE editing a published assessment that has in-flight sessions — write tools refuse such edits otherwise. The new draft is editable; publish_version when done.",
    inputSchema: {
      type: "object",
      properties: {
        assessmentId: { type: "string" },
        copyFrom: { type: "string", description: "'latest' (default) or a specific versionId" },
      },
      required: ["assessmentId"],
    },
  },
  {
    name: "publish_version",
    description:
      "Make a draft version the active one. Atomically archives the previously-published version. New invites/sessions land on the newly published version; existing in-flight sessions stay on their original version.",
    inputSchema: {
      type: "object",
      properties: { versionId: { type: "string" } },
      required: ["versionId"],
    },
  },
  {
    name: "list_assessment_versions",
    description: "List every version of an assessment with status, publish date, and session count.",
    inputSchema: {
      type: "object",
      properties: { assessmentId: { type: "string" } },
      required: ["assessmentId"],
    },
  },
  {
    name: "get_assessment_version",
    description: "Full tree (sections, questions, options, competency tags, thresholds) at a specific version.",
    inputSchema: {
      type: "object",
      properties: { versionId: { type: "string" } },
      required: ["versionId"],
    },
  },
  {
    name: "revert_to_version",
    description:
      "Roll back to an earlier version. Internally clones that version's tree into a new draft and publishes it — so the old version is preserved as a historical record.",
    inputSchema: {
      type: "object",
      properties: {
        assessmentId: { type: "string" },
        versionId: { type: "string", description: "Version to revert to" },
      },
      required: ["assessmentId", "versionId"],
    },
  },
  {
    name: "create_candidate_invite",
    description:
      "Create a candidate invite for an assessment. By default the email is NOT sent — the invite is created and the link is returned for review. Only pass sendEmail=true when the user explicitly says 'send the invite'. search_candidates first to avoid duplicates.",
    inputSchema: {
      type: "object",
      properties: {
        email: { type: "string" },
        name: { type: "string" },
        assessmentId: { type: "string", description: "AssessmentTemplate ID" },
        expiresInDays: { type: "integer", default: 7 },
        sendEmail: { type: "boolean", default: false, description: "MUST be explicitly confirmed by the user" },
        externalId: { type: "string", description: "Idempotency key — repeat calls return the existing invite" },
      },
      required: ["email", "name", "assessmentId"],
    },
  },
  {
    name: "delete_question",
    description: "Delete a question. Preview its usage in assessments first if unsure.",
    inputSchema: {
      type: "object",
      properties: { id: { type: "string" } },
      required: ["id"],
    },
  },

  // ── Round 3: invite management ──
  {
    name: "get_invite",
    description:
      "Read full state of a candidate invite — status (pending/started/completed/expired/revoked), candidate, assessment, expiry, and the magic link.",
    inputSchema: {
      type: "object",
      properties: { inviteId: { type: "string" } },
      required: ["inviteId"],
    },
  },
  {
    name: "list_invites",
    description:
      "Cursor-paginated browse of candidate invites. Filters: assessmentId, candidateEmail, status (pending/started/completed/expired/revoked), dateFrom/dateTo. Same shape as list_sessions — pass `cursor` from the previous nextCursor for the next page.",
    inputSchema: {
      type: "object",
      properties: {
        assessmentId: { type: "string" },
        candidateEmail: { type: "string" },
        status: {
          type: "string",
          enum: ["pending", "started", "completed", "expired", "revoked"],
        },
        dateFrom: { type: "string", description: "ISO date (inclusive)" },
        dateTo: { type: "string", description: "ISO date (inclusive)" },
        limit: { type: "integer", description: "1..100, default 25" },
        cursor: { type: "string" },
      },
    },
  },
  {
    name: "revoke_invite",
    description:
      "Invalidate an unused invite. Refuses if the invite is already started (mid-assessment) or completed — wait for those to finish or expire.",
    inputSchema: {
      type: "object",
      properties: { inviteId: { type: "string" } },
      required: ["inviteId"],
    },
  },
  {
    name: "resend_invite",
    description:
      "Re-email the same invite link. Default sendEmail=false (consistent with create_candidate_invite — only set true when the user explicitly says 'send'). Optional newExpiryDays extends the expiry. Refuses if invite is completed or revoked.",
    inputSchema: {
      type: "object",
      properties: {
        inviteId: { type: "string" },
        newExpiryDays: { type: "integer", description: "If set, expiry resets to now + this many days" },
        sendEmail: { type: "boolean", default: false },
      },
      required: ["inviteId"],
    },
  },
  {
    name: "extend_invite_expiry",
    description:
      "Push an invite's expiry without resending or emailing. Use for 'give them another week' without making noise.",
    inputSchema: {
      type: "object",
      properties: {
        inviteId: { type: "string" },
        expiresInDays: { type: "integer", description: "Days from now" },
      },
      required: ["inviteId", "expiresInDays"],
    },
  },
  {
    name: "update_candidate",
    description:
      "Fix typos in a candidate's name or email pre-completion. Updates every invite + session row matching the original email. Refuses if any session for that candidate is already in completed/expired/disqualified state — audit integrity is preserved post-completion. Pass either inviteId (preferred) or candidateEmail to identify the candidate.",
    inputSchema: {
      type: "object",
      properties: {
        inviteId: { type: "string" },
        candidateEmail: { type: "string", description: "Use only if inviteId is unavailable" },
        name: { type: "string" },
        email: { type: "string" },
      },
    },
  },
  {
    name: "bulk_create_candidate_invites",
    description:
      "Invite a list of candidates in one call. Runs sequentially — partial failure is reported per row. sendEmail default false (must be explicit). Each candidate may carry its own externalId for idempotency. Returns per-row results plus success/failure counts.",
    inputSchema: {
      type: "object",
      properties: {
        assessmentId: { type: "string" },
        candidates: {
          type: "array",
          items: {
            type: "object",
            properties: {
              email: { type: "string" },
              name: { type: "string" },
              expiresInDays: { type: "integer" },
              externalId: { type: "string", description: "Idempotency key for this row" },
            },
            required: ["email", "name"],
          },
        },
        sendEmail: { type: "boolean", default: false },
      },
      required: ["assessmentId", "candidates"],
    },
  },

  // ── Round 3: duplicate / clone ──
  {
    name: "duplicate_assessment",
    description:
      "Deep-copy an assessment's latest version (sections, questions, options, weights, thresholds) into a new DRAFT assessment template. Optionally reassign to a different jobRoleId. The new assessment is isActive=false and its version is at versionNumber=1 — histories are not entangled.",
    inputSchema: {
      type: "object",
      properties: {
        assessmentId: { type: "string" },
        newTitle: { type: "string" },
        newJobRoleId: { type: "string", description: "Defaults to source assessment's jobRoleId" },
      },
      required: ["assessmentId", "newTitle"],
    },
  },
  {
    name: "duplicate_question",
    description:
      "Clone a question (options + competency tags) into the same section, or a different one if newSectionId is provided. The new question is independent — editing it does not touch the source. Functionally equivalent to attach_question_to_section but defaults the target to the source's own section.",
    inputSchema: {
      type: "object",
      properties: {
        questionId: { type: "string" },
        newSectionId: { type: "string", description: "Defaults to the source question's section" },
      },
      required: ["questionId"],
    },
  },

  // ── Round 3: admin CRUD ──
  {
    name: "create_competency",
    description:
      "Create a new competency. ALWAYS call list_competencies first to confirm no duplicate. Optional externalId for idempotency.",
    inputSchema: {
      type: "object",
      properties: {
        name: { type: "string" },
        description: { type: "string" },
        category: { type: "string" },
        externalId: { type: "string", description: "Idempotency key" },
      },
      required: ["name"],
    },
  },
  {
    name: "update_competency",
    description: "Update a competency's name/description/category. Pass only the fields that change.",
    inputSchema: {
      type: "object",
      properties: {
        id: { type: "string" },
        name: { type: "string" },
        description: { type: "string" },
        category: { type: "string" },
      },
      required: ["id"],
    },
  },
  {
    name: "archive_competency",
    description:
      "Archive a competency (sets archivedAt). Refuses if any active question on a draft/published version is still tagged with it — re-tag those first.",
    inputSchema: {
      type: "object",
      properties: { id: { type: "string" } },
      required: ["id"],
    },
  },
  {
    name: "create_department",
    description:
      "Create a new department. ALWAYS call list_departments first to confirm no duplicate. Optional externalId for idempotency.",
    inputSchema: {
      type: "object",
      properties: {
        name: { type: "string" },
        description: { type: "string" },
        externalId: { type: "string", description: "Idempotency key" },
      },
      required: ["name"],
    },
  },
  {
    name: "update_department",
    description: "Update a department's name or description.",
    inputSchema: {
      type: "object",
      properties: {
        id: { type: "string" },
        name: { type: "string" },
        description: { type: "string" },
      },
      required: ["id"],
    },
  },
  {
    name: "archive_department",
    description:
      "Archive a department (sets archivedAt). Refuses if any active job role still belongs to it — archive those roles first.",
    inputSchema: {
      type: "object",
      properties: { id: { type: "string" } },
      required: ["id"],
    },
  },
  {
    name: "update_job_role",
    description:
      "Update a job role's title, short description, department, or structured Job Description fields (jdSummary, jdResponsibilities, jdRequirements, jdNiceToHaves, jdYearsExperience — used by the recruitment pre-screening agent to score candidate CVs). Reassigning to an archived department is refused.",
    inputSchema: {
      type: "object",
      properties: {
        id: { type: "string" },
        title: { type: "string" },
        description: { type: "string", description: "Short blurb shown on /careers cards. Use jdSummary for the full overview." },
        departmentId: { type: "string" },
        jdSummary: { type: "string", description: "1–2 paragraph 'About this role' overview." },
        jdResponsibilities: { type: "string", description: "Multi-line bulleted list of day-to-day duties." },
        jdRequirements: { type: "string", description: "Multi-line list of must-have skills/experience/education." },
        jdNiceToHaves: { type: "string", description: "Multi-line list of bonus skills (optional)." },
        jdYearsExperience: { type: "string", description: "e.g. '3–5 years'." },
      },
      required: ["id"],
    },
  },
  {
    name: "archive_job_role",
    description:
      "Archive a job role (isActive=false). Refuses if any active assessment template references it — deactivate those assessments first.",
    inputSchema: {
      type: "object",
      properties: { id: { type: "string" } },
      required: ["id"],
    },
  },

  // ── Round 3: automation hooks ──
  {
    name: "lookup_by_external_id",
    description:
      "Look up an existing record by its caller-supplied externalId. Use this when integrating an upstream system to map an external ID back to an Assessify ID without risking a duplicate create_*. Returns { type, externalId, found, record }.",
    inputSchema: {
      type: "object",
      properties: {
        type: {
          type: "string",
          enum: ["assessment", "candidate_invite", "competency", "department", "job_role", "question"],
        },
        externalId: { type: "string" },
      },
      required: ["type", "externalId"],
    },
  },
  {
    name: "bulk_tag_questions",
    description:
      "Atomically apply competency tags to a set of questions. Mode: 'replace' (drop existing then set), 'add' (union), or 'remove' (delete listed tags). Refuses if any target question lives on a published version with in-flight sessions.",
    inputSchema: {
      type: "object",
      properties: {
        questionIds: { type: "array", items: { type: "string" } },
        competencyIds: { type: "array", items: { type: "string" } },
        mode: { type: "string", enum: ["replace", "add", "remove"] },
      },
      required: ["questionIds", "competencyIds", "mode"],
    },
  },
  {
    name: "bulk_delete_questions",
    description:
      "Delete a batch of questions atomically. Refuses the WHOLE batch if any question has candidate responses — re-call with the safe subset.",
    inputSchema: {
      type: "object",
      properties: {
        questionIds: { type: "array", items: { type: "string" } },
      },
      required: ["questionIds"],
    },
  },
  {
    name: "bulk_toggle_assessment_active",
    description:
      "Activate or deactivate a list of assessment templates in one call. IDs not found are returned in `notFound`; assessments already in the target state are counted in `alreadyInStateCount`. Only call when the user explicitly asks to publish or unpublish.",
    inputSchema: {
      type: "object",
      properties: {
        assessmentIds: { type: "array", items: { type: "string" } },
        isActive: { type: "boolean" },
      },
      required: ["assessmentIds", "isActive"],
    },
  },
  // ── Recruitment pipeline (Phase 1.A) ──
  {
    name: "recruitment_search_candidates",
    description:
      "Search the recruitment Candidate table (people who applied for roles via the intake form) by email, name, office, or source. Distinct from `search_candidates`, which searches assessment sessions/invites.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "Free-text match against name/email/agency" },
        office: { type: "string", description: "Dubai or Singapore" },
        source: { type: "string", description: "agency | direct | career_page | referral" },
        limit: { type: "integer", default: 25 },
      },
    },
  },
  {
    name: "recruitment_get_candidate",
    description: "Get a recruitment Candidate by id, including all applications and recent invites.",
    inputSchema: {
      type: "object",
      properties: { id: { type: "string" } },
      required: ["id"],
    },
  },
  {
    name: "recruitment_create_candidate",
    description:
      "Create a recruitment Candidate manually. Prefer letting agencies use the intake form — only call this for one-off referrals or imports.",
    inputSchema: {
      type: "object",
      properties: {
        firstName: { type: "string" },
        lastName: { type: "string" },
        email: { type: "string" },
        phoneNumber: { type: "string" },
        nationality: { type: "string" },
        noticePeriod: { type: "string" },
        office: { type: "string" },
        source: { type: "string" },
        agencyName: { type: "string" },
        linkedinUrl: { type: "string" },
        cvDriveUrl: { type: "string" },
        externalId: { type: "string" },
        // Phase 1.B v3 — extended intake fields
        currentlyEmployed: {
          type: "string",
          enum: ["employed", "not_working", "freelancing"],
          description: "Employment status at time of application.",
        },
        visaStatus: {
          type: "string",
          description:
            "Free text. Examples: 'UAE Resident', 'Employment-Sponsored', 'Golden Visa', 'Tourist', 'No visa'.",
        },
        aiToolsProficiency: {
          type: "string",
          description:
            "Free text describing which AI tools the candidate uses (e.g. 'ChatGPT daily, Cursor IDE, Midjourney').",
        },
        hasDriversLicense: { type: "boolean" },
        locationStatus: {
          type: "string",
          enum: ["in_uae", "outside_uae"],
          description: "Where the candidate is currently located.",
        },
      },
      required: ["firstName", "lastName", "email"],
    },
  },
  {
    name: "recruitment_update_candidate",
    description: "Patch a recruitment Candidate by id. Pass only fields you want to change.",
    inputSchema: {
      type: "object",
      properties: {
        id: { type: "string" },
        firstName: { type: "string" },
        lastName: { type: "string" },
        phoneNumber: { type: "string" },
        nationality: { type: "string" },
        noticePeriod: { type: "string" },
        office: { type: "string" },
        source: { type: "string" },
        agencyName: { type: "string" },
        linkedinUrl: { type: "string" },
        cvDriveUrl: { type: "string" },
        cvDriveFolderUrl: { type: "string" },
        archived: { type: "boolean", description: "Set true to soft-archive" },
        // Phase 1.B v3 — extended intake fields
        currentlyEmployed: { type: "string", enum: ["employed", "not_working", "freelancing"] },
        visaStatus: { type: "string" },
        aiToolsProficiency: { type: "string" },
        hasDriversLicense: { type: ["boolean", "null"] },
        locationStatus: { type: "string", enum: ["in_uae", "outside_uae"] },
      },
      required: ["id"],
    },
  },
  {
    name: "recruitment_create_application",
    description:
      "Create an Application linking an existing Candidate to a JobRole. Use when a candidate applies for a second role, or when manually adding a referral.",
    inputSchema: {
      type: "object",
      properties: {
        candidateId: { type: "string" },
        jobRoleId: { type: "string" },
        office: { type: "string" },
        source: { type: "string" },
        agencyName: { type: "string" },
        externalId: { type: "string" },
        cvReceivedAt: {
          type: "string",
          description:
            "ISO date or datetime when the agency delivered the CV. Distinct from row creation time. Example: '2026-04-28' or '2026-04-28T10:00:00Z'.",
        },
      },
      required: ["candidateId", "jobRoleId"],
    },
  },
  {
    name: "recruitment_list_applications",
    description:
      "List Applications with filters. Each row includes candidate + jobRole. Cursor paginated.",
    inputSchema: {
      type: "object",
      properties: {
        currentStage: { type: "string" },
        status: { type: "string" },
        jobRoleId: { type: "string" },
        office: { type: "string" },
        source: { type: "string" },
        cursor: { type: "string" },
        limit: { type: "integer", default: 25 },
      },
    },
  },
  // ─── Recruitment scoring rubrics ────────────────────────────
  {
    name: "recruitment_list_rubrics",
    description:
      "List recruitment scoring rubrics. A rubric defines how the AI scores a candidate (the dimensions, their weights, and the recommendation thresholds). Filter by kind (pre_interview / post_interview), by jobRoleId (use the literal string \"global\" to match the global default rubric), and by isActive. Returns the rubric metadata plus its full criteria array.",
    inputSchema: {
      type: "object",
      properties: {
        kind: {
          type: "string",
          enum: ["pre_interview", "post_interview"],
          description: "Filter by rubric kind. Omit to return both.",
        },
        jobRoleId: {
          type: "string",
          description:
            "Filter by job role. Pass a JobRole id, or the literal \"global\" to match the global default rubric (jobRoleId is null in storage).",
        },
        isActive: {
          type: "boolean",
          description:
            "If true, only active rubrics. If false, only archived. Omit to return both.",
        },
      },
    },
  },
  {
    name: "recruitment_get_rubric",
    description:
      "Fetch a single recruitment rubric by id, including all criteria, weights, scoring prompts, and thresholds.",
    inputSchema: {
      type: "object",
      properties: { rubricId: { type: "string" } },
      required: ["rubricId"],
    },
  },
  {
    name: "recruitment_create_rubric",
    description:
      "Create a new recruitment scoring rubric. Criteria weights MUST sum to exactly 1.0 (within 0.001). Thresholds must descend (thresholdStrong > thresholdMatch > thresholdConsider). When jobRoleId is null/omitted, the rubric becomes the global default for the given kind. Each criterion has: key (snake_case unique within the rubric), label (human-readable title shown in the report), weight (0..1), scoringPrompt (instructions to the scoring agent — describe what to look for and how to assign 0–10), commentaryGuidance (optional — what facts the AI should reference), redFlagSignals (optional array of strings that surface as risks).",
    inputSchema: {
      type: "object",
      properties: {
        name: { type: "string", description: "Human-readable rubric name." },
        kind: {
          type: "string",
          enum: ["pre_interview", "post_interview"],
          description:
            "When the rubric is used: pre_interview scores from the CV; post_interview scores from interview transcripts/notes.",
        },
        jobRoleId: {
          type: ["string", "null"],
          description:
            "JobRole id to scope this rubric to. Pass null (or omit) for the global default rubric for the given kind.",
        },
        isActive: { type: "boolean", default: true },
        thresholdStrong: {
          type: "number",
          description: "Composite ≥ this → Strong Hire. Typical: 0.85.",
          default: 0.85,
        },
        thresholdMatch: {
          type: "number",
          description: "Composite ≥ this → Hire. Typical: 0.7.",
          default: 0.7,
        },
        thresholdConsider: {
          type: "number",
          description:
            "Composite ≥ this → Conditional Advance. Below 70% of this → Do Not Advance. Typical: 0.55.",
          default: 0.55,
        },
        criteria: {
          type: "array",
          minItems: 1,
          description:
            "Scoring dimensions. Weights must sum to 1.0. Each criterion's key must be unique within the rubric.",
          items: {
            type: "object",
            required: ["label", "weight", "scoringPrompt"],
            properties: {
              key: {
                type: "string",
                description:
                  "Optional snake_case identifier. If omitted, derived from the label. Must be unique within the rubric.",
              },
              label: { type: "string", description: "Human-readable title." },
              weight: {
                type: "number",
                minimum: 0,
                maximum: 1,
                description: "Fraction of the composite score, 0..1.",
              },
              scoringPrompt: {
                type: "string",
                description:
                  "Instructions to the scoring agent. Describe what to look for and how to assign a 0–10 score, including band examples.",
              },
              commentaryGuidance: {
                type: "string",
                description:
                  "Optional. What specific facts the AI should reference in its commentary on this dimension.",
              },
              redFlagSignals: {
                type: "array",
                items: { type: "string" },
                description:
                  "Optional. Specific concerns that, if found, should appear in the candidate's risk register.",
              },
            },
          },
        },
      },
      required: ["name", "kind", "criteria"],
    },
  },
  {
    name: "recruitment_update_rubric",
    description:
      "Update an existing recruitment rubric. Pass only the fields you want to change. If criteria is included, it REPLACES the existing criteria (weights must still sum to 1.0).",
    inputSchema: {
      type: "object",
      properties: {
        rubricId: { type: "string" },
        name: { type: "string" },
        kind: { type: "string", enum: ["pre_interview", "post_interview"] },
        jobRoleId: { type: ["string", "null"] },
        isActive: { type: "boolean" },
        thresholdStrong: { type: "number" },
        thresholdMatch: { type: "number" },
        thresholdConsider: { type: "number" },
        criteria: {
          type: "array",
          items: {
            type: "object",
            required: ["label", "weight", "scoringPrompt"],
            properties: {
              key: { type: "string" },
              label: { type: "string" },
              weight: { type: "number", minimum: 0, maximum: 1 },
              scoringPrompt: { type: "string" },
              commentaryGuidance: { type: "string" },
              redFlagSignals: { type: "array", items: { type: "string" } },
            },
          },
        },
      },
      required: ["rubricId"],
    },
  },
  {
    name: "recruitment_delete_rubric",
    description:
      "Delete a recruitment rubric. If any ApplicationScores reference it, it is soft-archived (isActive=false) to preserve historical scores. If unreferenced, it is hard-deleted.",
    inputSchema: {
      type: "object",
      properties: { rubricId: { type: "string" } },
      required: ["rubricId"],
    },
  },
  {
    name: "recruitment_clone_rubric",
    description:
      "Clone an existing rubric into a new one (with a new name and optionally a new jobRoleId / kind). Use this to seed a role-specific rubric from the global default.",
    inputSchema: {
      type: "object",
      properties: {
        rubricId: { type: "string", description: "Source rubric id to clone." },
        name: { type: "string", description: "Name for the new rubric." },
        jobRoleId: {
          type: ["string", "null"],
          description: "Target jobRoleId, or null for global. Defaults to the source's jobRoleId.",
        },
        kind: {
          type: "string",
          enum: ["pre_interview", "post_interview"],
          description: "Defaults to the source's kind.",
        },
      },
      required: ["rubricId", "name"],
    },
  },
  // ─── Team management — Employees & Line Managers ─────────────
  {
    name: "team_list_employees",
    description:
      "List Employee records used by the leave-request system. Each row may include the assigned line manager.",
    inputSchema: {
      type: "object",
      properties: {
        isActive: { type: "boolean", description: "Filter by active flag. Omit to return both." },
        department: { type: "string" },
      },
    },
  },
  {
    name: "team_create_employee",
    description:
      "Create a new Employee. Powers the leave-request dropdown and Slack DMs. slackUserId is what's used at runtime for DMs; slackHandle is a friendly fallback. lineManagerId is optional — link later via team_link_employee_to_manager if not known at creation.",
    inputSchema: {
      type: "object",
      properties: {
        firstName: { type: "string" },
        fullName: { type: "string" },
        email: { type: "string" },
        slackUserId: { type: "string" },
        slackHandle: { type: "string" },
        department: { type: "string" },
        isActive: { type: "boolean", default: true },
        lineManagerId: { type: ["string", "null"] },
      },
      required: ["firstName"],
    },
  },
  {
    name: "team_update_employee",
    description: "Patch an Employee. Pass only fields you want to change.",
    inputSchema: {
      type: "object",
      properties: {
        employeeId: { type: "string" },
        firstName: { type: "string" },
        fullName: { type: ["string", "null"] },
        email: { type: ["string", "null"] },
        slackUserId: { type: ["string", "null"] },
        slackHandle: { type: ["string", "null"] },
        department: { type: ["string", "null"] },
        isActive: { type: "boolean" },
        lineManagerId: { type: ["string", "null"] },
      },
      required: ["employeeId"],
    },
  },
  {
    name: "team_archive_employee",
    description: "Soft-archive an Employee by setting isActive=false. Leave history is preserved.",
    inputSchema: {
      type: "object",
      properties: { employeeId: { type: "string" } },
      required: ["employeeId"],
    },
  },
  {
    name: "team_list_managers",
    description: "List LineManager records. Optionally filter by isActive.",
    inputSchema: {
      type: "object",
      properties: { isActive: { type: "boolean" } },
    },
  },
  {
    name: "team_create_manager",
    description:
      "Create a new LineManager. slackUserId is required for the bot to DM them for leave approvals — fetch from Slack admin or use lookupByEmail.",
    inputSchema: {
      type: "object",
      properties: {
        name: { type: "string" },
        email: { type: "string" },
        slackUserId: { type: "string" },
        slackHandle: { type: "string" },
        isActive: { type: "boolean", default: true },
      },
      required: ["name"],
    },
  },
  {
    name: "team_update_manager",
    description: "Patch a LineManager.",
    inputSchema: {
      type: "object",
      properties: {
        managerId: { type: "string" },
        name: { type: "string" },
        email: { type: ["string", "null"] },
        slackUserId: { type: ["string", "null"] },
        slackHandle: { type: ["string", "null"] },
        isActive: { type: "boolean" },
      },
      required: ["managerId"],
    },
  },
  {
    name: "team_archive_manager",
    description:
      "Soft-archive a LineManager. Any employees with lineManagerId pointing to this manager will be un-linked (set to null) to avoid dangling references.",
    inputSchema: {
      type: "object",
      properties: { managerId: { type: "string" } },
      required: ["managerId"],
    },
  },
  {
    name: "team_link_employee_to_manager",
    description:
      "Convenience: assign an Employee to a LineManager. Pass managerId=null to un-link.",
    inputSchema: {
      type: "object",
      properties: {
        employeeId: { type: "string" },
        managerId: { type: ["string", "null"] },
      },
      required: ["employeeId"],
    },
  },
] as const;

// ─── Tool handlers ────────────────────────────────────────────

type ToolArgs = Record<string, unknown>;

export async function callTool(
  name: string,
  args: ToolArgs,
  session: McpSession,
  clientIp: string | null
): Promise<ToolResult> {
  try {
    switch (name) {
      case "list_departments":
        return await listDepartments();
      case "search_job_roles":
        return await searchJobRoles(args);
      case "search_assessments":
        return await searchAssessments(args);
      case "get_assessment":
        return await getAssessment(args);
      case "search_questions":
        return await searchQuestions(args);
      case "search_candidates":
        return await searchCandidates(args);
      case "list_competencies":
        return await listCompetencies();
      case "create_job_role":
        return await createJobRole(args, session, clientIp);
      case "create_assessment":
        return await createAssessment(args, session, clientIp);
      case "toggle_assessment_active":
        return await toggleAssessmentActive(args, session, clientIp);
      case "update_assessment":
        return await updateAssessmentTool(args, session, clientIp);
      case "update_thresholds":
        return await updateThresholdsTool(args, session, clientIp);
      case "add_section":
        return await addSectionTool(args, session, clientIp);
      case "update_section":
        return await updateSectionTool(args, session, clientIp);
      case "remove_section":
        return await removeSectionTool(args, session, clientIp);
      case "reorder_sections":
        return await reorderSectionsTool(args, session, clientIp);
      case "set_section_weights":
        return await setSectionWeightsTool(args, session, clientIp);
      case "add_question":
        return await addQuestionTool(args, session, clientIp);
      case "update_question":
        return await updateQuestionTool(args, session, clientIp);
      case "reorder_questions":
        return await reorderQuestionsTool(args, session, clientIp);
      case "create_question":
        return await createBankQuestionTool(args, session, clientIp);
      case "attach_question_to_section":
        return await attachQuestionTool(args, session, clientIp);
      case "detach_question_from_section":
        return await detachQuestionTool(args, session, clientIp);
      case "get_session":
        return await getSessionTool(args, session, clientIp);
      case "list_sessions":
        return await listSessionsTool(args, session, clientIp);
      case "get_session_results":
        return await getSessionResultsTool(args, session, clientIp);
      case "get_assessment_analytics":
        return await getAssessmentAnalyticsTool(args, session, clientIp);
      case "get_question_analytics":
        return await getQuestionAnalyticsTool(args, session, clientIp);
      case "export_sessions":
        return await exportSessionsTool(args, session, clientIp);
      case "create_new_version":
        return await createNewVersionTool(args, session, clientIp);
      case "publish_version":
        return await publishVersionTool(args, session, clientIp);
      case "list_assessment_versions":
        return await listAssessmentVersionsTool(args, session);
      case "get_assessment_version":
        return await getAssessmentVersionTool(args, session);
      case "revert_to_version":
        return await revertToVersionTool(args, session, clientIp);
      case "create_candidate_invite":
        return await createCandidateInvite(args, session, clientIp);
      case "delete_question":
        return await deleteQuestion(args, session, clientIp);
      case "get_invite":
        return await getInviteTool(args, session, clientIp);
      case "list_invites":
        return await listInvitesTool(args, session, clientIp);
      case "revoke_invite":
        return await revokeInviteTool(args, session, clientIp);
      case "resend_invite":
        return await resendInviteTool(args, session, clientIp);
      case "extend_invite_expiry":
        return await extendInviteExpiryTool(args, session, clientIp);
      case "update_candidate":
        return await updateCandidateTool(args, session, clientIp);
      case "bulk_create_candidate_invites":
        return await bulkCreateInvitesTool(args, session, clientIp);
      case "duplicate_assessment":
        return await duplicateAssessmentTool(args, session, clientIp);
      case "duplicate_question":
        return await duplicateQuestionTool(args, session, clientIp);
      case "create_competency":
        return await createCompetencyTool(args, session, clientIp);
      case "update_competency":
        return await updateCompetencyTool(args, session, clientIp);
      case "archive_competency":
        return await archiveCompetencyTool(args, session, clientIp);
      case "create_department":
        return await createDepartmentTool(args, session, clientIp);
      case "update_department":
        return await updateDepartmentTool(args, session, clientIp);
      case "archive_department":
        return await archiveDepartmentTool(args, session, clientIp);
      case "update_job_role":
        return await updateJobRoleTool(args, session, clientIp);
      case "archive_job_role":
        return await archiveJobRoleTool(args, session, clientIp);
      case "lookup_by_external_id":
        return await lookupByExternalIdTool(args, session);
      case "bulk_tag_questions":
        return await bulkTagQuestionsTool(args, session, clientIp);
      case "bulk_delete_questions":
        return await bulkDeleteQuestionsTool(args, session, clientIp);
      case "bulk_toggle_assessment_active":
        return await bulkToggleAssessmentActiveTool(args, session, clientIp);
      case "recruitment_search_candidates":
        return await recruitmentSearchCandidatesTool(args, session);
      case "recruitment_get_candidate":
        return await recruitmentGetCandidateTool(args, session);
      case "recruitment_create_candidate":
        return await recruitmentCreateCandidateTool(args, session, clientIp);
      case "recruitment_update_candidate":
        return await recruitmentUpdateCandidateTool(args, session, clientIp);
      case "recruitment_create_application":
        return await recruitmentCreateApplicationTool(args, session, clientIp);
      case "recruitment_list_applications":
        return await recruitmentListApplicationsTool(args, session);
      case "recruitment_list_rubrics":
        return await recruitmentListRubricsTool(args);
      case "recruitment_get_rubric":
        return await recruitmentGetRubricTool(args);
      case "recruitment_create_rubric":
        return await recruitmentCreateRubricTool(args, session, clientIp);
      case "recruitment_update_rubric":
        return await recruitmentUpdateRubricTool(args, session, clientIp);
      case "recruitment_delete_rubric":
        return await recruitmentDeleteRubricTool(args, session, clientIp);
      case "recruitment_clone_rubric":
        return await recruitmentCloneRubricTool(args, session, clientIp);
      case "team_list_employees":
        return await teamListEmployeesTool(args);
      case "team_create_employee":
        return await teamCreateEmployeeTool(args, session, clientIp);
      case "team_update_employee":
        return await teamUpdateEmployeeTool(args, session, clientIp);
      case "team_archive_employee":
        return await teamArchiveEmployeeTool(args, session, clientIp);
      case "team_list_managers":
        return await teamListManagersTool(args);
      case "team_create_manager":
        return await teamCreateManagerTool(args, session, clientIp);
      case "team_update_manager":
        return await teamUpdateManagerTool(args, session, clientIp);
      case "team_archive_manager":
        return await teamArchiveManagerTool(args, session, clientIp);
      case "team_link_employee_to_manager":
        return await teamLinkEmployeeToManagerTool(args, session, clientIp);
      default:
        return fail(`Unknown tool: ${name}`);
    }
  } catch (e) {
    if (e instanceof McpPermissionError) return fail(e.message);
    if (e instanceof McpValidationError) return fail(`validation: ${e.message}`);
    const msg = e instanceof Error ? e.message : String(e);
    return fail(msg);
  }
}

// ─── READ ──────────────────────────────────────────────────────

async function listDepartments(): Promise<ToolResult> {
  const rows = await prisma.department.findMany({
    orderBy: { name: "asc" },
    include: { _count: { select: { jobRoles: true } } },
  });
  return ok(rows.map((d) => ({ id: d.id, name: d.name, slug: d.slug, jobRoleCount: d._count.jobRoles })));
}

async function searchJobRoles(args: ToolArgs): Promise<ToolResult> {
  const query = (args.query as string | undefined)?.trim();
  const departmentId = args.departmentId as string | undefined;
  const rows = await prisma.jobRole.findMany({
    where: {
      ...(departmentId ? { departmentId } : {}),
      ...(query
        ? {
            OR: [
              { title: { contains: query } },
              { slug: { contains: query } },
              { description: { contains: query } },
            ],
          }
        : {}),
    },
    include: { department: true, _count: { select: { assessmentTemplates: true } } },
    orderBy: { title: "asc" },
    take: 50,
  });
  return ok(
    rows.map((r) => ({
      id: r.id,
      title: r.title,
      slug: r.slug,
      description: r.description,
      isActive: r.isActive,
      department: r.department.name,
      departmentId: r.department.id,
      assessmentCount: r._count.assessmentTemplates,
    }))
  );
}

async function searchAssessments(args: ToolArgs): Promise<ToolResult> {
  const query = (args.query as string | undefined)?.trim();
  const jobRoleId = args.jobRoleId as string | undefined;
  const activeOnly = Boolean(args.activeOnly);
  const rows = await prisma.assessmentTemplate.findMany({
    where: {
      ...(jobRoleId ? { jobRoleId } : {}),
      ...(activeOnly ? { isActive: true } : {}),
      ...(query ? { OR: [{ title: { contains: query } }, { slug: { contains: query } }] } : {}),
    },
    include: {
      jobRole: { include: { department: true } },
      versions: { orderBy: { versionNumber: "desc" }, take: 1, select: { id: true, versionNumber: true } },
    },
    take: 50,
    orderBy: { updatedAt: "desc" },
  });
  return ok(
    rows.map((r) => ({
      id: r.id,
      title: r.title,
      slug: r.slug,
      description: r.description,
      isActive: r.isActive,
      jobRole: r.jobRole.title,
      jobRoleId: r.jobRoleId,
      department: r.jobRole.department.name,
      latestVersionId: r.versions[0]?.id ?? null,
      latestVersionNumber: r.versions[0]?.versionNumber ?? null,
    }))
  );
}

async function getAssessment(args: ToolArgs): Promise<ToolResult> {
  const id = args.id as string;
  const t = await prisma.assessmentTemplate.findUnique({
    where: { id },
    include: {
      jobRole: { include: { department: true } },
      versions: {
        orderBy: { versionNumber: "desc" },
        take: 1,
        include: {
          sections: { orderBy: { sortOrder: "asc" }, include: { questions: { include: { options: true } } } },
        },
      },
    },
  });
  if (!t) return fail(`Assessment ${id} not found`);
  const v = t.versions[0];
  return ok({
    id: t.id,
    title: t.title,
    description: t.description,
    isActive: t.isActive,
    jobRole: t.jobRole.title,
    department: t.jobRole.department.name,
    versionId: v?.id,
    versionNumber: v?.versionNumber,
    sections:
      v?.sections.map((s) => ({
        id: s.id,
        title: s.title,
        slug: s.slug,
        weight: s.weight,
        questionCount: s.questions.length,
        questions: s.questions.map((q) => ({
          id: q.id,
          title: q.title,
          prompt: q.prompt,
          questionType: q.questionType,
          difficulty: q.difficulty,
          maxPoints: q.maxPoints,
          options: q.options.map((o) => ({ key: o.key, label: o.label, points: o.points, isCorrect: o.isCorrect })),
        })),
      })) ?? [],
  });
}

async function searchQuestions(args: ToolArgs): Promise<ToolResult> {
  const text = (args.text as string | undefined)?.trim();
  const limit = Number(args.limit ?? 20);
  const rows = await prisma.question.findMany({
    where: text
      ? { OR: [{ prompt: { contains: text } }, { title: { contains: text } }] }
      : {},
    include: { options: true, section: true },
    take: Math.min(limit, 100),
  });
  return ok(
    rows.map((q) => ({
      id: q.id,
      title: q.title,
      prompt: q.prompt,
      questionType: q.questionType,
      difficulty: q.difficulty,
      section: q.section?.title,
      optionCount: q.options.length,
    }))
  );
}

async function searchCandidates(args: ToolArgs): Promise<ToolResult> {
  const q = ((args.query as string) || "").trim();
  if (!q) return fail("query required");
  const [invites, sessions] = await Promise.all([
    prisma.candidateInvite.findMany({
      where: {
        OR: [{ candidateEmail: { contains: q } }, { candidateName: { contains: q } }],
      },
      include: { template: true },
      take: 20,
      orderBy: { createdAt: "desc" },
    }),
    prisma.candidateSession.findMany({
      where: {
        OR: [{ candidateEmail: { contains: q } }, { candidateName: { contains: q } }],
      },
      include: { version: { include: { template: true } } },
      take: 20,
      orderBy: { createdAt: "desc" },
    }),
  ]);
  return ok({
    invites: invites.map((i) => ({
      id: i.id,
      code: i.code,
      email: i.candidateEmail,
      name: i.candidateName,
      status: i.status,
      assessment: i.template.title,
      expiresAt: i.expiresAt,
      createdAt: i.createdAt,
    })),
    sessions: sessions.map((s) => ({
      id: s.id,
      email: s.candidateEmail,
      name: s.candidateName,
      status: s.status,
      assessment: s.version.template.title,
      startedAt: s.startedAt,
      completedAt: s.completedAt,
    })),
  });
}

async function listCompetencies(): Promise<ToolResult> {
  const rows = await prisma.competency.findMany({ orderBy: { name: "asc" } });
  return ok(rows.map((c) => ({ id: c.id, name: c.name, slug: c.slug, description: c.description })));
}

// ─── WRITE ─────────────────────────────────────────────────────

async function createJobRole(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  if (session.role !== "admin") return fail("admin role required");
  const { departmentId, title, description, externalId } = args as {
    departmentId: string;
    title: string;
    description?: string;
    externalId?: string;
  };
  if (!departmentId || !title) return fail("departmentId and title required");

  if (externalId) {
    const hit = await findByExternalId("job_role", externalId);
    if (hit) {
      const full = await prisma.jobRole.findUnique({
        where: { id: hit.id },
        include: { department: true },
      });
      if (full) {
        return ok({
          id: full.id,
          title: full.title,
          slug: full.slug,
          department: full.department.name,
          idempotent: true,
          portalUrl: `/admin/departments`,
        });
      }
    }
  }

  const dept = await prisma.department.findUnique({ where: { id: departmentId } });
  if (!dept) return fail(`Department ${departmentId} not found`);

  const slug = slugify(title);
  const existing = await prisma.jobRole.findFirst({
    where: { OR: [{ slug }, { AND: [{ departmentId }, { title }] }] },
  });
  if (existing) {
    return fail(
      `Duplicate: a job role titled "${existing.title}" (slug: ${existing.slug}) already exists in ${dept.name}. Use id=${existing.id} or rename.`
    );
  }

  const row = await prisma.jobRole.create({
    data: {
      departmentId,
      title,
      slug,
      description: description || null,
      ...(externalId ? { externalId } : {}),
    },
  });

  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.job_role.created",
    targetType: "JobRole",
    targetId: row.id,
    details: { title, slug, department: dept.name, mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });

  return ok({
    id: row.id,
    title: row.title,
    slug: row.slug,
    department: dept.name,
    portalUrl: `/admin/departments`,
  });
}

async function createAssessment(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const {
    jobRoleId,
    title,
    description,
    timeLimit = 45,
    sections = [],
    questions = [],
    thresholds,
    externalId,
  } = args as {
    jobRoleId: string;
    title: string;
    description?: string;
    timeLimit?: number;
    sections?: Array<{ title: string; slug?: string; weight: number; description?: string }>;
    questions?: Array<{
      sectionIndex: number;
      prompt: string;
      title?: string;
      questionType: string;
      difficulty?: string;
      maxPoints?: number;
      options?: Array<{ label: string; points: number }>;
      competencyIds?: string[];
    }>;
    thresholds?: { strongHire: number; hire: number; consider: number };
    externalId?: string;
  };

  if (!jobRoleId || !title || sections.length === 0) {
    return fail("jobRoleId, title, and at least one section required");
  }

  if (externalId) {
    const hit = await findByExternalId("assessment", externalId);
    if (hit) {
      const full = await prisma.assessmentTemplate.findUnique({
        where: { id: hit.id },
        select: { id: true, title: true, slug: true, isActive: true },
      });
      if (full) {
        return ok({
          ...full,
          idempotent: true,
          portalUrl: `/admin/assessments/${full.id}/edit`,
        });
      }
    }
  }

  const role = await prisma.jobRole.findUnique({ where: { id: jobRoleId } });
  if (!role) return fail(`Job role ${jobRoleId} not found`);

  const slug = slugify(title);
  const existing = await prisma.assessmentTemplate.findFirst({ where: { slug } });
  if (existing) {
    return fail(`Duplicate: assessment with slug "${slug}" already exists (id=${existing.id}). Rename or update the existing one.`);
  }

  const weightSum = sections.reduce((s, x) => s + (x.weight || 0), 0);
  if (Math.abs(weightSum - 1) > 0.01) {
    return fail(`Section weights must sum to ~1.0 (got ${weightSum.toFixed(2)}). Adjust and retry.`);
  }

  if (thresholds) {
    assertThresholds(thresholds);
  }

  // Validate every competencyId referenced across all questions before any DB
  // writes — surfaces typos as a single readable error rather than mid-transaction.
  const allCompetencyIds = Array.from(
    new Set(questions.flatMap((q) => q.competencyIds ?? []))
  );
  if (allCompetencyIds.length > 0) {
    await assertCompetencyIdsExist(allCompetencyIds);
  }

  const created = await prisma.$transaction(async (tx) => {
    const tpl = await tx.assessmentTemplate.create({
      data: {
        jobRoleId,
        title,
        slug,
        description: description || null,
        isActive: false,
        ...(externalId ? { externalId } : {}),
      },
    });

    const version = await tx.assessmentVersion.create({
      data: {
        templateId: tpl.id,
        versionNumber: 1,
        status: "draft",
        passingScore: 0.6,
        timeLimit,
        recommendationThresholds: thresholds ? JSON.stringify(thresholds) : null,
      },
    });

    const sectionRecords: Array<{ id: string; title: string; slug: string }> = [];
    for (let i = 0; i < sections.length; i++) {
      const s = sections[i];
      const sect = await tx.section.create({
        data: {
          versionId: version.id,
          title: s.title,
          slug: s.slug ? slugify(s.slug) : slugify(s.title),
          description: s.description || null,
          weight: s.weight,
          sortOrder: i,
        },
      });
      sectionRecords.push({ id: sect.id, title: sect.title, slug: sect.slug });
    }

    let qCount = 0;
    const letters = "abcdefghij".split("");
    for (let i = 0; i < questions.length; i++) {
      const q = questions[i];
      const sect = sectionRecords[q.sectionIndex];
      if (!sect) continue;
      const qTitle = q.title?.trim() || q.prompt.slice(0, 60);
      const qSlug = slugify(`${qTitle}-${i}`);
      const maxPoints = q.maxPoints ?? 1;
      const isMcq = q.questionType === "single_select" || q.questionType === "multi_select";
      const question = await tx.question.create({
        data: {
          sectionId: sect.id,
          slug: qSlug,
          title: qTitle,
          prompt: q.prompt,
          questionType: q.questionType,
          difficulty: q.difficulty || "medium",
          maxPoints,
          weight: 1,
          scoringStrategy: isMcq ? "weighted_options" : "exact",
          sortOrder: i,
        },
      });
      if (isMcq && Array.isArray(q.options)) {
        for (let oi = 0; oi < q.options.length; oi++) {
          const o = q.options[oi];
          await tx.answerOption.create({
            data: {
              questionId: question.id,
              key: letters[oi] ?? `opt${oi}`,
              label: o.label,
              value: o.label,
              points: o.points,
              isCorrect: o.points > 0,
              sortOrder: oi,
            },
          });
        }
      }
      if (q.competencyIds?.length) {
        await tx.questionCompetency.createMany({
          data: q.competencyIds.map((cid) => ({
            questionId: question.id,
            competencyId: cid,
            weight: 1.0,
          })),
        });
      }
      qCount++;
    }

    return { template: tpl, version, sectionCount: sectionRecords.length, questionCount: qCount };
  });

  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.assessment.created",
    targetType: "AssessmentTemplate",
    targetId: created.template.id,
    details: {
      title,
      slug,
      jobRole: role.title,
      sections: created.sectionCount,
      questions: created.questionCount,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });

  return ok({
    id: created.template.id,
    title: created.template.title,
    slug: created.template.slug,
    isActive: false,
    draftNotice: "Created as DRAFT (isActive=false). Review and activate from the admin portal before sending invites.",
    sections: created.sectionCount,
    questions: created.questionCount,
    portalUrl: `/admin/assessments/${created.template.id}/edit`,
  });
}

async function toggleAssessmentActive(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  if (session.role !== "admin") return fail("admin role required");
  const { id, isActive } = args as { id: string; isActive: boolean };
  const row = await prisma.assessmentTemplate.findUnique({ where: { id } });
  if (!row) return fail("Not found");
  await prisma.assessmentTemplate.update({ where: { id }, data: { isActive } });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: isActive ? "mcp.assessment.activated" : "mcp.assessment.deactivated",
    targetType: "AssessmentTemplate",
    targetId: id,
    details: { title: row.title, mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok({ id, title: row.title, isActive });
}

async function updateAssessmentTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await updateAssessmentOp({
    id: args.id as string,
    title: args.title as string | undefined,
    description: args.description as string | undefined,
    jobRoleId: args.jobRoleId as string | undefined,
    timeLimit: args.timeLimit as number | null | undefined,
    passingScore: args.passingScore as number | undefined,
    thresholds: args.thresholds as
      | { strongHire: number; hire: number; consider: number }
      | undefined,
    eggHuntEnabled: args.eggHuntEnabled as boolean | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.assessment.updated",
    targetType: "AssessmentTemplate",
    targetId: result.id,
    details: {
      title: result.title,
      changedFields: Object.keys(args).filter((k) => k !== "id"),
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function updateThresholdsTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const { assessmentId, strongHire, hire, consider } = args as {
    assessmentId: string;
    strongHire: number;
    hire: number;
    consider: number;
  };
  const result = await updateAssessmentOp({
    id: assessmentId,
    thresholds: { strongHire, hire, consider },
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.assessment.thresholds_updated",
    targetType: "AssessmentTemplate",
    targetId: assessmentId,
    details: { thresholds: { strongHire, hire, consider }, mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function addSectionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await addSectionOp({
    assessmentId: args.assessmentId as string,
    title: args.title as string,
    weight: args.weight as number,
    description: args.description as string | undefined,
    introText: args.introText as string | undefined,
    sortOrder: args.sortOrder as number | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.section.added",
    targetType: "Section",
    targetId: result.id,
    details: { assessmentId: args.assessmentId, title: result.title, mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function updateSectionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await updateSectionOp({
    sectionId: args.sectionId as string,
    title: args.title as string | undefined,
    description: args.description as string | undefined,
    introText: args.introText as string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.section.updated",
    targetType: "Section",
    targetId: result.id,
    details: {
      changedFields: Object.keys(args).filter((k) => k !== "sectionId"),
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function removeSectionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await removeSectionOp({ sectionId: args.sectionId as string });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.section.removed",
    targetType: "Section",
    targetId: args.sectionId as string,
    details: { mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function reorderSectionsTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await reorderSectionsOp({
    assessmentId: args.assessmentId as string,
    orderedSectionIds: args.orderedSectionIds as string[],
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.sections.reordered",
    targetType: "AssessmentTemplate",
    targetId: args.assessmentId as string,
    details: {
      newOrder: args.orderedSectionIds,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function setSectionWeightsTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await setSectionWeightsOp({
    assessmentId: args.assessmentId as string,
    weights: args.weights as Array<{ sectionId: string; weight: number }>,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.section.weights_set",
    targetType: "AssessmentTemplate",
    targetId: args.assessmentId as string,
    details: { weights: args.weights, mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function addQuestionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const externalId = args.externalId as string | undefined;
  if (externalId) {
    const hit = await findByExternalId("question", externalId);
    if (hit) return ok({ id: hit.id, idempotent: true });
  }
  const result = await addQuestionOp({
    sectionId: args.sectionId as string,
    prompt: args.prompt as string,
    questionType: args.questionType as string,
    title: args.title as string | undefined,
    difficulty: args.difficulty as string | undefined,
    maxPoints: args.maxPoints as number | undefined,
    options: args.options as Array<{ label: string; points: number }> | undefined,
    competencyIds: args.competencyIds as string[] | undefined,
    explanation: args.explanation as string | undefined,
  });
  if (externalId) {
    await prisma.question.update({ where: { id: result.id }, data: { externalId } });
  }
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.question.added",
    targetType: "Question",
    targetId: result.id,
    details: {
      sectionId: args.sectionId,
      questionType: result.questionType,
      externalId: externalId ?? null,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function updateQuestionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await updateQuestionOp({
    questionId: args.questionId as string,
    prompt: args.prompt as string | undefined,
    title: args.title as string | undefined,
    questionType: args.questionType as string | undefined,
    difficulty: args.difficulty as string | undefined,
    maxPoints: args.maxPoints as number | undefined,
    options: args.options as Array<{ label: string; points: number }> | undefined,
    competencyIds: args.competencyIds as string[] | undefined,
    explanation: args.explanation as string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.question.updated",
    targetType: "Question",
    targetId: result.id,
    details: {
      changedFields: Object.keys(args).filter((k) => k !== "questionId"),
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function reorderQuestionsTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await reorderQuestionsOp({
    sectionId: args.sectionId as string,
    orderedQuestionIds: args.orderedQuestionIds as string[],
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.questions.reordered",
    targetType: "Section",
    targetId: args.sectionId as string,
    details: { newOrder: args.orderedQuestionIds, mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function createBankQuestionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const externalId = args.externalId as string | undefined;
  if (externalId) {
    const hit = await findByExternalId("question", externalId);
    if (hit) return ok({ id: hit.id, idempotent: true });
  }
  const result = await createBankQuestionOp({
    departmentId: args.departmentId as string,
    bankSectionSlug: args.bankSectionSlug as
      | "cultural-fit"
      | "ai-awareness"
      | "department-specific"
      | "general"
      | undefined,
    prompt: args.prompt as string,
    questionType: args.questionType as string,
    title: args.title as string | undefined,
    difficulty: args.difficulty as string | undefined,
    maxPoints: args.maxPoints as number | undefined,
    options: args.options as Array<{ label: string; points: number }> | undefined,
    competencyIds: args.competencyIds as string[] | undefined,
    explanation: args.explanation as string | undefined,
  });
  if (externalId) {
    await prisma.question.update({ where: { id: result.id }, data: { externalId } });
  }
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.bank_question.created",
    targetType: "Question",
    targetId: result.id,
    details: {
      departmentId: args.departmentId,
      bankSectionSlug: args.bankSectionSlug ?? "general",
      externalId: externalId ?? null,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function attachQuestionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await attachQuestionOp({
    questionId: args.questionId as string,
    sectionId: args.sectionId as string,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.question.attached",
    targetType: "Question",
    targetId: result.id,
    details: {
      sourceQuestionId: args.questionId,
      targetSectionId: args.sectionId,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function detachQuestionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await detachQuestionOp({ questionId: args.questionId as string });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.question.detached",
    targetType: "Question",
    targetId: args.questionId as string,
    details: { mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

// ─── P1.1 Read tools (admin role required, audit-logged) ─────────

async function getSessionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const sessionId = args.sessionId as string;
  const result = await getSessionOp(sessionId);
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.session.read",
    targetType: "CandidateSession",
    targetId: sessionId,
    details: { mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function listSessionsTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await listSessionsOp({
    assessmentId: args.assessmentId as string | undefined,
    candidateEmail: args.candidateEmail as string | undefined,
    jobRoleId: args.jobRoleId as string | undefined,
    status: args.status as string | undefined,
    recommendation: args.recommendation as string | undefined,
    dateFrom: args.dateFrom as string | undefined,
    dateTo: args.dateTo as string | undefined,
    limit: args.limit as number | undefined,
    cursor: args.cursor as string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.sessions.list",
    targetType: "CandidateSession",
    details: {
      filters: {
        assessmentId: args.assessmentId,
        jobRoleId: args.jobRoleId,
        status: args.status,
        recommendation: args.recommendation,
      },
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok({ sessions: result.rows, nextCursor: result.nextCursor });
}

async function getSessionResultsTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const sessionId = args.sessionId as string;
  const result = await getSessionResultsOp(sessionId);
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.session.results_read",
    targetType: "CandidateSession",
    targetId: sessionId,
    details: { mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function getAssessmentAnalyticsTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await getAssessmentAnalyticsOp({
    assessmentId: args.assessmentId as string,
    dateFrom: args.dateFrom as string | undefined,
    dateTo: args.dateTo as string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.analytics.assessment_read",
    targetType: "AssessmentTemplate",
    targetId: args.assessmentId as string,
    details: { mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function getQuestionAnalyticsTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await getQuestionAnalyticsOp(args.questionId as string);
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.analytics.question_read",
    targetType: "Question",
    targetId: args.questionId as string,
    details: { mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function exportSessionsTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await exportSessionsOp({
    assessmentId: args.assessmentId as string,
    format: (args.format as "json" | "csv" | undefined) ?? "json",
    dateFrom: args.dateFrom as string | undefined,
    dateTo: args.dateTo as string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.sessions.export",
    targetType: "AssessmentTemplate",
    targetId: args.assessmentId as string,
    details: { format: result.format, mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

// ─── P1.2 Versioning tools ───────────────────────────────────────

async function createNewVersionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await createNewVersionOp({
    assessmentId: args.assessmentId as string,
    copyFrom: args.copyFrom as "latest" | string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.version.created",
    targetType: "AssessmentVersion",
    targetId: result.id,
    details: {
      assessmentId: args.assessmentId,
      copiedFrom: args.copyFrom ?? "latest",
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function publishVersionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await publishVersionOp(args.versionId as string);
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.version.published",
    targetType: "AssessmentVersion",
    targetId: args.versionId as string,
    details: { archivedPreviousId: result.archivedPreviousId, mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function listAssessmentVersionsTool(
  args: ToolArgs,
  session: McpSession
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await listAssessmentVersionsOp(args.assessmentId as string);
  return ok(result);
}

async function getAssessmentVersionTool(
  args: ToolArgs,
  session: McpSession
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await getAssessmentVersionOp(args.versionId as string);
  return ok(result);
}

async function revertToVersionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await revertToVersionOp({
    assessmentId: args.assessmentId as string,
    versionId: args.versionId as string,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.version.reverted",
    targetType: "AssessmentTemplate",
    targetId: args.assessmentId as string,
    details: {
      revertedTo: args.versionId,
      newVersionId: result.newVersionId,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function createCandidateInvite(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  if (session.role !== "admin") return fail("admin role required");
  const { email, name, assessmentId, expiresInDays = 7, sendEmail = false, externalId } = args as {
    email: string;
    name: string;
    assessmentId: string;
    expiresInDays?: number;
    sendEmail?: boolean;
    externalId?: string;
  };

  const { invite, idempotent } = await createInviteOp({
    email,
    name,
    assessmentId,
    expiresInDays,
    externalId,
  });

  // For email, we need the assessment context — fetch it cheaply.
  const template = await prisma.assessmentTemplate.findUnique({
    where: { id: assessmentId },
    include: { jobRole: { include: { department: true } } },
  });

  let emailSent = false;
  if (sendEmail && !idempotent && template) {
    try {
      await sendAssessmentInviteEmail({
        to: invite.candidateEmail,
        candidateName: invite.candidateName,
        assessmentTitle: template.title,
        department: template.jobRole.department.name,
        jobRole: template.jobRole.title,
        inviteLink: invite.inviteLink,
        expiresAt: invite.expiresAt ?? new Date(),
      });
      emailSent = true;
    } catch (e) {
      console.error("[mcp] invite email failed:", e);
    }
  }

  if (!idempotent) {
    await auditLog({
      userId: session.userId,
      userEmail: session.userEmail,
      action: "mcp.invite.created",
      targetType: "CandidateInvite",
      targetId: invite.id,
      details: {
        email,
        name,
        assessment: template?.title ?? invite.assessmentTitle,
        sendEmail,
        emailSent,
        externalId: externalId ?? null,
        mcpTokenId: session.tokenId,
      },
      ipAddress: ip ?? undefined,
    });
  }

  return ok({
    id: invite.id,
    code: invite.code,
    inviteLink: invite.inviteLink,
    expiresAt: invite.expiresAt,
    emailSent,
    idempotent,
    notice: idempotent
      ? "Idempotent: returned existing invite (matched by externalId)."
      : sendEmail
        ? emailSent
          ? "Email sent to candidate."
          : "Invite created, but email failed. You can share the link manually."
        : "Invite created WITHOUT sending email (sendEmail=false). Share the link manually, or re-call with sendEmail=true to dispatch.",
  });
}

async function deleteQuestion(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  if (session.role !== "admin") return fail("admin role required");
  const { id } = args as { id: string };
  const q = await prisma.question.findUnique({ where: { id } });
  if (!q) return fail("Not found");
  await prisma.question.delete({ where: { id } });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.question.deleted",
    targetType: "Question",
    targetId: id,
    details: { prompt: q.prompt.slice(0, 80), mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok({ deleted: true, id });
}

// ─── Round 3: invite management ────────────────────────────────────

async function getInviteTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await getInviteOp(args.inviteId as string);
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.invite.read",
    targetType: "CandidateInvite",
    targetId: args.inviteId as string,
    details: { mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function listInvitesTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await listInvitesOp({
    assessmentId: args.assessmentId as string | undefined,
    candidateEmail: args.candidateEmail as string | undefined,
    status: args.status as string | undefined,
    dateFrom: args.dateFrom as string | undefined,
    dateTo: args.dateTo as string | undefined,
    limit: args.limit as number | undefined,
    cursor: args.cursor as string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.invites.list",
    targetType: "CandidateInvite",
    details: {
      filters: {
        assessmentId: args.assessmentId,
        status: args.status,
        candidateEmail: args.candidateEmail,
      },
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok({ invites: result.rows, nextCursor: result.nextCursor });
}

async function revokeInviteTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await revokeInviteOp(args.inviteId as string);
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.invite.revoked",
    targetType: "CandidateInvite",
    targetId: result.id,
    details: { email: result.candidateEmail, mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function resendInviteTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await resendInviteOp({
    inviteId: args.inviteId as string,
    newExpiryDays: args.newExpiryDays as number | undefined,
    sendEmail: args.sendEmail as boolean | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.invite.resent",
    targetType: "CandidateInvite",
    targetId: result.id,
    details: {
      email: result.candidateEmail,
      sendEmail: Boolean(args.sendEmail),
      emailSent: result.emailSent,
      newExpiryDays: args.newExpiryDays ?? null,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function extendInviteExpiryTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await extendInviteExpiryOp({
    inviteId: args.inviteId as string,
    expiresInDays: args.expiresInDays as number,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.invite.expiry_extended",
    targetType: "CandidateInvite",
    targetId: result.id,
    details: { expiresAt: result.expiresAt, mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function updateCandidateTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await updateCandidateOp({
    inviteId: args.inviteId as string | undefined,
    candidateEmail: args.candidateEmail as string | undefined,
    name: args.name as string | undefined,
    email: args.email as string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.candidate.updated",
    targetType: "CandidateInvite",
    targetId: args.inviteId as string | undefined,
    details: {
      newEmail: result.email,
      newName: result.name,
      invitesUpdated: result.invitesUpdated,
      sessionsUpdated: result.sessionsUpdated,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function bulkCreateInvitesTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await bulkCreateInvitesOp({
    assessmentId: args.assessmentId as string,
    candidates: args.candidates as Array<{
      email: string;
      name: string;
      expiresInDays?: number;
      externalId?: string;
    }>,
    sendEmail: args.sendEmail as boolean | undefined,
  });
  for (const r of result.results) {
    if (r.ok && !r.idempotent) {
      await auditLog({
        userId: session.userId,
        userEmail: session.userEmail,
        action: "mcp.invite.created",
        targetType: "CandidateInvite",
        targetId: r.inviteId,
        details: {
          email: r.email,
          assessmentId: args.assessmentId,
          bulk: true,
          emailSent: r.emailSent ?? false,
          externalId: r.externalId ?? null,
          mcpTokenId: session.tokenId,
        },
        ipAddress: ip ?? undefined,
      });
    }
  }
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.invites.bulk_created",
    targetType: "AssessmentTemplate",
    targetId: args.assessmentId as string,
    details: {
      successCount: result.successCount,
      failureCount: result.failureCount,
      sendEmail: Boolean(args.sendEmail),
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

// ─── Round 3: duplicate / clone ───────────────────────────────────

async function duplicateAssessmentTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await duplicateAssessmentOp({
    assessmentId: args.assessmentId as string,
    newTitle: args.newTitle as string,
    newJobRoleId: args.newJobRoleId as string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.assessment.duplicated",
    targetType: "AssessmentTemplate",
    targetId: result.id,
    details: {
      sourceAssessmentId: result.sourceAssessmentId,
      sectionCount: result.sectionCount,
      questionCount: result.questionCount,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok({
    ...result,
    portalUrl: `/admin/assessments/${result.id}/edit`,
    draftNotice: "Created as DRAFT (isActive=false). Review before activating.",
  });
}

async function duplicateQuestionTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await duplicateQuestionOp({
    questionId: args.questionId as string,
    newSectionId: args.newSectionId as string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.question.duplicated",
    targetType: "Question",
    targetId: result.id,
    details: {
      sourceQuestionId: result.sourceQuestionId,
      targetSectionId: result.sectionId,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

// ─── Round 3: admin CRUD ──────────────────────────────────────────

async function createCompetencyTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const { record, idempotent } = await createCompetencyOp({
    name: args.name as string,
    description: args.description as string | undefined,
    category: args.category as string | undefined,
    externalId: args.externalId as string | undefined,
  });
  if (!idempotent) {
    await auditLog({
      userId: session.userId,
      userEmail: session.userEmail,
      action: "mcp.competency.created",
      targetType: "Competency",
      targetId: record.id,
      details: { name: record.name, externalId: record.externalId, mcpTokenId: session.tokenId },
      ipAddress: ip ?? undefined,
    });
  }
  return ok({ ...record, idempotent });
}

async function updateCompetencyTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await updateCompetencyOp({
    id: args.id as string,
    name: args.name as string | undefined,
    description: args.description as string | undefined,
    category: args.category as string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.competency.updated",
    targetType: "Competency",
    targetId: result.id,
    details: {
      changedFields: Object.keys(args).filter((k) => k !== "id"),
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function archiveCompetencyTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await archiveCompetencyOp(args.id as string);
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.competency.archived",
    targetType: "Competency",
    targetId: result.id,
    details: { archivedAt: result.archivedAt, mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function createDepartmentTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const { record, idempotent } = await createDepartmentOp({
    name: args.name as string,
    description: args.description as string | undefined,
    externalId: args.externalId as string | undefined,
  });
  if (!idempotent) {
    await auditLog({
      userId: session.userId,
      userEmail: session.userEmail,
      action: "mcp.department.created",
      targetType: "Department",
      targetId: record.id,
      details: { name: record.name, externalId: record.externalId, mcpTokenId: session.tokenId },
      ipAddress: ip ?? undefined,
    });
  }
  return ok({ ...record, idempotent });
}

async function updateDepartmentTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await updateDepartmentOp({
    id: args.id as string,
    name: args.name as string | undefined,
    description: args.description as string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.department.updated",
    targetType: "Department",
    targetId: result.id,
    details: {
      changedFields: Object.keys(args).filter((k) => k !== "id"),
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function archiveDepartmentTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await archiveDepartmentOp(args.id as string);
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.department.archived",
    targetType: "Department",
    targetId: result.id,
    details: { archivedAt: result.archivedAt, mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function updateJobRoleTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await updateJobRoleOp({
    id: args.id as string,
    title: args.title as string | undefined,
    description: args.description as string | undefined,
    departmentId: args.departmentId as string | undefined,
    jdSummary: args.jdSummary as string | undefined,
    jdResponsibilities: args.jdResponsibilities as string | undefined,
    jdRequirements: args.jdRequirements as string | undefined,
    jdNiceToHaves: args.jdNiceToHaves as string | undefined,
    jdYearsExperience: args.jdYearsExperience as string | undefined,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.job_role.updated",
    targetType: "JobRole",
    targetId: result.id,
    details: {
      changedFields: Object.keys(args).filter((k) => k !== "id"),
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function archiveJobRoleTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await archiveJobRoleOp(args.id as string);
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.job_role.archived",
    targetType: "JobRole",
    targetId: result.id,
    details: { mcpTokenId: session.tokenId },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

// ─── Round 3: automation hooks ────────────────────────────────────

async function lookupByExternalIdTool(
  args: ToolArgs,
  session: McpSession
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await lookupByExternalId({
    type: args.type as ExternalIdType,
    externalId: args.externalId as string,
  });
  return ok(result);
}

async function bulkTagQuestionsTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await bulkTagQuestionsOp({
    questionIds: args.questionIds as string[],
    competencyIds: args.competencyIds as string[],
    mode: args.mode as "replace" | "add" | "remove",
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.questions.bulk_tagged",
    targetType: "Question",
    details: {
      questionCount: result.questionsUpdated,
      mode: result.mode,
      tagsAdded: result.tagsAdded,
      tagsRemoved: result.tagsRemoved,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function bulkDeleteQuestionsTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await bulkDeleteQuestionsOp(args.questionIds as string[]);
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.questions.bulk_deleted",
    targetType: "Question",
    details: {
      deletedCount: result.deletedCount,
      deletedIds: result.deletedIds,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

async function bulkToggleAssessmentActiveTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null
): Promise<ToolResult> {
  requireAdmin(session);
  const result = await bulkToggleAssessmentActiveOp({
    assessmentIds: args.assessmentIds as string[],
    isActive: args.isActive as boolean,
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: args.isActive
      ? "mcp.assessments.bulk_activated"
      : "mcp.assessments.bulk_deactivated",
    targetType: "AssessmentTemplate",
    details: {
      changedCount: result.changedCount,
      changedIds: result.changedIds,
      alreadyInStateCount: result.alreadyInStateCount,
      notFound: result.notFound,
      mcpTokenId: session.tokenId,
    },
    ipAddress: ip ?? undefined,
  });
  return ok(result);
}

// ─── Recruitment pipeline (Phase 1.A) ────────────────────────

async function recruitmentSearchCandidatesTool(args: ToolArgs, session: McpSession): Promise<ToolResult> {
  const query = typeof args.query === "string" ? args.query.trim() : "";
  const office = typeof args.office === "string" ? args.office : null;
  const source = typeof args.source === "string" ? args.source : null;
  const limit = Math.max(1, Math.min(100, Number(args.limit ?? 25)));

  let where: Record<string, unknown> = { archivedAt: null };
  if (query) {
    where.OR = [
      { firstName: { contains: query } },
      { lastName: { contains: query } },
      { email: { contains: query } },
      { agencyName: { contains: query } },
    ];
  }
  if (office) where.office = office;
  if (source) where.source = source;
  where = applyOfficeScope({ office: session.office }, where);

  const rows = await prisma.candidate.findMany({
    where,
    take: limit,
    orderBy: { createdAt: "desc" },
    include: { _count: { select: { applications: true } } },
  });

  return ok(
    rows.map((c) => ({
      id: c.id,
      firstName: c.firstName,
      lastName: c.lastName,
      email: c.email,
      office: c.office,
      source: c.source,
      agencyName: c.agencyName,
      noticePeriod: c.noticePeriod,
      nationality: c.nationality,
      cvDriveUrl: c.cvDriveUrl,
      applicationsCount: c._count.applications,
      createdAt: c.createdAt,
    })),
  );
}

async function recruitmentGetCandidateTool(args: ToolArgs, session: McpSession): Promise<ToolResult> {
  const id = String(args.id ?? "");
  if (!id) throw new McpValidationError("id is required");

  const candidate = await prisma.candidate.findUnique({
    where: { id },
    include: {
      applications: {
        orderBy: { appliedAt: "desc" },
        include: { jobRole: { include: { department: true } } },
      },
      invites: { orderBy: { createdAt: "desc" }, take: 10 },
    },
  });
  if (!candidate) return fail("Candidate not found");

  // Office scope check
  if (session.office && candidate.office && candidate.office !== session.office) {
    throw new McpPermissionError("permission_denied: candidate belongs to a different office");
  }

  return ok(candidate);
}

async function recruitmentCreateCandidateTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  requireAdmin(session);

  const firstName = String(args.firstName ?? "").trim();
  const lastName = String(args.lastName ?? "").trim();
  const email = String(args.email ?? "").trim().toLowerCase();
  if (!firstName || !lastName || !email) {
    throw new McpValidationError("firstName, lastName, email are required");
  }

  const employmentEnum = ["employed", "not_working", "freelancing"] as const;
  const locationEnum = ["in_uae", "outside_uae"] as const;
  if (
    args.currentlyEmployed !== undefined &&
    !employmentEnum.includes(args.currentlyEmployed as (typeof employmentEnum)[number])
  ) {
    throw new McpValidationError(
      `currentlyEmployed must be one of: ${employmentEnum.join(", ")}`,
    );
  }
  if (
    args.locationStatus !== undefined &&
    !locationEnum.includes(args.locationStatus as (typeof locationEnum)[number])
  ) {
    throw new McpValidationError(
      `locationStatus must be one of: ${locationEnum.join(", ")}`,
    );
  }

  const candidate = await prisma.candidate.create({
    data: {
      firstName,
      lastName,
      email,
      phoneNumber: typeof args.phoneNumber === "string" ? args.phoneNumber : null,
      nationality: typeof args.nationality === "string" ? args.nationality : null,
      noticePeriod: typeof args.noticePeriod === "string" ? args.noticePeriod : null,
      office: typeof args.office === "string" ? args.office : null,
      source: typeof args.source === "string" ? args.source : null,
      agencyName: typeof args.agencyName === "string" ? args.agencyName : null,
      linkedinUrl: typeof args.linkedinUrl === "string" ? args.linkedinUrl : null,
      cvDriveUrl: typeof args.cvDriveUrl === "string" ? args.cvDriveUrl : null,
      externalId: typeof args.externalId === "string" ? args.externalId : null,
      currentlyEmployed:
        typeof args.currentlyEmployed === "string" ? args.currentlyEmployed : null,
      visaStatus: typeof args.visaStatus === "string" ? args.visaStatus : null,
      aiToolsProficiency:
        typeof args.aiToolsProficiency === "string" ? args.aiToolsProficiency : null,
      hasDriversLicense:
        typeof args.hasDriversLicense === "boolean" ? args.hasDriversLicense : null,
      locationStatus: typeof args.locationStatus === "string" ? args.locationStatus : null,
    },
  });

  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.recruitment.candidate.create",
    targetType: "Candidate",
    targetId: candidate.id,
    details: { email, firstName, lastName, office: candidate.office },
    ipAddress: ip ?? undefined,
  });

  return ok(candidate);
}

async function recruitmentUpdateCandidateTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  requireAdmin(session);

  const id = String(args.id ?? "");
  if (!id) throw new McpValidationError("id is required");

  const existing = await prisma.candidate.findUnique({ where: { id } });
  if (!existing) return fail("Candidate not found");

  const data: Record<string, unknown> = {};
  for (const key of [
    "firstName",
    "lastName",
    "phoneNumber",
    "nationality",
    "noticePeriod",
    "office",
    "source",
    "agencyName",
    "linkedinUrl",
    "cvDriveUrl",
    "cvDriveFolderUrl",
    "visaStatus",
    "aiToolsProficiency",
  ]) {
    if (typeof args[key] === "string") data[key] = args[key];
  }
  if (args.currentlyEmployed !== undefined) {
    const employmentEnum = ["employed", "not_working", "freelancing"];
    if (typeof args.currentlyEmployed !== "string" || !employmentEnum.includes(args.currentlyEmployed)) {
      throw new McpValidationError(
        `currentlyEmployed must be one of: ${employmentEnum.join(", ")}`,
      );
    }
    data.currentlyEmployed = args.currentlyEmployed;
  }
  if (args.locationStatus !== undefined) {
    const locationEnum = ["in_uae", "outside_uae"];
    if (typeof args.locationStatus !== "string" || !locationEnum.includes(args.locationStatus)) {
      throw new McpValidationError(
        `locationStatus must be one of: ${locationEnum.join(", ")}`,
      );
    }
    data.locationStatus = args.locationStatus;
  }
  if (args.hasDriversLicense !== undefined) {
    if (args.hasDriversLicense === null || typeof args.hasDriversLicense === "boolean") {
      data.hasDriversLicense = args.hasDriversLicense;
    } else {
      throw new McpValidationError("hasDriversLicense must be boolean or null");
    }
  }
  if (args.archived === true) data.archivedAt = new Date();
  if (args.archived === false) data.archivedAt = null;

  const candidate = await prisma.candidate.update({ where: { id }, data });

  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.recruitment.candidate.update",
    targetType: "Candidate",
    targetId: id,
    details: { fields: Object.keys(data) },
    ipAddress: ip ?? undefined,
  });

  return ok(candidate);
}

async function recruitmentCreateApplicationTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  requireAdmin(session);

  const candidateId = String(args.candidateId ?? "");
  const jobRoleId = String(args.jobRoleId ?? "");
  if (!candidateId || !jobRoleId) {
    throw new McpValidationError("candidateId and jobRoleId are required");
  }

  const candidate = await prisma.candidate.findUnique({ where: { id: candidateId } });
  if (!candidate) return fail("Candidate not found");
  const role = await prisma.jobRole.findUnique({ where: { id: jobRoleId } });
  if (!role) return fail("JobRole not found");

  let cvReceivedAt: Date | null = null;
  if (typeof args.cvReceivedAt === "string" && args.cvReceivedAt.trim()) {
    const d = new Date(args.cvReceivedAt);
    if (Number.isNaN(d.getTime())) {
      throw new McpValidationError("cvReceivedAt must be a valid ISO date or datetime");
    }
    cvReceivedAt = d;
  }

  const application = await prisma.application.create({
    data: {
      candidateId,
      jobRoleId,
      office: typeof args.office === "string" ? args.office : candidate.office,
      source: typeof args.source === "string" ? args.source : candidate.source,
      agencyName: typeof args.agencyName === "string" ? args.agencyName : candidate.agencyName,
      cvReceivedAt: cvReceivedAt ?? undefined,
      currentStage: "intake_received",
      status: "active",
      externalId: typeof args.externalId === "string" ? args.externalId : null,
    },
  });
  await prisma.applicationStage.create({
    data: {
      applicationId: application.id,
      stage: "intake_received",
      actorId: session.userId,
      notes: "Created via MCP recruitment_create_application",
    },
  });

  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.recruitment.application.create",
    targetType: "Application",
    targetId: application.id,
    details: { candidateId, jobRoleId },
    ipAddress: ip ?? undefined,
  });

  return ok(application);
}

async function recruitmentListApplicationsTool(args: ToolArgs, session: McpSession): Promise<ToolResult> {
  const limit = Math.max(1, Math.min(100, Number(args.limit ?? 25)));

  let where: Record<string, unknown> = {};
  if (typeof args.currentStage === "string") where.currentStage = args.currentStage;
  if (typeof args.status === "string") where.status = args.status;
  if (typeof args.jobRoleId === "string") where.jobRoleId = args.jobRoleId;
  if (typeof args.office === "string") where.office = args.office;
  if (typeof args.source === "string") where.source = args.source;

  where = applyRecruitmentScope(
    {
      id: session.userId,
      role: session.role,
      office: session.office,
      scopedDepartments: session.scopedDepartments,
    },
    where,
  );

  // Cursor pagination by appliedAt:id
  if (typeof args.cursor === "string" && args.cursor.length > 0) {
    try {
      const decoded = Buffer.from(args.cursor, "base64").toString("utf8");
      const [iso, id] = decoded.split("|");
      if (iso && id) {
        where.OR = [
          { appliedAt: { lt: new Date(iso) } },
          { appliedAt: new Date(iso), id: { lt: id } },
        ];
      }
    } catch {
      throw new McpValidationError("invalid cursor");
    }
  }

  const rows = await prisma.application.findMany({
    where,
    take: limit + 1,
    orderBy: [{ appliedAt: "desc" }, { id: "desc" }],
    include: {
      candidate: true,
      jobRole: { include: { department: true } },
    },
  });

  const hasMore = rows.length > limit;
  const items = hasMore ? rows.slice(0, limit) : rows;
  const last = items[items.length - 1];
  const nextCursor =
    hasMore && last
      ? Buffer.from(`${last.appliedAt.toISOString()}|${last.id}`).toString("base64")
      : null;

  return ok({
    items: items.map((a) => ({
      id: a.id,
      candidate: {
        id: a.candidate.id,
        firstName: a.candidate.firstName,
        lastName: a.candidate.lastName,
        email: a.candidate.email,
      },
      jobRole: {
        id: a.jobRole.id,
        title: a.jobRole.title,
        department: a.jobRole.department.name,
      },
      currentStage: a.currentStage,
      status: a.status,
      office: a.office,
      source: a.source,
      agencyName: a.agencyName,
      preScore: a.preScore,
      preScoreTier: a.preScoreTier,
      postScore: a.postScore,
      postScoreTier: a.postScoreTier,
      appliedAt: a.appliedAt,
    })),
    nextCursor,
  });
}

// ─── Recruitment scoring rubrics ────────────────────────────────

const RUBRIC_WEIGHT_TOLERANCE = 0.001;

type RubricCriterion = {
  key: string;
  label: string;
  weight: number;
  scoringPrompt: string;
  commentaryGuidance?: string;
  redFlagSignals?: string[];
};

function slugifyKey(s: string): string {
  return s
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, "_")
    .replace(/^_+|_+$/g, "")
    .replace(/_{2,}/g, "_")
    .slice(0, 60);
}

function uniqueRubricKey(base: string, existing: string[]): string {
  const safe = base || "criterion";
  if (!existing.includes(safe)) return safe;
  let i = 2;
  while (existing.includes(`${safe}_${i}`)) i++;
  return `${safe}_${i}`;
}

function normalizeCriteriaInput(raw: unknown): RubricCriterion[] {
  if (!Array.isArray(raw)) {
    throw new McpValidationError("criteria must be an array");
  }
  const out: RubricCriterion[] = [];
  const usedKeys: string[] = [];
  for (let i = 0; i < raw.length; i++) {
    const c = raw[i];
    if (typeof c !== "object" || c === null) {
      throw new McpValidationError(`criterion ${i}: must be an object`);
    }
    const obj = c as Record<string, unknown>;
    const label = typeof obj.label === "string" ? obj.label.trim() : "";
    if (!label) throw new McpValidationError(`criterion ${i}: label is required`);
    const weight = Number(obj.weight);
    if (!Number.isFinite(weight) || weight <= 0 || weight > 1) {
      throw new McpValidationError(`criterion ${i}: weight must be a number in (0, 1]`);
    }
    const scoringPrompt =
      typeof obj.scoringPrompt === "string" ? obj.scoringPrompt.trim() : "";
    if (!scoringPrompt) {
      throw new McpValidationError(`criterion ${i}: scoringPrompt is required`);
    }
    const providedKey = typeof obj.key === "string" ? obj.key.trim() : "";
    const key = providedKey
      ? slugifyKey(providedKey) || uniqueRubricKey(slugifyKey(label), usedKeys)
      : uniqueRubricKey(slugifyKey(label), usedKeys);
    if (usedKeys.includes(key)) {
      throw new McpValidationError(`criterion ${i}: duplicate key "${key}"`);
    }
    usedKeys.push(key);

    const criterion: RubricCriterion = { key, label, weight, scoringPrompt };
    if (typeof obj.commentaryGuidance === "string" && obj.commentaryGuidance.trim()) {
      criterion.commentaryGuidance = obj.commentaryGuidance.trim();
    }
    if (Array.isArray(obj.redFlagSignals)) {
      const flags = obj.redFlagSignals
        .filter((x): x is string => typeof x === "string")
        .map((s) => s.trim())
        .filter(Boolean);
      if (flags.length) criterion.redFlagSignals = flags;
    }
    out.push(criterion);
  }
  if (out.length === 0) throw new McpValidationError("criteria must be non-empty");

  const total = out.reduce((s, c) => s + c.weight, 0);
  if (Math.abs(total - 1) > RUBRIC_WEIGHT_TOLERANCE) {
    throw new McpValidationError(
      `criteria weights must sum to 1.0 (got ${total.toFixed(4)})`,
    );
  }
  return out;
}

function assertThresholdsValid(strong: number, match: number, consider: number) {
  for (const [name, v] of [
    ["thresholdStrong", strong],
    ["thresholdMatch", match],
    ["thresholdConsider", consider],
  ] as const) {
    if (!Number.isFinite(v) || v <= 0 || v > 1) {
      throw new McpValidationError(`${name} must be a number in (0, 1]`);
    }
  }
  if (!(strong > match && match > consider)) {
    throw new McpValidationError(
      "thresholds must descend: thresholdStrong > thresholdMatch > thresholdConsider",
    );
  }
}

function rubricToWire(r: {
  id: string;
  name: string;
  kind: string;
  jobRoleId: string | null;
  version: number;
  isActive: boolean;
  criteria: string;
  thresholdStrong: number;
  thresholdMatch: number;
  thresholdConsider: number;
  createdAt: Date;
  updatedAt: Date;
}) {
  let parsedCriteria: RubricCriterion[] = [];
  try {
    const decoded = JSON.parse(r.criteria);
    if (Array.isArray(decoded)) parsedCriteria = decoded as RubricCriterion[];
  } catch {
    parsedCriteria = [];
  }
  return {
    id: r.id,
    name: r.name,
    kind: r.kind,
    jobRoleId: r.jobRoleId,
    version: r.version,
    isActive: r.isActive,
    thresholdStrong: r.thresholdStrong,
    thresholdMatch: r.thresholdMatch,
    thresholdConsider: r.thresholdConsider,
    criteria: parsedCriteria,
    createdAt: r.createdAt,
    updatedAt: r.updatedAt,
  };
}

async function recruitmentListRubricsTool(args: ToolArgs): Promise<ToolResult> {
  const where: Record<string, unknown> = {};
  if (typeof args.kind === "string") {
    if (args.kind !== "pre_interview" && args.kind !== "post_interview") {
      throw new McpValidationError("kind must be 'pre_interview' or 'post_interview'");
    }
    where.kind = args.kind;
  }
  if (typeof args.jobRoleId === "string") {
    where.jobRoleId = args.jobRoleId === "global" ? null : args.jobRoleId;
  }
  if (typeof args.isActive === "boolean") where.isActive = args.isActive;

  const rows = await prisma.recruitmentRubric.findMany({
    where,
    orderBy: [{ kind: "asc" }, { isActive: "desc" }, { updatedAt: "desc" }],
  });
  return ok({ items: rows.map(rubricToWire) });
}

async function recruitmentGetRubricTool(args: ToolArgs): Promise<ToolResult> {
  const rubricId = typeof args.rubricId === "string" ? args.rubricId : "";
  if (!rubricId) throw new McpValidationError("rubricId is required");
  const r = await prisma.recruitmentRubric.findUnique({ where: { id: rubricId } });
  if (!r) return fail("Rubric not found");
  return ok({ rubric: rubricToWire(r) });
}

async function recruitmentCreateRubricTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  const name = typeof args.name === "string" ? args.name.trim() : "";
  if (!name) throw new McpValidationError("name is required");
  const kind = args.kind;
  if (kind !== "pre_interview" && kind !== "post_interview") {
    throw new McpValidationError("kind must be 'pre_interview' or 'post_interview'");
  }
  const jobRoleId =
    typeof args.jobRoleId === "string" && args.jobRoleId.length > 0 ? args.jobRoleId : null;
  if (jobRoleId) {
    const exists = await prisma.jobRole.findUnique({ where: { id: jobRoleId } });
    if (!exists) return fail("JobRole not found");
  }
  const isActive = typeof args.isActive === "boolean" ? args.isActive : true;
  const thresholdStrong = Number(args.thresholdStrong ?? 0.85);
  const thresholdMatch = Number(args.thresholdMatch ?? 0.7);
  const thresholdConsider = Number(args.thresholdConsider ?? 0.55);
  assertThresholdsValid(thresholdStrong, thresholdMatch, thresholdConsider);
  const criteria = normalizeCriteriaInput(args.criteria);

  const created = await prisma.recruitmentRubric.create({
    data: {
      name,
      kind,
      jobRoleId,
      version: 1,
      isActive,
      criteria: JSON.stringify(criteria),
      thresholdStrong,
      thresholdMatch,
      thresholdConsider,
    },
  });

  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.recruitment.rubric.create",
    targetType: "RecruitmentRubric",
    targetId: created.id,
    details: { name: created.name, kind: created.kind, jobRoleId: created.jobRoleId },
    ipAddress: ip ?? undefined,
  });

  return ok({ rubric: rubricToWire(created) });
}

async function recruitmentUpdateRubricTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  const rubricId = typeof args.rubricId === "string" ? args.rubricId : "";
  if (!rubricId) throw new McpValidationError("rubricId is required");
  const existing = await prisma.recruitmentRubric.findUnique({ where: { id: rubricId } });
  if (!existing) return fail("Rubric not found");

  const next: Record<string, unknown> = {};
  if (typeof args.name === "string" && args.name.trim()) next.name = args.name.trim();
  if (args.kind !== undefined) {
    if (args.kind !== "pre_interview" && args.kind !== "post_interview") {
      throw new McpValidationError("kind must be 'pre_interview' or 'post_interview'");
    }
    next.kind = args.kind;
  }
  if (args.jobRoleId !== undefined) {
    if (args.jobRoleId === null || args.jobRoleId === "") {
      next.jobRoleId = null;
    } else if (typeof args.jobRoleId === "string") {
      const exists = await prisma.jobRole.findUnique({ where: { id: args.jobRoleId } });
      if (!exists) return fail("JobRole not found");
      next.jobRoleId = args.jobRoleId;
    } else {
      throw new McpValidationError("jobRoleId must be string or null");
    }
  }
  if (typeof args.isActive === "boolean") next.isActive = args.isActive;

  // Thresholds: if any one is provided, validate against the merged set.
  const tStrong =
    args.thresholdStrong !== undefined ? Number(args.thresholdStrong) : existing.thresholdStrong;
  const tMatch =
    args.thresholdMatch !== undefined ? Number(args.thresholdMatch) : existing.thresholdMatch;
  const tConsider =
    args.thresholdConsider !== undefined
      ? Number(args.thresholdConsider)
      : existing.thresholdConsider;
  if (
    args.thresholdStrong !== undefined ||
    args.thresholdMatch !== undefined ||
    args.thresholdConsider !== undefined
  ) {
    assertThresholdsValid(tStrong, tMatch, tConsider);
    next.thresholdStrong = tStrong;
    next.thresholdMatch = tMatch;
    next.thresholdConsider = tConsider;
  }

  if (args.criteria !== undefined) {
    const criteria = normalizeCriteriaInput(args.criteria);
    next.criteria = JSON.stringify(criteria);
    next.version = existing.version + 1;
  }

  const updated = await prisma.recruitmentRubric.update({
    where: { id: rubricId },
    data: next,
  });

  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.recruitment.rubric.update",
    targetType: "RecruitmentRubric",
    targetId: updated.id,
    details: { keys: Object.keys(next) },
    ipAddress: ip ?? undefined,
  });

  return ok({ rubric: rubricToWire(updated) });
}

async function recruitmentDeleteRubricTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  const rubricId = typeof args.rubricId === "string" ? args.rubricId : "";
  if (!rubricId) throw new McpValidationError("rubricId is required");
  const existing = await prisma.recruitmentRubric.findUnique({ where: { id: rubricId } });
  if (!existing) return fail("Rubric not found");

  const referencedCount = await prisma.applicationScore.count({ where: { rubricId } });
  let mode: "soft_archive" | "hard_delete";
  if (referencedCount > 0) {
    await prisma.recruitmentRubric.update({
      where: { id: rubricId },
      data: { isActive: false },
    });
    mode = "soft_archive";
  } else {
    await prisma.recruitmentRubric.delete({ where: { id: rubricId } });
    mode = "hard_delete";
  }

  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.recruitment.rubric.delete",
    targetType: "RecruitmentRubric",
    targetId: rubricId,
    details: { mode, referencedCount },
    ipAddress: ip ?? undefined,
  });

  return ok({ mode, referencedScoreCount: referencedCount });
}

async function recruitmentCloneRubricTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  const rubricId = typeof args.rubricId === "string" ? args.rubricId : "";
  if (!rubricId) throw new McpValidationError("rubricId is required");
  const newName = typeof args.name === "string" ? args.name.trim() : "";
  if (!newName) throw new McpValidationError("name is required");
  const source = await prisma.recruitmentRubric.findUnique({ where: { id: rubricId } });
  if (!source) return fail("Source rubric not found");

  let nextJobRoleId: string | null = source.jobRoleId;
  if (args.jobRoleId !== undefined) {
    if (args.jobRoleId === null || args.jobRoleId === "") {
      nextJobRoleId = null;
    } else if (typeof args.jobRoleId === "string") {
      const exists = await prisma.jobRole.findUnique({ where: { id: args.jobRoleId } });
      if (!exists) return fail("JobRole not found");
      nextJobRoleId = args.jobRoleId;
    } else {
      throw new McpValidationError("jobRoleId must be string or null");
    }
  }
  let nextKind = source.kind;
  if (args.kind !== undefined) {
    if (args.kind !== "pre_interview" && args.kind !== "post_interview") {
      throw new McpValidationError("kind must be 'pre_interview' or 'post_interview'");
    }
    nextKind = args.kind;
  }

  const created = await prisma.recruitmentRubric.create({
    data: {
      name: newName,
      kind: nextKind,
      jobRoleId: nextJobRoleId,
      version: 1,
      isActive: true,
      criteria: source.criteria,
      thresholdStrong: source.thresholdStrong,
      thresholdMatch: source.thresholdMatch,
      thresholdConsider: source.thresholdConsider,
    },
  });

  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.recruitment.rubric.clone",
    targetType: "RecruitmentRubric",
    targetId: created.id,
    details: { sourceId: source.id },
    ipAddress: ip ?? undefined,
  });

  return ok({ rubric: rubricToWire(created) });
}

// ─── Team management (Employees + Line Managers) ────────────────

function trimOrNull(v: unknown): string | null {
  if (typeof v !== "string") return null;
  const t = v.trim();
  return t.length > 0 ? t : null;
}

async function teamListEmployeesTool(args: ToolArgs): Promise<ToolResult> {
  const where: Record<string, unknown> = {};
  if (typeof args.isActive === "boolean") where.isActive = args.isActive;
  if (typeof args.department === "string") where.department = args.department;
  const rows = await prisma.employee.findMany({
    where,
    include: { lineManager: { select: { id: true, name: true } } },
    orderBy: [{ isActive: "desc" }, { firstName: "asc" }],
  });
  return ok({ items: rows });
}

async function teamCreateEmployeeTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  const firstName = typeof args.firstName === "string" ? args.firstName.trim() : "";
  if (!firstName) throw new McpValidationError("firstName is required");
  const lineManagerId =
    typeof args.lineManagerId === "string" && args.lineManagerId.length > 0
      ? args.lineManagerId
      : null;
  if (lineManagerId) {
    const exists = await prisma.lineManager.findUnique({ where: { id: lineManagerId } });
    if (!exists) return fail("LineManager not found");
  }
  const employee = await prisma.employee.create({
    data: {
      firstName,
      fullName: trimOrNull(args.fullName),
      email: trimOrNull(args.email)?.toLowerCase() ?? null,
      slackUserId: trimOrNull(args.slackUserId),
      slackHandle: trimOrNull(args.slackHandle)?.replace(/^@/, "") ?? null,
      department: trimOrNull(args.department),
      isActive: typeof args.isActive === "boolean" ? args.isActive : true,
      lineManagerId,
    },
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.team.employee.create",
    targetType: "Employee",
    targetId: employee.id,
    details: { firstName, lineManagerId },
    ipAddress: ip ?? undefined,
  });
  return ok(employee);
}

async function teamUpdateEmployeeTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  const employeeId = typeof args.employeeId === "string" ? args.employeeId : "";
  if (!employeeId) throw new McpValidationError("employeeId is required");
  const existing = await prisma.employee.findUnique({ where: { id: employeeId } });
  if (!existing) return fail("Employee not found");

  const data: Record<string, unknown> = {};
  if (args.firstName !== undefined) {
    if (typeof args.firstName !== "string" || !args.firstName.trim()) {
      throw new McpValidationError("firstName cannot be empty");
    }
    data.firstName = args.firstName.trim();
  }
  if (args.fullName !== undefined) data.fullName = trimOrNull(args.fullName);
  if (args.email !== undefined) data.email = trimOrNull(args.email)?.toLowerCase() ?? null;
  if (args.slackUserId !== undefined) data.slackUserId = trimOrNull(args.slackUserId);
  if (args.slackHandle !== undefined) {
    data.slackHandle = trimOrNull(args.slackHandle)?.replace(/^@/, "") ?? null;
  }
  if (args.department !== undefined) data.department = trimOrNull(args.department);
  if (typeof args.isActive === "boolean") data.isActive = args.isActive;
  if (args.lineManagerId !== undefined) {
    if (args.lineManagerId === null || args.lineManagerId === "") {
      data.lineManagerId = null;
    } else if (typeof args.lineManagerId === "string") {
      const exists = await prisma.lineManager.findUnique({ where: { id: args.lineManagerId } });
      if (!exists) return fail("LineManager not found");
      data.lineManagerId = args.lineManagerId;
    } else {
      throw new McpValidationError("lineManagerId must be string or null");
    }
  }

  const employee = await prisma.employee.update({ where: { id: employeeId }, data });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.team.employee.update",
    targetType: "Employee",
    targetId: employeeId,
    details: { fields: Object.keys(data) },
    ipAddress: ip ?? undefined,
  });
  return ok(employee);
}

async function teamArchiveEmployeeTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  const employeeId = typeof args.employeeId === "string" ? args.employeeId : "";
  if (!employeeId) throw new McpValidationError("employeeId is required");
  const existing = await prisma.employee.findUnique({ where: { id: employeeId } });
  if (!existing) return fail("Employee not found");
  const employee = await prisma.employee.update({
    where: { id: employeeId },
    data: { isActive: false },
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.team.employee.archive",
    targetType: "Employee",
    targetId: employeeId,
    ipAddress: ip ?? undefined,
  });
  return ok(employee);
}

async function teamListManagersTool(args: ToolArgs): Promise<ToolResult> {
  const where: Record<string, unknown> = {};
  if (typeof args.isActive === "boolean") where.isActive = args.isActive;
  const rows = await prisma.lineManager.findMany({
    where,
    include: { _count: { select: { directReports: true } } },
    orderBy: [{ isActive: "desc" }, { name: "asc" }],
  });
  return ok({
    items: rows.map((r) => ({ ...r, directReports: r._count.directReports })),
  });
}

async function teamCreateManagerTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  const name = typeof args.name === "string" ? args.name.trim() : "";
  if (!name) throw new McpValidationError("name is required");
  const manager = await prisma.lineManager.create({
    data: {
      name,
      email: trimOrNull(args.email)?.toLowerCase() ?? null,
      slackUserId: trimOrNull(args.slackUserId),
      slackHandle: trimOrNull(args.slackHandle)?.replace(/^@/, "") ?? null,
      isActive: typeof args.isActive === "boolean" ? args.isActive : true,
    },
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.team.manager.create",
    targetType: "LineManager",
    targetId: manager.id,
    details: { name },
    ipAddress: ip ?? undefined,
  });
  return ok(manager);
}

async function teamUpdateManagerTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  const managerId = typeof args.managerId === "string" ? args.managerId : "";
  if (!managerId) throw new McpValidationError("managerId is required");
  const existing = await prisma.lineManager.findUnique({ where: { id: managerId } });
  if (!existing) return fail("LineManager not found");

  const data: Record<string, unknown> = {};
  if (args.name !== undefined) {
    if (typeof args.name !== "string" || !args.name.trim()) {
      throw new McpValidationError("name cannot be empty");
    }
    data.name = args.name.trim();
  }
  if (args.email !== undefined) data.email = trimOrNull(args.email)?.toLowerCase() ?? null;
  if (args.slackUserId !== undefined) data.slackUserId = trimOrNull(args.slackUserId);
  if (args.slackHandle !== undefined) {
    data.slackHandle = trimOrNull(args.slackHandle)?.replace(/^@/, "") ?? null;
  }
  if (typeof args.isActive === "boolean") data.isActive = args.isActive;

  const manager = await prisma.lineManager.update({ where: { id: managerId }, data });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.team.manager.update",
    targetType: "LineManager",
    targetId: managerId,
    details: { fields: Object.keys(data) },
    ipAddress: ip ?? undefined,
  });
  return ok(manager);
}

async function teamArchiveManagerTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  const managerId = typeof args.managerId === "string" ? args.managerId : "";
  if (!managerId) throw new McpValidationError("managerId is required");
  const existing = await prisma.lineManager.findUnique({ where: { id: managerId } });
  if (!existing) return fail("LineManager not found");
  const reportCount = await prisma.employee.count({ where: { lineManagerId: managerId } });
  if (reportCount > 0) {
    await prisma.employee.updateMany({
      where: { lineManagerId: managerId },
      data: { lineManagerId: null },
    });
  }
  const manager = await prisma.lineManager.update({
    where: { id: managerId },
    data: { isActive: false },
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.team.manager.archive",
    targetType: "LineManager",
    targetId: managerId,
    details: { unlinkedReports: reportCount },
    ipAddress: ip ?? undefined,
  });
  return ok({ manager, unlinkedReports: reportCount });
}

async function teamLinkEmployeeToManagerTool(
  args: ToolArgs,
  session: McpSession,
  ip: string | null,
): Promise<ToolResult> {
  const employeeId = typeof args.employeeId === "string" ? args.employeeId : "";
  if (!employeeId) throw new McpValidationError("employeeId is required");
  const employee = await prisma.employee.findUnique({ where: { id: employeeId } });
  if (!employee) return fail("Employee not found");
  let nextManagerId: string | null = null;
  if (args.managerId === null || args.managerId === "" || args.managerId === undefined) {
    nextManagerId = null;
  } else if (typeof args.managerId === "string") {
    const mgr = await prisma.lineManager.findUnique({ where: { id: args.managerId } });
    if (!mgr) return fail("LineManager not found");
    nextManagerId = args.managerId;
  } else {
    throw new McpValidationError("managerId must be string or null");
  }
  const updated = await prisma.employee.update({
    where: { id: employeeId },
    data: { lineManagerId: nextManagerId },
  });
  await auditLog({
    userId: session.userId,
    userEmail: session.userEmail,
    action: "mcp.team.employee.link",
    targetType: "Employee",
    targetId: employeeId,
    details: { previous: employee.lineManagerId, next: nextManagerId },
    ipAddress: ip ?? undefined,
  });
  return ok(updated);
}

```