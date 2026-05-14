---
type: source
source_type: laptop
title: page
slug: page-8
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/assessments/[id]/edit/page.tsx"
original_size: 95788
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/assessments/[id]/edit/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { motion, AnimatePresence } from "framer-motion";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Badge } from "@/components/ui/badge";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  ArrowLeft,
  Plus,
  Trash2,
  Loader2,
  Save,
  Eye as EyeIcon,
  ChevronLeft,
  ChevronRight as ChevronRightIcon,
  Calculator as CalculatorIcon,
  Library,
  Layers,
  HelpCircle,
  Brain,
  Send,
  AlertTriangle,
  ChevronDown,
  CheckCircle,
  Edit,
  X,
} from "lucide-react";

type Tab = "settings" | "sections" | "competencies" | "preview" | "calculator";

interface TemplateData {
  id: string;
  title: string;
  slug: string;
  description: string | null;
  eggHuntEnabled: boolean;
  jobRole: { title: string; department: { name: string; slug: string } };
  versions: Array<{
    id: string;
    versionNumber: number;
    status: string;
    passingScore: number;
    timeLimit: number | null;
    /** JSON-encoded { strongHire, hire, consider } — null until set. */
    recommendationThresholds: string | null;
    sections: Array<{
      id: string;
      title: string;
      slug: string;
      description: string | null;
      introText: string | null;
      iconName: string | null;
      sortOrder: number;
      weight: number;
      questions: Array<{
        id: string;
        title: string;
        prompt: string;
        questionType: string;
        difficulty: string;
        maxPoints: number;
        weight: number;
        scoringStrategy: string;
        correctAnswerKey: string | null;
        explanation: string | null;
        sortOrder: number;
        options: Array<{ id: string; key: string; label: string; value: string; points: number; isCorrect: boolean; sortOrder: number }>;
        competencies: Array<{ competency: { id: string; name: string; slug: string } }>;
      }>;
    }>;
  }>;
}

interface Competency {
  id: string;
  name: string;
  slug: string;
  category: string | null;
}

// Derived row types — used as prop/callback types throughout this page so the
// section/question/option shapes stay in sync with TemplateData.
type Version = TemplateData["versions"][number];
type Section = Version["sections"][number];
type Question = Section["questions"][number];
type AnswerOption = Question["options"][number];
// The junction also carries a `weight`; the API doesn't always fetch it but
// the legacy UI code reads `qc.weight ?? 1.0`, so model it as optional.
type QuestionCompetencyRef = Question["competencies"][number] & { weight?: number };

interface ThresholdRowProps {
  label: string;
  color: string;
  hint: string;
  /** Percent string ("75") — kept as string while the input is being edited. */
  value: string;
  onChange: (v: string) => void;
  disabled?: boolean;
}

interface TabProps {
  template: TemplateData;
  version: Version;
  competencies: Competency[];
  onUpdate: () => void;
  notify: (msg: string) => void;
  disabled?: boolean;
}

interface CompetenciesTabProps {
  competencies: Competency[];
  onUpdate: () => void;
  notify: (msg: string) => void;
}

interface BankPickerModalProps {
  templateId: string;
  sectionId: string;
  sectionSlug: string;
  sectionTitle: string;
  templateDepartmentSlug: string;
  onClose: () => void;
  onSave: (importedCount: number) => void;
}

// Shape returned by GET /api/admin/question-bank (deduped + enriched).
interface BankQuestion {
  id: string;
  title: string;
  prompt: string;
  questionType: string;
  difficulty: string;
  maxPoints: number;
  weight: number;
  scoringStrategy: string;
  correctAnswerKey: string | null;
  explanation: string | null;
  bankSection?: { slug: string; label: string };
  departments: Array<{ name: string; slug: string }>;
  departmentSlugs: string[];
  options: Array<{ key: string; label: string; value: string; points: number; isCorrect: boolean }>;
  competencies: Array<{ id: string; name: string; slug: string; weight: number }>;
  usages: Array<{
    templateId: string;
    templateTitle: string;
    department: string;
    departmentSlug: string;
    sectionTitle: string;
    isLibrary: boolean;
  }>;
}

interface SectionFormProps {
  templateId: string;
  onClose: () => void;
  onSave: () => void;
}

interface EditSectionModalProps extends SectionFormProps {
  section: Section;
}

interface QuestionModalProps {
  templateId: string;
  sectionId: string;
  question: Question | null;
  competencies: Competency[];
  onClose: () => void;
  onSave: () => void;
}

const questionTypes = [
  { value: "single_select", label: "Single Select" },
  { value: "multi_select", label: "Multi Select" },
  { value: "ranking", label: "Ranking" },
  { value: "scenario", label: "Scenario" },
  { value: "situational_judgment", label: "Situational Judgment" },
];

const scoringStrategies = [
  { value: "weighted_options", label: "Weighted Options (points per choice)" },
  { value: "exact", label: "Exact Match (all or nothing)" },
  { value: "partial", label: "Partial Credit" },
  { value: "scenario_based", label: "Scenario-Based" },
];

export default function EditAssessmentPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const [id, setId] = useState("");
  const [template, setTemplate] = useState<TemplateData | null>(null);
  const [competencies, setCompetencies] = useState<Competency[]>([]);
  const [tab, setTab] = useState<Tab>("settings");
  const [loading, setLoading] = useState(true);
  const [isSaving, setIsSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [saveNotice, setSaveNotice] = useState<string | null>(null);

  const loadData = async (templateId: string) => {
    setLoading(true);
    const [t, c] = await Promise.all([
      fetch(`/api/admin/assessments/${templateId}`).then((r) => r.json()),
      fetch("/api/admin/competencies").then((r) => r.json()),
    ]);
    if (t.template) setTemplate(t.template);
    if (c.competencies) setCompetencies(c.competencies);
    setLoading(false);
  };

  useEffect(() => {
    params.then((p) => {
      setId(p.id);
      loadData(p.id);
    });
     
  }, [params]);

  const notify = (msg: string) => {
    setSaveNotice(msg);
    setTimeout(() => setSaveNotice(null), 2500);
  };

  const version = template?.versions[0];
  const isPublished = version?.status === "published";

  const handlePublish = async () => {
    if (!id) return;
    setIsSaving(true);
    setError(null);
    try {
      const res = await fetch(`/api/admin/assessments/${id}/publish`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: isPublished ? "unpublish" : "publish" }),
      });
      const data = await res.json();
      if (!res.ok) { setError(data.error); setIsSaving(false); return; }
      await loadData(id);
      notify(isPublished ? "Unpublished" : "Published successfully");
    } catch { setError("Network error"); }
    setIsSaving(false);
  };

  if (loading || !template || !version) {
    return (
      <div className="flex min-h-[50vh] items-center justify-center">
        <Loader2 className="size-8 animate-spin text-primary" />
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center gap-4">
        <Link
          href="/admin/assessments"
          className="rounded-lg p-1.5 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800"
        >
          <ArrowLeft className="size-5" />
        </Link>
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2">
            <h1 className="truncate text-2xl font-semibold tracking-tight">{template.title}</h1>
            <Badge variant={isPublished ? "default" : "outline"}>{version.status}</Badge>
          </div>
          <p className="text-sm text-muted-foreground">
            {template.jobRole.department.name} &middot; {template.jobRole.title}
          </p>
        </div>
        <Button onClick={handlePublish} disabled={isSaving} className="gap-2">
          {isSaving ? <Loader2 className="size-4 animate-spin" /> : isPublished ? <X className="size-4" /> : <Send className="size-4" />}
          {isPublished ? "Unpublish" : "Publish"}
        </Button>
      </div>

      {saveNotice && (
        <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }} className="rounded-lg bg-emerald-50 p-3 text-sm text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300">
          <CheckCircle className="mr-2 inline-block size-3.5" />
          {saveNotice}
        </motion.div>
      )}

      {error && (
        <div className="rounded-lg bg-red-50 p-3 text-sm text-red-700 dark:bg-red-950 dark:text-red-300">
          <AlertTriangle className="mr-2 inline-block size-3.5" />
          {error}
        </div>
      )}

      {/* Tabs */}
      <div className="flex gap-1 border-b border-zinc-200 dark:border-zinc-800">
        {[
          { id: "settings", label: "Settings", icon: Edit },
          { id: "sections", label: "Sections & Questions", icon: Layers },
          { id: "competencies", label: "Competencies", icon: Brain },
          { id: "preview", label: "Preview", icon: EyeIcon },
          { id: "calculator", label: "Score Calculator", icon: CalculatorIcon },
        ].map((t) => (
          <button
            key={t.id}
            onClick={() => setTab(t.id as Tab)}
            className={`flex items-center gap-2 rounded-t-lg border-b-2 px-4 py-2 text-sm font-medium transition-colors ${
              tab === t.id
                ? "border-primary text-primary"
                : "border-transparent text-muted-foreground hover:text-foreground"
            }`}
          >
            <t.icon className="size-4" />
            {t.label}
          </button>
        ))}
      </div>

      {/* Tab content */}
      {tab === "settings" && (
        <SettingsTab template={template} version={version} onUpdate={() => loadData(id)} notify={notify} disabled={false} />
      )}
      {tab === "sections" && (
        <SectionsTab template={template} version={version} competencies={competencies} onUpdate={() => loadData(id)} notify={notify} disabled={false} />
      )}
      {tab === "competencies" && (
        <CompetenciesTab competencies={competencies} onUpdate={() => loadData(id)} notify={notify} />
      )}
      {tab === "preview" && (
        <PreviewTab version={version} />
      )}
      {tab === "calculator" && (
        <CalculatorTab version={version} />
      )}
    </div>
  );
}

// ─── Settings Tab ─────────────────────────────────────────

const DEFAULT_THRESHOLDS = { strongHire: 0.85, hire: 0.70, consider: 0.55, weakFit: 0.40 };

