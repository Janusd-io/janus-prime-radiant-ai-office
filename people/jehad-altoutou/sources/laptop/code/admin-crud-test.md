---
type: source
source_type: laptop
title: admin_crud.test
slug: admin-crud-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/admin_crud.test.ts
original_size: 5043
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# admin_crud.test

_Extracted from `[[assessify|assessify]]/src/lib/mcp/__tests__/admin_crud.test.ts` on 2026-05-14._

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

function parseJson(result: { content: Array<{ text: string }>; isError?: boolean }) {
  return JSON.parse(result.content[0].text);
}

describe("competencies CRUD", () => {
  it("creates with auto-slug, updates, and archives", async () => {
    const created = parseJson(
      await callTool(
        "create_competency",
        { name: "Customer Empathy", description: "Cares about users" },
        makeMcpSession(),
        null
      )
    );
    expect(created.id).toBeTruthy();
    expect(created.slug).toBe("customer-empathy");

    const updated = parseJson(
      await callTool(
        "update_competency",
        { id: created.id, description: "Cares deeply" },
        makeMcpSession(),
        null
      )
    );
    expect(updated.description).toBe("Cares deeply");

    const archived = parseJson(
      await callTool("archive_competency", { id: created.id }, makeMcpSession(), null)
    );
    expect(archived.archivedAt).toBeTruthy();
  });

  it("refuses archive when an active question is still tagged", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const a = await makeAssessment(role.id);
    const comp = await makeCompetency();
    await prisma.questionCompetency.create({
      data: { questionId: a.sections[0].questions[0].id, competencyId: comp.id, weight: 1.0 },
    });

    const r = await callTool("archive_competency", { id: comp.id }, makeMcpSession(), null);
    expect(r.isError).toBe(true);
    expect(r.content[0].text).toMatch(/still tagged/i);
  });

  it("disambiguates slug on duplicate name", async () => {
    const a = parseJson(
      await callTool("create_competency", { name: "Communication" }, makeMcpSession(), null)
    );
    const b = parseJson(
      await callTool("create_competency", { name: "Communication" }, makeMcpSession(), null)
    );
    expect(a.slug).not.toBe(b.slug);
  });
});

describe("departments CRUD", () => {
  it("creates, updates, archives", async () => {
    const created = parseJson(
      await callTool("create_department", { name: "Marketing" }, makeMcpSession(), null)
    );
    expect(created.slug).toBe("marketing");

    const updated = parseJson(
      await callTool(
        "update_department",
        { id: created.id, description: "B2B and brand" },
        makeMcpSession(),
        null
      )
    );
    expect(updated.description).toBe("B2B and brand");

    const archived = parseJson(
      await callTool("archive_department", { id: created.id }, makeMcpSession(), null)
    );
    expect(archived.archivedAt).toBeTruthy();
  });

  it("refuses archive when an active job role exists", async () => {
    const dept = await makeDepartment();
    await makeJobRole(dept.id); // isActive true by default
    const r = await callTool("archive_department", { id: dept.id }, makeMcpSession(), null);
    expect(r.isError).toBe(true);
    expect(r.content[0].text).toMatch(/active job role/i);
  });
});

describe("job roles update + archive", () => {
  it("updates title and reassigns department", async () => {
    const d1 = await makeDepartment();
    const d2 = await makeDepartment();
    const role = await makeJobRole(d1.id, { title: "Engineer" });

    const r = parseJson(
      await callTool(
        "update_job_role",
        { id: role.id, title: "Senior Engineer", departmentId: d2.id },
        makeMcpSession(),
        null
      )
    );
    expect(r.title).toBe("Senior Engineer");
    expect(r.departmentId).toBe(d2.id);
  });

  it("refuses reassign to an archived department", async () => {
    const d1 = await makeDepartment();
    const d2 = await makeDepartment();
    await prisma.department.update({ where: { id: d2.id }, data: { archivedAt: new Date() } });
    const role = await makeJobRole(d1.id);
    const r = await callTool(
      "update_job_role",
      { id: role.id, departmentId: d2.id },
      makeMcpSession(),
      null
    );
    expect(r.isError).toBe(true);
  });

  it("archives a job role with no active assessments", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const r = parseJson(await callTool("archive_job_role", { id: role.id }, makeMcpSession(), null));
    expect(r.isActive).toBe(false);
  });

  it("refuses archive when an active assessment references it", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const a = await makeAssessment(role.id);
    await prisma.assessmentTemplate.update({ where: { id: a.template.id }, data: { isActive: true } });
    const r = await callTool("archive_job_role", { id: role.id }, makeMcpSession(), null);
    expect(r.isError).toBe(true);
    expect(r.content[0].text).toMatch(/active assessment/i);
  });
});

```