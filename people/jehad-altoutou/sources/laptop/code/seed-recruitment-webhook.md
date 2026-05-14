---
type: source
source_type: laptop
title: seed-recruitment-webhook
slug: seed-recruitment-webhook
created: 2026-05-05
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/scripts/seed-recruitment-webhook.ts
original_size: 1949
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# seed-recruitment-webhook

_Extracted from `assessify/scripts/seed-recruitment-webhook.ts` on 2026-05-14._

```typescript
// Idempotent seeder for the recruitment n8n webhook (Phase 1.B).
// Registers the n8n endpoint as a WebhookEndpoint subscribed to form.submitted.
//
// Run locally:  npx tsx scripts/seed-recruitment-webhook.ts
// Run in prod:  copy DB out, run, copy back (until tsx is in container)
//
// Safe to re-run. The existing dispatchWebhook() in src/lib/webhooks.ts
// fans out form.submitted to all active endpoints — recruitment intakes
// already build a `recruitment` payload object the n8n flow can route on.

import "dotenv/config";
import { PrismaClient } from "../src/generated/prisma/client.js";
import { PrismaLibSql } from "@prisma/adapter-libsql";

const RECRUITMENT_WEBHOOK_URL =
  "https://n8n.janusd.io/webhook/655723ae-5213-4a5e-97c8-c2e4781067d1";

async function main() {
  const dbUrl = process.env.DATABASE_URL ?? "file:./dev.db";
  const adapter = new PrismaLibSql({ url: dbUrl });
  const prisma = new PrismaClient({ adapter });

  try {
    console.log(`Seeding recruitment webhook → ${RECRUITMENT_WEBHOOK_URL}`);

    // url is not @unique on WebhookEndpoint, so match-then-create.
    const existing = await prisma.webhookEndpoint.findFirst({
      where: { url: RECRUITMENT_WEBHOOK_URL },
    });

    const events = JSON.stringify(["form.submitted"]);

    if (existing) {
      const updated = await prisma.webhookEndpoint.update({
        where: { id: existing.id },
        data: { isActive: true, events },
      });
      console.log(`  ✓ Updated existing endpoint ${updated.id} (active=${updated.isActive})`);
    } else {
      const created = await prisma.webhookEndpoint.create({
        data: { url: RECRUITMENT_WEBHOOK_URL, events, isActive: true },
      });
      console.log(`  ✓ Created endpoint ${created.id}`);
    }

    console.log("Done.");
  } finally {
    // PrismaClient with LibSql adapter doesn't need explicit disconnect
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});

```