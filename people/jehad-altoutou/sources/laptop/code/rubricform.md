---
type: source
source_type: laptop
title: RubricForm
slug: rubricform
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/recruitment/rubrics/RubricForm.tsx
original_size: 32320
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# RubricForm

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/rubrics/RubricForm.tsx` on 2026-05-14._

```tsx
"use client";

import { useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import {
  AlertTriangle,
  ChevronDown,
  ChevronRight,
  HelpCircle,
  Loader2,
  Plus,
  Save,
  Sparkles,
  Trash2,
} from "lucide-react";

type Criterion = {
  key: string;
  label: string;
  weight: number; // 0..1
  scoringPrompt: string;
  commentaryGuidance?: string;
  redFlagSignals?: string[];
};

type JobRoleOption = { id: string; title: string; department: string };

type Mode = "create" | "edit";

type Props = {
  mode: Mode;
  rubricId?: string;
  initial: {
    name: string;
    kind: "pre_interview" | "post_interview";
    jobRoleId: string | null;
    isActive: boolean;
    criteria: Criterion[];
    thresholdStrong: number;
    thresholdMatch: number;
    thresholdConsider: number;
  };
  jobRoles: JobRoleOption[];
  onSuccess?: () => void;
};

const GLOBAL = "__global__";

const NEW_CRITERION = (): Criterion => ({
  key: "",
  label: "",
  weight: 0.1,
  scoringPrompt: "",
});

// A complete, realistic example criterion — used in the explainer + "Load example" button.
const EXAMPLE_CRITERION: Criterion = {
  key: "real_estate_ib_experience",
  label: "Real Estate Investment Banking Experience",
  weight: 0.3,
  scoringPrompt:
    "How many years of direct REIB experience does the candidate have at recognised platforms (JLL Capital Markets, CBRE Investment Banking, Cushman, Brookfield, Blackstone, etc.)? Score 8–10 for global Tier 1 platforms with named deal-lead roles; 5–7 for regional or boutique advisory; 3–4 for adjacent finance experience (private credit, fund-of-funds); 0–2 for none.",
  commentaryGuidance:
    "Name specific firms, named transactions, deal sizes (USD/AED/EUR), the candidate's exact role on each deal, and any ARGUS Enterprise or REIT-specific valuation experience.",
  redFlagSignals: [
    "fewer than 12 months at any real estate IB employer",
    "no named deals on CV",
    "developer-side only with no advisory exposure",
  ],
};

const EXAMPLE_TEMPLATE = {
  name: "Example: Associate Investment Banker — pre-interview",
  criteria: [
    EXAMPLE_CRITERION,
    {
      key: "capital_raising",
      label: "Capital Raising & Investor Engagement",
      weight: 0.25,
      scoringPrompt:
        "Has the candidate independently raised institutional capital? Score 8–10 for programmatic fund-level raises with Tier 1 LPs; 5–7 for individual term sheet origination at scale; 3–4 for supporting role on raises; 0–2 for none.",
      commentaryGuidance:
        "Quantify pipeline size, named investors engaged, term sheets generated, dollar amounts closed.",
      redFlagSignals: ["pipeline numbers without any named closed transactions"],
    },
    {
      key: "modelling_skill",
      label: "Financial Modelling & Valuation",
      weight: 0.25,
      scoringPrompt:
        "Depth of modelling vocabulary: ARGUS Enterprise, REIT NAV/FFO/AFFO, IRR/MOIC, waterfall structuring, LBO. Score 8–10 for ARGUS + REIT-specific fluency; 5–7 for general PE/credit modelling; 0–4 below.",
      commentaryGuidance:
        "Name the specific modelling tools and methodologies referenced in the CV.",
    },
    {
      key: "fit_and_availability",
      label: "Cultural Fit, Availability & Compensation",
      weight: 0.2,
      scoringPrompt:
        "Notice period, current location vs role location, language match, compensation range alignment with the band. 9–10 for immediately available in-market candidates; 5–7 for short notice with relocation; 0–4 for misalignment.",
      commentaryGuidance:
        "Be explicit about visa, relocation cost, notice period, and any disclosed compensation expectation.",
    },
  ] as Criterion[],
  thresholdStrong: 0.85,
  thresholdMatch: 0.7,
  thresholdConsider: 0.55,
};

// ─── slug helpers (auto-generate the internal ID from the label) ─────────────

function slugify(s: string): string {
  return s
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, "_")
    .replace(/^_+|_+$/g, "")
    .replace(/_{2,}/g, "_")
    .slice(0, 60);
}

