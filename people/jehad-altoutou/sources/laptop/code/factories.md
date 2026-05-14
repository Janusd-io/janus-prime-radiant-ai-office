---
type: source
source_type: laptop
title: factories
slug: factories
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/tests/factories.ts
original_size: 5658
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:32Z"
project: assessify

---

# factories

_Extracted from `[[assessify|assessify]]/tests/factories.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import type { McpSession } from "@/lib/mcp/auth";

let counter = 0;
const uniq = (prefix: string) => `${prefix}-${Date.now()}-${++counter}`;

export async function makeAdminUser(overrides: Partial<{ name: string; email: string; role: string }> = {}) {
  return prisma.adminUser.create({
    data: {
      name: overrides.name ?? "Test Admin",
      email: overrides.email ?? `${uniq("admin")}@test.local`,
      passwordHash: "test-hash",
      role: overrides.role ?? "admin",
      isActive: true,
    },
  });
}

export async function makeDepartment(overrides: Partial<{ name: string; slug: string }> = {}) {
  const name = overrides.name ?? `Dept ${uniq("d")}`;
  return prisma.department.create({
    data: { name, slug: overrides.slug ?? name.toLowerCase().replace(/\s+/g, "-") },
  });
}

export async function makeJobRole(deptId: string, overrides: Partial<{ title: string }> = {}) {
  return prisma.jobRole.create({
    data: {
      departmentId: deptId,
      title: overrides.title ?? `Role ${uniq("r")}`,
      slug: uniq("role"),
    },
  });
}

export async function makeCompetency(overrides: Partial<{ name: string }> = {}) {
  return prisma.competency.create({
    data: {
      name: overrides.name ?? `Competency ${uniq("c")}`,
      slug: uniq("comp"),
    },
  });
}

/**
 * Build a full assessment with one version, two sections (weights 0.6/0.4),
 * and one MCQ question. Returns the template + version + sections.
 */
export async function makeAssessment(jobRoleId: string) {
  const created = await prisma.assessmentTemplate.create({
    data: {
      jobRoleId,
      title: `Assessment ${uniq("a")}`,
      slug: uniq("assess"),
      isActive: false,
      versions: {
        create: {
          versionNumber: 1,
          status: "draft",
          timeLimit: 30,
          passingScore: 0.7,
          sections: {
            create: [
              {
                title: "Section A",
                slug: "section-a",
                weight: 0.6,
                sortOrder: 0,
                questions: {
                  create: {
                    slug: "q1",
                    title: "Q1",
                    prompt: "Q1 prompt",
                    questionType: "single_select",
                    difficulty: "medium",
                    maxPoints: 1,
                    sortOrder: 0,
                    options: {
                      create: [
                        { key: "a", label: "Right", value: "a", points: 1, sortOrder: 0 },
                        { key: "b", label: "Wrong", value: "b", points: 0, sortOrder: 1 },
                      ],
                    },
                  },
                },
              },
              {
                title: "Section B",
                slug: "section-b",
                weight: 0.4,
                sortOrder: 1,
              },
            ],
          },
        },
      },
    },
  });

  const template = await prisma.assessmentTemplate.findUniqueOrThrow({
    where: { id: created.id },
    include: {
      versions: {
        include: { sections: { include: { questions: { include: { options: true } } } } },
        orderBy: { versionNumber: "desc" },
      },
    },
  });
  const version = template.versions[0];
  return { template, version, sections: version.sections };
}

/**
 * Create a candidate session against the latest version of an assessment.
 * Optionally completes it with a result (recommendation, scores).
 */
export async function makeSession(args: {
  versionId: string;
  status?: string;
  candidateName?: string;
  candidateEmail?: string;
  withResult?: { totalScore: number; maxScore: number; normalizedScore: number; recommendation: string };
  startedAt?: Date;
  completedAt?: Date;
}) {
  const now = new Date();
  const session = await prisma.candidateSession.create({
    data: {
      versionId: args.versionId,
      candidateName: args.candidateName ?? `Cand ${uniq("c")}`,
      candidateEmail: args.candidateEmail ?? `${uniq("c")}@test.local`,
      status: args.status ?? "completed",
      startedAt: args.startedAt ?? new Date(now.getTime() - 60 * 60 * 1000),
      completedAt: args.completedAt ?? (args.status === "completed" || args.withResult ? now : null),
    },
  });
  if (args.withResult) {
    await prisma.candidateResult.create({
      data: {
        sessionId: session.id,
        totalScore: args.withResult.totalScore,
        maxScore: args.withResult.maxScore,
        normalizedScore: args.withResult.normalizedScore,
        recommendation: args.withResult.recommendation,
      },
    });
  }
  return session;
}

/** Mark an assessment's latest version as published. Returns the version id. */
export async function publishLatestVersion(assessmentId: string): Promise<string> {
  const latest = await prisma.assessmentVersion.findFirst({
    where: { templateId: assessmentId },
    orderBy: { versionNumber: "desc" },
  });
  if (!latest) throw new Error(`no version on ${assessmentId}`);
  await prisma.assessmentVersion.update({
    where: { id: latest.id },
    data: { status: "published", publishedAt: new Date() },
  });
  return latest.id;
}

export function makeMcpSession(overrides: Partial<McpSession> = {}): McpSession {
  return {
    userId: overrides.userId ?? "test-user",
    userName: overrides.userName ?? "Test Admin",
    userEmail: overrides.userEmail ?? "test@local",
    role: overrides.role ?? "admin",
    tokenId: overrides.tokenId ?? "test-token",
    scopes: overrides.scopes ?? ["read", "write"],
    office: overrides.office ?? null,
    scopedDepartments: overrides.scopedDepartments ?? null,
  };
}

```