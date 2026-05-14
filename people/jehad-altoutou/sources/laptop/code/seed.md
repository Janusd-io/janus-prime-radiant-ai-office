---
type: source
source_type: laptop
title: seed
slug: seed
created: 2026-04-10
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/prisma/seed.ts
original_size: 40244
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:32Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# seed

_Extracted from `[[assessify|assessify]]/prisma/seed.ts` on 2026-05-14._

```typescript
import "dotenv/config";
import { PrismaClient } from "../src/generated/prisma/client.js";
import { PrismaLibSql } from "@prisma/adapter-libsql";

const adapter = new PrismaLibSql({ url: "file:./dev.db" });
const prisma = new PrismaClient({ adapter });

async function main() {
  console.log("Seeding database...");

  // ─── Department ──────────────────────────────────────────
  const itDept = await prisma.department.create({
    data: {
      name: "Information Technology",
      slug: "information-technology",
    },
  });

  const opsDept = await prisma.department.create({
    data: {
      name: "Operations",
      slug: "operations",
    },
  });

  const hrDept = await prisma.department.create({
    data: {
      name: "Human Resources",
      slug: "human-resources",
    },
  });

  const financeDept = await prisma.department.create({
    data: {
      name: "Finance",
      slug: "finance",
    },
  });

  // ─── Job Roles ───────────────────────────────────────────
  const itSupport = await prisma.jobRole.create({
    data: {
      departmentId: itDept.id,
      title: "IT Support Specialist",
      slug: "it-support-specialist",
      description:
        "Front-line technical support responsible for troubleshooting hardware, software, and network issues while delivering outstanding end-user service.",
    },
  });

  await prisma.jobRole.create({
    data: {
      departmentId: opsDept.id,
      title: "Operations Coordinator",
      slug: "operations-coordinator",
      description:
        "Manages day-to-day operational workflows, vendor coordination, and process optimization across the organization.",
    },
  });

  await prisma.jobRole.create({
    data: {
      departmentId: opsDept.id,
      title: "Automation Specialist",
      slug: "automation-specialist",
      description:
        "Designs and implements workflow automations using tools like n8n, Zapier, and custom integrations to streamline operations.",
    },
  });

  await prisma.jobRole.create({
    data: {
      departmentId: hrDept.id,
      title: "HR Generalist",
      slug: "hr-generalist",
      description:
        "Supports the full employee lifecycle including recruitment, onboarding, employee relations, and compliance.",
    },
  });

  await prisma.jobRole.create({
    data: {
      departmentId: hrDept.id,
      title: "Talent Acquisition Specialist",
      slug: "talent-acquisition-specialist",
      description:
        "Leads sourcing, screening, and hiring processes to attract top talent across all departments.",
    },
  });

  await prisma.jobRole.create({
    data: {
      departmentId: financeDept.id,
      title: "Financial Analyst",
      slug: "financial-analyst",
      description:
        "Analyzes financial data, prepares reports, and supports budgeting and forecasting activities.",
    },
  });

  // ─── Competencies ────────────────────────────────────────
  const competencies = await Promise.all(
    [
      { name: "Communication", slug: "communication", category: "Soft Skills", description: "Clear, empathetic, and professional communication with end-users and stakeholders" },
      { name: "Troubleshooting", slug: "troubleshooting", category: "Technical", description: "Systematic approach to diagnosing and resolving technical issues" },
      { name: "Prioritization", slug: "prioritization", category: "Operational", description: "Ability to triage and manage competing demands effectively" },
      { name: "Security Awareness", slug: "security-awareness", category: "Technical", description: "Understanding of security best practices and threat recognition" },
      { name: "Accountability", slug: "accountability", category: "Cultural", description: "Takes ownership of tasks and follows through on commitments" },
      { name: "Collaboration", slug: "collaboration", category: "Cultural", description: "Works effectively with team members and cross-functional partners" },
      { name: "Adaptability", slug: "adaptability", category: "Cultural", description: "Responds positively to change and ambiguity" },
      { name: "AI Readiness", slug: "ai-readiness", category: "Emerging", description: "Openness and practical readiness to work with AI-powered tools" },
      { name: "Critical Thinking", slug: "critical-thinking", category: "Cognitive", description: "Evaluates information objectively and makes sound judgments" },
      { name: "Service Mindset", slug: "service-mindset", category: "Soft Skills", description: "Genuine commitment to helping others and delivering quality support" },
      { name: "Escalation Judgment", slug: "escalation-judgment", category: "Operational", description: "Knows when and how to escalate issues appropriately" },
      { name: "Documentation", slug: "documentation", category: "Operational", description: "Creates clear, useful records of issues and resolutions" },
      { name: "Professionalism", slug: "professionalism", category: "Cultural", description: "Maintains composure and professional standards under pressure" },
      { name: "Empathy", slug: "empathy", category: "Soft Skills", description: "Understands and relates to end-user frustrations and needs" },
      { name: "Learning Agility", slug: "learning-agility", category: "Cognitive", description: "Quickly acquires new skills and adapts to new technologies" },
    ].map((c) => prisma.competency.create({ data: c }))
  );

  const comp = Object.fromEntries(competencies.map((c) => [c.slug, c]));

  // ─── Assessment Template ─────────────────────────────────
  const template = await prisma.assessmentTemplate.create({
    data: {
      jobRoleId: itSupport.id,
      title: "IT Support Specialist Assessment",
      slug: "it-support-specialist-v1",
      description:
        "Comprehensive assessment evaluating cultural fit, AI readiness, and technical capabilities for IT Support Specialist candidates.",
    },
  });

  // ─── Assessment Version ──────────────────────────────────
  const version = await prisma.assessmentVersion.create({
    data: {
      templateId: template.id,
      versionNumber: 1,
      status: "published",
      passingScore: 0.6,
      timeLimit: 45,
      publishedAt: new Date(),
    },
  });

  // ─── SECTION 1: Cultural Fit ─────────────────────────────
  const cultureFit = await prisma.section.create({
    data: {
      versionId: version.id,
      title: "Cultural Fit",
      slug: "cultural-fit",
      description: "Understanding how you approach work, collaboration, and challenges.",
      introText:
        "In this section, we want to understand how you think about work and collaboration. There are no trick questions — we're looking for authenticity and self-awareness. Take your time and answer honestly.",
      iconName: "heart-handshake",
      sortOrder: 1,
      weight: 0.3,
    },
  });

  const cultureFitQuestions = [
    {
      slug: "cf-missed-deadline",
      title: "Missed Deadline Scenario",
      prompt:
        "You realize at 4 PM that you won't finish a task your manager expected by end of day. What do you do?",
      questionType: "single_select",
      difficulty: "medium",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 1,
      explanation: "This question assesses accountability and communication under pressure.",
      competencies: [
        { slug: "accountability", weight: 1.0 },
        { slug: "communication", weight: 0.8 },
        { slug: "professionalism", weight: 0.5 },
      ],
      options: [
        { key: "a", label: "Rush to finish it, even if the quality is poor", value: "rush_finish", points: 2, isCorrect: false },
        { key: "b", label: "Immediately message your manager, explain where you are, and propose a realistic timeline", value: "communicate_proactively", points: 10, isCorrect: true },
        { key: "c", label: "Wait until tomorrow morning and hope nobody notices", value: "ignore_hope", points: 0, isCorrect: false },
        { key: "d", label: "Ask a colleague to finish it for you without telling your manager", value: "delegate_secretly", points: 1, isCorrect: false },
      ],
    },
    {
      slug: "cf-coworker-struggle",
      title: "Struggling Coworker",
      prompt:
        "A coworker is visibly struggling with a task you're familiar with, but they haven't asked for help. What's your approach?",
      questionType: "single_select",
      difficulty: "easy",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 2,
      explanation: "Measures empathy, collaboration, and proactive support tendencies.",
      competencies: [
        { slug: "collaboration", weight: 1.0 },
        { slug: "empathy", weight: 1.0 },
        { slug: "service-mindset", weight: 0.5 },
      ],
      options: [
        { key: "a", label: "Mind your own business — they didn't ask", value: "ignore", points: 1, isCorrect: false },
        { key: "b", label: "Casually offer help without making them feel embarrassed: 'Hey, I've dealt with this before — want to tackle it together?'", value: "offer_tactfully", points: 10, isCorrect: true },
        { key: "c", label: "Tell your manager that your coworker is struggling", value: "report_to_manager", points: 2, isCorrect: false },
        { key: "d", label: "Do the task for them to save time", value: "do_it_for_them", points: 4, isCorrect: false },
      ],
    },
    {
      slug: "cf-conflicting-instructions",
      title: "Conflicting Instructions",
      prompt:
        "Two managers give you contradictory instructions on the same task. How do you handle it?",
      questionType: "single_select",
      difficulty: "hard",
      maxPoints: 10,
      weight: 1.2,
      scoringStrategy: "weighted_options",
      sortOrder: 3,
      explanation: "Tests adaptability, communication, and professional judgment in ambiguous situations.",
      competencies: [
        { slug: "adaptability", weight: 1.0 },
        { slug: "communication", weight: 1.0 },
        { slug: "critical-thinking", weight: 0.7 },
      ],
      options: [
        { key: "a", label: "Follow the instruction from whoever you like more", value: "pick_favorite", points: 0, isCorrect: false },
        { key: "b", label: "Do nothing until they sort it out", value: "freeze", points: 2, isCorrect: false },
        { key: "c", label: "Acknowledge both, flag the conflict to both managers, and ask them to align on priority", value: "flag_and_align", points: 10, isCorrect: true },
        { key: "d", label: "Follow the most recent instruction without questioning it", value: "follow_latest", points: 4, isCorrect: false },
      ],
    },
    {
      slug: "cf-feedback-reaction",
      title: "Receiving Critical Feedback",
      prompt:
        "During a review, your manager points out a pattern of small errors in your recent work. How do you respond?",
      questionType: "single_select",
      difficulty: "medium",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 4,
      explanation: "Assesses learning agility, accountability, and professionalism when receiving feedback.",
      competencies: [
        { slug: "accountability", weight: 1.0 },
        { slug: "learning-agility", weight: 1.0 },
        { slug: "professionalism", weight: 0.8 },
      ],
      options: [
        { key: "a", label: "Get defensive — you've been working hard and they should recognize that", value: "defensive", points: 0, isCorrect: false },
        { key: "b", label: "Thank them for the feedback, ask for specific examples, and create a plan to improve", value: "constructive_response", points: 10, isCorrect: true },
        { key: "c", label: "Agree in the moment but don't change anything", value: "agree_ignore", points: 2, isCorrect: false },
        { key: "d", label: "Blame your workload for the errors", value: "blame_workload", points: 3, isCorrect: false },
      ],
    },
    {
      slug: "cf-ambiguous-task",
      title: "Ambiguous Task",
      prompt:
        "You're assigned a task with very little context or documentation. The person who normally handles it is on vacation. What do you do?",
      questionType: "single_select",
      difficulty: "medium",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 5,
      explanation: "Measures adaptability, critical thinking, and resourcefulness.",
      competencies: [
        { slug: "adaptability", weight: 1.0 },
        { slug: "critical-thinking", weight: 0.8 },
        { slug: "accountability", weight: 0.6 },
      ],
      options: [
        { key: "a", label: "Wait for the person to come back from vacation", value: "wait", points: 1, isCorrect: false },
        { key: "b", label: "Research what you can, attempt a reasonable approach, document your decisions, and flag any assumptions", value: "research_attempt_document", points: 10, isCorrect: true },
        { key: "c", label: "Skip it and work on something else", value: "skip", points: 0, isCorrect: false },
        { key: "d", label: "Do it your own way without documenting anything", value: "wing_it", points: 3, isCorrect: false },
      ],
    },
    {
      slug: "cf-values-ranking",
      title: "Workplace Values Ranking",
      prompt: "Rank the following workplace values in order of personal importance to you (most important first):",
      questionType: "ranking",
      difficulty: "easy",
      maxPoints: 8,
      weight: 0.8,
      scoringStrategy: "scenario_based",
      correctAnswerKey: JSON.stringify(["reliability", "teamwork", "growth", "recognition"]),
      sortOrder: 6,
      explanation: "Reveals value priorities. We value reliability and teamwork highest for this role.",
      competencies: [
        { slug: "accountability", weight: 0.8 },
        { slug: "collaboration", weight: 0.8 },
      ],
      options: [
        { key: "reliability", label: "Being someone others can count on", value: "reliability", points: 0, isCorrect: false, sortOrder: 1 },
        { key: "teamwork", label: "Working well as part of a team", value: "teamwork", points: 0, isCorrect: false, sortOrder: 2 },
        { key: "growth", label: "Continuous personal and professional growth", value: "growth", points: 0, isCorrect: false, sortOrder: 3 },
        { key: "recognition", label: "Being recognized for your contributions", value: "recognition", points: 0, isCorrect: false, sortOrder: 4 },
      ],
    },
  ];

  // ─── SECTION 2: AI Awareness ─────────────────────────────
  const aiAwareness = await prisma.section.create({
    data: {
      versionId: version.id,
      title: "AI Awareness",
      slug: "ai-awareness",
      description: "Exploring your readiness to work alongside AI-powered tools and workflows.",
      introText:
        "AI is becoming part of everyday work. This section isn't about technical AI knowledge — it's about your mindset, awareness, and readiness to work in AI-enabled environments. Answer based on your genuine perspective.",
      iconName: "brain-circuit",
      sortOrder: 2,
      weight: 0.25,
    },
  });

  const aiAwarenessQuestions = [
    {
      slug: "ai-chatbot-suggestion",
      title: "AI Chatbot Suggestion",
      prompt:
        "Your company introduces an AI chatbot to help IT Support handle common ticket queries. A colleague says: 'This thing is going to replace us.' What's your take?",
      questionType: "single_select",
      difficulty: "medium",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 1,
      explanation: "Tests openness to AI and understanding that AI augments rather than replaces human judgment.",
      competencies: [
        { slug: "ai-readiness", weight: 1.0 },
        { slug: "adaptability", weight: 0.7 },
        { slug: "critical-thinking", weight: 0.5 },
      ],
      options: [
        { key: "a", label: "They're right — we should be worried about our jobs", value: "fearful", points: 1, isCorrect: false },
        { key: "b", label: "It'll handle the repetitive stuff so we can focus on more complex issues — let's learn how to use it well", value: "balanced_optimism", points: 10, isCorrect: true },
        { key: "c", label: "AI is overhyped, just ignore it", value: "dismissive", points: 0, isCorrect: false },
        { key: "d", label: "I'd want to test it first before forming an opinion", value: "cautious_open", points: 7, isCorrect: false },
      ],
    },
    {
      slug: "ai-email-draft",
      title: "AI-Generated Email",
      prompt:
        "You use an AI tool to draft a technical response to a frustrated user. The draft sounds professional but contains a factual error about the resolution steps. What do you do?",
      questionType: "single_select",
      difficulty: "medium",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 2,
      explanation: "Assesses responsible AI use and critical verification of AI output.",
      competencies: [
        { slug: "ai-readiness", weight: 0.8 },
        { slug: "critical-thinking", weight: 1.0 },
        { slug: "accountability", weight: 0.6 },
      ],
      options: [
        { key: "a", label: "Send it as-is — the AI probably knows better", value: "blind_trust", points: 0, isCorrect: false },
        { key: "b", label: "Fix the error, verify the rest, then send it — always review AI output before sending", value: "verify_correct", points: 10, isCorrect: true },
        { key: "c", label: "Throw away the draft and write your own from scratch", value: "discard_all", points: 4, isCorrect: false },
        { key: "d", label: "Report the AI tool as broken to your manager", value: "report_broken", points: 2, isCorrect: false },
      ],
    },
    {
      slug: "ai-sensitive-data",
      title: "AI and Sensitive Data",
      prompt:
        "A coworker shares that they pasted a customer's full account details into a public AI chatbot to troubleshoot an issue faster. What's the right response?",
      questionType: "single_select",
      difficulty: "hard",
      maxPoints: 10,
      weight: 1.2,
      scoringStrategy: "weighted_options",
      sortOrder: 3,
      explanation: "Tests security awareness in the context of AI tool usage.",
      competencies: [
        { slug: "security-awareness", weight: 1.0 },
        { slug: "ai-readiness", weight: 0.6 },
        { slug: "professionalism", weight: 0.5 },
      ],
      options: [
        { key: "a", label: "That's fine — AI tools are secure", value: "ignore_risk", points: 0, isCorrect: false },
        { key: "b", label: "Explain the privacy risk, suggest they use approved internal tools, and recommend they report the data exposure to the security team", value: "flag_educate_report", points: 10, isCorrect: true },
        { key: "c", label: "Report them to HR immediately without talking to them", value: "report_only", points: 4, isCorrect: false },
        { key: "d", label: "Say nothing — it's not your problem", value: "ignore", points: 0, isCorrect: false },
      ],
    },
    {
      slug: "ai-workflow-improvement",
      title: "AI Workflow Improvement",
      prompt:
        "Your team currently categorizes incoming support tickets manually, which takes significant time each morning. How would you feel about introducing an AI system that auto-categorizes them?",
      questionType: "situational_judgment",
      difficulty: "easy",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 4,
      explanation: "Measures practical AI readiness and process improvement mindset.",
      competencies: [
        { slug: "ai-readiness", weight: 1.0 },
        { slug: "adaptability", weight: 0.8 },
        { slug: "service-mindset", weight: 0.3 },
      ],
      options: [
        { key: "a", label: "Excited — I'd volunteer to help test and refine the categorization rules", value: "enthusiastic_contribute", points: 10, isCorrect: true },
        { key: "b", label: "Cautiously optimistic — I'd want to see accuracy metrics before trusting it", value: "cautious_positive", points: 8, isCorrect: false },
        { key: "c", label: "Indifferent — whatever management decides is fine", value: "passive", points: 3, isCorrect: false },
        { key: "d", label: "Opposed — I prefer the manual process because I know it works", value: "resistant", points: 1, isCorrect: false },
      ],
    },
    {
      slug: "ai-limitations",
      title: "Understanding AI Limitations",
      prompt:
        "Which of the following best describes a key limitation of current AI tools in a support environment? Select all that apply.",
      questionType: "multi_select",
      difficulty: "medium",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "partial",
      correctAnswerKey: JSON.stringify(["a", "c", "d"]),
      sortOrder: 5,
      explanation: "Tests understanding of real AI limitations versus misconceptions.",
      competencies: [
        { slug: "ai-readiness", weight: 1.0 },
        { slug: "critical-thinking", weight: 0.8 },
      ],
      options: [
        { key: "a", label: "AI can generate confident-sounding but incorrect answers", value: "hallucination", points: 3.33, isCorrect: true },
        { key: "b", label: "AI cannot help with any repetitive tasks", value: "no_repetitive", points: 0, isCorrect: false },
        { key: "c", label: "AI may not have context about your company's specific policies", value: "no_company_context", points: 3.33, isCorrect: true },
        { key: "d", label: "AI output should always be reviewed before acting on it", value: "needs_review", points: 3.34, isCorrect: true },
      ],
    },
  ];

  // ─── SECTION 3: IT Support Role-Specific ─────────────────
  const itRole = await prisma.section.create({
    data: {
      versionId: version.id,
      title: "IT Support Skills",
      slug: "it-support-skills",
      description: "Testing your technical troubleshooting, communication, and support fundamentals.",
      introText:
        "Time to put your IT support skills to the test. You'll encounter realistic scenarios you'd face on the job. Think through each situation carefully — we're evaluating your thought process as much as your answers.",
      iconName: "monitor-cog",
      sortOrder: 3,
      weight: 0.45,
    },
  });

  const itSupportQuestions = [
    {
      slug: "it-wifi-troubleshoot",
      title: "Wi-Fi Connectivity Issue",
      prompt:
        'A user reports: "My Wi-Fi keeps disconnecting every few minutes. I\'ve already restarted my laptop." What is your best first troubleshooting step?',
      questionType: "single_select",
      difficulty: "easy",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 1,
      explanation: "Tests systematic troubleshooting approach starting with gathering information.",
      competencies: [
        { slug: "troubleshooting", weight: 1.0 },
        { slug: "communication", weight: 0.5 },
      ],
      options: [
        { key: "a", label: "Tell them to restart their laptop again", value: "restart_again", points: 1, isCorrect: false },
        { key: "b", label: "Ask if other devices are affected, check if they're near the access point, and verify if other users in the area have the same issue", value: "gather_info", points: 10, isCorrect: true },
        { key: "c", label: "Immediately escalate to the network team", value: "escalate_immediately", points: 3, isCorrect: false },
        { key: "d", label: "Tell them to use a wired connection instead", value: "workaround_only", points: 4, isCorrect: false },
      ],
    },
    {
      slug: "it-phishing-email",
      title: "Phishing Email Report",
      prompt:
        'A user forwards you an email from "IT Department" asking them to verify their password by clicking a link. They ask: "Is this legit?" What do you do?',
      questionType: "single_select",
      difficulty: "medium",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 2,
      explanation: "Tests security awareness and proper incident handling for phishing.",
      competencies: [
        { slug: "security-awareness", weight: 1.0 },
        { slug: "communication", weight: 0.8 },
        { slug: "escalation-judgment", weight: 0.5 },
      ],
      options: [
        { key: "a", label: "Check the link yourself to verify", value: "click_link", points: 0, isCorrect: false },
        { key: "b", label: "Tell the user it's phishing, instruct them NOT to click, report it to the security team, and thank the user for flagging it", value: "full_response", points: 10, isCorrect: true },
        { key: "c", label: "Delete the email and tell them it's fine", value: "delete_dismiss", points: 1, isCorrect: false },
        { key: "d", label: "Forward the email to the whole company as a warning", value: "forward_all", points: 2, isCorrect: false },
      ],
    },
    {
      slug: "it-competing-tickets",
      title: "Competing Ticket Priorities",
      prompt:
        "You have three open tickets:\n1. CFO can't access the board presentation (meeting in 30 minutes)\n2. A developer's IDE crashed and lost unsaved work\n3. The office printer on floor 3 is jammed\n\nHow do you prioritize?",
      questionType: "ranking",
      difficulty: "hard",
      maxPoints: 12,
      weight: 1.2,
      scoringStrategy: "scenario_based",
      correctAnswerKey: JSON.stringify(["cfo_presentation", "developer_ide", "printer_jam"]),
      sortOrder: 3,
      explanation: "Tests prioritization skills: business impact + time sensitivity + user impact.",
      competencies: [
        { slug: "prioritization", weight: 1.0 },
        { slug: "critical-thinking", weight: 0.8 },
        { slug: "service-mindset", weight: 0.5 },
      ],
      options: [
        { key: "cfo_presentation", label: "CFO's board presentation access (meeting in 30 min)", value: "cfo_presentation", points: 0, isCorrect: false, sortOrder: 1 },
        { key: "developer_ide", label: "Developer's IDE crash with lost work", value: "developer_ide", points: 0, isCorrect: false, sortOrder: 2 },
        { key: "printer_jam", label: "Floor 3 printer jam", value: "printer_jam", points: 0, isCorrect: false, sortOrder: 3 },
      ],
    },
    {
      slug: "it-vpn-failure",
      title: "VPN Connection Failure",
      prompt:
        'A remote employee reports: "I can\'t connect to VPN since this morning. I have client calls starting in an hour and all my files are on the network drive." Walk through your troubleshooting approach.',
      questionType: "scenario",
      difficulty: "medium",
      maxPoints: 12,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 4,
      explanation: "Tests structured troubleshooting under time pressure and user empathy.",
      competencies: [
        { slug: "troubleshooting", weight: 1.0 },
        { slug: "communication", weight: 0.8 },
        { slug: "empathy", weight: 0.6 },
        { slug: "service-mindset", weight: 0.5 },
      ],
      options: [
        { key: "a", label: "Check for VPN server outages first, verify their client version, test their internet, and if unresolved quickly, provide temporary file access via cloud sharing while continuing to debug", value: "structured_with_workaround", points: 12, isCorrect: true },
        { key: "b", label: "Walk them through reinstalling the VPN client", value: "reinstall_only", points: 5, isCorrect: false },
        { key: "c", label: "Tell them to come into the office", value: "come_to_office", points: 2, isCorrect: false },
        { key: "d", label: "Escalate to the network team immediately", value: "escalate_first", points: 4, isCorrect: false },
      ],
    },
    {
      slug: "it-slow-device",
      title: "Slow Device Complaint",
      prompt:
        'A user says: "My laptop has been incredibly slow for weeks. I can barely open my email." What is your diagnostic approach?',
      questionType: "single_select",
      difficulty: "medium",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 5,
      explanation: "Tests methodical diagnostic process for common performance issues.",
      competencies: [
        { slug: "troubleshooting", weight: 1.0 },
        { slug: "documentation", weight: 0.4 },
      ],
      options: [
        { key: "a", label: "Tell them to restart and call back if it's still slow", value: "restart_only", points: 2, isCorrect: false },
        { key: "b", label: "Check Task Manager for resource usage, review startup programs, check disk space, scan for malware, and review recently installed software", value: "systematic_diagnosis", points: 10, isCorrect: true },
        { key: "c", label: "Order them a new laptop", value: "replace", points: 1, isCorrect: false },
        { key: "d", label: "Run a disk cleanup and hope for the best", value: "quick_fix", points: 4, isCorrect: false },
      ],
    },
    {
      slug: "it-locked-account",
      title: "Locked Account — Urgent",
      prompt:
        'An employee messages you in a panic: "I\'m locked out of everything — email, VPN, internal tools. I have a presentation to the board in 20 minutes!" What do you do?',
      questionType: "single_select",
      difficulty: "hard",
      maxPoints: 12,
      weight: 1.2,
      scoringStrategy: "weighted_options",
      sortOrder: 6,
      explanation: "Tests composure under pressure, security awareness, and service orientation.",
      competencies: [
        { slug: "troubleshooting", weight: 0.8 },
        { slug: "communication", weight: 0.8 },
        { slug: "empathy", weight: 0.7 },
        { slug: "security-awareness", weight: 0.6 },
        { slug: "prioritization", weight: 0.5 },
      ],
      options: [
        { key: "a", label: "Reset their password immediately without verification", value: "reset_no_verify", points: 3, isCorrect: false },
        { key: "b", label: "Calmly reassure them, verify their identity, check for security holds, perform a password reset through proper channels, and stay with them until they're back in", value: "calm_thorough_response", points: 12, isCorrect: true },
        { key: "c", label: "Tell them to log in from someone else's computer", value: "share_computer", points: 1, isCorrect: false },
        { key: "d", label: "Create a ticket and tell them you'll get to it within SLA", value: "follow_sla_blindly", points: 2, isCorrect: false },
      ],
    },
    {
      slug: "it-software-permission",
      title: "Unauthorized Software Request",
      prompt:
        "A team lead asks you to install a software tool that isn't on the approved list. They say: 'Just install it — I'll take responsibility.' What do you do?",
      questionType: "single_select",
      difficulty: "medium",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 7,
      explanation: "Tests policy adherence and professional pushback skills.",
      competencies: [
        { slug: "security-awareness", weight: 1.0 },
        { slug: "professionalism", weight: 0.8 },
        { slug: "escalation-judgment", weight: 0.7 },
      ],
      options: [
        { key: "a", label: "Install it — they said they'd take responsibility", value: "install_anyway", points: 0, isCorrect: false },
        { key: "b", label: "Explain the approval process, offer to submit the request on their behalf, and suggest an approved alternative if one exists", value: "policy_with_help", points: 10, isCorrect: true },
        { key: "c", label: "Refuse flatly and move on", value: "refuse_flat", points: 4, isCorrect: false },
        { key: "d", label: "Install it but log it in case there's an issue later", value: "install_and_log", points: 2, isCorrect: false },
      ],
    },
    {
      slug: "it-escalation-decision",
      title: "Escalation Judgment",
      prompt:
        "You've been troubleshooting a network issue for 25 minutes. You've ruled out the user's device and local switch, but the problem persists. Multiple users in the same area are now reporting the same issue. What's your next move?",
      questionType: "single_select",
      difficulty: "hard",
      maxPoints: 10,
      weight: 1.0,
      scoringStrategy: "weighted_options",
      sortOrder: 8,
      explanation: "Tests knowing when to escalate versus continuing solo troubleshooting.",
      competencies: [
        { slug: "escalation-judgment", weight: 1.0 },
        { slug: "troubleshooting", weight: 0.6 },
        { slug: "documentation", weight: 0.5 },
      ],
      options: [
        { key: "a", label: "Keep troubleshooting — you can figure it out", value: "keep_trying", points: 2, isCorrect: false },
        { key: "b", label: "Escalate to the network team with your findings so far: what you've tested, what you've ruled out, and the scope of impact", value: "escalate_with_context", points: 10, isCorrect: true },
        { key: "c", label: "Tell the users to wait and check back tomorrow", value: "delay", points: 0, isCorrect: false },
        { key: "d", label: "Restart the floor's network switch", value: "restart_switch", points: 4, isCorrect: false },
      ],
    },
    {
      slug: "it-documentation-approach",
      title: "Ticket Documentation",
      prompt:
        "You've just resolved a tricky issue that took 45 minutes and involved three different troubleshooting steps. How do you document it?",
      questionType: "single_select",
      difficulty: "easy",
      maxPoints: 8,
      weight: 0.8,
      scoringStrategy: "weighted_options",
      sortOrder: 9,
      explanation: "Tests documentation quality and knowledge-sharing mindset.",
      competencies: [
        { slug: "documentation", weight: 1.0 },
        { slug: "service-mindset", weight: 0.4 },
      ],
      options: [
        { key: "a", label: "Mark the ticket as resolved — the issue is fixed", value: "close_only", points: 1, isCorrect: false },
        { key: "b", label: "Document the symptoms, each troubleshooting step, the root cause, the resolution, and add it to the knowledge base if it could help others", value: "thorough_documentation", points: 8, isCorrect: true },
        { key: "c", label: "Write a brief note: 'Fixed network issue'", value: "brief_note", points: 3, isCorrect: false },
        { key: "d", label: "Send an email to your team about the fix", value: "email_only", points: 4, isCorrect: false },
      ],
    },
    {
      slug: "it-executive-pressure",
      title: "Executive Under Pressure",
      prompt:
        'The CEO stops you in the hallway: "My email isn\'t syncing and I have a board meeting in 10 minutes. Fix it NOW." They\'re visibly frustrated. What\'s your approach?',
      questionType: "scenario",
      difficulty: "hard",
      maxPoints: 12,
      weight: 1.2,
      scoringStrategy: "weighted_options",
      sortOrder: 10,
      explanation: "Tests composure, empathy, and structured problem-solving under high-pressure executive interaction.",
      competencies: [
        { slug: "communication", weight: 1.0 },
        { slug: "empathy", weight: 0.9 },
        { slug: "troubleshooting", weight: 0.7 },
        { slug: "professionalism", weight: 0.8 },
        { slug: "prioritization", weight: 0.5 },
      ],
      options: [
        { key: "a", label: "Stay calm, acknowledge the urgency, quickly check their email settings on their device, try a quick sync/restart, and if not resolved in 2 minutes, set up email access on their phone as a backup while you continue fixing", value: "calm_structured_backup", points: 12, isCorrect: true },
        { key: "b", label: "Tell them you'll look at it after your current ticket", value: "follow_queue", points: 0, isCorrect: false },
        { key: "c", label: "Panic and start clicking around randomly on their laptop", value: "panic", points: 1, isCorrect: false },
        { key: "d", label: "Immediately escalate to your manager", value: "escalate_up", points: 3, isCorrect: false },
      ],
    },
  ];

  // ─── Create Questions Helper ─────────────────────────────
  async function createQuestions(
    sectionId: string,
    questions: any[]
  ) {
    for (const q of questions) {
      const { competencies: questionCompetencies, options, ...questionData } = q;
      const question = await prisma.question.create({
        data: {
          sectionId,
          ...questionData,
          correctAnswerKey: questionData.correctAnswerKey ?? null,
          rubric: null,
          partialCreditRules: null,
          knockoutFlag: false,
          knockoutThreshold: null,
          automationLabel: q.slug,
          analyticsLabel: q.slug,
          isActive: true,
          version: 1,
        },
      });

      // Create answer options
      await Promise.all(
        options.map((opt, idx) =>
          prisma.answerOption.create({
            data: {
              questionId: question.id,
              key: opt.key,
              label: opt.label,
              value: opt.value,
              points: opt.points,
              isCorrect: opt.isCorrect,
              sortOrder: (opt as any).sortOrder ?? idx + 1,
            },
          })
        )
      );

      // Create competency mappings
      await Promise.all(
        questionCompetencies.map((c) =>
          prisma.questionCompetency.create({
            data: {
              questionId: question.id,
              competencyId: comp[c.slug].id,
              weight: c.weight,
            },
          })
        )
      );
    }
  }

  await createQuestions(cultureFit.id, cultureFitQuestions);
  await createQuestions(aiAwareness.id, aiAwarenessQuestions);
  await createQuestions(itRole.id, itSupportQuestions);

  // ─── Admin User ──────────────────────────────────────────
  const bcrypt = await import("bcryptjs");
  const hashedPassword = await bcrypt.hash("admin123", 12);
  await prisma.adminUser.create({
    data: {
      email: "jehada@janusd.io",
      name: "Jehad Altoutou",
      passwordHash: hashedPassword,
      role: "admin",
    },
  });

  // ─── HR Form Templates ───────────────────────────────────
  await prisma.formTemplate.create({
    data: {
      name: "Personal Data Form",
      slug: "personal-data",
      description: "Employee onboarding form collecting personal information, emergency contacts, education, qualifications, and language proficiency.",
      formType: "personal_data",
    },
  });

  await prisma.formTemplate.create({
    data: {
      name: "Bank Details Form",
      slug: "bank-details",
      description: "Employee bank account details for payroll setup.",
      formType: "bank_details",
    },
  });

  console.log("Seed complete!");
  console.log(`  Department: ${itDept.name}`);
  console.log(`  Job Role: ${itSupport.title}`);
  console.log(`  Competencies: ${competencies.length}`);
  console.log(`  Assessment: ${template.title} v${version.versionNumber}`);
  console.log(`  Sections: 3`);
  console.log(`  Questions: ${cultureFitQuestions.length + aiAwarenessQuestions.length + itSupportQuestions.length}`);
}

main()
  .then(() => prisma.$disconnect())
  .catch((e) => {
    console.error(e);
    prisma.$disconnect();
    process.exit(1);
  });

```