function parseThresholds(json: string | null) {
  if (!json) return DEFAULT_THRESHOLDS;
  try {
    const p = JSON.parse(json);
    return {
      strongHire: p.strongHire ?? DEFAULT_THRESHOLDS.strongHire,
      hire: p.hire ?? DEFAULT_THRESHOLDS.hire,
      consider: p.consider ?? DEFAULT_THRESHOLDS.consider,
      weakFit: p.weakFit ?? DEFAULT_THRESHOLDS.weakFit,
    };
  } catch { return DEFAULT_THRESHOLDS; }
}

function SettingsTab({
  template, version, onUpdate, notify, disabled,
}: Omit<TabProps, "competencies">) {
  const [title, setTitle] = useState(template.title);
  const [description, setDescription] = useState(template.description ?? "");
  const [passingScore, setPassingScore] = useState(Math.round(version.passingScore * 100).toString());
  const [timeLimit, setTimeLimit] = useState(version.timeLimit?.toString() ?? "");
  const [eggHuntEnabled, setEggHuntEnabled] = useState<boolean>(template.eggHuntEnabled === true);

  const initialThresholds = parseThresholds(version.recommendationThresholds);
  const [strongHire, setStrongHire] = useState(Math.round(initialThresholds.strongHire * 100).toString());
  const [hire, setHire] = useState(Math.round(initialThresholds.hire * 100).toString());
  const [consider, setConsider] = useState(Math.round(initialThresholds.consider * 100).toString());
  const [weakFit, setWeakFit] = useState(Math.round(initialThresholds.weakFit * 100).toString());

  const [saving, setSaving] = useState(false);

  const sh = parseInt(strongHire) || 0;
  const h = parseInt(hire) || 0;
  const c = parseInt(consider) || 0;
  const wf = parseInt(weakFit) || 0;

  const validThresholds = sh > h && h > c && c > wf && wf >= 0 && sh <= 100;

  const sampleScore = 75;
  const previewBand =
    sampleScore >= sh ? { label: "Strong Hire", color: "bg-emerald-100 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300" } :
    sampleScore >= h ? { label: "Hire", color: "bg-green-100 text-green-700 dark:bg-green-950 dark:text-green-300" } :
    sampleScore >= c ? { label: "Consider", color: "bg-amber-100 text-amber-700 dark:bg-amber-950 dark:text-amber-300" } :
    sampleScore >= wf ? { label: "Weak Fit", color: "bg-orange-100 text-orange-700 dark:bg-orange-950 dark:text-orange-300" } :
    { label: "Reject", color: "bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300" };

  const save = async () => {
    if (!validThresholds) return;
    setSaving(true);
    await fetch(`/api/admin/assessments/${template.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title,
        description,
        eggHuntEnabled,
        passingScore: parseInt(passingScore) / 100,
        timeLimit: timeLimit ? parseInt(timeLimit) : null,
        recommendationThresholds: {
          strongHire: sh / 100,
          hire: h / 100,
          consider: c / 100,
          weakFit: wf / 100,
        },
      }),
    });
    setSaving(false);
    notify("Settings saved");
    onUpdate();
  };

  const resetThresholds = () => {
    setStrongHire("85");
    setHire("70");
    setConsider("55");
    setWeakFit("40");
  };

  return (
    <div className="space-y-4">
      <Card>
        <CardHeader>
          <CardTitle>Basic Information</CardTitle>
          <CardDescription>Title, description, and scoring basics</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div>
              <Label>Title</Label>
              <Input value={title} onChange={(e) => setTitle(e.target.value)} disabled={disabled} className="mt-1.5" />
            </div>
            <div>
              <Label>Description</Label>
              <Input value={description} onChange={(e) => setDescription(e.target.value)} disabled={disabled} className="mt-1.5" />
            </div>
            <div className="grid grid-cols-2 gap-4">
              <div>
                <Label>Passing Score (%)</Label>
                <Input type="number" min="0" max="100" value={passingScore} onChange={(e) => setPassingScore(e.target.value)} disabled={disabled} className="mt-1.5" />
              </div>
              <div>
                <Label>Time Limit (minutes)</Label>
                <Input type="number" placeholder="No limit" value={timeLimit} onChange={(e) => setTimeLimit(e.target.value)} disabled={disabled} className="mt-1.5" />
              </div>
            </div>
            <div className="flex items-start gap-3 rounded-lg border border-zinc-200 bg-zinc-50 p-3 dark:border-zinc-800 dark:bg-zinc-900/40">
              <input
                id="egg-hunt-enabled"
                type="checkbox"
                checked={eggHuntEnabled}
                onChange={(e) => setEggHuntEnabled(e.target.checked)}
                disabled={disabled}
                className="mt-0.5 size-4 rounded border-zinc-300 text-primary focus:ring-primary"
              />
              <div className="flex-1">
                <Label htmlFor="egg-hunt-enabled" className="cursor-pointer">
                  Show Egg Hunt CTA on the result page
                </Label>
                <p className="mt-1 text-xs text-muted-foreground">
                  When enabled, candidates who finish this assessment see the optional 4-egg challenge after submitting. Curiosity / resourcefulness signal — best for technical or culturally playful roles.
                </p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <div className="flex items-center justify-between">
            <div>
              <CardTitle>Recommendation Thresholds</CardTitle>
              <CardDescription>
                What score earns each recommendation. Junior roles can use lower bars; senior roles, higher.
              </CardDescription>
            </div>
            <Button variant="outline" onClick={resetThresholds} disabled={disabled} className="text-xs">
              Reset to defaults
            </Button>
          </div>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {/* Visual scale */}
            <div className="pt-7 pb-10">
              <div className="relative h-3 rounded-full bg-zinc-100 shadow-inner dark:bg-zinc-800">
                {/* Bands */}
                <div className="absolute inset-y-0 left-0 rounded-l-full bg-gradient-to-r from-red-500 to-red-400 shadow-sm" style={{ width: `${wf}%` }} />
                <div className="absolute inset-y-0 bg-gradient-to-r from-orange-500 to-orange-400 shadow-sm" style={{ left: `${wf}%`, width: `${Math.max(0, c - wf)}%` }} />
                <div className="absolute inset-y-0 bg-gradient-to-r from-amber-400 to-amber-300 shadow-sm" style={{ left: `${c}%`, width: `${Math.max(0, h - c)}%` }} />
                <div className="absolute inset-y-0 bg-gradient-to-r from-green-500 to-green-400 shadow-sm" style={{ left: `${h}%`, width: `${Math.max(0, sh - h)}%` }} />
                <div className="absolute inset-y-0 right-0 rounded-r-full bg-gradient-to-r from-emerald-500 to-emerald-400 shadow-sm" style={{ left: `${sh}%` }} />

                {/* Threshold tick marks */}
                {[wf, c, h, sh].map((pos, i) => (
                  <div key={i} className="absolute top-1/2 h-5 w-0.5 -translate-x-1/2 -translate-y-1/2 bg-white shadow-sm dark:bg-zinc-200" style={{ left: `${pos}%` }} />
                ))}

                {/* Sample score marker */}
                <div className="absolute top-1/2 -translate-y-1/2" style={{ left: `${sampleScore}%` }}>
                  <div className="-translate-x-1/2">
                    <div className="absolute -top-7 left-1/2 -translate-x-1/2 whitespace-nowrap rounded-md bg-zinc-900 px-2 py-0.5 text-[10px] font-bold text-white shadow-lg dark:bg-white dark:text-zinc-900">
                      75%
                      <div className="absolute left-1/2 top-full -translate-x-1/2 border-4 border-transparent border-t-zinc-900 dark:border-t-white" />
                    </div>
                    <div className="h-7 w-3 rounded-full border-2 border-white bg-zinc-900 shadow-lg dark:border-zinc-900 dark:bg-white" />
                  </div>
                </div>

                {/* Scale labels (0, 25, 50, 75, 100) */}
                <div className="absolute -bottom-6 left-0 right-0 flex justify-between text-[10px] font-medium text-muted-foreground">
                  <span>0%</span>
                  <span>25%</span>
                  <span>50%</span>
                  <span>75%</span>
                  <span>100%</span>
                </div>
              </div>

              {/* Band legend below */}
              <div className="mt-8 flex flex-wrap items-center gap-3 text-[10px]">
                <div className="flex items-center gap-1.5">
                  <span className="h-2 w-2 rounded-full bg-red-500" />
                  <span className="text-muted-foreground">Reject &lt;{wf}%</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <span className="h-2 w-2 rounded-full bg-orange-500" />
                  <span className="text-muted-foreground">Weak Fit {wf}-{c}%</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <span className="h-2 w-2 rounded-full bg-amber-400" />
                  <span className="text-muted-foreground">Consider {c}-{h}%</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <span className="h-2 w-2 rounded-full bg-green-500" />
                  <span className="text-muted-foreground">Hire {h}-{sh}%</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <span className="h-2 w-2 rounded-full bg-emerald-500" />
                  <span className="text-muted-foreground">Strong Hire ≥{sh}%</span>
                </div>
              </div>
            </div>

            <p className={`inline-block rounded-full px-3 py-1 text-xs font-semibold ${previewBand.color}`}>
              A 75% score → {previewBand.label}
            </p>

            <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
              <ThresholdRow
                label="Strong Hire"
                color="bg-emerald-500"
                hint="Top performers — fast-track to interview"
                value={strongHire}
                onChange={setStrongHire}
                disabled={disabled}
              />
              <ThresholdRow
                label="Hire"
                color="bg-green-500"
                hint="Recommended candidates"
                value={hire}
                onChange={setHire}
                disabled={disabled}
              />
              <ThresholdRow
                label="Consider"
                color="bg-amber-500"
                hint="Borderline — review carefully"
                value={consider}
                onChange={setConsider}
                disabled={disabled}
              />
              <ThresholdRow
                label="Weak Fit"
                color="bg-orange-500"
                hint="Below expectations but not rejected"
                value={weakFit}
                onChange={setWeakFit}
                disabled={disabled}
              />
            </div>

            {!validThresholds && (
              <div className="rounded-lg bg-red-50 p-2.5 text-xs text-red-700 dark:bg-red-950 dark:text-red-300">
                <AlertTriangle className="mr-2 inline-block size-3.5" />
                Thresholds must be in descending order: Strong Hire &gt; Hire &gt; Consider &gt; Weak Fit
              </div>
            )}
          </div>
        </CardContent>
      </Card>

      <Button onClick={save} disabled={saving || disabled || !validThresholds} className="gap-2">
        {saving ? <Loader2 className="size-4 animate-spin" /> : <Save className="size-4" />}
        Save All Settings
      </Button>
    </div>
  );
}

function ThresholdRow({ label, color, hint, value, onChange, disabled }: ThresholdRowProps) {
  return (
    <div className="rounded-lg border border-zinc-200 p-3 dark:border-zinc-800">
      <div className="mb-1.5 flex items-center gap-2">
        <span className={`h-2.5 w-2.5 rounded-full ${color}`} />
        <Label className="text-sm font-semibold">{label}</Label>
      </div>
      <p className="mb-2 text-[10px] text-muted-foreground">{hint}</p>
      <div className="flex items-center gap-2">
        <Input type="number" min="0" max="100" value={value} onChange={(e) => onChange(e.target.value)} disabled={disabled} className="w-20" />
        <span className="text-sm text-muted-foreground">% and above</span>
      </div>
    </div>
  );
}

// ─── Sections Tab ─────────────────────────────────────────

function SectionsTab({ template, version, competencies, onUpdate, notify, disabled }: TabProps) {
  const [showNewSection, setShowNewSection] = useState(false);
  const [expanded, setExpanded] = useState<Set<string>>(new Set());
  const [editingSection, setEditingSection] = useState<Section | null>(null);
  const [addingQuestionTo, setAddingQuestionTo] = useState<string | null>(null);
  const [editingQuestion, setEditingQuestion] = useState<{ sectionId: string; section: Section; question: Question | null } | null>(null);
  const [bankPickerSection, setBankPickerSection] = useState<{ id: string; slug: string; title: string } | null>(null);

  const totalWeight = version.sections.reduce((sum: number, s: Section) => sum + s.weight, 0);

  const toggle = (sid: string) => {
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(sid)) next.delete(sid); else next.add(sid);
      return next;
    });
  };

  const deleteSection = async (sid: string) => {
    if (!confirm("Delete this section and all its questions?")) return;
    await fetch(`/api/admin/assessments/${template.id}/sections/${sid}`, { method: "DELETE" });
    notify("Section deleted");
    onUpdate();
  };

  const deleteQuestion = async (sid: string, qid: string) => {
    if (!confirm("Delete this question?")) return;
    await fetch(`/api/admin/assessments/${template.id}/sections/${sid}/questions/${qid}`, { method: "DELETE" });
    notify("Question deleted");
    onUpdate();
  };

  return (
    <div className="space-y-4">
      {/* Section weight warning */}
      {version.sections.length > 0 && Math.abs(totalWeight - 1.0) > 0.01 && (
        <div className="rounded-lg bg-amber-50 p-3 text-xs text-amber-800 dark:bg-amber-950 dark:text-amber-200">
          <AlertTriangle className="mr-2 inline-block size-3.5" />
          Section weights sum to {totalWeight.toFixed(2)}. They should sum to 1.0 for accurate scoring.
        </div>
      )}

      {version.sections.map((section: Section) => (
        <Card key={section.id}>
          <div className="px-6 py-4">
            <div className="flex items-start justify-between">
              <button onClick={() => toggle(section.id)} className="flex-1 text-left">
                <div className="flex items-center gap-2">
                  <ChevronDown className={`size-4 text-muted-foreground transition-transform ${expanded.has(section.id) ? "rotate-180" : ""}`} />
                  <h3 className="text-base font-semibold">{section.title}</h3>
                  <Badge variant="secondary">Weight: {section.weight}</Badge>
                  <Badge variant="outline">{section.questions.length} questions</Badge>
                </div>
                {section.description && (
                  <p className="mt-1 ml-6 text-xs text-muted-foreground">{section.description}</p>
                )}
              </button>
              <div className="flex gap-1">
                <button onClick={() => setEditingSection(section)} disabled={disabled} className="rounded-md p-1.5 text-zinc-400 hover:bg-zinc-100 hover:text-zinc-600 disabled:opacity-30 dark:hover:bg-zinc-800">
                  <Edit className="size-4" />
                </button>
                <button onClick={() => deleteSection(section.id)} disabled={disabled} className="rounded-md p-1.5 text-zinc-400 hover:bg-red-50 hover:text-red-500 disabled:opacity-30 dark:hover:bg-red-950">
                  <Trash2 className="size-4" />
                </button>
              </div>
            </div>
          </div>

          <AnimatePresence>
            {expanded.has(section.id) && (
              <motion.div initial={{ height: 0, opacity: 0 }} animate={{ height: "auto", opacity: 1 }} exit={{ height: 0, opacity: 0 }} className="overflow-hidden">
                <div className="border-t border-zinc-100 px-6 py-4 dark:border-zinc-800">
                  <div className="mb-3 flex items-center justify-between">
                    <p className="text-xs font-medium text-muted-foreground">Questions</p>
                    <div className="flex gap-2">
                      <Button variant="outline" onClick={() => setBankPickerSection({ id: section.id, slug: section.slug, title: section.title })} disabled={disabled} className="gap-1.5 text-xs">
                        <Library className="size-3" /> Add from Bank
                      </Button>
                      <Button variant="outline" onClick={() => setAddingQuestionTo(section.id)} disabled={disabled} className="gap-1.5 text-xs">
                        <Plus className="size-3" /> Add Question
                      </Button>
                    </div>
                  </div>

                  {section.questions.length === 0 ? (
                    <p className="py-4 text-center text-xs text-muted-foreground">No questions yet.</p>
                  ) : (
                    <div className="space-y-2">
                      {section.questions.map((q: Question, i: number) => (
                        <div key={q.id} className="flex items-center justify-between rounded-lg border border-zinc-100 p-3 dark:border-zinc-800">
                          <div className="min-w-0 flex-1">
                            <div className="flex items-center gap-2">
                              <span className="text-[10px] font-bold text-muted-foreground">#{i + 1}</span>
                              <p className="truncate text-sm font-medium">{q.title}</p>
                              <Badge variant="outline">{q.difficulty}</Badge>
                              <Badge variant="secondary">{q.maxPoints} pts</Badge>
                            </div>
                            <p className="mt-0.5 truncate text-xs text-muted-foreground">{q.prompt}</p>
                          </div>
                          <div className="flex gap-1">
                            <button onClick={() => setEditingQuestion({ sectionId: section.id, section, question: q })} disabled={disabled} className="rounded-md p-1.5 text-zinc-400 hover:text-zinc-600 disabled:opacity-30">
                              <Edit className="size-3.5" />
                            </button>
                            <button onClick={() => deleteQuestion(section.id, q.id)} disabled={disabled} className="rounded-md p-1.5 text-zinc-400 hover:text-red-500 disabled:opacity-30">
                              <Trash2 className="size-3.5" />
                            </button>
                          </div>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </Card>
      ))}

      {/* Add section button */}
      {!showNewSection ? (
        <Button variant="outline" onClick={() => setShowNewSection(true)} disabled={disabled} className="w-full gap-2">
          <Plus className="size-4" /> Add Section
        </Button>
      ) : (
        <SectionForm
          templateId={template.id}
          onClose={() => setShowNewSection(false)}
          onSave={() => { setShowNewSection(false); onUpdate(); notify("Section added"); }}
        />
      )}

      {/* Edit section modal */}
      {editingSection && (
        <EditSectionModal
          templateId={template.id}
          section={editingSection}
          onClose={() => setEditingSection(null)}
          onSave={() => { setEditingSection(null); onUpdate(); notify("Section updated"); }}
        />
      )}

      {/* Add question modal */}
      {addingQuestionTo && (
        <QuestionModal
          templateId={template.id}
          sectionId={addingQuestionTo}
          question={null}
          competencies={competencies}
          onClose={() => setAddingQuestionTo(null)}
          onSave={() => { setAddingQuestionTo(null); onUpdate(); notify("Question added"); }}
        />
      )}

      {/* Edit question modal */}
      {editingQuestion && (
        <QuestionModal
          templateId={template.id}
          sectionId={editingQuestion.section.id}
          question={editingQuestion.question}
          competencies={competencies}
          onClose={() => setEditingQuestion(null)}
          onSave={() => { setEditingQuestion(null); onUpdate(); notify("Question updated"); }}
        />
      )}

      {/* Question Bank picker */}
      {bankPickerSection && (
        <BankPickerModal
          templateId={template.id}
          sectionId={bankPickerSection.id}
          sectionSlug={bankPickerSection.slug}
          sectionTitle={bankPickerSection.title}
          templateDepartmentSlug={template.jobRole.department.slug}
          onClose={() => setBankPickerSection(null)}
          onSave={(count: number) => { setBankPickerSection(null); onUpdate(); notify(`Added ${count} question${count !== 1 ? "s" : ""} from bank`); }}
        />
      )}
    </div>
  );
}

// ─── Bank Picker Modal ────────────────────────────────────

const BANK_SECTION_OPTIONS = [
  { slug: "cultural-fit", label: "Cultural Fit" },
  { slug: "ai-awareness", label: "AI Awareness" },
  { slug: "department-specific", label: "Department-Specific" },
  { slug: "general", label: "General" },
];

function inferBankSectionFromSlug(slug: string, title: string): string {
  const s = slug.toLowerCase();
  const t = title.toLowerCase();
  if (s.includes("cultur") || t.includes("cultur")) return "cultural-fit";
  if (s.includes("ai-aware") || t.includes("ai aware") || t.includes("ai readiness")) return "ai-awareness";
  if (s === "library" || s.startsWith("library-")) return "general";
  return "department-specific";
}

function BankPickerModal({ templateId, sectionId, sectionSlug, sectionTitle, templateDepartmentSlug, onClose, onSave }: BankPickerModalProps) {
  const [questions, setQuestions] = useState<BankQuestion[]>([]);
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [importing, setImporting] = useState(false);
  const [deptFilter, setDeptFilter] = useState<string>(templateDepartmentSlug ?? "all");
  const [sectionFilter, setSectionFilter] = useState<string>(
    sectionSlug ? inferBankSectionFromSlug(sectionSlug, sectionTitle ?? "") : "all"
  );

  useEffect(() => {
    fetch(`/api/admin/question-bank?excludeTemplateId=${templateId}`)
      .then((r) => r.json())
      .then((d) => {
        setQuestions(d.questions ?? []);
        setLoading(false);
      });
  }, [templateId]);

  const availableDepartments = useMemo(() => {
    const seen = new Map<string, string>();
    for (const q of questions) {
      for (const d of q.departments ?? []) {
        if (!seen.has(d.slug)) seen.set(d.slug, d.name);
      }
    }
    return [...seen.entries()].map(([slug, name]) => ({ slug, name }));
  }, [questions]);

  const filtered = questions.filter((q) => {
    if (deptFilter !== "all" && !(q.departmentSlugs ?? []).includes(deptFilter)) return false;
    if (sectionFilter !== "all" && q.bankSection?.slug !== sectionFilter) return false;
    if (search.trim() && !`${q.title} ${q.prompt}`.toLowerCase().includes(search.toLowerCase())) return false;
    return true;
  });

  const toggle = (id: string) => {
    setSelected((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id); else next.add(id);
      return next;
    });
  };

  const importSelected = async () => {
    setImporting(true);
    const picks = questions.filter((q) => selected.has(q.id));
    for (const q of picks) {
      await fetch(`/api/admin/assessments/${templateId}/sections/${sectionId}/questions`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: q.title,
          prompt: q.prompt,
          questionType: q.questionType,
          difficulty: q.difficulty,
          maxPoints: q.maxPoints,
          weight: q.weight,
          scoringStrategy: q.scoringStrategy,
          correctAnswerKey: q.correctAnswerKey,
          explanation: q.explanation,
          options: q.options,
          competencies: q.competencies.map((c) => ({ competencyId: c.id, weight: c.weight ?? 1.0 })),
        }),
      });
    }
    setImporting(false);
    onSave(picks.length);
  };

  return (
    <Modal title="Add Questions from Bank" onClose={onClose} wide>
      <div className="space-y-3">
        <div className="grid grid-cols-1 gap-2 sm:grid-cols-3">
          <Input
            placeholder="Search questions..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
          <Select value={deptFilter} onValueChange={(v) => setDeptFilter(v ?? "all")}>
            <SelectTrigger className="w-full"><SelectValue placeholder="Department" /></SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All Departments</SelectItem>
              {availableDepartments.map((d) => (
                <SelectItem key={d.slug} value={d.slug}>{d.name}</SelectItem>
              ))}
            </SelectContent>
          </Select>
          <Select value={sectionFilter} onValueChange={(v) => setSectionFilter(v ?? "all")}>
            <SelectTrigger className="w-full"><SelectValue placeholder="Bank Section" /></SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All Sections</SelectItem>
              {BANK_SECTION_OPTIONS.map((s) => (
                <SelectItem key={s.slug} value={s.slug}>{s.label}</SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>
        <p className="text-[11px] text-muted-foreground">
          Showing {filtered.length} of {questions.length} bank questions.
        </p>

        {loading ? (
          <div className="flex justify-center py-12">
            <Loader2 className="size-6 animate-spin text-muted-foreground" />
          </div>
        ) : filtered.length === 0 ? (
          <div className="py-12 text-center text-sm text-muted-foreground">
            {questions.length === 0 ? "No questions in the bank yet." : "No questions match your search."}
          </div>
        ) : (
          <div className="max-h-[50vh] space-y-2 overflow-y-auto pr-1">
            {filtered.map((q) => {
              const isSelected = selected.has(q.id);
              return (
                <button
                  key={q.id}
                  onClick={() => toggle(q.id)}
                  className={`flex w-full items-start gap-3 rounded-lg border-2 p-3 text-left transition-all ${
                    isSelected ? "border-primary bg-primary/5" : "border-zinc-200 hover:border-zinc-300 dark:border-zinc-800"
                  }`}
                >
                  <span className={`mt-0.5 flex h-4 w-4 flex-shrink-0 items-center justify-center rounded-md border-2 ${
                    isSelected ? "border-primary bg-primary" : "border-zinc-300 dark:border-zinc-600"
                  }`}>
                    {isSelected && <span className="text-[8px] text-white">✓</span>}
                  </span>
                  <div className="min-w-0 flex-1">
                    <div className="flex flex-wrap items-center gap-2">
                      <p className="text-sm font-medium">{q.title}</p>
                      <Badge variant="outline" className="text-[10px]">{q.difficulty}</Badge>
                      <Badge variant="secondary" className="text-[10px]">{q.maxPoints} pts</Badge>
                      <Badge variant="outline" className="text-[10px]">{q.questionType.replace(/_/g, " ")}</Badge>
                    </div>
                    <p className="mt-1 line-clamp-2 text-xs text-muted-foreground">{q.prompt}</p>
                    {q.competencies.length > 0 && (
                      <div className="mt-1.5 flex flex-wrap gap-1">
                        {q.competencies.slice(0, 4).map((c) => (
                          <span key={c.id} className="rounded-full bg-blue-50 px-1.5 py-0.5 text-[9px] text-blue-700 dark:bg-blue-950 dark:text-blue-300">
                            {c.name}
                          </span>
                        ))}
                      </div>
                    )}
                    {q.usages.length > 0 && (
                      <p className="mt-1 text-[9px] text-muted-foreground">
                        From: {q.usages[0].templateTitle}{q.usages.length > 1 ? ` (+${q.usages.length - 1} more)` : ""}
                      </p>
                    )}
                  </div>
                </button>
              );
            })}
          </div>
        )}

        <div className="flex items-center justify-between pt-2">
          <p className="text-xs text-muted-foreground">{selected.size} selected</p>
          <div className="flex gap-3">
            <Button variant="outline" onClick={onClose}>Cancel</Button>
            <Button onClick={importSelected} disabled={selected.size === 0 || importing} className="gap-2">
              {importing ? <Loader2 className="size-4 animate-spin" /> : <Library className="size-4" />}
              Add {selected.size} Question{selected.size !== 1 ? "s" : ""}
            </Button>
          </div>
        </div>
      </div>
    </Modal>
  );
}

// ─── Section Form (inline) ────────────────────────────────

function SectionForm({ templateId, onClose, onSave }: SectionFormProps) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [introText, setIntroText] = useState("");
  const [weight, setWeight] = useState("0.33");
  const [saving, setSaving] = useState(false);

  const save = async () => {
    if (!title.trim()) return;
    setSaving(true);
    await fetch(`/api/admin/assessments/${templateId}/sections`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, description, introText, weight: parseFloat(weight) }),
    });
    setSaving(false);
    onSave();
  };

  return (
    <Card>
      <CardHeader>
        <CardTitle>New Section</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-3">
          <div>
            <Label>Title</Label>
            <Input placeholder="e.g. Cultural Fit" value={title} onChange={(e) => setTitle(e.target.value)} className="mt-1.5" />
          </div>
          <div>
            <Label>Short Description</Label>
            <Input placeholder="What this section assesses" value={description} onChange={(e) => setDescription(e.target.value)} className="mt-1.5" />
          </div>
          <div>
            <Label>Intro Text (shown before section starts)</Label>
            <textarea
              value={introText}
              onChange={(e) => setIntroText(e.target.value)}
              placeholder="Welcome message for candidates entering this section..."
              className="mt-1.5 min-h-[80px] w-full rounded-lg border border-input bg-transparent p-3 text-sm outline-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50"
            />
          </div>
          <div>
            <Label>Weight (0 to 1, contribution to final score)</Label>
            <Input type="number" step="0.01" min="0" max="1" value={weight} onChange={(e) => setWeight(e.target.value)} className="mt-1.5" />
          </div>
          <div className="flex gap-3">
            <Button onClick={save} disabled={!title.trim() || saving} className="gap-2">
              {saving ? <Loader2 className="size-4 animate-spin" /> : <Save className="size-4" />}
              Add Section
            </Button>
            <Button variant="outline" onClick={onClose}>Cancel</Button>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}

// ─── Edit Section Modal ───────────────────────────────────

function EditSectionModal({ templateId, section, onClose, onSave }: EditSectionModalProps) {
  const [title, setTitle] = useState(section.title);
  const [description, setDescription] = useState(section.description ?? "");
  const [introText, setIntroText] = useState(section.introText ?? "");
  const [weight, setWeight] = useState(section.weight.toString());
  const [saving, setSaving] = useState(false);

  const save = async () => {
    setSaving(true);
    await fetch(`/api/admin/assessments/${templateId}/sections/${section.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, description, introText, weight: parseFloat(weight) }),
    });
    setSaving(false);
    onSave();
  };

  return (
    <Modal title="Edit Section" onClose={onClose}>
      <div className="space-y-3">
        <div><Label>Title</Label><Input value={title} onChange={(e) => setTitle(e.target.value)} className="mt-1.5" /></div>
        <div><Label>Description</Label><Input value={description} onChange={(e) => setDescription(e.target.value)} className="mt-1.5" /></div>
        <div>
          <Label>Intro Text</Label>
          <textarea value={introText} onChange={(e) => setIntroText(e.target.value)} className="mt-1.5 min-h-[80px] w-full rounded-lg border border-input bg-transparent p-3 text-sm outline-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50" />
        </div>
        <div><Label>Weight</Label><Input type="number" step="0.01" value={weight} onChange={(e) => setWeight(e.target.value)} className="mt-1.5" /></div>
        <div className="flex gap-3">
          <Button onClick={save} disabled={saving} className="gap-2">
            {saving ? <Loader2 className="size-4 animate-spin" /> : <Save className="size-4" />}
            Save
          </Button>
          <Button variant="outline" onClick={onClose}>Cancel</Button>
        </div>
      </div>
    </Modal>
  );
}

