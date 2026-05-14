---
type: source
source_type: laptop
title: invites.test
slug: invites-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/invites.test.ts
original_size: 9606
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# invites.test

_Extracted from `[[assessify|assessify]]/src/lib/mcp/__tests__/invites.test.ts` on 2026-05-14._

```typescript
import { describe, expect, it } from "vitest";
import { prisma } from "@/lib/db";
import { callTool } from "@/lib/mcp/tools";
import {
  makeAssessment,
  makeDepartment,
  makeJobRole,
  makeMcpSession,
} from "../../../../tests/factories";

function parseJson(result: { content: Array<{ text: string }>; isError?: boolean }) {
  return JSON.parse(result.content[0].text);
}

async function setup() {
  const dept = await makeDepartment();
  const role = await makeJobRole(dept.id);
  const a = await makeAssessment(role.id);
  // Activate so create_candidate_invite is accepted
  await prisma.assessmentTemplate.update({
    where: { id: a.template.id },
    data: { isActive: true },
  });
  return { dept, role, ...a };
}

async function makeInvite(templateId: string, overrides: Partial<{ email: string; name: string; status: string }> = {}) {
  return prisma.candidateInvite.create({
    data: {
      code: `code-${Math.random().toString(36).slice(2, 12)}`,
      candidateEmail: overrides.email ?? "alice@test.local",
      candidateName: overrides.name ?? "Alice",
      templateId,
      status: overrides.status ?? "pending",
      expiresAt: new Date(Date.now() + 7 * 86400000),
    },
  });
}

describe("get_invite", () => {
  it("returns full state including the invite link", async () => {
    const { template } = await setup();
    const invite = await makeInvite(template.id, { email: "alice@test.local" });
    const session = makeMcpSession();
    const r = parseJson(await callTool("get_invite", { inviteId: invite.id }, session, null));
    expect(r.id).toBe(invite.id);
    expect(r.candidateEmail).toBe("alice@test.local");
    expect(r.assessmentTitle).toBe(template.title);
    expect(r.inviteLink).toMatch(/\/assess\/invite\//);
    expect(r.status).toBe("pending");
  });

  it("denies non-admin", async () => {
    const r = await callTool("get_invite", { inviteId: "x" }, makeMcpSession({ role: "viewer" }), null);
    expect(r.isError).toBe(true);
    expect(r.content[0].text).toMatch(/admin/i);
  });
});

describe("list_invites", () => {
  it("paginates with cursor and filters by status", async () => {
    const { template } = await setup();
    for (let i = 0; i < 3; i++) {
      await makeInvite(template.id, { email: `c${i}@test.local`, status: "pending" });
    }
    await makeInvite(template.id, { email: "revoked@test.local", status: "revoked" });

    const session = makeMcpSession();
    const all = parseJson(await callTool("list_invites", { assessmentId: template.id, limit: 2 }, session, null));
    expect(all.invites).toHaveLength(2);
    expect(all.nextCursor).toBeTruthy();

    const next = parseJson(
      await callTool("list_invites", { assessmentId: template.id, limit: 2, cursor: all.nextCursor }, session, null)
    );
    expect(next.invites.length).toBeGreaterThanOrEqual(1);
    expect(next.nextCursor).toBeNull();

    const revokedOnly = parseJson(
      await callTool("list_invites", { assessmentId: template.id, status: "revoked" }, session, null)
    );
    expect(revokedOnly.invites).toHaveLength(1);
    expect(revokedOnly.invites[0].candidateEmail).toBe("revoked@test.local");
  });
});

describe("revoke_invite", () => {
  it("revokes a pending invite", async () => {
    const { template } = await setup();
    const invite = await makeInvite(template.id);
    const r = parseJson(await callTool("revoke_invite", { inviteId: invite.id }, makeMcpSession(), null));
    expect(r.status).toBe("revoked");
  });

  it("refuses to revoke an in-progress invite", async () => {
    const { template } = await setup();
    const invite = await makeInvite(template.id, { status: "started" });
    const r = await callTool("revoke_invite", { inviteId: invite.id }, makeMcpSession(), null);
    expect(r.isError).toBe(true);
    expect(r.content[0].text).toMatch(/in-progress|cannot revoke/i);
  });

  it("refuses to revoke a completed invite", async () => {
    const { template } = await setup();
    const invite = await makeInvite(template.id, { status: "completed" });
    const r = await callTool("revoke_invite", { inviteId: invite.id }, makeMcpSession(), null);
    expect(r.isError).toBe(true);
  });
});

describe("resend_invite", () => {
  it("does not email by default and does not change expiry without newExpiryDays", async () => {
    const { template } = await setup();
    const original = await makeInvite(template.id);
    const originalExpiry = original.expiresAt!.getTime();
    const r = parseJson(await callTool("resend_invite", { inviteId: original.id }, makeMcpSession(), null));
    expect(r.emailSent).toBe(false);
    expect(new Date(r.expiresAt).getTime()).toBe(originalExpiry);
  });

  it("extends expiry when newExpiryDays is provided", async () => {
    const { template } = await setup();
    const invite = await makeInvite(template.id);
    const r = parseJson(
      await callTool("resend_invite", { inviteId: invite.id, newExpiryDays: 30 }, makeMcpSession(), null)
    );
    const ms = new Date(r.expiresAt).getTime() - Date.now();
    expect(ms).toBeGreaterThan(28 * 86400000);
    expect(ms).toBeLessThan(31 * 86400000);
  });

  it("refuses to resend completed or revoked invites", async () => {
    const { template } = await setup();
    const completed = await makeInvite(template.id, { status: "completed" });
    const revoked = await makeInvite(template.id, { email: "b@test.local", status: "revoked" });
    expect((await callTool("resend_invite", { inviteId: completed.id }, makeMcpSession(), null)).isError).toBe(true);
    expect((await callTool("resend_invite", { inviteId: revoked.id }, makeMcpSession(), null)).isError).toBe(true);
  });
});

describe("extend_invite_expiry", () => {
  it("pushes expiry without sending email", async () => {
    const { template } = await setup();
    const invite = await makeInvite(template.id);
    const r = parseJson(
      await callTool("extend_invite_expiry", { inviteId: invite.id, expiresInDays: 14 }, makeMcpSession(), null)
    );
    const ms = new Date(r.expiresAt).getTime() - Date.now();
    expect(ms).toBeGreaterThan(13 * 86400000);
  });

  it("refuses zero or negative expiresInDays", async () => {
    const { template } = await setup();
    const invite = await makeInvite(template.id);
    const r = await callTool("extend_invite_expiry", { inviteId: invite.id, expiresInDays: 0 }, makeMcpSession(), null);
    expect(r.isError).toBe(true);
  });
});

describe("update_candidate", () => {
  it("renames pre-completion across invites and sessions", async () => {
    const { template, version } = await setup();
    await makeInvite(template.id, { email: "old@test.local", name: "Old Name" });
    await prisma.candidateSession.create({
      data: {
        versionId: version.id,
        candidateEmail: "old@test.local",
        candidateName: "Old Name",
        status: "in_progress",
      },
    });

    const r = parseJson(
      await callTool(
        "update_candidate",
        { candidateEmail: "old@test.local", name: "New Name", email: "new@test.local" },
        makeMcpSession(),
        null
      )
    );
    expect(r.email).toBe("new@test.local");
    expect(r.invitesUpdated).toBe(1);
    expect(r.sessionsUpdated).toBe(1);

    const inv = await prisma.candidateInvite.findFirst({ where: { candidateEmail: "new@test.local" } });
    expect(inv?.candidateName).toBe("New Name");
  });

  it("refuses post-completion edits", async () => {
    const { template, version } = await setup();
    await makeInvite(template.id, { email: "done@test.local" });
    await prisma.candidateSession.create({
      data: {
        versionId: version.id,
        candidateEmail: "done@test.local",
        candidateName: "Done",
        status: "completed",
      },
    });
    const r = await callTool(
      "update_candidate",
      { candidateEmail: "done@test.local", name: "Cannot" },
      makeMcpSession(),
      null
    );
    expect(r.isError).toBe(true);
    expect(r.content[0].text).toMatch(/audit integrity/i);
  });
});

describe("bulk_create_candidate_invites", () => {
  it("creates several invites and reports per-row results", async () => {
    const { template } = await setup();
    const r = parseJson(
      await callTool(
        "bulk_create_candidate_invites",
        {
          assessmentId: template.id,
          candidates: [
            { email: "one@test.local", name: "One" },
            { email: "two@test.local", name: "Two" },
          ],
        },
        makeMcpSession(),
        null
      )
    );
    expect(r.successCount).toBe(2);
    expect(r.failureCount).toBe(0);
    expect(r.results).toHaveLength(2);
    expect(r.results[0].ok).toBe(true);
    expect(r.results[0].inviteLink).toMatch(/\/assess\/invite\//);
  });

  it("reports failures per row without aborting the rest", async () => {
    const { template } = await setup();
    // Pre-existing pending invite for one@test.local will collide
    await makeInvite(template.id, { email: "one@test.local" });
    const r = parseJson(
      await callTool(
        "bulk_create_candidate_invites",
        {
          assessmentId: template.id,
          candidates: [
            { email: "one@test.local", name: "Dup" },
            { email: "two@test.local", name: "Two" },
          ],
        },
        makeMcpSession(),
        null
      )
    );
    expect(r.successCount).toBe(1);
    expect(r.failureCount).toBe(1);
    const fail = r.results.find((x: { email: string }) => x.email === "one@test.local");
    expect(fail.ok).toBe(false);
    expect(fail.error).toMatch(/duplicate|already/i);
  });
});

```