---
type: source
source_type: laptop
title: setup
slug: setup
created: 2026-04-27
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/tests/setup.ts
original_size: 2282
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:32Z"
---

# setup

_Extracted from `assessify/tests/setup.ts` on 2026-05-14._

```typescript
import { execSync } from "node:child_process";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { afterAll, afterEach, beforeAll } from "vitest";

// Each test process gets a fresh ephemeral SQLite database. We push the
// schema once at startup, then truncate all data tables between tests so
// every test starts from a clean state.

const tmpDir = mkdtempSync(path.join(tmpdir(), "assessify-test-"));
const dbPath = path.join(tmpDir, "test.db");
process.env.DATABASE_URL = `file:${dbPath}`;

// Tables to truncate between tests, in dependency order (children first).
// Keeping this list explicit is safer than introspecting sqlite_master at
// runtime — Prisma may add hidden indexes/triggers that mass-deletes break.
const TRUNCATE_ORDER = [
  "AnalyticsEvent",
  "CandidateCompetencyScore",
  "CandidateSectionScore",
  "CandidateResult",
  "CandidateResponse",
  "CandidateSession",
  "CandidateInvite",
  "AnswerOption",
  "QuestionCompetency",
  "Question",
  "Section",
  "AssessmentVersion",
  "AssessmentTemplate",
  "JobRole",
  "Department",
  "Competency",
  "FormFile",
  "FormSubmission",
  "FormInvite",
  "FormTemplate",
  "WebhookDelivery",
  "WebhookEndpoint",
  "EasterEggClaim",
  "AuditLog",
  "PasswordOtp",
  "AdminUser",
  "OAuthAuthorizationCode",
  "OAuthClient",
  "McpToken",
  "LeaveBalance",
  "LeaveRequest",
  "LineManager",
  "Employee",
];

beforeAll(() => {
  // `prisma db push` builds the schema from prisma/schema.prisma into the
  // ephemeral file. The client is already generated for the same schema.
  execSync("npx prisma db push --accept-data-loss", {
    env: { ...process.env, DATABASE_URL: `file:${dbPath}` },
    stdio: "pipe",
  });
});

afterEach(async () => {
  const { prisma } = await import("@/lib/db");
  // Disable FK checks during truncation, then re-enable.
  await prisma.$executeRawUnsafe("PRAGMA foreign_keys = OFF");
  for (const table of TRUNCATE_ORDER) {
    await prisma.$executeRawUnsafe(`DELETE FROM "${table}"`);
  }
  await prisma.$executeRawUnsafe("PRAGMA foreign_keys = ON");
});

afterAll(async () => {
  const { prisma } = await import("@/lib/db");
  await prisma.$disconnect();
  rmSync(tmpDir, { recursive: true, force: true });
});

```