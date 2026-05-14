---
type: source
source_type: laptop
title: sessions_read.test
slug: sessions-read-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/sessions_read.test.ts
original_size: 8273
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# sessions_read.test

_Extracted from `[[assessify|assessify]]/src/lib/mcp/__tests__/sessions_read.test.ts` on 2026-05-14._

```typescript
import { describe, expect, it } from "vitest";
import { prisma } from "@/lib/db";
import { callTool } from "@/lib/mcp/tools";
import {
  makeAssessment,
  makeDepartment,
  makeJobRole,
  makeMcpSession,
  makeSession,
} from "../../../../tests/factories";

function parseToolJson(result: { content: Array<{ text: string }>; isError?: boolean }) {
  return JSON.parse(result.content[0].text);
}

async function setup() {
  const dept = await makeDepartment();
  const role = await makeJobRole(dept.id);
  const a = await makeAssessment(role.id);
  return { dept, role, ...a };
}

describe("get_session", () => {
  it("returns full session detail with responses + scores", async () => {
    const { version, sections } = await setup();
    const session = await makeSession({
      versionId: version.id,
      withResult: { totalScore: 7, maxScore: 10, normalizedScore: 0.7, recommendation: "hire" },
    });
    await prisma.candidateResponse.create({
      data: {
        sessionId: session.id,
        sectionId: sections[0].id,
        questionId: sections[0].questions[0].id,
        answerPayload: JSON.stringify({ a: "b" }),
        earnedPoints: 1,
        maxPoints: 1,
        normalizedScore: 1,
        timeSpent: 30,
      },
    });

    const result = await callTool("get_session", { sessionId: session.id }, makeMcpSession(), null);
    expect(result.isError).toBeFalsy();
    const data = parseToolJson(result);
    expect(data.id).toBe(session.id);
    expect(data.result.recommendation).toBe("hire");
    expect(data.responses).toHaveLength(1);
    expect(data.totals.total).toBeGreaterThan(0);
  });

  it("denies non-admin", async () => {
    const { version } = await setup();
    const session = await makeSession({ versionId: version.id });
    const result = await callTool(
      "get_session",
      { sessionId: session.id },
      makeMcpSession({ role: "user" }),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/permission_denied/);
  });

  it("returns clear error for missing session", async () => {
    const result = await callTool(
      "get_session",
      { sessionId: "missing" },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/session not found/);
  });
});

describe("list_sessions", () => {
  it("returns sessions ordered by createdAt desc with cursor pagination", async () => {
    const { version } = await setup();
    for (let i = 0; i < 5; i++) {
      await makeSession({ versionId: version.id });
    }

    const page1 = await callTool(
      "list_sessions",
      { limit: 2 },
      makeMcpSession(),
      null
    );
    const d1 = parseToolJson(page1);
    expect(d1.sessions).toHaveLength(2);
    expect(d1.nextCursor).toBeTruthy();

    const page2 = await callTool(
      "list_sessions",
      { limit: 2, cursor: d1.nextCursor },
      makeMcpSession(),
      null
    );
    const d2 = parseToolJson(page2);
    expect(d2.sessions).toHaveLength(2);
    // Ensure no overlap
    const ids1 = new Set(d1.sessions.map((s: { id: string }) => s.id));
    for (const s of d2.sessions) expect(ids1.has(s.id)).toBe(false);

    const page3 = await callTool(
      "list_sessions",
      { limit: 2, cursor: d2.nextCursor },
      makeMcpSession(),
      null
    );
    const d3 = parseToolJson(page3);
    expect(d3.sessions).toHaveLength(1);
    expect(d3.nextCursor).toBeNull();
  });

  it("filters by recommendation tier", async () => {
    const { version } = await setup();
    await makeSession({
      versionId: version.id,
      withResult: { totalScore: 9, maxScore: 10, normalizedScore: 0.9, recommendation: "strong_hire" },
    });
    await makeSession({
      versionId: version.id,
      withResult: { totalScore: 4, maxScore: 10, normalizedScore: 0.4, recommendation: "reject" },
    });

    const result = await callTool(
      "list_sessions",
      { recommendation: "strong_hire" },
      makeMcpSession(),
      null
    );
    const data = parseToolJson(result);
    expect(data.sessions).toHaveLength(1);
    expect(data.sessions[0].recommendation).toBe("strong_hire");
  });

  it("filters by status", async () => {
    const { version } = await setup();
    await makeSession({ versionId: version.id, status: "completed" });
    await makeSession({ versionId: version.id, status: "in_progress" });

    const result = await callTool(
      "list_sessions",
      { status: "in_progress" },
      makeMcpSession(),
      null
    );
    const data = parseToolJson(result);
    expect(data.sessions).toHaveLength(1);
    expect(data.sessions[0].status).toBe("in_progress");
  });
});

describe("get_session_results", () => {
  it("returns scoring view with duration", async () => {
    const { version } = await setup();
    const start = new Date(Date.now() - 25 * 60 * 1000);
    const end = new Date();
    const session = await makeSession({
      versionId: version.id,
      startedAt: start,
      completedAt: end,
      withResult: { totalScore: 8, maxScore: 10, normalizedScore: 0.8, recommendation: "hire" },
    });

    const result = await callTool(
      "get_session_results",
      { sessionId: session.id },
      makeMcpSession(),
      null
    );
    const data = parseToolJson(result);
    expect(data.recommendation).toBe("hire");
    expect(data.durationMinutes).toBeGreaterThanOrEqual(20);
  });

  it("refuses if session has no result yet", async () => {
    const { version } = await setup();
    const session = await makeSession({ versionId: version.id, status: "in_progress" });
    const result = await callTool(
      "get_session_results",
      { sessionId: session.id },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/no result yet/);
  });
});

describe("export_sessions", () => {
  it("returns JSON rows by default", async () => {
    const { template, version } = await setup();
    await makeSession({
      versionId: version.id,
      withResult: { totalScore: 7, maxScore: 10, normalizedScore: 0.7, recommendation: "hire" },
    });
    const result = await callTool(
      "export_sessions",
      { assessmentId: template.id },
      makeMcpSession(),
      null
    );
    const data = parseToolJson(result);
    expect(data.format).toBe("json");
    expect(Array.isArray(data.data)).toBe(true);
    expect(data.data[0].recommendation).toBe("hire");
  });

  it("returns a CSV string when format=csv", async () => {
    const { template, version } = await setup();
    await makeSession({
      versionId: version.id,
      withResult: { totalScore: 7, maxScore: 10, normalizedScore: 0.7, recommendation: "hire" },
    });
    const result = await callTool(
      "export_sessions",
      { assessmentId: template.id, format: "csv" },
      makeMcpSession(),
      null
    );
    const data = parseToolJson(result);
    expect(data.format).toBe("csv");
    expect(typeof data.data).toBe("string");
    expect(data.data.split("\n")[0]).toMatch(/sessionId,inviteCode,candidateName/);
  });
});

describe("audit logging on results reads", () => {
  it("writes mcp.session.read on get_session", async () => {
    const { version } = await setup();
    const session = await makeSession({ versionId: version.id });
    const adminSession = makeMcpSession({ userEmail: "auditor@test.local" });

    await callTool("get_session", { sessionId: session.id }, adminSession, "10.0.0.1");

    const log = await prisma.auditLog.findFirst({
      where: { action: "mcp.session.read", targetId: session.id },
    });
    expect(log).toBeTruthy();
    expect(log?.userEmail).toBe("auditor@test.local");
    expect(log?.ipAddress).toBe("10.0.0.1");
  });

  it("does NOT include candidate names/emails in audit details for list", async () => {
    const { version } = await setup();
    await makeSession({ versionId: version.id, candidateEmail: "secret@candidate.test" });
    await callTool("list_sessions", { limit: 5 }, makeMcpSession(), null);

    const log = await prisma.auditLog.findFirst({ where: { action: "mcp.sessions.list" } });
    expect(log).toBeTruthy();
    expect(log?.details ?? "").not.toMatch(/secret@candidate\.test/);
  });
});

```