---
type: source
source_type: laptop
title: Assessify — page
slug: page-38
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/assess/[sessionId]/eggs/page.tsx"
original_size: 28311
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/assess/[sessionId]/eggs/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Loader2,
  CheckCircle,
  XCircle,
  Lightbulb,
  Lock,
  ChevronRight,
  Trophy,
  Fingerprint,
  Skull,
} from "lucide-react";

interface EggState {
  id: string;
  difficulty: string;
  label: string;
  solved: boolean;
  solvedAt?: string;
}

const eggMeta: Record<
  string,
  {
    difficulty: string;
    label: string;
    description: string;
    icon: React.ElementType;
    gradient: string;
    border: string;
    badge: string;
    dot: string;
  }
> = {
  egg_1: {
    difficulty: "Easy",
    label: "The First Clue",
    description:
      "Every great discovery starts with a simple question: what am I not seeing? You are looking at this page right now, but are you really seeing all of it? Browsers have built-in tools that let you peek behind the curtain. The egg is here, on this very page — hidden in a place only an inspector would think to look.",
    icon: Fingerprint,
    gradient: "from-emerald-50 to-white dark:from-emerald-950/30 dark:to-zinc-900",
    border: "border-emerald-200 dark:border-emerald-800",
    badge: "bg-emerald-100 text-emerald-700 dark:bg-emerald-900 dark:text-emerald-300",
    dot: "bg-emerald-500",
  },
  egg_2: {
    difficulty: "Medium",
    label: "The Silent Messenger",
    description:
      "When your browser talks to a server, the conversation goes both ways — and not everything is shown on screen. The response you get back carries more than just the page content. Open your browser's developer tools and watch what happens when this page loads. The egg is hiding in the server's reply.",
    icon: Fingerprint,
    gradient: "from-blue-50 to-white dark:from-blue-950/30 dark:to-zinc-900",
    border: "border-blue-200 dark:border-blue-800",
    badge: "bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300",
    dot: "bg-blue-500",
  },
  egg_3: {
    difficulty: "Hard",
    label: "The Vault",
    description:
      "Systems often leave traces when they run — messages, IDs, diagnostic output that most people ignore. Open your browser console right now. Something was just logged. It does not look like an egg, but it holds the key to one. Decode it, find the vault, and use the key to open it.",
    icon: Trophy,
    gradient: "from-orange-50 to-white dark:from-orange-950/30 dark:to-zinc-900",
    border: "border-orange-200 dark:border-orange-800",
    badge: "bg-orange-100 text-orange-700 dark:bg-orange-900 dark:text-orange-300",
    dot: "bg-orange-500",
  },
  egg_4: {
    difficulty: "Impossible",
    label: "???",
    description:
      "If you have made it this far, you have proven yourself resourceful. This final challenge has no hints, no guidance, and no mercy. The egg is not on this page. It is not in the console. It is not in a header. You will need to think differently about where information can be hidden on a website. Only those who think beyond the obvious will find it. Good luck.",
    icon: Skull,
    gradient: "from-red-50 to-white dark:from-red-950/30 dark:to-zinc-900",
    border: "border-red-200 dark:border-red-800",
    badge: "bg-red-100 text-red-700 dark:bg-red-900 dark:text-red-300",
    dot: "bg-red-500",
  },
};

