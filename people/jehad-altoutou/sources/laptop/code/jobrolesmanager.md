---
type: source
source_type: laptop
title: JobRolesManager
slug: jobrolesmanager
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/components/admin/JobRolesManager.tsx
original_size: 18627
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# JobRolesManager

_Extracted from `[[assessify|assessify]]/src/components/admin/JobRolesManager.tsx` on 2026-05-14._

```tsx
"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  Briefcase,
  Plus,
  Trash2,
  Loader2,
  X,
  AlertTriangle,
  Save,
  Pencil,
} from "lucide-react";

interface JobRole {
  id: string;
  title: string;
  slug: string;
  description: string | null;
  isActive: boolean;
  templateCount?: number;
  jdSummary?: string | null;
  jdResponsibilities?: string | null;
  jdRequirements?: string | null;
  jdNiceToHaves?: string | null;
  jdYearsExperience?: string | null;
  interviewerEmail?: string | null;
}

interface Props {
  departmentId: string;
  departmentName: string;
  initialRoles: JobRole[];
}

type RoleFormFields = {
  title: string;
  description: string;
  jdSummary: string;
  jdResponsibilities: string;
  jdRequirements: string;
  jdNiceToHaves: string;
  jdYearsExperience: string;
  interviewerEmail: string;
};

const EMPTY_FORM: RoleFormFields = {
  title: "",
  description: "",
  jdSummary: "",
  jdResponsibilities: "",
  jdRequirements: "",
  jdNiceToHaves: "",
  jdYearsExperience: "",
  interviewerEmail: "",
};

function formFromRole(role: JobRole): RoleFormFields {
  return {
    title: role.title ?? "",
    description: role.description ?? "",
    jdSummary: role.jdSummary ?? "",
    jdResponsibilities: role.jdResponsibilities ?? "",
    jdRequirements: role.jdRequirements ?? "",
    jdNiceToHaves: role.jdNiceToHaves ?? "",
    jdYearsExperience: role.jdYearsExperience ?? "",
    interviewerEmail: role.interviewerEmail ?? "",
  };
}

export function JobRolesManager({ departmentId, departmentName, initialRoles }: Props) {
  const [roles, setRoles] = useState(initialRoles);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [createForm, setCreateForm] = useState<RoleFormFields>(EMPTY_FORM);
  const [isCreating, setIsCreating] = useState(false);
  const [createError, setCreateError] = useState<string | null>(null);

  const [editTarget, setEditTarget] = useState<JobRole | null>(null);
  const [editForm, setEditForm] = useState<RoleFormFields>(EMPTY_FORM);
  const [isSaving, setIsSaving] = useState(false);
  const [editError, setEditError] = useState<string | null>(null);

  const [deleteTarget, setDeleteTarget] = useState<JobRole | null>(null);
  const [isDeleting, setIsDeleting] = useState(false);
  const [deleteError, setDeleteError] = useState<string | null>(null);

  const startEdit = (role: JobRole) => {
    setEditTarget(role);
    setEditForm(formFromRole(role));
    setEditError(null);
  };

  const handleCreate = async () => {
    if (!createForm.title.trim()) return;
    setIsCreating(true);
    setCreateError(null);
    try {
      const res = await fetch("/api/admin/job-roles", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...createForm, departmentId }),
      });
      const data = await res.json();
      if (!res.ok) {
        setCreateError(data.error);
        setIsCreating(false);
        return;
      }
      setRoles([...roles, { ...data.role, templateCount: 0 }]);
      setCreateForm(EMPTY_FORM);
      setShowCreateForm(false);
    } catch {
      setCreateError("Network error");
    }
    setIsCreating(false);
  };

  const handleSave = async () => {
    if (!editTarget || !editForm.title.trim()) return;
    setIsSaving(true);
    setEditError(null);
    try {
      const res = await fetch(`/api/admin/job-roles/${editTarget.id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(editForm),
      });
      const data = await res.json();
      if (!res.ok) {
        setEditError(data.error ?? "Failed to save");
        setIsSaving(false);
        return;
      }
      setRoles((prev) =>
        prev.map((r) => (r.id === editTarget.id ? { ...r, ...editForm } : r)),
      );
      setEditTarget(null);
    } catch {
      setEditError("Network error");
    }
    setIsSaving(false);
  };

  const handleDelete = async () => {
    if (!deleteTarget) return;
    setIsDeleting(true);
    setDeleteError(null);
    try {
      const res = await fetch(`/api/admin/job-roles/${deleteTarget.id}`, { method: "DELETE" });
      const data = await res.json();
      if (!res.ok) {
        setDeleteError(data.error);
        setIsDeleting(false);
        return;
      }
      setRoles(roles.filter((r) => r.id !== deleteTarget.id));
      setDeleteTarget(null);
    } catch {
      setDeleteError("Network error");
    }
    setIsDeleting(false);
  };

  return (
    <Card>
      <CardHeader>
        <div className="flex items-center justify-between">
          <div>
            <CardTitle>Job Roles</CardTitle>
            <CardDescription>
              Roles in {departmentName}. New assessments use these roles.
            </CardDescription>
          </div>
          <Button onClick={() => setShowCreateForm(!showCreateForm)} className="gap-2">
            <Plus className="size-4" /> Add Role
          </Button>
        </div>
      </CardHeader>
      <CardContent>
        {showCreateForm && (
          <div className="mb-4 rounded-xl border border-zinc-200 bg-zinc-50 p-4 dark:border-zinc-800 dark:bg-zinc-800/30">
            <h4 className="mb-3 text-sm font-semibold">New Role</h4>
            <RoleFormFieldsBlock
              values={createForm}
              onChange={(patch) => setCreateForm((prev) => ({ ...prev, ...patch }))}
            />
            {createError && <p className="mt-3 text-xs text-red-600">{createError}</p>}
            <div className="mt-4 flex gap-2">
              <Button
                onClick={handleCreate}
                disabled={!createForm.title.trim() || isCreating}
                className="gap-2"
              >
                {isCreating ? <Loader2 className="size-4 animate-spin" /> : <Save className="size-4" />}
                Add Role
              </Button>
              <Button
                variant="outline"
                onClick={() => {
                  setShowCreateForm(false);
                  setCreateError(null);
                  setCreateForm(EMPTY_FORM);
                }}
              >
                Cancel
              </Button>
            </div>
          </div>
        )}

        {roles.length === 0 ? (
          <div className="flex flex-col items-center py-8">
            <Briefcase className="size-10 text-muted-foreground" />
            <p className="mt-3 text-sm text-muted-foreground">No roles in this department yet.</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {roles.map((role) => {
              const hasJd =
                !!role.jdSummary ||
                !!role.jdResponsibilities ||
                !!role.jdRequirements;
              return (
                <div key={role.id} className="rounded-xl border border-zinc-100 p-4 dark:border-zinc-800">
                  <div className="flex items-start justify-between gap-2">
                    <div className="flex items-center gap-3">
                      <div className="rounded-lg bg-zinc-100 p-2 dark:bg-zinc-800">
                        <Briefcase className="size-4 text-zinc-600 dark:text-zinc-400" />
                      </div>
                      <div>
                        <p className="text-sm font-semibold">{role.title}</p>
                        <div className="flex items-center gap-1.5">
                          {role.templateCount !== undefined && (
                            <p className="text-[10px] text-muted-foreground">
                              {role.templateCount} assessment{role.templateCount !== 1 ? "s" : ""}
                            </p>
                          )}
                          <span
                            className={
                              "inline-flex items-center rounded-full px-1.5 py-0.5 text-[9px] font-medium " +
                              (hasJd
                                ? "bg-emerald-50 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300"
                                : "bg-amber-50 text-amber-700 dark:bg-amber-950 dark:text-amber-300")
                            }
                            title={hasJd ? "Job description set" : "Job description missing — add it for accurate pre-screening"}
                          >
                            {hasJd ? "JD set" : "No JD"}
                          </span>
                        </div>
                      </div>
                    </div>
                    <div className="flex items-center gap-1">
                      <button
                        onClick={() => startEdit(role)}
                        aria-label="Edit role"
                        className="rounded-md p-1 text-zinc-400 hover:bg-zinc-100 hover:text-zinc-700 dark:hover:bg-zinc-800 dark:hover:text-zinc-200"
                      >
                        <Pencil className="size-3.5" />
                      </button>
                      <button
                        onClick={() => {
                          setDeleteTarget(role);
                          setDeleteError(null);
                        }}
                        aria-label="Delete role"
                        className="rounded-md p-1 text-zinc-400 hover:bg-red-50 hover:text-red-500 dark:hover:bg-red-950"
                      >
                        <Trash2 className="size-3.5" />
                      </button>
                    </div>
                  </div>
                  {role.description && (
                    <p className="mt-2 text-xs text-muted-foreground">{role.description}</p>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </CardContent>

      {/* Edit modal */}
      {editTarget && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          <div className="fixed inset-0 bg-black/50" onClick={() => setEditTarget(null)} />
          <div className="relative z-10 max-h-[90vh] w-full max-w-2xl overflow-y-auto rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
            <div className="mb-4 flex items-center justify-between">
              <div>
                <h3 className="text-base font-semibold">Edit role</h3>
                <p className="text-xs text-muted-foreground">
                  Fill in the Job Description below — the pre-screening agent uses these fields to
                  score candidate CVs against the role.
                </p>
              </div>
              <button
                onClick={() => setEditTarget(null)}
                className="rounded-md p-1 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800"
              >
                <X className="size-4" />
              </button>
            </div>

            <RoleFormFieldsBlock
              values={editForm}
              onChange={(patch) => setEditForm((prev) => ({ ...prev, ...patch }))}
            />

            {editError && <p className="mt-3 text-xs text-red-600">{editError}</p>}

            <div className="mt-5 flex justify-end gap-2">
              <Button variant="outline" onClick={() => setEditTarget(null)} disabled={isSaving}>
                Cancel
              </Button>
              <Button
                onClick={handleSave}
                disabled={!editForm.title.trim() || isSaving}
                className="gap-2"
              >
                {isSaving ? <Loader2 className="size-4 animate-spin" /> : <Save className="size-4" />}
                Save changes
              </Button>
            </div>
          </div>
        </div>
      )}

      {/* Delete confirmation */}
      {deleteTarget && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          <div className="fixed inset-0 bg-black/50" onClick={() => setDeleteTarget(null)} />
          <div className="relative z-10 w-full max-w-sm rounded-2xl border border-zinc-200 bg-white p-6 shadow-xl dark:border-zinc-800 dark:bg-zinc-900">
            <div className="mb-4 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="rounded-lg bg-red-50 p-2 dark:bg-red-950">
                  <AlertTriangle className="size-5 text-red-600" />
                </div>
                <div>
                  <h3 className="text-sm font-semibold">Delete Role</h3>
                  <p className="text-xs text-muted-foreground">This action cannot be undone.</p>
                </div>
              </div>
              <button onClick={() => setDeleteTarget(null)} className="rounded-md p-1 text-muted-foreground hover:bg-zinc-100 dark:hover:bg-zinc-800">
                <X className="size-4" />
              </button>
            </div>
            <p className="mb-5 text-sm text-muted-foreground">
              Delete <strong className="text-foreground">{deleteTarget.title}</strong>?
            </p>
            {deleteError && (
              <p className="mb-3 rounded-lg bg-red-50 p-2 text-xs text-red-700 dark:bg-red-950 dark:text-red-300">
                {deleteError}
              </p>
            )}
            <div className="flex justify-end gap-3">
              <Button variant="outline" onClick={() => setDeleteTarget(null)} disabled={isDeleting}>
                Cancel
              </Button>
              <Button variant="destructive" onClick={handleDelete} disabled={isDeleting} className="gap-2">
                {isDeleting ? <Loader2 className="size-4 animate-spin" /> : <Trash2 className="size-4" />}
                Delete
              </Button>
            </div>
          </div>
        </div>
      )}
    </Card>
  );
}

function RoleFormFieldsBlock({
  values,
  onChange,
}: {
  values: RoleFormFields;
  onChange: (patch: Partial<RoleFormFields>) => void;
}) {
  return (
    <div className="space-y-4">
      <div>
        <Label htmlFor="role-title">Title</Label>
        <Input
          id="role-title"
          placeholder="e.g. Senior Operations Manager"
          value={values.title}
          onChange={(e) => onChange({ title: e.target.value })}
          className="mt-1.5"
        />
      </div>
      <div>
        <Label htmlFor="role-description">Short description</Label>
        <Input
          id="role-description"
          placeholder="One-line summary shown on the careers page"
          value={values.description}
          onChange={(e) => onChange({ description: e.target.value })}
          className="mt-1.5"
        />
        <p className="mt-1 text-[10px] text-muted-foreground">
          Used on /careers cards. Keep it short — full JD goes below.
        </p>
      </div>

      <div className="rounded-lg border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
        <h5 className="mb-1 text-xs font-semibold uppercase tracking-wide text-zinc-500">
          Job Description
        </h5>
        <p className="mb-3 text-[10px] text-muted-foreground">
          Used by the pre-screening agent to score candidate CVs. Markdown line breaks supported.
        </p>
        <div className="space-y-3">
          <div>
            <Label htmlFor="jd-summary">About this role</Label>
            <Textarea
              id="jd-summary"
              rows={3}
              placeholder="One or two paragraphs describing the role's purpose and impact."
              value={values.jdSummary}
              onChange={(e) => onChange({ jdSummary: e.target.value })}
              className="mt-1.5"
            />
          </div>
          <div>
            <Label htmlFor="jd-responsibilities">Responsibilities</Label>
            <Textarea
              id="jd-responsibilities"
              rows={5}
              placeholder={"• Lead the X workflow\n• Coordinate with Y team\n• Own Z deliverables"}
              value={values.jdResponsibilities}
              onChange={(e) => onChange({ jdResponsibilities: e.target.value })}
              className="mt-1.5"
            />
          </div>
          <div>
            <Label htmlFor="jd-requirements">Requirements (must-have)</Label>
            <Textarea
              id="jd-requirements"
              rows={5}
              placeholder={"• Bachelor's degree in <field>\n• 3+ years in <skill>\n• Proficient in <tool>"}
              value={values.jdRequirements}
              onChange={(e) => onChange({ jdRequirements: e.target.value })}
              className="mt-1.5"
            />
          </div>
          <div>
            <Label htmlFor="jd-nice-to-haves">Nice to have (optional)</Label>
            <Textarea
              id="jd-nice-to-haves"
              rows={3}
              placeholder={"• Experience with <bonus skill>\n• Familiarity with <bonus tool>"}
              value={values.jdNiceToHaves}
              onChange={(e) => onChange({ jdNiceToHaves: e.target.value })}
              className="mt-1.5"
            />
          </div>
          <div>
            <Label htmlFor="jd-years">Years of experience</Label>
            <Input
              id="jd-years"
              placeholder="e.g. 3–5 years"
              value={values.jdYearsExperience}
              onChange={(e) => onChange({ jdYearsExperience: e.target.value })}
              className="mt-1.5"
            />
          </div>
        </div>
      </div>

      <div className="rounded-lg border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
        <h5 className="mb-1 text-xs font-semibold uppercase tracking-wide text-zinc-500">
          Interview scheduling
        </h5>
        <p className="mb-3 text-[10px] text-muted-foreground">
          Optional. Wins over the department&rsquo;s default interviewer when
          HR clicks &ldquo;Schedule interview&rdquo; on a pre-score message.
        </p>
        <Label htmlFor="role-interviewer">Interviewer email (override)</Label>
        <Input
          id="role-interviewer"
          type="email"
          placeholder="e.g. ahmed@janusd.com"
          value={values.interviewerEmail}
          onChange={(e) => onChange({ interviewerEmail: e.target.value })}
          className="mt-1.5"
        />
      </div>
    </div>
  );
}

```