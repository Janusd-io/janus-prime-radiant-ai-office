---
type: source
source_type: laptop
title: SendInviteButton
slug: sendinvitebutton
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/recruitment/[id]/SendInviteButton.tsx"
original_size: 14342
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# SendInviteButton

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/[id]/SendInviteButton.tsx` on 2026-05-14._

```tsx
"use client";

/**
 * Schedule Interview button + modal.
 *
 * The filename is `SendInviteButton.tsx` for backwards compat with the page
 * that imports it; the component is now the Phase 1.D interview scheduler.
 * Books a Google Calendar event with Meet + Fireflies, persists Interview,
 * advances Application to `interview_scheduled`, and emails the candidate.
 */
import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  AlertTriangle,
  Loader2,
  CalendarClock,
  X,
  CheckCircle2,
  ExternalLink,
} from "lucide-react";

type Props = {
  applicationId: string;
  currentStage: string;
  candidateName: string;
  candidateEmail: string;
  roleTitle: string;
};

const TERMINAL_STAGES = new Set(["hired", "rejected", "withdrawn"]);

type Alternative = { start: string; end: string };

type Success = {
  interviewId: string;
  scheduledAt: string;
  durationMin: number;
  interviewerEmail: string;
  meetUrl: string | null;
  calendarHtmlLink: string | null;
  mock: boolean;
};

