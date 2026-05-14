---
type: source
source_type: laptop
title: post-score-service.test
slug: post-score-service-test
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/__tests__/post-score-service.test.ts
original_size: 1122
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# post-score-service.test

_Extracted from `assessify/src/lib/__tests__/post-score-service.test.ts` on 2026-05-14._

```typescript
import { describe, expect, it } from "vitest";
import {
  MAX_TRANSCRIPT_LENGTH,
  MIN_TRANSCRIPT_LENGTH,
  normalizeDuration,
  validateTranscript,
} from "@/lib/recruitment/post-score-service";

describe("validateTranscript", () => {
  it("trims and accepts a transcript above minimum length", () => {
    const transcript = ` ${"A".repeat(MIN_TRANSCRIPT_LENGTH)} `;
    expect(validateTranscript(transcript)).toHaveLength(MIN_TRANSCRIPT_LENGTH);
  });

  it("rejects short transcripts", () => {
    expect(() => validateTranscript("Too short")).toThrow(/at least/);
  });

  it("rejects oversized transcripts", () => {
    expect(() => validateTranscript("A".repeat(MAX_TRANSCRIPT_LENGTH + 1))).toThrow(/too long/);
  });
});

describe("normalizeDuration", () => {
  it("keeps valid positive durations", () => {
    expect(normalizeDuration(44)).toBe(44);
    expect(normalizeDuration("30")).toBe(30);
  });

  it("returns null for invalid durations", () => {
    expect(normalizeDuration(-1)).toBeNull();
    expect(normalizeDuration("oops")).toBeNull();
    expect(normalizeDuration(undefined)).toBeNull();
  });
});

```