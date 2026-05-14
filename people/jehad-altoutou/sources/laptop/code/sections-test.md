---
type: source
source_type: laptop
title: sections.test
slug: sections-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/sections.test.ts
original_size: 9307
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# sections.test

_Extracted from `assessify/src/lib/mcp/__tests__/sections.test.ts` on 2026-05-14._

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

function parseToolJson(result: { content: Array<{ text: string }>; isError?: boolean }) {
  return JSON.parse(result.content[0].text);
}

async function setupAssessment() {
  const dept = await makeDepartment();
  const role = await makeJobRole(dept.id);
  return makeAssessment(role.id);
}

describe("add_section", () => {
  it("appends a new section at the end by default", async () => {
    const { template, sections } = await setupAssessment();
    const result = await callTool(
      "add_section",
      { assessmentId: template.id, title: "Section C", weight: 0.0 },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();
    const data = parseToolJson(result);
    expect(data.title).toBe("Section C");
    expect(data.sortOrder).toBe(sections.length);
  });

  it("inserts at a specific sortOrder and shifts others", async () => {
    const { template } = await setupAssessment();
    await callTool(
      "add_section",
      { assessmentId: template.id, title: "Inserted", weight: 0.0, sortOrder: 0 },
      makeMcpSession(),
      null
    );
    const all = await prisma.section.findMany({
      where: { version: { templateId: template.id } },
      orderBy: { sortOrder: "asc" },
    });
    expect(all[0].title).toBe("Inserted");
    expect(all.length).toBe(3);
  });

  it("rejects weight outside 0..1", async () => {
    const { template } = await setupAssessment();
    const result = await callTool(
      "add_section",
      { assessmentId: template.id, title: "Bad", weight: 1.5 },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/section weight/);
  });

  it("rejects unknown assessment", async () => {
    const result = await callTool(
      "add_section",
      { assessmentId: "missing", title: "Bad", weight: 0.5 },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/assessment not found/);
  });

  it("denies non-admins", async () => {
    const { template } = await setupAssessment();
    const result = await callTool(
      "add_section",
      { assessmentId: template.id, title: "X", weight: 0.5 },
      makeMcpSession({ role: "user" }),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/permission_denied/);
  });

  it("dedupes the slug on title collision", async () => {
    const { template } = await setupAssessment();
    await callTool(
      "add_section",
      { assessmentId: template.id, title: "Dup", weight: 0.0 },
      makeMcpSession(),
      null
    );
    const second = await callTool(
      "add_section",
      { assessmentId: template.id, title: "Dup", weight: 0.0 },
      makeMcpSession(),
      null
    );
    expect(second.isError).toBeFalsy();
    const data = parseToolJson(second);
    expect(data.slug).toBe("dup-2");
  });
});

describe("update_section", () => {
  it("updates title without touching weight", async () => {
    const { sections } = await setupAssessment();
    const before = sections[0].weight;
    await callTool(
      "update_section",
      { sectionId: sections[0].id, title: "Renamed" },
      makeMcpSession(),
      null
    );
    const fresh = await prisma.section.findUnique({ where: { id: sections[0].id } });
    expect(fresh?.title).toBe("Renamed");
    expect(fresh?.weight).toBe(before);
  });

  it("rejects unknown section", async () => {
    const result = await callTool(
      "update_section",
      { sectionId: "missing", title: "X" },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/section not found/);
  });
});

describe("remove_section", () => {
  it("deletes the section and cascades questions", async () => {
    const { sections } = await setupAssessment();
    const sectionA = sections[0];
    await callTool(
      "remove_section",
      { sectionId: sectionA.id },
      makeMcpSession(),
      null
    );
    expect(await prisma.section.findUnique({ where: { id: sectionA.id } })).toBeNull();
    expect(await prisma.question.count({ where: { sectionId: sectionA.id } })).toBe(0);
  });

  it("refuses if any candidate has answered the section", async () => {
    const { sections } = await setupAssessment();
    const sectionA = sections[0];
    const q = sectionA.questions[0];

    // Manually create a session+response that references the section's question
    const tmpl = await prisma.assessmentTemplate.findFirst();
    const version = await prisma.assessmentVersion.findFirst({ where: { templateId: tmpl!.id } });
    const session = await prisma.candidateSession.create({
      data: {
        versionId: version!.id,
        candidateName: "Test",
        candidateEmail: "t@test",
        status: "in_progress",
      },
    });
    await prisma.candidateResponse.create({
      data: {
        sessionId: session.id,
        sectionId: sectionA.id,
        questionId: q.id,
        answerPayload: JSON.stringify({ a: "b" }),
        maxPoints: 1,
      },
    });

    const result = await callTool(
      "remove_section",
      { sectionId: sectionA.id },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/candidate response/);
    expect(await prisma.section.findUnique({ where: { id: sectionA.id } })).not.toBeNull();
  });
});

describe("reorder_sections", () => {
  it("reorders all sections by ID", async () => {
    const { template, sections } = await setupAssessment();
    const reversed = [sections[1].id, sections[0].id];
    const result = await callTool(
      "reorder_sections",
      { assessmentId: template.id, orderedSectionIds: reversed },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();
    const fresh = await prisma.section.findMany({
      where: { version: { templateId: template.id } },
      orderBy: { sortOrder: "asc" },
    });
    expect(fresh.map((s) => s.id)).toEqual(reversed);
  });

  it("rejects partial section list", async () => {
    const { template, sections } = await setupAssessment();
    const result = await callTool(
      "reorder_sections",
      { assessmentId: template.id, orderedSectionIds: [sections[0].id] },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/exactly once/);
  });

  it("rejects foreign section ID", async () => {
    const { template, sections } = await setupAssessment();
    const result = await callTool(
      "reorder_sections",
      {
        assessmentId: template.id,
        orderedSectionIds: [sections[0].id, "outside"],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
  });
});

describe("set_section_weights", () => {
  it("atomically sets weights when sum=1.0", async () => {
    const { template, sections } = await setupAssessment();
    const result = await callTool(
      "set_section_weights",
      {
        assessmentId: template.id,
        weights: [
          { sectionId: sections[0].id, weight: 0.3 },
          { sectionId: sections[1].id, weight: 0.7 },
        ],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();
    const fresh = await prisma.section.findMany({
      where: { version: { templateId: template.id } },
    });
    const map = new Map(fresh.map((s) => [s.id, s.weight]));
    expect(map.get(sections[0].id)).toBe(0.3);
    expect(map.get(sections[1].id)).toBe(0.7);
  });

  it("rejects weights that don't sum to 1.0", async () => {
    const { template, sections } = await setupAssessment();
    const result = await callTool(
      "set_section_weights",
      {
        assessmentId: template.id,
        weights: [
          { sectionId: sections[0].id, weight: 0.5 },
          { sectionId: sections[1].id, weight: 0.4 }, // sum 0.9
        ],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/sum to 1\.0/);
  });

  it("rejects when not every section is provided", async () => {
    const { template, sections } = await setupAssessment();
    const result = await callTool(
      "set_section_weights",
      {
        assessmentId: template.id,
        weights: [{ sectionId: sections[0].id, weight: 1.0 }],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/every section/);
  });

  it("rejects duplicate sectionIds in input", async () => {
    const { template, sections } = await setupAssessment();
    const result = await callTool(
      "set_section_weights",
      {
        assessmentId: template.id,
        weights: [
          { sectionId: sections[0].id, weight: 0.5 },
          { sectionId: sections[0].id, weight: 0.5 },
        ],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
  });
});

```