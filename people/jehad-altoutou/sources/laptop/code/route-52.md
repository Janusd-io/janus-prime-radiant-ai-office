---
type: source
source_type: laptop
title: route
slug: route-52
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/question-bank/route.ts
original_size: 12030
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/question-bank/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

// Normalize a section title into a bank category so questions from
// different templates' "Cultural Fit" sections all group together.
function normalizeSectionCategory(sectionSlug: string, sectionTitle: string): { slug: string; label: string } {
  const slug = sectionSlug.toLowerCase();
  const title = sectionTitle.toLowerCase();
  if (slug.includes("cultur") || title.includes("cultur")) return { slug: "cultural-fit", label: "Cultural Fit" };
  if (slug.includes("ai-aware") || title.includes("ai aware") || title.includes("ai readiness")) return { slug: "ai-awareness", label: "AI Awareness" };
  if (slug === "library" || slug.startsWith("library-")) return { slug: "general", label: "General" };
  return { slug: "department-specific", label: "Department-Specific" };
}

// GET: List all questions across all assessments grouped by department
export async function GET(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const url = new URL(req.url);
    const excludeTemplateId = url.searchParams.get("excludeTemplateId");

    const questions = await prisma.question.findMany({
      where: { isActive: true },
      include: {
        section: {
          include: {
            version: {
              include: {
                template: {
                  include: { jobRole: { include: { department: true } } },
                },
              },
            },
          },
        },
        options: { orderBy: { sortOrder: "asc" } },
        competencies: { include: { competency: true } },
      },
      orderBy: { createdAt: "desc" },
    });

    // Deduplicate by (title + prompt)
    type Usage = {
      templateId: string;
      templateTitle: string;
      department: string;
      departmentSlug: string;
      sectionTitle: string;
      sectionId: string;
      questionId: string;
      isLibrary: boolean;
    };
    type DedupedQuestion = {
      id: string;
      sectionId: string;
      templateId: string;
      isLibraryPrimary: boolean;
      bankSection: ReturnType<typeof normalizeSectionCategory>;
      title: string;
      prompt: string;
      questionType: string;
      difficulty: string;
      maxPoints: number;
      weight: number;
      scoringStrategy: string;
      correctAnswerKey: string | null;
      explanation: string | null;
      options: Array<{ key: string; label: string; value: string; points: number; isCorrect: boolean }>;
      competencies: Array<{ id: string; name: string; slug: string; weight: number }>;
      departments: Array<{ name: string; slug: string }>;
      departmentSlugs: string[];
      usages: Usage[];
    };
    const seen = new Map<string, DedupedQuestion>();
    for (const q of questions) {
      const templateId = q.section.version.template.id;
      if (excludeTemplateId && templateId === excludeTemplateId) continue;

      const key = `${q.title}|||${q.prompt}`;
      const dept = q.section.version.template.jobRole.department;
      const isLibrary = q.section.version.template.slug.startsWith("library-");
      const usage = {
        templateId,
        templateTitle: q.section.version.template.title,
        department: dept.name,
        departmentSlug: dept.slug,
        sectionTitle: q.section.title,
        sectionId: q.section.id,
        questionId: q.id,
        isLibrary,
      };

      const existing = seen.get(key);
      if (existing) {
        existing.usages.push(usage);
        if (isLibrary && !existing.isLibraryPrimary) {
          existing.id = q.id;
          existing.sectionId = q.section.id;
          existing.templateId = templateId;
          existing.isLibraryPrimary = true;
          existing.bankSection = normalizeSectionCategory(q.section.slug, q.section.title);
        }
        if (!existing.departmentSlugs.includes(dept.slug)) {
          existing.departmentSlugs.push(dept.slug);
          existing.departments.push({ name: dept.name, slug: dept.slug });
        }
      } else {
        const bankSection = normalizeSectionCategory(q.section.slug, q.section.title);
        seen.set(key, {
          id: q.id,
          sectionId: q.section.id,
          templateId,
          isLibraryPrimary: isLibrary,
          bankSection,
          title: q.title,
          prompt: q.prompt,
          questionType: q.questionType,
          difficulty: q.difficulty,
          maxPoints: q.maxPoints,
          weight: q.weight,
          scoringStrategy: q.scoringStrategy,
          correctAnswerKey: q.correctAnswerKey,
          explanation: q.explanation,
          options: q.options.map((o) => ({
            key: o.key,
            label: o.label,
            value: o.value,
            points: o.points,
            isCorrect: o.isCorrect,
          })),
          competencies: q.competencies.map((qc) => ({
            id: qc.competency.id,
            name: qc.competency.name,
            slug: qc.competency.slug,
            weight: qc.weight,
          })),
          departments: [{ name: dept.name, slug: dept.slug }],
          departmentSlugs: [dept.slug],
          usages: [usage],
        });
      }
    }

    return Response.json({ questions: [...seen.values()] });
  } catch (error) {
    console.error("GET /api/admin/question-bank error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

// POST: Create a standalone question in the department's hidden Library template
export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const body = await req.json();
    const {
      departmentId,
      bankSectionSlug,
      title,
      prompt,
      questionType,
      difficulty,
      maxPoints,
      weight,
      scoringStrategy,
      correctAnswerKey,
      explanation,
      options,
      competencies,
    } = body as {
      departmentId: string;
      bankSectionSlug?: string;
      title: string;
      prompt: string;
      questionType: string;
      difficulty?: string;
      maxPoints: number;
      weight?: number;
      scoringStrategy?: string;
      correctAnswerKey?: string;
      explanation?: string;
      options?: Array<{ key: string; label: string; value?: string; points: number; isCorrect: boolean }>;
      competencies?: { competencyId: string; weight?: number }[];
    };

    if (!departmentId || !title || !prompt || !questionType || maxPoints === undefined) {
      return Response.json(
        { error: "departmentId, title, prompt, questionType, and maxPoints are required" },
        { status: 400 }
      );
    }

    // Map bank section slug to section title and library section slug
    const sectionMap: Record<string, { title: string; slug: string }> = {
      "cultural-fit": { title: "Cultural Fit", slug: "cultural-fit" },
      "ai-awareness": { title: "AI Awareness", slug: "ai-awareness" },
      "department-specific": { title: "Department-Specific", slug: "department-specific" },
      "general": { title: "General", slug: "library" },
    };
    const targetSection = sectionMap[bankSectionSlug ?? "general"] ?? sectionMap.general;

    const department = await prisma.department.findUnique({ where: { id: departmentId } });
    if (!department) return Response.json({ error: "Department not found" }, { status: 404 });

    const librarySlug = `library-${department.slug}`;
    let libraryTemplate = await prisma.assessmentTemplate.findUnique({
      where: { slug: librarySlug },
      include: { versions: { include: { sections: true } } },
    });

    if (!libraryTemplate) {
      let placeholderRole = await prisma.jobRole.findFirst({ where: { departmentId } });
      if (!placeholderRole) {
        placeholderRole = await prisma.jobRole.create({
          data: {
            departmentId,
            title: "Question Library",
            slug: `library-role-${department.slug}-${Date.now()}`,
            description: "Internal — holds standalone bank questions",
            isActive: false,
          },
        });
      }

      libraryTemplate = await prisma.assessmentTemplate.create({
        data: {
          jobRoleId: placeholderRole.id,
          title: `${department.name} Question Library`,
          slug: librarySlug,
          description: "Standalone questions added to the bank",
          isActive: false,
          versions: {
            create: {
              versionNumber: 1,
              status: "draft",
              passingScore: 0.6,
            },
          },
        },
        include: { versions: { include: { sections: true } } },
      });
    }

    const version = libraryTemplate.versions[0];
    // Find or create the section in the library template
    let section = version.sections.find((s) => s.slug === targetSection.slug);
    if (!section) {
      section = await prisma.section.create({
        data: {
          versionId: version.id,
          title: targetSection.title,
          slug: targetSection.slug,
          sortOrder: version.sections.length + 1,
          weight: 0.33,
        },
      });
    }

    const existingCount = await prisma.question.count({ where: { sectionId: section.id } });

    const question = await prisma.question.create({
      data: {
        sectionId: section.id,
        slug: `bank-q-${Date.now()}`,
        title,
        prompt,
        questionType,
        difficulty: difficulty ?? "medium",
        maxPoints,
        weight: weight ?? 1.0,
        scoringStrategy: scoringStrategy ?? "weighted_options",
        correctAnswerKey: correctAnswerKey ?? null,
        explanation: explanation ?? null,
        sortOrder: existingCount + 1,
        isActive: true,
      },
    });

    if (Array.isArray(options) && options.length > 0) {
      await prisma.answerOption.createMany({
        data: options.map((opt, i) => ({
          questionId: question.id,
          key: opt.key,
          label: opt.label,
          value: opt.value ?? opt.key,
          points: opt.points,
          isCorrect: opt.isCorrect ?? false,
          sortOrder: i + 1,
        })),
      });
    }

    if (Array.isArray(competencies) && competencies.length > 0) {
      await prisma.questionCompetency.createMany({
        data: competencies.map((c: { competencyId: string; weight?: number }) => ({
          questionId: question.id,
          competencyId: c.competencyId,
          weight: c.weight ?? 1.0,
        })),
      });
    }

    return Response.json({ question }, { status: 201 });
  } catch (error) {
    console.error("POST /api/admin/question-bank error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

// DELETE: ?id=questionId — removes question from the bank (only if not used by candidates)
export async function DELETE(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const id = new URL(req.url).searchParams.get("id");
    if (!id) return Response.json({ error: "id is required" }, { status: 400 });

    const responseCount = await prisma.candidateResponse.count({ where: { questionId: id } });
    if (responseCount > 0) {
      return Response.json(
        { error: `Cannot delete: question has ${responseCount} candidate response(s).` },
        { status: 400 }
      );
    }

    await prisma.questionCompetency.deleteMany({ where: { questionId: id } });
    await prisma.answerOption.deleteMany({ where: { questionId: id } });
    await prisma.question.delete({ where: { id } });

    return Response.json({ ok: true });
  } catch (error) {
    console.error("DELETE /api/admin/question-bank error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```