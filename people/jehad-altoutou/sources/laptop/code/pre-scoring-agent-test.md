---
type: source
source_type: laptop
title: pre-scoring-agent.test
slug: pre-scoring-agent-test
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/__tests__/pre-scoring-agent.test.ts
original_size: 13709
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# pre-scoring-agent.test

_Extracted from `[[assessify|assessify]]/src/lib/__tests__/pre-scoring-agent.test.ts` on 2026-05-14._

```typescript
import { describe, expect, it } from "vitest";
import {
  buildPrompt,
  computeComposite,
  parseCriteria,
  parseReport,
  pickTopCriteria,
} from "@/lib/recruitment/pre-scoring-agent";
import type { FullPreScreeningReport } from "@/lib/recruitment";

const SAMPLE_CRITERIA = [
  { key: "experience_years", label: "Years of relevant experience", weight: 0.3, scoringPrompt: "Years vs JD" },
  { key: "skill_match", label: "Skills coverage vs JD", weight: 0.35, scoringPrompt: "Fraction of must-haves" },
  { key: "education_alignment", label: "Education alignment", weight: 0.15, scoringPrompt: "Degree fit" },
  { key: "language_fit", label: "Language fit", weight: 0.1, scoringPrompt: "English required" },
  { key: "tenure_stability", label: "Tenure stability", weight: 0.1, scoringPrompt: "Avoid hopping" },
];

const SAMPLE_APPLICATION = {
  candidate: {
    firstName: "Ada",
    lastName: "Lovelace",
    email: "ada@example.com",
    phoneNumber: "+44 20 7946 0958",
    nationality: "British",
    noticePeriod: "1 month",
    office: "Dubai",
    source: "agency",
    agencyName: "Acme Search",
    linkedinUrl: "https://linkedin.com/in/ada",
  },
  office: "Dubai",
  source: "agency",
  agencyName: "Acme Search",
  jobRole: {
    title: "Senior Software Engineer",
    department: { name: "Engineering" },
    description: "Design and build platform services.",
    jdSummary: "Build durable platform services that scale.",
    jdResponsibilities: "- Lead architecture\n- Mentor team\n- Ship roadmap",
    jdRequirements: "- 5+ years TypeScript\n- Distributed systems experience",
    jdNiceToHaves: "- Public-cloud certifications",
    jdYearsExperience: "5–8 years",
  },
};

function fullReportFixture(scoreOverrides?: Partial<Record<string, number>>): FullPreScreeningReport {
  const scoresByKey: Record<string, number> = {
    experience_years: 7,
    skill_match: 6,
    education_alignment: 8,
    language_fit: 9,
    tenure_stability: 5,
    ...(scoreOverrides ?? {}),
  };
  return {
    scoreOutOf100: 70,
    scoreOutOf10: 7,
    recommendation: "hire",
    candidateSnapshot: [
      { label: "Candidate", value: "Ada Lovelace" },
      { label: "Applying For", value: "Senior Software Engineer — Engineering" },
    ],
    careerArc: { phases: [{ title: "Phase 1 — Analytics (2019-2022)", narrative: "Built X, Y." }] },
    scorecard: SAMPLE_CRITERIA.map((c) => ({
      key: c.key,
      label: c.label,
      weight: c.weight,
      score: scoresByKey[c.key],
      commentary: `Commentary for ${c.label}`,
    })),
    positioningSummary: "Strong analytical foundation.",
    structuralGaps: [
      { title: "Gap 1 — No leadership", detail: "..." },
      { title: "Gap 2 — Light cloud experience", detail: "..." },
      { title: "Gap 3 — No distributed systems experience", detail: "..." },
    ],
    whyToHire: ["Quantitatively strong"],
    riskRegister: [{ risk: "Short tenure", severity: "MEDIUM", detail: "...", mitigation: "..." }],
    interviewQuestions: [{ theme: "Deal Ownership", question: "Walk me through X", listenFor: "Y" }],
    decisionFramework: [{ outcome: "Strong on probes", recommendation: "Advance" }],
    compensation: [{ component: "Base Salary", proposed: "AED 30,000", rationale: "Aligns" }],
    onboardingPlan: [{ phase: "Days 1-14", title: "Immersion", narrative: "..." }],
    finalAssessment: "Hire with onboarding plan.",
  };
}

describe("parseCriteria", () => {
  it("parses a valid criteria JSON array", () => {
    const json = JSON.stringify(SAMPLE_CRITERIA);
    const parsed = parseCriteria(json);
    expect(parsed).toHaveLength(5);
    expect(parsed[0].key).toBe("experience_years");
    expect(parsed[0].weight).toBe(0.3);
  });

  it("throws on non-array JSON", () => {
    expect(() => parseCriteria(`{"foo":"bar"}`)).toThrow("not an array");
  });

  it("throws on malformed criterion (missing weight)", () => {
    const bad = JSON.stringify([{ key: "x", label: "X" }]);
    expect(() => parseCriteria(bad)).toThrow(/malformed/);
  });

  it("falls back scoringPrompt to label when missing", () => {
    const json = JSON.stringify([{ key: "k", label: "Lbl", weight: 1 }]);
    const parsed = parseCriteria(json);
    expect(parsed[0].scoringPrompt).toBe("Lbl");
  });

  it("preserves optional commentaryGuidance and redFlagSignals", () => {
    const json = JSON.stringify([
      {
        key: "k",
        label: "L",
        weight: 1,
        scoringPrompt: "S",
        commentaryGuidance: "Mention X",
        redFlagSignals: ["red 1", "red 2"],
      },
    ]);
    const parsed = parseCriteria(json);
    expect(parsed[0].commentaryGuidance).toBe("Mention X");
    expect(parsed[0].redFlagSignals).toEqual(["red 1", "red 2"]);
  });
});

describe("buildPrompt", () => {
  it("includes role title, department, and JD sections", () => {
    const p = buildPrompt({ application: SAMPLE_APPLICATION, criteria: SAMPLE_CRITERIA });
    expect(p).toContain("Senior Software Engineer");
    expect(p).toContain("Engineering");
    expect(p).toContain("Build durable platform services");
    expect(p).toContain("Lead architecture");
    expect(p).toContain("5+ years TypeScript");
    expect(p).toContain("Public-cloud certifications");
    expect(p).toContain("5–8 years");
  });

  it("includes candidate fields (name, email, nationality, notice period, source/agency)", () => {
    const p = buildPrompt({ application: SAMPLE_APPLICATION, criteria: SAMPLE_CRITERIA });
    expect(p).toContain("Ada Lovelace");
    expect(p).toContain("ada@example.com");
    expect(p).toContain("British");
    expect(p).toContain("1 month");
    expect(p).toContain("Acme Search");
  });

  it("lists every criterion with key + weight + prompt", () => {
    const p = buildPrompt({ application: SAMPLE_APPLICATION, criteria: SAMPLE_CRITERIA });
    for (const c of SAMPLE_CRITERIA) {
      expect(p).toContain(c.key);
      expect(p).toContain(c.label);
    }
  });

  it("falls back to short description when no structured JD", () => {
    const noJd = {
      ...SAMPLE_APPLICATION,
      jobRole: {
        ...SAMPLE_APPLICATION.jobRole,
        jdSummary: null,
        jdResponsibilities: null,
        jdRequirements: null,
        jdNiceToHaves: null,
        jdYearsExperience: null,
      },
    };
    const p = buildPrompt({ application: noJd, criteria: SAMPLE_CRITERIA });
    expect(p).toContain("Design and build platform services.");
  });

  it("falls back to a placeholder line when neither JD nor description is set", () => {
    const empty = {
      ...SAMPLE_APPLICATION,
      jobRole: {
        ...SAMPLE_APPLICATION.jobRole,
        description: null,
        jdSummary: null,
        jdResponsibilities: null,
        jdRequirements: null,
        jdNiceToHaves: null,
        jdYearsExperience: null,
      },
    };
    const p = buildPrompt({ application: empty, criteria: SAMPLE_CRITERIA });
    expect(p).toContain("(no structured JD on file");
  });

  it("instructs JSON-only output and demands the full HR-format shape", () => {
    const p = buildPrompt({ application: SAMPLE_APPLICATION, criteria: SAMPLE_CRITERIA });
    expect(p).toContain("Return ONLY the JSON object");
    expect(p).toContain('"scoreOutOf100"');
    expect(p).toContain('"scorecard"');
    expect(p).toContain('"structuralGaps"');
    expect(p).toContain('"riskRegister"');
    expect(p).toContain('"interviewQuestions"');
    expect(p).toContain('"compensation"');
    expect(p).toContain('"onboardingPlan"');
  });

  it("surfaces redFlagSignals from the rubric in the criterion section", () => {
    const c = [
      {
        ...SAMPLE_CRITERIA[0],
        redFlagSignals: ["job-hopping", "lack of certifications"],
      },
      ...SAMPLE_CRITERIA.slice(1),
    ];
    const p = buildPrompt({ application: SAMPLE_APPLICATION, criteria: c });
    expect(p).toContain("job-hopping");
    expect(p).toContain("lack of certifications");
  });
});

describe("parseReport", () => {
  it("parses a clean full-report JSON", () => {
    const fixture = fullReportFixture();
    const raw = JSON.stringify(fixture);
    const parsed = parseReport(raw, SAMPLE_CRITERIA);
    expect(parsed.scorecard).toHaveLength(SAMPLE_CRITERIA.length);
    expect(parsed.recommendation).toBe("hire");
    expect(parsed.structuralGaps).toHaveLength(3);
  });

  it("strips markdown fences", () => {
    const fixture = fullReportFixture();
    const raw = "```json\n" + JSON.stringify(fixture) + "\n```";
    const parsed = parseReport(raw, SAMPLE_CRITERIA);
    expect(parsed.scorecard).toHaveLength(SAMPLE_CRITERIA.length);
  });

  it("salvages JSON wrapped in commentary", () => {
    const fixture = fullReportFixture();
    const raw = "Here you go:\n" + JSON.stringify(fixture) + "\nLet me know if you need more.";
    const parsed = parseReport(raw, SAMPLE_CRITERIA);
    expect(parsed.recommendation).toBe("hire");
  });

  it("throws when scorecard length doesn't match rubric criteria count", () => {
    const fixture = fullReportFixture();
    fixture.scorecard = fixture.scorecard.slice(0, 2);
    const raw = JSON.stringify(fixture);
    expect(() => parseReport(raw, SAMPLE_CRITERIA)).toThrow(/scorecard length/);
  });

  it("backfills missing label and weight from rubric", () => {
    const fixture = fullReportFixture();
    fixture.scorecard.forEach((s) => {
      delete (s as unknown as { label?: string }).label;
      delete (s as unknown as { weight?: number }).weight;
    });
    const raw = JSON.stringify(fixture);
    const parsed = parseReport(raw, SAMPLE_CRITERIA);
    expect(parsed.scorecard[0].label).toBe("Years of relevant experience");
    expect(parsed.scorecard[0].weight).toBe(0.3);
  });

  it("normalises 'MEDIUM HIGH' severity to 'MEDIUM-HIGH'", () => {
    const fixture = fullReportFixture();
    (fixture.riskRegister[0] as unknown as { severity: string }).severity = "MEDIUM HIGH";
    const raw = JSON.stringify(fixture);
    const parsed = parseReport(raw, SAMPLE_CRITERIA);
    expect(parsed.riskRegister[0].severity).toBe("MEDIUM-HIGH");
  });

  it("falls back to MEDIUM for unknown severities", () => {
    const fixture = fullReportFixture();
    (fixture.riskRegister[0] as unknown as { severity: string }).severity = "WTF";
    const raw = JSON.stringify(fixture);
    const parsed = parseReport(raw, SAMPLE_CRITERIA);
    expect(parsed.riskRegister[0].severity).toBe("MEDIUM");
  });

  it("falls back to 'consider' for unknown recommendation", () => {
    const fixture = fullReportFixture();
    (fixture as unknown as { recommendation: string }).recommendation = "MAYBE";
    const raw = JSON.stringify(fixture);
    const parsed = parseReport(raw, SAMPLE_CRITERIA);
    expect(parsed.recommendation).toBe("consider");
  });

  it("backfills missing optional sections with empty defaults", () => {
    const fixture = fullReportFixture();
    delete (fixture as Partial<FullPreScreeningReport>).structuralGaps;
    delete (fixture as Partial<FullPreScreeningReport>).riskRegister;
    delete (fixture as Partial<FullPreScreeningReport>).whyToHire;
    const raw = JSON.stringify(fixture);
    const parsed = parseReport(raw, SAMPLE_CRITERIA);
    expect(parsed.structuralGaps).toEqual([]);
    expect(parsed.riskRegister).toEqual([]);
    expect(parsed.whyToHire).toEqual([]);
  });
});

describe("computeComposite", () => {
  it("computes weighted /100 from scorecard scores 0-10", () => {
    const fixture = fullReportFixture({
      experience_years: 10,
      skill_match: 5,
      education_alignment: 10,
      language_fit: 10,
      tenure_stability: 0,
    });
    // (10*0.3 + 5*0.35 + 10*0.15 + 10*0.1 + 0*0.1) = 3 + 1.75 + 1.5 + 1 + 0 = 7.25
    // 7.25 / 10 / 1.0 = 0.725 → /100 = 72.5
    const result = computeComposite(fixture.scorecard, SAMPLE_CRITERIA);
    expect(result).toBeCloseTo(72.5, 1);
  });

  it("clamps individual scorecard scores to [0,10]", () => {
    const fixture = fullReportFixture({
      experience_years: 15,   // clamped to 10 → contributes 10*0.3 = 3
      skill_match: -2,         // clamped to 0
      education_alignment: 5,  // 5*0.15 = 0.75
      language_fit: 5,         // 5*0.1 = 0.5
      tenure_stability: 5,     // 5*0.1 = 0.5
    });
    // (3 + 0 + 0.75 + 0.5 + 0.5) = 4.75 → /10 = 0.475 → 47.5
    const result = computeComposite(fixture.scorecard, SAMPLE_CRITERIA);
    expect(result).toBeCloseTo(47.5, 1);
  });

  it("returns 0 when criteria total weight is 0", () => {
    expect(computeComposite([], [])).toBe(0);
  });

  it("ignores scorecard entries that don't match a criterion key", () => {
    const fixture = fullReportFixture();
    fixture.scorecard.push({
      key: "totally_unknown",
      label: "Nope",
      weight: 0.5,
      score: 10,
      commentary: "",
    });
    // Adding an unknown key should NOT affect the composite (only criteria keys count)
    const baseline = computeComposite(fullReportFixture().scorecard, SAMPLE_CRITERIA);
    const augmented = computeComposite(fixture.scorecard, SAMPLE_CRITERIA);
    expect(augmented).toBeCloseTo(baseline, 5);
  });
});

describe("pickTopCriteria", () => {
  it("returns top-3 highest-scoring criteria with score normalised to 0-1", () => {
    const fixture = fullReportFixture({
      experience_years: 6,
      skill_match: 9,
      education_alignment: 4,
      language_fit: 9.5,
      tenure_stability: 3,
    });
    const top = pickTopCriteria(fixture.scorecard);
    expect(top).toHaveLength(3);
    expect(top[0].label).toBe("Language fit");
    expect(top[0].score).toBeCloseTo(0.95, 2);
    expect(top[1].label).toBe("Skills coverage vs JD");
    expect(top[2].label).toBe("Years of relevant experience");
  });
});

```