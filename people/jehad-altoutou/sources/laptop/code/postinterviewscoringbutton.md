---
type: source
source_type: laptop
title: PostInterviewScoringButton
slug: postinterviewscoringbutton
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/recruitment/[id]/PostInterviewScoringButton.tsx"
original_size: 7785
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# PostInterviewScoringButton

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/[id]/PostInterviewScoringButton.tsx` on 2026-05-14._

```tsx
"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { AlertTriangle, CheckCircle2, FileText, Loader2, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";

type Props = {
  applicationId: string;
  currentStage: string;
  candidateName: string;
};

const STAGES_BLOCKING_POST_SCORE = new Set(["offer", "hired", "rejected", "withdrawn"]);

export function PostInterviewScoringButton({ applicationId, currentStage, candidateName }: Props) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();
  const [open, setOpen] = useState(false);
  const [transcript, setTranscript] = useState("");
  const [sourceRef, setSourceRef] = useState("manual transcript");
  const [interviewDate, setInterviewDate] = useState("");
  const [interviewer, setInterviewer] = useState("");
  const [interviewFormat, setInterviewFormat] = useState("Manual notes");
  const [durationMin, setDurationMin] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<{ scoreOutOf100: number; recommendation: string } | null>(null);

  const blocked = STAGES_BLOCKING_POST_SCORE.has(currentStage);
  const close = () => {
    setOpen(false);
    setError(null);
    setSuccess(null);
  };

  const handleSubmit = async () => {
    setSubmitting(true);
    setError(null);
    try {
      const res = await fetch(`/api/admin/recruitment/applications/${applicationId}/post-score`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          transcript,
          sourceRef,
          interviewDate: interviewDate || null,
          interviewer: interviewer || null,
          interviewFormat: interviewFormat || null,
          durationMin: durationMin ? Number(durationMin) : null,
        }),
      });
      const data = await res.json();
      if (!res.ok) {
        setError(data.error ?? "Failed to score interview");
        setSubmitting(false);
        return;
      }
      setSuccess({
        scoreOutOf100: data.scoreOutOf100,
        recommendation: data.recommendation,
      });
      startTransition(() => router.refresh());
    } catch {
      setError("Network error");
    }
    setSubmitting(false);
  };

  return (
    <>
      <Button
        type="button"
        variant="outline"
        onClick={() => setOpen(true)}
        disabled={blocked}
        title={blocked ? "This application is closed or already in offer workflow." : undefined}
        className="gap-2"
      >
        <FileText className="size-4" />
        Score Interview
      </Button>

      {open && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          <div className="fixed inset-0 bg-black/50" onClick={close} />
          <div className="relative z-10 max-h-[90vh] w-full max-w-2xl overflow-y-auto rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
            <div className="mb-4 flex items-center justify-between">
              <h3 className="text-base font-semibold">
                {success ? "Interview scored" : "Score post-interview"}
              </h3>
              <button onClick={close} className="rounded-md p-1 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800">
                <X className="size-4" />
              </button>
            </div>

            {!success ? (
              <>
                <p className="mb-4 text-sm text-muted-foreground">
                  Paste transcript or interviewer notes for <strong className="text-foreground">{candidateName}</strong>.
                </p>

                <div className="mb-4 grid grid-cols-1 gap-3 sm:grid-cols-2">
                  <div>
                    <Label htmlFor="source-ref">Source</Label>
                    <Input id="source-ref" value={sourceRef} onChange={(e) => setSourceRef(e.target.value)} className="mt-1.5" />
                  </div>
                  <div>
                    <Label htmlFor="interview-date">Date</Label>
                    <Input id="interview-date" type="date" value={interviewDate} onChange={(e) => setInterviewDate(e.target.value)} className="mt-1.5" />
                  </div>
                  <div>
                    <Label htmlFor="interviewer">Interviewer</Label>
                    <Input id="interviewer" value={interviewer} onChange={(e) => setInterviewer(e.target.value)} className="mt-1.5" />
                  </div>
                  <div className="grid grid-cols-[1fr_7rem] gap-2">
                    <div>
                      <Label htmlFor="interview-format">Format</Label>
                      <Input id="interview-format" value={interviewFormat} onChange={(e) => setInterviewFormat(e.target.value)} className="mt-1.5" />
                    </div>
                    <div>
                      <Label htmlFor="duration-min">Minutes</Label>
                      <Input id="duration-min" type="number" min={0} value={durationMin} onChange={(e) => setDurationMin(e.target.value)} className="mt-1.5" />
                    </div>
                  </div>
                </div>

                <div className="mb-4">
                  <Label htmlFor="transcript">Transcript / notes</Label>
                  <Textarea
                    id="transcript"
                    value={transcript}
                    onChange={(e) => setTranscript(e.target.value)}
                    rows={12}
                    className="mt-1.5 font-mono text-xs"
                  />
                  <div className="mt-1 text-right text-[11px] text-muted-foreground">
                    {transcript.trim().length.toLocaleString()} characters
                  </div>
                </div>

                {error && (
                  <div className="mb-3 flex items-start gap-2 rounded-lg bg-red-50 p-2.5 text-xs text-red-700 dark:bg-red-950 dark:text-red-300">
                    <AlertTriangle className="mt-0.5 size-3.5 shrink-0" />
                    <span>{error}</span>
                  </div>
                )}

                <div className="flex justify-end gap-2">
                  <Button variant="outline" onClick={close} disabled={submitting}>
                    Cancel
                  </Button>
                  <Button onClick={handleSubmit} disabled={submitting || transcript.trim().length < 80} className="gap-2">
                    {submitting ? <Loader2 className="size-4 animate-spin" /> : <FileText className="size-4" />}
                    Score interview
                  </Button>
                </div>
              </>
            ) : (
              <>
                <div className="mb-4 flex items-start gap-3 rounded-lg bg-emerald-50 p-3 text-sm text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200">
                  <CheckCircle2 className="mt-0.5 size-4 shrink-0" />
                  <div>
                    <p className="font-medium">Post-interview report generated.</p>
                    <p className="mt-0.5 text-xs">
                      Score {success.scoreOutOf100.toFixed(1)}/100 · {success.recommendation}
                    </p>
                  </div>
                </div>
                <div className="flex justify-end">
                  <Button onClick={close} disabled={isPending}>
                    Done
                  </Button>
                </div>
              </>
            )}
          </div>
        </div>
      )}
    </>
  );
}

```