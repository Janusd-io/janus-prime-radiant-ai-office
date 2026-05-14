---
type: source
source_type: laptop
title: page
slug: page-39
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/assess/eggs/page.tsx
original_size: 6915
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/assess/eggs/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Fingerprint, ArrowRight, Loader2, RotateCcw } from "lucide-react";

export default function EggHuntResumePage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [hasSaved, setHasSaved] = useState(false);

  // Check if there's a saved session in localStorage
  useEffect(() => {
    const saved = localStorage.getItem("assessify_egg_hunt");
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        if (parsed.sessionId && parsed.email) {
          // eslint-disable-next-line react-hooks/set-state-in-effect
          setEmail(parsed.email);
          setHasSaved(true);
        }
      } catch {
        // ignore — corrupt/old localStorage value
      }
    }
  }, []);

  const handleResumeSaved = () => {
    const saved = localStorage.getItem("assessify_egg_hunt");
    if (!saved) return;
    try {
      const parsed = JSON.parse(saved);
      router.push(`/assess/${parsed.sessionId}/eggs`);
    } catch { /* ignore */ }
  };

  const handleResumeByEmail = async () => {
    if (!email.trim()) return;
    setIsLoading(true);
    setError(null);

    try {
      // Find a session by email
      const res = await fetch(
        `/api/easter/claim?email=${encodeURIComponent(email.trim())}`
      );
      const data = await res.json();

      // If they have claims, they have a session — find it
      if (data.claims?.length > 0) {
        // We need to find their session. Check analytics events.
        // For now, look up their most recent completed session
        const sessRes = await fetch(
          `/api/easter/resume?email=${encodeURIComponent(email.trim())}`
        );
        const sessData = await sessRes.json();

        if (sessData.sessionId) {
          // Save to localStorage for future
          localStorage.setItem(
            "assessify_egg_hunt",
            JSON.stringify({
              sessionId: sessData.sessionId,
              email: email.trim(),
              name: sessData.candidateName ?? "",
              lastVisit: new Date().toISOString(),
            })
          );
          router.push(`/assess/${sessData.sessionId}/eggs`);
          return;
        }
      }

      // Try finding session directly
      const sessRes = await fetch(
        `/api/easter/resume?email=${encodeURIComponent(email.trim())}`
      );
      const sessData = await sessRes.json();

      if (sessData.sessionId) {
        localStorage.setItem(
          "assessify_egg_hunt",
          JSON.stringify({
            sessionId: sessData.sessionId,
            email: email.trim(),
            name: sessData.candidateName ?? "",
            lastVisit: new Date().toISOString(),
          })
        );
        router.push(`/assess/${sessData.sessionId}/eggs`);
      } else {
        setError(
          "No assessment session found for this email. Complete the assessment first to unlock the egg hunt."
        );
      }
    } catch {
      setError("Something went wrong. Please try again.");
    }
    setIsLoading(false);
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 px-4 dark:bg-zinc-950">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
        className="w-full max-w-sm"
      >
        <div className="mb-8 text-center">
          <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-zinc-900 dark:bg-zinc-100">
            <Fingerprint className="size-7 text-white dark:text-zinc-900" />
          </div>
          <h1 className="text-2xl font-bold tracking-tight">
            Resume Egg Hunt
          </h1>
          <p className="mt-1 text-sm text-muted-foreground">
            Pick up where you left off
          </p>
        </div>

        <div className="space-y-4">
          {hasSaved && (
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
            >
              <button
                onClick={handleResumeSaved}
                className="flex w-full items-center gap-4 rounded-xl border border-zinc-200 bg-white p-4 text-left transition-colors hover:bg-zinc-50 dark:border-zinc-800 dark:bg-zinc-900 dark:hover:bg-zinc-800/50"
              >
                <div className="rounded-lg bg-emerald-50 p-2 dark:bg-emerald-950">
                  <RotateCcw className="size-5 text-emerald-600 dark:text-emerald-400" />
                </div>
                <div className="flex-1">
                  <p className="text-sm font-semibold">Continue your hunt</p>
                  <p className="text-xs text-muted-foreground">
                    Saved session found for {email}
                  </p>
                </div>
                <ArrowRight className="size-4 text-muted-foreground" />
              </button>
            </motion.div>
          )}

          <div className="rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900">
            <div className="space-y-3">
              <div>
                <Label htmlFor="email">
                  {hasSaved ? "Or enter a different email" : "Your email address"}
                </Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="you@company.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="mt-1.5"
                  onKeyDown={(e) => e.key === "Enter" && handleResumeByEmail()}
                />
                <p className="mt-1 text-[10px] text-muted-foreground">
                  Enter the email you used for the assessment.
                </p>
              </div>

              {error && (
                <p className="text-xs text-red-600 dark:text-red-400">
                  {error}
                </p>
              )}

              <Button
                onClick={handleResumeByEmail}
                disabled={!email.trim() || isLoading}
                className="w-full gap-2"
              >
                {isLoading ? (
                  <Loader2 className="size-4 animate-spin" />
                ) : (
                  <>
                    Resume <ArrowRight className="size-4" />
                  </>
                )}
              </Button>
            </div>
          </div>
        </div>
      </motion.div>
    </div>
  );
}

```