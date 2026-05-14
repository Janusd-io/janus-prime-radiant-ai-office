---
type: source
source_type: laptop
title: DepartmentInterviewerCard
slug: departmentinterviewercard
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/components/admin/DepartmentInterviewerCard.tsx
original_size: 3164
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# DepartmentInterviewerCard

_Extracted from `assessify/src/components/admin/DepartmentInterviewerCard.tsx` on 2026-05-14._

```tsx
"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Loader2, Save, CalendarClock } from "lucide-react";

interface Props {
  departmentId: string;
  initialEmail: string | null;
}

export function DepartmentInterviewerCard({ departmentId, initialEmail }: Props) {
  const [email, setEmail] = useState(initialEmail ?? "");
  const [savedEmail, setSavedEmail] = useState(initialEmail ?? "");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [saved, setSaved] = useState(false);

  const dirty = email.trim() !== (savedEmail ?? "").trim();

  const save = async () => {
    setSaving(true);
    setError(null);
    setSaved(false);
    try {
      const res = await fetch(`/api/admin/departments/${departmentId}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ defaultInterviewer: email }),
      });
      if (!res.ok) {
        const body = (await res.json().catch(() => ({}))) as { error?: string };
        throw new Error(body.error ?? `Save failed (${res.status})`);
      }
      setSavedEmail(email);
      setSaved(true);
      setTimeout(() => setSaved(false), 2000);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Save failed");
    } finally {
      setSaving(false);
    }
  };

  return (
    <Card>
      <CardHeader>
        <div className="flex items-center gap-2">
          <CalendarClock className="size-4 text-muted-foreground" />
          <CardTitle className="text-base">Default interviewer</CardTitle>
        </div>
        <CardDescription>
          Email used when HR clicks &ldquo;Schedule interview&rdquo; on a
          pre-score Slack message. Individual roles can override this on the
          role edit form.
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="flex flex-col gap-3 sm:flex-row sm:items-end">
          <div className="flex-1">
            <Label htmlFor="dept-interviewer">Interviewer email</Label>
            <Input
              id="dept-interviewer"
              type="email"
              placeholder="e.g. ahmed@janusd.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="mt-1.5"
            />
          </div>
          <Button onClick={save} disabled={!dirty || saving} className="gap-2">
            {saving ? (
              <Loader2 className="size-4 animate-spin" />
            ) : (
              <Save className="size-4" />
            )}
            Save
          </Button>
        </div>
        {error && (
          <p className="mt-2 text-xs text-red-600 dark:text-red-400">{error}</p>
        )}
        {saved && (
          <p className="mt-2 text-xs text-emerald-600 dark:text-emerald-400">
            Saved.
          </p>
        )}
      </CardContent>
    </Card>
  );
}

```