---
type: source
source_type: laptop
title: page
slug: page-12
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/admin/hr-forms/[id]/page.tsx"
original_size: 10432
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# page

_Extracted from `[[assessify|assessify]]/src/app/admin/hr-forms/[id]/page.tsx` on 2026-05-14._

```tsx
import { requireAuth } from "@/lib/auth";
import { prisma } from "@/lib/db";
import { notFound } from "next/navigation";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {  } from "@/components/ui/badge";
import { ArrowLeft, Paperclip } from "lucide-react";
import Link from "next/link";

// Hoisted to module scope so React Compiler can optimize. Accepts any
// stringifiable value coming from the dynamic JSON form blob.
function FieldDisplay({ label, value }: { label: string; value: unknown }) {
  if (value === null || value === undefined || value === "") return null;
  return (
    <div>
      <p className="text-[10px] font-medium uppercase tracking-wider text-muted-foreground">{label}</p>
      <p className="text-sm">{String(value)}</p>
    </div>
  );
}

export default async function FormSubmissionDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  await requireAuth();
  const { id } = await params;

  const submission = await prisma.formSubmission.findUnique({
    where: { id },
    include: { template: true, files: true },
  });

  if (!submission) notFound();

  const formData = JSON.parse(submission.formData);
  const isPersonalData = submission.template.formType === "personal_data";

  const statusColors: Record<string, string> = {
    submitted: "bg-blue-100 text-blue-800",
    reviewed: "bg-emerald-100 text-emerald-800",
    flagged: "bg-red-100 text-red-800",
    draft: "bg-zinc-100 text-zinc-600",
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center gap-4">
        <Link
          href="/admin/hr-forms"
          className="rounded-lg p-1.5 text-muted-foreground transition-colors hover:bg-zinc-100 hover:text-foreground dark:hover:bg-zinc-800"
        >
          <ArrowLeft className="size-5" />
        </Link>
        <div className="flex-1">
          <h1 className="text-2xl font-semibold tracking-tight">
            {submission.employeeName}
          </h1>
          <p className="text-sm text-muted-foreground">
            {submission.template.name} &middot; {submission.employeeEmail} &middot; {submission.region === "uae" ? "UAE" : "Global"}
          </p>
        </div>
        <span className={`inline-flex items-center rounded-full px-3 py-1 text-xs font-semibold ${statusColors[submission.status] ?? ""}`}>
          {submission.status}
        </span>
      </div>

      {isPersonalData ? (
        <>
          <Card>
            <CardHeader><CardTitle>Personal Information</CardTitle></CardHeader>
            <CardContent>
              <div className="grid grid-cols-2 gap-4 sm:grid-cols-3">
                <FieldDisplay label="Title" value={formData.title} />
                <FieldDisplay label="First Name" value={formData.firstName} />
                <FieldDisplay label="Preferred Name" value={formData.preferredName} />
                <FieldDisplay label="Surname" value={formData.surname} />
                <FieldDisplay label="Nationality" value={formData.nationality} />
                <FieldDisplay label="Place of Birth" value={formData.placeOfBirth} />
                <FieldDisplay label="Date of Birth" value={formData.dateOfBirth} />
                <FieldDisplay label="Marital Status" value={formData.maritalStatus} />
                <FieldDisplay label="Religion" value={formData.religion} />
                <FieldDisplay label="Personal Email" value={formData.personalEmail} />
                <FieldDisplay label="Mobile Phone" value={formData.mobilePhone} />
                <FieldDisplay label="Home Phone" value={formData.homePhone} />
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader><CardTitle>Address</CardTitle></CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                <FieldDisplay label="Physical Address" value={formData.physicalAddress} />
                <FieldDisplay label="Overseas Address" value={formData.overseasAddress} />
                <FieldDisplay label="Overseas Phone" value={formData.overseasHomePhone} />
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader><CardTitle>Family</CardTitle></CardHeader>
            <CardContent>
              <div className="grid grid-cols-2 gap-4 sm:grid-cols-3">
                <FieldDisplay label="Father's Name" value={formData.fatherName} />
                <FieldDisplay label="Mother's Name" value={formData.motherName} />
                <FieldDisplay label="Spouse Name" value={formData.spouseName} />
                <FieldDisplay label="Spouse DOB" value={formData.spouseDateOfBirth} />
              </div>
              {formData.children?.length > 0 && (
                <div className="mt-4">
                  <p className="mb-2 text-xs font-semibold">Children</p>
                  {(formData.children as Array<{ name?: string; gender?: string; dateOfBirth?: string }>).map((c, i) => (
                    <div key={i} className="mb-1 rounded bg-zinc-50 p-2 text-xs dark:bg-zinc-800/50">
                      {c.name} &middot; {c.gender} &middot; {c.dateOfBirth}
                    </div>
                  ))}
                </div>
              )}
            </CardContent>
          </Card>

          {formData.education?.length > 0 && (
            <Card>
              <CardHeader><CardTitle>Education</CardTitle></CardHeader>
              <CardContent>
                {(formData.education as Array<{ university?: string; degreeType?: string; majorSubject?: string; gradeGpa?: string; startDate?: string; endDate?: string }>).map((e, i) => (
                  <div key={i} className="mb-2 rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800/50">
                    <p className="text-sm font-medium">{e.university}</p>
                    <p className="text-xs text-muted-foreground">
                      {e.degreeType} in {e.majorSubject} &middot; GPA: {e.gradeGpa} &middot; {e.startDate} — {e.endDate}
                    </p>
                  </div>
                ))}
              </CardContent>
            </Card>
          )}

          {formData.languages?.length > 0 && (
            <Card>
              <CardHeader><CardTitle>Languages</CardTitle></CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-2">
                  {(formData.languages as Array<{ language?: string; level?: string }>).map((l, i) => (
                    <span key={i} className="rounded-full bg-zinc-100 px-3 py-1 text-xs dark:bg-zinc-800">
                      {l.language} — {l.level}
                    </span>
                  ))}
                </div>
              </CardContent>
            </Card>
          )}

          <Card>
            <CardHeader><CardTitle>Emergency Contacts</CardTitle></CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <div>
                  <p className="mb-2 text-xs font-semibold">Next of Kin</p>
                  <div className="space-y-2">
                    <FieldDisplay label="Name" value={formData.nextOfKinName} />
                    <FieldDisplay label="Relationship" value={formData.nextOfKinRelationship} />
                    <FieldDisplay label="Address" value={formData.nextOfKinAddress} />
                    <FieldDisplay label="Phone" value={formData.nextOfKinMobilePhone} />
                  </div>
                </div>
                <div>
                  <p className="mb-2 text-xs font-semibold">Emergency Contact</p>
                  {formData.emergencyContactSameAsNextOfKin ? (
                    <p className="rounded-lg bg-zinc-50 p-2 text-xs text-muted-foreground dark:bg-zinc-800/50">
                      Same as Next of Kin
                    </p>
                  ) : (
                    <div className="space-y-2">
                      <FieldDisplay label="Name" value={formData.emergencyContactName} />
                      <FieldDisplay label="Relationship" value={formData.emergencyContactRelationship} />
                      <FieldDisplay label="Address" value={formData.emergencyContactAddress} />
                      <FieldDisplay label="Phone" value={formData.emergencyContactMobilePhone} />
                    </div>
                  )}
                </div>
              </div>
            </CardContent>
          </Card>
        </>
      ) : (
        <Card>
          <CardHeader><CardTitle>Bank Details</CardTitle></CardHeader>
          <CardContent>
            <div className="grid grid-cols-2 gap-4 sm:grid-cols-3">
              <FieldDisplay label="Bank Name" value={formData.bankName} />
              <FieldDisplay label="Branch" value={formData.branchLocation} />
              <FieldDisplay label="Address" value={formData.address} />
              <FieldDisplay label="Account Name" value={formData.accountName} />
              <FieldDisplay label="Account No" value={formData.accountNo} />
              <FieldDisplay label="IBAN" value={formData.iban} />
              <FieldDisplay label="SWIFT" value={formData.swiftCode} />
              <FieldDisplay label="Sort Code" value={formData.sortCode} />
              <FieldDisplay label="Signature Date" value={formData.signatureDate} />
            </div>
          </CardContent>
        </Card>
      )}

      {formData.notes && (
        <Card>
          <CardHeader><CardTitle>Notes</CardTitle></CardHeader>
          <CardContent><p className="text-sm">{formData.notes}</p></CardContent>
        </Card>
      )}

      {submission.files.length > 0 && (
        <Card>
          <CardHeader><CardTitle>Attachments</CardTitle></CardHeader>
          <CardContent>
            {submission.files.map((f) => (
              <div key={f.id} className="mb-2 flex items-center gap-3 rounded-lg bg-zinc-50 p-3 dark:bg-zinc-800/50">
                <Paperclip className="size-4 text-muted-foreground" />
                <div>
                  <p className="text-sm font-medium">{f.fileName}</p>
                  <p className="text-[10px] text-muted-foreground">
                    {f.fileType} &middot; {(f.fileSize / 1024).toFixed(0)} KB
                  </p>
                </div>
              </div>
            ))}
          </CardContent>
        </Card>
      )}
    </div>
  );
}

```