---
type: source
source_type: laptop
title: page
slug: page-20
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/admin/setup/page.tsx
original_size: 8340
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# page

_Extracted from `[[assessify|assessify]]/src/app/admin/setup/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
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
import { Loader2, ShieldCheck, AlertTriangle } from "lucide-react";

function getPasswordStrength(pw: string): { label: string; percent: number; color: string } {
  if (!pw) return { label: "", percent: 0, color: "bg-zinc-200" };
  let score = 0;
  if (pw.length >= 8) score++;
  if (pw.length >= 12) score++;
  if (/[A-Z]/.test(pw)) score++;
  if (/[0-9]/.test(pw)) score++;
  if (/[^A-Za-z0-9]/.test(pw)) score++;
  if (score <= 1) return { label: "Weak", percent: 20, color: "bg-red-500" };
  if (score <= 2) return { label: "Fair", percent: 40, color: "bg-orange-500" };
  if (score <= 3) return { label: "Good", percent: 60, color: "bg-amber-500" };
  if (score <= 4) return { label: "Strong", percent: 80, color: "bg-green-500" };
  return { label: "Very Strong", percent: 100, color: "bg-emerald-500" };
}

export default function SetupPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const token = searchParams.get("token") ?? "";

  const [status, setStatus] = useState<"loading" | "invalid" | "form" | "saving" | "success">("loading");
  const [email, setEmail] = useState("");
  const [errorMsg, setErrorMsg] = useState("");
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [formError, setFormError] = useState<string | null>(null);

  useEffect(() => {
    // Canonical "fetch on mount → setState" pattern; React Compiler's
    // set-state-in-effect rule over-flags it. The cascade is bounded
    // (one fetch, no transitive setState chain).
    if (!token) {
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setStatus("invalid");
      setErrorMsg("No invite token provided.");
      return;
    }
    fetch(`/api/admin/setup?token=${encodeURIComponent(token)}`)
      .then((r) => r.json())
      .then((d) => {
        if (d.valid) {
          setEmail(d.email);
          setStatus("form");
        } else {
          setStatus("invalid");
          setErrorMsg(d.reason ?? "Invalid or expired invite.");
        }
      })
      .catch(() => {
        setStatus("invalid");
        setErrorMsg("Network error.");
      });
  }, [token]);

  const strength = getPasswordStrength(password);
  const canSubmit = name.trim() && password.length >= 8 && password === confirmPassword;

  const handleSubmit = async () => {
    if (!canSubmit) return;
    setFormError(null);
    setStatus("saving");
    try {
      const res = await fetch("/api/admin/setup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token, name: name.trim(), password }),
      });
      const data = await res.json();
      if (!res.ok) { setFormError(data.error); setStatus("form"); return; }
      setStatus("success");
      setTimeout(() => router.push("/admin"), 1500);
    } catch {
      setFormError("Network error");
      setStatus("form");
    }
  };

  if (status === "loading") {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 dark:bg-zinc-950">
        <Loader2 className="size-8 animate-spin text-primary" />
      </div>
    );
  }

  if (status === "invalid") {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 p-4 dark:bg-zinc-950">
        <Card className="w-full max-w-md">
          <CardContent className="flex flex-col items-center py-12">
            <div className="rounded-lg bg-red-50 p-3 dark:bg-red-950">
              <AlertTriangle className="size-8 text-red-600" />
            </div>
            <h2 className="mt-4 text-lg font-semibold">Invalid Invite</h2>
            <p className="mt-2 text-center text-sm text-muted-foreground">{errorMsg}</p>
            <p className="mt-4 text-xs text-muted-foreground">Please ask your admin to resend the invitation.</p>
          </CardContent>
        </Card>
      </div>
    );
  }

  if (status === "success") {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 p-4 dark:bg-zinc-950">
        <Card className="w-full max-w-md">
          <CardContent className="flex flex-col items-center py-12">
            <div className="rounded-lg bg-emerald-50 p-3 dark:bg-emerald-950">
              <ShieldCheck className="size-8 text-emerald-600" />
            </div>
            <h2 className="mt-4 text-lg font-semibold">Account Created</h2>
            <p className="mt-2 text-sm text-muted-foreground">Redirecting to the dashboard...</p>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 p-4 dark:bg-zinc-950">
      <Card className="w-full max-w-md">
        <CardHeader className="text-center">
          <div className="mx-auto mb-2 rounded-lg bg-primary/10 p-3">
            <ShieldCheck className="size-6 text-primary" />
          </div>
          <CardTitle>Set Up Your Account</CardTitle>
          <CardDescription>Complete your profile to access Assessify.</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div>
              <Label>Email</Label>
              <Input value={email} disabled className="mt-1.5 bg-zinc-50 dark:bg-zinc-800/50" />
            </div>

            <div>
              <Label htmlFor="setup-name">Full Name</Label>
              <Input
                id="setup-name"
                placeholder="Your full name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="mt-1.5"
              />
            </div>

            <div>
              <Label htmlFor="setup-password">Password</Label>
              <Input
                id="setup-password"
                type="password"
                placeholder="Minimum 8 characters"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="mt-1.5"
              />
              {password && (
                <div className="mt-2">
                  <div className="flex items-center justify-between text-[10px]">
                    <span className="text-muted-foreground">Strength</span>
                    <span className="font-medium">{strength.label}</span>
                  </div>
                  <div className="mt-1 h-1.5 w-full rounded-full bg-zinc-200 dark:bg-zinc-800">
                    <div
                      className={`h-full rounded-full transition-all ${strength.color}`}
                      style={{ width: `${strength.percent}%` }}
                    />
                  </div>
                </div>
              )}
            </div>

            <div>
              <Label htmlFor="setup-confirm">Confirm Password</Label>
              <Input
                id="setup-confirm"
                type="password"
                placeholder="Re-enter password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                className="mt-1.5"
              />
              {confirmPassword && password !== confirmPassword && (
                <p className="mt-1 text-xs text-red-600">Passwords do not match.</p>
              )}
            </div>

            {formError && (
              <p className="rounded-lg bg-red-50 p-2 text-xs text-red-700 dark:bg-red-950 dark:text-red-300">
                {formError}
              </p>
            )}

            <Button
              onClick={handleSubmit}
              disabled={!canSubmit || status === "saving"}
              className="w-full gap-2"
            >
              {status === "saving" ? <Loader2 className="size-4 animate-spin" /> : <ShieldCheck className="size-4" />}
              Create Account
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

```