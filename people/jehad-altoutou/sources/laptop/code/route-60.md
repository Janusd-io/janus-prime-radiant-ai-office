---
type: source
source_type: laptop
title: Assessify — route
slug: route-60
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/uploads/route.ts
original_size: 2025
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/uploads/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { writeFile, mkdir } from "fs/promises";
import { join } from "path";
import { nanoid } from "nanoid";
import { validateFile, getFileRules } from "@/lib/file-validation";

export async function POST(req: NextRequest) {
  try {
    const formData = await req.formData();
    const file = formData.get("file") as File | null;
    const region = (formData.get("region") as string) ?? "global";
    const fieldName = (formData.get("fieldName") as string) ?? "attachment";

    if (!file) {
      return Response.json({ error: "No file provided" }, { status: 400 });
    }

    // Validate file format based on region
    const validation = validateFile(
      { type: file.type, size: file.size, name: file.name },
      region
    );

    if (!validation.valid) {
      return Response.json({ error: validation.error }, { status: 400 });
    }

    // Generate unique filename
    const ext = file.name.split(".").pop()?.toLowerCase() ?? "bin";
    const uniqueName = `${nanoid(16)}.${ext}`;

    // Store in data/uploads (inside the Docker volume so it persists)
    const uploadDir = join(process.cwd(), "data", "uploads");
    await mkdir(uploadDir, { recursive: true });

    const filePath = join(uploadDir, uniqueName);
    const bytes = await file.arrayBuffer();
    await writeFile(filePath, Buffer.from(bytes));

    return Response.json({
      file: {
        fileName: file.name,
        fileType: file.type,
        fileSize: file.size,
        filePath: `data/uploads/${uniqueName}`,
        storedName: uniqueName,
        fieldName,
      },
    });
  } catch (error) {
    console.error("POST /api/uploads error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

// GET: Return file format rules for a region
export async function GET(req: NextRequest) {
  const region = new URL(req.url).searchParams.get("region") ?? "global";
  const rules = getFileRules(region);
  return Response.json({ region, ...rules });
}

```