function uniqueKey(base: string, existing: string[]): string {
  const safe = base || "criterion";
  if (!existing.includes(safe)) return safe;
  let i = 2;
  while (existing.includes(`${safe}_${i}`)) i++;
  return `${safe}_${i}`;
}

// ─── Form ────────────────────────────────────────────────────────────────────

export function RubricForm({ mode, rubricId, initial, jobRoles, onSuccess }: Props) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [showExplainer, setShowExplainer] = useState(mode === "create");

  const [name, setName] = useState(initial.name);
  const [kind, setKind] = useState(initial.kind);
  const [jobRoleId, setJobRoleId] = useState<string>(initial.jobRoleId ?? GLOBAL);
  const [isActive, setIsActive] = useState(initial.isActive);
  const [criteria, setCriteria] = useState<Criterion[]>(initial.criteria);
  const [thresholdStrong, setThresholdStrong] = useState(initial.thresholdStrong);
  const [thresholdMatch, setThresholdMatch] = useState(initial.thresholdMatch);
  const [thresholdConsider, setThresholdConsider] = useState(initial.thresholdConsider);

  const totalWeight = criteria.reduce((s, c) => s + (Number(c.weight) || 0), 0);
  const weightOk = Math.abs(totalWeight - 1) < 0.001;

  function patchCriterion(i: number, patch: Partial<Criterion>) {
    setCriteria((prev) =>
      prev.map((c, idx) => {
        if (idx !== i) return c;
        const next: Criterion = { ...c, ...patch };
        // Auto-derive key from label as the user types — but only when we
        // don't already have a manually-set key (i.e. on creation). Once a
        // key has been persisted (edit mode existing criterion), preserve it.
        if (patch.label !== undefined && !c.key) {
          const others = prev.filter((_, idx2) => idx2 !== i).map((x) => x.key).filter(Boolean);
          next.key = uniqueKey(slugify(patch.label), others);
        }
        return next;
      }),
    );
  }
  function addCriterion() {
    setCriteria((prev) => [...prev, NEW_CRITERION()]);
  }
  function removeCriterion(i: number) {
    setCriteria((prev) => prev.filter((_, idx) => idx !== i));
  }
  function distributeWeightsEvenly() {
    if (criteria.length === 0) return;
    const w = +(1 / criteria.length).toFixed(4);
    const last = +(1 - w * (criteria.length - 1)).toFixed(4);
    setCriteria((prev) =>
      prev.map((c, idx) => ({ ...c, weight: idx === prev.length - 1 ? last : w })),
    );
  }
  function loadExample() {
    if (
      criteria.some((c) => c.label || c.scoringPrompt) &&
      !confirm("Replace the current criteria with the example template?")
    ) {
      return;
    }
    if (!name.trim()) setName(EXAMPLE_TEMPLATE.name);
    setCriteria(EXAMPLE_TEMPLATE.criteria.map((c) => ({ ...c })));
    setThresholdStrong(EXAMPLE_TEMPLATE.thresholdStrong);
    setThresholdMatch(EXAMPLE_TEMPLATE.thresholdMatch);
    setThresholdConsider(EXAMPLE_TEMPLATE.thresholdConsider);
  }

  async function save() {
    setError(null);
    if (!name.trim()) return setError("Name is required.");
    if (criteria.length === 0) return setError("Add at least one scoring dimension.");
    if (!weightOk) {
      return setError(
        `Weights must add up to 100%. They currently total ${(totalWeight * 100).toFixed(1)}%. Use “Distribute evenly” or adjust manually.`,
      );
    }
    if (!(thresholdStrong > thresholdMatch && thresholdMatch > thresholdConsider)) {
      return setError("Thresholds must descend: Strong > Match > Consider.");
    }
    // Backfill any auto-generated keys before validation (covers the case where
    // the user typed a label, then immediately hit Save with focus still in the field).
    const finalCriteria = criteria.map((c, i, arr) => {
      if (c.key && c.key.trim()) return c;
      const others = arr.filter((_, idx) => idx !== i).map((x) => x.key).filter(Boolean);
      return { ...c, key: uniqueKey(slugify(c.label), others) };
    });
    for (let i = 0; i < finalCriteria.length; i++) {
      const c = finalCriteria[i];
      if (!c.label.trim()) return setError(`Dimension ${i + 1}: title is required.`);
      if (!c.scoringPrompt.trim()) {
        return setError(`Dimension ${i + 1}: "What to evaluate" is required.`);
      }
    }

    setSubmitting(true);
    try {
      const url =
        mode === "create"
          ? "/api/admin/recruitment/rubrics"
          : `/api/admin/recruitment/rubrics/${rubricId}`;
      const method = mode === "create" ? "POST" : "PATCH";
      const res = await fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: name.trim(),
          kind,
          jobRoleId: jobRoleId === GLOBAL ? null : jobRoleId,
          isActive,
          criteria: finalCriteria,
          thresholdStrong,
          thresholdMatch,
          thresholdConsider,
        }),
      });
      const data = await res.json();
      if (!res.ok) {
        setError(data.error ?? "Failed to save");
        setSubmitting(false);
        return;
      }
      if (onSuccess) {
        onSuccess();
        startTransition(() => router.refresh());
      } else {
        startTransition(() => router.push("/admin/recruitment/rubrics"));
      }
    } catch {
      setError("Network error");
    }
    setSubmitting(false);
  }

  async function archive() {
    if (mode !== "edit" || !rubricId) return;
    if (!confirm("Archive this rubric? Existing scores will be preserved.")) return;
    setSubmitting(true);
    try {
      const res = await fetch(`/api/admin/recruitment/rubrics/${rubricId}`, { method: "DELETE" });
      const data = await res.json();
      if (!res.ok) {
        setError(data.error ?? "Failed to archive");
        setSubmitting(false);
        return;
      }
      if (onSuccess) {
        onSuccess();
        startTransition(() => router.refresh());
      } else {
        startTransition(() => router.push("/admin/recruitment/rubrics"));
      }
    } catch {
      setError("Network error");
    }
    setSubmitting(false);
  }

  return (
    <TooltipProvider>
      <div className="space-y-6">
        {/* Explainer / template */}
        <ExplainerCard
          open={showExplainer}
          onToggle={() => setShowExplainer((v) => !v)}
          onLoadExample={loadExample}
        />

        {/* Top-level metadata */}
        <section className="rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900">
          <h3 className="mb-4 text-sm font-semibold">Rubric details</h3>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div>
              <FieldLabel
                htmlFor="rubric-name"
                help="A descriptive title for this rubric. Include the role and the stage (pre- or post-interview) so it's easy to recognise in the list. Example: 'Associate Investment Banker (REIB) — pre-interview'."
              >
                Rubric name
              </FieldLabel>
              <Input
                id="rubric-name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="e.g. Associate Investment Banker (REIB) — pre-interview"
                className="mt-1.5"
              />
            </div>
            <div>
              <FieldLabel
                htmlFor="rubric-kind"
                help="When does the AI use this rubric? 'Pre-interview' scores from the CV before any conversation. 'Post-interview' scores from interview transcripts and notes."
              >
                Stage
              </FieldLabel>
              <Select value={kind} onValueChange={(v) => setKind(v as typeof kind)}>
                <SelectTrigger id="rubric-kind" className="mt-1.5 w-full">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="pre_interview">Pre-interview (scoring from CV)</SelectItem>
                  <SelectItem value="post_interview">
                    Post-interview (scoring from interview)
                  </SelectItem>
                </SelectContent>
              </Select>
            </div>
            <div className="sm:col-span-2">
              <FieldLabel
                htmlFor="rubric-role"
                help="Pick a specific role to make this rubric apply only to applications for that role. Choose 'Global default' to make it the fallback for any role that doesn't have its own rubric."
              >
                Applies to
              </FieldLabel>
              <Select value={jobRoleId} onValueChange={(v) => setJobRoleId(v ?? GLOBAL)}>
                <SelectTrigger id="rubric-role" className="mt-1.5 w-full">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value={GLOBAL}>
                    Global default — used when no role-specific rubric exists
                  </SelectItem>
                  {jobRoles.map((r) => (
                    <SelectItem key={r.id} value={r.id}>
                      {r.department} → {r.title}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
              <p className="mt-1 text-[11px] text-muted-foreground">
                Role-specific rubrics override the global default for that role.
              </p>
            </div>

            <div className="sm:col-span-2">
              <label className="flex cursor-pointer items-center gap-2 text-xs">
                <input
                  type="checkbox"
                  checked={isActive}
                  onChange={(e) => setIsActive(e.target.checked)}
                  className="size-4 rounded border-zinc-300"
                />
                <span>
                  <strong>Active</strong> — used by the AI scoring agent. Uncheck to keep the rubric saved but pause its use.
                </span>
              </label>
            </div>
          </div>
        </section>

        {/* Thresholds */}
        <section className="rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900">
          <h3 className="mb-1 text-sm font-semibold">Recommendation thresholds</h3>
          <p className="mb-4 text-xs text-muted-foreground">
            After scoring, the AI converts the weighted total to a recommendation tier. These cut-offs
            decide which tier the candidate lands in. Higher numbers = harder to clear.
          </p>
          <div className="mb-4 rounded-md bg-zinc-50 p-3 text-[11px] leading-relaxed text-zinc-700 dark:bg-zinc-800/50 dark:text-zinc-300">
            <div>
              At or above <strong>Strong</strong> ({(thresholdStrong * 100).toFixed(0)}%) → <em>Strong Hire</em>
            </div>
            <div>
              At or above <strong>Match</strong> ({(thresholdMatch * 100).toFixed(0)}%) → <em>Hire</em>
            </div>
            <div>
              At or above <strong>Consider</strong> ({(thresholdConsider * 100).toFixed(0)}%) →{" "}
              <em>Conditional Advance — interview required</em>
            </div>
            <div>
              Below <strong>{(thresholdConsider * 0.7 * 100).toFixed(0)}%</strong> →{" "}
              <em>Do Not Advance</em>
            </div>
          </div>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
            <ThresholdInput
              label="Strong"
              help="The cut-off for the top tier ('Strong Hire'). Defaults to 0.85 (85%). Only candidates whose weighted score reaches this bar get the strongest recommendation."
              value={thresholdStrong}
              onChange={setThresholdStrong}
            />
            <ThresholdInput
              label="Match"
              help="The cut-off for a clear 'Hire' recommendation. Defaults to 0.70 (70%). Below this, the AI will recommend interviewing rather than offering."
              value={thresholdMatch}
              onChange={setThresholdMatch}
            />
            <ThresholdInput
              label="Consider"
              help="The minimum bar to move forward at all. Defaults to 0.55 (55%). Below this, the candidate is conditionally rejected."
              value={thresholdConsider}
              onChange={setThresholdConsider}
            />
          </div>
        </section>

        {/* Criteria editor */}
        <section className="rounded-xl border border-zinc-200 bg-white p-5 dark:border-zinc-800 dark:bg-zinc-900">
          <div className="mb-1 flex items-center justify-between">
            <h3 className="text-sm font-semibold">Scoring dimensions</h3>
            <div className="flex items-center gap-2">
              <span
                className={
                  "rounded-full px-2 py-0.5 text-[10px] font-semibold " +
                  (weightOk
                    ? "bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200"
                    : "bg-rose-100 text-rose-900 dark:bg-rose-950 dark:text-rose-200")
                }
              >
                Weights total: {(totalWeight * 100).toFixed(1)}%
                {weightOk ? " ✓" : " (must = 100%)"}
              </span>
              <Button type="button" variant="outline" size="sm" onClick={distributeWeightsEvenly}>
                Distribute evenly
              </Button>
              <Button type="button" size="sm" onClick={addCriterion} className="gap-1.5">
                <Plus className="size-3.5" /> Add dimension
              </Button>
            </div>
          </div>
          <p className="mb-4 text-xs text-muted-foreground">
            Each dimension is one thing the AI evaluates the candidate on. The weight is how much that
            dimension counts toward the final score. Weights must add up to 100%.
          </p>

          {criteria.length === 0 ? (
            <p className="rounded-lg border border-dashed border-zinc-300 p-6 text-center text-sm text-muted-foreground dark:border-zinc-700">
              No scoring dimensions yet. Click <strong>Add dimension</strong> to create one, or
              load the example template above.
            </p>
          ) : (
            <div className="space-y-4">
              {criteria.map((c, i) => (
                <CriterionRow
                  key={i}
                  index={i}
                  value={c}
                  onChange={(patch) => patchCriterion(i, patch)}
                  onRemove={() => removeCriterion(i)}
                />
              ))}
            </div>
          )}
        </section>

        {error && (
          <div className="flex items-start gap-2 rounded-lg bg-rose-50 p-3 text-xs text-rose-700 dark:bg-rose-950 dark:text-rose-300">
            <AlertTriangle className="mt-0.5 size-3.5 shrink-0" />
            <span>{error}</span>
          </div>
        )}

        <div className="flex items-center justify-between">
          {mode === "edit" ? (
            <Button
              type="button"
              variant="outline"
              onClick={archive}
              disabled={submitting || isPending}
              className="gap-2 text-rose-700 hover:bg-rose-50 dark:text-rose-300 dark:hover:bg-rose-950"
            >
              <Trash2 className="size-4" /> Archive
            </Button>
          ) : (
            <span />
          )}
          <Button onClick={save} disabled={submitting || isPending} className="gap-2">
            {submitting || isPending ? (
              <Loader2 className="size-4 animate-spin" />
            ) : (
              <Save className="size-4" />
            )}
            Save rubric
          </Button>
        </div>
      </div>
    </TooltipProvider>
  );
}

// ─── Sub-components ─────────────────────────────────────────────────────────

function FieldLabel({
  children,
  help,
  htmlFor,
}: {
  children: React.ReactNode;
  help: string;
  htmlFor?: string;
}) {
  return (
    <div className="flex items-center gap-1.5">
      <Label htmlFor={htmlFor} className="cursor-default">
        {children}
      </Label>
      <Tooltip>
        <TooltipTrigger
          render={
            <button
              type="button"
              className="rounded-full text-zinc-400 transition-colors hover:text-zinc-700 dark:hover:text-zinc-200"
              aria-label="What goes here?"
            />
          }
        >
          <HelpCircle className="size-3.5" />
        </TooltipTrigger>
        <TooltipContent className="max-w-xs text-xs leading-relaxed">{help}</TooltipContent>
      </Tooltip>
    </div>
  );
}

function ExplainerCard({
  open,
  onToggle,
  onLoadExample,
}: {
  open: boolean;
  onToggle: () => void;
  onLoadExample: () => void;
}) {
  return (
    <section className="overflow-hidden rounded-xl border border-blue-200 bg-blue-50/40 dark:border-blue-900 dark:bg-blue-950/30">
      <button
        type="button"
        onClick={onToggle}
        className="flex w-full items-center justify-between px-5 py-3 text-left text-sm font-semibold text-blue-900 dark:text-blue-200"
      >
        <span className="flex items-center gap-2">
          <Sparkles className="size-4" />
          How rubrics work — read this if it&apos;s your first one
        </span>
        {open ? <ChevronDown className="size-4" /> : <ChevronRight className="size-4" />}
      </button>

      {open && (
        <div className="space-y-4 border-t border-blue-200 px-5 py-4 text-[13px] leading-relaxed text-blue-950 dark:border-blue-900 dark:text-blue-100">
          <div>
            <strong>What is a rubric?</strong> A rubric is the scoring sheet the AI uses to evaluate
            a candidate. You define the dimensions (e.g. <em>experience</em>, <em>modelling skill</em>,{" "}
            <em>cultural fit</em>), how much each one counts (the weight), and what the AI should look
            for in each. The AI scores every dimension 0–10, multiplies by the weights, and produces
            a single overall recommendation.
          </div>

          <div>
            <strong>What you fill in:</strong>
            <ul className="ml-4 mt-1 list-disc space-y-1">
              <li>
                <strong>Name</strong> — a label so you can find this rubric later.
              </li>
              <li>
                <strong>Stage</strong> — pre-interview (CV scoring) or post-interview.
              </li>
              <li>
                <strong>Applies to</strong> — pick a job role, or leave as the global default.
              </li>
              <li>
                <strong>Thresholds</strong> — the cut-offs for Strong Hire / Hire / Conditional
                Advance / Do Not Advance.
              </li>
              <li>
                <strong>Scoring dimensions</strong> — the actual things the AI evaluates. For each
                one you give a title, a weight, and a paragraph telling the AI what to look for.
              </li>
            </ul>
          </div>

          <div className="rounded-lg bg-white p-3 text-zinc-700 dark:bg-zinc-900 dark:text-zinc-200">
            <div className="mb-2 text-[11px] font-semibold uppercase tracking-wide text-zinc-500">
              Example — a fully-filled scoring dimension
            </div>
            <div className="space-y-1.5 text-xs">
              <div>
                <span className="font-semibold">Title:</span> {EXAMPLE_CRITERION.label}
              </div>
              <div>
                <span className="font-semibold">Weight:</span>{" "}
                {(EXAMPLE_CRITERION.weight * 100).toFixed(0)}% (i.e. this dimension is{" "}
                {(EXAMPLE_CRITERION.weight * 100).toFixed(0)}% of the total score)
              </div>
              <div>
                <span className="font-semibold">What to evaluate:</span>{" "}
                <span className="italic">{EXAMPLE_CRITERION.scoringPrompt}</span>
              </div>
              <div>
                <span className="font-semibold">What the AI should mention:</span>{" "}
                <span className="italic">{EXAMPLE_CRITERION.commentaryGuidance}</span>
              </div>
              <div>
                <span className="font-semibold">Red flags to watch for:</span>{" "}
                <span className="italic">{EXAMPLE_CRITERION.redFlagSignals?.join(" · ")}</span>
              </div>
            </div>
          </div>

          <div className="flex items-center justify-between gap-3 rounded-lg border border-blue-200 bg-white px-3 py-2 dark:border-blue-900 dark:bg-zinc-900">
            <span className="text-xs">
              Want a complete sample rubric to start from? Click to fill the form with the example.
            </span>
            <Button type="button" size="sm" variant="outline" onClick={onLoadExample} className="gap-1.5">
              <Sparkles className="size-3.5" /> Load example
            </Button>
          </div>
        </div>
      )}
    </section>
  );
}

function ThresholdInput({
  label,
  help,
  value,
  onChange,
}: {
  label: string;
  help: string;
  value: number;
  onChange: (n: number) => void;
}) {
  return (
    <div>
      <FieldLabel htmlFor={`thresh-${label}`} help={help}>
        {label}
      </FieldLabel>
      <div className="mt-1.5 flex items-center gap-2">
        <Input
          id={`thresh-${label}`}
          type="number"
          step="0.01"
          min="0"
          max="1"
          value={value}
          onChange={(e) => onChange(Number(e.target.value))}
          className="w-28"
        />
        <span className="text-xs text-muted-foreground">({(value * 100).toFixed(0)}%)</span>
      </div>
    </div>
  );
}

function CriterionRow({
  index,
  value,
  onChange,
  onRemove,
}: {
  index: number;
  value: Criterion;
  onChange: (patch: Partial<Criterion>) => void;
  onRemove: () => void;
}) {
  const redFlagsString = (value.redFlagSignals ?? []).join("; ");
  const derivedKey = value.key || (value.label ? slugify(value.label) : "");

  return (
    <div className="rounded-lg border border-zinc-200 bg-zinc-50/50 p-4 dark:border-zinc-800 dark:bg-zinc-800/30">
      <div className="mb-3 flex items-center justify-between">
        <span className="text-[10px] font-semibold uppercase tracking-wide text-zinc-500">
          Dimension {index + 1}
        </span>
        <button
          type="button"
          onClick={onRemove}
          className="rounded-md p-1 text-zinc-400 hover:bg-rose-50 hover:text-rose-500 dark:hover:bg-rose-950"
          aria-label="Remove dimension"
        >
          <Trash2 className="size-3.5" />
        </button>
      </div>
      <div className="grid grid-cols-1 gap-3 sm:grid-cols-12">
        <div className="sm:col-span-9">
          <FieldLabel
            help="A short, plain-English title for the dimension. This is what shows up in the candidate report. Examples: 'Real Estate IB Experience', 'Communication & Stakeholder Management', 'Cultural Fit'."
          >
            Dimension title
          </FieldLabel>
          <Input
            value={value.label}
            onChange={(e) => onChange({ label: e.target.value })}
            placeholder="e.g. Real Estate Investment Banking Experience"
            className="mt-1.5"
          />
          {derivedKey && (
            <p className="mt-1 text-[10px] text-muted-foreground">
              Internal ID:{" "}
              <code className="rounded bg-zinc-100 px-1 py-0.5 text-[10px] dark:bg-zinc-800">
                {derivedKey}
              </code>{" "}
              (auto-generated)
            </p>
          )}
        </div>
        <div className="sm:col-span-3">
          <FieldLabel
            help="How much this dimension counts toward the total score, as a decimal between 0 and 1. All dimensions must add up to 1.0 (100%). Use 'Distribute evenly' if you're unsure."
          >
            Weight
          </FieldLabel>
          <Input
            type="number"
            step="0.01"
            min="0"
            max="1"
            value={value.weight}
            onChange={(e) => onChange({ weight: Number(e.target.value) })}
            className="mt-1.5"
          />
          <p className="mt-1 text-[10px] text-muted-foreground">
            {(value.weight * 100).toFixed(0)}% of total
          </p>
        </div>
        <div className="sm:col-span-12">
          <FieldLabel
            help="Tell the AI exactly what it's evaluating and how to assign a score from 0 to 10. Be specific — name companies, qualifications, deal sizes, or experience levels that map to specific score bands. The clearer you are, the more consistent the AI's scoring will be."
          >
            What to evaluate
          </FieldLabel>
          <Textarea
            rows={3}
            value={value.scoringPrompt}
            onChange={(e) => onChange({ scoringPrompt: e.target.value })}
            placeholder={
              "Tell the AI what to look for and how to score it 0–10.\n\n" +
              "e.g. 'Years of direct REIB experience at named platforms (JLL, CBRE, Cushman, Brookfield, Blackstone). Score 8–10 for global Tier 1 platforms with named deal-lead roles; 5–7 for regional or boutique advisory; 3–4 for adjacent finance experience; 0–2 for none.'"
            }
            className="mt-1.5"
          />
        </div>
        <div className="sm:col-span-12">
          <FieldLabel
            help="Optional. What specific facts, names, numbers, or details should the AI reference when writing its commentary on this dimension? This helps make the report feel concrete rather than vague."
          >
            What the AI should mention <span className="text-muted-foreground">(optional)</span>
          </FieldLabel>
          <Textarea
            rows={2}
            value={value.commentaryGuidance ?? ""}
            onChange={(e) => onChange({ commentaryGuidance: e.target.value })}
            placeholder="e.g. 'Name the firms, deal sizes, ARGUS proficiency, REIT-specific valuation experience.'"
            className="mt-1.5"
          />
        </div>
        <div className="sm:col-span-12">
          <FieldLabel
            help="Optional. Specific concerns that, if found, should appear in the candidate's risk register. Separate items with a semicolon (;). Example: 'predatory lending association; multiple <1y stints; no named deals'."
          >
            Red flags to watch for{" "}
            <span className="text-muted-foreground">(optional)</span>
          </FieldLabel>
          <Input
            value={redFlagsString}
            onChange={(e) =>
              onChange({
                redFlagSignals: e.target.value
                  .split(";")
                  .map((s) => s.trim())
                  .filter(Boolean),
              })
            }
            placeholder="e.g. predatory lending association; multiple <1y stints; gaps in employment"
            className="mt-1.5"
          />
          <p className="mt-1 text-[10px] text-muted-foreground">
            Separate multiple red flags with semicolons. If the AI detects any, they appear in the
            candidate&apos;s risk register.
          </p>
        </div>
      </div>
    </div>
  );
}

```