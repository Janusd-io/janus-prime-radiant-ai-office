---
type: source
source_type: laptop
title: CandidateFiltersBar
slug: candidatefiltersbar
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/recruitment/candidates/CandidateFiltersBar.tsx
original_size: 5560
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# CandidateFiltersBar

_Extracted from `[[assessify|assessify]]/src/app/admin/recruitment/candidates/CandidateFiltersBar.tsx` on 2026-05-14._

```tsx
"use client";

import { useState, useTransition } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { Search, X, RotateCcw, SlidersHorizontal } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

const ALL = "__all__";

const sourceOptions: Array<[string, string]> = [
  ["agency", "Agency"],
  ["direct", "Direct"],
  ["career_page", "Career page"],
  ["referral", "Referral"],
];
const officeOptions: Array<[string, string]> = [
  ["Dubai", "Dubai"],
  ["Singapore", "Singapore"],
];

type Props = {
  initial: { q?: string; office?: string; source?: string };
};

export function CandidateFiltersBar({ initial }: Props) {
  const router = useRouter();
  const search = useSearchParams();
  const [isPending, startTransition] = useTransition();

  const [q, setQ] = useState(initial.q ?? "");
  const [office, setOffice] = useState(initial.office ?? "");
  const [source, setSource] = useState(initial.source ?? "");

  const activeCount = [q, office, source].filter(Boolean).length;
  const hasPersistedFilters = Array.from(search.keys()).length > 0;

  function apply() {
    const params = new URLSearchParams();
    if (q.trim()) params.set("q", q.trim());
    if (office) params.set("office", office);
    if (source) params.set("source", source);
    const qs = params.toString();
    startTransition(() => router.push(qs ? `?${qs}` : "?"));
  }

  function reset() {
    setQ("");
    setOffice("");
    setSource("");
    startTransition(() => router.push("?"));
  }

  function onKeyDown(e: React.KeyboardEvent<HTMLInputElement>) {
    if (e.key === "Enter") {
      e.preventDefault();
      apply();
    }
  }

  return (
    <div className="mb-4 rounded-xl border border-zinc-200 bg-white p-4 shadow-sm dark:border-zinc-800 dark:bg-zinc-900">
      <div className="mb-3 flex items-center gap-2">
        <SlidersHorizontal className="size-4 text-zinc-500" />
        <span className="text-sm font-medium">Filters</span>
        {activeCount > 0 && (
          <span className="rounded-full bg-zinc-100 px-2 py-0.5 text-[10px] font-semibold text-zinc-700 dark:bg-zinc-800 dark:text-zinc-200">
            {activeCount} active
          </span>
        )}
      </div>

      <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <div className="lg:col-span-2">
          <Label htmlFor="cand-search" className="text-xs">
            Search
          </Label>
          <div className="relative mt-1.5">
            <Search className="pointer-events-none absolute left-2.5 top-1/2 size-4 -translate-y-1/2 text-zinc-400" />
            <Input
              id="cand-search"
              value={q}
              onChange={(e) => setQ(e.target.value)}
              onKeyDown={onKeyDown}
              placeholder="Name, email, agency"
              className="pl-8"
            />
            {q && (
              <button
                type="button"
                aria-label="Clear search"
                onClick={() => setQ("")}
                className="absolute right-2 top-1/2 flex size-5 -translate-y-1/2 items-center justify-center rounded-full text-zinc-400 hover:bg-zinc-100 hover:text-zinc-700 dark:hover:bg-zinc-800 dark:hover:text-zinc-200"
              >
                <X className="size-3" />
              </button>
            )}
          </div>
        </div>

        <FilterSelect
          id="cand-office"
          label="Office"
          value={office}
          onChange={setOffice}
          options={officeOptions}
          placeholder="All offices"
        />
        <FilterSelect
          id="cand-source"
          label="Source"
          value={source}
          onChange={setSource}
          options={sourceOptions}
          placeholder="All sources"
        />
      </div>

      <div className="mt-4 flex items-center justify-end gap-2 border-t border-zinc-100 pt-3 dark:border-zinc-800">
        {(activeCount > 0 || hasPersistedFilters) && (
          <Button
            type="button"
            variant="ghost"
            size="sm"
            onClick={reset}
            disabled={isPending}
            className="gap-1.5"
          >
            <RotateCcw className="size-3.5" />
            Reset
          </Button>
        )}
        <Button type="button" size="sm" onClick={apply} disabled={isPending} className="gap-1.5">
          {isPending ? "Applying…" : "Apply filters"}
        </Button>
      </div>
    </div>
  );
}

function FilterSelect({
  id,
  label,
  value,
  onChange,
  options,
  placeholder,
}: {
  id: string;
  label: string;
  value: string;
  onChange: (v: string) => void;
  options: Array<[string, string]>;
  placeholder: string;
}) {
  return (
    <div>
      <Label htmlFor={id} className="text-xs">
        {label}
      </Label>
      <Select
        value={value || ALL}
        onValueChange={(v) => onChange(!v || v === ALL ? "" : v)}
      >
        <SelectTrigger id={id} className="mt-1.5 w-full">
          <SelectValue placeholder={placeholder} />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value={ALL}>{placeholder}</SelectItem>
          {options.map(([v, l]) => (
            <SelectItem key={v} value={v}>
              {l}
            </SelectItem>
          ))}
        </SelectContent>
      </Select>
    </div>
  );
}

```