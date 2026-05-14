---
type: source
source_type: laptop
title: leave-calendar.test
slug: leave-calendar-test
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/__tests__/leave-calendar.test.ts
original_size: 2380
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# leave-calendar.test

_Extracted from `[[assessify|assessify]]/src/lib/__tests__/leave-calendar.test.ts` on 2026-05-14._

```typescript
import { describe, expect, it } from "vitest";
import { buildLeaveCalendar } from "@/lib/leave";

describe("buildLeaveCalendar", () => {
  it("builds manager rows and detects overlaps on matching business days", () => {
    const startDate = new Date("2026-05-11T00:00:00.000Z");
    const result = buildLeaveCalendar(
      [
        {
          id: "req-1",
          leaveType: "Annual Leave",
          startDate: new Date("2026-05-11T00:00:00.000Z"),
          endDate: new Date("2026-05-12T00:00:00.000Z"),
          status: "approved",
          employee: { fullName: "Alice Tan", firstName: "Alice" },
          lineManager: { id: "mgr-1", name: "Mariam" },
        },
        {
          id: "req-2",
          leaveType: "Sick Leave",
          startDate: new Date("2026-05-12T00:00:00.000Z"),
          endDate: new Date("2026-05-13T00:00:00.000Z"),
          status: "pending_manager",
          employee: { fullName: "Bob Lim", firstName: "Bob" },
          lineManager: { id: "mgr-1", name: "Mariam" },
        },
      ],
      startDate,
      5,
    );

    expect(result.days).toHaveLength(5);
    expect(result.rows).toHaveLength(1);
    expect(result.rows[0].managerName).toBe("Mariam");
    expect(result.rows[0].approvedCount).toBe(1);
    expect(result.rows[0].pendingCount).toBe(1);
    expect(result.rows[0].cells["2026-05-12"].entries).toHaveLength(2);
    expect(result.overlaps).toHaveLength(1);
    expect(result.overlaps[0].employees).toEqual(["Alice Tan", "Bob Lim"]);
  });

  it("skips weekends when building the grid and occupancy", () => {
    const result = buildLeaveCalendar(
      [
        {
          id: "req-1",
          leaveType: "Annual Leave",
          startDate: new Date("2026-05-15T00:00:00.000Z"),
          endDate: new Date("2026-05-18T00:00:00.000Z"),
          status: "approved",
          employee: { fullName: null, firstName: "Cara" },
          lineManager: { id: "mgr-1", name: "Mariam" },
        },
      ],
      new Date("2026-05-15T00:00:00.000Z"),
      3,
    );

    expect(result.days.map((day) => day.dateKey)).toEqual([
      "2026-05-15",
      "2026-05-18",
      "2026-05-19",
    ]);
    expect(result.rows[0].cells["2026-05-15"].entries).toHaveLength(1);
    expect(result.rows[0].cells["2026-05-18"].entries).toHaveLength(1);
    expect(result.rows[0].cells["2026-05-17"]).toBeUndefined();
  });
});

```