---
type: source
source_type: laptop
title: page
slug: page-27
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/question-bank/page.tsx
original_size: 33649
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `assessify/src/app/admin/question-bank/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useMemo, useState } from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  HelpCircle,
  Search,
  Loader2,
  Brain,
  Building2,
  ChevronDown,
  Plus,
  Trash2,
  AlertTriangle,
  X,
  Save,
  Library,
} from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

interface BankQuestion {
  id: string;
  sectionId: string;
  templateId: string;
  isLibraryPrimary: boolean;
  bankSection: { slug: string; label: string };
  title: string;
  prompt: string;
  questionType: string;
  difficulty: string;
  maxPoints: number;
  scoringStrategy?: string;
  options: Array<{ key: string; label: string; points: number; isCorrect: boolean }>;
  competencies: Array<{ id: string; name: string; slug: string }>;
  departments: Array<{ name: string; slug: string }>;
  departmentSlugs: string[];
  usages: Array<{
    templateId: string; templateTitle: string; department: string;
    departmentSlug: string; sectionTitle: string; isLibrary: boolean;
  }>;
}

const BANK_SECTIONS = [
  { slug: "cultural-fit", label: "Cultural Fit", color: "text-pink-600 bg-pink-50 dark:bg-pink-950" },
  { slug: "ai-awareness", label: "AI Awareness", color: "text-blue-600 bg-blue-50 dark:bg-blue-950" },
  { slug: "department-specific", label: "Department-Specific", color: "text-purple-600 bg-purple-50 dark:bg-purple-950" },
  { slug: "general", label: "General", color: "text-zinc-600 bg-zinc-100 dark:bg-zinc-800" },
];

interface Department {
  id: string;
  name: string;
  slug: string;
}

interface Competency {
  id: string;
  name: string;
  slug: string;
  category: string | null;
}

const difficultyColors: Record<string, string> = {
  easy: "bg-green-100 text-green-700 dark:bg-green-950 dark:text-green-300",
  medium: "bg-amber-100 text-amber-700 dark:bg-amber-950 dark:text-amber-300",
  hard: "bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300",
};

export default function QuestionBankPage() {
  const [questions, setQuestions] = useState<BankQuestion[]>([]);
  const [departments, setDepartments] = useState<Department[]>([]);
  const [competencies, setCompetencies] = useState<Competency[]>([]);
  const [activeDept, setActiveDept] = useState<string>("all");
  const [activeBankSection, setActiveBankSection] = useState<string>("all");
  const [search, setSearch] = useState("");
  const [filterCompetency, setFilterCompetency] = useState("all");
  const [filterDifficulty, setFilterDifficulty] = useState("all");
  const [filterType, setFilterType] = useState("all");
  const [expanded, setExpanded] = useState<Set<string>>(new Set());
  const [loading, setLoading] = useState(true);
  const [showAddModal, setShowAddModal] = useState(false);
  const [deleteTarget, setDeleteTarget] = useState<BankQuestion | null>(null);
  const [deleteError, setDeleteError] = useState<string | null>(null);
  const [isDeleting, setIsDeleting] = useState(false);

  const loadAll = async () => {
    setLoading(true);
    const [q, d, c] = await Promise.all([
      fetch("/api/admin/question-bank").then((r) => r.json()),
      fetch("/api/admin/departments").then((r) => r.json()),
      fetch("/api/admin/competencies").then((r) => r.json()),
    ]);
    setQuestions(q.questions ?? []);
    setDepartments(d.departments ?? []);
    setCompetencies(c.competencies ?? []);
    setLoading(false);
  };

  useEffect(() => {
    // Canonical fetch-on-mount; cascade is bounded.
    // eslint-disable-next-line react-hooks/set-state-in-effect
    loadAll();
  }, []);

  const filtered = useMemo(() => {
    const s = search.trim().toLowerCase();
    return questions.filter((q) => {
      if (activeDept !== "all" && !q.departmentSlugs.includes(activeDept)) return false;
      if (activeBankSection !== "all" && q.bankSection?.slug !== activeBankSection) return false;
      if (s && !`${q.title} ${q.prompt}`.toLowerCase().includes(s)) return false;
      if (filterCompetency !== "all" && !q.competencies.some((c) => c.slug === filterCompetency)) return false;
      if (filterDifficulty !== "all" && q.difficulty !== filterDifficulty) return false;
      if (filterType !== "all" && q.questionType !== filterType) return false;
      return true;
    });
  }, [questions, activeDept, activeBankSection, search, filterCompetency, filterDifficulty, filterType]);

  const sectionCounts = useMemo(() => {
    const base = questions.filter((q) => activeDept === "all" || q.departmentSlugs.includes(activeDept));
    const counts: Record<string, number> = { all: base.length };
    for (const s of BANK_SECTIONS) {
      counts[s.slug] = base.filter((q) => q.bankSection?.slug === s.slug).length;
    }
    return counts;
  }, [questions, activeDept]);

  const deptCounts = useMemo(() => {
    const counts: Record<string, number> = { all: questions.length };
    for (const d of departments) {
      counts[d.slug] = questions.filter((q) => q.departmentSlugs.includes(d.slug)).length;
    }
    return counts;
  }, [questions, departments]);

  const toggle = (id: string) => {
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id); else next.add(id);
      return next;
    });
  };

  const handleDelete = async () => {
    if (!deleteTarget) return;
    setIsDeleting(true);
    setDeleteError(null);
    try {
      const res = await fetch(`/api/admin/question-bank?id=${deleteTarget.id}`, { method: "DELETE" });
      const data = await res.json();
      if (!res.ok) { setDeleteError(data.error); setIsDeleting(false); return; }
      await loadAll();
      setDeleteTarget(null);
    } catch { setDeleteError("Network error"); }
    setIsDeleting(false);
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">Question Bank</h1>
          <p className="text-sm text-muted-foreground">
            Browse, add, and reuse questions across departments.
          </p>
        </div>
        <Button onClick={() => setShowAddModal(true)} className="gap-2">
          <Plus className="size-4" /> Add Question
        </Button>
      </div>

      {/* Department tabs */}
      <div className="flex gap-1 overflow-x-auto border-b border-zinc-200 dark:border-zinc-800">
        {[{ slug: "all", name: "All" }, ...departments].map((d) => (
          <button
            key={d.slug}
            onClick={() => setActiveDept(d.slug)}
            className={`flex items-center gap-2 whitespace-nowrap rounded-t-lg border-b-2 px-4 py-2 text-sm font-medium transition-colors ${
              activeDept === d.slug
                ? "border-primary text-primary"
                : "border-transparent text-muted-foreground hover:text-foreground"
            }`}
          >
            {d.slug !== "all" && <Building2 className="size-3.5" />}
            {d.name}
            <span className={`rounded-full px-1.5 py-0.5 text-[10px] font-medium ${
              activeDept === d.slug ? "bg-primary/10 text-primary" : "bg-zinc-100 text-muted-foreground dark:bg-zinc-800"
            }`}>
              {deptCounts[d.slug] ?? 0}
            </span>
          </button>
        ))}
      </div>

      {/* Section sub-tabs */}
      <div className="flex flex-wrap gap-2">
        {[{ slug: "all", label: "All Sections", color: "text-foreground bg-zinc-100 dark:bg-zinc-800" }, ...BANK_SECTIONS].map((s) => {
          const active = activeBankSection === s.slug;
          return (
            <button
              key={s.slug}
              onClick={() => setActiveBankSection(s.slug)}
              className={`inline-flex items-center gap-2 rounded-full border px-3 py-1 text-xs font-medium transition-colors ${
                active
                  ? "border-primary bg-primary/10 text-primary"
                  : "border-zinc-200 text-muted-foreground hover:border-zinc-300 dark:border-zinc-700"
              }`}
            >
              {s.label}
              <span className="rounded-full bg-zinc-200/60 px-1.5 py-0.5 text-[10px] dark:bg-zinc-700/60">
                {sectionCounts[s.slug] ?? 0}
              </span>
            </button>
          );
        })}
      </div>

      {/* Filters */}
      <Card>
        <CardContent className="pt-3">
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-4">
            <div className="relative sm:col-span-2">
              <Search className="absolute left-3 top-1/2 size-3.5 -translate-y-1/2 text-muted-foreground" />
              <Input
                placeholder="Search questions..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className="pl-9"
              />
            </div>
            <Select value={filterCompetency} onValueChange={(v) => setFilterCompetency(v ?? "all")}>
              <SelectTrigger><SelectValue placeholder="Competency" /></SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Competencies</SelectItem>
                {competencies.map((c) => (
                  <SelectItem key={c.id} value={c.slug}>{c.name}</SelectItem>
                ))}
              </SelectContent>
            </Select>
            <div className="flex gap-2">
              <Select value={filterDifficulty} onValueChange={(v) => setFilterDifficulty(v ?? "all")}>
                <SelectTrigger><SelectValue placeholder="Difficulty" /></SelectTrigger>
                <SelectContent>
                  <SelectItem value="all">All</SelectItem>
                  <SelectItem value="easy">Easy</SelectItem>
                  <SelectItem value="medium">Medium</SelectItem>
                  <SelectItem value="hard">Hard</SelectItem>
                </SelectContent>
              </Select>
              <Select value={filterType} onValueChange={(v) => setFilterType(v ?? "all")}>
                <SelectTrigger><SelectValue placeholder="Type" /></SelectTrigger>
                <SelectContent>
                  <SelectItem value="all">All Types</SelectItem>
                  <SelectItem value="single_select">Single Select</SelectItem>
                  <SelectItem value="multi_select">Multi Select</SelectItem>
                  <SelectItem value="ranking">Ranking</SelectItem>
                  <SelectItem value="scenario">Scenario</SelectItem>
                  <SelectItem value="situational_judgment">Situational</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* List */}
      {loading ? (
        <Card>
          <CardContent className="flex items-center justify-center py-12">
            <Loader2 className="size-6 animate-spin text-muted-foreground" />
          </CardContent>
        </Card>
      ) : filtered.length === 0 ? (
        <Card>
          <CardContent className="flex flex-col items-center py-12">
            <HelpCircle className="size-10 text-muted-foreground" />
            <p className="mt-3 text-sm text-muted-foreground">
              {questions.length === 0
                ? "No questions in the bank yet."
                : "No questions match your filters."}
            </p>
            {questions.length === 0 && (
              <Button onClick={() => setShowAddModal(true)} className="mt-3 gap-2">
                <Plus className="size-4" /> Add your first question
              </Button>
            )}
          </CardContent>
        </Card>
      ) : (
        <Card>
          <CardHeader>
            <CardTitle>{filtered.length} {filtered.length === 1 ? "question" : "questions"}</CardTitle>
            <CardDescription>
              Click any question to expand and see options, scoring, and where it&apos;s used
            </CardDescription>
          </CardHeader>
          <CardContent className="px-3 sm:px-4">
            <div className="space-y-2">
              {filtered.map((q) => {
                const isOpen = expanded.has(q.id);
                return (
                  <div key={q.id} className="rounded-lg border border-zinc-100 dark:border-zinc-800">
                    <div className="flex items-start gap-3 px-4 py-3">
                      <button onClick={() => toggle(q.id)} className="mt-0.5 text-muted-foreground hover:text-foreground">
                        <ChevronDown className={`size-4 transition-transform ${isOpen ? "rotate-180" : ""}`} />
                      </button>
                      <button
                        onClick={() => toggle(q.id)}
                        className="min-w-0 flex-1 text-left"
                      >
                        <div className="flex flex-wrap items-center gap-2">
                          <p className="text-sm font-medium">{q.title}</p>
                          <span className={`rounded-full px-2 py-0.5 text-[10px] font-medium ${difficultyColors[q.difficulty] ?? ""}`}>
                            {q.difficulty}
                          </span>
                          <Badge variant="secondary" className="text-[10px]">{q.maxPoints} pts</Badge>
                          <Badge variant="outline" className="text-[10px]">{q.questionType.replace(/_/g, " ")}</Badge>
                          {q.bankSection && (
                            <span className={`rounded-full px-2 py-0.5 text-[10px] font-medium ${
                              BANK_SECTIONS.find((s) => s.slug === q.bankSection.slug)?.color ?? "bg-zinc-100 text-zinc-700"
                            }`}>
                              {q.bankSection.label}
                            </span>
                          )}
                        </div>
                        <p className="mt-1 line-clamp-1 text-xs text-muted-foreground">{q.prompt}</p>
                        <div className="mt-1.5 flex flex-wrap gap-1">
                          {q.departments.map((d) => (
                            <span key={d.slug} className="inline-flex items-center gap-1 rounded-full bg-zinc-100 px-1.5 py-0.5 text-[9px] text-zinc-700 dark:bg-zinc-800 dark:text-zinc-300">
                              <Building2 className="size-2.5" />{d.name}
                            </span>
                          ))}
                          {q.competencies.slice(0, 2).map((c) => (
                            <span key={c.id} className="inline-flex items-center gap-1 rounded-full bg-blue-50 px-1.5 py-0.5 text-[9px] text-blue-700 dark:bg-blue-950 dark:text-blue-300">
                              <Brain className="size-2.5" />{c.name}
                            </span>
                          ))}
                          {q.competencies.length > 2 && (
                            <span className="text-[9px] text-muted-foreground">+{q.competencies.length - 2} more</span>
                          )}
                          {q.usages.length > 1 && (
                            <span className="ml-auto inline-flex items-center gap-1 rounded-full bg-amber-50 px-1.5 py-0.5 text-[9px] text-amber-700 dark:bg-amber-950 dark:text-amber-300">
                              Used in {q.usages.length}
                            </span>
                          )}
                        </div>
                      </button>
                      <button
                        onClick={() => { setDeleteTarget(q); setDeleteError(null); }}
                        className="rounded-md p-1.5 text-zinc-400 hover:bg-red-50 hover:text-red-500 dark:hover:bg-red-950"
                      >
                        <Trash2 className="size-3.5" />
                      </button>
                    </div>

                    <AnimatePresence>
                      {isOpen && (
                        <motion.div
                          initial={{ height: 0, opacity: 0 }}
                          animate={{ height: "auto", opacity: 1 }}
                          exit={{ height: 0, opacity: 0 }}
                          className="overflow-hidden"
                        >
                          <div className="border-t border-zinc-100 px-6 py-4 dark:border-zinc-800">
                            <p className="mb-3 whitespace-pre-line text-sm text-muted-foreground">{q.prompt}</p>
                            {q.options.length > 0 && (
                              <div className="mb-3">
                                <p className="mb-1.5 text-[10px] font-semibold uppercase tracking-wider text-muted-foreground">Options</p>
                                <div className="space-y-1">
                                  {q.options.map((opt) => (
                                    <div key={opt.key} className="flex items-center gap-2 rounded-md bg-zinc-50 px-2 py-1.5 text-xs dark:bg-zinc-800/50">
                                      <span className="font-mono text-[10px] text-muted-foreground">{opt.key}</span>
                                      <span className="flex-1">{opt.label}</span>
                                      <span className="text-[10px] text-muted-foreground">{opt.points} pts</span>
                                      {opt.isCorrect && (
                                        <span className="rounded-full bg-emerald-100 px-1.5 py-0.5 text-[9px] font-bold text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300">✓</span>
                                      )}
                                    </div>
                                  ))}
                                </div>
                              </div>
                            )}
                            {q.usages.length > 0 && (
                              <div>
                                <p className="mb-1.5 text-[10px] font-semibold uppercase tracking-wider text-muted-foreground">Used In</p>
                                <div className="space-y-0.5">
                                  {q.usages.map((u, i) => (
                                    <div key={i} className="flex items-center gap-1 text-[10px]">
                                      <Building2 className="size-2.5 text-muted-foreground" />
                                      <span className="text-muted-foreground">{u.department}</span>
                                      <span>·</span>
                                      <span>{u.templateTitle}</span>
                                      <span className="text-muted-foreground">→ {u.sectionTitle}</span>
                                      {u.isLibrary && (
                                        <Badge variant="secondary" className="text-[9px]">Library</Badge>
                                      )}
                                    </div>
                                  ))}
                                </div>
                              </div>
                            )}
                          </div>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>
                );
              })}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Add modal */}
      {showAddModal && (
        <AddQuestionModal
          departments={departments}
          competencies={competencies}
          defaultDepartmentSlug={activeDept !== "all" ? activeDept : undefined}
          defaultBankSectionSlug={activeBankSection !== "all" ? activeBankSection : undefined}
          onClose={() => setShowAddModal(false)}
          onSaved={() => { setShowAddModal(false); loadAll(); }}
        />
      )}

      {/* Delete confirmation */}
      {deleteTarget && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          <div className="fixed inset-0 bg-black/50" onClick={() => setDeleteTarget(null)} />
          <div className="relative z-10 w-full max-w-sm rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
            <div className="mb-4 flex items-center gap-3">
              <div className="rounded-lg bg-red-50 p-2 dark:bg-red-950">
                <AlertTriangle className="size-5 text-red-600" />
              </div>
              <div>
                <h3 className="text-sm font-semibold">Delete Question</h3>
                <p className="text-xs text-muted-foreground">This removes it from the bank.</p>
              </div>
            </div>
            <p className="mb-5 text-sm text-muted-foreground">
              Delete <strong className="text-foreground">{deleteTarget.title}</strong>?
              {deleteTarget.usages.length > 1 && (
                <span className="mt-1 block text-xs text-amber-600 dark:text-amber-400">
                  Note: this question appears in {deleteTarget.usages.length} places.
                  Only the primary copy will be removed.
                </span>
              )}
            </p>
            {deleteError && (
              <p className="mb-3 rounded-lg bg-red-50 p-2 text-xs text-red-700 dark:bg-red-950 dark:text-red-300">
                {deleteError}
              </p>
            )}
            <div className="flex justify-end gap-3">
              <Button variant="outline" onClick={() => setDeleteTarget(null)} disabled={isDeleting}>Cancel</Button>
              <Button variant="destructive" onClick={handleDelete} disabled={isDeleting} className="gap-2">
                {isDeleting ? <Loader2 className="size-4 animate-spin" /> : <Trash2 className="size-4" />}
                Delete
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

// ─── Add Question Modal ───────────────────────────────────

function AddQuestionModal({
  departments, competencies, defaultDepartmentSlug, defaultBankSectionSlug, onClose, onSaved,
}: {
  departments: Department[];
  competencies: Competency[];
  defaultDepartmentSlug?: string;
  defaultBankSectionSlug?: string;
  onClose: () => void;
  onSaved: () => void;
}) {
  const initialDept = defaultDepartmentSlug
    ? departments.find((d) => d.slug === defaultDepartmentSlug)?.id ?? ""
    : "";

  const [departmentId, setDepartmentId] = useState(initialDept);
  const [bankSectionSlug, setBankSectionSlug] = useState(defaultBankSectionSlug ?? "general");
  const [title, setTitle] = useState("");
  const [prompt, setPrompt] = useState("");
  const [questionType, setQuestionType] = useState("single_select");
  const [difficulty, setDifficulty] = useState("medium");
  const [maxPoints, setMaxPoints] = useState("10");
  const [scoringStrategy, setScoringStrategy] = useState("weighted_options");
  const [options, setOptions] = useState<Array<{ key: string; label: string; points: number; isCorrect: boolean }>>([
    { key: "a", label: "", points: 0, isCorrect: false },
    { key: "b", label: "", points: 0, isCorrect: false },
  ]);
  const [selectedComps, setSelectedComps] = useState<Set<string>>(new Set());
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const addOption = () => {
    const key = String.fromCharCode(97 + options.length);
    setOptions([...options, { key, label: "", points: 0, isCorrect: false }]);
  };

  const removeOption = (i: number) => setOptions(options.filter((_, idx) => idx !== i));

  const save = async () => {
    if (!departmentId || !title.trim() || !prompt.trim()) return;
    setSaving(true);
    setError(null);
    try {
      const res = await fetch("/api/admin/question-bank", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          departmentId,
          bankSectionSlug,
          title,
          prompt,
          questionType,
          difficulty,
          maxPoints: parseFloat(maxPoints),
          scoringStrategy,
          options,
          competencies: [...selectedComps].map((id) => ({ competencyId: id, weight: 1.0 })),
        }),
      });
      const data = await res.json();
      if (!res.ok) { setError(data.error); setSaving(false); return; }
      onSaved();
    } catch { setError("Network error"); }
    setSaving(false);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div className="fixed inset-0 bg-black/50" onClick={onClose} />
      <div className="relative z-10 max-h-[90vh] w-full max-w-2xl overflow-y-auto rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
        <div className="mb-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="rounded-lg bg-primary/10 p-2">
              <Library className="size-5 text-primary" />
            </div>
            <div>
              <h3 className="text-sm font-semibold">Add Question to Bank</h3>
              <p className="text-xs text-muted-foreground">This question will be reusable across assessments.</p>
            </div>
          </div>
          <button onClick={onClose} className="rounded-md p-1 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800">
            <X className="size-4" />
          </button>
        </div>

        <div className="space-y-4">
          <div>
            <Label>Department</Label>
            <div className="mt-1.5">
              <Select value={departmentId} onValueChange={(v) => setDepartmentId(v ?? "")}>
                <SelectTrigger className="w-full">
                  <SelectValue placeholder="Pick a department" />
                </SelectTrigger>
                <SelectContent>
                  {departments.map((d) => (
                    <SelectItem key={d.id} value={d.id}>{d.name}</SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
          </div>

          <div>
            <Label>Bank Section</Label>
            <div className="mt-1.5">
              <Select value={bankSectionSlug} onValueChange={(v) => setBankSectionSlug(v ?? "general")}>
                <SelectTrigger className="w-full">
                  <SelectValue placeholder="Pick a section" />
                </SelectTrigger>
                <SelectContent>
                  {BANK_SECTIONS.map((s) => (
                    <SelectItem key={s.slug} value={s.slug}>{s.label}</SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            <p className="mt-1 text-[11px] text-muted-foreground">
              Determines which group this question appears under in the bank.
            </p>
          </div>

          <div>
            <Label>Question Title</Label>
            <Input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Short internal title" className="mt-1.5" />
          </div>

          <div>
            <Label>Question Prompt (shown to candidate)</Label>
            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="The full question text..."
              className="mt-1.5 min-h-[80px] w-full rounded-lg border border-input bg-transparent p-3 text-sm outline-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50"
            />
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <Label>Type</Label>
              <div className="mt-1.5">
                <Select value={questionType} onValueChange={(v) => setQuestionType(v ?? "single_select")}>
                  <SelectTrigger className="w-full"><SelectValue /></SelectTrigger>
                  <SelectContent>
                    <SelectItem value="single_select">Single Select</SelectItem>
                    <SelectItem value="multi_select">Multi Select</SelectItem>
                    <SelectItem value="ranking">Ranking</SelectItem>
                    <SelectItem value="scenario">Scenario</SelectItem>
                    <SelectItem value="situational_judgment">Situational Judgment</SelectItem>
                  </SelectContent>
                </Select>
              </div>
            </div>
            <div>
              <Label>Difficulty</Label>
              <div className="mt-1.5">
                <Select value={difficulty} onValueChange={(v) => setDifficulty(v ?? "medium")}>
                  <SelectTrigger className="w-full"><SelectValue /></SelectTrigger>
                  <SelectContent>
                    {["easy", "medium", "hard"].map((d) => <SelectItem key={d} value={d}>{d}</SelectItem>)}
                  </SelectContent>
                </Select>
              </div>
            </div>
            <div>
              <Label>Max Points</Label>
              <Input type="number" step="0.1" value={maxPoints} onChange={(e) => setMaxPoints(e.target.value)} className="mt-1.5" />
            </div>
            <div>
              <Label>Scoring Strategy</Label>
              <div className="mt-1.5">
                <Select value={scoringStrategy} onValueChange={(v) => setScoringStrategy(v ?? "weighted_options")}>
                  <SelectTrigger className="w-full"><SelectValue /></SelectTrigger>
                  <SelectContent>
                    <SelectItem value="weighted_options">Weighted Options</SelectItem>
                    <SelectItem value="exact">Exact Match</SelectItem>
                    <SelectItem value="partial">Partial Credit</SelectItem>
                    <SelectItem value="scenario_based">Scenario-Based</SelectItem>
                  </SelectContent>
                </Select>
              </div>
            </div>
          </div>

          {/* Options */}
          <div>
            <div className="mb-2 flex items-center justify-between">
              <Label>Answer Options</Label>
              <Button variant="outline" onClick={addOption} className="gap-1 text-xs">
                <Plus className="size-3" /> Add Option
              </Button>
            </div>
            <div className="space-y-2">
              {options.map((opt, i) => (
                <div key={i} className="flex items-center gap-2 rounded-lg bg-zinc-50 p-2 dark:bg-zinc-800/50">
                  <Input value={opt.key} onChange={(e) => { const u = [...options]; u[i] = { ...u[i], key: e.target.value }; setOptions(u); }} className="w-16" placeholder="Key" />
                  <Input value={opt.label} onChange={(e) => { const u = [...options]; u[i] = { ...u[i], label: e.target.value }; setOptions(u); }} className="flex-1" placeholder="Option text" />
                  <Input type="number" step="0.1" value={opt.points} onChange={(e) => { const u = [...options]; u[i] = { ...u[i], points: parseFloat(e.target.value) || 0 }; setOptions(u); }} className="w-20" placeholder="Points" />
                  <label className="flex items-center gap-1 text-xs">
                    <input type="checkbox" checked={opt.isCorrect} onChange={(e) => { const u = [...options]; u[i] = { ...u[i], isCorrect: e.target.checked }; setOptions(u); }} />
                    Correct
                  </label>
                  <button onClick={() => removeOption(i)} className="rounded-md p-1 text-zinc-400 hover:text-red-500">
                    <Trash2 className="size-3.5" />
                  </button>
                </div>
              ))}
            </div>
          </div>

          {/* Competencies */}
          <div>
            <Label>Competencies</Label>
            <div className="mt-2 flex flex-wrap gap-1.5">
              {competencies.map((c) => {
                const selected = selectedComps.has(c.id);
                return (
                  <button
                    key={c.id}
                    onClick={() => {
                      const next = new Set(selectedComps);
                      if (next.has(c.id)) next.delete(c.id); else next.add(c.id);
                      setSelectedComps(next);
                    }}
                    className={`rounded-full border px-2.5 py-0.5 text-xs transition-colors ${
                      selected
                        ? "border-primary bg-primary/10 text-primary"
                        : "border-zinc-200 text-muted-foreground hover:border-zinc-300 dark:border-zinc-700"
                    }`}
                  >
                    {c.name}
                  </button>
                );
              })}
              {competencies.length === 0 && (
                <p className="text-xs text-muted-foreground">
                  No competencies yet. Add some in Assessments → Competencies tab.
                </p>
              )}
            </div>
          </div>

          {error && <p className="text-xs text-red-600">{error}</p>}

          <div className="flex justify-end gap-3 pt-2">
            <Button variant="outline" onClick={onClose} disabled={saving}>Cancel</Button>
            <Button onClick={save} disabled={!departmentId || !title.trim() || !prompt.trim() || saving} className="gap-2">
              {saving ? <Loader2 className="size-4 animate-spin" /> : <Save className="size-4" />}
              Add to Bank
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}

```