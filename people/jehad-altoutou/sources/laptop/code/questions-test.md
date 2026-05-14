---
type: source
source_type: laptop
title: questions.test
slug: questions-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/questions.test.ts
original_size: 10625
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# questions.test

_Extracted from `[[assessify|assessify]]/src/lib/mcp/__tests__/questions.test.ts` on 2026-05-14._

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

async function setupAssessment() {
  const dept = await makeDepartment();
  const role = await makeJobRole(dept.id);
  const a = await makeAssessment(role.id);
  return { dept, role, ...a };
}

describe("add_question", () => {
  it("creates an MCQ with options + competency tag", async () => {
    const { sections } = await setupAssessment();
    const comp = await makeCompetency({ name: "Communication" });
    const result = await callTool(
      "add_question",
      {
        sectionId: sections[1].id,
        prompt: "Pick the best response",
        questionType: "single_select",
        options: [
          { label: "Right", points: 1 },
          { label: "Wrong", points: 0 },
        ],
        competencyIds: [comp.id],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();
    const data = parseToolJson(result);
    expect(data.questionType).toBe("single_select");
    expect(data.options).toHaveLength(2);
    expect(data.options[0].key).toBe("a");
    expect(data.competencyIds).toEqual([comp.id]);
  });

  it("rejects MCQ without a correct option", async () => {
    const { sections } = await setupAssessment();
    const result = await callTool(
      "add_question",
      {
        sectionId: sections[1].id,
        prompt: "All wrong",
        questionType: "single_select",
        options: [
          { label: "Wrong A", points: 0 },
          { label: "Wrong B", points: 0 },
        ],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/at least one option with points > 0/);
  });

  it("rejects unknown competencyId", async () => {
    const { sections } = await setupAssessment();
    const result = await callTool(
      "add_question",
      {
        sectionId: sections[1].id,
        prompt: "Q",
        questionType: "short_text",
        competencyIds: ["nonexistent"],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/competency not found/);
  });

  it("denies non-admin", async () => {
    const { sections } = await setupAssessment();
    const result = await callTool(
      "add_question",
      { sectionId: sections[1].id, prompt: "Q", questionType: "short_text" },
      makeMcpSession({ role: "user" }),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/permission_denied/);
  });

  it("dedupes slug on duplicate titles", async () => {
    const { sections } = await setupAssessment();
    await callTool(
      "add_question",
      { sectionId: sections[1].id, prompt: "Same", title: "X", questionType: "short_text" },
      makeMcpSession(),
      null
    );
    const second = await callTool(
      "add_question",
      { sectionId: sections[1].id, prompt: "Same", title: "X", questionType: "short_text" },
      makeMcpSession(),
      null
    );
    expect(second.isError).toBeFalsy();
  });
});

describe("update_question", () => {
  it("replaces options when provided", async () => {
    const { sections } = await setupAssessment();
    const q = sections[0].questions[0];

    await callTool(
      "update_question",
      {
        questionId: q.id,
        options: [
          { label: "New Right", points: 2 },
          { label: "New Wrong", points: 0 },
          { label: "Also Wrong", points: 0 },
        ],
      },
      makeMcpSession(),
      null
    );
    const opts = await prisma.answerOption.findMany({
      where: { questionId: q.id },
      orderBy: { sortOrder: "asc" },
    });
    expect(opts).toHaveLength(3);
    expect(opts[0].label).toBe("New Right");
    expect(opts[0].points).toBe(2);
  });

  it("replaces competency tags when provided", async () => {
    const { sections } = await setupAssessment();
    const q = sections[0].questions[0];
    const c1 = await makeCompetency();
    const c2 = await makeCompetency();
    await prisma.questionCompetency.create({
      data: { questionId: q.id, competencyId: c1.id, weight: 1 },
    });

    await callTool(
      "update_question",
      { questionId: q.id, competencyIds: [c2.id] },
      makeMcpSession(),
      null
    );
    const tags = await prisma.questionCompetency.findMany({ where: { questionId: q.id } });
    expect(tags).toHaveLength(1);
    expect(tags[0].competencyId).toBe(c2.id);
  });

  it("clears competencies when [] passed", async () => {
    const { sections } = await setupAssessment();
    const q = sections[0].questions[0];
    const c = await makeCompetency();
    await prisma.questionCompetency.create({
      data: { questionId: q.id, competencyId: c.id, weight: 1 },
    });

    await callTool(
      "update_question",
      { questionId: q.id, competencyIds: [] },
      makeMcpSession(),
      null
    );
    expect(await prisma.questionCompetency.count({ where: { questionId: q.id } })).toBe(0);
  });

  it("rejects MCQ with no correct option when changing options", async () => {
    const { sections } = await setupAssessment();
    const q = sections[0].questions[0];
    const result = await callTool(
      "update_question",
      {
        questionId: q.id,
        options: [
          { label: "All wrong", points: 0 },
          { label: "Also wrong", points: 0 },
        ],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
  });
});

describe("reorder_questions", () => {
  it("reorders questions within a section", async () => {
    const { sections } = await setupAssessment();
    const sectionA = sections[0];

    // Add a second question to section A
    const r2 = await callTool(
      "add_question",
      { sectionId: sectionA.id, prompt: "Q2", questionType: "short_text" },
      makeMcpSession(),
      null
    );
    const q2 = parseToolJson(r2);

    const ordered = [q2.id, sectionA.questions[0].id];
    await callTool(
      "reorder_questions",
      { sectionId: sectionA.id, orderedQuestionIds: ordered },
      makeMcpSession(),
      null
    );

    const fresh = await prisma.question.findMany({
      where: { sectionId: sectionA.id },
      orderBy: { sortOrder: "asc" },
    });
    expect(fresh.map((q) => q.id)).toEqual(ordered);
  });
});

describe("create_question (Bank)", () => {
  it("creates a Bank question in the department's hidden library template", async () => {
    const dept = await makeDepartment({ name: "Operations", slug: "operations" });
    const result = await callTool(
      "create_question",
      {
        departmentId: dept.id,
        bankSectionSlug: "general",
        prompt: "Bank Q1",
        questionType: "single_select",
        options: [
          { label: "Right", points: 1 },
          { label: "Wrong", points: 0 },
        ],
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();

    const libTemplate = await prisma.assessmentTemplate.findUnique({
      where: { slug: "library-operations" },
    });
    expect(libTemplate).not.toBeNull();
    expect(libTemplate!.isActive).toBe(false);

    const data = parseToolJson(result);
    expect(data.prompt).toBe("Bank Q1");
  });

  it("rejects unknown department", async () => {
    const result = await callTool(
      "create_question",
      { departmentId: "missing", prompt: "X", questionType: "short_text" },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/department not found/);
  });
});

describe("attach_question_to_section", () => {
  it("clones a question (with options + competencies) into a new section", async () => {
    const { sections } = await setupAssessment();
    const source = sections[0].questions[0];
    const comp = await makeCompetency();
    await prisma.questionCompetency.create({
      data: { questionId: source.id, competencyId: comp.id, weight: 1 },
    });

    const result = await callTool(
      "attach_question_to_section",
      { questionId: source.id, sectionId: sections[1].id },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();

    const data = parseToolJson(result);
    expect(data.id).not.toBe(source.id);
    expect(data.sectionId).toBe(sections[1].id);
    expect(data.competencyIds).toEqual([comp.id]);
    expect(data.options.length).toBe(source.options.length);
    // Source must still exist
    expect(await prisma.question.findUnique({ where: { id: source.id } })).not.toBeNull();
  });

  it("rejects unknown source question", async () => {
    const { sections } = await setupAssessment();
    const result = await callTool(
      "attach_question_to_section",
      { questionId: "missing", sectionId: sections[0].id },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/source question not found/);
  });
});

describe("detach_question_from_section", () => {
  it("hard-deletes a question with no responses", async () => {
    const { sections } = await setupAssessment();
    const q = sections[0].questions[0];
    await callTool(
      "detach_question_from_section",
      { questionId: q.id },
      makeMcpSession(),
      null
    );
    expect(await prisma.question.findUnique({ where: { id: q.id } })).toBeNull();
  });

  it("refuses if the question has candidate responses", async () => {
    const { sections, version } = await setupAssessment();
    const q = sections[0].questions[0];

    const session = await prisma.candidateSession.create({
      data: {
        versionId: version.id,
        candidateName: "Test",
        candidateEmail: "t@test",
        status: "completed",
      },
    });
    await prisma.candidateResponse.create({
      data: {
        sessionId: session.id,
        sectionId: q.sectionId,
        questionId: q.id,
        answerPayload: JSON.stringify({ a: "b" }),
        maxPoints: 1,
      },
    });

    const result = await callTool(
      "detach_question_from_section",
      { questionId: q.id },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/candidate response/);
  });
});

```