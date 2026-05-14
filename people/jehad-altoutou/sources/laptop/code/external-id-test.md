---
type: source
source_type: laptop
title: external_id.test
slug: external-id-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/external_id.test.ts
original_size: 3926
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# external_id.test

_Extracted from `assessify/src/lib/mcp/__tests__/external_id.test.ts` on 2026-05-14._

```typescript
import { describe, expect, it } from "vitest";
import { prisma } from "@/lib/db";
import { callTool } from "@/lib/mcp/tools";
import { makeDepartment, makeMcpSession } from "../../../../tests/factories";

function parseJson(result: { content: Array<{ text: string }>; isError?: boolean }) {
  return JSON.parse(result.content[0].text);
}

describe("idempotent create_competency", () => {
  it("returns the existing record when externalId matches", async () => {
    const first = parseJson(
      await callTool(
        "create_competency",
        { name: "Ownership", externalId: "ext-comp-1" },
        makeMcpSession(),
        null
      )
    );
    expect(first.idempotent).toBe(false);
    expect(first.externalId).toBe("ext-comp-1");

    const second = parseJson(
      await callTool(
        "create_competency",
        { name: "Different Name", externalId: "ext-comp-1" },
        makeMcpSession(),
        null
      )
    );
    expect(second.idempotent).toBe(true);
    expect(second.id).toBe(first.id);
    // The "Different Name" was ignored — original wins
    expect(second.name).toBe("Ownership");
  });

  it("only writes one audit row for an idempotent re-create", async () => {
    await callTool(
      "create_competency",
      { name: "Bias", externalId: "ext-bias" },
      makeMcpSession({ userEmail: "audit@test.local" }),
      null
    );
    await callTool(
      "create_competency",
      { name: "Bias", externalId: "ext-bias" },
      makeMcpSession({ userEmail: "audit@test.local" }),
      null
    );
    const auditCount = await prisma.auditLog.count({
      where: { action: "mcp.competency.created", userEmail: "audit@test.local" },
    });
    expect(auditCount).toBe(1);
  });
});

describe("idempotent create_department", () => {
  it("returns the existing record when externalId matches", async () => {
    const first = parseJson(
      await callTool(
        "create_department",
        { name: "Sales", externalId: "ext-dept-1" },
        makeMcpSession(),
        null
      )
    );
    const second = parseJson(
      await callTool(
        "create_department",
        { name: "Sales", externalId: "ext-dept-1" },
        makeMcpSession(),
        null
      )
    );
    expect(second.idempotent).toBe(true);
    expect(second.id).toBe(first.id);
  });
});

describe("idempotent create_job_role", () => {
  it("returns the existing record when externalId matches", async () => {
    const dept = await makeDepartment();
    const first = parseJson(
      await callTool(
        "create_job_role",
        { departmentId: dept.id, title: "Tester", externalId: "ext-role-1" },
        makeMcpSession(),
        null
      )
    );
    const second = parseJson(
      await callTool(
        "create_job_role",
        { departmentId: dept.id, title: "Tester", externalId: "ext-role-1" },
        makeMcpSession(),
        null
      )
    );
    expect(second.idempotent).toBe(true);
    expect(second.id).toBe(first.id);
  });
});

describe("lookup_by_external_id", () => {
  it("returns found:true with the record when present", async () => {
    const created = parseJson(
      await callTool(
        "create_department",
        { name: "Ops", externalId: "ext-ops" },
        makeMcpSession(),
        null
      )
    );
    const r = parseJson(
      await callTool(
        "lookup_by_external_id",
        { type: "department", externalId: "ext-ops" },
        makeMcpSession(),
        null
      )
    );
    expect(r.found).toBe(true);
    expect((r.record as { id: string }).id).toBe(created.id);
  });

  it("returns found:false when the externalId is unknown", async () => {
    const r = parseJson(
      await callTool(
        "lookup_by_external_id",
        { type: "department", externalId: "does-not-exist" },
        makeMcpSession(),
        null
      )
    );
    expect(r.found).toBe(false);
    expect(r.record).toBeNull();
  });
});

```