---
type: source
source_type: laptop
title: auth-scope.test
slug: auth-scope-test
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/__tests__/auth-scope.test.ts
original_size: 3784
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# auth-scope.test

_Extracted from `[[assessify|assessify]]/src/lib/__tests__/auth-scope.test.ts` on 2026-05-14._

```typescript
import { describe, expect, it } from "vitest";
import {
  applyDepartmentScope,
  applyOfficeScope,
  applyRecruitmentScope,
  parseScopedDepartments,
} from "@/lib/auth-scope";

describe("parseScopedDepartments", () => {
  it("returns null for null/undefined/empty", () => {
    expect(parseScopedDepartments(null)).toBeNull();
    expect(parseScopedDepartments(undefined)).toBeNull();
    expect(parseScopedDepartments("")).toBeNull();
  });

  it("returns null for invalid JSON", () => {
    expect(parseScopedDepartments("not-json")).toBeNull();
  });

  it("returns null for non-array JSON", () => {
    expect(parseScopedDepartments(`{"a":1}`)).toBeNull();
  });

  it("returns null for array of non-strings", () => {
    expect(parseScopedDepartments(`[1, 2, 3]`)).toBeNull();
  });

  it("returns null for empty array", () => {
    expect(parseScopedDepartments(`[]`)).toBeNull();
  });

  it("returns the array of strings when valid", () => {
    expect(parseScopedDepartments(`["a","b","c"]`)).toEqual(["a", "b", "c"]);
  });

  it("filters out non-string entries from a mixed array", () => {
    expect(parseScopedDepartments(`["a", 2, "b"]`)).toEqual(["a", "b"]);
  });
});

describe("applyOfficeScope", () => {
  it("is a no-op when office is null (global session)", () => {
    const where = { status: "active" };
    expect(applyOfficeScope({ office: null }, where)).toEqual(where);
  });

  it("adds OR clause to allow rows matching office or null-office", () => {
    const result = applyOfficeScope({ office: "Dubai" }, { status: "active" });
    expect(result).toEqual({
      status: "active",
      OR: [{ office: "Dubai" }, { office: null }],
    });
  });
});

describe("applyDepartmentScope", () => {
  it("is a no-op when scopedDepartments is null", () => {
    const where = { status: "active" };
    expect(applyDepartmentScope({ scopedDepartments: null }, where)).toEqual(where);
  });

  it("filters by departmentId IN scopedDepartments", () => {
    const result = applyDepartmentScope(
      { scopedDepartments: `["d1","d2"]` },
      { status: "active" },
    );
    expect(result).toEqual({
      status: "active",
      departmentId: { in: ["d1", "d2"] },
    });
  });

  it("supports a custom field name", () => {
    const result = applyDepartmentScope(
      { scopedDepartments: `["d1"]` },
      { status: "active" },
      "deptId",
    );
    expect(result).toEqual({ status: "active", deptId: { in: ["d1"] } });
  });
});

describe("applyRecruitmentScope", () => {
  const session = {
    id: "u1",
    role: "admin",
    office: null as string | null,
    scopedDepartments: null as string | null,
  };

  it("returns where unchanged for global admin", () => {
    expect(applyRecruitmentScope(session, { status: "active" })).toEqual({ status: "active" });
  });

  it("adds office OR clause when office is set", () => {
    const result = applyRecruitmentScope(
      { ...session, office: "Singapore" },
      { status: "active" },
    );
    expect(result).toEqual({
      status: "active",
      OR: [{ office: "Singapore" }, { office: null }],
    });
  });

  it("adds jobRole.departmentId scope when scopedDepartments is set", () => {
    const result = applyRecruitmentScope(
      { ...session, scopedDepartments: `["d1","d2"]` },
      { status: "active" },
    );
    expect(result).toEqual({
      status: "active",
      jobRole: { departmentId: { in: ["d1", "d2"] } },
    });
  });

  it("composes office AND department scope when both set", () => {
    const result = applyRecruitmentScope(
      { ...session, office: "Dubai", scopedDepartments: `["d1"]` },
      {},
    );
    expect(result).toEqual({
      OR: [{ office: "Dubai" }, { office: null }],
      jobRole: { departmentId: { in: ["d1"] } },
    });
  });
});

```