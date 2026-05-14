---
type: source
source_type: laptop
title: route
slug: route
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/easter/route.ts
original_size: 550
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/easter/route.ts` on 2026-05-14._

```typescript
import { rot13 } from "@/lib/easter-eggs";

// The gateway to the impossible egg
// Discoverable via robots.txt → /api/easter/
export async function GET() {
  // ROT13 of "egg{the_impossible_is_just_the_untried}"
  const cipher = rot13("egg{the_impossible_is_just_the_untried}");

  return Response.json({
    "🥚": "So you found the door. But can you find the key?",
    cipher,
    instructions:
      "This message is encrypted. Decode it, then POST your answer to /api/easter/claim with your name and email to prove you cracked it.",
  });
}

```