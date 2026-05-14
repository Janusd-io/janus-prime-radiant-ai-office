---
type: source
source_type: laptop
title: webhooks
slug: webhooks
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/webhooks.ts
original_size: 2422
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# webhooks

_Extracted from `[[assessify|assessify]]/src/lib/webhooks.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import type { WebhookPayload } from "@/types/assessment";
import crypto from "crypto";
import { slackAlert } from "@/lib/slack";

export async function dispatchWebhook(
  eventType: string,
  data: Record<string, unknown>
) {
  const endpoints = await prisma.webhookEndpoint.findMany({
    where: { isActive: true },
  });

  const payload: WebhookPayload = {
    event: eventType,
    timestamp: new Date().toISOString(),
    data,
  };

  const deliveries = [];

  for (const endpoint of endpoints) {
    const subscribedEvents: string[] = JSON.parse(endpoint.events);
    if (!subscribedEvents.includes(eventType) && !subscribedEvents.includes("*")) {
      continue;
    }

    const body = JSON.stringify(payload);
    const signature = endpoint.secret
      ? crypto.createHmac("sha256", endpoint.secret).update(body).digest("hex")
      : null;

    try {
      const res = await fetch(endpoint.url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(signature ? { "X-Webhook-Signature": signature } : {}),
          "X-Webhook-Event": eventType,
        },
        body,
      });

      const responseText = await res.text().catch(() => null);
      deliveries.push(
        prisma.webhookDelivery.create({
          data: {
            endpointId: endpoint.id,
            eventType,
            payload: body,
            statusCode: res.status,
            response: responseText,
            deliveredAt: new Date(),
          },
        })
      );
      if (res.status >= 400) {
        slackAlert(`Webhook ${res.status} — ${eventType}`, `POST ${endpoint.url} returned ${res.status}`, {
          endpoint: endpoint.url,
          event: eventType,
          statusCode: res.status,
          response: responseText?.slice(0, 500) ?? null,
        });
      }
    } catch (error) {
      deliveries.push(
        prisma.webhookDelivery.create({
          data: {
            endpointId: endpoint.id,
            eventType,
            payload: body,
            statusCode: 0,
            response: error instanceof Error ? error.message : "Unknown error",
          },
        })
      );
      slackAlert(`Webhook network error — ${eventType}`, error, {
        endpoint: endpoint.url,
        event: eventType,
      });
    }
  }

  if (deliveries.length > 0) {
    await Promise.allSettled(deliveries);
  }
}

```