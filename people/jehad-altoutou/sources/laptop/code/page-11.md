---
type: source
source_type: laptop
title: page
slug: page-11
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/hr-forms/page.tsx
original_size: 52990
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/hr-forms/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useState } from "react";
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
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Plus,
  Send,
  Copy,
  Check,
  Loader2,
  FileText,
  Eye,
  Users,
  CheckCircle,
  Trash2,
  AlertTriangle,
  Clock,
  ChevronDown,
  Settings2,
  Save,
  X,
  GripVertical,
  Upload,
  ToggleLeft,
  ToggleRight,
} from "lucide-react";
import Link from "next/link";
import { AnimatePresence, motion } from "framer-motion";

interface Template {
  id: string;
  name: string;
  slug: string;
  formType: string;
  fields: string | null;
  isActive: boolean;
  _count?: { submissions: number; invites: number };
}

interface Submission {
  id: string;
  employeeName: string;
  employeeEmail: string;
  region: string;
  status: string;
  template: { name: string; formType: string };
  submittedAt: string;
  createdAt: string;
  files: unknown[];
}

interface Invite {
  id: string;
  code: string;
  employeeName: string;
  employeeEmail: string;
  region: string;
  status: string;
  template: { name: string };
  createdAt: string;
  expiresAt: string | null;
}

function CollapsibleSection({
  title,
  description,
  count,
  isOpen,
  onToggle,
  children,
}: {
  title: string;
  description: string;
  count: number;
  isOpen: boolean;
  onToggle: () => void;
  children: React.ReactNode;
}) {
  return (
    <Card>
      <button
        onClick={onToggle}
        className="flex w-full items-center justify-between px-6 py-4 text-left transition-colors hover:bg-zinc-50 dark:hover:bg-zinc-800/50"
      >
        <div className="flex items-center gap-3">
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-base font-semibold">{title}</h3>
              <span className="rounded-full bg-zinc-100 px-2 py-0.5 text-xs font-medium text-zinc-600 dark:bg-zinc-800 dark:text-zinc-400">
                {count}
              </span>
            </div>
            <p className="text-xs text-muted-foreground">{description}</p>
          </div>
        </div>
        <ChevronDown
          className={`size-4 text-muted-foreground transition-transform ${isOpen ? "rotate-180" : ""}`}
        />
      </button>
      <AnimatePresence initial={false}>
        {isOpen && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="overflow-hidden"
          >
            <div className="border-t border-zinc-100 dark:border-zinc-800">{children}</div>
          </motion.div>
        )}
      </AnimatePresence>
    </Card>
  );
}

const statusConfig: Record<string, { label: string; variant: "default" | "secondary" | "outline" | "destructive" }> = {
  pending: { label: "Pending", variant: "outline" },
  started: { label: "In Progress", variant: "secondary" },
  submitted: { label: "Submitted", variant: "default" },
  reviewed: { label: "Reviewed", variant: "default" },
  flagged: { label: "Flagged", variant: "destructive" },
  draft: { label: "Draft", variant: "outline" },
  expired: { label: "Expired", variant: "destructive" },
};

