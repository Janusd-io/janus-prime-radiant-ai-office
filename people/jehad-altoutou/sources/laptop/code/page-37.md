---
type: source
source_type: laptop
title: page
slug: page-37
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/assess/[sessionId]/result/page.tsx"
original_size: 7451
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `[[assessify|assessify]]/src/app/assess/[sessionId]/result/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import {
  CheckCircle,
  Loader2,
  Mail,
  Building2,
  Fingerprint,
  ChevronRight,
} from "lucide-react";

export default function ResultPage({
  params,
}: {
  params: Promise<{ sessionId: string }>;
}) {
  const router = useRouter();
  const [loaded, setLoaded] = useState(false);
  const [candidateName, setCandidateName] = useState("");
  const [resolvedSessionId, setResolvedSessionId] = useState("");
  const [eggHuntEnabled, setEggHuntEnabled] = useState(false);

  useEffect(() => {
    params.then((p) => {
      setResolvedSessionId(p.sessionId);
      fetch(`/api/sessions/${p.sessionId}`)
        .then((r) => r.json())
        .then((d) => {
          setCandidateName(d.session?.candidateName ?? "");
          setEggHuntEnabled(d.session?.assessment?.eggHuntEnabled === true);
          setLoaded(true);
        })
        .catch(() => setLoaded(true));
    });
  }, [params]);

  if (!loaded) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <Loader2 className="size-8 animate-spin text-primary" />
      </div>
    );
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 px-4 py-12 dark:bg-zinc-950">
{/* Eggs are on the challenge pages, not here */}
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
        className="w-full max-w-lg"
      >
        <div className="text-center">
          <motion.div
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            transition={{ delay: 0.2, type: "spring", stiffness: 200 }}
            className="mx-auto mb-6 flex h-20 w-20 items-center justify-center rounded-full bg-green-100 dark:bg-green-950"
          >
            <CheckCircle className="size-10 text-green-600 dark:text-green-400" />
          </motion.div>

          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="mb-3 text-3xl font-bold tracking-tight"
          >
            Thank You{candidateName ? `, ${candidateName}` : ""}!
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
            className="mb-8 text-base leading-relaxed text-muted-foreground"
          >
            Your assessment has been submitted successfully. Our hiring team
            will review your responses and get back to you soon.
          </motion.p>
        </div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.5 }}
          className="space-y-4"
        >
          <div className="rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900">
            <div className="flex items-start gap-4">
              <div className="rounded-lg bg-blue-50 p-2 dark:bg-blue-950">
                <Mail className="size-5 text-blue-600 dark:text-blue-400" />
              </div>
              <div className="text-left">
                <h3 className="text-sm font-semibold">What happens next?</h3>
                <p className="mt-1 text-xs leading-relaxed text-muted-foreground">
                  Our team will carefully review your responses. You will receive
                  an email with next steps within a few business days.
                </p>
              </div>
            </div>
          </div>

          <div className="rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900">
            <div className="flex items-start gap-4">
              <div className="rounded-lg bg-purple-50 p-2 dark:bg-purple-950">
                <Building2 className="size-5 text-purple-600 dark:text-purple-400" />
              </div>
              <div className="text-left">
                <h3 className="text-sm font-semibold">About our process</h3>
                <p className="mt-1 text-xs leading-relaxed text-muted-foreground">
                  We evaluate candidates holistically — technical skills,
                  cultural alignment, and growth potential all matter to us.
                </p>
              </div>
            </div>
          </div>
        </motion.div>

        {/* Egg Hunt CTA — opt-in per assessment via AssessmentTemplate.eggHuntEnabled */}
        {eggHuntEnabled && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.7 }}
          className="mt-6"
        >
          <div className="overflow-hidden rounded-xl border border-zinc-200 bg-gradient-to-br from-zinc-900 to-zinc-800 p-6 text-white dark:from-zinc-800 dark:to-zinc-900">
            <div className="flex items-start gap-4">
              <div className="rounded-lg bg-white/10 p-2.5">
                <Fingerprint className="size-6 text-white/80" />
              </div>
              <div className="flex-1">
                <h3 className="text-base font-semibold">
                  Bonus: The Egg Hunt
                </h3>
                <p className="mt-1.5 text-sm leading-relaxed text-zinc-400">
                  Think you have what it takes? We have hidden{" "}
                  <strong className="text-zinc-200">4 easter eggs</strong>{" "}
                  across this platform — each one harder than the last. This
                  optional challenge tests curiosity, resourcefulness, and
                  technical thinking. Those who find them stand out.
                </p>
                <div className="mt-3 flex items-center gap-3">
                  <div className="flex gap-1.5">
                    <span className="h-2 w-2 rounded-full bg-emerald-400" title="Easy" />
                    <span className="h-2 w-2 rounded-full bg-blue-400" title="Medium" />
                    <span className="h-2 w-2 rounded-full bg-orange-400" title="Hard" />
                    <span className="h-2 w-2 rounded-full bg-red-400" title="Impossible" />
                  </div>
                  <span className="text-xs text-zinc-500">
                    Easy &middot; Medium &middot; Hard &middot; Impossible
                  </span>
                </div>
                <Button
                  onClick={() =>
                    router.push(`/assess/${resolvedSessionId}/eggs`)
                  }
                  className="mt-4 gap-2 bg-white text-zinc-900 hover:bg-zinc-100"
                >
                  Ready to Engage <ChevronRight className="size-4" />
                </Button>
              </div>
            </div>
          </div>
        </motion.div>
        )}

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.9 }}
          className="mt-6 text-center text-xs text-muted-foreground"
          aria-label={eggHuntEnabled ? "Some doors are hidden in plain sight. The robots know where they are." : undefined}
        >
          We appreciate your time and effort. Good luck!
        </motion.p>
      </motion.div>
    </div>
  );
}

```