---
type: source
source_type: laptop
title: seed-recruitment
slug: seed-recruitment
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/scripts/seed-recruitment.ts
original_size: 10087
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# seed-recruitment

_Extracted from `assessify/scripts/seed-recruitment.ts` on 2026-05-14._

```typescript
// Idempotent seeder for Phase 1.A recruitment data.
//   - Upserts two FormTemplates: recruitment_intake_agency, recruitment_intake_direct
//   - Upserts a default placeholder RecruitmentRubric (pre_interview, post_interview)
//
// Run locally:  npx tsx scripts/seed-recruitment.ts
// Run in prod:  docker compose exec app npx tsx scripts/seed-recruitment.ts
//
// Safe to re-run. Existing rows are updated to the canonical Phase 1.A shape.

import "dotenv/config";
import { PrismaClient } from "../src/generated/prisma/client.js";
import { PrismaLibSql } from "@prisma/adapter-libsql";
import { COUNTRIES } from "../src/lib/countries.js";

const dbUrl = process.env.DATABASE_URL ?? "file:./dev.db";
const adapter = new PrismaLibSql({ url: dbUrl });
const prisma = new PrismaClient({ adapter });

type FieldDef = {
  name: string;
  label: string;
  type: string;
  required?: boolean;
  placeholder?: string;
  options?: string[];
  dynamicOptionsSource?: string;
  section?: string;
};

const NOTICE_PERIOD_OPTIONS = [
  "Immediately available",
  "Less than 1 month",
  "1 month",
  "2 months",
  "3 months",
  "More than 3 months",
];

const EMPLOYMENT_STATUS_OPTIONS = ["Currently employed", "Not working", "Freelancing"];
const LOCATION_OPTIONS = ["Inside UAE", "Outside UAE"];
const YES_NO_OPTIONS = ["Yes", "No"];
const NATIONALITY_OPTIONS = COUNTRIES.map((c) => c.name);

function commonFields(includeAgency: boolean): FieldDef[] {
  const fields: FieldDef[] = [
    { name: "candidate_first_name", label: "Candidate first name", type: "text", required: true, placeholder: "Jane" },
    { name: "candidate_last_name", label: "Candidate last name", type: "text", required: true, placeholder: "Doe" },
    { name: "candidate_email", label: "Email address", type: "email", required: true, placeholder: "jane@example.com" },
    { name: "candidate_phone", label: "Phone number", type: "phone", required: true, placeholder: "+971 50 123 4567" },
    {
      name: "candidate_nationality",
      label: "Nationality",
      type: "select",
      required: true,
      options: NATIONALITY_OPTIONS,
      placeholder: "Select nationality",
    },
    {
      name: "notice_period",
      label: "Time to join (notice period)",
      type: "select",
      required: true,
      options: NOTICE_PERIOD_OPTIONS,
      placeholder: "Select notice period",
    },
    { name: "linkedin_url", label: "LinkedIn URL (optional)", type: "text", required: false, placeholder: "https://linkedin.com/in/..." },
  ];
  if (includeAgency) {
    fields.push({ name: "agency_name", label: "Agency name", type: "text", required: true, placeholder: "Your recruitment agency" });
    // Note: cvReceivedAt is auto-set to the submission timestamp by the
    // /api/forms/[submissionId] handler — not asked from the agency.
  }
  fields.push({
    name: "currently_employed",
    label: "Currently employed?",
    type: "select",
    required: true,
    options: EMPLOYMENT_STATUS_OPTIONS,
    placeholder: "Select employment status",
  });
  fields.push({
    name: "visa_status",
    label: "Current visa status",
    type: "text",
    required: true,
    placeholder: "e.g. UAE Resident · Employment-Sponsored · Golden Visa · Tourist · None",
  });
  fields.push({
    name: "location_status",
    label: "Currently located",
    type: "select",
    required: true,
    options: LOCATION_OPTIONS,
    placeholder: "Select current location",
  });
  fields.push({
    name: "drivers_license",
    label: "Driver's license?",
    type: "select",
    required: true,
    options: YES_NO_OPTIONS,
    placeholder: "Yes or No",
  });
  fields.push({
    name: "ai_tools_proficiency",
    label: "AI tools proficiency (optional)",
    type: "textarea",
    required: false,
    placeholder: "e.g. ChatGPT (daily), Claude, Cursor IDE, Midjourney, Copilot…",
  });
  fields.push({
    name: "role_id",
    label: "Job role applying for",
    type: "select",
    required: true,
    placeholder: "Select an open role",
    dynamicOptionsSource: "active_job_roles",
    options: [],
  });
  fields.push({
    name: "office",
    label: "Office",
    type: "select",
    required: true,
    options: ["Dubai", "Singapore"],
    placeholder: "Select office",
  });
  fields.push({
    name: "cv",
    label: "Upload CV (PDF, max 1 MB)",
    type: "file",
    required: true,
    placeholder: "PDF only",
  });
  return fields;
}

const PLACEHOLDER_PRE_CRITERIA = [
  {
    key: "experience_years",
    label: "Years of relevant experience",
    weight: 0.3,
    scoringPrompt:
      "Compare the candidate's years of relevant experience against the job description. Score 1.0 for exceeding the requirement, 0.6 for meeting it, lower for shortfalls.",
  },
  {
    key: "skill_match",
    label: "Skills coverage vs JD",
    weight: 0.35,
    scoringPrompt:
      "Compute the fraction of must-have skills from the job description that the CV demonstrates with concrete evidence. Score = covered / total.",
  },
  {
    key: "education_alignment",
    label: "Education alignment",
    weight: 0.15,
    scoringPrompt:
      "Score 1.0 if degree level + field meets the JD requirement, 0.5 if partial fit, 0.0 if no relevant education and JD requires it.",
  },
  {
    key: "language_fit",
    label: "Language fit",
    weight: 0.1,
    scoringPrompt:
      "Score 1.0 if the candidate's primary working language matches what the role needs (English required for all Janus offices); 0.5 partial; 0.0 missing.",
  },
  {
    key: "tenure_stability",
    label: "Tenure stability",
    weight: 0.1,
    scoringPrompt:
      "Penalise excessive job-hopping (multiple <1y stints) unless explained. Score 1.0 for healthy 2-4y tenures, 0.5 for mixed, lower if many short stints.",
  },
];

const PLACEHOLDER_POST_CRITERIA = [
  {
    key: "communication_clarity",
    label: "Communication clarity",
    weight: 0.25,
    scoringPrompt:
      "Score how clearly the candidate articulates ideas in the interview transcript. 1.0 = consistently clear and concise; lower for rambling or vague answers.",
  },
  {
    key: "technical_depth",
    label: "Technical depth",
    weight: 0.3,
    scoringPrompt:
      "Did the candidate demonstrate hands-on knowledge in the role's core technical areas? Score by depth of specifics, examples, and trade-off awareness.",
  },
  {
    key: "problem_solving",
    label: "Problem-solving approach",
    weight: 0.2,
    scoringPrompt:
      "Score the candidate's reasoning under ambiguity — do they decompose problems, ask clarifying questions, consider trade-offs? 1.0 = strong, 0.0 = jumps to answers.",
  },
  {
    key: "cultural_fit",
    label: "Cultural fit signals",
    weight: 0.15,
    scoringPrompt:
      "Look for signals of collaboration, ownership, and humility (Janus values). 1.0 = strongly aligned; 0.0 = misaligned or red flags.",
  },
  {
    key: "consistency_with_cv",
    label: "Consistency with CV claims",
    weight: 0.1,
    scoringPrompt:
      "Did the interview answers corroborate or contradict the CV? Penalise contradictions or inability to substantiate claimed skills.",
  },
];

async function upsertFormTemplate(
  slug: string,
  name: string,
  formType: string,
  description: string,
  fields: FieldDef[],
) {
  const existing = await prisma.formTemplate.findUnique({ where: { slug } });
  const fieldsJson = JSON.stringify(fields);
  if (existing) {
    return prisma.formTemplate.update({
      where: { slug },
      data: { name, formType, description, fields: fieldsJson, isActive: true },
    });
  }
  return prisma.formTemplate.create({
    data: { slug, name, formType, description, fields: fieldsJson, isActive: true },
  });
}

async function upsertDefaultRubric(
  name: string,
  kind: "pre_interview" | "post_interview",
  criteria: typeof PLACEHOLDER_PRE_CRITERIA,
) {
  // Default rubric = global (jobRoleId is NULL). Only one active per kind.
  const existing = await prisma.recruitmentRubric.findFirst({
    where: { kind, jobRoleId: null, isActive: true },
  });
  const criteriaJson = JSON.stringify(criteria);
  if (existing) {
    return prisma.recruitmentRubric.update({
      where: { id: existing.id },
      data: { name, criteria: criteriaJson },
    });
  }
  return prisma.recruitmentRubric.create({
    data: {
      name,
      kind,
      jobRoleId: null,
      version: 1,
      isActive: true,
      criteria: criteriaJson,
      thresholdStrong: 0.85,
      thresholdMatch: 0.7,
      thresholdConsider: 0.55,
    },
  });
}

async function main() {
  console.log("Seeding recruitment foundation (Phase 1.A)...");

  const agencyTemplate = await upsertFormTemplate(
    "recruitment-intake-agency",
    "Recruitment Intake — Agency Submission",
    "recruitment_intake_agency",
    "Recruitment agencies use this form to submit candidates for open roles. Auto-creates Candidate + Application records and (Phase 1.B) triggers pre-interview scoring.",
    commonFields(true),
  );
  console.log(`  ✓ FormTemplate (agency): ${agencyTemplate.id}`);

  const directTemplate = await upsertFormTemplate(
    "recruitment-intake-direct",
    "Recruitment Intake — Direct Application",
    "recruitment_intake_direct",
    "Public form for candidates applying themselves (e.g. via career page). Auto-creates Candidate + Application records and (Phase 1.B) triggers pre-interview scoring.",
    commonFields(false),
  );
  console.log(`  ✓ FormTemplate (direct): ${directTemplate.id}`);

  const preRubric = await upsertDefaultRubric(
    "Default pre-interview rubric (placeholder)",
    "pre_interview",
    PLACEHOLDER_PRE_CRITERIA,
  );
  console.log(`  ✓ RecruitmentRubric (pre): ${preRubric.id}`);

  const postRubric = await upsertDefaultRubric(
    "Default post-interview rubric (placeholder)",
    "post_interview",
    PLACEHOLDER_POST_CRITERIA,
  );
  console.log(`  ✓ RecruitmentRubric (post): ${postRubric.id}`);

  console.log("Done.");
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });

```