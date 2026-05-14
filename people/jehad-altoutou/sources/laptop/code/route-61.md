---
type: source
source_type: laptop
title: route
slug: route-61
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/uploads/[filename]/route.ts"
original_size: 1048
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/uploads/[filename]/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { readFile } from "fs/promises";
import { join } from "path";

export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ filename: string }> }
) {
  try {
    const { filename } = await ctx.params;

    // Sanitize — prevent directory traversal
    const safe = filename.replace(/[^a-zA-Z0-9._-]/g, "");
    const filePath = join(process.cwd(), "data", "uploads", safe);

    const buffer = await readFile(filePath);

    // Determine content type from extension
    const ext = safe.split(".").pop()?.toLowerCase();
    const contentTypes: Record<string, string> = {
      jpg: "image/jpeg",
      jpeg: "image/jpeg",
      png: "image/png",
      pdf: "application/pdf",
    };

    return new Response(buffer, {
      headers: {
        "Content-Type": contentTypes[ext ?? ""] ?? "application/octet-stream",
        "Content-Disposition": `inline; filename="${safe}"`,
      },
    });
  } catch {
    return Response.json({ error: "File not found" }, { status: 404 });
  }
}

```