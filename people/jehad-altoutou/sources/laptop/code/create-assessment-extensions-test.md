---
type: source
source_type: laptop
title: create_assessment_extensions.test
slug: create-assessment-extensions-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/create_assessment_extensions.test.ts
original_size: 4958
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# create_assessment_extensions.test

_Extracted from `[[assessify|assessify]]/src/lib/mcp/__tests__/create_assessment_extensions.test.ts` on 2026-05-14._

```typescript
import { describe, expect, it } from "vitest";
import { prisma } from "@/lib/db";
import { callTool } from "@/lib/mcp/tools";
import {
  makeCompetency,
  makeDepartment,
  makeJobRole,
  makeMcpSession,
} from "../../../../tests/factories";

function parseToolJson(result: { content: Array<{ text: string }>; isError?: boolean }) {
  return JSON.parse(result.content[0].text);
}

describe("create_assessment — competencyIds + thresholds extension", () => {
  it("persists thresholds on the latest version", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const result = await callTool(
      "create_assessment",
      {
        jobRoleId: role.id,
        title: "With Thresholds",
        thresholds: { strongHire: 0.85, hire: 0.7, consider: 0.55 },
        sections: [{ title: "Only", weight: 1.0 }],
        questions: [{ sectionIndex: 0, prompt: "Q1", questionType: "short_text" }],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();
    const data = parseToolJson(result);

    const version = await prisma.assessmentVersion.findFirst({
      where: { templateId: data.id },
    });
    expect(version?.recommendationThresholds).toBeTruthy();
    expect(JSON.parse(version!.recommendationThresholds!)).toEqual({
      strongHire: 0.85,
      hire: 0.7,
      consider: 0.55,
    });
  });

  it("rejects thresholds out of order", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const result = await callTool(
      "create_assessment",
      {
        jobRoleId: role.id,
        title: "Bad Thresholds",
        thresholds: { strongHire: 0.5, hire: 0.7, consider: 0.6 },
        sections: [{ title: "Only", weight: 1.0 }],
        questions: [],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/strongHire > hire > consider/);
  });

  it("attaches competencies to questions on creation", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const c1 = await makeCompetency({ name: "Comm" });
    const c2 = await makeCompetency({ name: "Tech" });

    const result = await callTool(
      "create_assessment",
      {
        jobRoleId: role.id,
        title: "Tagged",
        sections: [{ title: "Only", weight: 1.0 }],
        questions: [
          {
            sectionIndex: 0,
            prompt: "Q",
            questionType: "single_select",
            options: [
              { label: "R", points: 1 },
              { label: "W", points: 0 },
            ],
            competencyIds: [c1.id, c2.id],
          },
        ],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();
    const data = parseToolJson(result);

    const created = await prisma.question.findFirst({
      where: { section: { version: { templateId: data.id } } },
      include: { competencies: true },
    });
    expect(created?.competencies.map((c) => c.competencyId).sort()).toEqual([c1.id, c2.id].sort());
  });

  it("rejects unknown competencyId surfaced before any DB writes", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const before = await prisma.assessmentTemplate.count();

    const result = await callTool(
      "create_assessment",
      {
        jobRoleId: role.id,
        title: "Should not persist",
        sections: [{ title: "Only", weight: 1.0 }],
        questions: [
          {
            sectionIndex: 0,
            prompt: "Q",
            questionType: "short_text",
            competencyIds: ["nonexistent"],
          },
        ],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/competency not found/);
    // The pre-validation must have prevented the template from being created.
    expect(await prisma.assessmentTemplate.count()).toBe(before);
  });
});

describe("update_thresholds (P1 thin wrapper)", () => {
  it("sets thresholds on an existing assessment", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const created = await callTool(
      "create_assessment",
      {
        jobRoleId: role.id,
        title: "T",
        sections: [{ title: "S", weight: 1.0 }],
        questions: [],
      },
      makeMcpSession(),
      null
    );
    const data = parseToolJson(created);

    const result = await callTool(
      "update_thresholds",
      { assessmentId: data.id, strongHire: 0.9, hire: 0.75, consider: 0.6 },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();

    const log = await prisma.auditLog.findFirst({
      where: { action: "mcp.assessment.thresholds_updated", targetId: data.id },
    });
    expect(log).toBeTruthy();
  });
});

```