---
type: source
source_type: laptop
title: page
slug: page-28
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/api-docs/page.tsx
original_size: 44791
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/admin/api-docs/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {  } from "@/components/ui/badge";
import {
  ChevronDown,
  Copy,
  Check,
  Shield,
  Users,
  FileText,
  Send,
  BarChart3,
  Egg,
  Zap,
  UserPlus,
  FileDown,
  CalendarDays,
  Webhook,
} from "lucide-react";

// ─── API Definition ─────────────────────────────────────────

interface Param {
  name: string;
  type: string;
  required: boolean;
  description: string;
}

interface Endpoint {
  method: "GET" | "POST" | "DELETE" | "PUT" | "PATCH";
  path: string;
  summary: string;
  description: string;
  auth: boolean;
  params?: Param[];
  queryParams?: Param[];
  body?: Param[];
  responseExample: string;
}

interface ApiSection {
  title: string;
  description: string;
  icon: React.ElementType;
  color: string;
  endpoints: Endpoint[];
}

const methodColors: Record<string, string> = {
  GET: "bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200",
  POST: "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200",
  DELETE: "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200",
  PUT: "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-200",
  PATCH: "bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200",
};

const apiSections: ApiSection[] = [
  {
    title: "Authentication",
    description: "Admin login and session management",
    icon: Shield,
    color: "text-red-600",
    endpoints: [
      {
        method: "POST",
        path: "/api/admin/auth",
        summary: "Admin login",
        description:
          "Authenticate as an admin user. Returns a session cookie that must be included in subsequent admin API requests.",
        auth: false,
        body: [
          { name: "email", type: "string", required: true, description: "Admin email address" },
          { name: "password", type: "string", required: true, description: "Admin password" },
        ],
        responseExample: JSON.stringify(
          {
            user: {
              id: "uuid",
              email: "admin@assessify.com",
              name: "Admin User",
              role: "admin",
            },
          },
          null,
          2
        ),
      },
      {
        method: "DELETE",
        path: "/api/admin/auth",
        summary: "Admin logout",
        description: "Destroy the current admin session.",
        auth: true,
        responseExample: JSON.stringify({ ok: true }, null, 2),
      },
    ],
  },
  {
    title: "Invites",
    description: "Create and manage candidate assessment invitations",
    icon: Send,
    color: "text-blue-600",
    endpoints: [
      {
        method: "GET",
        path: "/api/admin/invites",
        summary: "List all invites",
        description:
          "Returns all candidate invites with their status, assessment template, and department info.",
        auth: true,
        responseExample: JSON.stringify(
          {
            invites: [
              {
                id: "uuid",
                code: "abc123xyz456",
                candidateName: "Jane Smith",
                candidateEmail: "jane@company.com",
                status: "pending",
                expiresAt: "2026-04-16T00:00:00Z",
                createdAt: "2026-04-09T00:00:00Z",
                template: {
                  title: "IT Support Specialist Assessment",
                  jobRole: { title: "IT Support Specialist", department: { name: "Information Technology" } },
                },
              },
            ],
          },
          null,
          2
        ),
      },
      {
        method: "POST",
        path: "/api/admin/invites",
        summary: "Create invite and send email",
        description:
          "Creates a unique invite link for a candidate and sends them an email with the assessment details. The invite is tied to a specific assessment template.",
        auth: true,
        body: [
          { name: "candidateName", type: "string", required: true, description: "Full name of the candidate" },
          { name: "candidateEmail", type: "string", required: true, description: "Email address to send the invite to" },
          { name: "templateId", type: "string", required: true, description: "Assessment template ID" },
          { name: "expiresInDays", type: "number", required: false, description: "Days until the invite expires (default: 7)" },
        ],
        responseExample: JSON.stringify(
          {
            invite: {
              id: "uuid",
              code: "abc123xyz456",
              candidateName: "Jane Smith",
              candidateEmail: "jane@company.com",
              status: "pending",
              expiresAt: "2026-04-16T00:00:00Z",
              link: "/assess/invite/abc123xyz456",
              template: { title: "IT Support Specialist Assessment", jobRole: "IT Support Specialist", department: "Information Technology" },
            },
            emailSent: true,
          },
          null,
          2
        ),
      },
      {
        method: "DELETE",
        path: "/api/admin/invites?id={inviteId}",
        summary: "Delete an invite",
        description: "Permanently deletes an invite. The invite link will immediately stop working.",
        auth: true,
        queryParams: [
          { name: "id", type: "string", required: true, description: "Invite ID to delete" },
        ],
        responseExample: JSON.stringify({ ok: true }, null, 2),
      },
    ],
  },
  {
    title: "Assessments",
    description: "Browse available assessments and their structure",
    icon: FileText,
    color: "text-purple-600",
    endpoints: [
      {
        method: "GET",
        path: "/api/assessments",
        summary: "List published assessments",
        description:
          "Returns all active assessment templates that have a published version. Includes department, job role, sections, and question counts.",
        auth: false,
        responseExample: JSON.stringify(
          {
            assessments: [
              {
                id: "uuid",
                title: "IT Support Specialist Assessment",
                slug: "it-support-specialist-v1",
                description: "Comprehensive assessment...",
                jobRole: { id: "uuid", title: "IT Support Specialist", slug: "it-support-specialist", department: "Information Technology" },
                version: { id: "uuid", versionNumber: 1, passingScore: 0.6, timeLimit: 45 },
                sections: [{ id: "uuid", title: "Cultural Fit", slug: "cultural-fit", questionCount: 6, weight: 0.3 }],
              },
            ],
          },
          null,
          2
        ),
      },
      {
        method: "GET",
        path: "/api/assessments/{slug}",
        summary: "Get full assessment by slug",
        description:
          "Returns the complete assessment structure including all sections, questions, and options. Scoring data (points, correct answers) is excluded to prevent cheating.",
        auth: false,
        params: [
          { name: "slug", type: "string", required: true, description: "Assessment template slug" },
        ],
        responseExample: JSON.stringify(
          {
            assessment: {
              id: "uuid",
              title: "IT Support Specialist Assessment",
              sections: [
                {
                  id: "uuid",
                  title: "Cultural Fit",
                  questions: [
                    {
                      id: "uuid",
                      title: "Missed Deadline Scenario",
                      prompt: "You realize at 4 PM that...",
                      questionType: "single_select",
                      options: [{ key: "a", label: "Rush to finish it..." }],
                    },
                  ],
                },
              ],
            },
          },
          null,
          2
        ),
      },
    ],
  },
  {
    title: "Candidate Sessions",
    description: "Start assessments, submit answers, and complete sessions",
    icon: Users,
    color: "text-green-600",
    endpoints: [
      {
        method: "POST",
        path: "/api/sessions",
        summary: "Start a new session",
        description:
          "Creates a new candidate session for an assessment. Returns the session ID and full assessment data. Typically triggered via invite links, but can be called directly.",
        auth: false,
        body: [
          { name: "assessmentSlug", type: "string", required: true, description: "Assessment template slug" },
          { name: "candidateName", type: "string", required: true, description: "Candidate full name" },
          { name: "candidateEmail", type: "string", required: true, description: "Candidate email" },
        ],
        responseExample: JSON.stringify(
          {
            session: { id: "uuid", status: "in_progress", startedAt: "2026-04-09T00:00:00Z" },
            assessment: { title: "...", sections: ["..."] },
          },
          null,
          2
        ),
      },
      {
        method: "GET",
        path: "/api/sessions/{sessionId}",
        summary: "Get session status",
        description:
          "Returns the current session status, progress, and assessment metadata. Includes answered question count per section.",
        auth: false,
        params: [
          { name: "sessionId", type: "string", required: true, description: "Session ID" },
        ],
        responseExample: JSON.stringify(
          {
            session: {
              id: "uuid",
              status: "in_progress",
              candidateName: "Jane Smith",
              assessment: { title: "...", departmentSlug: "information-technology" },
              progress: { totalQuestions: 21, answeredQuestions: 8, completionPercent: 38 },
            },
          },
          null,
          2
        ),
      },
      {
        method: "POST",
        path: "/api/sessions/{sessionId}/answers",
        summary: "Submit an answer",
        description:
          "Submits and immediately scores a candidate's answer. Returns earned points, normalized score, and any flags. Supports upsert (resubmitting overwrites).",
        auth: false,
        params: [
          { name: "sessionId", type: "string", required: true, description: "Session ID" },
        ],
        body: [
          { name: "questionId", type: "string", required: true, description: "Question ID" },
          { name: "sectionId", type: "string", required: true, description: "Section ID" },
          {
            name: "answerPayload",
            type: "object",
            required: true,
            description: "Answer data: { questionId, selectedOptions?, rankingOrder?, timeSpent }",
          },
        ],
        responseExample: JSON.stringify(
          {
            responseId: "uuid",
            questionId: "uuid",
            earnedPoints: 10,
            maxPoints: 10,
            normalizedScore: 1,
            scoringReason: "Scored via weighted options: 10/10",
            flaggedIndicators: [],
          },
          null,
          2
        ),
      },
      {
        method: "POST",
        path: "/api/sessions/{sessionId}/complete",
        summary: "Complete assessment",
        description:
          "Finalizes the assessment. Runs the full scoring pipeline: section scores, competency scores, recommendation, confidence, hiring summary, automation labels, and risk indicators. Fires webhooks and updates invite status.",
        auth: false,
        params: [
          { name: "sessionId", type: "string", required: true, description: "Session ID" },
        ],
        responseExample: JSON.stringify(
          {
            result: {
              totalScore: 84,
              maxScore: 100,
              normalizedScore: 0.84,
              recommendation: "hire",
              confidenceRating: 0.91,
              hiringSummary: "Strong candidate with...",
              automationLabels: ["eligible_for_interview", "high_ai_readiness"],
              riskIndicators: [],
              flags: [],
              sectionScores: [{ sectionId: "uuid", title: "Cultural Fit", normalizedScore: 0.87 }],
              competencyScores: [{ competencyId: "uuid", name: "Communication", normalizedScore: 0.9 }],
            },
          },
          null,
          2
        ),
      },
      {
        method: "GET",
        path: "/api/sessions/{sessionId}/result",
        summary: "Get assessment result",
        description:
          "Returns the full structured result for a completed session. Includes scores, recommendation, flags, and automation labels. This is the primary endpoint for n8n/webhook integrations.",
        auth: false,
        params: [
          { name: "sessionId", type: "string", required: true, description: "Session ID" },
        ],
        responseExample: JSON.stringify(
          {
            result: {
              normalizedScore: 0.84,
              recommendation: "hire",
              hiringSummary: "Strong candidate...",
              sectionScores: ["..."],
              competencyScores: ["..."],
              flags: [],
              automationLabels: ["eligible_for_interview"],
            },
          },
          null,
          2
        ),
      },
    ],
  },
  {
    title: "Admin Sessions",
    description: "View and manage candidate sessions from the admin side",
    icon: Users,
    color: "text-amber-600",
    endpoints: [
      {
        method: "GET",
        path: "/api/admin/sessions",
        summary: "List all sessions",
        description:
          "Returns all candidate sessions with result summaries. Used by the admin dashboard.",
        auth: true,
        responseExample: JSON.stringify(
          {
            sessions: [
              {
                id: "uuid",
                candidateName: "Jane Smith",
                status: "completed",
                assessment: { title: "...", slug: "..." },
                result: { recommendation: "hire", normalizedScore: 0.84 },
              },
            ],
            total: 1,
          },
          null,
          2
        ),
      },
      {
        method: "GET",
        path: "/api/admin/sessions/{sessionId}",
        summary: "Get full session detail",
        description:
          "Returns complete session data including all responses (with decoded payloads), result, section scores, and competency scores.",
        auth: true,
        params: [
          { name: "sessionId", type: "string", required: true, description: "Session ID" },
        ],
        responseExample: JSON.stringify(
          {
            session: {
              id: "uuid",
              candidateName: "Jane Smith",
              responses: [{ questionTitle: "...", earnedPoints: 10, maxPoints: 10 }],
              result: { recommendation: "hire", normalizedScore: 0.84 },
              sectionScores: ["..."],
              competencyScores: ["..."],
            },
          },
          null,
          2
        ),
      },
    ],
  },
  {
    title: "Analytics",
    description: "Assessment funnel, question stats, and competency data",
    icon: BarChart3,
    color: "text-indigo-600",
    endpoints: [
      {
        method: "GET",
        path: "/api/admin/analytics",
        summary: "Get analytics data",
        description:
          "Returns analytics data for a specific assessment version. Supports different data types via the type parameter.",
        auth: true,
        queryParams: [
          { name: "versionId", type: "string", required: true, description: "Assessment version ID" },
          { name: "type", type: "string", required: true, description: "One of: funnel, questions, competencies, distribution" },
        ],
        responseExample: JSON.stringify(
          {
            "type: funnel": { total: 50, started: 45, completed: 38, completionRate: 0.76 },
            "type: questions": [{ questionId: "uuid", title: "...", avgScore: 0.72, failRate: 0.15 }],
            "type: competencies": [{ slug: "communication", name: "Communication", avgScore: 0.81 }],
            "type: distribution": { distribution: { strong_hire: 5, hire: 12, consider: 8 }, totalCandidates: 38 },
          },
          null,
          2
        ),
      },
    ],
  },
  {
    title: "Invite Flow",
    description: "Candidate-facing invite endpoints",
    icon: Zap,
    color: "text-cyan-600",
    endpoints: [
      {
        method: "GET",
        path: "/api/assess/invite/{code}",
        summary: "Get invite details",
        description:
          "Returns invite info and assessment details for the candidate landing page. Validates expiry.",
        auth: false,
        params: [
          { name: "code", type: "string", required: true, description: "Unique invite code" },
        ],
        responseExample: JSON.stringify(
          {
            invite: { id: "uuid", code: "abc123", candidateName: "Jane", status: "pending" },
            assessment: { title: "...", department: "Information Technology", jobRole: "IT Support Specialist", sectionCount: 3, questionCount: 21, timeLimit: 45 },
          },
          null,
          2
        ),
      },
      {
        method: "POST",
        path: "/api/assess/invite/{code}/start",
        summary: "Start assessment from invite",
        description:
          "Creates a candidate session linked to the invite. If already started, returns the existing session ID. Updates invite status to 'started'.",
        auth: false,
        params: [
          { name: "code", type: "string", required: true, description: "Unique invite code" },
        ],
        responseExample: JSON.stringify({ sessionId: "uuid" }, null, 2),
      },
    ],
  },
  {
    title: "Easter Eggs",
    description: "Hidden challenge system endpoints",
    icon: Egg,
    color: "text-orange-600",
    endpoints: [
      {
        method: "GET",
        path: "/api/easter/claim?email={email}",
        summary: "Get claimed eggs for a candidate",
        description: "Returns all easter eggs claimed by a specific email address.",
        auth: false,
        queryParams: [
          { name: "email", type: "string", required: true, description: "Candidate email" },
        ],
        responseExample: JSON.stringify(
          { claims: [{ eggId: "egg_1", claimedAt: "2026-04-09T00:00:00Z" }] },
          null,
          2
        ),
      },
      {
        method: "POST",
        path: "/api/easter/claim",
        summary: "Claim an easter egg",
        description: "Validates and records an easter egg discovery. Prevents duplicate claims per email.",
        auth: false,
        body: [
          { name: "egg", type: "string", required: true, description: "The full egg code (e.g. egg{...})" },
          { name: "candidateName", type: "string", required: true, description: "Candidate name" },
          { name: "candidateEmail", type: "string", required: true, description: "Candidate email" },
          { name: "sessionId", type: "string", required: false, description: "Session ID (optional)" },
        ],
        responseExample: JSON.stringify(
          { "\ud83c\udf89": "Congratulations! You found \"The Source Seeker\"!", egg: "egg_1", difficulty: "easy" },
          null,
          2
        ),
      },
      {
        method: "GET",
        path: "/api/easter/hints?egg={eggId}&email={email}",
        summary: "Get hint for an egg",
        description:
          "Returns a progressive hint for the specified egg. Hint difficulty increases based on how many eggs the candidate has already found. Egg 4 has no hints.",
        auth: false,
        queryParams: [
          { name: "egg", type: "string", required: true, description: "Egg ID (egg_1, egg_2, egg_3, egg_4)" },
          { name: "email", type: "string", required: false, description: "Candidate email (for hint level)" },
        ],
        responseExample: JSON.stringify(
          { egg: "egg_1", difficulty: "easy", hintLevel: 1, totalHints: 3, hint: "Great explorers always check what is beneath the surface." },
          null,
          2
        ),
      },
    ],
  },
  {
    title: "Team Management",
    description: "Invite, manage, and control access for admin users",
    icon: UserPlus,
    color: "text-indigo-600",
    endpoints: [
      {
        method: "GET",
        path: "/api/admin/users",
        summary: "List all admin users",
        description: "Returns all admin/user accounts with their role, status, and creation date. Requires authentication.",
        auth: true,
        responseExample: JSON.stringify(
          { users: [{ id: "uuid", email: "admin@example.com", name: "Jehad", role: "admin", isActive: true, createdAt: "2026-04-10T..." }] },
          null, 2
        ),
      },
      {
        method: "POST",
        path: "/api/admin/users",
        summary: "Invite a new team member",
        description: "Creates a pending user account and sends an invite email. Admin role required.",
        auth: true,
        body: [
          { name: "email", type: "string", required: true, description: "Work email address" },
          { name: "role", type: "string", required: true, description: "'admin' or 'user'" },
        ],
        responseExample: JSON.stringify(
          { ok: true, emailSent: true, inviteLink: "http://localhost:3000/admin/setup?token=abc123" },
          null, 2
        ),
      },
      {
        method: "PATCH",
        path: "/api/admin/users/{id}",
        summary: "Update a user (role, status, password)",
        description: "Toggle active status, change role, or force-reset password. Admin role required. Cannot modify yourself or remove the last admin.",
        auth: true,
        params: [{ name: "id", type: "string", required: true, description: "User ID" }],
        body: [
          { name: "isActive", type: "boolean", required: false, description: "Activate/deactivate user" },
          { name: "role", type: "string", required: false, description: "'admin' or 'user'" },
          { name: "newPassword", type: "string", required: false, description: "Force-reset password (min 8 chars)" },
        ],
        responseExample: JSON.stringify({ ok: true }, null, 2),
      },
      {
        method: "DELETE",
        path: "/api/admin/users/{id}",
        summary: "Delete a user permanently",
        description: "Removes the user and all their OTP tokens. Admin role required. Cannot delete yourself or the last admin.",
        auth: true,
        params: [{ name: "id", type: "string", required: true, description: "User ID" }],
        responseExample: JSON.stringify({ ok: true }, null, 2),
      },
      {
        method: "POST",
        path: "/api/admin/users/{id}/resend",
        summary: "Resend invite to a pending user",
        description: "Generates a new invite token and re-sends the setup email. Only works for inactive (pending) users. Admin role required.",
        auth: true,
        params: [{ name: "id", type: "string", required: true, description: "User ID" }],
        responseExample: JSON.stringify({ ok: true, emailSent: true, inviteLink: "http://localhost:3000/admin/setup?token=newtoken" }, null, 2),
      },
      {
        method: "GET",
        path: "/api/admin/setup?token={token}",
        summary: "Validate invite token",
        description: "Public endpoint (no auth). Checks if the invite token is valid and not expired. Returns the email for the setup form.",
        auth: false,
        queryParams: [{ name: "token", type: "string", required: true, description: "Invite token from email" }],
        responseExample: JSON.stringify({ valid: true, email: "colleague@company.com" }, null, 2),
      },
      {
        method: "POST",
        path: "/api/admin/setup",
        summary: "Activate account from invite",
        description: "Public endpoint (no auth). Sets the user's name and password, activates the account, and auto-logs them in. Rate limited to 5/min.",
        auth: false,
        body: [
          { name: "token", type: "string", required: true, description: "Invite token" },
          { name: "name", type: "string", required: true, description: "Full name" },
          { name: "password", type: "string", required: true, description: "Password (min 8 chars)" },
        ],
        responseExample: JSON.stringify({ ok: true }, null, 2),
      },
      {
        method: "GET",
        path: "/api/admin/auth",
        summary: "Get current session",
        description: "Returns the currently authenticated user, or null if not logged in.",
        auth: false,
        responseExample: JSON.stringify({ user: { id: "uuid", email: "admin@example.com", name: "Jehad", role: "admin" } }, null, 2),
      },
    ],
  },
  {
    title: "PDF Export",
    description: "Generate printable reports for candidate sessions",
    icon: FileDown,
    color: "text-cyan-600",
    endpoints: [
      {
        method: "GET",
        path: "/api/admin/sessions/{sessionId}/pdf",
        summary: "Export candidate report as PDF",
        description: "Returns a print-ready HTML page with the full assessment report. Open in browser and use print-to-PDF. Includes summary, section scores, competency scores, and all question responses.",
        auth: true,
        params: [{ name: "sessionId", type: "string", required: true, description: "Candidate session ID" }],
        responseExample: "<!-- Returns HTML, not JSON. Open the URL directly in a browser tab. -->",
      },
    ],
  },
  {
    title: "Leave Management",
    description: "Leave request submission, approval workflow, and PDF document generation. Public form at /leave/new; admin views under /admin/leave-requests.",
    icon: CalendarDays,
    color: "text-blue-600",
    endpoints: [
      {
        method: "POST",
        path: "/api/leave",
        summary: "Submit a new leave request",
        description: "Public endpoint. Validates input, checks employee leave balance, creates a LeaveRequest record, and DMs the line manager via Slack with Approve/Reject buttons. If balance is drained, creates a blocked record and DMs both the employee and HR (mariamm) with an advisory message. The employee signature must match the selected employee's registered name (case-insensitive).",
        auth: false,
        body: [
          { name: "employeeId", type: "string", required: true, description: "Employee ID from the Employee directory (e.g. emp-jehad)" },
          { name: "lineManagerId", type: "string", required: true, description: "Line Manager ID (e.g. mgr-michael-bruck)" },
          { name: "leaveType", type: "string", required: true, description: "One of: Annual Leave, Sick Leave, Business Travel Leave, Maternity Leave, Paternity Leave, Emergency Leave, Hajj Leave, Unpaid / Other Leave" },
          { name: "startDate", type: "string (ISO date)", required: true, description: "First day of leave, YYYY-MM-DD" },
          { name: "endDate", type: "string (ISO date)", required: true, description: "Last day of leave (inclusive)" },
          { name: "employeeSignature", type: "string", required: true, description: "Typed full name — must match the employee's registered name" },
          { name: "department", type: "string", required: false, description: "Employee's department / team (for the document)" },
          { name: "reason", type: "string", required: false, description: "Optional notes / reason for the request" },
        ],
        responseExample: JSON.stringify(
          { ok: true, status: "pending_manager", message: "Your request has been sent to Michael Bruck for approval. You will be notified once a decision is made." },
          null,
          2
        ),
      },
      {
        method: "DELETE",
        path: "/api/leave/{id}",
        summary: "Delete a leave request",
        description: "Permanently removes a LeaveRequest record. Does not refund consumed balance if the request was previously approved — balance adjustments must be done manually in the Leave Balances dashboard.",
        auth: true,
        params: [{ name: "id", type: "string", required: true, description: "LeaveRequest ID (UUID)" }],
        responseExample: JSON.stringify({ ok: true }, null, 2),
      },
      {
        method: "POST",
        path: "/api/leave/{id}/mark-viewed",
        summary: "Mark a leave request as viewed by HR",
        description: "Clears the unread indicator for the request. Called automatically by the detail page on mount; rarely used manually.",
        auth: true,
        params: [{ name: "id", type: "string", required: true, description: "LeaveRequest ID" }],
        responseExample: JSON.stringify({ ok: true }, null, 2),
      },
      {
        method: "GET",
        path: "/api/leave/{id}/pdf",
        summary: "View / download leave request document",
        description: "Returns a print-ready HTML page with the full leave request document — employee details, leave details, approval history, and typed signatures. Open in browser and use print-to-PDF to save. This URL is sent to the employee via Slack after final HR approval.",
        auth: false,
        params: [{ name: "id", type: "string", required: true, description: "LeaveRequest ID" }],
        responseExample: "<!-- Returns HTML, not JSON. Open the URL directly in a browser tab. -->",
      },
    ],
  },
  {
    title: "Slack Integration",
    description: "Slack webhook endpoint consumed by the Nomi bot for interactive approvals. All requests must carry a valid X-Slack-Signature header — Slack signs with HMAC-SHA256 using the signing secret.",
    icon: Webhook,
    color: "text-purple-600",
    endpoints: [
      {
        method: "POST",
        path: "/api/slack/interactive",
        summary: "Slack interactivity callback",
        description:
          "Handles button clicks and modal submissions from Nomi DMs during the leave approval flow. Verifies the X-Slack-Signature header (HMAC-SHA256 of `v0:{timestamp}:{rawBody}` using SLACK_SIGNING_SECRET) and rejects requests older than 5 minutes (replay protection). Routes by action_id: approve_manager → transitions to pending_hr and DMs HR; reject_manager → opens rejection modal; approve_hr → finalizes, consumes balance, DMs employee with PDF link; reject_hr → opens rejection modal. Modal submissions record the rejection reason and DM the employee. Not intended for direct use by developers — configure Slack App Interactivity Request URL to point here.",
        auth: false,
        body: [
          { name: "payload", type: "string (JSON)", required: true, description: "Slack payload as form-urlencoded field — see https://api.slack.com/reference/interaction-payloads" },
        ],
        responseExample: "HTTP 200 (empty) — or response_action:errors for validation failures",
      },
    ],
  },
];

