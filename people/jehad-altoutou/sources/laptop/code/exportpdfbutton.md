---
type: source
source_type: laptop
title: ExportPdfButton
slug: exportpdfbutton
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/recruitment/[id]/ExportPdfButton.tsx"
original_size: 3860
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# ExportPdfButton

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/[id]/ExportPdfButton.tsx` on 2026-05-14._

```tsx
"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { AlertTriangle, Download, Loader2, X } from "lucide-react";

type Props = {
  applicationId: string;
};

export function ExportPdfButton({ applicationId }: Props) {
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [warning, setWarning] = useState<string | null>(null);

  const handleClick = async () => {
    setBusy(true);
    setError(null);
    setWarning(null);
    try {
      const res = await fetch(
        `/api/admin/recruitment/applications/${applicationId}/profile.pdf`,
      );
      if (!res.ok) {
        const detail = await readErrorDetail(res);
        setError(detail ?? `Failed to export PDF (${res.status})`);
        return;
      }
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const filename =
        parseFilename(res.headers.get("Content-Disposition")) ?? "candidate_profile.pdf";
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
      if (res.headers.get("X-PDF-Degraded") === "1") {
        setWarning("Exported a basics-only PDF — full report rendering failed. The team has been notified.");
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Network error");
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="relative">
      <Button
        type="button"
        variant="outline"
        onClick={handleClick}
        disabled={busy}
        className="gap-2"
      >
        {busy ? <Loader2 className="size-4 animate-spin" /> : <Download className="size-4" />}
        Export PDF
      </Button>

      {error && (
        <div className="absolute right-0 top-full z-20 mt-2 flex w-80 items-start gap-2 rounded-lg border border-red-200 bg-red-50 p-2.5 text-xs text-red-700 shadow-md dark:border-red-900 dark:bg-red-950 dark:text-red-300">
          <AlertTriangle className="mt-0.5 size-3.5 shrink-0" />
          <span className="flex-1 break-words">{error}</span>
          <button
            type="button"
            onClick={() => setError(null)}
            className="rounded p-0.5 hover:bg-red-100 dark:hover:bg-red-900"
            aria-label="Dismiss"
          >
            <X className="size-3.5" />
          </button>
        </div>
      )}

      {warning && !error && (
        <div className="absolute right-0 top-full z-20 mt-2 flex w-80 items-start gap-2 rounded-lg border border-amber-200 bg-amber-50 p-2.5 text-xs text-amber-800 shadow-md dark:border-amber-900 dark:bg-amber-950 dark:text-amber-200">
          <AlertTriangle className="mt-0.5 size-3.5 shrink-0" />
          <span className="flex-1 break-words">{warning}</span>
          <button
            type="button"
            onClick={() => setWarning(null)}
            className="rounded p-0.5 hover:bg-amber-100 dark:hover:bg-amber-900"
            aria-label="Dismiss"
          >
            <X className="size-3.5" />
          </button>
        </div>
      )}
    </div>
  );
}

async function readErrorDetail(res: Response): Promise<string | null> {
  try {
    const data = await res.json();
    if (data && typeof data === "object") {
      const detail = (data as { detail?: unknown }).detail;
      const error = (data as { error?: unknown }).error;
      if (typeof detail === "string" && detail) return `${error ?? "Error"}: ${detail}`;
      if (typeof error === "string") return error;
    }
  } catch {
    // not JSON
  }
  return null;
}

function parseFilename(header: string | null): string | null {
  if (!header) return null;
  const m = /filename="([^"]+)"/.exec(header);
  return m ? m[1] : null;
}

```