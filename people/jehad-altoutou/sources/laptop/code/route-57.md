---
type: source
source_type: laptop
title: route
slug: route-57
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/form-templates/route.ts
original_size: 2618
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/admin/form-templates/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

// GET: list all form templates
export async function GET() {
  try {
    const session = await getSession();
    if (!session) return Response.json({ error: "Unauthorized" }, { status: 401 });

    const templates = await prisma.formTemplate.findMany({
      orderBy: { createdAt: "desc" },
      include: {
        _count: { select: { submissions: true, invites: true } },
      },
    });

    return Response.json({ templates });
  } catch (error) {
    console.error("GET /api/admin/form-templates error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

// POST: create a new form template
export async function POST(req: NextRequest) {
  try {
    const session = await getSession();
    if (!session) return Response.json({ error: "Unauthorized" }, { status: 401 });
    if (session.role !== "admin") return Response.json({ error: "Admin only" }, { status: 403 });

    const { name, description, fields } = (await req.json()) as {
      name?: string;
      description?: string;
      fields?: Array<{
        name: string;
        label: string;
        type: string;
        required?: boolean;
        placeholder?: string;
        options?: string[];
        section?: string;
      }>;
    };

    if (!name?.trim()) return Response.json({ error: "Name is required" }, { status: 400 });
    if (!fields || fields.length === 0) return Response.json({ error: "At least one field is required" }, { status: 400 });

    // Validate field definitions
    for (const f of fields) {
      if (!f.name || !f.label || !f.type) {
        return Response.json({ error: `Each field needs name, label, and type` }, { status: 400 });
      }
    }

    // Generate slug
    const baseSlug = name.trim().toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
    let slug = baseSlug;
    let counter = 1;
    while (await prisma.formTemplate.findUnique({ where: { slug } })) {
      slug = `${baseSlug}-${counter}`;
      counter++;
    }

    const template = await prisma.formTemplate.create({
      data: {
        name: name.trim(),
        slug,
        description: description?.trim() || null,
        formType: "custom",
        fields: JSON.stringify(fields),
        isActive: true,
      },
    });

    return Response.json({ template }, { status: 201 });
  } catch (error) {
    console.error("POST /api/admin/form-templates error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```