// ─── Component ──────────────────────────────────────────────

function buildCurl(endpoint: Endpoint, baseUrl: string): string {
  let path = endpoint.path;

  // Replace path params with example values
  path = path.replace("{sessionId}", "SESSION_ID");
  path = path.replace("{slug}", "it-support-specialist-v1");
  path = path.replace("{code}", "INVITE_CODE");
  path = path.replace("{inviteId}", "INVITE_ID");
  path = path.replace("{email}", "candidate@email.com");
  path = path.replace("{eggId}", "egg_1");

  const url = `${baseUrl}${path}`;
  const parts: string[] = [`curl`];

  if (endpoint.method !== "GET") {
    parts.push(`-X ${endpoint.method}`);
  }

  parts.push(`"${url}"`);

  // Always include headers
  const headers: string[] = [];

  if (endpoint.auth) {
    headers.push(`-H "Cookie: assessify_admin_session=YOUR_SESSION_TOKEN"`);
  }

  if (endpoint.body && endpoint.body.length > 0) {
    headers.push(`-H "Content-Type: application/json"`);
    headers.push(`-H "Accept: application/json"`);
  } else {
    headers.push(`-H "Accept: application/json"`);
  }

  parts.push(...headers);

  if (endpoint.body && endpoint.body.length > 0) {
    const bodyObj: Record<string, unknown> = {};
    for (const p of endpoint.body) {
      if (p.type === "object") {
        bodyObj[p.name] = { questionId: "QUESTION_ID", selectedOptions: ["b"], timeSpent: 15 };
      } else if (p.type === "number") {
        bodyObj[p.name] = 7;
      } else {
        bodyObj[p.name] =
          p.name === "email" || p.name === "candidateEmail"
            ? "candidate@email.com"
            : p.name === "candidateName"
              ? "Jane Smith"
              : p.name === "templateId"
                ? "TEMPLATE_ID"
                : p.name === "assessmentSlug"
                  ? "it-support-specialist-v1"
                  : p.name === "password"
                    ? "admin123"
                    : p.name === "egg"
                      ? "egg{your_egg_value}"
                      : p.name === "sessionId"
                        ? "SESSION_ID"
                        : `YOUR_${p.name.toUpperCase()}`;
      }
    }
    parts.push(`-d '${JSON.stringify(bodyObj, null, 2)}'`);
  }

  return parts.join(" \\\n  ");
}

