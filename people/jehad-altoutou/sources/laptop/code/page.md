---
type: source
source_type: laptop
title: page
slug: page
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/page.tsx
original_size: 4655
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `assessify/src/app/page.tsx` on 2026-05-14._

```tsx
"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import {
  ArrowRight,
  Sparkles,
  BarChart3,
  Zap,
} from "lucide-react";

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col bg-white dark:bg-zinc-950">
      {/* Nav */}
      <nav className="flex items-center justify-between border-b border-zinc-100 px-6 py-4 dark:border-zinc-800">
        <span className="text-lg font-bold tracking-tight">Assessify</span>
        <Link
          href="/admin"
          className="text-sm font-medium text-muted-foreground transition-colors hover:text-foreground"
        >
          Admin
        </Link>
      </nav>

      {/* Hero */}
      <main className="flex flex-1 flex-col items-center justify-center px-4 py-20">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }}
          className="max-w-2xl text-center"
        >
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.15 }}
            className="mx-auto mb-6 flex h-16 w-16 items-center justify-center rounded-2xl bg-primary/10"
          >
            <Sparkles className="size-8 text-primary" />
          </motion.div>

          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.25 }}
            className="text-4xl font-bold tracking-tight sm:text-5xl"
          >
            Hiring assessments
            <br />
            <span className="text-primary">people actually enjoy.</span>
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.35 }}
            className="mx-auto mt-4 max-w-md text-base leading-relaxed text-muted-foreground"
          >
            Immersive, beautifully designed assessments that give candidates a
            great experience and give you the data you need to hire with
            confidence.
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.45 }}
            className="mt-8 flex flex-col items-center gap-3 sm:flex-row sm:justify-center"
          >
            <Link
              href="/assess"
              className="inline-flex h-9 items-center justify-center gap-2 rounded-lg bg-primary px-4 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/80"
            >
              Start Assessment <ArrowRight className="size-4" />
            </Link>
            <Link
              href="/admin"
              className="inline-flex h-9 items-center justify-center gap-2 rounded-lg border border-border bg-background px-4 text-sm font-medium transition-colors hover:bg-muted"
            >
              Open Dashboard
            </Link>
          </motion.div>
        </motion.div>

        {/* Features */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.6, duration: 0.6 }}
          className="mt-20 grid max-w-3xl grid-cols-1 gap-6 sm:grid-cols-3"
        >
          {[
            {
              icon: Sparkles,
              title: "Premium Experience",
              desc: "Beautiful motion, engaging interactions, and a flow that feels rewarding.",
            },
            {
              icon: BarChart3,
              title: "Deep Analytics",
              desc: "Competency heatmaps, funnel analytics, and question-level insights.",
            },
            {
              icon: Zap,
              title: "Automation Ready",
              desc: "Webhook events, structured JSON payloads, and n8n-compatible outputs.",
            },
          ].map((f, i) => (
            <motion.div
              key={f.title}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.7 + i * 0.1 }}
              className="rounded-xl border border-zinc-100 p-5 dark:border-zinc-800"
            >
              <f.icon className="mb-3 size-5 text-primary" />
              <h3 className="text-sm font-semibold">{f.title}</h3>
              <p className="mt-1 text-xs leading-relaxed text-muted-foreground">
                {f.desc}
              </p>
            </motion.div>
          ))}
        </motion.div>
      </main>
    </div>
  );
}

```