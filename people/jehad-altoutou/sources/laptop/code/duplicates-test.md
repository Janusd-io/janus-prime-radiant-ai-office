---
type: source
source_type: laptop
title: duplicates.test
slug: duplicates-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/duplicates.test.ts
original_size: 4645
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# duplicates.test

_Extracted from `assessify/src/lib/mcp/__tests__/duplicates.test.ts` on 2026-05-14._

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

async function setupWithCompetencyTag() {
  const dept = await makeDepartment();
  const role = await makeJobRole(dept.id);
  const a = await makeAssessment(role.id);
  const comp = await makeCompetency();
  const q = a.sections[0].questions[0];
  await prisma.questionCompetency.create({
    data: { questionId: q.id, competencyId: comp.id, weight: 1.0 },
  });
  return { dept, role, comp, ...a };
}

describe("duplicate_assessment", () => {
  it("deep-copies sections, questions, options, competency tags into a new draft", async () => {
    const { template, comp } = await setupWithCompetencyTag();
    await prisma.assessmentTemplate.update({ where: { id: template.id }, data: { isActive: true } });

    const r = parseJson(
      await callTool(
        "duplicate_assessment",
        { assessmentId: template.id, newTitle: "Senior Eng Assessment" },
        makeMcpSession(),
        null
      )
    );
    expect(r.id).not.toBe(template.id);
    expect(r.sourceAssessmentId).toBe(template.id);
    expect(r.sectionCount).toBe(2);
    expect(r.questionCount).toBe(1);

    const cloned = await prisma.assessmentTemplate.findUniqueOrThrow({
      where: { id: r.id },
      include: {
        versions: {
          include: {
            sections: { include: { questions: { include: { options: true, competencies: true } } } },
          },
        },
      },
    });
    expect(cloned.isActive).toBe(false);
    expect(cloned.versions[0].versionNumber).toBe(1);

    // Source unaffected
    const source = await prisma.assessmentTemplate.findUniqueOrThrow({ where: { id: template.id } });
    expect(source.isActive).toBe(true);

    // Competency tag preserved
    const allTags = cloned.versions[0].sections.flatMap((s) =>
      s.questions.flatMap((q) => q.competencies.map((c) => c.competencyId))
    );
    expect(allTags).toContain(comp.id);
  });

  it("can reassign to a different job role", async () => {
    const { template } = await setupWithCompetencyTag();
    const dept2 = await makeDepartment();
    const role2 = await makeJobRole(dept2.id);
    const r = parseJson(
      await callTool(
        "duplicate_assessment",
        { assessmentId: template.id, newTitle: "X", newJobRoleId: role2.id },
        makeMcpSession(),
        null
      )
    );
    const cloned = await prisma.assessmentTemplate.findUniqueOrThrow({ where: { id: r.id } });
    expect(cloned.jobRoleId).toBe(role2.id);
  });

  it("disambiguates the slug when a clone already exists with the same title", async () => {
    const { template } = await setupWithCompetencyTag();
    const r1 = parseJson(
      await callTool(
        "duplicate_assessment",
        { assessmentId: template.id, newTitle: "Same Title" },
        makeMcpSession(),
        null
      )
    );
    const r2 = parseJson(
      await callTool(
        "duplicate_assessment",
        { assessmentId: template.id, newTitle: "Same Title" },
        makeMcpSession(),
        null
      )
    );
    expect(r1.slug).not.toBe(r2.slug);
  });
});

describe("duplicate_question", () => {
  it("clones a question with options + competency tags into the same section", async () => {
    const { sections, comp } = await setupWithCompetencyTag();
    const sourceQ = sections[0].questions[0];
    const r = parseJson(
      await callTool("duplicate_question", { questionId: sourceQ.id }, makeMcpSession(), null)
    );
    expect(r.sectionId).toBe(sections[0].id);
    expect(r.sourceQuestionId).toBe(sourceQ.id);

    const cloned = await prisma.question.findUniqueOrThrow({
      where: { id: r.id },
      include: { options: true, competencies: true },
    });
    expect(cloned.options).toHaveLength(2);
    expect(cloned.competencies.map((c) => c.competencyId)).toContain(comp.id);
    expect(cloned.id).not.toBe(sourceQ.id);
  });

  it("clones into a different section when newSectionId is given", async () => {
    const { sections } = await setupWithCompetencyTag();
    const sourceQ = sections[0].questions[0];
    const r = parseJson(
      await callTool(
        "duplicate_question",
        { questionId: sourceQ.id, newSectionId: sections[1].id },
        makeMcpSession(),
        null
      )
    );
    expect(r.sectionId).toBe(sections[1].id);
  });
});

```