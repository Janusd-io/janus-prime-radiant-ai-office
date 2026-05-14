---
type: source
source_type: laptop
title: analytics.test
slug: analytics-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/analytics.test.ts
original_size: 4748
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# analytics.test

_Extracted from `[[assessify|assessify]]/src/lib/mcp/__tests__/analytics.test.ts` on 2026-05-14._

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

describe("get_assessment_analytics", () => {
  it("aggregates basic counts + score histogram", async () => {
    const { template, version } = await setup();
    // 3 completed sessions with varied scores
    for (const score of [0.9, 0.65, 0.3]) {
      await makeSession({
        versionId: version.id,
        withResult: {
          totalScore: score * 10,
          maxScore: 10,
          normalizedScore: score,
          recommendation: score > 0.7 ? "hire" : score > 0.5 ? "consider" : "reject",
        },
      });
    }

    const result = await callTool(
      "get_assessment_analytics",
      { assessmentId: template.id },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();
    const data = parseToolJson(result);
    expect(data.sessions.completed).toBe(3);
    expect(data.avgNormalizedScore).toBeCloseTo((0.9 + 0.65 + 0.3) / 3, 4);
    expect(data.recommendationBreakdown.hire).toBe(1);
    expect(data.recommendationBreakdown.consider).toBe(1);
    expect(data.recommendationBreakdown.reject).toBe(1);
    const totalInBuckets = data.scoreHistogram.reduce(
      (acc: number, b: { count: number }) => acc + b.count,
      0
    );
    expect(totalInBuckets).toBe(3);
  });

  it("rejects unknown assessment", async () => {
    const result = await callTool(
      "get_assessment_analytics",
      { assessmentId: "missing" },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
  });

  it("denies non-admin", async () => {
    const { template } = await setup();
    const result = await callTool(
      "get_assessment_analytics",
      { assessmentId: template.id },
      makeMcpSession({ role: "user" }),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/permission_denied/);
  });
});

describe("get_question_analytics", () => {
  it("returns pctCorrect + option distribution from real responses", async () => {
    const { sections, version } = await setup();
    const q = sections[0].questions[0];
    // 2 correct (selected option a) + 1 incorrect (option b)
    for (const [score, picked] of [[1, "a"], [1, "a"], [0, "b"]] as const) {
      const session = await makeSession({
        versionId: version.id,
        withResult: { totalScore: 1, maxScore: 1, normalizedScore: score, recommendation: "hire" },
      });
      await prisma.candidateResponse.create({
        data: {
          sessionId: session.id,
          sectionId: sections[0].id,
          questionId: q.id,
          answerPayload: JSON.stringify({ selected: [picked] }),
          selectedOptions: JSON.stringify([picked]),
          earnedPoints: score,
          maxPoints: 1,
          normalizedScore: score,
          timeSpent: 30,
        },
      });
    }

    const result = await callTool(
      "get_question_analytics",
      { questionId: q.id },
      makeMcpSession(),
      null
    );
    const data = parseToolJson(result);
    expect(data.sampleSize).toBe(3);
    expect(data.pctCorrect).toBeCloseTo(2 / 3, 2);
    const optA = data.optionDistribution.find((o: { key: string }) => o.key === "a");
    expect(optA?.pickedCount).toBe(2);
    const optB = data.optionDistribution.find((o: { key: string }) => o.key === "b");
    expect(optB?.pickedCount).toBe(1);
  });

  it("returns null discrimination index when sample < 6", async () => {
    const { sections, version } = await setup();
    const q = sections[0].questions[0];
    const session = await makeSession({
      versionId: version.id,
      withResult: { totalScore: 1, maxScore: 1, normalizedScore: 1, recommendation: "hire" },
    });
    await prisma.candidateResponse.create({
      data: {
        sessionId: session.id,
        sectionId: sections[0].id,
        questionId: q.id,
        answerPayload: "{}",
        earnedPoints: 1,
        maxPoints: 1,
        normalizedScore: 1,
        timeSpent: 10,
      },
    });

    const result = await callTool(
      "get_question_analytics",
      { questionId: q.id },
      makeMcpSession(),
      null
    );
    const data = parseToolJson(result);
    expect(data.discriminationIndex).toBeNull();
  });
});

```