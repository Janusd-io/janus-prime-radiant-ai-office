---
type: source
source_type: laptop
title: page
slug: page-34
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/assess/page.tsx
original_size: 6289
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/assess/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { ArrowRight, Loader2, Sparkles } from "lucide-react";

interface Assessment {
  id: string;
  title: string;
  slug: string;
  description: string;
  jobRole: { title: string; department: string };
  version: { timeLimit: number | null };
  sections: { questionCount: number }[];
}

export default function AssessStartPage() {
  const router = useRouter();
  const [assessments, setAssessments] = useState<Assessment[]>([]);
  const [selectedSlug, setSelectedSlug] = useState<string>("");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/assessments")
      .then((r) => r.json())
      .then((d) => {
        setAssessments(d.assessments ?? []);
        if (d.assessments?.length === 1) {
          setSelectedSlug(d.assessments[0].slug);
        }
      });
  }, []);

  const selected = assessments.find((a) => a.slug === selectedSlug);

  const handleStart = async () => {
    if (!name.trim() || !email.trim() || !selectedSlug) return;
    setIsLoading(true);
    setError(null);

    try {
      const res = await fetch("/api/sessions", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          assessmentSlug: selectedSlug,
          candidateName: name.trim(),
          candidateEmail: email.trim(),
        }),
      });

      const data = await res.json();
      if (!res.ok) {
        setError(data.error || "Failed to start assessment");
        setIsLoading(false);
        return;
      }

      router.push(`/assess/${data.session.id}`);
    } catch {
      setError("Network error. Please try again.");
      setIsLoading(false);
    }
  };

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
            Welcome to Assessify
          </h1>
          <p className="mt-1 text-sm text-muted-foreground">
            Enter your details to begin
          </p>
        </div>

        <div className="rounded-2xl border border-zinc-200 bg-white p-6 shadow-sm dark:border-zinc-800 dark:bg-zinc-900">
          <div className="space-y-4">
            <div>
              <Label htmlFor="name">Full Name</Label>
              <Input
                id="name"
                placeholder="Jane Smith"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="mt-1.5"
              />
            </div>

            <div>
              <Label htmlFor="email">Email Address</Label>
              <Input
                id="email"
                type="email"
                placeholder="jane@company.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="mt-1.5"
              />
            </div>

            {assessments.length > 1 && (
              <div>
                <Label>Assessment</Label>
                <div className="mt-1.5 space-y-2">
                  {assessments.map((a) => (
                    <button
                      key={a.slug}
                      onClick={() => setSelectedSlug(a.slug)}
                      className={`w-full rounded-lg border-2 p-3 text-left transition-all ${
                        selectedSlug === a.slug
                          ? "border-primary bg-primary/5"
                          : "border-zinc-200 hover:border-zinc-300 dark:border-zinc-800"
                      }`}
                    >
                      <p className="text-sm font-medium">{a.title}</p>
                      <p className="text-xs text-muted-foreground">
                        {a.jobRole.department} &middot; {a.jobRole.title}
                      </p>
                    </button>
                  ))}
                </div>
              </div>
            )}

            {selected && (
              <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: "auto" }}
                className="rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800/50"
              >
                <p className="text-xs font-medium">{selected.title}</p>
                <p className="mt-0.5 text-xs text-muted-foreground">
                  {selected.sections.length} sections &middot;{" "}
                  {selected.sections.reduce((acc, s) => acc + s.questionCount, 0)} questions
                  {selected.version.timeLimit && ` · ${selected.version.timeLimit} min`}
                </p>
              </motion.div>
            )}

            {error && (
              <p className="text-sm text-red-600 dark:text-red-400">{error}</p>
            )}

            <Button
              onClick={handleStart}
              disabled={!name.trim() || !email.trim() || !selectedSlug || isLoading}
              className="w-full gap-2"
              size="lg"
            >
              {isLoading ? (
                <Loader2 className="size-4 animate-spin" />
              ) : (
                <>
                  Start Assessment <ArrowRight className="size-4" />
                </>
              )}
            </Button>
          </div>
        </div>
      </motion.div>
    </div>
  );
}

```