---
type: source
source_type: laptop
title: update_assessment.test
slug: update-assessment-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/update_assessment.test.ts
original_size: 7380
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# update_assessment.test

_Extracted from `[[assessify|assessify]]/src/lib/mcp/__tests__/update_assessment.test.ts` on 2026-05-14._

```typescript
import { describe, expect, it } from "vitest";
import { prisma } from "@/lib/db";
import { callTool } from "@/lib/mcp/tools";
import {
  makeAssessment,
  makeCompetency,
  makeDepartment,
  makeJobRole,
  makeMcpSession,
} from "../../../../tests/factories";

function parseToolJson(result: { content: Array<{ text: string }>; isError?: boolean }) {
  return JSON.parse(result.content[0].text);
}

describe("update_assessment", () => {
  it("updates title + description on the template", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const { template } = await makeAssessment(role.id);

    const result = await callTool(
      "update_assessment",
      { id: template.id, title: "Renamed", description: "New blurb" },
      makeMcpSession(),
      null
    );

    expect(result.isError).toBeFalsy();
    const data = parseToolJson(result);
    expect(data.title).toBe("Renamed");
    expect(data.description).toBe("New blurb");

    const fresh = await prisma.assessmentTemplate.findUnique({ where: { id: template.id } });
    expect(fresh?.title).toBe("Renamed");
  });

  it("updates timeLimit + passingScore on the latest version", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const { template, version } = await makeAssessment(role.id);

    await callTool(
      "update_assessment",
      { id: template.id, timeLimit: 60, passingScore: 0.8 },
      makeMcpSession(),
      null
    );

    const fresh = await prisma.assessmentVersion.findUnique({ where: { id: version.id } });
    expect(fresh?.timeLimit).toBe(60);
    expect(fresh?.passingScore).toBe(0.8);
  });

  it("stores recommendation thresholds as JSON on the latest version", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const { template, version } = await makeAssessment(role.id);

    const result = await callTool(
      "update_assessment",
      {
        id: template.id,
        thresholds: { strongHire: 0.9, hire: 0.75, consider: 0.6 },
      },
      makeMcpSession(),
      null
    );

    expect(result.isError).toBeFalsy();
    const fresh = await prisma.assessmentVersion.findUnique({ where: { id: version.id } });
    expect(fresh?.recommendationThresholds).toBeTruthy();
    const parsed = JSON.parse(fresh!.recommendationThresholds!);
    expect(parsed).toEqual({ strongHire: 0.9, hire: 0.75, consider: 0.6 });
  });

  it("rejects thresholds out of order (validation)", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const { template } = await makeAssessment(role.id);

    const result = await callTool(
      "update_assessment",
      {
        id: template.id,
        // hire > strongHire — invalid
        thresholds: { strongHire: 0.5, hire: 0.7, consider: 0.6 },
      },
      makeMcpSession(),
      null
    );

    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/strongHire > hire > consider/);
  });

  it("rejects passingScore outside 0..1", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const { template } = await makeAssessment(role.id);

    const result = await callTool(
      "update_assessment",
      { id: template.id, passingScore: 1.5 },
      makeMcpSession(),
      null
    );

    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/passingScore/);
  });

  it("rejects unknown jobRoleId", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const { template } = await makeAssessment(role.id);

    const result = await callTool(
      "update_assessment",
      { id: template.id, jobRoleId: "nonexistent" },
      makeMcpSession(),
      null
    );

    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/jobRole not found/);
  });

  it("rejects unknown assessment id", async () => {
    const result = await callTool(
      "update_assessment",
      { id: "nonexistent" },
      makeMcpSession(),
      null
    );

    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/assessment not found/);
  });

  it("denies non-admin callers", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const { template } = await makeAssessment(role.id);

    const result = await callTool(
      "update_assessment",
      { id: template.id, title: "Should not apply" },
      makeMcpSession({ role: "user" }),
      null
    );

    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/permission_denied/);

    const fresh = await prisma.assessmentTemplate.findUnique({ where: { id: template.id } });
    expect(fresh?.title).toBe(template.title);
  });

  it("writes an audit log entry on success", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const { template } = await makeAssessment(role.id);
    const session = makeMcpSession({ userEmail: "auditor@test.local" });

    await callTool(
      "update_assessment",
      { id: template.id, title: "Audited" },
      session,
      "127.0.0.1"
    );

    const log = await prisma.auditLog.findFirst({
      where: { action: "mcp.assessment.updated", targetId: template.id },
    });
    expect(log).toBeTruthy();
    expect(log?.userEmail).toBe("auditor@test.local");
    expect(log?.ipAddress).toBe("127.0.0.1");
  });

  // Future: when create_question / attach lands, this test should also verify
  // that competencyIds on the question are validated. Touched here so we don't
  // forget.
  it("toggles eggHuntEnabled on the template", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const { template } = await makeAssessment(role.id);

    expect(template.eggHuntEnabled).toBe(false);

    await callTool(
      "update_assessment",
      { id: template.id, eggHuntEnabled: true },
      makeMcpSession(),
      null
    );
    let fresh = await prisma.assessmentTemplate.findUnique({ where: { id: template.id } });
    expect(fresh?.eggHuntEnabled).toBe(true);

    await callTool(
      "update_assessment",
      { id: template.id, eggHuntEnabled: false },
      makeMcpSession(),
      null
    );
    fresh = await prisma.assessmentTemplate.findUnique({ where: { id: template.id } });
    expect(fresh?.eggHuntEnabled).toBe(false);
  });

  it("noop is harmless (no fields beyond id)", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const { template } = await makeAssessment(role.id);

    const result = await callTool("update_assessment", { id: template.id }, makeMcpSession(), null);

    expect(result.isError).toBeFalsy();
    const data = parseToolJson(result);
    expect(data.id).toBe(template.id);
  });

  it("ignores foreign keys for unrelated competencies (sanity)", async () => {
    // Just confirms the test infra cleans up between tests and competencies
    // from previous tests don't leak into this one.
    const before = await prisma.competency.count();
    expect(before).toBe(0);
    await makeCompetency();
    expect(await prisma.competency.count()).toBe(1);
  });
});

```