// ─── Question Modal (create + edit) ───────────────────────

function QuestionModal({ templateId, sectionId, question, competencies, onClose, onSave }: QuestionModalProps) {
  const isEdit = !!question;
  const [title, setTitle] = useState(question?.title ?? "");
  const [prompt, setPrompt] = useState(question?.prompt ?? "");
  const [questionType, setQuestionType] = useState(question?.questionType ?? "single_select");
  const [difficulty, setDifficulty] = useState(question?.difficulty ?? "medium");
  const [maxPoints, setMaxPoints] = useState(question?.maxPoints?.toString() ?? "10");
  const [weight, setWeight] = useState(question?.weight?.toString() ?? "1.0");
  const [scoringStrategy, setScoringStrategy] = useState(question?.scoringStrategy ?? "weighted_options");
  const [explanation, setExplanation] = useState(question?.explanation ?? "");
  const [options, setOptions] = useState<Array<{ key: string; label: string; points: number; isCorrect: boolean }>>(
    question?.options?.map((o) => ({ key: o.key, label: o.label, points: o.points, isCorrect: o.isCorrect })) ??
    [
      { key: "a", label: "", points: 0, isCorrect: false },
      { key: "b", label: "", points: 0, isCorrect: false },
    ]
  );
  const [selectedCompetencies, setSelectedCompetencies] = useState<Array<{ competencyId: string; weight: number }>>(
    question?.competencies?.map((qc) => ({ competencyId: qc.competency.id, weight: 1.0 })) ?? []
  );
  const [saving, setSaving] = useState(false);

  const addOption = () => {
    const key = String.fromCharCode(97 + options.length); // a, b, c, d...
    setOptions([...options, { key, label: "", points: 0, isCorrect: false }]);
  };

  const removeOption = (i: number) => setOptions(options.filter((_, idx) => idx !== i));

  const save = async () => {
    if (!title.trim() || !prompt.trim()) return;
    setSaving(true);

    const body = {
      title,
      prompt,
      questionType,
      difficulty,
      maxPoints: parseFloat(maxPoints),
      weight: parseFloat(weight),
      scoringStrategy,
      explanation,
      options,
      competencies: selectedCompetencies,
    };

    const url = isEdit
      ? `/api/admin/assessments/${templateId}/sections/${sectionId}/questions/${question.id}`
      : `/api/admin/assessments/${templateId}/sections/${sectionId}/questions`;

    await fetch(url, {
      method: isEdit ? "PATCH" : "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    setSaving(false);
    onSave();
  };

  const toggleCompetency = (competencyId: string) => {
    setSelectedCompetencies((prev) => {
      if (prev.some((c) => c.competencyId === competencyId)) {
        return prev.filter((c) => c.competencyId !== competencyId);
      }
      return [...prev, { competencyId, weight: 1.0 }];
    });
  };

  return (
    <Modal title={isEdit ? "Edit Question" : "New Question"} onClose={onClose} wide>
      <div className="space-y-4">
        <div>
          <Label>Question Title</Label>
          <Input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Short internal title" className="mt-1.5" />
        </div>
        <div>
          <Label>Question Prompt (shown to candidate)</Label>
          <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} placeholder="The full question text..." className="mt-1.5 min-h-[80px] w-full rounded-lg border border-input bg-transparent p-3 text-sm outline-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50" />
        </div>

        <div className="grid grid-cols-2 gap-3">
          <div>
            <Label>Question Type</Label>
            <div className="mt-1.5">
              <Select value={questionType} onValueChange={(v) => setQuestionType(v ?? "single_select")}>
                <SelectTrigger className="w-full"><SelectValue /></SelectTrigger>
                <SelectContent>
                  {questionTypes.map((t) => <SelectItem key={t.value} value={t.value}>{t.label}</SelectItem>)}
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
            <Label>Weight</Label>
            <Input type="number" step="0.1" value={weight} onChange={(e) => setWeight(e.target.value)} className="mt-1.5" />
          </div>
        </div>

        <div>
          <Label>Scoring Strategy</Label>
          <div className="mt-1.5">
            <Select value={scoringStrategy} onValueChange={(v) => setScoringStrategy(v ?? "weighted_options")}>
              <SelectTrigger className="w-full"><SelectValue /></SelectTrigger>
              <SelectContent>
                {scoringStrategies.map((s) => <SelectItem key={s.value} value={s.value}>{s.label}</SelectItem>)}
              </SelectContent>
            </Select>
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
          <Label>Competencies (what this question measures)</Label>
          <div className="mt-2 flex flex-wrap gap-1.5">
            {competencies.map((c: Competency) => {
              const selected = selectedCompetencies.some((sc) => sc.competencyId === c.id);
              return (
                <button
                  key={c.id}
                  onClick={() => toggleCompetency(c.id)}
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
              <p className="text-xs text-muted-foreground">No competencies yet. Add some in the Competencies tab.</p>
            )}
          </div>
        </div>

        <div>
          <Label>Explanation (optional, shown after completion)</Label>
          <Input value={explanation} onChange={(e) => setExplanation(e.target.value)} className="mt-1.5" />
        </div>

        <div className="flex gap-3">
          <Button onClick={save} disabled={!title.trim() || !prompt.trim() || saving} className="gap-2">
            {saving ? <Loader2 className="size-4 animate-spin" /> : <Save className="size-4" />}
            {isEdit ? "Save Question" : "Add Question"}
          </Button>
          <Button variant="outline" onClick={onClose}>Cancel</Button>
        </div>
      </div>
    </Modal>
  );
}

// ─── Competencies Tab ─────────────────────────────────────

function CompetenciesTab({ competencies, onUpdate, notify }: CompetenciesTabProps) {
  const [name, setName] = useState("");
  const [category, setCategory] = useState("");
  const [description, setDescription] = useState("");
  const [saving, setSaving] = useState(false);

  const add = async () => {
    if (!name.trim()) return;
    setSaving(true);
    await fetch("/api/admin/competencies", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, category, description }),
    });
    setName("");
    setCategory("");
    setDescription("");
    setSaving(false);
    onUpdate();
    notify("Competency added");
  };

  const del = async (id: string) => {
    if (!confirm("Delete this competency?")) return;
    const res = await fetch(`/api/admin/competencies/${id}`, { method: "DELETE" });
    const data = await res.json();
    if (!res.ok) { alert(data.error); return; }
    notify("Competency deleted");
    onUpdate();
  };

  const grouped = new Map<string, Competency[]>();
  for (const c of competencies) {
    const cat = c.category ?? "Other";
    if (!grouped.has(cat)) grouped.set(cat, []);
    grouped.get(cat)!.push(c);
  }

  return (
    <div className="space-y-4">
      <Card>
        <CardHeader>
          <CardTitle>Add Competency</CardTitle>
          <CardDescription>
            Competencies are skills or traits that questions measure (e.g. Communication, Problem Solving).
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
            <Input placeholder="Name (e.g. Communication)" value={name} onChange={(e) => setName(e.target.value)} />
            <Input placeholder="Category (e.g. Soft Skills)" value={category} onChange={(e) => setCategory(e.target.value)} />
            <Input placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
          </div>
          <Button onClick={add} disabled={!name.trim() || saving} className="mt-3 gap-2">
            {saving ? <Loader2 className="size-4 animate-spin" /> : <Plus className="size-4" />}
            Add Competency
          </Button>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>All Competencies ({competencies.length})</CardTitle>
        </CardHeader>
        <CardContent>
          {competencies.length === 0 ? (
            <p className="text-sm text-muted-foreground">No competencies yet.</p>
          ) : (
            <div className="space-y-4">
              {Array.from(grouped.entries()).map(([cat, items]) => (
                <div key={cat}>
                  <p className="mb-2 text-xs font-semibold uppercase tracking-wider text-muted-foreground">{cat}</p>
                  <div className="flex flex-wrap gap-2">
                    {items.map((c) => (
                      <div key={c.id} className="inline-flex items-center gap-1 rounded-full border border-zinc-200 px-3 py-1 text-xs dark:border-zinc-700">
                        {c.name}
                        <button onClick={() => del(c.id)} className="ml-1 text-zinc-400 hover:text-red-500">
                          <X className="size-3" />
                        </button>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}

// ─── Modal wrapper ─────────────────────────────────────────

// ─── Preview Tab ──────────────────────────────────────────

function PreviewTab({ version }: { version: Version }) {
  const [sectionIndex, setSectionIndex] = useState(0);
  const [questionIndex, setQuestionIndex] = useState(0);
  const [selectedKey, setSelectedKey] = useState<string | null>(null);
  const [selectedKeys, setSelectedKeys] = useState<string[]>([]);
  const [, setRankingOrder] = useState<string[]>([]);

  if (version.sections.length === 0) {
    return (
      <Card>
        <CardContent className="flex flex-col items-center py-12">
          <EyeIcon className="size-10 text-muted-foreground" />
          <p className="mt-4 text-sm text-muted-foreground">No sections yet. Add a section to preview.</p>
        </CardContent>
      </Card>
    );
  }

  const section = version.sections[sectionIndex];
  const question = section?.questions?.[questionIndex];
  const totalQuestions = version.sections.reduce((sum: number, s: Section) => sum + s.questions.length, 0);
  const currentNumber =
    version.sections
      .slice(0, sectionIndex)
      .reduce((sum: number, s: Section) => sum + s.questions.length, 0) + questionIndex + 1;

  const goNext = () => {
    if (!section) return;
    if (questionIndex < section.questions.length - 1) {
      setQuestionIndex(questionIndex + 1);
    } else if (sectionIndex < version.sections.length - 1) {
      setSectionIndex(sectionIndex + 1);
      setQuestionIndex(0);
    }
    resetSelections();
  };

  const goPrev = () => {
    if (questionIndex > 0) {
      setQuestionIndex(questionIndex - 1);
    } else if (sectionIndex > 0) {
      const prevSection = version.sections[sectionIndex - 1];
      setSectionIndex(sectionIndex - 1);
      setQuestionIndex(prevSection.questions.length - 1);
    }
    resetSelections();
  };

  const resetSelections = () => {
    setSelectedKey(null);
    setSelectedKeys([]);
    setRankingOrder([]);
  };

  const difficultyColors: Record<string, string> = {
    easy: "bg-green-100 text-green-700 dark:bg-green-950 dark:text-green-300",
    medium: "bg-amber-100 text-amber-700 dark:bg-amber-950 dark:text-amber-300",
    hard: "bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300",
  };

  return (
    <div className="space-y-4">
      {/* Section selector and navigation */}
      <Card>
        <CardContent className="pt-3">
          <div className="flex items-center justify-between gap-3">
            <div className="flex items-center gap-2">
              <Label className="text-xs">Section:</Label>
              <Select
                value={String(sectionIndex)}
                onValueChange={(v) => {
                  setSectionIndex(parseInt(v ?? "0"));
                  setQuestionIndex(0);
                  resetSelections();
                }}
              >
                <SelectTrigger className="min-w-[200px]">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  {version.sections.map((s: Section, i: number) => (
                    <SelectItem key={s.id} value={String(i)}>
                      {s.title} ({s.questions.length} questions)
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            <div className="text-xs text-muted-foreground">
              Question {currentNumber} of {totalQuestions}
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Candidate-style preview */}
      <Card className="overflow-hidden">
        <div className="border-b border-zinc-200 bg-gradient-to-b from-zinc-50 to-white px-6 py-3 dark:border-zinc-800 dark:from-zinc-800/50 dark:to-zinc-900">
          <div className="flex items-center gap-2">
            <Badge variant="outline" className="text-[10px]">CANDIDATE PREVIEW</Badge>
            <span className="text-xs text-muted-foreground">{section.title}</span>
          </div>
        </div>

        <div className="px-6 py-8">
          {!question ? (
            <div className="flex flex-col items-center py-12">
              <HelpCircle className="size-10 text-muted-foreground" />
              <p className="mt-4 text-sm text-muted-foreground">No questions in this section yet.</p>
            </div>
          ) : (
            <div className="mx-auto max-w-2xl">
              {/* Question header */}
              <div className="mb-6">
                <div className="mb-3 flex items-center gap-2">
                  <span className="text-xs font-medium text-muted-foreground">
                    Question {questionIndex + 1} of {section.questions.length}
                  </span>
                  <span className={`rounded-full px-2 py-0.5 text-[10px] font-medium ${difficultyColors[question.difficulty] ?? ""}`}>
                    {question.difficulty}
                  </span>
                  <span className="rounded-full bg-zinc-100 px-2 py-0.5 text-[10px] font-medium dark:bg-zinc-800">
                    {question.maxPoints} pts
                  </span>
                </div>
                <h3 className="text-xl font-semibold leading-snug tracking-tight">
                  {question.title}
                </h3>
                <p className="mt-2 text-sm leading-relaxed text-muted-foreground whitespace-pre-line">
                  {question.prompt}
                </p>
              </div>

              {/* Question body — render based on type */}
              <div className="mb-6">
                {(question.questionType === "single_select" ||
                  question.questionType === "scenario" ||
                  question.questionType === "situational_judgment") && (
                  <div className="space-y-3">
                    {question.options.map((opt: AnswerOption) => {
                      const isSelected = selectedKey === opt.key;
                      return (
                        <button
                          key={opt.id}
                          onClick={() => setSelectedKey(opt.key)}
                          className={`group flex w-full items-start gap-3 rounded-xl border-2 p-4 text-left transition-all ${
                            isSelected
                              ? "border-primary bg-primary/5"
                              : "border-zinc-200 hover:border-zinc-300 dark:border-zinc-800"
                          }`}
                        >
                          <span className={`mt-0.5 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full border-2 ${
                            isSelected ? "border-primary bg-primary" : "border-zinc-300 dark:border-zinc-600"
                          }`}>
                            {isSelected && <div className="h-2 w-2 rounded-full bg-white" />}
                          </span>
                          <span className={`text-sm leading-relaxed ${isSelected ? "font-medium" : "text-zinc-600 dark:text-zinc-400"}`}>
                            {opt.label}
                          </span>
                          {/* Admin-only hints */}
                          <div className="ml-auto flex flex-shrink-0 items-center gap-2">
                            <span className="text-[10px] font-medium text-muted-foreground">
                              {opt.points} pts
                            </span>
                            {opt.isCorrect && (
                              <span className="rounded-full bg-emerald-100 px-1.5 py-0.5 text-[9px] font-bold text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300">
                                CORRECT
                              </span>
                            )}
                          </div>
                        </button>
                      );
                    })}
                  </div>
                )}

                {question.questionType === "multi_select" && (
                  <div className="space-y-3">
                    <p className="text-xs text-muted-foreground">Select all that apply</p>
                    {question.options.map((opt: AnswerOption) => {
                      const isSelected = selectedKeys.includes(opt.key);
                      return (
                        <button
                          key={opt.id}
                          onClick={() => setSelectedKeys((prev) => prev.includes(opt.key) ? prev.filter((k) => k !== opt.key) : [...prev, opt.key])}
                          className={`group flex w-full items-start gap-3 rounded-xl border-2 p-4 text-left transition-all ${
                            isSelected ? "border-primary bg-primary/5" : "border-zinc-200 hover:border-zinc-300 dark:border-zinc-800"
                          }`}
                        >
                          <span className={`mt-0.5 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-md border-2 ${
                            isSelected ? "border-primary bg-primary" : "border-zinc-300 dark:border-zinc-600"
                          }`}>
                            {isSelected && <div className="text-white">✓</div>}
                          </span>
                          <span className={`text-sm leading-relaxed ${isSelected ? "font-medium" : "text-zinc-600 dark:text-zinc-400"}`}>
                            {opt.label}
                          </span>
                          <div className="ml-auto flex flex-shrink-0 items-center gap-2">
                            <span className="text-[10px] font-medium text-muted-foreground">{opt.points} pts</span>
                            {opt.isCorrect && (
                              <span className="rounded-full bg-emerald-100 px-1.5 py-0.5 text-[9px] font-bold text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300">
                                CORRECT
                              </span>
                            )}
                          </div>
                        </button>
                      );
                    })}
                  </div>
                )}

                {question.questionType === "ranking" && (
                  <div>
                    <p className="mb-3 text-xs text-muted-foreground">Drag to rank from most to least important</p>
                    <div className="space-y-2">
                      {question.options.map((opt: AnswerOption, i: number) => (
                        <div key={opt.id} className="flex items-center gap-3 rounded-xl border-2 border-zinc-200 bg-white p-3 dark:border-zinc-800 dark:bg-zinc-950">
                          <span className="flex h-7 w-7 flex-shrink-0 items-center justify-center rounded-lg bg-primary/10 text-xs font-bold text-primary">
                            {i + 1}
                          </span>
                          <span className="flex-1 text-sm">{opt.label}</span>
                          <span className="text-[10px] font-medium text-muted-foreground">{opt.points} pts</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              {/* Competencies + explanation (admin info) */}
              {(question.competencies?.length > 0 || question.explanation) && (
                <div className="mt-6 rounded-xl border border-dashed border-zinc-300 p-4 dark:border-zinc-700">
                  <p className="mb-2 text-[10px] font-bold uppercase tracking-wider text-muted-foreground">
                    Admin info (not shown to candidates)
                  </p>
                  {question.competencies?.length > 0 && (
                    <div className="mb-2">
                      <p className="text-[10px] text-muted-foreground">Competencies measured:</p>
                      <div className="mt-1 flex flex-wrap gap-1">
                        {question.competencies.map((qc: QuestionCompetencyRef) => (
                          <Badge key={qc.competency.id} variant="secondary" className="text-[10px]">
                            {qc.competency.name}
                          </Badge>
                        ))}
                      </div>
                    </div>
                  )}
                  {question.explanation && (
                    <div>
                      <p className="text-[10px] text-muted-foreground">Explanation:</p>
                      <p className="text-xs italic">{question.explanation}</p>
                    </div>
                  )}
                  <p className="mt-2 text-[10px] text-muted-foreground">
                    Scoring: {question.scoringStrategy} &middot; Weight: {question.weight}
                  </p>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Footer navigation */}
        {question && (
          <div className="flex items-center justify-between border-t border-zinc-100 px-6 py-3 dark:border-zinc-800">
            <Button
              variant="outline"
              onClick={goPrev}
              disabled={sectionIndex === 0 && questionIndex === 0}
              className="gap-1.5 text-xs"
            >
              <ChevronLeft className="size-3" /> Previous
            </Button>
            <Button
              onClick={goNext}
              disabled={sectionIndex === version.sections.length - 1 && questionIndex === section.questions.length - 1}
              className="gap-1.5 text-xs"
            >
              Next <ChevronRightIcon className="size-3" />
            </Button>
          </div>
        )}
      </Card>
    </div>
  );
}

// ─── Calculator Tab ───────────────────────────────────────

function CalculatorTab({ version }: { version: Version }) {
  // Map of questionId → { selectedKeys: string[] } (for single + multi select)
  const [answers, setAnswers] = useState<Record<string, string[]>>({});

  const totalQuestions = version.sections.reduce(
    (sum: number, s: Section) => sum + s.questions.length, 0
  );

  if (totalQuestions === 0) {
    return (
      <Card>
        <CardContent className="flex flex-col items-center py-12">
          <CalculatorIcon className="size-10 text-muted-foreground" />
          <p className="mt-4 text-sm text-muted-foreground">
            Add questions to start calculating sample scores.
          </p>
        </CardContent>
      </Card>
    );
  }

  const setAnswer = (qid: string, keys: string[]) =>
    setAnswers((prev) => ({ ...prev, [qid]: keys }));

  const toggleAnswer = (qid: string, key: string, multi: boolean) => {
    const current = answers[qid] ?? [];
    if (multi) {
      const next = current.includes(key) ? current.filter((k) => k !== key) : [...current, key];
      setAnswer(qid, next);
    } else {
      setAnswer(qid, current[0] === key ? [] : [key]);
    }
  };

  // ─── Calculate scores ─────────────────────────────────
  type SectionResult = {
    sectionId: string; title: string; weight: number;
    earned: number; max: number; normalizedScore: number;
    questionResults: Array<{ qid: string; title: string; earned: number; max: number; answered: boolean }>;
  };

  const competencyMap = new Map<string, { name: string; earned: number; max: number }>();
  const sectionResults: SectionResult[] = [];
  let totalEarned = 0;
  let totalMax = 0;
  let answeredCount = 0;

  for (const section of version.sections) {
    let sectionEarned = 0;
    let sectionMax = 0;
    const questionResults = [];

    for (const q of section.questions) {
      const selectedKeys = answers[q.id] ?? [];
      const answered = selectedKeys.length > 0;
      if (answered) answeredCount++;

      let earned = 0;
      const max = q.maxPoints;

      // Compute earned points based on question type and scoring strategy
      const isRanking = q.questionType === "ranking" || q.questionType === "drag_order";

      if (answered) {
        if (isRanking) {
          // Ranking: compare candidate's order against correctAnswerKey
          let correctOrder: string[] = [];
          try {
            if (q.correctAnswerKey) correctOrder = JSON.parse(q.correctAnswerKey);
          } catch { /* ignore */ }

          if (correctOrder.length > 0 && selectedKeys.length === correctOrder.length) {
            // Score by position match (full credit for exact pos, half credit if off by 1)
            let score = 0;
            for (let i = 0; i < correctOrder.length; i++) {
              if (selectedKeys[i] === correctOrder[i]) {
                score += 1;
              } else {
                const actualPos = selectedKeys.indexOf(correctOrder[i]);
                if (actualPos >= 0 && Math.abs(actualPos - i) === 1) score += 0.5;
              }
            }
            earned = max * (score / correctOrder.length);
          } else if (correctOrder.length === 0) {
            // No correct order defined — fall back to summing option points
            for (const key of selectedKeys) {
              const opt = q.options.find((o: AnswerOption) => o.key === key);
              if (opt) earned += opt.points;
            }
            earned = Math.min(earned, max);
          }
        } else if (q.scoringStrategy === "weighted_options" || q.scoringStrategy === "exact" || q.scoringStrategy === "scenario_based") {
          // Sum the points of all selected options
          for (const key of selectedKeys) {
            const opt = q.options.find((o: AnswerOption) => o.key === key);
            if (opt) earned += opt.points;
          }
          // Cap at maxPoints for safety
          earned = Math.min(earned, max);
        } else if (q.scoringStrategy === "partial") {
          // Award proportional points for each correct selection
          const correctKeys = q.options.filter((o: AnswerOption) => o.isCorrect).map((o: AnswerOption) => o.key);
          if (correctKeys.length > 0) {
            const correctSelected = selectedKeys.filter((k) => correctKeys.includes(k)).length;
            const incorrectSelected = selectedKeys.filter((k) => !correctKeys.includes(k)).length;
            const ratio = Math.max(0, (correctSelected - incorrectSelected) / correctKeys.length);
            earned = max * ratio;
          }
        }
      }

      sectionEarned += earned;
      sectionMax += max;
      questionResults.push({ qid: q.id, title: q.title, earned, max, answered });

      // Competency contributions (use question weight for each linked competency)
      for (const qc of q.competencies as QuestionCompetencyRef[]) {
        const compName = qc.competency.name;
        const compId = qc.competency.id;
        const existing = competencyMap.get(compId) ?? { name: compName, earned: 0, max: 0 };
        const w = qc.weight ?? 1.0;
        existing.earned += earned * w;
        existing.max += max * w;
        competencyMap.set(compId, existing);
      }
    }

    sectionResults.push({
      sectionId: section.id,
      title: section.title,
      weight: section.weight,
      earned: sectionEarned,
      max: sectionMax,
      normalizedScore: sectionMax > 0 ? sectionEarned / sectionMax : 0,
      questionResults,
    });

    totalEarned += sectionEarned;
    totalMax += sectionMax;
  }

  const overallScore = totalMax > 0 ? totalEarned / totalMax : 0;
  const overallPercent = Math.round(overallScore * 100);

  // Apply weighted average if section weights are configured
  const totalWeight = sectionResults.reduce((sum, s) => sum + s.weight, 0);
  const weightedScore = totalWeight > 0
    ? sectionResults.reduce((sum, s) => sum + (s.normalizedScore * s.weight), 0) / totalWeight
    : overallScore;
  const weightedPercent = Math.round(weightedScore * 100);

  // Get template thresholds
  const t = parseThresholds(version.recommendationThresholds);
  const sh = t.strongHire * 100;
  const h = t.hire * 100;
  const c = t.consider * 100;
  const wf = t.weakFit * 100;

  const recommendation =
    weightedPercent >= sh ? { label: "Strong Hire", color: "bg-emerald-500", textColor: "text-emerald-700 dark:text-emerald-300", bg: "bg-emerald-50 dark:bg-emerald-950" } :
    weightedPercent >= h ? { label: "Hire", color: "bg-green-500", textColor: "text-green-700 dark:text-green-300", bg: "bg-green-50 dark:bg-green-950" } :
    weightedPercent >= c ? { label: "Consider", color: "bg-amber-500", textColor: "text-amber-700 dark:text-amber-300", bg: "bg-amber-50 dark:bg-amber-950" } :
    weightedPercent >= wf ? { label: "Weak Fit", color: "bg-orange-500", textColor: "text-orange-700 dark:text-orange-300", bg: "bg-orange-50 dark:bg-orange-950" } :
    { label: "Reject", color: "bg-red-500", textColor: "text-red-700 dark:text-red-300", bg: "bg-red-50 dark:bg-red-950" };

  // Auto-fill helpers
  const fillBest = () => {
    const newAnswers: Record<string, string[]> = {};
    for (const section of version.sections) {
      for (const q of section.questions) {
        if (q.options.length === 0) continue;
        const isRanking = q.questionType === "ranking" || q.questionType === "drag_order";
        if (isRanking) {
          // Use the correct order from correctAnswerKey
          try {
            const correctOrder = q.correctAnswerKey ? JSON.parse(q.correctAnswerKey) : null;
            if (Array.isArray(correctOrder) && correctOrder.length > 0) {
              newAnswers[q.id] = correctOrder;
            } else {
              newAnswers[q.id] = q.options.map((o: AnswerOption) => o.key);
            }
          } catch {
            newAnswers[q.id] = q.options.map((o: AnswerOption) => o.key);
          }
        } else if (q.questionType === "multi_select") {
          newAnswers[q.id] = q.options.filter((o: AnswerOption) => o.isCorrect).map((o: AnswerOption) => o.key);
        } else {
          const best = [...q.options].sort((a: AnswerOption, b: AnswerOption) => b.points - a.points)[0];
          newAnswers[q.id] = [best.key];
        }
      }
    }
    setAnswers(newAnswers);
  };

  const fillWorst = () => {
    const newAnswers: Record<string, string[]> = {};
    for (const section of version.sections) {
      for (const q of section.questions) {
        if (q.options.length === 0) continue;
        const isRanking = q.questionType === "ranking" || q.questionType === "drag_order";
        if (isRanking) {
          // Reverse the correct order
          try {
            const correctOrder = q.correctAnswerKey ? JSON.parse(q.correctAnswerKey) : null;
            if (Array.isArray(correctOrder) && correctOrder.length > 0) {
              newAnswers[q.id] = [...correctOrder].reverse();
            } else {
              newAnswers[q.id] = [...q.options.map((o: AnswerOption) => o.key)].reverse();
            }
          } catch {
            newAnswers[q.id] = [...q.options.map((o: AnswerOption) => o.key)].reverse();
          }
        } else {
          const worst = [...q.options].sort((a: AnswerOption, b: AnswerOption) => a.points - b.points)[0];
          newAnswers[q.id] = [worst.key];
        }
      }
    }
    setAnswers(newAnswers);
  };

  const fillRandom = () => {
    const newAnswers: Record<string, string[]> = {};
    for (const section of version.sections) {
      for (const q of section.questions) {
        if (q.options.length === 0) continue;
        const isRanking = q.questionType === "ranking" || q.questionType === "drag_order";
        if (isRanking) {
          // Shuffle the option keys
          const keys = q.options.map((o: AnswerOption) => o.key);
          for (let i = keys.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [keys[i], keys[j]] = [keys[j], keys[i]];
          }
          newAnswers[q.id] = keys;
          continue;
        }
        const random = q.options[Math.floor(Math.random() * q.options.length)];
        newAnswers[q.id] = [random.key];
      }
    }
    setAnswers(newAnswers);
  };

  const clearAll = () => setAnswers({});

  return (
    <div className="grid grid-cols-1 gap-4 lg:grid-cols-[1fr_380px]">
      {/* Left: Question picker */}
      <div className="space-y-4">
        <Card>
          <CardContent className="flex flex-wrap items-center gap-2 pt-3">
            <span className="text-xs font-medium text-muted-foreground">Quick fill:</span>
            <Button variant="outline" onClick={fillBest} className="text-xs">Best answers</Button>
            <Button variant="outline" onClick={fillWorst} className="text-xs">Worst answers</Button>
            <Button variant="outline" onClick={fillRandom} className="text-xs">Random</Button>
            <Button variant="outline" onClick={clearAll} className="text-xs">Clear all</Button>
            <span className="ml-auto text-xs text-muted-foreground">
              {answeredCount} / {totalQuestions} answered
            </span>
          </CardContent>
        </Card>

        {version.sections.map((section: Section, sIdx: number) => (
          <Card key={section.id}>
            <CardHeader className="pb-3">
              <CardTitle className="text-sm">
                Section {sIdx + 1}: {section.title}
              </CardTitle>
              <CardDescription>Weight: {section.weight}</CardDescription>
            </CardHeader>
            <CardContent>
              {section.questions.length === 0 ? (
                <p className="text-xs text-muted-foreground">No questions in this section.</p>
              ) : (
                <div className="space-y-3">
                  {section.questions.map((q: Question, qIdx: number) => {
                    const selectedKeys = answers[q.id] ?? [];
                    const isMulti = q.questionType === "multi_select";
                    const isRanking = q.questionType === "ranking" || q.questionType === "drag_order";
                    return (
                      <div key={q.id} className="rounded-lg border border-zinc-100 p-3 dark:border-zinc-800">
                        <div className="mb-2 flex items-start justify-between gap-2">
                          <p className="text-sm font-medium">
                            <span className="text-muted-foreground">Q{qIdx + 1}.</span> {q.title}
                          </p>
                          <Badge variant="secondary" className="text-[10px]">{q.maxPoints} pts</Badge>
                        </div>
                        {isRanking && (
                          <p className="mb-1.5 text-[10px] italic text-muted-foreground">
                            Click options in order from most to least important. Click again to remove.
                          </p>
                        )}
                        <div className="space-y-1.5">
                          {q.options.map((opt: AnswerOption) => {
                            const rankIdx = isRanking ? selectedKeys.indexOf(opt.key) : -1;
                            const isRanked = rankIdx >= 0;
                            const selected = isRanking ? isRanked : selectedKeys.includes(opt.key);
                            return (
                              <button
                                key={opt.id}
                                onClick={() => {
                                  if (isRanking) {
                                    setAnswer(q.id, isRanked ? selectedKeys.filter((k) => k !== opt.key) : [...selectedKeys, opt.key]);
                                  } else {
                                    toggleAnswer(q.id, opt.key, isMulti);
                                  }
                                }}
                                className={`flex w-full items-center gap-2 rounded-lg border-2 p-2 text-left text-xs transition-all ${
                                  selected
                                    ? "border-primary bg-primary/5"
                                    : "border-zinc-200 hover:border-zinc-300 dark:border-zinc-800"
                                }`}
                              >
                                {isRanking ? (
                                  <span className={`flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-md text-[10px] font-bold ${
                                    isRanked ? "bg-primary text-white" : "border-2 border-zinc-300 text-zinc-400 dark:border-zinc-600"
                                  }`}>
                                    {isRanked ? rankIdx + 1 : "·"}
                                  </span>
                                ) : (
                                  <span className={`flex h-4 w-4 flex-shrink-0 items-center justify-center ${isMulti ? "rounded-md" : "rounded-full"} border-2 ${
                                    selected ? "border-primary bg-primary" : "border-zinc-300 dark:border-zinc-600"
                                  }`}>
                                    {selected && <span className="text-[8px] text-white">{isMulti ? "✓" : "●"}</span>}
                                  </span>
                                )}
                                <span className="flex-1">{opt.label}</span>
                                {!isRanking && (
                                  <span className="text-[10px] text-muted-foreground">{opt.points} pts</span>
                                )}
                                {opt.isCorrect && (
                                  <span className="rounded-full bg-emerald-100 px-1.5 py-0.5 text-[8px] font-bold text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300">✓</span>
                                )}
                              </button>
                            );
                          })}
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Right: Live score panel */}
      <div className="space-y-4">
        <div className="sticky top-4 space-y-4">
          {/* Overall score */}
          <Card>
            <CardHeader className="pb-3">
              <CardTitle className="text-sm">Live Score</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-center">
                <div className={`mx-auto mb-3 inline-flex items-baseline gap-1 ${recommendation.textColor}`}>
                  <span className="text-5xl font-bold">{weightedPercent}</span>
                  <span className="text-xl font-semibold">%</span>
                </div>
                <p className={`inline-block rounded-full px-3 py-1 text-xs font-semibold ${recommendation.bg} ${recommendation.textColor}`}>
                  {recommendation.label}
                </p>
                <p className="mt-2 text-[10px] text-muted-foreground">
                  Raw: {totalEarned.toFixed(1)} / {totalMax} pts ({overallPercent}%)
                </p>
                <p className="text-[10px] text-muted-foreground">
                  Weighted by section weights → {weightedPercent}%
                </p>
              </div>

              {/* Threshold scale */}
              <div className="mt-5 pt-2">
                <div className="relative h-2 rounded-full bg-zinc-100 dark:bg-zinc-800">
                  <div className="absolute inset-y-0 left-0 rounded-l-full bg-red-500" style={{ width: `${wf}%` }} />
                  <div className="absolute inset-y-0 bg-orange-500" style={{ left: `${wf}%`, width: `${Math.max(0, c - wf)}%` }} />
                  <div className="absolute inset-y-0 bg-amber-400" style={{ left: `${c}%`, width: `${Math.max(0, h - c)}%` }} />
                  <div className="absolute inset-y-0 bg-green-500" style={{ left: `${h}%`, width: `${Math.max(0, sh - h)}%` }} />
                  <div className="absolute inset-y-0 right-0 rounded-r-full bg-emerald-500" style={{ left: `${sh}%` }} />
                  <div className="absolute top-1/2 -translate-x-1/2 -translate-y-1/2" style={{ left: `${weightedPercent}%` }}>
                    <div className="h-5 w-2 rounded-full border-2 border-white bg-zinc-900 shadow dark:border-zinc-900 dark:bg-white" />
                  </div>
                </div>
                <div className="mt-1 flex justify-between text-[9px] text-muted-foreground">
                  <span>0%</span><span>{wf}%</span><span>{c}%</span><span>{h}%</span><span>{sh}%</span><span>100%</span>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Section breakdown */}
          {sectionResults.length > 0 && (
            <Card>
              <CardHeader className="pb-3">
                <CardTitle className="text-sm">Section Scores</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  {sectionResults.map((s) => (
                    <div key={s.sectionId}>
                      <div className="mb-1 flex items-center justify-between">
                        <span className="text-xs font-medium">{s.title}</span>
                        <span className="text-xs font-bold">{Math.round(s.normalizedScore * 100)}%</span>
                      </div>
                      <div className="h-1.5 overflow-hidden rounded-full bg-zinc-100 dark:bg-zinc-800">
                        <div
                          className={`h-full rounded-full ${
                            s.normalizedScore >= 0.7 ? "bg-green-500" : s.normalizedScore >= 0.5 ? "bg-amber-500" : "bg-red-500"
                          }`}
                          style={{ width: `${Math.round(s.normalizedScore * 100)}%` }}
                        />
                      </div>
                      <p className="mt-0.5 text-[10px] text-muted-foreground">
                        {s.earned.toFixed(1)} / {s.max} pts &middot; weight: {s.weight}
                      </p>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          )}

          {/* Competency breakdown */}
          {competencyMap.size > 0 && (
            <Card>
              <CardHeader className="pb-3">
                <CardTitle className="text-sm">Competency Scores</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-2">
                  {Array.from(competencyMap.entries())
                    .map(([id, c]) => ({ id, ...c, score: c.max > 0 ? c.earned / c.max : 0 }))
                    .sort((a, b) => b.score - a.score)
                    .map((c) => (
                      <div key={c.id}>
                        <div className="mb-0.5 flex items-center justify-between">
                          <span className="text-xs">{c.name}</span>
                          <span className={`text-xs font-bold ${
                            c.score >= 0.7 ? "text-green-600" : c.score >= 0.5 ? "text-amber-600" : "text-red-600"
                          }`}>
                            {Math.round(c.score * 100)}%
                          </span>
                        </div>
                        <div className="h-1 overflow-hidden rounded-full bg-zinc-100 dark:bg-zinc-800">
                          <div
                            className={`h-full rounded-full ${
                              c.score >= 0.7 ? "bg-green-500" : c.score >= 0.5 ? "bg-amber-500" : "bg-red-500"
                            }`}
                            style={{ width: `${Math.round(c.score * 100)}%` }}
                          />
                        </div>
                      </div>
                    ))}
                </div>
              </CardContent>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
}

function Modal({ title, children, onClose, wide }: { title: string; children: React.ReactNode; onClose: () => void; wide?: boolean }) {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div className="fixed inset-0 bg-black/50" onClick={onClose} />
      <div className={`relative z-10 w-full rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900 ${wide ? "max-w-2xl" : "max-w-md"} max-h-[90vh] overflow-y-auto`}>
        <div className="mb-4 flex items-center justify-between">
          <h3 className="text-base font-semibold">{title}</h3>
          <button onClick={onClose} className="rounded-md p-1 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800">
            <X className="size-4" />
          </button>
        </div>
        {children}
      </div>
    </div>
  );
}

```