---
type: source
source_type: laptop
title: versions.test
slug: versions-test
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/__tests__/versions.test.ts
original_size: 9217
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# versions.test

_Extracted from `assessify/src/lib/mcp/__tests__/versions.test.ts` on 2026-05-14._

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
  publishLatestVersion,
} from "../../../../tests/factories";

function parseToolJson(result: { content: Array<{ text: string }>; isError?: boolean }) {
  return JSON.parse(result.content[0].text);
}

async function setup() {
  const dept = await makeDepartment();
  const role = await makeJobRole(dept.id);
  return { dept, role, ...(await makeAssessment(role.id)) };
}

describe("create_new_version", () => {
  it("snapshots latest version's tree into a new draft", async () => {
    const { template, sections } = await setup();
    const result = await callTool(
      "create_new_version",
      { assessmentId: template.id },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();
    const data = parseToolJson(result);
    expect(data.versionNumber).toBe(2);
    expect(data.status).toBe("draft");

    // Source version untouched
    const versions = await prisma.assessmentVersion.findMany({
      where: { templateId: template.id },
      orderBy: { versionNumber: "asc" },
    });
    expect(versions).toHaveLength(2);
    expect(versions[0].versionNumber).toBe(1);

    // New draft has the same number of sections + questions
    const newSections = await prisma.section.findMany({ where: { versionId: data.id } });
    expect(newSections).toHaveLength(sections.length);
  });

  it("denies non-admin", async () => {
    const { template } = await setup();
    const result = await callTool(
      "create_new_version",
      { assessmentId: template.id },
      makeMcpSession({ role: "user" }),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/permission_denied/);
  });
});

describe("in-flight session refusal", () => {
  it("update_assessment threshold change refuses with in-flight session on published version", async () => {
    const { template, version } = await setup();
    await prisma.assessmentVersion.update({
      where: { id: version.id },
      data: { status: "published", publishedAt: new Date() },
    });
    await makeSession({ versionId: version.id, status: "in_progress" });

    const result = await callTool(
      "update_assessment",
      {
        id: template.id,
        thresholds: { strongHire: 0.9, hire: 0.75, consider: 0.6 },
      },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/in-flight session/);
    expect(result.content[0].text).toMatch(/create_new_version/);
  });

  it("ALLOWS template-only edits (title) on a published version with in-flight sessions", async () => {
    const { template, version } = await setup();
    await prisma.assessmentVersion.update({
      where: { id: version.id },
      data: { status: "published", publishedAt: new Date() },
    });
    await makeSession({ versionId: version.id, status: "in_progress" });

    // Title lives on the template, not the version, so it's safe
    const result = await callTool(
      "update_assessment",
      { id: template.id, title: "Renamed Live" },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();
  });

  it("add_section refuses on a published version with in-flight sessions", async () => {
    const { template, version } = await setup();
    await prisma.assessmentVersion.update({
      where: { id: version.id },
      data: { status: "published", publishedAt: new Date() },
    });
    await makeSession({ versionId: version.id, status: "not_started" });

    const result = await callTool(
      "add_section",
      { assessmentId: template.id, title: "C", weight: 0.0 },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/in-flight/);
  });

  it("ALLOWS edits when the only sessions are completed/expired", async () => {
    const { template, version } = await setup();
    await prisma.assessmentVersion.update({
      where: { id: version.id },
      data: { status: "published", publishedAt: new Date() },
    });
    await makeSession({
      versionId: version.id,
      status: "completed",
      withResult: { totalScore: 5, maxScore: 10, normalizedScore: 0.5, recommendation: "consider" },
    });
    await makeSession({ versionId: version.id, status: "expired" });

    const result = await callTool(
      "add_section",
      { assessmentId: template.id, title: "C", weight: 0.0 },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();
  });

  it("ALLOWS edits on the new draft after create_new_version", async () => {
    const { template, version } = await setup();
    await prisma.assessmentVersion.update({
      where: { id: version.id },
      data: { status: "published", publishedAt: new Date() },
    });
    await makeSession({ versionId: version.id, status: "in_progress" });

    // Create a new draft — no in-flight sessions reference it
    await callTool("create_new_version", { assessmentId: template.id }, makeMcpSession(), null);

    // Now adding a section targets the new draft and should succeed
    const result = await callTool(
      "add_section",
      { assessmentId: template.id, title: "C", weight: 0.0 },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();
  });
});

describe("publish_version", () => {
  it("publishes a draft and archives the previously-published one", async () => {
    const { template } = await setup();
    await publishLatestVersion(template.id);

    const draft = parseToolJson(
      await callTool("create_new_version", { assessmentId: template.id }, makeMcpSession(), null)
    );

    const published = await callTool(
      "publish_version",
      { versionId: draft.id },
      makeMcpSession(),
      null
    );
    expect(published.isError).toBeFalsy();
    const data = parseToolJson(published);
    expect(data.archivedPreviousId).toBeTruthy();

    const versions = await prisma.assessmentVersion.findMany({
      where: { templateId: template.id },
      orderBy: { versionNumber: "asc" },
    });
    expect(versions[0].status).toBe("archived");
    expect(versions[1].status).toBe("published");
  });

  it("rejects publishing an archived version", async () => {
    const { version } = await setup();
    await prisma.assessmentVersion.update({
      where: { id: version.id },
      data: { status: "archived" },
    });
    const result = await callTool(
      "publish_version",
      { versionId: version.id },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBe(true);
    expect(result.content[0].text).toMatch(/archived/);
  });
});

describe("list_assessment_versions + get_assessment_version", () => {
  it("lists versions with status + sessionsCount", async () => {
    const { template, version } = await setup();
    await makeSession({ versionId: version.id });
    await callTool("create_new_version", { assessmentId: template.id }, makeMcpSession(), null);

    const result = await callTool(
      "list_assessment_versions",
      { assessmentId: template.id },
      makeMcpSession(),
      null
    );
    const data = parseToolJson(result);
    expect(data).toHaveLength(2);
    const v1 = data.find((v: { versionNumber: number }) => v.versionNumber === 1);
    expect(v1?.sessionsCount).toBe(1);
  });

  it("get_assessment_version returns the full tree", async () => {
    const { template } = await setup();
    const versions = await prisma.assessmentVersion.findMany({
      where: { templateId: template.id },
    });
    const result = await callTool(
      "get_assessment_version",
      { versionId: versions[0].id },
      makeMcpSession(),
      null
    );
    const data = parseToolJson(result);
    expect(data.sections.length).toBeGreaterThan(0);
    expect(data.sections[0].questions).toBeDefined();
  });
});

describe("revert_to_version", () => {
  it("clones an old version into a new published draft (preserves history)", async () => {
    const { template } = await setup();
    const v1 = await publishLatestVersion(template.id);

    // Create v2, publish it
    const v2 = parseToolJson(
      await callTool("create_new_version", { assessmentId: template.id }, makeMcpSession(), null)
    );
    await callTool("publish_version", { versionId: v2.id }, makeMcpSession(), null);

    // Revert to v1
    const result = await callTool(
      "revert_to_version",
      { assessmentId: template.id, versionId: v1 },
      makeMcpSession(),
      null
    );
    expect(result.isError).toBeFalsy();
    const data = parseToolJson(result);

    const all = await prisma.assessmentVersion.findMany({
      where: { templateId: template.id },
      orderBy: { versionNumber: "asc" },
    });
    expect(all).toHaveLength(3);
    expect(all[2].id).toBe(data.newVersionId);
    expect(all[2].status).toBe("published");
    // v1 unchanged (still archived from earlier publish)
    const v1After = all.find((v) => v.id === v1);
    expect(v1After?.status).toBe("archived");
  });
});

```