---
type: source
source_type: laptop
title: page
slug: page-35
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/assess/invite/[code]/page.tsx"
original_size: 7194
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/assess/invite/[code]/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import {
  Loader2,
  Sparkles,
  ArrowRight,
  Clock,
  Layers,
  HelpCircle,
  AlertTriangle,
} from "lucide-react";

interface InviteData {
  invite: {
    id: string;
    code: string;
    candidateName: string;
    candidateEmail: string;
    status: string;
    expiresAt: string | null;
  };
  assessment: {
    title: string;
    slug: string;
    description: string;
    department: string;
    jobRole: string;
    timeLimit: number | null;
    sectionCount: number;
    questionCount: number;
  };
}

export default function InvitePage({
  params,
}: {
  params: Promise<{ code: string }>;
}) {
  const router = useRouter();
  const [data, setData] = useState<InviteData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isStarting, setIsStarting] = useState(false);

  useEffect(() => {
    params.then((p) => {
      fetch(`/api/assess/invite/${p.code}`)
        .then((r) => r.json())
        .then((d) => {
          if (d.error) {
            setError(d.error);
          } else {
            setData(d);
          }
        })
        .catch(() => setError("Failed to load invite."));
    });
  }, [params]);

  const handleStart = async () => {
    if (!data) return;
    setIsStarting(true);

    try {
      const res = await fetch(`/api/assess/invite/${data.invite.code}/start`, {
        method: "POST",
      });
      const result = await res.json();

      if (!res.ok) {
        setError(result.error || "Failed to start assessment.");
        setIsStarting(false);
        return;
      }

      router.push(`/assess/${result.sessionId}`);
    } catch {
      setError("Something went wrong. Please try again.");
      setIsStarting(false);
    }
  };

  if (error) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 px-4 dark:bg-zinc-950">
        <div className="max-w-sm text-center">
          <AlertTriangle className="mx-auto mb-4 size-12 text-red-500" />
          <h1 className="mb-2 text-xl font-bold">Unable to Load Invite</h1>
          <p className="text-sm text-muted-foreground">{error}</p>
        </div>
      </div>
    );
  }

  if (!data) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <Loader2 className="size-8 animate-spin text-primary" />
      </div>
    );
  }

  const isExpired =
    data.invite.expiresAt && new Date(data.invite.expiresAt) < new Date();
  const isAlreadyUsed =
    data.invite.status === "started" || data.invite.status === "completed";

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 px-4 dark:bg-zinc-950">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
        className="w-full max-w-md"
      >
        <div className="mb-8 text-center">
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.1 }}
            className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-primary/10"
          >
            <Sparkles className="size-7 text-primary" />
          </motion.div>
          <h1 className="text-2xl font-bold tracking-tight">
            Welcome, {data.invite.candidateName}
          </h1>
          <p className="mt-1 text-sm text-muted-foreground">
            You have been invited to take an assessment
          </p>
        </div>

        <div className="rounded-2xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-900">
          {/* Assessment info */}
          <div className="mb-5">
            <h2 className="text-lg font-semibold">{data.assessment.title}</h2>
            <p className="mt-0.5 text-xs text-muted-foreground">
              {data.assessment.department} &middot; {data.assessment.jobRole}
            </p>
            {data.assessment.description && (
              <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
                {data.assessment.description}
              </p>
            )}
          </div>

          {/* Stats */}
          <div className="mb-5 grid grid-cols-3 gap-3">
            <div className="rounded-lg bg-zinc-50 p-3 text-center dark:bg-zinc-800/50">
              <Layers className="mx-auto mb-1 size-4 text-muted-foreground" />
              <p className="text-sm font-bold">{data.assessment.sectionCount}</p>
              <p className="text-[10px] text-muted-foreground">Sections</p>
            </div>
            <div className="rounded-lg bg-zinc-50 p-3 text-center dark:bg-zinc-800/50">
              <HelpCircle className="mx-auto mb-1 size-4 text-muted-foreground" />
              <p className="text-sm font-bold">{data.assessment.questionCount}</p>
              <p className="text-[10px] text-muted-foreground">Questions</p>
            </div>
            <div className="rounded-lg bg-zinc-50 p-3 text-center dark:bg-zinc-800/50">
              <Clock className="mx-auto mb-1 size-4 text-muted-foreground" />
              <p className="text-sm font-bold">
                {data.assessment.timeLimit ?? "No limit"}
              </p>
              <p className="text-[10px] text-muted-foreground">
                {data.assessment.timeLimit ? "Minutes" : ""}
              </p>
            </div>
          </div>

          {/* Expiry warning */}
          {isExpired && (
            <div className="mb-4 rounded-lg bg-red-50 p-3 text-xs text-red-700 dark:bg-red-950 dark:text-red-300">
              This invite has expired. Please contact the hiring team for a new
              link.
            </div>
          )}

          {isAlreadyUsed && !isExpired && (
            <div className="mb-4 rounded-lg bg-amber-50 p-3 text-xs text-amber-700 dark:bg-amber-950 dark:text-amber-300">
              You have already started this assessment. Redirecting you to
              continue.
            </div>
          )}

          {/* CTA */}
          {!isExpired && (
            <Button
              onClick={handleStart}
              disabled={isStarting}
              className="w-full gap-2"
              size="lg"
            >
              {isStarting ? (
                <Loader2 className="size-4 animate-spin" />
              ) : isAlreadyUsed ? (
                <>
                  Continue Assessment <ArrowRight className="size-4" />
                </>
              ) : (
                <>
                  Start Assessment <ArrowRight className="size-4" />
                </>
              )}
            </Button>
          )}
        </div>

        <p className="mt-4 text-center text-[10px] text-muted-foreground">
          This invite is for {data.invite.candidateEmail}
          {data.invite.expiresAt &&
            !isExpired &&
            ` · Expires ${new Date(data.invite.expiresAt).toLocaleDateString()}`}
        </p>
      </motion.div>
    </div>
  );
}

```