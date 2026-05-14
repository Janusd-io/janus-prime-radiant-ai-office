---
type: source
source_type: laptop
title: RubricDashboard
slug: rubricdashboard
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/recruitment/rubrics/RubricDashboard.tsx
original_size: 15701
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# RubricDashboard

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/rubrics/RubricDashboard.tsx` on 2026-05-14._

```tsx
"use client";

import { useState, useMemo, useEffect } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import { motion } from "framer-motion";
import {
  Plus,
  Briefcase,
  Globe,
  SlidersHorizontal,
  CheckCircle2,
  Archive,
  ChevronRight,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { RubricFormSheet } from "./RubricFormSheet";

type Tier = "strong_match" | "match" | "consider" | "weak" | "reject";

const TIER_ORDER: Tier[] = ["strong_match", "match", "consider", "weak", "reject"];

const TIER_LABEL: Record<Tier, string> = {
  strong_match: "Strong",
  match: "Match",
  consider: "Consider",
  weak: "Weak",
  reject: "Reject",
};

const TIER_BAR_COLOR: Record<Tier, string> = {
  strong_match: "bg-emerald-500",
  match: "bg-green-400",
  consider: "bg-amber-400",
  weak: "bg-orange-400",
  reject: "bg-rose-500",
};

type Criterion = {
  key: string;
  label: string;
  weight: number;
  scoringPrompt: string;
  commentaryGuidance?: string;
  redFlagSignals?: string[];
};

export type RubricRow = {
  id: string;
  name: string;
  kind: "pre_interview" | "post_interview";
  jobRoleId: string | null;
  jobRoleLabel: string | null;
  isActive: boolean;
  version: number;
  criteria: Criterion[];
  thresholdStrong: number;
  thresholdMatch: number;
  thresholdConsider: number;
  scoreCount: number;
  avgScore: number | null; // 0..1
  tierCounts: Record<Tier, number>;
  updatedAt: string;
};

export type JobRoleOption = { id: string; title: string; department: string };

type FilterKind = "all" | "pre_interview" | "post_interview";
type FilterScope = "all" | "global" | "role";

type Props = {
  rubrics: RubricRow[];
  jobRoles: JobRoleOption[];
};

const DEFAULT_INITIAL = {
  name: "",
  kind: "pre_interview" as const,
  jobRoleId: null as string | null,
  isActive: true,
  criteria: [
    {
      key: "experience_match",
      label: "Experience match",
      weight: 0.3,
      scoringPrompt:
        "Years of relevant experience vs the JD requirement. Reference specific employers and roles from the CV.",
    },
    {
      key: "skill_coverage",
      label: "Skills coverage vs JD",
      weight: 0.35,
      scoringPrompt:
        "Fraction of must-have skills from the JD demonstrated with concrete CV evidence.",
    },
    {
      key: "education_alignment",
      label: "Education alignment",
      weight: 0.15,
      scoringPrompt:
        "Score 1.0 if degree level + field meets the JD requirement; 0.5 if partial fit; 0.0 if no relevant education and JD requires it.",
    },
    {
      key: "tenure_stability",
      label: "Tenure stability",
      weight: 0.1,
      scoringPrompt:
        "Score 1.0 for healthy 2–4y tenures; lower if many short stints. Penalise excessive job-hopping unless explained.",
    },
    {
      key: "cultural_fit",
      label: "Cultural fit & availability",
      weight: 0.1,
      scoringPrompt:
        "Notice period, location/relocation needs, language fit, compensation alignment with role band.",
    },
  ],
  thresholdStrong: 0.85,
  thresholdMatch: 0.7,
  thresholdConsider: 0.55,
};

export function RubricDashboard({ rubrics, jobRoles }: Props) {
  const router = useRouter();
  const search = useSearchParams();
  const [filterKind, setFilterKind] = useState<FilterKind>("all");
  const [filterScope, setFilterScope] = useState<FilterScope>("all");
  const [sheetState, setSheetState] = useState<
    | { mode: "create" }
    | { mode: "edit"; rubric: RubricRow }
    | null
  >(null);

  // Auto-open the Sheet when ?open=new or ?open=<id> arrives — keeps the
  // legacy /new and /[id]/edit URLs working via redirect.
  useEffect(() => {
    const open = search.get("open");
    if (!open) return;
    if (open === "new") {
      setSheetState({ mode: "create" });
    } else {
      const found = rubrics.find((r) => r.id === open);
      if (found) setSheetState({ mode: "edit", rubric: found });
    }
    // Strip the param so reload doesn't re-open
    const params = new URLSearchParams(search.toString());
    params.delete("open");
    const qs = params.toString();
    router.replace(qs ? `?${qs}` : "?", { scroll: false });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const filtered = useMemo(() => {
    return rubrics.filter((r) => {
      if (filterKind !== "all" && r.kind !== filterKind) return false;
      if (filterScope === "global" && r.jobRoleId) return false;
      if (filterScope === "role" && !r.jobRoleId) return false;
      return true;
    });
  }, [rubrics, filterKind, filterScope]);

  const stats = useMemo(() => {
    const total = rubrics.length;
    const active = rubrics.filter((r) => r.isActive).length;
    const pre = rubrics.filter((r) => r.kind === "pre_interview").length;
    const post = rubrics.filter((r) => r.kind === "post_interview").length;
    const roleSpecific = rubrics.filter((r) => r.jobRoleId).length;
    return { total, active, pre, post, roleSpecific };
  }, [rubrics]);

  const closeSheet = () => setSheetState(null);

  return (
    <div>
      <div className="mb-6 flex items-start justify-between gap-4">
        <div>
          <Link href="/admin/recruitment" className="text-xs text-zinc-500 hover:underline">
            ← Pipeline
          </Link>
          <h1 className="mt-1 text-2xl font-bold tracking-tight">Scoring rubrics</h1>
          <p className="mt-1 text-sm text-muted-foreground">
            Configure how candidates are scored. Role-specific rubrics override the global default.
          </p>
        </div>
        <Button onClick={() => setSheetState({ mode: "create" })} className="gap-2">
          <Plus className="size-4" /> New rubric
        </Button>
      </div>

      {/* Stat strip */}
      <div className="mb-5 grid grid-cols-2 gap-3 sm:grid-cols-5">
        <StatCard label="Total" value={stats.total} icon={SlidersHorizontal} />
        <StatCard label="Active" value={stats.active} icon={CheckCircle2} accent="emerald" />
        <StatCard label="Pre-interview" value={stats.pre} />
        <StatCard label="Post-interview" value={stats.post} />
        <StatCard label="Role-specific" value={stats.roleSpecific} icon={Briefcase} />
      </div>

      {/* Filter chips */}
      <div className="mb-5 flex flex-wrap items-center gap-2 rounded-xl border border-zinc-200 bg-white p-3 dark:border-zinc-800 dark:bg-zinc-900">
        <span className="mr-1 text-[10px] font-semibold uppercase tracking-wide text-zinc-500">
          Filters:
        </span>
        <FilterChipRow
          values={[
            { value: "all", label: "All kinds" },
            { value: "pre_interview", label: "Pre-interview" },
            { value: "post_interview", label: "Post-interview" },
          ]}
          active={filterKind}
          onChange={(v) => setFilterKind(v as FilterKind)}
        />
        <span className="mx-2 h-4 w-px bg-zinc-200 dark:bg-zinc-700" />
        <FilterChipRow
          values={[
            { value: "all", label: "All scopes" },
            { value: "global", label: "Global" },
            { value: "role", label: "Role-specific" },
          ]}
          active={filterScope}
          onChange={(v) => setFilterScope(v as FilterScope)}
        />
        <span className="ml-auto text-[10px] text-muted-foreground">
          {filtered.length} of {rubrics.length}
        </span>
      </div>

      {/* Card grid */}
      {filtered.length === 0 ? (
        <div className="rounded-xl border border-dashed border-zinc-300 bg-white p-12 text-center dark:border-zinc-700 dark:bg-zinc-900">
          <SlidersHorizontal className="mx-auto size-8 text-zinc-400" />
          <p className="mt-3 text-sm text-muted-foreground">
            {rubrics.length === 0
              ? "No rubrics yet. Click \"New rubric\" to create one."
              : "No rubrics match these filters."}
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-3 lg:grid-cols-2">
          {filtered.map((r, i) => (
            <RubricCard key={r.id} rubric={r} index={i} onClick={() => setSheetState({ mode: "edit", rubric: r })} />
          ))}
        </div>
      )}

      {/* Edit / create sheet */}
      <RubricFormSheet
        open={sheetState !== null}
        onOpenChange={(open) => !open && closeSheet()}
        mode={sheetState?.mode === "edit" ? "edit" : "create"}
        rubricId={sheetState?.mode === "edit" ? sheetState.rubric.id : undefined}
        initial={
          sheetState?.mode === "edit"
            ? {
                name: sheetState.rubric.name,
                kind: sheetState.rubric.kind,
                jobRoleId: sheetState.rubric.jobRoleId,
                isActive: sheetState.rubric.isActive,
                criteria: sheetState.rubric.criteria,
                thresholdStrong: sheetState.rubric.thresholdStrong,
                thresholdMatch: sheetState.rubric.thresholdMatch,
                thresholdConsider: sheetState.rubric.thresholdConsider,
              }
            : DEFAULT_INITIAL
        }
        jobRoles={jobRoles}
      />
    </div>
  );
}

function RubricCard({
  rubric,
  index,
  onClick,
}: {
  rubric: RubricRow;
  index: number;
  onClick: () => void;
}) {
  const total = TIER_ORDER.reduce((s, t) => s + (rubric.tierCounts[t] ?? 0), 0);

  return (
    <motion.button
      type="button"
      onClick={onClick}
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.03, duration: 0.22, ease: [0.16, 1, 0.3, 1] }}
      className="group block w-full rounded-xl border border-zinc-200 bg-white p-4 text-left transition-all hover:-translate-y-px hover:border-zinc-300 hover:shadow-sm dark:border-zinc-800 dark:bg-zinc-900 dark:hover:border-zinc-700"
    >
      {/* Header: scope + active + chevron */}
      <div className="flex items-start justify-between gap-3">
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2 text-[10px] font-semibold uppercase tracking-wide text-zinc-500">
            {rubric.jobRoleId ? (
              <Briefcase className="size-3" />
            ) : (
              <Globe className="size-3" />
            )}
            <span className="truncate">{rubric.jobRoleLabel ?? "Global default"}</span>
            <span>·</span>
            <span>{rubric.kind === "pre_interview" ? "Pre" : "Post"}</span>
            <span>· v{rubric.version}</span>
          </div>
          <h3 className="mt-1 text-sm font-semibold">{rubric.name}</h3>
        </div>
        <div className="flex shrink-0 items-center gap-2">
          {rubric.isActive ? (
            <span className="inline-flex items-center gap-1 rounded-full bg-emerald-100 px-2 py-0.5 text-[10px] font-medium text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200">
              <CheckCircle2 className="size-3" /> Active
            </span>
          ) : (
            <span className="inline-flex items-center gap-1 rounded-full bg-zinc-100 px-2 py-0.5 text-[10px] font-medium text-zinc-700 dark:bg-zinc-800 dark:text-zinc-300">
              <Archive className="size-3" /> Archived
            </span>
          )}
          <ChevronRight className="size-4 text-zinc-400 transition-transform group-hover:translate-x-0.5" />
        </div>
      </div>

      {/* Tier-distribution mini-bar */}
      <div className="mt-4">
        {total === 0 ? (
          <div className="flex items-center justify-between text-[11px] text-zinc-400">
            <span>No scores yet</span>
            <span>{rubric.scoreCount} scores</span>
          </div>
        ) : (
          <>
            <div className="flex h-2 w-full overflow-hidden rounded-full bg-zinc-100 dark:bg-zinc-800">
              {TIER_ORDER.map((tier) => {
                const count = rubric.tierCounts[tier] ?? 0;
                if (count === 0) return null;
                const pct = (count / total) * 100;
                return (
                  <motion.div
                    key={tier}
                    initial={{ width: 0 }}
                    animate={{ width: `${pct}%` }}
                    transition={{ delay: 0.1 + index * 0.03, duration: 0.5, ease: "easeOut" }}
                    className={`h-full ${TIER_BAR_COLOR[tier]}`}
                    title={`${TIER_LABEL[tier]}: ${count}`}
                  />
                );
              })}
            </div>
            <div className="mt-2 flex flex-wrap items-center gap-x-3 gap-y-1 text-[10px] text-zinc-500">
              {TIER_ORDER.map((tier) => {
                const count = rubric.tierCounts[tier] ?? 0;
                if (count === 0) return null;
                return (
                  <span key={tier} className="inline-flex items-center gap-1">
                    <span className={`size-2 rounded-full ${TIER_BAR_COLOR[tier]}`} />
                    {TIER_LABEL[tier]} {count}
                  </span>
                );
              })}
            </div>
          </>
        )}
      </div>

      {/* Stats footer */}
      <div className="mt-3 flex flex-wrap items-center justify-between gap-2 border-t border-zinc-100 pt-3 text-[11px] text-zinc-500 dark:border-zinc-800">
        <span>
          {rubric.scoreCount} score{rubric.scoreCount === 1 ? "" : "s"} computed
          {rubric.avgScore !== null && (
            <span className="ml-1">· avg {(rubric.avgScore * 100).toFixed(0)}%</span>
          )}
        </span>
        <span>
          {rubric.criteria.length} criteria · thresholds {Math.round(rubric.thresholdStrong * 100)}/
          {Math.round(rubric.thresholdMatch * 100)}/{Math.round(rubric.thresholdConsider * 100)}
        </span>
      </div>
    </motion.button>
  );
}

function StatCard({
  label,
  value,
  icon: Icon,
  accent,
}: {
  label: string;
  value: number;
  icon?: React.ComponentType<{ className?: string }>;
  accent?: "emerald";
}) {
  const accentClass =
    accent === "emerald"
      ? "text-emerald-600 dark:text-emerald-400"
      : "text-zinc-500 dark:text-zinc-400";
  return (
    <div className="rounded-xl border border-zinc-200 bg-white p-3 dark:border-zinc-800 dark:bg-zinc-900">
      <div className="flex items-center gap-2 text-[10px] font-semibold uppercase tracking-wide text-zinc-500">
        {Icon && <Icon className={`size-3 ${accentClass}`} />}
        {label}
      </div>
      <div className="mt-1 text-2xl font-bold tabular-nums">{value}</div>
    </div>
  );
}

function FilterChipRow<T extends string>({
  values,
  active,
  onChange,
}: {
  values: Array<{ value: T; label: string }>;
  active: T;
  onChange: (v: T) => void;
}) {
  return (
    <div className="flex items-center gap-1">
      {values.map((v) => {
        const isActive = active === v.value;
        return (
          <button
            key={v.value}
            type="button"
            onClick={() => onChange(v.value)}
            className={`relative rounded-md px-2.5 py-1 text-xs transition-colors ${
              isActive
                ? "text-zinc-900 dark:text-zinc-100"
                : "text-zinc-500 hover:text-zinc-700 dark:text-zinc-500 dark:hover:text-zinc-300"
            }`}
          >
            {isActive && (
              <motion.span
                layoutId={`chip-${values.map((x) => x.value).join("-")}`}
                className="absolute inset-0 rounded-md bg-zinc-100 dark:bg-zinc-800"
                transition={{ type: "spring", stiffness: 380, damping: 30 }}
              />
            )}
            <span className="relative">{v.label}</span>
          </button>
        );
      })}
    </div>
  );
}

```