function EndpointCard({ endpoint }: { endpoint: Endpoint }) {
  const [open, setOpen] = useState(false);
  const [copiedField, setCopiedField] = useState<string | null>(null);

  const copyCode = (text: string, field: string) => {
    navigator.clipboard.writeText(text);
    setCopiedField(field);
    setTimeout(() => setCopiedField(null), 2000);
  };

  const baseUrl = typeof window !== "undefined" ? window.location.origin : "http://localhost:3000";
  const curlExample = buildCurl(endpoint, baseUrl);

  return (
    <div className="rounded-lg border border-zinc-200 dark:border-zinc-800">
      <button
        onClick={() => setOpen(!open)}
        className="flex w-full items-center gap-3 p-4 text-left transition-colors hover:bg-zinc-50 dark:hover:bg-zinc-800/50"
      >
        <span
          className={`inline-flex w-16 items-center justify-center rounded-md px-2 py-0.5 text-[10px] font-bold ${
            methodColors[endpoint.method]
          }`}
        >
          {endpoint.method}
        </span>
        <code className="flex-1 font-mono text-sm text-muted-foreground">
          {endpoint.path}
        </code>
        <span className="hidden text-xs text-muted-foreground sm:block">
          {endpoint.summary}
        </span>
        {endpoint.auth && (
          <span title="Requires authentication"><Shield className="size-3.5 text-red-500" /></span>
        )}
        <ChevronDown
          className={`size-4 text-muted-foreground transition-transform ${
            open ? "rotate-180" : ""
          }`}
        />
      </button>

      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="overflow-hidden"
          >
            <div className="border-t border-zinc-200 p-4 dark:border-zinc-800">
              <p className="mb-4 text-sm leading-relaxed text-muted-foreground">
                {endpoint.description}
              </p>

              {endpoint.auth && (
                <div className="mb-4 flex items-center gap-2 rounded-lg bg-red-50 p-2.5 text-xs text-red-700 dark:bg-red-950 dark:text-red-300">
                  <Shield className="size-3.5" />
                  Requires admin authentication (session cookie)
                </div>
              )}

              {/* URL Params */}
              {endpoint.params && endpoint.params.length > 0 && (
                <div className="mb-4">
                  <h4 className="mb-2 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                    URL Parameters
                  </h4>
                  <ParamTable params={endpoint.params} />
                </div>
              )}

              {/* Query Params */}
              {endpoint.queryParams && endpoint.queryParams.length > 0 && (
                <div className="mb-4">
                  <h4 className="mb-2 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                    Query Parameters
                  </h4>
                  <ParamTable params={endpoint.queryParams} />
                </div>
              )}

              {/* Body */}
              {endpoint.body && endpoint.body.length > 0 && (
                <div className="mb-4">
                  <h4 className="mb-2 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                    Request Body (JSON)
                  </h4>
                  <ParamTable params={endpoint.body} />
                </div>
              )}

              {/* cURL Example */}
              <div className="mb-4">
                <div className="mb-2 flex items-center justify-between">
                  <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                    cURL Example
                  </h4>
                  <button
                    onClick={() => copyCode(curlExample, "curl")}
                    className="inline-flex items-center gap-1 rounded-md px-2 py-1 text-[10px] font-medium text-muted-foreground transition-colors hover:bg-zinc-100 dark:hover:bg-zinc-800"
                  >
                    {copiedField === "curl" ? (
                      <>
                        <Check className="size-3 text-green-500" /> Copied
                      </>
                    ) : (
                      <>
                        <Copy className="size-3" /> Copy
                      </>
                    )}
                  </button>
                </div>
                <pre className="overflow-x-auto rounded-lg bg-zinc-900 p-4 text-xs leading-relaxed text-emerald-400 dark:bg-zinc-800">
                  <code>{curlExample}</code>
                </pre>
              </div>

              {/* Response */}
              <div>
                <div className="mb-2 flex items-center justify-between">
                  <h4 className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                    Response Example
                  </h4>
                  <button
                    onClick={() => copyCode(endpoint.responseExample, "response")}
                    className="inline-flex items-center gap-1 rounded-md px-2 py-1 text-[10px] font-medium text-muted-foreground transition-colors hover:bg-zinc-100 dark:hover:bg-zinc-800"
                  >
                    {copiedField === "response" ? (
                      <>
                        <Check className="size-3 text-green-500" /> Copied
                      </>
                    ) : (
                      <>
                        <Copy className="size-3" /> Copy
                      </>
                    )}
                  </button>
                </div>
                <pre className="overflow-x-auto rounded-lg bg-zinc-950 p-4 text-xs leading-relaxed text-zinc-300 dark:bg-zinc-800">
                  <code>{endpoint.responseExample}</code>
                </pre>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

function ParamTable({ params }: { params: Param[] }) {
  return (
    <div className="overflow-hidden rounded-lg border border-zinc-200 dark:border-zinc-800">
      <table className="w-full text-xs">
        <thead>
          <tr className="border-b border-zinc-200 bg-zinc-50 dark:border-zinc-800 dark:bg-zinc-800/50">
            <th className="px-3 py-2 text-left font-medium">Name</th>
            <th className="px-3 py-2 text-left font-medium">Type</th>
            <th className="px-3 py-2 text-left font-medium">Required</th>
            <th className="px-3 py-2 text-left font-medium">Description</th>
          </tr>
        </thead>
        <tbody>
          {params.map((p) => (
            <tr
              key={p.name}
              className="border-b border-zinc-100 last:border-0 dark:border-zinc-800"
            >
              <td className="px-3 py-2 font-mono font-medium">{p.name}</td>
              <td className="px-3 py-2 text-muted-foreground">{p.type}</td>
              <td className="px-3 py-2">
                {p.required ? (
                  <span className="text-red-600">required</span>
                ) : (
                  <span className="text-muted-foreground">optional</span>
                )}
              </td>
              <td className="px-3 py-2 text-muted-foreground">
                {p.description}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default function ApiDocsPage() {
  const totalEndpoints = apiSections.reduce(
    (sum, s) => sum + s.endpoints.length,
    0
  );

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">
          API Documentation
        </h1>
        <p className="text-sm text-muted-foreground">
          {totalEndpoints} endpoints available for automation and integration.
        </p>
      </div>

      {/* Quick reference */}
      <Card>
        <CardHeader>
          <CardTitle>Quick Reference</CardTitle>
          <CardDescription>
            Base URL and authentication
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            <div className="rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800/50">
              <p className="mb-1 text-xs font-medium">Base URL</p>
              <code className="text-sm text-muted-foreground">
                {typeof window !== "undefined" ? window.location.origin : "http://localhost:3000"}
              </code>
            </div>
            <div className="rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800/50">
              <p className="mb-1 text-xs font-medium">Authentication</p>
              <p className="text-xs text-muted-foreground">
                Admin endpoints (marked with <Shield className="inline size-3 text-red-500" />) require a session cookie obtained via <code className="rounded bg-zinc-200 px-1 dark:bg-zinc-700">POST /api/admin/auth</code>.
                Candidate-facing endpoints do not require authentication.
              </p>
            </div>
            <div className="rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800/50">
              <p className="mb-1 text-xs font-medium">Content Type</p>
              <p className="text-xs text-muted-foreground">
                All POST requests expect <code className="rounded bg-zinc-200 px-1 dark:bg-zinc-700">Content-Type: application/json</code>
              </p>
            </div>
            <div className="rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800/50">
              <p className="mb-1 text-xs font-medium">Automation (n8n / Webhooks)</p>
              <p className="text-xs text-muted-foreground">
                Key endpoints for automation: <code className="rounded bg-zinc-200 px-1 dark:bg-zinc-700">POST /api/admin/invites</code> (send assessments),{" "}
                <code className="rounded bg-zinc-200 px-1 dark:bg-zinc-700">GET /api/sessions/&#123;id&#125;/result</code> (fetch results),{" "}
                <code className="rounded bg-zinc-200 px-1 dark:bg-zinc-700">GET /api/admin/analytics</code> (pipeline data).
                Webhooks fire automatically on assessment completion.
              </p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* API Sections */}
      {apiSections.map((section) => (
        <div key={section.title}>
          <div className="mb-3 flex items-center gap-2">
            <section.icon className={`size-4 ${section.color}`} />
            <h2 className="text-lg font-semibold">{section.title}</h2>
            <span className="text-xs text-muted-foreground">
              {section.endpoints.length} endpoint{section.endpoints.length !== 1 ? "s" : ""}
            </span>
          </div>
          <p className="mb-3 text-sm text-muted-foreground">
            {section.description}
          </p>
          <div className="space-y-2">
            {section.endpoints.map((ep) => (
              <EndpointCard key={`${ep.method}-${ep.path}`} endpoint={ep} />
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

```