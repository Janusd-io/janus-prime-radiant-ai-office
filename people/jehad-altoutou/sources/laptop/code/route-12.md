---
type: source
source_type: laptop
title: Assessify — route
slug: route-12
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/forms/[submissionId]/route.ts"
original_size: 16170
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/forms/[submissionId]/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { RECRUITMENT_INTAKE_AGENCY, RECRUITMENT_INTAKE_DIRECT } from "@/lib/recruitment";

// GET: Fetch submission data (for resuming drafts)
export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ submissionId: string }> }
) {
  try {
    const { submissionId } = await ctx.params;

    const submission = await prisma.formSubmission.findUnique({
      where: { id: submissionId },
      include: {
        template: true,
        files: true,
      },
    });

    if (!submission) {
      return Response.json({ error: "Submission not found" }, { status: 404 });
    }

    return Response.json({
      submission: {
        id: submission.id,
        templateId: submission.templateId,
        formType: submission.template.formType,
        formName: submission.template.name,
        employeeName: submission.employeeName,
        employeeEmail: submission.employeeEmail,
        region: submission.region,
        status: submission.status,
        formData: JSON.parse(submission.formData),
        files: submission.files,
        startedAt: submission.startedAt,
        submittedAt: submission.submittedAt,
      },
    });
  } catch (error) {
    console.error("GET /api/forms/[submissionId] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

// PUT: Save draft or submit form
export async function PUT(
  req: NextRequest,
  ctx: { params: Promise<{ submissionId: string }> }
) {
  try {
    const { submissionId } = await ctx.params;
    const body = await req.json();
    const { formData, files, submit } = body as {
      formData: Record<string, unknown>;
      files?: { fileName: string; fileType: string; fileSize: number; fieldName: string; base64Data?: string }[];
      submit?: boolean;
    };

    const submission = await prisma.formSubmission.findUnique({
      where: { id: submissionId },
    });

    if (!submission) {
      return Response.json({ error: "Submission not found" }, { status: 404 });
    }

    if (submission.status === "submitted" || submission.status === "reviewed") {
      return Response.json({ error: "This form has already been submitted" }, { status: 409 });
    }

    // Format dates from YYYY-MM-DD to DD/MM/YYYY
    const dateFields = [
      "dateOfBirth", "spouseDateOfBirth", "signatureDate",
    ];
    const formatted = { ...formData } as Record<string, unknown>;
    for (const field of dateFields) {
      const v = formatted[field];
      if (typeof v === "string" && /^\d{4}-\d{2}-\d{2}$/.test(v)) {
        const [y, m, d] = v.split("-");
        formatted[field] = `${d}/${m}/${y}`;
      }
    }
    // Format dates in children array
    if (Array.isArray(formatted.children)) {
      formatted.children = (formatted.children as Array<Record<string, unknown>>).map((c) => {
        const dob = c.dateOfBirth;
        if (typeof dob === "string" && /^\d{4}-\d{2}-\d{2}$/.test(dob)) {
          const [y, m, d] = dob.split("-");
          return { ...c, dateOfBirth: `${d}/${m}/${y}` };
        }
        return c;
      });
    }
    // Format dates in education array
    if (Array.isArray(formatted.education)) {
      formatted.education = (formatted.education as Array<Record<string, unknown>>).map((e) => {
        const out: Record<string, unknown> = { ...e };
        for (const df of ["startDate", "endDate"]) {
          const v = out[df];
          if (typeof v === "string" && /^\d{4}-\d{2}-\d{2}$/.test(v)) {
            const [y, m, d] = v.split("-");
            out[df] = `${d}/${m}/${y}`;
          }
        }
        return out;
      });
    }

    // Update form data
    await prisma.formSubmission.update({
      where: { id: submissionId },
      data: {
        formData: JSON.stringify(formatted),
        status: submit ? "submitted" : "draft",
        submittedAt: submit ? new Date() : undefined,
      },
    });

    // Save file metadata (no server storage — files go directly to webhook as base64)
    if (files && files.length > 0) {
      await prisma.formFile.deleteMany({ where: { submissionId } });
      await prisma.formFile.createMany({
        data: files.map((f) => ({
          submissionId,
          fileName: f.fileName,
          fileType: f.fileType,
          fileSize: f.fileSize,
          filePath: "webhook-delivery",
          fieldName: f.fieldName,
        })),
      });
    }

    // Update invite status if submitting
    if (submit && submission.inviteCode) {
      await prisma.formInvite.updateMany({
        where: { code: submission.inviteCode },
        data: { status: "submitted" },
      });
    }

    // Fire n8n webhook on submission
    if (submit) {
      const template = await prisma.formTemplate.findUnique({
        where: { id: submission.templateId },
      });

      // Build clean webhook payload — no mixed/nested JSON
      const emergencySameAsKin = formatted.emergencyContactSameAsNextOfKin === true;

      const webhookPayload: Record<string, unknown> = {
        event: "form.submitted",
        timestamp: new Date().toISOString(),
        submissionId,
        formType: template?.formType ?? "unknown",
        formName: template?.name ?? "Unknown Form",
        employee: {
          name: submission.employeeName,
          email: submission.employeeEmail,
        },
        region: submission.region,
      };

      if (template?.formType === "personal_data") {
        webhookPayload.personalInformation = {
          title: formatted.title ?? null,
          firstName: formatted.firstName ?? null,
          preferredName: formatted.preferredName ?? null,
          surname: formatted.surname ?? null,
          otherSurname: formatted.otherSurname ?? null,
          nationality: formatted.nationality ?? null,
          placeOfBirth: formatted.placeOfBirth ?? null,
          dateOfBirth: formatted.dateOfBirth ?? null,
          maritalStatus: formatted.maritalStatus ?? null,
          religion: formatted.religion ?? null,
          personalEmail: formatted.personalEmail ?? null,
          mobilePhone: formatted.mobilePhone ?? null,
          homePhone: formatted.homePhone ?? null,
        };
        webhookPayload.address = {
          physical: formatted.physicalAddress ?? null,
          overseas: formatted.overseasAddress ?? null,
          overseasPhone: formatted.overseasHomePhone ?? null,
        };
        webhookPayload.family = {
          fatherName: formatted.fatherName ?? null,
          motherName: formatted.motherName ?? null,
          spouseName: formatted.spouseName ?? null,
          spouseDateOfBirth: formatted.spouseDateOfBirth ?? null,
          children: formatted.children ?? [],
        };
        webhookPayload.education = formatted.education ?? [];
        webhookPayload.languages = ((formatted.languages ?? []) as Array<{ language: string; level: string }>).map((l) => ({
          language: l.language,
          proficiency: l.level,
        }));
        webhookPayload.nextOfKin = {
          name: formatted.nextOfKinName ?? null,
          relationship: formatted.nextOfKinRelationship ?? null,
          address: formatted.nextOfKinAddress ?? null,
          homePhone: formatted.nextOfKinHomePhone ?? null,
          mobilePhone: formatted.nextOfKinMobilePhone ?? null,
        };
        webhookPayload.emergencyContact = emergencySameAsKin
          ? { sameAsNextOfKin: true }
          : {
              sameAsNextOfKin: false,
              name: formatted.emergencyContactName ?? null,
              relationship: formatted.emergencyContactRelationship ?? null,
              address: formatted.emergencyContactAddress ?? null,
              homePhone: formatted.emergencyContactHomePhone ?? null,
              mobilePhone: formatted.emergencyContactMobilePhone ?? null,
            };
        webhookPayload.previousEmployment = {
          company: formatted.previousCompany ?? null,
          jobTitle: formatted.previousJobTitle ?? null,
        };
      } else if (template?.formType === "bank_details") {
        webhookPayload.bankDetails = {
          bankName: formatted.bankName ?? null,
          branchLocation: formatted.branchLocation ?? null,
          address: formatted.address ?? null,
          accountName: formatted.accountName ?? null,
          accountNumber: formatted.accountNo ?? null,
          iban: formatted.iban ?? null,
          swiftCode: formatted.swiftCode ?? null,
          sortCode: formatted.sortCode ?? null,
          signatureDate: formatted.signatureDate ?? null,
        };
      } else if (
        template?.formType === RECRUITMENT_INTAKE_AGENCY ||
        template?.formType === RECRUITMENT_INTAKE_DIRECT
      ) {
        const isAgency = template.formType === RECRUITMENT_INTAKE_AGENCY;
        const roleId = formatted.role_id as string | undefined;
        const role = roleId
          ? await prisma.jobRole.findUnique({
              where: { id: roleId },
              include: { department: true },
            })
          : null;

        const firstName = String(formatted.candidate_first_name ?? "").trim();
        const lastName = String(formatted.candidate_last_name ?? "").trim();
        const email = String(formatted.candidate_email ?? "").trim().toLowerCase();
        const phone = String(formatted.candidate_phone ?? "").trim();
        const nationality = String(formatted.candidate_nationality ?? "").trim();
        const noticePeriod = String(formatted.notice_period ?? "").trim();
        const office = String(formatted.office ?? "").trim();
        const linkedinUrl = formatted.linkedin_url ? String(formatted.linkedin_url) : null;
        const agencyName = isAgency
          ? String(formatted.agency_name ?? "").trim() || null
          : null;
        const source = isAgency ? "agency" : "direct";
        const cvFile = (files ?? [])[0];

        // Phase 1.B v3: extended intake fields. Map the human-readable form
        // values to the structured strings/booleans persisted on Candidate.
        const employmentLabel = String(formatted.currently_employed ?? "").trim().toLowerCase();
        const currentlyEmployed =
          employmentLabel === "currently employed"
            ? "employed"
            : employmentLabel === "freelancing"
              ? "freelancing"
              : employmentLabel === "not working"
                ? "not_working"
                : null;
        const visaStatus = String(formatted.visa_status ?? "").trim() || null;
        const locationLabel = String(formatted.location_status ?? "").trim().toLowerCase();
        const locationStatus =
          locationLabel === "inside uae" || locationLabel === "in uae"
            ? "in_uae"
            : locationLabel === "outside uae"
              ? "outside_uae"
              : null;
        const driversLabel = String(formatted.drivers_license ?? "").trim().toLowerCase();
        const hasDriversLicense =
          driversLabel === "yes" ? true : driversLabel === "no" ? false : null;
        const aiToolsProficiency = String(formatted.ai_tools_proficiency ?? "").trim() || null;
        // cvReceivedAt is auto-set to the submission timestamp for both
        // agency and direct intakes — semantically it's "when we received
        // the CV", regardless of who submitted it.
        const cvReceivedAt: Date = new Date();

        // Upsert Candidate by email + create Application. These rows are the
        // dashboard's source of truth — written BEFORE the webhook fires so
        // the dashboard sees the application immediately.
        const candidate = await prisma.candidate.upsert({
          where: { email },
          update: {
            firstName,
            lastName,
            phoneNumber: phone || null,
            nationality: nationality || null,
            noticePeriod: noticePeriod || null,
            office: office || null,
            source,
            agencyName,
            linkedinUrl,
            cvFileName: cvFile?.fileName ?? null,
            currentlyEmployed,
            visaStatus,
            aiToolsProficiency,
            hasDriversLicense,
            locationStatus,
          },
          create: {
            firstName,
            lastName,
            email,
            phoneNumber: phone || null,
            nationality: nationality || null,
            noticePeriod: noticePeriod || null,
            office: office || null,
            source,
            agencyName,
            linkedinUrl,
            cvFileName: cvFile?.fileName ?? null,
            currentlyEmployed,
            visaStatus,
            aiToolsProficiency,
            hasDriversLicense,
            locationStatus,
          },
        });

        let applicationId: string | null = null;
        if (role) {
          const application = await prisma.application.create({
            data: {
              candidateId: candidate.id,
              jobRoleId: role.id,
              intakeSubmissionId: submissionId,
              office: office || null,
              source,
              agencyName,
              cvReceivedAt,
              currentStage: "intake_received",
              status: "active",
            },
          });
          applicationId = application.id;
          await prisma.applicationStage.create({
            data: {
              applicationId,
              stage: "intake_received",
              notes: `Form submission ${submissionId} (${source})`,
            },
          });
        }

        webhookPayload.recruitment = {
          candidateId: candidate.id,
          applicationId,
          candidateName: `${firstName} ${lastName}`.trim(),
          candidateFirstName: firstName,
          candidateLastName: lastName,
          candidateEmail: email,
          candidatePhone: phone || null,
          nationality: nationality || null,
          noticePeriod: noticePeriod || null,
          linkedinUrl,
          agencyName,
          source,
          roleId: role?.id ?? null,
          roleTitle: role?.title ?? null,
          roleSlug: role?.slug ?? null,
          department: role?.department?.name ?? null,
          departmentId: role?.departmentId ?? null,
          office: office || null,
          drivePathHint: office && firstName && lastName
            ? `Recruitment/${office}/${firstName}_${lastName}`
            : null,
          // Phase 1.B v3 — extended intake fields
          cvReceivedAt: cvReceivedAt.toISOString(),
          currentlyEmployed,
          visaStatus,
          locationStatus,
          hasDriversLicense,
          aiToolsProficiency,
        };
        webhookPayload.cv = cvFile ?? null;

        // Phase 1.B: kick the pre-scoring agent. Fire-and-forget — the agent
        // catches its own errors + slackAlerts. Independent of the n8n Drive
        // webhook below; failure here doesn't block submission or Drive.
        if (applicationId && cvFile?.base64Data) {
          const { scorePreInterview } = await import("@/lib/recruitment/pre-scoring-agent");
          void scorePreInterview({
            applicationId,
            cvBase64: cvFile.base64Data,
            cvFileName: cvFile.fileName ?? "cv.pdf",
          });
        }
      }

      // Pass files as base64 binary directly to webhook — no server storage
      webhookPayload.files = (files ?? []).map((f) => ({
        fileName: f.fileName,
        fileType: f.fileType,
        fileSize: f.fileSize,
        base64Data: f.base64Data ?? null,
      }));

      // Dispatch to all active webhook endpoints
      const { dispatchWebhook } = await import("@/lib/webhooks");
      await dispatchWebhook("form.submitted", webhookPayload).catch(() => {
        console.error("Webhook dispatch failed (non-blocking)");
      });
    }

    return Response.json({
      ok: true,
      status: submit ? "submitted" : "draft",
      message: submit ? "Form submitted successfully" : "Draft saved",
    });
  } catch (error) {
    console.error("PUT /api/forms/[submissionId] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```