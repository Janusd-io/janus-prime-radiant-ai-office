---
type: source
source_type: laptop
title: Assessify — route
slug: route-13
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/forms/invite/[code]/route.ts"
original_size: 3270
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/forms/invite/[code]/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { getFileRules } from "@/lib/file-validation";

export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ code: string }> }
) {
  try {
    const { code } = await ctx.params;

    const invite = await prisma.formInvite.findUnique({
      where: { code },
      include: { template: true },
    });

    if (!invite) {
      return Response.json({ error: "Invite not found or invalid link." }, { status: 404 });
    }

    if (invite.expiresAt && invite.expiresAt < new Date()) {
      return Response.json({ error: "This invite has expired. Please contact HR for a new link." }, { status: 410 });
    }

    const fileRules = getFileRules(invite.region);

    // Resolve any field with `dynamicOptionsSource` against live data. Lets
    // the recruitment intake form pull the role list from JobRole every
    // request — no caching, no static option list — so admin changes show up
    // instantly on the next form load. See plan: Phase 1.A "dynamic options".
    type FieldDef = {
      name: string;
      label: string;
      type: string;
      required?: boolean;
      placeholder?: string;
      options?: string[];
      optionLabels?: Record<string, string>;
      dynamicOptionsSource?: string;
      section?: string;
    };

    const rawFields: FieldDef[] = invite.template.fields ? JSON.parse(invite.template.fields) : [];
    const fields = await resolveDynamicFields(rawFields);

    return Response.json({
      invite: {
        id: invite.id,
        code: invite.code,
        employeeName: invite.employeeName,
        employeeEmail: invite.employeeEmail,
        region: invite.region,
        status: invite.status,
        submissionId: invite.submissionId,
        expiresAt: invite.expiresAt,
      },
      form: {
        id: invite.template.id,
        name: invite.template.name,
        slug: invite.template.slug,
        description: invite.template.description,
        formType: invite.template.formType,
        fields,
      },
      fileRules,
    });
  } catch (error) {
    console.error("GET /api/forms/invite/[code] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

type ResolvableField = {
  name: string;
  label: string;
  type: string;
  required?: boolean;
  placeholder?: string;
  options?: string[];
  optionLabels?: Record<string, string>;
  dynamicOptionsSource?: string;
  section?: string;
};

async function resolveDynamicFields(fields: ResolvableField[]): Promise<ResolvableField[]> {
  if (!fields.length) return fields;
  const out: ResolvableField[] = [];
  for (const f of fields) {
    if (f.dynamicOptionsSource === "active_job_roles") {
      const roles = await prisma.jobRole.findMany({
        where: { isActive: true },
        include: { department: true },
        orderBy: [{ department: { name: "asc" } }, { title: "asc" }],
      });
      const optionLabels: Record<string, string> = {};
      const options = roles.map((r) => {
        optionLabels[r.id] = `${r.title} — ${r.department.name}`;
        return r.id;
      });
      out.push({ ...f, options, optionLabels });
    } else {
      out.push(f);
    }
  }
  return out;
}

```