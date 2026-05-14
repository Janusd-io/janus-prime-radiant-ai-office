---
type: source
source_type: laptop
title: page
slug: page-33
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/careers/apply/[roleSlug]/page.tsx"
original_size: 3241
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/careers/apply/[roleSlug]/page.tsx` on 2026-05-14._

```tsx
import { prisma } from "@/lib/db";
import { redirect, notFound } from "next/navigation";
import { nanoid } from "nanoid";
import { RECRUITMENT_INTAKE_DIRECT } from "@/lib/recruitment";

export const dynamic = "force-dynamic";

export default async function CareersApplyPage({
  params,
}: {
  params: Promise<{ roleSlug: string }>;
}) {
  const { roleSlug } = await params;

  const role = await prisma.jobRole.findUnique({
    where: { slug: roleSlug },
    include: { department: true },
  });
  if (!role || !role.isActive) notFound();

  const directTemplate = await prisma.formTemplate.findFirst({
    where: { formType: RECRUITMENT_INTAKE_DIRECT, isActive: true },
  });
  if (!directTemplate) {
    return (
      <main className="mx-auto max-w-xl px-6 py-12 text-center">
        <h1 className="text-2xl font-bold">Application form unavailable</h1>
        <p className="mt-2 text-sm text-zinc-500">
          The direct application form has not been configured yet. Please email careers@janusd.io.
        </p>
      </main>
    );
  }

  async function continueToForm() {
    "use server";
    const code = nanoid(12);
    const expiresAt = new Date(Date.now() + 30 * 24 * 60 * 60 * 1000); // 30d
    await prisma.formInvite.create({
      data: {
        code,
        employeeName: "(self-apply)",
        employeeEmail: `careers+${code}@janusd.io`,
        templateId: directTemplate!.id,
        region: "global",
        status: "pending",
        expiresAt,
        createdBy: "system:careers",
      },
    });
    redirect(`/forms/${code}`);
  }

  return (
    <main className="mx-auto max-w-xl px-6 py-12">
      <a href="/careers" className="text-xs text-zinc-500 hover:underline">
        ← All open positions
      </a>
      <h1 className="mt-2 text-2xl font-bold tracking-tight">{role.title}</h1>
      <p className="mt-1 text-sm text-zinc-500">{role.department.name}</p>

      {role.description && (
        <section className="mt-6 rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900">
          <h2 className="mb-3 text-sm font-semibold">About this role</h2>
          <p className="whitespace-pre-wrap text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
            {role.description}
          </p>
        </section>
      )}

      <section className="mt-6 rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900">
        <h2 className="mb-2 text-sm font-semibold">Ready to apply?</h2>
        <p className="text-sm text-zinc-600 dark:text-zinc-400">
          The next step takes ~3 minutes. You&apos;ll fill in your details and upload your CV (PDF,
          max 1 MB). We&apos;ll get back to you after reviewing.
        </p>
        <form action={continueToForm} className="mt-4">
          <button
            type="submit"
            className="rounded-lg bg-zinc-900 px-5 py-2.5 text-sm font-medium text-white hover:bg-zinc-700 dark:bg-white dark:text-zinc-900 dark:hover:bg-zinc-100"
          >
            Continue to application form
          </button>
        </form>
      </section>

      <footer className="mt-12 text-xs text-zinc-500">
        Powered by Assessify · Janus Digital
      </footer>
    </main>
  );
}

```