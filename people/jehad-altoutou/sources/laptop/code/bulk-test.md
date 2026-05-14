---
type: source
source_type: laptop
title: bulk.test
slug: bulk-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/bulk.test.ts
original_size: 6586
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# bulk.test

_Extracted from `[[assessify|assessify]]/src/lib/mcp/__tests__/bulk.test.ts` on 2026-05-14._

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

async function setupTwoQuestions() {
  const dept = await makeDepartment();
  const role = await makeJobRole(dept.id);
  const a = await makeAssessment(role.id);
  const q1 = a.sections[0].questions[0];
  // Add a second question on section A
  const q2 = await prisma.question.create({
    data: {
      sectionId: a.sections[0].id,
      slug: "q2",
      title: "Q2",
      prompt: "Q2 prompt",
      questionType: "single_select",
      difficulty: "medium",
      maxPoints: 1,
      sortOrder: 1,
      options: {
        create: [
          { key: "a", label: "Right", value: "a", points: 1, sortOrder: 0 },
          { key: "b", label: "Wrong", value: "b", points: 0, sortOrder: 1 },
        ],
      },
    },
  });
  return { ...a, q1, q2 };
}

describe("bulk_tag_questions", () => {
  it("adds the same competency tag to multiple questions", async () => {
    const { q1, q2 } = await setupTwoQuestions();
    const comp = await makeCompetency();
    const r = parseJson(
      await callTool(
        "bulk_tag_questions",
        { questionIds: [q1.id, q2.id], competencyIds: [comp.id], mode: "add" },
        makeMcpSession(),
        null
      )
    );
    expect(r.questionsUpdated).toBe(2);
    expect(r.tagsAdded).toBe(2);

    const tags = await prisma.questionCompetency.findMany({
      where: { questionId: { in: [q1.id, q2.id] } },
    });
    expect(tags).toHaveLength(2);
  });

  it("replace mode drops existing tags before applying new ones", async () => {
    const { q1 } = await setupTwoQuestions();
    const oldComp = await makeCompetency();
    const newComp = await makeCompetency();
    await prisma.questionCompetency.create({
      data: { questionId: q1.id, competencyId: oldComp.id, weight: 1.0 },
    });

    parseJson(
      await callTool(
        "bulk_tag_questions",
        { questionIds: [q1.id], competencyIds: [newComp.id], mode: "replace" },
        makeMcpSession(),
        null
      )
    );

    const tags = await prisma.questionCompetency.findMany({ where: { questionId: q1.id } });
    expect(tags).toHaveLength(1);
    expect(tags[0].competencyId).toBe(newComp.id);
  });

  it("remove mode deletes only the specified tags", async () => {
    const { q1 } = await setupTwoQuestions();
    const c1 = await makeCompetency();
    const c2 = await makeCompetency();
    await prisma.questionCompetency.createMany({
      data: [
        { questionId: q1.id, competencyId: c1.id, weight: 1.0 },
        { questionId: q1.id, competencyId: c2.id, weight: 1.0 },
      ],
    });
    parseJson(
      await callTool(
        "bulk_tag_questions",
        { questionIds: [q1.id], competencyIds: [c1.id], mode: "remove" },
        makeMcpSession(),
        null
      )
    );
    const remaining = await prisma.questionCompetency.findMany({ where: { questionId: q1.id } });
    expect(remaining).toHaveLength(1);
    expect(remaining[0].competencyId).toBe(c2.id);
  });

  it("rejects invalid mode", async () => {
    const { q1 } = await setupTwoQuestions();
    const r = await callTool(
      "bulk_tag_questions",
      { questionIds: [q1.id], competencyIds: [], mode: "frobnicate" },
      makeMcpSession(),
      null
    );
    expect(r.isError).toBe(true);
  });
});

describe("bulk_delete_questions", () => {
  it("deletes a batch with no responses", async () => {
    const { q1, q2 } = await setupTwoQuestions();
    const r = parseJson(
      await callTool(
        "bulk_delete_questions",
        { questionIds: [q1.id, q2.id] },
        makeMcpSession(),
        null
      )
    );
    expect(r.deletedCount).toBe(2);

    const remaining = await prisma.question.count({ where: { id: { in: [q1.id, q2.id] } } });
    expect(remaining).toBe(0);
  });

  it("refuses the WHOLE batch if any question has responses", async () => {
    const { q1, q2, version } = await setupTwoQuestions();
    const session = await prisma.candidateSession.create({
      data: {
        versionId: version.id,
        candidateEmail: "x@test.local",
        candidateName: "X",
        status: "completed",
      },
    });
    await prisma.candidateResponse.create({
      data: {
        sessionId: session.id,
        sectionId: q1.sectionId,
        questionId: q1.id,
        answerPayload: JSON.stringify({}),
        earnedPoints: 0,
        maxPoints: 1,
        normalizedScore: 0,
        timeSpent: 5,
      },
    });

    const r = await callTool(
      "bulk_delete_questions",
      { questionIds: [q1.id, q2.id] },
      makeMcpSession(),
      null
    );
    expect(r.isError).toBe(true);

    // Neither was deleted
    const remaining = await prisma.question.count({ where: { id: { in: [q1.id, q2.id] } } });
    expect(remaining).toBe(2);
  });
});

describe("bulk_toggle_assessment_active", () => {
  it("activates a list and reports counts", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const a = await makeAssessment(role.id);
    const b = await makeAssessment(role.id);

    const r = parseJson(
      await callTool(
        "bulk_toggle_assessment_active",
        { assessmentIds: [a.template.id, b.template.id, "fake-id"], isActive: true },
        makeMcpSession(),
        null
      )
    );
    expect(r.changedCount).toBe(2);
    expect(r.alreadyInStateCount).toBe(0);
    expect(r.notFound).toEqual(["fake-id"]);

    const after = await prisma.assessmentTemplate.findMany({
      where: { id: { in: [a.template.id, b.template.id] } },
      select: { isActive: true },
    });
    expect(after.every((x) => x.isActive)).toBe(true);
  });

  it("counts already-active assessments as alreadyInStateCount", async () => {
    const dept = await makeDepartment();
    const role = await makeJobRole(dept.id);
    const a = await makeAssessment(role.id);
    await prisma.assessmentTemplate.update({ where: { id: a.template.id }, data: { isActive: true } });

    const r = parseJson(
      await callTool(
        "bulk_toggle_assessment_active",
        { assessmentIds: [a.template.id], isActive: true },
        makeMcpSession(),
        null
      )
    );
    expect(r.changedCount).toBe(0);
    expect(r.alreadyInStateCount).toBe(1);
  });
});

```