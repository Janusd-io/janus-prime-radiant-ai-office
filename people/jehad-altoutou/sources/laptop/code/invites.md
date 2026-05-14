---
type: source
source_type: laptop
title: invites
slug: invites
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/invites.ts
original_size: 17756
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# invites

_Extracted from `[[assessify|assessify]]/src/lib/operations/invites.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import { nanoid } from "nanoid";
import {
  clampLimit,
  cursorWhere,
  decodeCursor,
  pageResult,
  type CursorPaged,
} from "@/lib/mcp/pagination";
import { McpValidationError } from "@/lib/mcp/validation";
import { sendAssessmentInviteEmail } from "@/lib/email";
import { findByExternalId } from "./external-id";

// ─── Shared shape ──────────────────────────────────────────────────

export interface InviteRecord {
  id: string;
  code: string;
  candidateName: string;
  candidateEmail: string;
  status: string;
  templateId: string;
  assessmentTitle: string;
  expiresAt: Date | null;
  createdAt: Date;
  updatedAt: Date;
  externalId: string | null;
  inviteLink: string;
  sessionId: string | null;
}

function buildInviteLink(code: string): string {
  const base = process.env.PUBLIC_APP_URL || process.env.APP_URL || "http://localhost:3000";
  return `${base}/assess/invite/${code}`;
}

function toInviteRecord(invite: {
  id: string;
  code: string;
  candidateName: string;
  candidateEmail: string;
  status: string;
  templateId: string;
  expiresAt: Date | null;
  createdAt: Date;
  updatedAt: Date;
  externalId: string | null;
  sessionId: string | null;
  template: { title: string };
}): InviteRecord {
  return {
    id: invite.id,
    code: invite.code,
    candidateName: invite.candidateName,
    candidateEmail: invite.candidateEmail,
    status: invite.status,
    templateId: invite.templateId,
    assessmentTitle: invite.template.title,
    expiresAt: invite.expiresAt,
    createdAt: invite.createdAt,
    updatedAt: invite.updatedAt,
    externalId: invite.externalId,
    sessionId: invite.sessionId,
    inviteLink: buildInviteLink(invite.code),
  };
}

// ─── get_invite ────────────────────────────────────────────────────

export async function getInvite(inviteId: string): Promise<InviteRecord> {
  const invite = await prisma.candidateInvite.findUnique({
    where: { id: inviteId },
    include: { template: { select: { title: true } } },
  });
  if (!invite) throw new McpValidationError(`invite not found: ${inviteId}`);
  return toInviteRecord(invite);
}

// ─── list_invites ──────────────────────────────────────────────────

export interface ListInvitesInput {
  assessmentId?: string;
  candidateEmail?: string;
  status?: string;
  dateFrom?: string;
  dateTo?: string;
  limit?: number;
  cursor?: string;
}

const ALLOWED_STATUSES = ["pending", "started", "completed", "expired", "revoked"];

export async function listInvites(
  input: ListInvitesInput
): Promise<CursorPaged<InviteRecord>> {
  const limit = clampLimit(input.limit);
  const cursor = decodeCursor(input.cursor);
  const where: Record<string, unknown> = {};
  if (input.assessmentId) where.templateId = input.assessmentId;
  if (input.candidateEmail) where.candidateEmail = input.candidateEmail.toLowerCase();
  if (input.status) {
    if (!ALLOWED_STATUSES.includes(input.status)) {
      throw new McpValidationError(
        `invalid status "${input.status}" — must be one of: ${ALLOWED_STATUSES.join(", ")}`
      );
    }
    where.status = input.status;
  }
  if (input.dateFrom || input.dateTo) {
    where.createdAt = {
      ...(input.dateFrom ? { gte: new Date(input.dateFrom) } : {}),
      ...(input.dateTo ? { lte: new Date(input.dateTo) } : {}),
    };
  }

  const cw = cursorWhere(cursor);
  const finalWhere = cw ? { AND: [where, cw] } : where;

  const rows = await prisma.candidateInvite.findMany({
    where: finalWhere,
    take: limit + 1,
    orderBy: [{ createdAt: "desc" }, { id: "desc" }],
    include: { template: { select: { title: true } } },
  });

  return pageResult(rows.map(toInviteRecord), limit);
}

// ─── revoke_invite ─────────────────────────────────────────────────

export async function revokeInvite(inviteId: string): Promise<InviteRecord> {
  const invite = await prisma.candidateInvite.findUnique({
    where: { id: inviteId },
    include: { template: { select: { title: true } } },
  });
  if (!invite) throw new McpValidationError(`invite not found: ${inviteId}`);
  if (invite.status === "completed") {
    throw new McpValidationError(
      `cannot revoke completed invite ${inviteId} — the candidate has already finished`
    );
  }
  if (invite.status === "started") {
    throw new McpValidationError(
      `cannot revoke an in-progress invite ${inviteId} — the candidate is mid-assessment. Wait for completion or expiration.`
    );
  }
  if (invite.status === "revoked") {
    return toInviteRecord(invite);
  }
  const updated = await prisma.candidateInvite.update({
    where: { id: inviteId },
    data: { status: "revoked" },
    include: { template: { select: { title: true } } },
  });
  return toInviteRecord(updated);
}

// ─── resend_invite ─────────────────────────────────────────────────

export interface ResendInviteInput {
  inviteId: string;
  newExpiryDays?: number;
  sendEmail?: boolean;
}

export async function resendInvite(
  input: ResendInviteInput
): Promise<InviteRecord & { emailSent: boolean }> {
  const invite = await prisma.candidateInvite.findUnique({
    where: { id: input.inviteId },
    include: {
      template: {
        select: { title: true, jobRole: { select: { title: true, department: { select: { name: true } } } } },
      },
    },
  });
  if (!invite) throw new McpValidationError(`invite not found: ${input.inviteId}`);
  if (invite.status === "completed") {
    throw new McpValidationError(
      `cannot resend completed invite — candidate already finished`
    );
  }
  if (invite.status === "revoked") {
    throw new McpValidationError(
      `cannot resend revoked invite — create a new invite instead`
    );
  }

  let expiresAt = invite.expiresAt;
  if (typeof input.newExpiryDays === "number") {
    if (input.newExpiryDays <= 0) {
      throw new McpValidationError(`newExpiryDays must be a positive number`);
    }
    expiresAt = new Date(Date.now() + input.newExpiryDays * 86400000);
  }

  const updated = await prisma.candidateInvite.update({
    where: { id: input.inviteId },
    data: { expiresAt, status: invite.status === "expired" ? "pending" : invite.status },
    include: { template: { select: { title: true } } },
  });

  let emailSent = false;
  if (input.sendEmail) {
    try {
      await sendAssessmentInviteEmail({
        to: invite.candidateEmail,
        candidateName: invite.candidateName,
        assessmentTitle: invite.template.title,
        department: invite.template.jobRole.department.name,
        jobRole: invite.template.jobRole.title,
        inviteLink: buildInviteLink(invite.code),
        expiresAt: expiresAt ?? new Date(),
      });
      emailSent = true;
    } catch (e) {
      console.error("[invites] resend email failed:", e);
    }
  }

  return { ...toInviteRecord(updated), emailSent };
}

// ─── extend_invite_expiry ──────────────────────────────────────────

export async function extendInviteExpiry(input: {
  inviteId: string;
  expiresInDays: number;
}): Promise<InviteRecord> {
  if (!Number.isFinite(input.expiresInDays) || input.expiresInDays <= 0) {
    throw new McpValidationError(`expiresInDays must be a positive number`);
  }
  const invite = await prisma.candidateInvite.findUnique({
    where: { id: input.inviteId },
  });
  if (!invite) throw new McpValidationError(`invite not found: ${input.inviteId}`);
  if (invite.status === "completed") {
    throw new McpValidationError(`cannot extend completed invite — candidate already finished`);
  }
  if (invite.status === "revoked") {
    throw new McpValidationError(`cannot extend revoked invite`);
  }
  const expiresAt = new Date(Date.now() + input.expiresInDays * 86400000);
  const updated = await prisma.candidateInvite.update({
    where: { id: input.inviteId },
    data: {
      expiresAt,
      status: invite.status === "expired" ? "pending" : invite.status,
    },
    include: { template: { select: { title: true } } },
  });
  return toInviteRecord(updated);
}

// ─── update_candidate ──────────────────────────────────────────────
//
// "Candidate" isn't a first-class table — identity is the email. We update
// every CandidateInvite + CandidateSession row matching the current email
// (or the inviteId-anchored email) so name/email stay consistent across
// records. Refused once any session in finalized state exists, to preserve
// audit integrity.

export interface UpdateCandidateInput {
  /** One of inviteId or candidateEmail must be provided. inviteId is preferred. */
  inviteId?: string;
  candidateEmail?: string;
  name?: string;
  email?: string;
}

export interface UpdateCandidateResult {
  email: string;
  name: string;
  invitesUpdated: number;
  sessionsUpdated: number;
}

const FINALIZED_SESSION_STATUSES = ["completed", "expired", "disqualified"];

export async function updateCandidate(
  input: UpdateCandidateInput
): Promise<UpdateCandidateResult> {
  if (!input.name && !input.email) {
    throw new McpValidationError("update_candidate requires at least one of name or email");
  }
  let originalEmail: string | null = null;
  if (input.inviteId) {
    const invite = await prisma.candidateInvite.findUnique({
      where: { id: input.inviteId },
      select: { candidateEmail: true },
    });
    if (!invite) throw new McpValidationError(`invite not found: ${input.inviteId}`);
    originalEmail = invite.candidateEmail;
  } else if (input.candidateEmail) {
    originalEmail = input.candidateEmail.toLowerCase();
  } else {
    throw new McpValidationError("update_candidate requires inviteId or candidateEmail");
  }

  const finalized = await prisma.candidateSession.count({
    where: {
      candidateEmail: originalEmail,
      status: { in: FINALIZED_SESSION_STATUSES },
    },
  });
  if (finalized > 0) {
    throw new McpValidationError(
      `cannot update candidate — ${finalized} finalized session(s) exist for ${originalEmail}. Audit integrity prohibits post-completion edits.`
    );
  }

  const newEmail = input.email ? input.email.toLowerCase() : originalEmail;
  if (input.email && newEmail !== originalEmail) {
    const collision = await prisma.candidateInvite.findFirst({
      where: { candidateEmail: newEmail },
      select: { id: true },
    });
    if (collision) {
      throw new McpValidationError(
        `cannot change email to ${newEmail} — another candidate already uses that address`
      );
    }
  }

  const data: { candidateEmail?: string; candidateName?: string } = {};
  if (input.email) data.candidateEmail = newEmail;
  if (input.name) data.candidateName = input.name;

  const [invitesUpdated, sessionsUpdated] = await prisma.$transaction([
    prisma.candidateInvite.updateMany({
      where: { candidateEmail: originalEmail },
      data,
    }),
    prisma.candidateSession.updateMany({
      where: { candidateEmail: originalEmail },
      data,
    }),
  ]);

  // Resolve final name (use new name if provided, else fetch from a remaining row)
  let finalName = input.name ?? "";
  if (!finalName) {
    const sample = await prisma.candidateInvite.findFirst({
      where: { candidateEmail: newEmail },
      select: { candidateName: true },
    });
    finalName = sample?.candidateName ?? "";
  }

  return {
    email: newEmail!,
    name: finalName,
    invitesUpdated: invitesUpdated.count,
    sessionsUpdated: sessionsUpdated.count,
  };
}

// ─── create_candidate_invite (shared internals) ────────────────────
//
// Extracted so create_candidate_invite (single) and bulk_create_candidate_invites
// can share validation + write logic. The MCP-level handler still owns the
// audit log and the user-facing "notice" message.

export interface CreateInviteInput {
  email: string;
  name: string;
  assessmentId: string;
  expiresInDays?: number;
  externalId?: string | null;
}

export interface CreateInviteResult {
  invite: InviteRecord;
  idempotent: boolean;
}

export async function createInvite(input: CreateInviteInput): Promise<CreateInviteResult> {
  const { email, name, assessmentId, expiresInDays = 7, externalId } = input;
  if (!email || !name || !assessmentId) {
    throw new McpValidationError("email, name, assessmentId required");
  }

  if (externalId) {
    const hit = await findByExternalId("candidate_invite", externalId);
    if (hit) {
      const full = await prisma.candidateInvite.findUnique({
        where: { id: hit.id },
        include: { template: { select: { title: true } } },
      });
      if (full) return { invite: toInviteRecord(full), idempotent: true };
    }
  }

  const template = await prisma.assessmentTemplate.findUnique({
    where: { id: assessmentId },
    select: { id: true, title: true, isActive: true },
  });
  if (!template) throw new McpValidationError(`assessment not found: ${assessmentId}`);
  if (!template.isActive) {
    throw new McpValidationError(
      `assessment "${template.title}" is a draft (inactive). Activate it before inviting.`
    );
  }

  const existing = await prisma.candidateInvite.findFirst({
    where: {
      candidateEmail: email.toLowerCase(),
      templateId: assessmentId,
      status: { in: ["pending", "started"] },
    },
  });
  if (existing) {
    throw new McpValidationError(
      `duplicate: ${email} already has a ${existing.status} invite for "${template.title}" (code: ${existing.code}). Revoke the existing invite first.`
    );
  }

  const code = nanoid(16);
  const expiresAt = new Date(Date.now() + expiresInDays * 86400000);
  const invite = await prisma.candidateInvite.create({
    data: {
      code,
      candidateEmail: email.toLowerCase(),
      candidateName: name,
      templateId: assessmentId,
      expiresAt,
      status: "pending",
      ...(externalId ? { externalId } : {}),
    },
    include: { template: { select: { title: true } } },
  });

  return { invite: toInviteRecord(invite), idempotent: false };
}

// ─── bulk_create_candidate_invites ────────────────────────────────
//
// Sequential per-candidate so partial success is reportable. NOT wrapped in
// a single transaction. Returns one row per input candidate with either
// {ok:true, inviteId} or {ok:false, error}.

export interface BulkInviteCandidate {
  email: string;
  name: string;
  expiresInDays?: number;
  externalId?: string;
}

export interface BulkInviteInput {
  assessmentId: string;
  candidates: BulkInviteCandidate[];
  sendEmail?: boolean;
}

export interface BulkInviteRowResult {
  email: string;
  ok: boolean;
  inviteId?: string;
  inviteLink?: string;
  externalId?: string | null;
  idempotent?: boolean;
  emailSent?: boolean;
  error?: string;
}

export interface BulkInviteSummary {
  results: BulkInviteRowResult[];
  successCount: number;
  failureCount: number;
}

export async function bulkCreateInvites(input: BulkInviteInput): Promise<BulkInviteSummary> {
  if (!input.assessmentId) throw new McpValidationError("assessmentId required");
  if (!Array.isArray(input.candidates) || input.candidates.length === 0) {
    throw new McpValidationError("candidates must be a non-empty array");
  }
  if (input.candidates.length > 200) {
    throw new McpValidationError("bulk_create_candidate_invites: max 200 candidates per call");
  }

  const template = await prisma.assessmentTemplate.findUnique({
    where: { id: input.assessmentId },
    include: { jobRole: { include: { department: true } } },
  });
  if (!template) throw new McpValidationError(`assessment not found: ${input.assessmentId}`);

  const results: BulkInviteRowResult[] = [];
  for (const c of input.candidates) {
    try {
      const { invite, idempotent } = await createInvite({
        email: c.email,
        name: c.name,
        assessmentId: input.assessmentId,
        expiresInDays: c.expiresInDays,
        externalId: c.externalId,
      });

      let emailSent = false;
      if (input.sendEmail && !idempotent) {
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
          console.error(`[invites] bulk email to ${c.email} failed:`, e);
        }
      }

      results.push({
        email: c.email,
        ok: true,
        inviteId: invite.id,
        inviteLink: invite.inviteLink,
        externalId: invite.externalId,
        idempotent,
        emailSent,
      });
    } catch (e) {
      results.push({
        email: c.email,
        ok: false,
        error: e instanceof Error ? e.message : String(e),
      });
    }
  }

  return {
    results,
    successCount: results.filter((r) => r.ok).length,
    failureCount: results.filter((r) => !r.ok).length,
  };
}

```