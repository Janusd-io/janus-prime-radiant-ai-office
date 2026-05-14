---
type: source
source_type: laptop
title: Assessify — migration
slug: migration-2
created: 2026-05-05
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/prisma/migrations/20260505000000_jobrole_jd_fields/migration.sql
original_size: 405
original_ext: .sql
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:32Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# migration

_Extracted from `[[assessify|assessify]]/prisma/migrations/20260505000000_jobrole_jd_fields/migration.sql` on 2026-05-14._

```sql
-- Phase 1.B: structured Job Description fields on JobRole.
-- Additive only. Existing rows get NULL for all five columns.

ALTER TABLE "JobRole" ADD COLUMN "jdSummary" TEXT;
ALTER TABLE "JobRole" ADD COLUMN "jdResponsibilities" TEXT;
ALTER TABLE "JobRole" ADD COLUMN "jdRequirements" TEXT;
ALTER TABLE "JobRole" ADD COLUMN "jdNiceToHaves" TEXT;
ALTER TABLE "JobRole" ADD COLUMN "jdYearsExperience" TEXT;

```