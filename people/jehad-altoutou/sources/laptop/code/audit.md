---
type: source
source_type: laptop
title: audit
slug: audit
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/audit.ts
original_size: 786
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# audit

_Extracted from `[[assessify|assessify]]/src/lib/audit.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";

export interface AuditEntry {
  userId: string;
  userEmail: string;
  action: string;
  targetType?: string;
  targetId?: string;
  details?: Record<string, unknown>;
  ipAddress?: string;
}

export async function auditLog(entry: AuditEntry) {
  try {
    await prisma.auditLog.create({
      data: {
        userId: entry.userId,
        userEmail: entry.userEmail,
        action: entry.action,
        targetType: entry.targetType ?? null,
        targetId: entry.targetId ?? null,
        details: entry.details ? JSON.stringify(entry.details) : null,
        ipAddress: entry.ipAddress ?? null,
      },
    });
  } catch (error) {
    // Audit logging should never break the main operation
    console.error("Audit log failed:", error);
  }
}

```