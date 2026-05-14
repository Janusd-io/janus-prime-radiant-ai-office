---
type: source
source_type: laptop
title: page
slug: page-3
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/forms/[code]/page.tsx"
original_size: 56683
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# page

_Extracted from `[[assessify|assessify]]/src/app/forms/[code]/page.tsx` on 2026-05-14._

```tsx
"use client";

import { useEffect, useState, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
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
import { COUNTRIES } from "@/lib/countries";
import { LANGUAGES } from "@/lib/languages";
import {
  Loader2,
  ArrowRight,
  FileText,
  CheckCircle,
  Upload,
  X,
  Plus,
  Trash2,
  AlertTriangle,
  Sparkles,
  Save,
} from "lucide-react";

// ─── Types ──────────────────────────────────────────────────

interface FormInviteData {
  invite: {
    id: string;
    code: string;
    employeeName: string;
    employeeEmail: string;
    region: string;
    status: string;
    submissionId: string | null;
  };
  form: {
    id: string;
    name: string;
    slug: string;
    description: string;
    formType: string;
    fields: Array<{
      name: string;
      label: string;
      type: string;
      required: boolean;
      placeholder: string;
      options: string[];
      optionLabels?: Record<string, string>;
      section: string;
    }> | null;
  };
  fileRules: {
    formats: string[];
    mimeTypes: string[];
    label: string;
  };
}

type Step = "welcome" | "form" | "submitted";

// ─── Reusable Components ────────────────────────────────────

function FormSection({
  title,
  description,
  step,
  children,
}: {
  title: string;
  description?: string;
  step?: number;
  children: React.ReactNode;
}) {
  return (
    <motion.section
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-2xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-900"
    >
      <div className="mb-5 flex items-center gap-3">
        {step && (
          <span className="flex h-7 w-7 items-center justify-center rounded-full bg-primary/10 text-xs font-bold text-primary">
            {step}
          </span>
        )}
        <div>
          <h3 className="text-base font-semibold">{title}</h3>
          {description && (
            <p className="text-xs text-muted-foreground">{description}</p>
          )}
        </div>
      </div>
      {children}
    </motion.section>
  );
}

function FormField({
  label,
  required = false,
  error = false,
  children,
}: {
  label: string;
  required?: boolean;
  error?: boolean;
  children: React.ReactNode;
}) {
  return (
    <div data-field-error={error || undefined}>
      <Label className={`mb-1.5 block text-sm transition-colors ${error ? "text-red-600 dark:text-red-400" : ""}`}>
        {label}
        {required && <span className="ml-0.5 text-red-500">*</span>}
      </Label>
      <div className={error ? "[&_input]:border-red-500 [&_input]:focus-visible:border-red-500 [&_input]:focus-visible:ring-red-500/30 [&_[data-slot=select-trigger]]:border-red-500 [&_[data-slot=select-trigger]]:ring-red-500/30" : ""}>
        {children}
      </div>
      {error && <p className="mt-1 text-[10px] font-medium text-red-500">This field is required</p>}
    </div>
  );
}

// ─── Main Page ──────────────────────────────────────────────

export default function FormPage({
  params,
}: {
  params: Promise<{ code: string }>;
}) {
  const [code, setCode] = useState("");
  const [data, setData] = useState<FormInviteData | null>(null);
  const [submissionId, setSubmissionId] = useState<string | null>(null);
  const [step, setStep] = useState<Step>("welcome");
  // Free-form form-data bag: each field's runtime type depends on the dynamic
  // FormTemplate.fields config and is checked at submission time. `any` is the
  // honest type here — narrowing per-access would be 100+ casts of `formValues.x`
  // back to string for every <Input value=...>.
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const [formValues, setFormValues] = useState<Record<string, any>>({});
  const [files, setFiles] = useState<{ file: File; fieldName: string }[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isSaving, setIsSaving] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [fileError, setFileError] = useState<string | null>(null);
  const [sameAsNextOfKin, setSameAsNextOfKin] = useState(false);

  // Dynamic arrays — entries are loose key/value bags built up by the user
  // form. Same rationale as formValues above for keeping `any`.
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  type DynamicRow = Record<string, any>;
  const [children, setChildren] = useState<DynamicRow[]>([]);
  const [education, setEducation] = useState<DynamicRow[]>([]);
  const [qualifications, setQualifications] = useState<DynamicRow[]>([]);
  const [languages, setLanguages] = useState<DynamicRow[]>([]);

  useEffect(() => {
    params.then((p) => {
      setCode(p.code);
      fetch(`/api/forms/invite/${p.code}`)
        .then((r) => r.json())
        .then((d) => {
          if (d.error) { setError(d.error); setIsLoading(false); return; }
          setData(d);
          if (d.invite.status === "submitted") setStep("submitted");
          setIsLoading(false);
        })
        .catch(() => { setError("Failed to load form."); setIsLoading(false); });
    });
  }, [params]);

  const handleStart = async () => {
    if (!data) return;
    setIsLoading(true);

    if (data.invite.submissionId) {
      setSubmissionId(data.invite.submissionId);
      try {
        const res = await fetch(`/api/forms/${data.invite.submissionId}`);
        const d = await res.json();
        if (d.submission?.formData) {
          setFormValues(d.submission.formData);
          if (d.submission.formData.children) setChildren(d.submission.formData.children);
          if (d.submission.formData.education) setEducation(d.submission.formData.education);
          if (d.submission.formData.qualifications) setQualifications(d.submission.formData.qualifications);
          if (d.submission.formData.languages) setLanguages(d.submission.formData.languages);
        }
      } catch { /* ignore */ }
      setStep("form");
      setIsLoading(false);
      return;
    }

    try {
      const res = await fetch(`/api/forms/invite/${code}/start`, { method: "POST" });
      const d = await res.json();
      if (d.submissionId) { setSubmissionId(d.submissionId); setStep("form"); }
    } catch { setError("Failed to start form."); }
    setIsLoading(false);
  };

  // value is whatever the dynamic field renders — string most often, but
  // also array (multi-select), boolean, or nested object for the dynamic rows.
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const updateField = (name: string, value: any) => {
    setFormValues((prev) => ({ ...prev, [name]: value }));
    // Clear error for this field when user starts filling it
    if (errorFields.has(name) && value?.trim?.()) {
      setErrorFields((prev) => { const next = new Set(prev); next.delete(name); return next; });
    }
  };

  const validateFile = (f: File): string | null => {
    if (!data) return null;
    if (!data.fileRules.mimeTypes.includes(f.type)) {
      return `Invalid format: ${f.name}. Accepted: ${data.fileRules.label}`;
    }
    if (f.size > 1 * 1024 * 1024) return `File too large: ${f.name}. Maximum 1MB.`;
    return null;
  };

  const handleFileAdd = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!e.target.files || !data) return;
    setFileError(null);
    const newFiles = Array.from(e.target.files);
    for (const f of newFiles) {
      const err = validateFile(f);
      if (err) { setFileError(err); return; }
    }
    setFiles((prev) => [...prev, ...newFiles.map((f) => ({ file: f, fieldName: "attachment" }))]);
    e.target.value = "";
  };

  // Per-field file upload (recruitment forms etc.). Single-file slot per field —
  // a fresh upload replaces any prior file tagged with the same fieldName.
  const handleFieldFile = (fieldName: string, e: React.ChangeEvent<HTMLInputElement>) => {
    if (!e.target.files || !data) return;
    setFileError(null);
    const newFile = e.target.files[0];
    if (!newFile) return;
    const err = validateFile(newFile);
    if (err) { setFileError(err); return; }
    setFiles((prev) => [
      ...prev.filter((p) => p.fieldName !== fieldName),
      { file: newFile, fieldName },
    ]);
    if (errorFields.has(fieldName)) {
      setErrorFields((prev) => { const next = new Set(prev); next.delete(fieldName); return next; });
    }
    e.target.value = "";
  };

  const removeFieldFile = (fieldName: string) => {
    setFiles((prev) => prev.filter((p) => p.fieldName !== fieldName));
  };

  const saveDraft = useCallback(async () => {
    if (!submissionId) return;
    setIsSaving(true);
    const fullData = { ...formValues, children, education, qualifications, languages, emergencyContactSameAsNextOfKin: sameAsNextOfKin };
    await fetch(`/api/forms/${submissionId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ formData: fullData }),
    }).catch(() => {});
    setIsSaving(false);
  }, [submissionId, formValues, children, education, qualifications, languages, sameAsNextOfKin]);

  useEffect(() => {
    if (step !== "form" || !submissionId) return;
    const interval = setInterval(saveDraft, 30000);
    return () => clearInterval(interval);
  }, [step, submissionId, saveDraft]);

  const [errorFields, setErrorFields] = useState<Set<string>>(new Set());

  const hasError = (fieldName: string) => errorFields.has(fieldName);

  const validateForm = (): string[] => {
    const errors: string[] = [];
    const fields: string[] = [];
    const isPersonal = data?.form.formType === "personal_data";
    const isBank = data?.form.formType === "bank_details";

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    const check = (field: string, label: string) => {
      if (!formValues[field]?.trim()) { errors.push(label); fields.push(field); }
    };

    if (isPersonal) {
      check("firstName", "First Name");
      check("surname", "Surname");
      check("nationality", "Nationality");
      check("dateOfBirth", "Date of Birth");
      check("personalEmail", "Personal Email");
      check("mobilePhone", "Mobile Phone");
      check("fatherName", "Father's Name");
      check("motherName", "Mother's Name");
      check("nextOfKinName", "Next of Kin — Name");
      check("nextOfKinRelationship", "Next of Kin — Relationship");
      check("nextOfKinAddress", "Next of Kin — Address");
      check("nextOfKinMobilePhone", "Next of Kin — Mobile Phone");
      if (!sameAsNextOfKin) {
        check("emergencyContactName", "Emergency Contact — Name");
        check("emergencyContactRelationship", "Emergency Contact — Relationship");
        check("emergencyContactAddress", "Emergency Contact — Address");
        check("emergencyContactMobilePhone", "Emergency Contact — Mobile Phone");
      }
    } else if (isBank) {
      check("bankName", "Bank Name");
      check("branchLocation", "Branch / Location");
      check("accountName", "Account Name");
      check("accountNo", "Account Number");
      check("iban", "IBAN");
      check("swiftCode", "SWIFT Code");
    }

    // Custom form validation — covers any form driven by `data.form.fields`
    // (custom + recruitment_intake_*).
    const fieldsArray = data?.form.fields;
    const isFieldsDriven =
      Array.isArray(fieldsArray) &&
      data?.form.formType !== "personal_data" &&
      data?.form.formType !== "bank_details";
    if (isFieldsDriven && fieldsArray) {
      for (const f of fieldsArray) {
        if (f.type === "heading") continue;
        if (f.required && f.type === "file") {
          if (!files.some((p) => p.fieldName === f.name)) {
            errors.push(`${f.label} (file required)`);
            fields.push(f.name);
          }
          continue;
        }
        if (f.required) check(f.name, f.label);
        if (f.type === "email" && formValues[f.name]?.trim() && !emailRegex.test(formValues[f.name].trim())) {
          errors.push(`${f.label} — invalid format`);
          fields.push(f.name);
        }
      }
    }

    // Email format validation (built-in forms)
    if (formValues.personalEmail?.trim() && !emailRegex.test(formValues.personalEmail.trim())) {
      errors.push("Personal Email — invalid format");
      fields.push("personalEmail");
    }

    setErrorFields(new Set(fields));
    return errors;
  };

  const handleSubmit = async () => {
    if (!submissionId || !data) return;

    const errors = validateForm();
    if (errors.length > 0) {
      setError(`Please complete ${errors.length} required field${errors.length > 1 ? "s" : ""} before submitting.`);
      // Scroll to first error field
      const firstErrorField = document.querySelector("[data-field-error=true]");
      if (firstErrorField) {
        firstErrorField.scrollIntoView({ behavior: "smooth", block: "center" });
      } else {
        window.scrollTo({ top: 0, behavior: "smooth" });
      }
      return;
    }
    setIsSubmitting(true);
    setError(null);

    // Convert files to base64 for direct webhook delivery (no server storage)
    type FilePayload = {
      fileName: string;
      fileType: string;
      fileSize: number;
      fieldName: string;
      base64Data: string;
    };
    const filePayloads: FilePayload[] = [];
    for (const { file, fieldName } of files) {
      const buffer = await file.arrayBuffer();
      const base64 = btoa(
        new Uint8Array(buffer).reduce((data, byte) => data + String.fromCharCode(byte), "")
      );
      filePayloads.push({
        fileName: file.name,
        fileType: file.type,
        fileSize: file.size,
        fieldName,
        base64Data: base64,
      });
    }

    const fullData = { ...formValues, children, education, qualifications, languages, emergencyContactSameAsNextOfKin: sameAsNextOfKin };
    const res = await fetch(`/api/forms/${submissionId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ formData: fullData, files: filePayloads, submit: true }),
    });

    if (res.ok) { setStep("submitted"); } else { setError("Failed to submit form. Please try again."); }
    setIsSubmitting(false);
  };

  // ─── Loading / Error ─────────────────────────────────────

  if (isLoading) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <Loader2 className="size-8 animate-spin text-primary" />
      </div>
    );
  }

  if (error && step === "welcome") {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 px-4 dark:bg-zinc-950">
        <div className="max-w-sm text-center">
          <AlertTriangle className="mx-auto mb-4 size-12 text-red-500" />
          <h1 className="mb-2 text-xl font-bold">Unable to Load Form</h1>
          <p className="text-sm text-muted-foreground">{error}</p>
        </div>
      </div>
    );
  }

  if (!data) return null;

  // ─── Submitted ───────────────────────────────────────────

  if (step === "submitted") {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 px-4 dark:bg-zinc-950">
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="max-w-md text-center">
          <div className="mx-auto mb-6 flex h-20 w-20 items-center justify-center rounded-full bg-green-100 dark:bg-green-950">
            <CheckCircle className="size-10 text-green-600" />
          </div>
          <h1 className="mb-3 text-2xl font-bold tracking-tight">Form Submitted</h1>
          <p className="text-muted-foreground">
            Thank you, {data.invite.employeeName}. Your {data.form.name.toLowerCase()} has
            been submitted successfully. HR will review it shortly.
          </p>
        </motion.div>
      </div>
    );
  }

  // ─── Welcome ─────────────────────────────────────────────

  if (step === "welcome") {
    return (
      <div className="flex min-h-screen items-center justify-center bg-zinc-50 px-4 dark:bg-zinc-950">
        <motion.div initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} className="w-full max-w-md">
          <div className="mb-8 text-center">
            <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-primary/10">
              <FileText className="size-7 text-primary" />
            </div>
            <h1 className="text-2xl font-bold tracking-tight">Welcome, {data.invite.employeeName}</h1>
            <p className="mt-1 text-sm text-muted-foreground">Please complete the following form</p>
          </div>
          <div className="rounded-2xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-900">
            <h2 className="text-lg font-semibold">{data.form.name}</h2>
            {data.form.description && <p className="mt-1 text-sm text-muted-foreground">{data.form.description}</p>}
            <div className="mt-4 space-y-2">
              <div className="flex items-center gap-2 rounded-lg bg-zinc-50 px-3 py-2 dark:bg-zinc-800/50">
                <span className="text-xs text-muted-foreground">Region:</span>
                <span className="text-xs font-medium">{data.invite.region === "uae" ? "UAE" : "Global"}</span>
              </div>
              <div className="flex items-center gap-2 rounded-lg bg-zinc-50 px-3 py-2 dark:bg-zinc-800/50">
                <span className="text-xs text-muted-foreground">Accepted files:</span>
                <span className="text-xs font-medium">{data.fileRules.label}</span>
              </div>
              <div className="flex items-center gap-2 rounded-lg bg-zinc-50 px-3 py-2 dark:bg-zinc-800/50">
                <span className="text-xs text-muted-foreground">Auto-save:</span>
                <span className="text-xs font-medium">Your progress is saved automatically</span>
              </div>
            </div>
            <Button onClick={handleStart} className="mt-5 w-full gap-2" size="lg">
              Get Started <ArrowRight className="size-4" />
            </Button>
          </div>
        </motion.div>
      </div>
    );
  }

  // ─── Form ────────────────────────────────────────────────

  const isPersonalData = data.form.formType === "personal_data";
  const isBankDetails = data.form.formType === "bank_details";
  // "Custom" = anything driven by `data.form.fields` (custom + recruitment_intake_*).
  // The two legacy fixed-shape forms (personal_data / bank_details) hardcode their
  // own UI and don't have a fields array.
  const isCustom = !isPersonalData && !isBankDetails && Array.isArray(data.form.fields) && data.form.fields.length > 0;
  const hasExplicitFileFields = isCustom && data.form.fields!.some((f) => f.type === "file");

  return (
    <div className="min-h-screen bg-zinc-50 dark:bg-zinc-950">
      {/* Header */}
      <div className="sticky top-0 z-50 border-b border-zinc-200 bg-white/80 backdrop-blur-lg dark:border-zinc-800 dark:bg-zinc-950/80">
        <div className="mx-auto flex max-w-3xl items-center justify-between px-4 py-3">
          <div className="flex items-center gap-3">
            <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-primary/10">
              <FileText className="size-4 text-primary" />
            </div>
            <div>
              <p className="text-xs text-muted-foreground">{data.form.name}</p>
              <p className="text-sm font-semibold">{data.invite.employeeName}</p>
            </div>
          </div>
          <Button variant="outline" onClick={saveDraft} disabled={isSaving} className="gap-2">
            {isSaving ? <Loader2 className="size-3 animate-spin" /> : <Save className="size-3" />}
            {isSaving ? "Saving..." : "Save Draft"}
          </Button>
        </div>
      </div>

      <div className="mx-auto max-w-3xl px-4 py-8">
        <div className="space-y-6">
          {isPersonalData && (
            <>
              {/* Step 1: Personal Information */}
              <FormSection title="Personal Information" description="Basic details about yourself" step={1}>
                <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                  <FormField label="Title">
                    <Select value={formValues.title ?? ""} onValueChange={(v) => updateField("title", v)}>
                      <SelectTrigger className="w-full"><SelectValue placeholder="Select title" /></SelectTrigger>
                      <SelectContent>
                        {["Mr", "Mrs", "Ms", "Dr", "Prof"].map((t) => (
                          <SelectItem key={t} value={t}>{t}</SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                  </FormField>
                  <FormField label="First Name" required error={hasError("firstName")}>
                    <Input value={formValues.firstName ?? ""} onChange={(e) => updateField("firstName", e.target.value)} placeholder="Enter your first name" />
                  </FormField>
                  <FormField label="Preferred Name">
                    <Input value={formValues.preferredName ?? ""} onChange={(e) => updateField("preferredName", e.target.value)} placeholder="What should we call you?" />
                  </FormField>
                  <FormField label="Surname" required error={hasError("surname")}>
                    <Input value={formValues.surname ?? ""} onChange={(e) => updateField("surname", e.target.value)} placeholder="Enter your surname" />
                  </FormField>
                  <FormField label="Other Surname">
                    <Input value={formValues.otherSurname ?? ""} onChange={(e) => updateField("otherSurname", e.target.value)} placeholder="If applicable" />
                  </FormField>
                  <FormField label="Nationality" required error={hasError("nationality")}>
                    <Select value={formValues.nationality ?? ""} onValueChange={(v) => updateField("nationality", v)}>
                      <SelectTrigger className="w-full"><SelectValue placeholder="Select your nationality" /></SelectTrigger>
                      <SelectContent>
                        {COUNTRIES.map((c) => (
                          <SelectItem key={c.code} value={c.name}>{c.name}</SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                  </FormField>
                  <FormField label="Place of Birth">
                    <Input value={formValues.placeOfBirth ?? ""} onChange={(e) => updateField("placeOfBirth", e.target.value)} placeholder="City, Country" />
                  </FormField>
                  <FormField label="Date of Birth" required error={hasError("dateOfBirth")}>
                    <Input type="date" value={formValues.dateOfBirth ?? ""} onChange={(e) => updateField("dateOfBirth", e.target.value)} />
                  </FormField>
                  <FormField label="Marital Status">
                    <Select value={formValues.maritalStatus ?? ""} onValueChange={(v) => updateField("maritalStatus", v)}>
                      <SelectTrigger className="w-full"><SelectValue placeholder="Select status" /></SelectTrigger>
                      <SelectContent>
                        {["Single", "Married", "Divorced", "Widowed"].map((s) => (
                          <SelectItem key={s} value={s}>{s}</SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                  </FormField>
                  <FormField label="Religion">
                    <Input value={formValues.religion ?? ""} onChange={(e) => updateField("religion", e.target.value)} placeholder="Optional" />
                  </FormField>
                  <FormField label="Personal Email" required error={hasError("personalEmail")}>
                    <Input type="email" value={formValues.personalEmail ?? ""} onChange={(e) => updateField("personalEmail", e.target.value)} placeholder="your@email.com" />
                  </FormField>
                  <FormField label="Mobile Phone" required error={hasError("mobilePhone")}>
                    <Input type="tel" value={formValues.mobilePhone ?? ""} onChange={(e) => updateField("mobilePhone", e.target.value)} placeholder="+971 50 000 0000" />
                  </FormField>
                  <FormField label="Home Phone">
                    <Input type="tel" value={formValues.homePhone ?? ""} onChange={(e) => updateField("homePhone", e.target.value)} placeholder="Optional" />
                  </FormField>
                </div>
              </FormSection>

              {/* Step 2: Address */}
              <FormSection title="Address" description="Your current residential details" step={2}>
                <div className="grid grid-cols-1 gap-4">
                  <FormField label="Physical Address">
                    <Input value={formValues.physicalAddress ?? ""} onChange={(e) => updateField("physicalAddress", e.target.value)} placeholder="Full residential address" />
                  </FormField>
                  <FormField label="Overseas Address">
                    <Input value={formValues.overseasAddress ?? ""} onChange={(e) => updateField("overseasAddress", e.target.value)} placeholder="If applicable" />
                  </FormField>
                  <div className="sm:w-1/2">
                    <FormField label="Overseas Phone">
                      <Input type="tel" value={formValues.overseasHomePhone ?? ""} onChange={(e) => updateField("overseasHomePhone", e.target.value)} placeholder="Optional" />
                    </FormField>
                  </div>
                </div>
              </FormSection>

              {/* Step 3: Family */}
              <FormSection title="Family Details" description="Family and dependant information" step={3}>
                <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                  <FormField label="Father's Name" required error={hasError("fatherName")}>
                    <Input value={formValues.fatherName ?? ""} onChange={(e) => updateField("fatherName", e.target.value)} />
                  </FormField>
                  <FormField label="Mother's Name" required error={hasError("motherName")}>
                    <Input value={formValues.motherName ?? ""} onChange={(e) => updateField("motherName", e.target.value)} />
                  </FormField>
                  <FormField label="Spouse Name">
                    <Input value={formValues.spouseName ?? ""} onChange={(e) => updateField("spouseName", e.target.value)} placeholder="If applicable" />
                  </FormField>
                  <FormField label="Spouse Date of Birth">
                    <Input type="date" value={formValues.spouseDateOfBirth ?? ""} onChange={(e) => updateField("spouseDateOfBirth", e.target.value)} />
                  </FormField>
                </div>

                {/* Children */}
                <div className="mt-6">
                  <div className="mb-3 flex items-center justify-between">
                    <p className="text-sm font-medium">Children</p>
                    <Button variant="outline" onClick={() => setChildren([...children, { name: "", gender: "", dateOfBirth: "" }])} className="gap-1.5 text-xs">
                      <Plus className="size-3" /> Add Child
                    </Button>
                  </div>
                  <AnimatePresence>
                    {children.map((child, i) => (
                      <motion.div key={i} initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: "auto" }} exit={{ opacity: 0, height: 0 }} className="mb-2 overflow-hidden">
                        <div className="flex items-center gap-2 rounded-xl bg-zinc-50 p-3 dark:bg-zinc-800/50">
                          <span className="flex h-6 w-6 items-center justify-center rounded-full bg-primary/10 text-[10px] font-bold text-primary">{i + 1}</span>
                          <Input placeholder="Child's name" value={child.name} onChange={(e) => { const u = [...children]; u[i] = { ...u[i], name: e.target.value }; setChildren(u); }} className="flex-1" />
                          <Select value={child.gender} onValueChange={(v) => { const u = [...children]; u[i] = { ...u[i], gender: v }; setChildren(u); }}>
                            <SelectTrigger className="w-28"><SelectValue placeholder="Gender" /></SelectTrigger>
                            <SelectContent>
                              <SelectItem value="Male">Male</SelectItem>
                              <SelectItem value="Female">Female</SelectItem>
                            </SelectContent>
                          </Select>
                          <Input type="date" value={child.dateOfBirth} onChange={(e) => { const u = [...children]; u[i] = { ...u[i], dateOfBirth: e.target.value }; setChildren(u); }} className="w-36" />
                          <button onClick={() => setChildren(children.filter((_, j) => j !== i))} className="rounded-md p-1.5 text-zinc-400 transition-colors hover:bg-red-50 hover:text-red-500">
                            <Trash2 className="size-3.5" />
                          </button>
                        </div>
                      </motion.div>
                    ))}
                  </AnimatePresence>
                  {children.length === 0 && <p className="text-xs text-muted-foreground">No children added.</p>}
                </div>
              </FormSection>

              {/* Step 4: Education */}
              <FormSection title="Education" description="Your academic background" step={4}>
                <div className="mb-3 flex justify-end">
                  <Button variant="outline" onClick={() => setEducation([...education, { university: "", startDate: "", endDate: "", degreeType: "", majorSubject: "", gradeGpa: "" }])} className="gap-1.5 text-xs">
                    <Plus className="size-3" /> Add Education
                  </Button>
                </div>
                <AnimatePresence>
                  {education.map((edu, i) => (
                    <motion.div key={i} initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, height: 0 }} className="mb-3 overflow-hidden">
                      <div className="rounded-xl border border-zinc-100 bg-zinc-50/50 p-4 dark:border-zinc-800 dark:bg-zinc-800/30">
                        <div className="mb-3 flex items-center justify-between">
                          <span className="text-xs font-semibold text-primary">Education #{i + 1}</span>
                          <button onClick={() => setEducation(education.filter((_, j) => j !== i))} className="rounded-md p-1 text-zinc-400 hover:text-red-500"><Trash2 className="size-3.5" /></button>
                        </div>
                        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
                          <Input placeholder="University / Institution" value={edu.university} onChange={(e) => { const u = [...education]; u[i] = { ...u[i], university: e.target.value }; setEducation(u); }} />
                          <Input placeholder="Degree Type (e.g. BSc, MSc)" value={edu.degreeType} onChange={(e) => { const u = [...education]; u[i] = { ...u[i], degreeType: e.target.value }; setEducation(u); }} />
                          <Input placeholder="Major / Subject" value={edu.majorSubject} onChange={(e) => { const u = [...education]; u[i] = { ...u[i], majorSubject: e.target.value }; setEducation(u); }} />
                          <Input placeholder="GPA" value={edu.gradeGpa} onChange={(e) => { const u = [...education]; u[i] = { ...u[i], gradeGpa: e.target.value }; setEducation(u); }} />
                          <div>
                            <label className="mb-1 block text-[10px] text-muted-foreground">Start Date</label>
                            <Input type="date" value={edu.startDate} onChange={(e) => { const u = [...education]; u[i] = { ...u[i], startDate: e.target.value }; setEducation(u); }} />
                          </div>
                          <div>
                            <label className="mb-1 block text-[10px] text-muted-foreground">End Date</label>
                            <Input type="date" value={edu.endDate} onChange={(e) => { const u = [...education]; u[i] = { ...u[i], endDate: e.target.value }; setEducation(u); }} />
                          </div>
                        </div>
                      </div>
                    </motion.div>
                  ))}
                </AnimatePresence>
                {education.length === 0 && <p className="text-xs text-muted-foreground">No education entries added yet.</p>}
              </FormSection>

              {/* Step 5: Languages */}
              <FormSection title="Language Proficiency" description="What languages do you speak?" step={5}>
                <div className="mb-3 flex justify-end">
                  <Button variant="outline" onClick={() => setLanguages([...languages, { language: "", level: "" }])} className="gap-1.5 text-xs">
                    <Plus className="size-3" /> Add Language
                  </Button>
                </div>
                <AnimatePresence>
                  {languages.map((lang, i) => (
                    <motion.div key={i} initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, height: 0 }} className="mb-2 overflow-hidden">
                      <div className="flex items-center gap-2 rounded-xl bg-zinc-50 p-3 dark:bg-zinc-800/50">
                        <Select value={lang.language} onValueChange={(v) => { const u = [...languages]; u[i] = { ...u[i], language: v }; setLanguages(u); }}>
                          <SelectTrigger className="flex-1"><SelectValue placeholder="Select language" /></SelectTrigger>
                          <SelectContent>
                            {LANGUAGES.map((l) => (
                              <SelectItem key={l} value={l}>{l}</SelectItem>
                            ))}
                          </SelectContent>
                        </Select>
                        <Select value={lang.level} onValueChange={(v) => { const u = [...languages]; u[i] = { ...u[i], level: v }; setLanguages(u); }}>
                          <SelectTrigger className="w-40"><SelectValue placeholder="Proficiency" /></SelectTrigger>
                          <SelectContent>
                            {["Basic", "Intermediate", "Fluent", "Native"].map((l) => <SelectItem key={l} value={l}>{l}</SelectItem>)}
                          </SelectContent>
                        </Select>
                        <button onClick={() => setLanguages(languages.filter((_, j) => j !== i))} className="rounded-md p-1.5 text-zinc-400 hover:text-red-500"><Trash2 className="size-3.5" /></button>
                      </div>
                    </motion.div>
                  ))}
                </AnimatePresence>
                {languages.length === 0 && <p className="text-xs text-muted-foreground">No languages added yet.</p>}
              </FormSection>

              {/* Step 6: Next of Kin + Emergency Contact */}
              <FormSection title="Next of Kin" description="Required for emergency and legal purposes" step={6}>
                <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                  <FormField label="Full Name" required error={hasError("nextOfKinName")}>
                    <Input value={formValues.nextOfKinName ?? ""} onChange={(e) => updateField("nextOfKinName", e.target.value)} />
                  </FormField>
                  <FormField label="Relationship" required error={hasError("nextOfKinRelationship")}>
                    <Select value={formValues.nextOfKinRelationship ?? ""} onValueChange={(v) => updateField("nextOfKinRelationship", v)}>
                      <SelectTrigger className="w-full"><SelectValue placeholder="Select relationship" /></SelectTrigger>
                      <SelectContent>
                        {["Spouse", "Parent", "Sibling", "Child", "Relative", "Friend", "Other"].map((r) => <SelectItem key={r} value={r}>{r}</SelectItem>)}
                      </SelectContent>
                    </Select>
                  </FormField>
                  <div className="sm:col-span-2">
                    <FormField label="Address" required error={hasError("nextOfKinAddress")}>
                      <Input value={formValues.nextOfKinAddress ?? ""} onChange={(e) => updateField("nextOfKinAddress", e.target.value)} />
                    </FormField>
                  </div>
                  <FormField label="Home Phone">
                    <Input type="tel" value={formValues.nextOfKinHomePhone ?? ""} onChange={(e) => updateField("nextOfKinHomePhone", e.target.value)} />
                  </FormField>
                  <FormField label="Mobile Phone" required error={hasError("nextOfKinMobilePhone")}>
                    <Input type="tel" value={formValues.nextOfKinMobilePhone ?? ""} onChange={(e) => updateField("nextOfKinMobilePhone", e.target.value)} />
                  </FormField>
                </div>

                {/* Emergency Contact */}
                <div className="mt-6 border-t border-zinc-100 pt-6 dark:border-zinc-800">
                  <div className="mb-4 flex items-center justify-between">
                    <div>
                      <p className="text-sm font-semibold">Emergency Contact</p>
                      <p className="text-xs text-muted-foreground">Who should we contact in an emergency?</p>
                    </div>
                    <Button
                      variant={sameAsNextOfKin ? "default" : "outline"}
                      onClick={() => {
                        setSameAsNextOfKin(!sameAsNextOfKin);
                        if (!sameAsNextOfKin) {
                          updateField("emergencyContactName", formValues.nextOfKinName ?? "");
                          updateField("emergencyContactRelationship", formValues.nextOfKinRelationship ?? "");
                          updateField("emergencyContactAddress", formValues.nextOfKinAddress ?? "");
                          updateField("emergencyContactHomePhone", formValues.nextOfKinHomePhone ?? "");
                          updateField("emergencyContactMobilePhone", formValues.nextOfKinMobilePhone ?? "");
                        }
                      }}
                      className="gap-1.5 text-xs"
                    >
                      <CheckCircle className="size-3" />
                      Same as Next of Kin
                    </Button>
                  </div>

                  <AnimatePresence>
                    {!sameAsNextOfKin && (
                      <motion.div initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: "auto" }} exit={{ opacity: 0, height: 0 }} className="overflow-hidden">
                        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                          <FormField label="Full Name" required error={hasError("emergencyContactName")}>
                            <Input value={formValues.emergencyContactName ?? ""} onChange={(e) => updateField("emergencyContactName", e.target.value)} />
                          </FormField>
                          <FormField label="Relationship" required error={hasError("emergencyContactRelationship")}>
                            <Select value={formValues.emergencyContactRelationship ?? ""} onValueChange={(v) => updateField("emergencyContactRelationship", v)}>
                              <SelectTrigger className="w-full"><SelectValue placeholder="Select relationship" /></SelectTrigger>
                              <SelectContent>
                                {["Spouse", "Parent", "Sibling", "Child", "Relative", "Friend", "Other"].map((r) => <SelectItem key={r} value={r}>{r}</SelectItem>)}
                              </SelectContent>
                            </Select>
                          </FormField>
                          <div className="sm:col-span-2">
                            <FormField label="Address" required error={hasError("emergencyContactAddress")}>
                              <Input value={formValues.emergencyContactAddress ?? ""} onChange={(e) => updateField("emergencyContactAddress", e.target.value)} />
                            </FormField>
                          </div>
                          <FormField label="Home Phone">
                            <Input type="tel" value={formValues.emergencyContactHomePhone ?? ""} onChange={(e) => updateField("emergencyContactHomePhone", e.target.value)} />
                          </FormField>
                          <FormField label="Mobile Phone" required error={hasError("emergencyContactMobilePhone")}>
                            <Input type="tel" value={formValues.emergencyContactMobilePhone ?? ""} onChange={(e) => updateField("emergencyContactMobilePhone", e.target.value)} />
                          </FormField>
                        </div>
                      </motion.div>
                    )}
                  </AnimatePresence>
                </div>
              </FormSection>

              {/* Step 7: Previous Employment */}
              <FormSection title="Previous Employment" description="Your most recent employer" step={7}>
                <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                  <FormField label="Previous Company">
                    <Input value={formValues.previousCompany ?? ""} onChange={(e) => updateField("previousCompany", e.target.value)} placeholder="Company name" />
                  </FormField>
                  <FormField label="Previous Job Title">
                    <Input value={formValues.previousJobTitle ?? ""} onChange={(e) => updateField("previousJobTitle", e.target.value)} placeholder="Your role" />
                  </FormField>
                </div>
              </FormSection>
            </>
          )}

          {isBankDetails && (
            /* Bank Details Form */
            <FormSection title="Bank Details" description="Your bank account information for payroll setup" step={1}>
              <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                <FormField label="Bank Name" required error={hasError("bankName")}>
                  <Input value={formValues.bankName ?? ""} onChange={(e) => updateField("bankName", e.target.value)} placeholder="e.g. Emirates NBD" />
                </FormField>
                <FormField label="Branch / Location" required error={hasError("branchLocation")}>
                  <Input value={formValues.branchLocation ?? ""} onChange={(e) => updateField("branchLocation", e.target.value)} placeholder="e.g. Dubai Main Branch" />
                </FormField>
                <div className="sm:col-span-2">
                  <FormField label="Bank Address">
                    <Input value={formValues.address ?? ""} onChange={(e) => updateField("address", e.target.value)} placeholder="Full bank address" />
                  </FormField>
                </div>
                <FormField label="Account Name" required error={hasError("accountName")}>
                  <Input value={formValues.accountName ?? ""} onChange={(e) => updateField("accountName", e.target.value)} placeholder="Name on the account" />
                </FormField>
                <FormField label="Account Number" required error={hasError("accountNo")}>
                  <Input value={formValues.accountNo ?? ""} onChange={(e) => updateField("accountNo", e.target.value)} placeholder="Account number" />
                </FormField>
                <FormField label="IBAN" required error={hasError("iban")}>
                  <Input value={formValues.iban ?? ""} onChange={(e) => updateField("iban", e.target.value)} placeholder="e.g. AE070331234567890123456" />
                </FormField>
                <FormField label="SWIFT Code" required error={hasError("swiftCode")}>
                  <Input value={formValues.swiftCode ?? ""} onChange={(e) => updateField("swiftCode", e.target.value)} placeholder="e.g. EABORAAE" />
                </FormField>
                <FormField label="Sort Code">
                  <Input value={formValues.sortCode ?? ""} onChange={(e) => updateField("sortCode", e.target.value)} placeholder="If applicable" />
                </FormField>
                <FormField label="Signature Date">
                  <Input type="date" value={formValues.signatureDate ?? ""} onChange={(e) => updateField("signatureDate", e.target.value)} />
                </FormField>
              </div>
            </FormSection>
          )}

          {/* Custom Form Fields */}
          {isCustom && data.form.fields && (() => {
            // Group fields by section headings
            const groups: Array<{ heading: string | null; fields: typeof data.form.fields }> = [];
            let currentGroup: typeof data.form.fields = [];
            let currentHeading: string | null = null;

            for (const f of data.form.fields!) {
              if (f.type === "heading") {
                if (currentGroup.length > 0 || currentHeading !== null) {
                  groups.push({ heading: currentHeading, fields: currentGroup });
                }
                currentHeading = f.label;
                currentGroup = [];
              } else {
                currentGroup.push(f);
              }
            }
            if (currentGroup.length > 0 || currentHeading !== null) {
              groups.push({ heading: currentHeading, fields: currentGroup });
            }

            return groups.map((group, gIdx) => (
              <FormSection
                key={gIdx}
                title={group.heading ?? data.form.name}
                description={gIdx === 0 && !group.heading ? (data.form.description ?? "") : ""}
                step={gIdx + 1}
              >
                <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                  {group.fields!.map((field) => {
                    if (field.type === "textarea") {
                      return (
                        <div key={field.name} className="sm:col-span-2">
                          <FormField label={field.label} required={field.required} error={hasError(field.name)}>
                            <textarea
                              value={formValues[field.name] ?? ""}
                              onChange={(e) => updateField(field.name, e.target.value)}
                              placeholder={field.placeholder}
                              className="min-h-[80px] w-full rounded-lg border border-input bg-transparent p-3 text-sm outline-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50"
                            />
                          </FormField>
                        </div>
                      );
                    }
                    if (field.type === "select") {
                      return (
                        <FormField key={field.name} label={field.label} required={field.required} error={hasError(field.name)}>
                          <Select value={formValues[field.name] ?? ""} onValueChange={(v) => updateField(field.name, v)}>
                            <SelectTrigger className="w-full"><SelectValue placeholder={field.placeholder || "Select..."} /></SelectTrigger>
                            <SelectContent>
                              {(field.options ?? []).map((opt) => (
                                <SelectItem key={opt} value={opt}>
                                  {field.optionLabels?.[opt] ?? opt}
                                </SelectItem>
                              ))}
                            </SelectContent>
                          </Select>
                        </FormField>
                      );
                    }
                    if (field.type === "file") {
                      const fileForField = files.find((p) => p.fieldName === field.name);
                      return (
                        <div key={field.name} className="sm:col-span-2">
                          <FormField label={field.label} required={field.required} error={hasError(field.name)}>
                            <label className="flex cursor-pointer flex-col items-center gap-2 rounded-xl border-2 border-dashed border-zinc-300 p-6 transition-all hover:border-primary hover:bg-primary/5 dark:border-zinc-700">
                              <div className="rounded-full bg-zinc-100 p-2 dark:bg-zinc-800">
                                <Upload className="size-4 text-muted-foreground" />
                              </div>
                              <span className="text-sm font-medium text-muted-foreground">
                                {fileForField ? "Replace file" : `Click to upload ${field.label.toLowerCase()}`}
                              </span>
                              <span className="text-[10px] text-muted-foreground">
                                {data.fileRules.label} &middot; Max 1MB
                              </span>
                              <input
                                type="file"
                                accept={data.fileRules.mimeTypes.join(",")}
                                onChange={(e) => handleFieldFile(field.name, e)}
                                className="hidden"
                              />
                            </label>
                            {fileForField && (
                              <div className="mt-2 flex items-center justify-between rounded-xl bg-zinc-50 p-3 dark:bg-zinc-800/50">
                                <div className="flex items-center gap-3">
                                  <div className="rounded-lg bg-primary/10 p-1.5">
                                    <FileText className="size-4 text-primary" />
                                  </div>
                                  <div>
                                    <p className="text-xs font-medium">{fileForField.file.name}</p>
                                    <p className="text-[10px] text-muted-foreground">
                                      {(fileForField.file.size / 1024).toFixed(0)} KB
                                    </p>
                                  </div>
                                </div>
                                <button
                                  type="button"
                                  onClick={() => removeFieldFile(field.name)}
                                  aria-label={`Remove ${field.label}`}
                                  className="rounded-md p-1.5 text-zinc-400 hover:text-red-500"
                                >
                                  <X className="size-3.5" />
                                </button>
                              </div>
                            )}
                          </FormField>
                        </div>
                      );
                    }
                    // text, email, phone, date
                    return (
                      <FormField key={field.name} label={field.label} required={field.required} error={hasError(field.name)}>
                        <Input
                          type={field.type === "phone" ? "tel" : field.type === "date" ? "date" : field.type === "email" ? "email" : "text"}
                          value={formValues[field.name] ?? ""}
                          onChange={(e) => updateField(field.name, e.target.value)}
                          placeholder={field.placeholder}
                        />
                      </FormField>
                    );
                  })}
                </div>
              </FormSection>
            ));
          })()}

          {/* Attachments — only for forms that don't declare their own file fields.
              Recruitment intake forms render labeled per-field uploads inline above. */}
          {!hasExplicitFileFields && (
          <FormSection title="Attachments" description={`Accepted formats: ${data.fileRules.label}. Maximum 1MB per file.`}>
            <label className="flex cursor-pointer flex-col items-center gap-2 rounded-xl border-2 border-dashed border-zinc-300 p-8 transition-all hover:border-primary hover:bg-primary/5 dark:border-zinc-700">
              <div className="rounded-full bg-zinc-100 p-3 dark:bg-zinc-800">
                <Upload className="size-5 text-muted-foreground" />
              </div>
              <span className="text-sm font-medium text-muted-foreground">Click to upload files</span>
              <span className="text-[10px] text-muted-foreground">{data.fileRules.label} &middot; Max 1MB</span>
              <input type="file" multiple accept={data.fileRules.mimeTypes.join(",")} onChange={handleFileAdd} className="hidden" />
            </label>

            {fileError && <p className="mt-2 text-xs text-red-600">{fileError}</p>}

            {files.length > 0 && (
              <div className="mt-3 space-y-2">
                {files.map((f, i) => (
                  <div key={i} className="flex items-center justify-between rounded-xl bg-zinc-50 p-3 dark:bg-zinc-800/50">
                    <div className="flex items-center gap-3">
                      <div className="rounded-lg bg-primary/10 p-1.5">
                        <FileText className="size-4 text-primary" />
                      </div>
                      <div>
                        <p className="text-xs font-medium">{f.file.name}</p>
                        <p className="text-[10px] text-muted-foreground">{(f.file.size / 1024).toFixed(0)} KB</p>
                      </div>
                    </div>
                    <button onClick={() => setFiles(files.filter((_, j) => j !== i))} className="rounded-md p-1.5 text-zinc-400 hover:text-red-500">
                      <X className="size-3.5" />
                    </button>
                  </div>
                ))}
              </div>
            )}
          </FormSection>
          )}

          {/* Validation error summary */}
          {errorFields.size > 0 && (
            <motion.div
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              className="rounded-2xl border border-red-200 bg-red-50 p-4 dark:border-red-900 dark:bg-red-950/50"
            >
              <div className="flex items-center gap-2">
                <AlertTriangle className="size-4 text-red-600" />
                <p className="text-sm font-medium text-red-800 dark:text-red-200">
                  {errorFields.size} required field{errorFields.size > 1 ? "s" : ""} still need{errorFields.size === 1 ? "s" : ""} to be completed. They are highlighted in red above.
                </p>
              </div>
            </motion.div>
          )}

          {/* Submit */}
          <div className="flex items-center justify-between rounded-2xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-900">
            <div>
              <p className="text-sm font-medium">Ready to submit?</p>
              <p className="text-xs text-muted-foreground">Make sure all required fields are filled in.</p>
            </div>
            <Button onClick={handleSubmit} disabled={isSubmitting} className="gap-2" size="lg">
              {isSubmitting ? <Loader2 className="size-4 animate-spin" /> : <><Sparkles className="size-4" /> Submit Form</>}
            </Button>
          </div>

          {error && <p className="pb-4 text-center text-sm text-red-600">{error}</p>}
        </div>
      </div>
    </div>
  );
}

```