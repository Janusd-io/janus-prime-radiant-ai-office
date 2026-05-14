---
type: source
source_type: laptop
title: file-validation
slug: file-validation
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/file-validation.ts
original_size: 1247
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# file-validation

_Extracted from `[[assessify|assessify]]/src/lib/file-validation.ts` on 2026-05-14._

```typescript
// Region-based file format rules
// UAE: JPEG, PNG only (legal document requirements)
// Global (Singapore, UK, etc.): JPEG, PNG, PDF

export const FILE_RULES: Record<string, { formats: string[]; mimeTypes: string[]; label: string }> = {
  uae: {
    formats: ["JPEG"],
    mimeTypes: ["image/jpeg"],
    label: "JPEG only (UAE requirement)",
  },
  global: {
    formats: ["JPEG", "PNG", "PDF"],
    mimeTypes: ["image/jpeg", "image/png", "application/pdf"],
    label: "JPEG, PNG, or PDF",
  },
};

export const MAX_FILE_SIZE = 1 * 1024 * 1024; // 1MB

export function getFileRules(region: string) {
  return FILE_RULES[region] ?? FILE_RULES.global;
}

export function validateFile(
  file: { type: string; size: number; name: string },
  region: string
): { valid: boolean; error?: string } {
  const rules = getFileRules(region);

  if (!rules.mimeTypes.includes(file.type)) {
    return {
      valid: false,
      error: `Invalid file format. Accepted formats for ${region === "uae" ? "UAE" : "your region"}: ${rules.formats.join(", ")}`,
    };
  }

  if (file.size > MAX_FILE_SIZE) {
    return {
      valid: false,
      error: `File too large. Maximum size is ${MAX_FILE_SIZE / 1024 / 1024}MB`,
    };
  }

  return { valid: true };
}

```