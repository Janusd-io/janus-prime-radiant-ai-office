---
type: source
source_type: laptop
title: Assessify — migration
slug: migration
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/prisma/migrations/20260501144000_recruitment_foundation/migration.sql
original_size: 8038
original_ext: .sql
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:32Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# migration

_Extracted from `[[assessify|assessify]]/prisma/migrations/20260501144000_recruitment_foundation/migration.sql` on 2026-05-14._

```sql
-- Phase 1.A: Recruitment pipeline foundation.
-- Additive migration. Existing data on AdminUser, JobRole, CandidateInvite is preserved.
-- See plan: /Users/jehad/.claude/plans/vast-tumbling-glacier.md

-- AlterTable: AdminUser scoping fields (nullable; existing admins remain global)
ALTER TABLE "AdminUser" ADD COLUMN "office" TEXT;
ALTER TABLE "AdminUser" ADD COLUMN "scopedDepartments" TEXT;

-- CreateTable: Candidate
CREATE TABLE "Candidate" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "firstName" TEXT NOT NULL,
    "lastName" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "phoneNumber" TEXT,
    "nationality" TEXT,
    "noticePeriod" TEXT,
    "office" TEXT,
    "source" TEXT,
    "agencyName" TEXT,
    "linkedinUrl" TEXT,
    "cvDriveUrl" TEXT,
    "cvDriveFolderUrl" TEXT,
    "cvFileName" TEXT,
    "cvUploadedAt" DATETIME,
    "externalId" TEXT,
    "archivedAt" DATETIME,
    "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" DATETIME NOT NULL
);

-- CreateTable: Application
CREATE TABLE "Application" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "candidateId" TEXT NOT NULL,
    "jobRoleId" TEXT NOT NULL,
    "intakeSubmissionId" TEXT,
    "office" TEXT,
    "source" TEXT,
    "agencyName" TEXT,
    "currentStage" TEXT NOT NULL DEFAULT 'intake_received',
    "status" TEXT NOT NULL DEFAULT 'active',
    "closeReason" TEXT,
    "assignedAdminId" TEXT,
    "preScore" REAL,
    "preScoreTier" TEXT,
    "postScore" REAL,
    "postScoreTier" TEXT,
    "appliedAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "closedAt" DATETIME,
    "externalId" TEXT,
    "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" DATETIME NOT NULL,
    CONSTRAINT "Application_candidateId_fkey" FOREIGN KEY ("candidateId") REFERENCES "Candidate" ("id") ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT "Application_jobRoleId_fkey" FOREIGN KEY ("jobRoleId") REFERENCES "JobRole" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable: ApplicationStage
CREATE TABLE "ApplicationStage" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "applicationId" TEXT NOT NULL,
    "stage" TEXT NOT NULL,
    "enteredAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "exitedAt" DATETIME,
    "notes" TEXT,
    "actorId" TEXT,
    "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "ApplicationStage_applicationId_fkey" FOREIGN KEY ("applicationId") REFERENCES "Application" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable: ApplicationFeedback
CREATE TABLE "ApplicationFeedback" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "applicationId" TEXT NOT NULL,
    "actorId" TEXT NOT NULL,
    "kind" TEXT NOT NULL,
    "content" TEXT NOT NULL,
    "score" INTEGER,
    "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "ApplicationFeedback_applicationId_fkey" FOREIGN KEY ("applicationId") REFERENCES "Application" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateTable: RecruitmentRubric
CREATE TABLE "RecruitmentRubric" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "kind" TEXT NOT NULL,
    "jobRoleId" TEXT,
    "version" INTEGER NOT NULL DEFAULT 1,
    "isActive" BOOLEAN NOT NULL DEFAULT true,
    "criteria" TEXT NOT NULL,
    "thresholdStrong" REAL NOT NULL DEFAULT 0.85,
    "thresholdMatch" REAL NOT NULL DEFAULT 0.70,
    "thresholdConsider" REAL NOT NULL DEFAULT 0.55,
    "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" DATETIME NOT NULL,
    CONSTRAINT "RecruitmentRubric_jobRoleId_fkey" FOREIGN KEY ("jobRoleId") REFERENCES "JobRole" ("id") ON DELETE SET NULL ON UPDATE CASCADE
);

-- CreateTable: ApplicationScore
CREATE TABLE "ApplicationScore" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "applicationId" TEXT NOT NULL,
    "rubricId" TEXT NOT NULL,
    "kind" TEXT NOT NULL,
    "score" REAL NOT NULL,
    "tier" TEXT NOT NULL,
    "breakdown" TEXT NOT NULL,
    "sourceRef" TEXT,
    "computedBy" TEXT,
    "computedAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "ApplicationScore_applicationId_fkey" FOREIGN KEY ("applicationId") REFERENCES "Application" ("id") ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT "ApplicationScore_rubricId_fkey" FOREIGN KEY ("rubricId") REFERENCES "RecruitmentRubric" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- AlterTable: extend CandidateInvite (data-preserving redefinition for FK additions)
PRAGMA defer_foreign_keys=ON;
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_CandidateInvite" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "code" TEXT NOT NULL,
    "candidateName" TEXT NOT NULL,
    "candidateEmail" TEXT NOT NULL,
    "templateId" TEXT NOT NULL,
    "status" TEXT NOT NULL DEFAULT 'pending',
    "sessionId" TEXT,
    "expiresAt" DATETIME,
    "createdBy" TEXT,
    "externalId" TEXT,
    "candidateId" TEXT,
    "applicationId" TEXT,
    "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" DATETIME NOT NULL,
    CONSTRAINT "CandidateInvite_templateId_fkey" FOREIGN KEY ("templateId") REFERENCES "AssessmentTemplate" ("id") ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT "CandidateInvite_candidateId_fkey" FOREIGN KEY ("candidateId") REFERENCES "Candidate" ("id") ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT "CandidateInvite_applicationId_fkey" FOREIGN KEY ("applicationId") REFERENCES "Application" ("id") ON DELETE SET NULL ON UPDATE CASCADE
);
INSERT INTO "new_CandidateInvite" ("id", "code", "candidateName", "candidateEmail", "templateId", "status", "sessionId", "expiresAt", "createdBy", "externalId", "createdAt", "updatedAt") SELECT "id", "code", "candidateName", "candidateEmail", "templateId", "status", "sessionId", "expiresAt", "createdBy", "externalId", "createdAt", "updatedAt" FROM "CandidateInvite";
DROP TABLE "CandidateInvite";
ALTER TABLE "new_CandidateInvite" RENAME TO "CandidateInvite";
CREATE UNIQUE INDEX "CandidateInvite_code_key" ON "CandidateInvite"("code");
CREATE UNIQUE INDEX "CandidateInvite_externalId_key" ON "CandidateInvite"("externalId");
CREATE INDEX "CandidateInvite_code_idx" ON "CandidateInvite"("code");
CREATE INDEX "CandidateInvite_candidateEmail_idx" ON "CandidateInvite"("candidateEmail");
CREATE INDEX "CandidateInvite_status_idx" ON "CandidateInvite"("status");
CREATE INDEX "CandidateInvite_candidateId_idx" ON "CandidateInvite"("candidateId");
CREATE INDEX "CandidateInvite_applicationId_idx" ON "CandidateInvite"("applicationId");
PRAGMA foreign_keys=ON;
PRAGMA defer_foreign_keys=OFF;

-- CreateIndex: Candidate
CREATE UNIQUE INDEX "Candidate_email_key" ON "Candidate"("email");
CREATE UNIQUE INDEX "Candidate_externalId_key" ON "Candidate"("externalId");
CREATE INDEX "Candidate_email_idx" ON "Candidate"("email");
CREATE INDEX "Candidate_office_idx" ON "Candidate"("office");
CREATE INDEX "Candidate_archivedAt_idx" ON "Candidate"("archivedAt");
CREATE INDEX "Candidate_source_idx" ON "Candidate"("source");

-- CreateIndex: Application
CREATE UNIQUE INDEX "Application_externalId_key" ON "Application"("externalId");
CREATE INDEX "Application_candidateId_idx" ON "Application"("candidateId");
CREATE INDEX "Application_jobRoleId_idx" ON "Application"("jobRoleId");
CREATE INDEX "Application_currentStage_idx" ON "Application"("currentStage");
CREATE INDEX "Application_status_idx" ON "Application"("status");
CREATE INDEX "Application_office_idx" ON "Application"("office");
CREATE INDEX "Application_source_idx" ON "Application"("source");

-- CreateIndex: ApplicationStage / ApplicationFeedback
CREATE INDEX "ApplicationStage_applicationId_idx" ON "ApplicationStage"("applicationId");
CREATE INDEX "ApplicationFeedback_applicationId_idx" ON "ApplicationFeedback"("applicationId");

-- CreateIndex: RecruitmentRubric / ApplicationScore
CREATE INDEX "RecruitmentRubric_kind_jobRoleId_isActive_idx" ON "RecruitmentRubric"("kind", "jobRoleId", "isActive");
CREATE INDEX "ApplicationScore_applicationId_idx" ON "ApplicationScore"("applicationId");
CREATE INDEX "ApplicationScore_rubricId_idx" ON "ApplicationScore"("rubricId");

```