export default function HRFormsPage() {
  const [submissions, setSubmissions] = useState<Submission[]>([]);
  const [invites, setInvites] = useState<Invite[]>([]);
  const [templates, setTemplates] = useState<Template[]>([]);
  const [showForm, setShowForm] = useState(false);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [templateId, setTemplateId] = useState("");
  const [region, setRegion] = useState("global");
  const [expiresInDays] = useState("7");
  const [isCreating, setIsCreating] = useState(false);
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const [deleteTarget, setDeleteTarget] = useState<Invite | null>(null);
  const [deleteSubmissionTarget, setDeleteSubmissionTarget] = useState<Submission | null>(null);
  const [isDeleting, setIsDeleting] = useState(false);
  const [openSections, setOpenSections] = useState<Set<string>>(new Set(["submitted", "drafts", "invites"]));
  const [showTemplateManager, setShowTemplateManager] = useState(false);
  const [allTemplates, setAllTemplates] = useState<Template[]>([]);

  const toggleSection = (key: string) => {
    setOpenSections((prev) => {
      const next = new Set(prev);
      if (next.has(key)) next.delete(key); else next.add(key);
      return next;
    });
  };

  const loadData = () => {
    fetch("/api/admin/hr-forms")
      .then((r) => r.json())
      .then((d) => {
        setSubmissions(d.submissions ?? []);
        setInvites(d.invites ?? []);
        setTemplates(d.templates ?? []);
        if (d.templates?.length === 1) setTemplateId(d.templates[0].id);
      });
  };

  const loadTemplates = () => {
    fetch("/api/admin/form-templates")
      .then((r) => r.json())
      .then((d) => setAllTemplates(d.templates ?? []));
  };

  useEffect(() => { loadData(); }, []);

  const handleCreate = async () => {
    if (!name.trim() || !email.trim() || !templateId) return;
    setIsCreating(true);
    try {
      await fetch("/api/admin/hr-forms", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          employeeName: name.trim(),
          employeeEmail: email.trim(),
          templateId,
          region,
          expiresInDays: parseInt(expiresInDays) || 7,
        }),
      });
      // Refresh
      const d = await fetch("/api/admin/hr-forms").then((r) => r.json());
      setSubmissions(d.submissions ?? []);
      setInvites(d.invites ?? []);
      setName("");
      setEmail("");
      setShowForm(false);
    } catch { /* ignore */ }
    setIsCreating(false);
  };

  const copyLink = (code: string, id: string) => {
    navigator.clipboard.writeText(`${window.location.origin}/forms/${code}`);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const handleDeleteSubmission = async () => {
    if (!deleteSubmissionTarget) return;
    setIsDeleting(true);
    try {
      await fetch(`/api/admin/hr-forms/${deleteSubmissionTarget.id}`, { method: "DELETE" });
      const d = await fetch("/api/admin/hr-forms").then((r) => r.json());
      setSubmissions(d.submissions ?? []);
      setInvites(d.invites ?? []);
    } catch { /* ignore */ }
    setIsDeleting(false);
    setDeleteSubmissionTarget(null);
  };

  const handleDeleteInvite = async () => {
    if (!deleteTarget) return;
    setIsDeleting(true);
    try {
      await fetch(`/api/admin/hr-forms?id=${deleteTarget.id}`, { method: "DELETE" });
      setInvites((prev) => prev.filter((i) => i.id !== deleteTarget.id));
    } catch { /* ignore */ }
    setIsDeleting(false);
    setDeleteTarget(null);
  };

  const submitted = submissions.filter((s) => s.status === "submitted" || s.status === "reviewed");
  const drafts = submissions.filter((s) => s.status === "draft");

  // Group submitted forms by employee email so one row shows all their forms
  const submittedByEmployee = (() => {
    const map = new Map<string, { employeeName: string; employeeEmail: string; region: string; forms: Submission[] }>();
    for (const s of submitted) {
      const existing = map.get(s.employeeEmail);
      if (existing) {
        existing.forms.push(s);
      } else {
        map.set(s.employeeEmail, {
          employeeName: s.employeeName,
          employeeEmail: s.employeeEmail,
          region: s.region,
          forms: [s],
        });
      }
    }
    return [...map.values()];
  })();

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">HR Forms</h1>
          <p className="text-sm text-muted-foreground">
            Send and manage employee onboarding forms.
          </p>
        </div>
        <div className="flex gap-2">
          <Button variant="outline" onClick={() => { setShowTemplateManager(true); loadTemplates(); }} className="gap-2">
            <Settings2 className="size-4" /> Templates
          </Button>
          <Button onClick={() => setShowForm(!showForm)} className="gap-2">
            <Plus className="size-4" /> Send Form
          </Button>
        </div>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-4">
        <Card>
          <CardContent className="flex items-center gap-4 pt-2">
            <div className="rounded-lg bg-blue-50 p-2.5 dark:bg-blue-950">
              <Send className="size-5 text-blue-600" />
            </div>
            <div>
              <p className="text-2xl font-bold">{invites.length}</p>
              <p className="text-xs text-muted-foreground">Total Sent</p>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="flex items-center gap-4 pt-2">
            <div className="rounded-lg bg-emerald-50 p-2.5 dark:bg-emerald-950">
              <CheckCircle className="size-5 text-emerald-600" />
            </div>
            <div>
              <p className="text-2xl font-bold">{submitted.length}</p>
              <p className="text-xs text-muted-foreground">Submitted</p>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="flex items-center gap-4 pt-2">
            <div className="rounded-lg bg-amber-50 p-2.5 dark:bg-amber-950">
              <Clock className="size-5 text-amber-600" />
            </div>
            <div>
              <p className="text-2xl font-bold">{drafts.length}</p>
              <p className="text-xs text-muted-foreground">In Progress</p>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="flex items-center gap-4 pt-2">
            <div className="rounded-lg bg-pink-50 p-2.5 dark:bg-pink-950">
              <Users className="size-5 text-pink-600" />
            </div>
            <div>
              <p className="text-2xl font-bold">
                {invites.filter((i) => i.status === "pending").length}
              </p>
              <p className="text-xs text-muted-foreground">Pending</p>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Create form */}
      {showForm && (
        <Card>
          <CardHeader>
            <CardTitle>Send Form to Employee</CardTitle>
            <CardDescription>
              Generate a unique link and send an email invitation.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
              <div>
                <Label>Employee Name</Label>
                <Input placeholder="Jane Smith" value={name} onChange={(e) => setName(e.target.value)} className="mt-1.5" />
              </div>
              <div>
                <Label>Email</Label>
                <Input type="email" placeholder="jane@company.com" value={email} onChange={(e) => setEmail(e.target.value)} className="mt-1.5" />
              </div>
              <div>
                <Label>Form Type</Label>
                <div className="mt-1.5">
                  <Select value={templateId} onValueChange={(v) => setTemplateId(v ?? "")}>
                    <SelectTrigger className="w-full">
                      <SelectValue placeholder="Select a form" />
                    </SelectTrigger>
                    <SelectContent>
                      {templates.map((t) => (
                        <SelectItem key={t.id} value={t.id}>
                          {t.name}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
              </div>
              <div>
                <Label>Region</Label>
                <div className="mt-1.5">
                  <Select value={region} onValueChange={(v) => setRegion(v ?? "global")}>
                    <SelectTrigger className="w-full">
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="uae">UAE (JPEG only)</SelectItem>
                      <SelectItem value="global">Global (JPEG/PNG/PDF)</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
              </div>
            </div>
            <div className="mt-4 flex gap-3">
              <Button onClick={handleCreate} disabled={!name.trim() || !email.trim() || !templateId || isCreating} className="gap-2">
                {isCreating ? <Loader2 className="size-4 animate-spin" /> : <Send className="size-4" />}
                Send Invite
              </Button>
              <Button variant="outline" onClick={() => setShowForm(false)}>Cancel</Button>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Submitted Forms */}
      <CollapsibleSection
        title="Submitted Forms"
        description="Completed and submitted by employees"
        count={submitted.length}
        isOpen={openSections.has("submitted")}
        onToggle={() => toggleSection("submitted")}
      >
        <div className="px-4 sm:px-6">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead className="pl-0">Employee</TableHead>
                <TableHead>Form</TableHead>
                <TableHead>Region</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Files</TableHead>
                <TableHead className="pr-0 text-right">Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {submittedByEmployee.length === 0 ? (
                <TableRow>
                  <TableCell colSpan={6} className="py-8 text-center text-muted-foreground">
                    No submitted forms yet.
                  </TableCell>
                </TableRow>
              ) : (
                submittedByEmployee.map((emp) => {
                  const totalFiles = emp.forms.reduce((sum, f) => sum + f.files.length, 0);
                  return (
                    <TableRow key={emp.employeeEmail}>
                      <TableCell className="pl-0">
                        <p className="text-sm font-medium">{emp.employeeName}</p>
                        <p className="text-xs text-muted-foreground">{emp.employeeEmail}</p>
                      </TableCell>
                      <TableCell>
                        <div className="flex flex-wrap gap-1">
                          {emp.forms.map((f) => (
                            <span key={f.id} className="inline-flex items-center rounded-full bg-zinc-100 px-2 py-0.5 text-[10px] font-medium text-zinc-700 dark:bg-zinc-800 dark:text-zinc-300">
                              {f.template.name.replace(" Form", "")}
                            </span>
                          ))}
                        </div>
                      </TableCell>
                      <TableCell className="text-xs">{emp.region === "uae" ? "UAE" : "Global"}</TableCell>
                      <TableCell><Badge variant="default">Submitted</Badge></TableCell>
                      <TableCell className="text-xs">{totalFiles} files</TableCell>
                      <TableCell className="pr-0 text-right">
                        <div className="flex items-center justify-end gap-1">
                          {emp.forms.map((f) => (
                            <Link
                              key={f.id}
                              href={`/admin/hr-forms/${f.id}`}
                              className="inline-flex items-center gap-1 rounded-md px-2 py-1 text-xs font-medium text-muted-foreground hover:bg-zinc-100 hover:text-foreground dark:hover:bg-zinc-800"
                              title={`View ${f.template.name}`}
                            >
                              <Eye className="size-3" /> {f.template.name.replace(" Form", "")}
                            </Link>
                          ))}
                        </div>
                      </TableCell>
                    </TableRow>
                  );
                })
              )}
            </TableBody>
          </Table>
        </div>
      </CollapsibleSection>

      {/* Drafts (in-progress) */}
      <CollapsibleSection
        title="Drafts"
        description="Forms employees have started but not submitted"
        count={drafts.length}
        isOpen={openSections.has("drafts")}
        onToggle={() => toggleSection("drafts")}
      >
        <div className="px-4 sm:px-6">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead className="pl-0">Employee</TableHead>
                <TableHead>Form</TableHead>
                <TableHead>Region</TableHead>
                <TableHead className="pr-0 text-right">Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {drafts.length === 0 ? (
                <TableRow>
                  <TableCell colSpan={4} className="py-8 text-center text-muted-foreground">
                    No drafts in progress.
                  </TableCell>
                </TableRow>
              ) : (
                drafts.map((sub) => (
                  <TableRow key={sub.id}>
                    <TableCell className="pl-0">
                      <p className="text-sm font-medium">{sub.employeeName}</p>
                      <p className="text-xs text-muted-foreground">{sub.employeeEmail}</p>
                    </TableCell>
                    <TableCell className="text-xs">{sub.template.name}</TableCell>
                    <TableCell className="text-xs">{sub.region === "uae" ? "UAE" : "Global"}</TableCell>
                    <TableCell className="pr-0 text-right">
                      <div className="flex items-center justify-end gap-1">
                        <Link
                          href={`/admin/hr-forms/${sub.id}`}
                          className="inline-flex items-center gap-1 rounded-md px-2 py-1 text-xs font-medium text-muted-foreground hover:bg-zinc-100 hover:text-foreground dark:hover:bg-zinc-800"
                        >
                          <Eye className="size-3" /> View
                        </Link>
                        <button
                          onClick={() => setDeleteSubmissionTarget(sub)}
                          className="inline-flex items-center gap-1 rounded-md px-2 py-1 text-xs font-medium text-muted-foreground hover:bg-red-50 hover:text-red-600 dark:hover:bg-red-950 dark:hover:text-red-400"
                        >
                          <Trash2 className="size-3" />
                        </button>
                      </div>
                    </TableCell>
                  </TableRow>
                ))
              )}
            </TableBody>
          </Table>
        </div>
      </CollapsibleSection>

      {/* Sent Invites (pending + started only — submitted ones are shown in Submitted Forms) */}
      <CollapsibleSection
        title="Sent Invites"
        description="Invitation links waiting for employee response"
        count={invites.filter((i) => i.status !== "submitted" && i.status !== "reviewed").length}
        isOpen={openSections.has("invites")}
        onToggle={() => toggleSection("invites")}
      >
        <div className="px-4 sm:px-6">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead className="pl-0">Employee</TableHead>
                <TableHead>Form</TableHead>
                <TableHead>Region</TableHead>
                <TableHead>Status</TableHead>
                <TableHead className="pr-0 text-right">Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {invites.filter((i) => i.status !== "submitted" && i.status !== "reviewed").length === 0 ? (
                <TableRow>
                  <TableCell colSpan={5} className="py-8 text-center text-muted-foreground">
                    No pending invites.
                  </TableCell>
                </TableRow>
              ) : (
                invites
                  .filter((i) => i.status !== "submitted" && i.status !== "reviewed")
                  .map((inv) => {
                    const sc = statusConfig[inv.status] ?? statusConfig.pending;
                    return (
                      <TableRow key={inv.id}>
                        <TableCell className="pl-0">
                          <p className="text-sm font-medium">{inv.employeeName}</p>
                          <p className="text-xs text-muted-foreground">{inv.employeeEmail}</p>
                        </TableCell>
                        <TableCell className="text-xs">{inv.template.name}</TableCell>
                        <TableCell className="text-xs">{inv.region === "uae" ? "UAE" : "Global"}</TableCell>
                        <TableCell><Badge variant={sc.variant}>{sc.label}</Badge></TableCell>
                        <TableCell className="pr-0 text-right">
                          <div className="flex items-center justify-end gap-1">
                            <button
                              onClick={() => copyLink(inv.code, inv.id)}
                              className="inline-flex items-center gap-1.5 rounded-md px-2 py-1 text-xs font-medium text-muted-foreground hover:bg-zinc-100 hover:text-foreground dark:hover:bg-zinc-800"
                            >
                              {copiedId === inv.id ? (
                                <><Check className="size-3 text-green-500" /> Copied</>
                              ) : (
                                <><Copy className="size-3" /> Copy</>
                              )}
                            </button>
                            <button
                              onClick={() => setDeleteTarget(inv)}
                              className="inline-flex items-center gap-1.5 rounded-md px-2 py-1 text-xs font-medium text-muted-foreground hover:bg-red-50 hover:text-red-600 dark:hover:bg-red-950 dark:hover:text-red-400"
                            >
                              <Trash2 className="size-3" />
                            </button>
                          </div>
                        </TableCell>
                      </TableRow>
                    );
                  })
              )}
            </TableBody>
          </Table>
        </div>
      </CollapsibleSection>

      {/* Delete confirmation dialog */}
      {deleteTarget && (
        <div className="fixed inset-0 z-50 flex items-center justify-center">
          <div className="fixed inset-0 bg-black/50" onClick={() => setDeleteTarget(null)} />
          <div className="relative z-10 w-full max-w-sm rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
            <div className="mb-4 flex items-center gap-3">
              <div className="rounded-lg bg-red-50 p-2 dark:bg-red-950">
                <AlertTriangle className="size-5 text-red-600 dark:text-red-400" />
              </div>
              <div>
                <h3 className="text-sm font-semibold">Delete Invite</h3>
                <p className="text-xs text-muted-foreground">This action cannot be undone.</p>
              </div>
            </div>
            <p className="mb-5 text-sm text-muted-foreground">
              Are you sure you want to delete the form invite for{" "}
              <strong className="text-foreground">{deleteTarget.employeeName}</strong>{" "}
              ({deleteTarget.employeeEmail})? The invite link will stop working immediately.
            </p>
            <div className="flex justify-end gap-3">
              <Button variant="outline" onClick={() => setDeleteTarget(null)} disabled={isDeleting}>
                Cancel
              </Button>
              <Button variant="destructive" onClick={handleDeleteInvite} disabled={isDeleting} className="gap-2">
                {isDeleting ? <Loader2 className="size-4 animate-spin" /> : <Trash2 className="size-4" />}
                Delete
              </Button>
            </div>
          </div>
        </div>
      )}

      {/* Template Manager */}
      {showTemplateManager && (
        <TemplateManagerModal
          templates={allTemplates}
          onClose={() => setShowTemplateManager(false)}
          onRefresh={() => { loadTemplates(); loadData(); }}
        />
      )}

      {/* Draft delete confirmation */}
      {deleteSubmissionTarget && (
        <div className="fixed inset-0 z-50 flex items-center justify-center">
          <div className="fixed inset-0 bg-black/50" onClick={() => setDeleteSubmissionTarget(null)} />
          <div className="relative z-10 w-full max-w-sm rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
            <div className="mb-4 flex items-center gap-3">
              <div className="rounded-lg bg-red-50 p-2 dark:bg-red-950">
                <AlertTriangle className="size-5 text-red-600 dark:text-red-400" />
              </div>
              <div>
                <h3 className="text-sm font-semibold">Delete Draft</h3>
                <p className="text-xs text-muted-foreground">This action cannot be undone.</p>
              </div>
            </div>
            <p className="mb-5 text-sm text-muted-foreground">
              Are you sure you want to delete the draft for{" "}
              <strong className="text-foreground">{deleteSubmissionTarget.employeeName}</strong>?
              Any saved progress will be lost, and the employee will be able to start fresh from their invite link.
            </p>
            <div className="flex justify-end gap-3">
              <Button variant="outline" onClick={() => setDeleteSubmissionTarget(null)} disabled={isDeleting}>
                Cancel
              </Button>
              <Button variant="destructive" onClick={handleDeleteSubmission} disabled={isDeleting} className="gap-2">
                {isDeleting ? <Loader2 className="size-4 animate-spin" /> : <Trash2 className="size-4" />}
                Delete Draft
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

// ─── Field Types ─────────────────────────────────────────────

const FIELD_TYPES = [
  { value: "text", label: "Text" },
  { value: "email", label: "Email" },
  { value: "phone", label: "Phone" },
  { value: "date", label: "Date" },
  { value: "textarea", label: "Text Area" },
  { value: "select", label: "Dropdown" },
  { value: "file", label: "File Upload" },
  { value: "heading", label: "Section Heading" },
];

interface FieldDef {
  name: string;
  label: string;
  type: string;
  required: boolean;
  placeholder: string;
  options: string[];
  section: string;
}

// ─── Template Manager Modal ──────────────────────────────────

function TemplateManagerModal({
  templates, onClose, onRefresh,
}: {
  templates: Template[];
  onClose: () => void;
  onRefresh: () => void;
}) {
  const [showBuilder, setShowBuilder] = useState(false);
  const [editingTemplate, setEditingTemplate] = useState<Template | null>(null);
  const [previewTemplate, setPreviewTemplate] = useState<Template | null>(null);
  const [deleting, setDeleting] = useState<string | null>(null);
  const [deleteError, setDeleteError] = useState<string | null>(null);

  const handleDelete = async (id: string) => {
    setDeleting(id);
    setDeleteError(null);
    const res = await fetch(`/api/admin/form-templates/${id}`, { method: "DELETE" });
    if (!res.ok) {
      const d = await res.json();
      setDeleteError(d.error);
      setDeleting(null);
      return;
    }
    setDeleting(null);
    onRefresh();
  };

  const handleToggleActive = async (t: Template) => {
    await fetch(`/api/admin/form-templates/${t.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ isActive: !t.isActive }),
    });
    onRefresh();
  };

  if (previewTemplate) {
    return (
      <FormTemplatePreview
        template={previewTemplate}
        onClose={() => setPreviewTemplate(null)}
      />
    );
  }

  if (showBuilder || editingTemplate) {
    return (
      <FormTemplateBuilder
        existing={editingTemplate}
        onClose={() => { setShowBuilder(false); setEditingTemplate(null); }}
        onSaved={() => { setShowBuilder(false); setEditingTemplate(null); onRefresh(); }}
      />
    );
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div className="fixed inset-0 bg-black/50" onClick={onClose} />
      <div className="relative z-10 max-h-[85vh] w-full max-w-2xl overflow-y-auto rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
        <div className="mb-5 flex items-center justify-between">
          <div>
            <h3 className="text-lg font-semibold">Form Templates</h3>
            <p className="text-xs text-muted-foreground">Create and manage HR form templates.</p>
          </div>
          <div className="flex items-center gap-2">
            <Button onClick={() => setShowBuilder(true)} className="gap-2">
              <Plus className="size-4" /> New Template
            </Button>
            <button onClick={onClose} className="rounded-md p-1 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800">
              <X className="size-4" />
            </button>
          </div>
        </div>

        {deleteError && (
          <p className="mb-3 rounded-lg bg-red-50 p-2 text-xs text-red-700 dark:bg-red-950 dark:text-red-300">{deleteError}</p>
        )}

        <div className="space-y-2">
          {templates.length === 0 ? (
            <div className="flex flex-col items-center py-8">
              <FileText className="size-10 text-muted-foreground" />
              <p className="mt-3 text-sm text-muted-foreground">No form templates yet.</p>
            </div>
          ) : (
            templates.map((t) => {
              const fieldCount = t.fields ? JSON.parse(t.fields).length : 0;
              const isBuiltIn = t.formType !== "custom";
              return (
                <div key={t.id} className="flex items-center gap-4 rounded-xl border border-zinc-100 p-4 dark:border-zinc-800">
                  <div className="rounded-lg bg-zinc-100 p-2.5 dark:bg-zinc-800">
                    <FileText className="size-4 text-zinc-600 dark:text-zinc-400" />
                  </div>
                  <div className="min-w-0 flex-1">
                    <div className="flex items-center gap-2">
                      <p className="text-sm font-semibold">{t.name}</p>
                      <Badge variant={t.isActive ? "default" : "outline"} className="text-[10px]">
                        {t.isActive ? "Active" : "Inactive"}
                      </Badge>
                      {isBuiltIn && <Badge variant="secondary" className="text-[10px]">Built-in</Badge>}
                      {!isBuiltIn && <Badge variant="outline" className="text-[10px]">Custom</Badge>}
                    </div>
                    <p className="text-xs text-muted-foreground">
                      {isBuiltIn ? `Type: ${t.formType.replace(/_/g, " ")}` : `${fieldCount} fields`}
                      {t._count ? ` · ${t._count.submissions} submissions · ${t._count.invites} invites` : ""}
                    </p>
                  </div>
                  <div className="flex items-center gap-1">
                    {t.fields && (
                      <button
                        onClick={() => setPreviewTemplate(t)}
                        className="rounded-md p-1.5 text-zinc-400 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-blue-950"
                        title="Preview"
                      >
                        <Eye className="size-3.5" />
                      </button>
                    )}
                    {!isBuiltIn && (
                      <button
                        onClick={() => setEditingTemplate(t)}
                        className="rounded-md p-1.5 text-zinc-400 hover:bg-zinc-100 hover:text-zinc-600 dark:hover:bg-zinc-800"
                        title="Edit"
                      >
                        <Settings2 className="size-3.5" />
                      </button>
                    )}
                    <button
                      onClick={() => handleToggleActive(t)}
                      className={`rounded-md p-1.5 ${t.isActive ? "text-green-500 hover:bg-red-50 hover:text-red-500 dark:hover:bg-red-950" : "text-zinc-400 hover:bg-green-50 hover:text-green-600 dark:hover:bg-green-950"}`}
                      title={t.isActive ? "Deactivate" : "Activate"}
                    >
                      {t.isActive ? <ToggleRight className="size-4" /> : <ToggleLeft className="size-4" />}
                    </button>
                    {!isBuiltIn && (
                      <button
                        onClick={() => handleDelete(t.id)}
                        disabled={deleting === t.id}
                        className="rounded-md p-1.5 text-zinc-400 hover:bg-red-50 hover:text-red-500 dark:hover:bg-red-950"
                        title="Delete"
                      >
                        {deleting === t.id ? <Loader2 className="size-3.5 animate-spin" /> : <Trash2 className="size-3.5" />}
                      </button>
                    )}
                  </div>
                </div>
              );
            })
          )}
        </div>
      </div>
    </div>
  );
}

// ─── Form Template Builder ───────────────────────────────────

function FormTemplateBuilder({
  existing, onClose, onSaved,
}: {
  existing: Template | null;
  onClose: () => void;
  onSaved: () => void;
}) {
  const [name, setName] = useState(existing?.name ?? "");
  const [description, setDescription] = useState("");
  const [fields, setFields] = useState<FieldDef[]>(() => {
    if (existing?.fields) {
      try { return JSON.parse(existing.fields); } catch { return []; }
    }
    return [];
  });
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const addField = (type: string) => {
    const idx = fields.length + 1;
    setFields([...fields, {
      name: type === "heading" ? `section_${idx}` : `field_${idx}`,
      label: type === "heading" ? "Section Title" : "",
      type,
      required: false,
      placeholder: "",
      options: type === "select" ? ["Option 1", "Option 2"] : [],
      section: "",
    }]);
  };

  const updateField = (index: number, updates: Partial<FieldDef>) => {
    const next = [...fields];
    next[index] = { ...next[index], ...updates };
    // Auto-generate name from label
    if (updates.label !== undefined) {
      next[index].name = updates.label.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/(^_|_$)/g, "") || `field_${index + 1}`;
    }
    setFields(next);
  };

  const removeField = (index: number) => setFields(fields.filter((_, i) => i !== index));

  const moveField = (index: number, direction: -1 | 1) => {
    const newIndex = index + direction;
    if (newIndex < 0 || newIndex >= fields.length) return;
    const next = [...fields];
    [next[index], next[newIndex]] = [next[newIndex], next[index]];
    setFields(next);
  };

  const handleSave = async () => {
    if (!name.trim()) return;
    if (fields.length === 0) { setError("Add at least one field"); return; }

    // Validate all fields have labels
    for (const f of fields) {
      if (!f.label.trim()) { setError("All fields must have a label"); return; }
    }

    setSaving(true);
    setError(null);

    const url = existing
      ? `/api/admin/form-templates/${existing.id}`
      : "/api/admin/form-templates";
    const method = existing ? "PATCH" : "POST";

    try {
      const res = await fetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name.trim(), description: description.trim(), fields }),
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
      <div className="relative z-10 max-h-[90vh] w-full max-w-3xl overflow-y-auto rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
        <div className="mb-5 flex items-center justify-between">
          <div>
            <h3 className="text-lg font-semibold">{existing ? "Edit Template" : "New Form Template"}</h3>
            <p className="text-xs text-muted-foreground">Define the fields employees will fill out.</p>
          </div>
          <button onClick={onClose} className="rounded-md p-1 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800">
            <X className="size-4" />
          </button>
        </div>

        <div className="space-y-4">
          {/* Template name */}
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div>
              <Label>Template Name</Label>
              <Input value={name} onChange={(e) => setName(e.target.value)} placeholder="e.g. Employee Equipment Request" className="mt-1.5" />
            </div>
            <div>
              <Label>Description (optional)</Label>
              <Input value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Brief description" className="mt-1.5" />
            </div>
          </div>

          {/* Add field buttons */}
          <div>
            <Label>Add Fields</Label>
            <div className="mt-2 flex flex-wrap gap-2">
              {FIELD_TYPES.map((ft) => (
                <Button key={ft.value} variant="outline" onClick={() => addField(ft.value)} className="gap-1.5 text-xs">
                  <Plus className="size-3" /> {ft.label}
                </Button>
              ))}
            </div>
          </div>

          {/* Field list */}
          {fields.length === 0 ? (
            <div className="rounded-xl border-2 border-dashed border-zinc-200 py-12 text-center dark:border-zinc-700">
              <FileText className="mx-auto size-8 text-muted-foreground" />
              <p className="mt-2 text-sm text-muted-foreground">No fields yet. Click the buttons above to add fields.</p>
            </div>
          ) : (
            <div className="space-y-2">
              {fields.map((field, idx) => (
                <div key={idx} className="flex items-start gap-2 rounded-xl border border-zinc-100 p-3 dark:border-zinc-800">
                  <div className="flex flex-col gap-1 pt-1">
                    <button onClick={() => moveField(idx, -1)} disabled={idx === 0} className="text-zinc-300 hover:text-zinc-600 disabled:opacity-30">
                      <ChevronDown className="size-3 rotate-180" />
                    </button>
                    <GripVertical className="size-3 text-zinc-300" />
                    <button onClick={() => moveField(idx, 1)} disabled={idx === fields.length - 1} className="text-zinc-300 hover:text-zinc-600 disabled:opacity-30">
                      <ChevronDown className="size-3" />
                    </button>
                  </div>
                  <div className="min-w-0 flex-1 space-y-2">
                    {field.type === "heading" ? (
                      <Input
                        value={field.label}
                        onChange={(e) => updateField(idx, { label: e.target.value })}
                        placeholder="Section heading text"
                        className="font-semibold"
                      />
                    ) : (
                      <div className="grid grid-cols-1 gap-2 sm:grid-cols-3">
                        <Input
                          value={field.label}
                          onChange={(e) => updateField(idx, { label: e.target.value })}
                          placeholder="Field label"
                        />
                        <Input
                          value={field.placeholder}
                          onChange={(e) => updateField(idx, { placeholder: e.target.value })}
                          placeholder="Placeholder text"
                        />
                        <div className="flex items-center gap-3">
                          <Badge variant="outline" className="whitespace-nowrap text-[10px]">{field.type}</Badge>
                          <label className="flex items-center gap-1.5 text-xs">
                            <input
                              type="checkbox"
                              checked={field.required}
                              onChange={(e) => updateField(idx, { required: e.target.checked })}
                            />
                            Required
                          </label>
                        </div>
                      </div>
                    )}
                    {field.type === "select" && (
                      <div>
                        <p className="mb-1 text-[10px] text-muted-foreground">Options (comma-separated)</p>
                        <Input
                          value={field.options.join(", ")}
                          onChange={(e) => updateField(idx, { options: e.target.value.split(",").map((s) => s.trim()).filter(Boolean) })}
                          placeholder="Option 1, Option 2, Option 3"
                        />
                      </div>
                    )}
                  </div>
                  <button onClick={() => removeField(idx)} className="mt-1 rounded-md p-1 text-zinc-400 hover:bg-red-50 hover:text-red-500 dark:hover:bg-red-950">
                    <Trash2 className="size-3.5" />
                  </button>
                </div>
              ))}
            </div>
          )}

          {error && <p className="text-xs text-red-600">{error}</p>}

          <div className="flex justify-end gap-3 pt-2">
            <Button variant="outline" onClick={onClose} disabled={saving}>Cancel</Button>
            <Button onClick={handleSave} disabled={!name.trim() || fields.length === 0 || saving} className="gap-2">
              {saving ? <Loader2 className="size-4 animate-spin" /> : <Save className="size-4" />}
              {existing ? "Update Template" : "Create Template"}
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}

// ─── Form Template Preview ───────────────────────────────────

function FormTemplatePreview({
  template, onClose,
}: {
  template: Template;
  onClose: () => void;
}) {
  const fields: FieldDef[] = template.fields ? JSON.parse(template.fields) : [];

  // Group by section headings
  const groups: Array<{ heading: string | null; fields: FieldDef[] }> = [];
  let currentFields: FieldDef[] = [];
  let currentHeading: string | null = null;

  for (const f of fields) {
    if (f.type === "heading") {
      if (currentFields.length > 0 || currentHeading !== null) {
        groups.push({ heading: currentHeading, fields: currentFields });
      }
      currentHeading = f.label;
      currentFields = [];
    } else {
      currentFields.push(f);
    }
  }
  if (currentFields.length > 0 || currentHeading !== null) {
    groups.push({ heading: currentHeading, fields: currentFields });
  }

  // If any explicit `file` field is declared, skip the legacy generic
  // "Attachments" preview block — the form already renders labeled per-field
  // dropzones inline (matches the public /forms/[code] behaviour).
  const hasExplicitFileFields = fields.some((f) => f.type === "file");

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div className="fixed inset-0 bg-black/50" onClick={onClose} />
      <div className="relative z-10 max-h-[90vh] w-full max-w-3xl overflow-y-auto rounded-2xl border border-zinc-200 bg-zinc-50 shadow-xl dark:border-zinc-800 dark:bg-zinc-950">
        {/* Preview header bar */}
        <div className="sticky top-0 z-10 flex items-center justify-between border-b border-zinc-200 bg-white/80 px-6 py-3 backdrop-blur-lg dark:border-zinc-800 dark:bg-zinc-950/80">
          <div className="flex items-center gap-3">
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary/10">
              <FileText className="size-4 text-primary" />
            </div>
            <div>
              <p className="text-xs text-muted-foreground">{template.name}</p>
              <p className="text-sm font-semibold">Preview Mode</p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <Badge variant="outline" className="text-[10px]">Preview — not submittable</Badge>
            <button onClick={onClose} className="rounded-md p-1.5 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800">
              <X className="size-4" />
            </button>
          </div>
        </div>

        {/* Preview body — mimics candidate form layout */}
        <div className="px-6 py-8">
          <div className="space-y-6">
            {groups.length === 0 ? (
              <div className="rounded-2xl border border-zinc-200 bg-white p-8 text-center dark:border-zinc-800 dark:bg-zinc-900">
                <FileText className="mx-auto size-8 text-muted-foreground" />
                <p className="mt-2 text-sm text-muted-foreground">No fields defined. Edit the template to add fields.</p>
              </div>
            ) : (
              groups.map((group, gIdx) => (
                <div
                  key={gIdx}
                  className="rounded-2xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-900"
                >
                  <div className="mb-5 flex items-center gap-3">
                    <span className="flex h-7 w-7 items-center justify-center rounded-full bg-primary/10 text-xs font-bold text-primary">
                      {gIdx + 1}
                    </span>
                    <h3 className="text-base font-semibold">{group.heading ?? template.name}</h3>
                  </div>
                  <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                    {group.fields.map((field) => {
                      if (field.type === "textarea") {
                        return (
                          <div key={field.name} className="sm:col-span-2">
                            <label className="mb-1.5 block text-sm font-medium">
                              {field.label}
                              {field.required && <span className="ml-0.5 text-red-500">*</span>}
                            </label>
                            <textarea
                              disabled
                              placeholder={field.placeholder || field.label}
                              className="min-h-[80px] w-full rounded-lg border border-input bg-zinc-50/50 p-3 text-sm text-muted-foreground dark:bg-zinc-800/30"
                            />
                          </div>
                        );
                      }
                      if (field.type === "select") {
                        return (
                          <div key={field.name}>
                            <label className="mb-1.5 block text-sm font-medium">
                              {field.label}
                              {field.required && <span className="ml-0.5 text-red-500">*</span>}
                            </label>
                            <Select disabled>
                              <SelectTrigger className="w-full">
                                <SelectValue placeholder={field.placeholder || "Select..."} />
                              </SelectTrigger>
                              <SelectContent>
                                {(field.options ?? []).map((opt) => (
                                  <SelectItem key={opt} value={opt}>{opt}</SelectItem>
                                ))}
                              </SelectContent>
                            </Select>
                          </div>
                        );
                      }
                      if (field.type === "file") {
                        return (
                          <div key={field.name} className="sm:col-span-2">
                            <label className="mb-1.5 block text-sm font-medium">
                              {field.label}
                              {field.required && <span className="ml-0.5 text-red-500">*</span>}
                            </label>
                            <div className="flex cursor-not-allowed flex-col items-center gap-2 rounded-xl border-2 border-dashed border-zinc-300 p-6 opacity-60 dark:border-zinc-700">
                              <Upload className="size-4 text-muted-foreground" />
                              <span className="text-xs text-muted-foreground">File upload area</span>
                            </div>
                          </div>
                        );
                      }
                      return (
                        <div key={field.name}>
                          <label className="mb-1.5 block text-sm font-medium">
                            {field.label}
                            {field.required && <span className="ml-0.5 text-red-500">*</span>}
                          </label>
                          <Input
                            disabled
                            type={field.type === "phone" ? "tel" : field.type === "date" ? "date" : field.type === "email" ? "email" : "text"}
                            placeholder={field.placeholder || field.label}
                            className="bg-zinc-50/50 dark:bg-zinc-800/30"
                          />
                        </div>
                      );
                    })}
                  </div>
                </div>
              ))
            )}

            {/* Attachments preview — only shown when the form has no explicit file fields */}
            {!hasExplicitFileFields && (
              <div className="rounded-2xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-900">
                <div className="mb-5 flex items-center gap-3">
                  <span className="flex h-7 w-7 items-center justify-center rounded-full bg-primary/10 text-xs font-bold text-primary">
                    {groups.length + 1}
                  </span>
                  <h3 className="text-base font-semibold">Attachments</h3>
                </div>
                <div className="flex cursor-not-allowed flex-col items-center gap-2 rounded-xl border-2 border-dashed border-zinc-300 p-8 opacity-60 dark:border-zinc-700">
                  <Upload className="size-5 text-muted-foreground" />
                  <span className="text-sm font-medium text-muted-foreground">Click to upload files</span>
                  <span className="text-[10px] text-muted-foreground">File upload area (disabled in preview)</span>
                </div>
              </div>
            )}

            {/* Submit bar preview */}
            <div className="rounded-2xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-900">
              <div className="flex items-center justify-between">
                <p className="text-xs text-muted-foreground">This is how the form will appear to employees.</p>
                <Button disabled className="gap-2 opacity-60">
                  <Send className="size-4" /> Submit Form
                </Button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

```