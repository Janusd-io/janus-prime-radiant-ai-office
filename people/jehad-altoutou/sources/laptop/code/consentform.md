---
type: source
source_type: laptop
title: ConsentForm
slug: consentform
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/oauth/authorize/ConsentForm.tsx
original_size: 2044
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# ConsentForm

_Extracted from `[[assessify|assessify]]/src/app/oauth/authorize/ConsentForm.tsx` on 2026-05-14._

```tsx
"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";

export function ConsentForm({
  clientId,
  redirectUri,
  codeChallenge,
  codeChallengeMethod,
  state,
  scope,
}: {
  clientId: string;
  redirectUri: string;
  codeChallenge: string;
  codeChallengeMethod: string;
  state: string;
  scope: string;
}) {
  const [submitting, setSubmitting] = useState<null | "approve" | "deny">(null);
  const [error, setError] = useState<string | null>(null);

  async function handle(decision: "approve" | "deny") {
    setSubmitting(decision);
    setError(null);
    try {
      const res = await fetch("/api/oauth/authorize/consent", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          decision,
          clientId,
          redirectUri,
          codeChallenge,
          codeChallengeMethod,
          state,
          scope,
        }),
      });
      const data = await res.json();
      if (!res.ok || !data.redirect) {
        setError(data.error ?? "Authorization failed");
        setSubmitting(null);
        return;
      }
      window.location.href = data.redirect;
    } catch {
      setError("Network error");
      setSubmitting(null);
    }
  }

  return (
    <>
      {error && (
        <div className="mt-4 rounded-lg border border-red-200 bg-red-50 p-3 text-sm text-red-800 dark:border-red-800 dark:bg-red-950 dark:text-red-200">
          {error}
        </div>
      )}
      <div className="mt-6 flex gap-3">
        <Button
          variant="outline"
          onClick={() => handle("deny")}
          disabled={submitting !== null}
          className="flex-1"
        >
          {submitting === "deny" ? "Denying…" : "Deny"}
        </Button>
        <Button
          onClick={() => handle("approve")}
          disabled={submitting !== null}
          className="flex-1"
        >
          {submitting === "approve" ? "Authorizing…" : "Approve"}
        </Button>
      </div>
    </>
  );
}

```