export function SendInviteButton({
  applicationId,
  currentStage,
  candidateName,
  candidateEmail,
  roleTitle,
}: Props) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();
  const [open, setOpen] = useState(false);

  const defaults = nextBusinessSlotDefaults();
  const [date, setDate] = useState(defaults.date);
  const [time, setTime] = useState(defaults.time);
  const [duration, setDuration] = useState(60);
  const [notes, setNotes] = useState("");

  const [error, setError] = useState<string | null>(null);
  const [alternatives, setAlternatives] = useState<Alternative[] | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [success, setSuccess] = useState<Success | null>(null);

  const blocked = TERMINAL_STAGES.has(currentStage);
  const blockedReason = blocked
    ? "This application is closed — re-open it before scheduling an interview."
    : null;

  const close = () => {
    setOpen(false);
    setError(null);
    setAlternatives(null);
    setSuccess(null);
  };

  const applyAlternative = (alt: Alternative) => {
    const d = new Date(alt.start);
    const local = dubaiPartsFromIso(d);
    setDate(local.date);
    setTime(local.time);
    setAlternatives(null);
    setError(null);
  };

  const handleSchedule = async () => {
    setSubmitting(true);
    setError(null);
    setAlternatives(null);
    try {
      const res = await fetch(
        `/api/admin/recruitment/applications/${applicationId}/schedule-interview`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ date, time, durationMin: duration, notes }),
        },
      );
      const data = await res.json();
      if (!res.ok) {
        setError(data.error ?? "Failed to schedule");
        if (data.conflict && Array.isArray(data.alternatives)) {
          setAlternatives(data.alternatives);
        }
        setSubmitting(false);
        return;
      }
      setSuccess({
        interviewId: data.interview.id,
        scheduledAt: data.interview.scheduledAt,
        durationMin: data.interview.durationMin,
        interviewerEmail: data.interview.interviewerEmail,
        meetUrl: data.interview.meetUrl,
        calendarHtmlLink: data.interview.calendarHtmlLink,
        mock: !!data.mock,
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
        onClick={() => setOpen(true)}
        disabled={blocked}
        title={blockedReason ?? undefined}
        className="gap-2"
      >
        <CalendarClock className="size-4" />
        Schedule Interview
      </Button>

      {open && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          <div className="fixed inset-0 bg-black/50" onClick={close} />
          <div className="relative z-10 w-full max-w-md rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
            <div className="mb-4 flex items-center justify-between">
              <h3 className="text-base font-semibold">
                {success ? "Interview scheduled" : "Schedule Interview"}
              </h3>
              <button
                onClick={close}
                className="rounded-md p-1 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800"
              >
                <X className="size-4" />
              </button>
            </div>

            {!success ? (
              <>
                <div className="mb-4 rounded-lg bg-zinc-50 p-3 text-xs dark:bg-zinc-800/50">
                  <div className="flex justify-between">
                    <span className="text-muted-foreground">Candidate</span>
                    <span className="font-medium">{candidateName}</span>
                  </div>
                  <div className="mt-1 flex justify-between">
                    <span className="text-muted-foreground">Role</span>
                    <span>{roleTitle}</span>
                  </div>
                  <div className="mt-1 flex justify-between">
                    <span className="text-muted-foreground">Email</span>
                    <span>{candidateEmail}</span>
                  </div>
                </div>

                <div className="mb-3 grid grid-cols-2 gap-3">
                  <div>
                    <Label htmlFor="iv-date">Date (Dubai)</Label>
                    <Input
                      id="iv-date"
                      type="date"
                      value={date}
                      onChange={(e) => setDate(e.target.value)}
                      className="mt-1.5"
                    />
                  </div>
                  <div>
                    <Label htmlFor="iv-time">Start time</Label>
                    <Input
                      id="iv-time"
                      type="time"
                      step={900}
                      value={time}
                      onChange={(e) => setTime(e.target.value)}
                      className="mt-1.5"
                    />
                  </div>
                </div>

                <div className="mb-3">
                  <Label htmlFor="iv-duration">Duration</Label>
                  <select
                    id="iv-duration"
                    value={duration}
                    onChange={(e) => setDuration(Number(e.target.value))}
                    className="mt-1.5 w-full rounded-md border border-zinc-200 bg-white px-3 py-2 text-sm dark:border-zinc-700 dark:bg-zinc-900"
                  >
                    <option value={30}>30 min</option>
                    <option value={45}>45 min</option>
                    <option value={60}>60 min</option>
                    <option value={90}>90 min</option>
                  </select>
                </div>

                <div className="mb-4">
                  <Label htmlFor="iv-notes">Notes for the candidate (optional)</Label>
                  <textarea
                    id="iv-notes"
                    value={notes}
                    onChange={(e) => setNotes(e.target.value)}
                    rows={3}
                    placeholder="Included in the calendar invite description."
                    className="mt-1.5 w-full rounded-md border border-zinc-200 bg-white px-3 py-2 text-sm dark:border-zinc-700 dark:bg-zinc-900"
                  />
                </div>

                {error && (
                  <div className="mb-3 flex items-start gap-2 rounded-lg bg-red-50 p-2.5 text-xs text-red-700 dark:bg-red-950 dark:text-red-300">
                    <AlertTriangle className="mt-0.5 size-3.5 shrink-0" />
                    <span>{error}</span>
                  </div>
                )}

                {alternatives && alternatives.length > 0 && (
                  <div className="mb-3 rounded-lg border border-amber-200 bg-amber-50 p-3 text-xs dark:border-amber-900 dark:bg-amber-950">
                    <p className="mb-2 font-semibold text-amber-900 dark:text-amber-100">
                      Next open slots:
                    </p>
                    <div className="flex flex-col gap-1.5">
                      {alternatives.map((a) => (
                        <button
                          key={a.start}
                          onClick={() => applyAlternative(a)}
                          className="rounded-md border border-amber-300 bg-white px-2.5 py-1.5 text-left text-amber-900 hover:bg-amber-100 dark:border-amber-800 dark:bg-amber-900/40 dark:text-amber-100 dark:hover:bg-amber-900/70"
                        >
                          {formatAlternative(a.start)}
                        </button>
                      ))}
                    </div>
                  </div>
                )}

                <div className="flex justify-end gap-2">
                  <Button variant="outline" onClick={close} disabled={submitting}>
                    Cancel
                  </Button>
                  <Button onClick={handleSchedule} disabled={submitting} className="gap-2">
                    {submitting ? (
                      <Loader2 className="size-4 animate-spin" />
                    ) : (
                      <CalendarClock className="size-4" />
                    )}
                    Book
                  </Button>
                </div>
              </>
            ) : (
              <>
                <div className="mb-4 flex items-start gap-3 rounded-lg bg-emerald-50 p-3 text-sm text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200">
                  <CheckCircle2 className="mt-0.5 size-4 shrink-0" />
                  <div>
                    <p className="font-medium">
                      {success.mock ? "Mock event booked." : "Calendar event booked."}
                    </p>
                    <p className="mt-0.5 text-xs">
                      {formatSuccessTime(success.scheduledAt, success.durationMin)} with{" "}
                      {success.interviewerEmail}. Confirmation email sent to {candidateEmail}.
                    </p>
                  </div>
                </div>

                <div className="space-y-2 text-sm">
                  {success.meetUrl && (
                    <a
                      href={success.meetUrl}
                      target="_blank"
                      rel="noreferrer"
                      className="flex items-center justify-between rounded-md border border-zinc-200 px-3 py-2 hover:bg-zinc-50 dark:border-zinc-700 dark:hover:bg-zinc-800"
                    >
                      <span>Google Meet link</span>
                      <ExternalLink className="size-3.5 text-muted-foreground" />
                    </a>
                  )}
                  {success.calendarHtmlLink && (
                    <a
                      href={success.calendarHtmlLink}
                      target="_blank"
                      rel="noreferrer"
                      className="flex items-center justify-between rounded-md border border-zinc-200 px-3 py-2 hover:bg-zinc-50 dark:border-zinc-700 dark:hover:bg-zinc-800"
                    >
                      <span>Open in Google Calendar</span>
                      <ExternalLink className="size-3.5 text-muted-foreground" />
                    </a>
                  )}
                </div>

                <div className="mt-4 flex justify-end">
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

// ─── helpers ─────────────────────────────────────────────────

function nextBusinessSlotDefaults(): { date: string; time: string } {
  const tz = "Asia/Dubai";
  const now = new Date();
  const fmt = new Intl.DateTimeFormat("en-CA", {
    timeZone: tz,
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    weekday: "short",
  });
  const parts = fmt.formatToParts(now);
  const y = Number(parts.find((p) => p.type === "year")?.value);
  const m = Number(parts.find((p) => p.type === "month")?.value);
  const d = Number(parts.find((p) => p.type === "day")?.value);
  const dowStr = parts.find((p) => p.type === "weekday")?.value ?? "Mon";
  const dayMap: Record<string, number> = {
    Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6,
  };
  const dow = dayMap[dowStr] ?? 1;
  const base = new Date(Date.UTC(y, m - 1, d));
  let addDays = 1;
  while (true) {
    const next = (dow + addDays) % 7;
    if (next !== 0 && next !== 6) break;
    addDays += 1;
  }
  base.setUTCDate(base.getUTCDate() + addDays);
  return { date: base.toISOString().slice(0, 10), time: "10:00" };
}

function dubaiPartsFromIso(d: Date): { date: string; time: string } {
  const fmt = new Intl.DateTimeFormat("en-CA", {
    timeZone: "Asia/Dubai",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  });
  const parts = fmt.formatToParts(d);
  const get = (t: string) => parts.find((p) => p.type === t)?.value ?? "00";
  return {
    date: `${get("year")}-${get("month")}-${get("day")}`,
    time: `${get("hour")}:${get("minute")}`,
  };
}

function formatAlternative(iso: string): string {
  const d = new Date(iso);
  return new Intl.DateTimeFormat("en-GB", {
    timeZone: "Asia/Dubai",
    weekday: "short",
    day: "numeric",
    month: "short",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  }).format(d) + " GST";
}

function formatSuccessTime(iso: string, durationMin: number): string {
  const d = new Date(iso);
  const fmt = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Asia/Dubai",
    weekday: "short",
    day: "numeric",
    month: "short",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  });
  return `${fmt.format(d)} GST (${durationMin} min)`;
}

```