export default function EggHuntPage({
  params,
}: {
  params: Promise<{ sessionId: string }>;
}) {
  const [sessionId, setSessionId] = useState("");
  const [candidateName, setCandidateName] = useState("");
  const [candidateEmail, setCandidateEmail] = useState("");
  const [loaded, setLoaded] = useState(false);
  const [currentEgg, setCurrentEgg] = useState(0);
  const [eggs, setEggs] = useState<EggState[]>([
    { id: "egg_1", difficulty: "Easy", label: "The First Clue", solved: false },
    { id: "egg_2", difficulty: "Medium", label: "The Silent Messenger", solved: false },
    { id: "egg_3", difficulty: "Hard", label: "The Vault", solved: false },
    { id: "egg_4", difficulty: "Impossible", label: "???", solved: false },
  ]);
  const [input, setInput] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [feedback, setFeedback] = useState<{
    type: "success" | "error";
    message: string;
  } | null>(null);
  const [hint, setHint] = useState<string | null>(null);
  const [hintLoading, setHintLoading] = useState(false);
  const [allComplete, setAllComplete] = useState(false);
  const [gaveUp, setGaveUp] = useState(false);
  const [showGiveUpConfirm, setShowGiveUpConfirm] = useState(false);

  useEffect(() => {
    params.then(async (p) => {
      setSessionId(p.sessionId);

      // Try to restore from localStorage first (survives refresh/close)
      const saved = localStorage.getItem("assessify_egg_hunt");
      let email = "";
      let name = "";

      try {
        const sessionRes = await fetch(`/api/sessions/${p.sessionId}`);
        const sessionData = await sessionRes.json();
        email = sessionData.session?.candidateEmail ?? "";
        name = sessionData.session?.candidateName ?? "";
      } catch {
        // Session fetch failed — fall back to localStorage
      }

      // If session fetch didn't return data, use saved data
      if (!email && saved) {
        try {
          const parsed = JSON.parse(saved);
          email = parsed.email ?? "";
          name = parsed.name ?? "";
        } catch { /* ignore */ }
      }

      setCandidateName(name);
      setCandidateEmail(email);

      // Save to localStorage for resume
      if (email) {
        localStorage.setItem(
          "assessify_egg_hunt",
          JSON.stringify({
            sessionId: p.sessionId,
            email,
            name,
            lastVisit: new Date().toISOString(),
          })
        );
      }

      // Track egg hunt start
      fetch("/api/easter/track", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          sessionId: p.sessionId,
          candidateName: name,
          candidateEmail: email,
          event: "egg_hunt_started",
        }),
      }).catch(() => {});

      // Load previously claimed eggs
      if (email) {
        try {
          const claimsRes = await fetch(
            `/api/easter/claim?email=${encodeURIComponent(email)}`
          );
          const claimsData = await claimsRes.json();
          if (claimsData.claims?.length > 0) {
            setEggs((prev) =>
              prev.map((egg) => {
                const claim = claimsData.claims.find(
                  (c: { eggId: string }) => c.eggId === egg.id
                );
                return claim
                  ? { ...egg, solved: true, solvedAt: claim.claimedAt }
                  : egg;
              })
            );
            const firstUnsolved = ["egg_1", "egg_2", "egg_3", "egg_4"].findIndex(
              (id) => !claimsData.claims.some((c: { eggId: string }) => c.eggId === id)
            );
            if (firstUnsolved >= 0) setCurrentEgg(firstUnsolved);
            if (claimsData.claims.length === 4) setAllComplete(true);
          }
        } catch {
          // ignore claims load failure
        }
      }

      setLoaded(true);
    });
  }, [params]);

  const activeEgg = eggs[currentEgg];
  const meta = activeEgg ? eggMeta[activeEgg.id] : null;

  // Egg 2: Fetch a challenge-specific endpoint when challenge 2 is active
  // The egg is in the response headers — candidates need to check the Network tab
  const [egg2Status, setEgg2Status] = useState<string | null>(null);
  useEffect(() => {
    if (currentEgg === 1 && !eggs[1].solved) {
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setEgg2Status(null);
      fetch("/api/easter/challenge-2")
        .then((r) => r.json())
        .then((d) => setEgg2Status(d.message ?? "Check complete."))
        .catch(() => setEgg2Status("Connection error."));
    }

  }, [currentEgg, eggs]);

  // Egg 3: Log the hex runtime ID when challenge 3 is active
  useEffect(() => {
    if (currentEgg === 2 && !eggs[2].solved) {
      const runtimeId = Array.from(
        new TextEncoder().encode("assessify_runtime_2024")
      )
        .map((b) => b.toString(16).padStart(2, "0"))
        .join("");
      console.log(
        `%c[Assessify] Runtime ID: ${runtimeId}`,
        "color: #f97316; font-size: 11px;"
      );
    }
  }, [currentEgg, eggs]);

  const handleSubmit = async () => {
    if (!input.trim() || submitting || !activeEgg) return;
    setSubmitting(true);
    setFeedback(null);

    try {
      const res = await fetch("/api/easter/claim", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          egg: input.trim(),
          candidateName,
          candidateEmail,
          sessionId,
        }),
      });

      const data = await res.json();

      if (!res.ok) {
        setFeedback({
          type: "error",
          message: data["❌"] || data.error || "That is not the right code. Keep searching.",
        });
        setSubmitting(false);
        return;
      }

      // Check if the claimed egg matches the current one
      const claimedEggId = data.egg;
      const eggIndex = eggs.findIndex((e) => e.id === claimedEggId);

      if (eggIndex >= 0) {
        const updated = [...eggs];
        updated[eggIndex] = {
          ...updated[eggIndex],
          solved: true,
          solvedAt: data.claimedAt,
        };
        setEggs(updated);

        setFeedback({
          type: "success",
          message: data["🎉"] || data["🥚"] || "You found it!",
        });

        // Move to next unsolved egg after a delay
        setTimeout(() => {
          const nextUnsolved = updated.findIndex(
            (e, i) => !e.solved && i > eggIndex
          );
          if (nextUnsolved >= 0) {
            setCurrentEgg(nextUnsolved);
            setInput("");
            setFeedback(null);
            setHint(null);
          } else if (updated.every((e) => e.solved)) {
            setAllComplete(true);
            // Track completion
            fetch("/api/easter/track", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                sessionId,
                candidateName,
                candidateEmail,
                event: "egg_hunt_finished",
                data: { reason: "completed_all", eggsSolved: 4 },
              }),
            }).catch(() => {});
          }
        }, 2500);
      }
    } catch {
      setFeedback({ type: "error", message: "Something went wrong. Please try again." });
    }
    setSubmitting(false);
  };

  const fetchHint = async () => {
    if (!activeEgg || activeEgg.id === "egg_4") return;
    setHintLoading(true);
    try {
      const res = await fetch(
        `/api/easter/hints?egg=${activeEgg.id}&email=${encodeURIComponent(candidateEmail)}`
      );
      const data = await res.json();
      setHint(data.hint ?? "No hints available for this challenge.");
    } catch {
      setHint("Could not load hint.");
    }
    setHintLoading(false);
  };

  const handleGiveUp = async () => {
    const solvedCount = eggs.filter((e) => e.solved).length;
    const bestEgg = [...eggs].reverse().find((e) => e.solved);

    await fetch("/api/easter/track", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        sessionId,
        candidateName,
        candidateEmail,
        event: "egg_hunt_finished",
        data: {
          reason: "gave_up",
          eggsSolved: solvedCount,
          bestAchievement: bestEgg?.id ?? "none",
        },
      }),
    }).catch(() => {});

    setGaveUp(true);
    setShowGiveUpConfirm(false);
  };

  if (!loaded) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <Loader2 className="size-8 animate-spin text-primary" />
      </div>
    );
  }

  if (allComplete) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 px-4 dark:bg-zinc-950">
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          className="max-w-md text-center"
        >
          <motion.div
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            transition={{ type: "spring", stiffness: 200 }}
            className="mx-auto mb-6 flex h-24 w-24 items-center justify-center rounded-3xl bg-gradient-to-br from-emerald-100 to-blue-100 dark:from-emerald-900 dark:to-blue-900"
          >
            <Trophy className="size-12 text-emerald-600 dark:text-emerald-400" />
          </motion.div>
          <h1 className="mb-3 text-3xl font-bold tracking-tight">
            You found them all.
          </h1>
          <p className="mb-2 text-muted-foreground">
            All 4 easter eggs — including the impossible one. That is genuinely
            impressive.
          </p>
          <p className="text-sm text-muted-foreground">
            The hiring team has been notified. You are exactly the kind of
            person we are looking for.
          </p>
          <div className="mt-8 grid grid-cols-4 gap-3">
            {eggs.map((egg) => {
              const m = eggMeta[egg.id];
              return (
                <div
                  key={egg.id}
                  className={`rounded-xl border p-3 text-center ${m?.border}`}
                >
                  <span className={`inline-block h-3 w-3 rounded-full ${m?.dot}`} />
                  <p className="mt-1 text-[10px] font-medium">{m?.difficulty}</p>
                  <CheckCircle className="mx-auto mt-1 size-4 text-emerald-500" />
                </div>
              );
            })}
          </div>
        </motion.div>
      </div>
    );
  }

  if (gaveUp) {
    const solvedCount = eggs.filter((e) => e.solved).length;
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 px-4 dark:bg-zinc-950">
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          className="max-w-md text-center"
        >
          <motion.div
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            transition={{ type: "spring", stiffness: 200 }}
            className="mx-auto mb-6 flex h-20 w-20 items-center justify-center rounded-3xl bg-zinc-100 dark:bg-zinc-800"
          >
            <Trophy className="size-10 text-zinc-500" />
          </motion.div>
          <h1 className="mb-3 text-2xl font-bold tracking-tight">
            Challenge Complete
          </h1>
          <p className="mb-2 text-muted-foreground">
            {solvedCount === 0
              ? "You gave it a shot — that takes courage. Not everyone even tries."
              : solvedCount === 1
                ? "You found 1 egg. A solid start — curiosity is a great trait."
                : solvedCount === 2
                  ? `You found ${solvedCount} eggs. That shows real resourcefulness.`
                  : `You found ${solvedCount} out of 4. Impressive work.`}
          </p>
          <p className="text-sm text-muted-foreground">
            Your results have been recorded. Thank you for taking on the
            challenge.
          </p>
          <div className="mt-8 grid grid-cols-4 gap-3">
            {eggs.map((egg) => {
              const m = eggMeta[egg.id];
              return (
                <div
                  key={egg.id}
                  className={`rounded-xl border p-3 text-center ${
                    egg.solved ? m?.border : "border-zinc-200 dark:border-zinc-800"
                  }`}
                >
                  <span
                    className={`inline-block h-3 w-3 rounded-full ${
                      egg.solved ? m?.dot : "bg-zinc-300 dark:bg-zinc-600"
                    }`}
                  />
                  <p className="mt-1 text-[10px] font-medium">{m?.difficulty}</p>
                  {egg.solved ? (
                    <CheckCircle className="mx-auto mt-1 size-4 text-emerald-500" />
                  ) : (
                    <Lock className="mx-auto mt-1 size-4 text-zinc-300 dark:text-zinc-600" />
                  )}
                </div>
              );
            })}
          </div>
        </motion.div>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen flex-col bg-zinc-50 dark:bg-zinc-950">
      {/* Progress bar */}
      <div className="border-b border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900">
        <div className="mx-auto flex max-w-2xl items-center justify-between px-4 py-3">
          <div>
            <p className="text-xs font-medium text-muted-foreground">
              The Egg Hunt
            </p>
            <p className="text-sm font-semibold">
              {eggs.filter((e) => e.solved).length} of 4 found
            </p>
          </div>
          <div className="flex gap-2">
            {eggs.map((egg, i) => {
              const m = eggMeta[egg.id];
              return (
                <button
                  key={egg.id}
                  onClick={() => {
                    setCurrentEgg(i);
                    setInput("");
                    setFeedback(null);
                    setHint(null);
                  }}
                  className={`flex h-8 w-8 items-center justify-center rounded-lg border text-xs font-bold transition-all ${
                    i === currentEgg
                      ? `${m?.border} ${m?.badge}`
                      : egg.solved
                        ? "border-emerald-200 bg-emerald-50 text-emerald-600 dark:border-emerald-800 dark:bg-emerald-950 dark:text-emerald-400"
                        : "border-zinc-200 text-zinc-400 dark:border-zinc-700"
                  }`}
                >
                  {egg.solved ? (
                    <CheckCircle className="size-4" />
                  ) : (
                    i + 1
                  )}
                </button>
              );
            })}
          </div>
        </div>
        <div className="h-1 bg-zinc-100 dark:bg-zinc-800">
          <motion.div
            className="h-full bg-emerald-500"
            animate={{
              width: `${(eggs.filter((e) => e.solved).length / 4) * 100}%`,
            }}
            transition={{ duration: 0.5 }}
          />
        </div>
      </div>

      {/* Main content */}
      <div className="mx-auto flex w-full max-w-2xl flex-1 flex-col px-4 py-8">
        <AnimatePresence mode="wait">
          {activeEgg && meta && (
            <motion.div
              key={activeEgg.id}
              initial={{ opacity: 0, x: 40 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -40 }}
              transition={{ duration: 0.3 }}
              className="flex-1"
            >
              {/* Egg header */}
              <div className="mb-6">
                <div className="mb-3 flex items-center gap-2">
                  <span
                    className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold ${meta.badge}`}
                  >
                    {meta.difficulty}
                  </span>
                  <span className="text-xs text-muted-foreground">
                    Challenge {currentEgg + 1} of 4
                  </span>
                </div>
                <h2 className="text-2xl font-bold tracking-tight">
                  {meta.label}
                </h2>
              </div>

              {/* Challenge card */}
              <div
                className={`mb-6 rounded-2xl border bg-gradient-to-b p-6 ${meta.gradient} ${meta.border}`}
                {...(activeEgg.id === "egg_1"
                  ? { "data-challenge-config": "active", "data-egg": "egg{curiosity_is_the_first_step}" }
                  : {})}
              >
                <p className="text-sm leading-relaxed text-zinc-700 dark:text-zinc-300">
                  {meta.description}
                </p>

                {/* Hint button */}
                {activeEgg.id !== "egg_4" && !activeEgg.solved && (
                  <div className="mt-4">
                    <button
                      onClick={fetchHint}
                      disabled={hintLoading}
                      className="inline-flex items-center gap-1.5 rounded-lg bg-white/60 px-3 py-1.5 text-xs font-medium text-zinc-600 transition-colors hover:bg-white dark:bg-zinc-800/60 dark:text-zinc-400 dark:hover:bg-zinc-800"
                    >
                      {hintLoading ? (
                        <Loader2 className="size-3 animate-spin" />
                      ) : (
                        <Lightbulb className="size-3" />
                      )}
                      {hint ? "Get another hint" : "Need a hint?"}
                    </button>
                    <AnimatePresence>
                      {hint && (
                        <motion.p
                          initial={{ opacity: 0, y: -5 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0 }}
                          className="mt-2 rounded-lg bg-white/80 p-3 text-xs italic leading-relaxed text-zinc-500 dark:bg-zinc-800/80 dark:text-zinc-400"
                        >
                          {hint}
                        </motion.p>
                      )}
                    </AnimatePresence>
                  </div>
                )}

                {activeEgg.id === "egg_2" && !activeEgg.solved && egg2Status && (
                  <div className="mt-4 rounded-lg bg-white/80 p-3 font-mono text-xs text-zinc-500 dark:bg-zinc-800/80 dark:text-zinc-400">
                    <span className="text-zinc-400">GET /api/easter/challenge-2</span> → <span className="text-emerald-600">200 OK</span>
                    <p className="mt-1 text-zinc-400">{egg2Status}</p>
                  </div>
                )}

                {activeEgg.id === "egg_4" && !activeEgg.solved && (
                  <div className="mt-4 flex items-center gap-2 text-xs text-zinc-400">
                    <Lock className="size-3" />
                    No hints. You are on your own.
                  </div>
                )}
              </div>

              {/* Solved state */}
              {activeEgg.solved ? (
                <motion.div
                  initial={{ opacity: 0, scale: 0.95 }}
                  animate={{ opacity: 1, scale: 1 }}
                  className="rounded-2xl border border-emerald-200 bg-emerald-50 p-6 text-center dark:border-emerald-800 dark:bg-emerald-950/50"
                >
                  <CheckCircle className="mx-auto mb-3 size-10 text-emerald-500" />
                  <h3 className="text-lg font-bold text-emerald-800 dark:text-emerald-200">
                    Solved!
                  </h3>
                  <p className="mt-1 text-sm text-emerald-600 dark:text-emerald-400">
                    You cracked this one. Well done.
                  </p>
                  {currentEgg < 3 && (
                    <Button
                      onClick={() => {
                        const next = eggs.findIndex(
                          (e, i) => !e.solved && i > currentEgg
                        );
                        if (next >= 0) {
                          setCurrentEgg(next);
                          setInput("");
                          setFeedback(null);
                          setHint(null);
                        }
                      }}
                      className="mt-4 gap-2"
                    >
                      Next Challenge <ChevronRight className="size-4" />
                    </Button>
                  )}
                </motion.div>
              ) : (
                /* Input area */
                <div>
                  <label className="mb-2 block text-sm font-medium">
                    Enter the egg code
                  </label>
                  <p className="mb-3 text-xs text-muted-foreground">
                    When you find it, paste the full code here (e.g.{" "}
                    <code className="rounded bg-zinc-100 px-1 py-0.5 font-mono dark:bg-zinc-800">
                      egg&#123;...&#125;
                    </code>
                    ).
                  </p>
                  <div className="flex gap-2">
                    <Input
                      value={input}
                      onChange={(e) => setInput(e.target.value)}
                      placeholder="egg{your_answer_here}"
                      className="font-mono"
                      onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
                    />
                    <Button
                      onClick={handleSubmit}
                      disabled={!input.trim() || submitting}
                    >
                      {submitting ? (
                        <Loader2 className="size-4 animate-spin" />
                      ) : (
                        "Submit"
                      )}
                    </Button>
                  </div>

                  {/* Feedback */}
                  <AnimatePresence>
                    {feedback && (
                      <motion.div
                        initial={{ opacity: 0, y: -5 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0 }}
                        className={`mt-3 flex items-start gap-2 rounded-lg p-3 text-sm ${
                          feedback.type === "success"
                            ? "bg-emerald-50 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300"
                            : "bg-red-50 text-red-700 dark:bg-red-950 dark:text-red-300"
                        }`}
                      >
                        {feedback.type === "success" ? (
                          <CheckCircle className="mt-0.5 size-4 flex-shrink-0" />
                        ) : (
                          <XCircle className="mt-0.5 size-4 flex-shrink-0" />
                        )}
                        {feedback.message}
                      </motion.div>
                    )}
                  </AnimatePresence>
                </div>
              )}
            </motion.div>
          )}
        </AnimatePresence>

        {/* Give up section */}
        <div className="mt-8 border-t border-zinc-200 pt-6 text-center dark:border-zinc-800">
          {!showGiveUpConfirm ? (
            <button
              onClick={() => setShowGiveUpConfirm(true)}
              className="text-xs text-zinc-400 transition-colors hover:text-zinc-600 dark:hover:text-zinc-300"
            >
              Had enough? Call it a day.
            </button>
          ) : (
            <motion.div
              initial={{ opacity: 0, y: -5 }}
              animate={{ opacity: 1, y: 0 }}
              className="rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900"
            >
              <p className="mb-1 text-sm font-medium">
                Ready to wrap up?
              </p>
              <p className="mb-4 text-xs text-muted-foreground">
                Your progress so far ({eggs.filter((e) => e.solved).length}/4
                eggs) will be saved. You can always come back later if you
                change your mind.
              </p>
              <div className="flex items-center justify-center gap-3">
                <Button
                  variant="outline"
                  onClick={() => setShowGiveUpConfirm(false)}
                  className="text-xs"
                >
                  Keep going
                </Button>
                <Button
                  onClick={handleGiveUp}
                  className="bg-zinc-900 text-xs text-white hover:bg-zinc-800 dark:bg-zinc-100 dark:text-zinc-900 dark:hover:bg-zinc-200"
                >
                  I am done — submit my results
                </Button>
              </div>
            </motion.div>
          )}
        </div>
      </div>
    </div>
  );
}

```