---
type: source
source_type: laptop
title: ProposalContent
slug: proposalcontent
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/proposals/ProposalContent.tsx
original_size: 50570
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# ProposalContent

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/proposals/ProposalContent.tsx` on 2026-05-14._

```tsx
'use client';

import { useEffect, useRef, useState } from 'react';
import { useRouter } from 'next/navigation';
import {
  CheckCircle2, Zap, Shield, Target, BarChart3, Users, ArrowRight,
  Building2, Phone, Mail, Globe, MapPin, LogOut, ChevronRight,
  Sparkles, TrendingUp, Database, Send, Clock, Star, Award,
  Filter, Brain, Layers, Calendar, AlertTriangle, UserCheck, Timer
} from 'lucide-react';
import type { ProposalClientRecord } from '@/types/proposals';

interface Props {
  client: ProposalClientRecord;
}

const NAV_SECTIONS = [
  { id: 'hero', label: 'Overview' },
  { id: 'agenda', label: 'This Session' },
  { id: 'challenge', label: 'The Challenge' },
  { id: 'solution', label: 'Our Solution' },
  { id: 'how-it-works', label: 'How It Works' },
  { id: 'qualification', label: 'AI Layer' },
  { id: 'delivery', label: 'What You Receive' },
  { id: 'team-fit', label: 'Team Fit' },
  { id: 'sales-approach', label: 'Your Team' },
  { id: 'pricing', label: 'Pricing' },
  { id: 'why-us', label: 'Why Us' },
  { id: 'next-steps', label: 'Next Steps' },
];

function useIntersect(ids: string[]) {
  const [active, setActive] = useState(ids[0]);

  useEffect(() => {
    const observers: IntersectionObserver[] = [];
    ids.forEach((id) => {
      const el = document.getElementById(id);
      if (!el) return;
      const obs = new IntersectionObserver(
        ([entry]) => { if (entry.isIntersecting) setActive(id); },
        { rootMargin: '-30% 0px -60% 0px', threshold: 0 }
      );
      obs.observe(el);
      observers.push(obs);
    });
    return () => observers.forEach((o) => o.disconnect());
  }, [ids]);

  return active;
}

// ── Reusable primitives ──────────────────────────────────────────

function SectionBadge({ children }: { children: React.ReactNode }) {
  return (
    <span
      className="inline-block text-[10px] font-bold uppercase tracking-[0.25em] px-3 py-1 rounded-full mb-4"
      style={{ background: 'rgba(37,99,235,0.15)', border: '1px solid rgba(37,99,235,0.3)', color: '#93c5fd' }}
    >
      {children}
    </span>
  );
}

function SectionTitle({ children }: { children: React.ReactNode }) {
  return (
    <h2 className="font-heading text-3xl md:text-4xl font-black text-white leading-tight mb-4">
      {children}
    </h2>
  );
}

function SectionSubtitle({ children }: { children: React.ReactNode }) {
  return <p className="text-slate-400 text-lg leading-relaxed mb-10">{children}</p>;
}

function Card({ children, className = '' }: { children: React.ReactNode; className?: string }) {
  return (
    <div
      className={`rounded-2xl p-6 ${className}`}
      style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.07)' }}
    >
      {children}
    </div>
  );
}

function GoldCard({ children, className = '' }: { children: React.ReactNode; className?: string }) {
  return (
    <div
      className={`rounded-2xl p-6 ${className}`}
      style={{
        background: 'rgba(245,158,11,0.05)',
        border: '1px solid rgba(245,158,11,0.2)',
      }}
    >
      {children}
    </div>
  );
}

// ── Sections ────────────────────────────────────────────────────

function HeroSection({ client }: { client: ProposalClientRecord }) {
  const date = new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' });

  return (
    <section id="hero" className="min-h-screen flex flex-col justify-center py-24 px-6 md:px-12 relative overflow-hidden">
      {/* Radial glow */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          background: 'radial-gradient(ellipse 80% 50% at 50% -10%, rgba(37,99,235,0.12) 0%, transparent 70%)',
        }}
      />

      <div className="relative max-w-4xl">
        {/* Partnership header */}
        <div
          className="inline-flex items-center gap-3 px-4 py-2 rounded-full mb-8 proposal-fade-up"
          style={{
            background: 'rgba(255,255,255,0.04)',
            border: '1px solid rgba(255,255,255,0.1)',
            animationDelay: '0ms',
          }}
        >
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Dubai Property Leads</span>
          <span className="text-slate-600">×</span>
          <span className="text-xs font-bold text-white uppercase tracking-wider">{client.companyName}</span>
        </div>

        <h1
          className="font-heading text-5xl md:text-7xl font-black text-white tracking-tight leading-[1.05] mb-6 proposal-fade-up"
          style={{ animationDelay: '100ms' }}
        >
          Your Premium
          <br />
          <span
            style={{
              background: 'linear-gradient(135deg, #3b82f6 0%, #818cf8 100%)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
              backgroundClip: 'text',
            }}
          >
            Lead System.
          </span>
        </h1>

        <p
          className="text-xl text-slate-400 max-w-2xl leading-relaxed mb-12 proposal-fade-up"
          style={{ animationDelay: '200ms' }}
        >
          Built exclusively for {client.companyName} — a tailored overview of how
          our AI-qualified lead pipeline integrates with your sales team.
        </p>

        {/* Meta row */}
        <div
          className="flex flex-wrap gap-6 proposal-fade-up"
          style={{ animationDelay: '300ms' }}
        >
          <div>
            <p className="text-[10px] font-bold uppercase tracking-widest text-slate-600 mb-1">Prepared For</p>
            <p className="text-sm font-semibold text-slate-200">
              {client.contactName}
              {client.role && <span className="text-slate-500"> · {client.role}</span>}
            </p>
          </div>
          {client.proposal?.packageVolume && (
            <div>
              <p className="text-[10px] font-bold uppercase tracking-widest text-slate-600 mb-1">Lead Volume</p>
              <p className="text-sm font-semibold text-slate-200">
                {client.proposal.packageVolume.toLocaleString()} Leads
              </p>
            </div>
          )}
          <div>
            <p className="text-[10px] font-bold uppercase tracking-widest text-slate-600 mb-1">Date</p>
            <p className="text-sm font-semibold text-slate-200">{date}</p>
          </div>
          {client.website && (
            <div>
              <p className="text-[10px] font-bold uppercase tracking-widest text-slate-600 mb-1">Company</p>
              <p className="text-sm font-semibold text-slate-200">{client.website}</p>
            </div>
          )}
        </div>

        {/* Scroll indicator */}
        <div className="mt-16 flex items-center gap-3 text-slate-600 proposal-fade-up" style={{ animationDelay: '400ms' }}>
          <div className="w-px h-8 bg-slate-700" />
          <span className="text-xs font-medium uppercase tracking-widest">Scroll to explore</span>
        </div>
      </div>
    </section>
  );
}

function AgendaSection({ client }: { client: ProposalClientRecord }) {
  const agendaItems = [
    'Overview of how our lead generation system works (acquisition channels & funnels)',
    'How our AI-driven qualification layer filters and validates lead quality',
    'Lead structure, delivery model, and what your sales team receives',
    'Best practices for handling and converting leads internally',
    `Pricing structure based on volume${client.proposal?.packageVolume ? ` (${client.proposal.packageVolume.toLocaleString()} leads)` : ''}`,
    'Q&A and next steps',
  ];

  return (
    <section id="agenda" className="py-24 px-6 md:px-12">
      <div className="max-w-4xl">
        <SectionBadge>This Session</SectionBadge>
        <SectionTitle>What We&apos;re Covering Today</SectionTitle>
        <SectionSubtitle>
          This session is designed to walk you through how Dubai Property Leads generates and
          delivers high-intent, pre-qualified investor leads for the off-plan market, and how
          this can be structured specifically for {client.companyName}&apos;s team.
        </SectionSubtitle>

        <div className="space-y-3">
          {agendaItems.map((item, i) => (
            <div
              key={i}
              className="flex items-start gap-4 p-4 rounded-xl transition-all hover:border-white/10"
              style={{ background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.05)' }}
            >
              <div
                className="flex-shrink-0 w-7 h-7 rounded-full flex items-center justify-center text-xs font-black"
                style={{ background: 'rgba(37,99,235,0.15)', color: '#93c5fd', border: '1px solid rgba(37,99,235,0.25)' }}
              >
                {i + 1}
              </div>
              <p className="text-slate-300 text-sm leading-relaxed pt-0.5">{item}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function ChallengeSection() {
  const challenges = [
    {
      icon: <Target className="w-5 h-5" />,
      title: 'Unqualified Contacts',
      body: 'Most lead sources deliver raw enquiries with no intent validation. Agents spend hours chasing leads who were never serious buyers.',
    },
    {
      icon: <BarChart3 className="w-5 h-5" />,
      title: 'Low Conversion Rates',
      body: 'Traditional portals and cold-call lists convert at 1–3%. The cost per deal is enormous when you factor in agent time and acquisition spend.',
    },
    {
      icon: <Clock className="w-5 h-5" />,
      title: 'Time Wasted on Dead Leads',
      body: 'Research shows 60%+ of agent time is spent on leads that will never transact. That is revenue lost to friction, not market conditions.',
    },
    {
      icon: <Database className="w-5 h-5" />,
      title: 'No Intelligence Layer',
      body: 'A phone number and an email is not enough. Without budget confirmation, timeline, and intent signals, you are flying blind.',
    },
  ];

  return (
    <section id="challenge" className="py-24 px-6 md:px-12">
      <div className="max-w-4xl">
        <SectionBadge>The Problem</SectionBadge>
        <SectionTitle>Why Traditional Lead Generation Is Broken</SectionTitle>
        <SectionSubtitle>
          Dubai&apos;s off-plan market is competitive. The brokerages that win are not the ones
          with the largest advertising budgets — they are the ones with the best lead quality and
          the fastest follow-up on genuinely qualified buyers.
        </SectionSubtitle>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {challenges.map((c, i) => (
            <Card key={i}>
              <div
                className="w-9 h-9 rounded-xl flex items-center justify-center mb-4"
                style={{ background: 'rgba(239,68,68,0.1)', color: '#f87171', border: '1px solid rgba(239,68,68,0.15)' }}
              >
                {c.icon}
              </div>
              <h3 className="font-heading font-bold text-white mb-2">{c.title}</h3>
              <p className="text-slate-500 text-sm leading-relaxed">{c.body}</p>
            </Card>
          ))}
        </div>

        <div
          className="mt-8 p-6 rounded-2xl flex items-start gap-4"
          style={{ background: 'rgba(245,158,11,0.05)', border: '1px solid rgba(245,158,11,0.15)' }}
        >
          <Star className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" />
          <p className="text-slate-300 text-sm leading-relaxed">
            <span className="text-white font-semibold">The result: </span>
            Sales teams in Dubai are running at a fraction of their potential efficiency.
            The fix is not more leads — it is <span className="text-amber-400 font-semibold">better-qualified leads</span>, delivered faster.
          </p>
        </div>
      </div>
    </section>
  );
}

function SolutionSection({ client }: { client: ProposalClientRecord }) {
  const benefits = [
    { icon: <Zap className="w-4 h-4" />, text: 'AI-filtered for genuine purchase intent' },
    { icon: <Shield className="w-4 h-4" />, text: 'Budget-confirmed and timeline-qualified' },
    { icon: <Users className="w-4 h-4" />, text: `Sized for ${client.companyName}'s team` },
    { icon: <Send className="w-4 h-4" />, text: 'Delivered clean, ready for immediate outreach' },
    { icon: <Target className="w-4 h-4" />, text: 'Off-plan specialist focus' },
    { icon: <Star className="w-4 h-4" />, text: 'Exclusive — not shared with other brokerages' },
  ];

  return (
    <section id="solution" className="py-24 px-6 md:px-12">
      <div className="max-w-4xl">
        <SectionBadge>Our Solution</SectionBadge>
        <SectionTitle>
          High-Intent Investor Leads,
          <br />
          <span
            style={{
              background: 'linear-gradient(135deg, #3b82f6 0%, #818cf8 100%)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
              backgroundClip: 'text',
            }}
          >
            Ready to Buy.
          </span>
        </SectionTitle>
        <SectionSubtitle>
          Dubai Property Leads operates a purpose-built lead generation and qualification
          infrastructure for the off-plan real estate market. Every lead your team receives
          has passed our multi-stage intelligence filter.
        </SectionSubtitle>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-10">
          {benefits.map((b, i) => (
            <div
              key={i}
              className="flex items-center gap-3 p-4 rounded-xl"
              style={{ background: 'rgba(37,99,235,0.06)', border: '1px solid rgba(37,99,235,0.15)' }}
            >
              <div
                className="flex-shrink-0 w-7 h-7 rounded-lg flex items-center justify-center"
                style={{ background: 'rgba(37,99,235,0.15)', color: '#93c5fd' }}
              >
                {b.icon}
              </div>
              <span className="text-sm text-slate-300">{b.text}</span>
            </div>
          ))}
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[
            { value: '300+', label: 'Leads/batch', sub: 'Structured volume delivery' },
            { value: 'AI', label: 'Qualification', sub: 'Intent-scored every lead' },
            { value: '24–72h', label: 'First delivery', sub: 'After contract activation' },
          ].map((stat, i) => (
            <GoldCard key={i} className="text-center">
              <p className="font-heading text-4xl font-black text-white mb-1">{stat.value}</p>
              <p className="text-amber-400 font-bold text-sm uppercase tracking-wider mb-1">{stat.label}</p>
              <p className="text-slate-500 text-xs">{stat.sub}</p>
            </GoldCard>
          ))}
        </div>
      </div>
    </section>
  );
}

function HowItWorksSection() {
  const steps = [
    {
      step: '01',
      title: 'Targeted Acquisition — Not Random Traffic',
      body: 'We run intent-specific campaigns across Meta, Google, and programmatic channels. Every ad is designed to attract serious off-plan buyers — not casual browsers or form-fillers.',
      icon: <Globe className="w-5 h-5" />,
      color: '#3b82f6',
    },
    {
      step: '02',
      title: 'Structured Capture with Full Context',
      body: 'Prospects enter our purpose-built landing flow. We collect name, phone, email, budget range, property type, and location preference — so your team receives leads with real context, not just a number.',
      icon: <Layers className="w-5 h-5" />,
      color: '#8b5cf6',
    },
    {
      step: '03',
      title: 'AI Filtering — Only High-Intent Passes',
      body: 'This is the critical step. Our AI model validates contacts, scores purchase intent, and removes noise. What does not pass the filter never reaches you. You receive only the contacts that cleared the bar.',
      icon: <Brain className="w-5 h-5" />,
      color: '#06b6d4',
    },
    {
      step: '04',
      title: 'Clean Delivery — Ready to Act On',
      body: 'Qualified leads are packaged as a structured CSV and delivered within 24–72 hours. Every field complete. Every contact verified. Your team picks up the phone and starts the conversation.',
      icon: <Send className="w-5 h-5" />,
      color: '#10b981',
    },
  ];

  return (
    <section id="how-it-works" className="py-24 px-6 md:px-12">
      <div className="max-w-4xl">
        <SectionBadge>Process</SectionBadge>
        <SectionTitle>How the System Works</SectionTitle>
        <SectionSubtitle>
          What your team receives is not raw traffic or a bulk list. It is the output of a
          four-stage pipeline designed to deliver only contacts with a genuine reason to buy.
        </SectionSubtitle>

        <div className="space-y-4">
          {steps.map((s, i) => (
            <div
              key={i}
              className="flex gap-6 p-6 rounded-2xl transition-all"
              style={{ background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.06)' }}
            >
              <div className="flex-shrink-0">
                <div
                  className="w-11 h-11 rounded-xl flex items-center justify-center"
                  style={{ background: `${s.color}18`, color: s.color, border: `1px solid ${s.color}30` }}
                >
                  {s.icon}
                </div>
              </div>
              <div>
                <div className="flex items-center gap-3 mb-2">
                  <span
                    className="text-[10px] font-black tracking-widest"
                    style={{ color: s.color }}
                  >
                    STEP {s.step}
                  </span>
                  {i < steps.length - 1 && (
                    <ChevronRight className="w-3 h-3 text-slate-700" />
                  )}
                </div>
                <h3 className="font-heading font-bold text-white text-lg mb-2">{s.title}</h3>
                <p className="text-slate-500 text-sm leading-relaxed">{s.body}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function QualificationSection() {
  const filters = [
    {
      icon: <Phone className="w-4 h-4" />,
      title: 'Contact Validation',
      body: 'Phone numbers and emails verified for format, carrier validity, and reachability before a lead passes.',
    },
    {
      icon: <BarChart3 className="w-4 h-4" />,
      title: 'Budget Confirmation',
      body: 'Self-declared budget ranges are cross-referenced with property type, location, and nationality signals to assess credibility.',
    },
    {
      icon: <TrendingUp className="w-4 h-4" />,
      title: 'Intent Scoring',
      body: 'Behavioural signals — time-on-page, query depth, form completeness — are weighted into an intent score for every submission.',
    },
    {
      icon: <Filter className="w-4 h-4" />,
      title: 'Noise Filtering',
      body: 'Duplicate submissions, test entries, competitor probes, and low-credibility signals are automatically removed.',
    },
    {
      icon: <Sparkles className="w-4 h-4" />,
      title: 'Enrichment',
      body: 'Where available, nationality and demographic context is enriched to help agents personalise their approach.',
    },
    {
      icon: <Award className="w-4 h-4" />,
      title: 'Quality Guarantee',
      body: 'Leads failing our quality bar are replaced. You never pay for a contact you cannot reach.',
    },
  ];

  return (
    <section id="qualification" className="py-24 px-6 md:px-12">
      <div className="max-w-4xl">
        <SectionBadge>Intelligence Layer</SectionBadge>
        <SectionTitle>The AI Qualification Engine</SectionTitle>
        <SectionSubtitle>
          Our qualification layer is what separates our leads from a raw list of enquiries.
          Every contact goes through a multi-stage validation pipeline before your team ever sees it.
        </SectionSubtitle>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {filters.map((f, i) => (
            <Card key={i}>
              <div
                className="w-8 h-8 rounded-lg flex items-center justify-center mb-3"
                style={{ background: 'rgba(99,102,241,0.12)', color: '#a5b4fc', border: '1px solid rgba(99,102,241,0.2)' }}
              >
                {f.icon}
              </div>
              <h3 className="font-heading font-bold text-white mb-2 text-sm">{f.title}</h3>
              <p className="text-slate-500 text-sm leading-relaxed">{f.body}</p>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}

function DeliverySection() {
  const fields = [
    { label: 'Full Name', note: 'First + last name' },
    { label: 'Phone Number', note: 'Mobile, validated' },
    { label: 'Email Address', note: 'Confirmed reachable' },
    { label: 'Nationality', note: 'Country of origin' },
    { label: 'Budget Range', note: 'AED, self-declared' },
    { label: 'Property Type', note: 'Villa, apt, penthouse, plot…' },
    { label: 'Location Interest', note: 'Dubai area preferences' },
    { label: 'Enquiry Message', note: 'Original inquiry text' },
    { label: 'Timestamp', note: 'Date of submission' },
  ];

  return (
    <section id="delivery" className="py-24 px-6 md:px-12">
      <div className="max-w-4xl">
        <SectionBadge>Delivery</SectionBadge>
        <SectionTitle>What Your Team Receives</SectionTitle>
        <SectionSubtitle>
          Every lead is delivered with full structured contact data, ready to load into
          your CRM, distribute across agents, or act on immediately.
        </SectionSubtitle>

        <Card className="mb-8">
          <div className="flex items-center gap-3 mb-5">
            <Database className="w-5 h-5 text-blue-400" />
            <h3 className="font-heading font-bold text-white">Lead Data Fields</h3>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            {fields.map((f, i) => (
              <div
                key={i}
                className="p-3 rounded-xl"
                style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.06)' }}
              >
                <p className="text-sm font-semibold text-slate-200">{f.label}</p>
                <p className="text-xs text-slate-600 mt-0.5">{f.note}</p>
              </div>
            ))}
          </div>
        </Card>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[
            { icon: <Send className="w-5 h-5" />, title: 'CSV Delivery', body: 'Structured spreadsheet format, importable into any CRM or dialler system.' },
            { icon: <CheckCircle2 className="w-5 h-5" />, title: 'Verified Contacts', body: 'Every phone and email passes our reachability check before delivery.' },
            { icon: <Zap className="w-5 h-5" />, title: 'Fast Turnaround', body: 'First batch within 24–72 hours of activation. Subsequent batches on schedule.' },
          ].map((c, i) => (
            <div
              key={i}
              className="p-5 rounded-2xl text-center"
              style={{ background: 'rgba(16,185,129,0.05)', border: '1px solid rgba(16,185,129,0.15)' }}
            >
              <div
                className="w-10 h-10 rounded-xl flex items-center justify-center mx-auto mb-3"
                style={{ background: 'rgba(16,185,129,0.12)', color: '#6ee7b7' }}
              >
                {c.icon}
              </div>
              <h3 className="font-heading font-bold text-white text-sm mb-2">{c.title}</h3>
              <p className="text-slate-500 text-xs leading-relaxed">{c.body}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function TeamFitSection({ client }: { client: ProposalClientRecord }) {
  const volume = client.proposal?.packageVolume ?? 300;
  const agentCount = 5;
  const perAgent = Math.round(volume / agentCount);

  return (
    <section id="team-fit" className="py-24 px-6 md:px-12">
      <div className="max-w-4xl">
        <SectionBadge>Team Fit</SectionBadge>
        <SectionTitle>How 300 Leads Work Across Your Team</SectionTitle>
        <SectionSubtitle>
          Based on your {agentCount}-agent setup, 300 leads gives each person a focused,
          workable pipeline — enough volume to drive real results without overloading anyone.
        </SectionSubtitle>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
          {[
            { value: volume.toLocaleString(), label: 'Total Leads', sub: 'Your package volume' },
            { value: `~${perAgent}`, label: 'Per Agent', sub: `Across ${agentCount} sales agents` },
            { value: '24–72h', label: 'Delivery Window', sub: 'First batch after activation' },
          ].map((s, i) => (
            <Card key={i} className="text-center">
              <p className="font-heading text-3xl font-black text-white mb-1">{s.value}</p>
              <p className="text-blue-400 font-bold text-xs uppercase tracking-widest mb-1">{s.label}</p>
              <p className="text-slate-600 text-xs">{s.sub}</p>
            </Card>
          ))}
        </div>

        <Card>
          <h3 className="font-heading font-bold text-white mb-4 flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            Distribution Best Practices
          </h3>
          <ul className="space-y-3">
            {[
              'Split the 300 leads equally across your 5 agents — 60 contacts per person, a focused and manageable pipeline',
              'Assign leads by property type or location where agents have existing familiarity',
              'First contact within 2 hours of receiving a batch — response speed is the single biggest conversion lever',
              'Use the enquiry message in your opening call — it signals you read their brief and builds immediate credibility',
              'Track attempted vs. connected vs. booked at each stage to identify where the drop-off is',
              'Flag any unreachable contacts within 7 days — replacements are covered under our quality guarantee',
            ].map((r, i) => (
              <li key={i} className="flex items-start gap-3">
                <div
                  className="mt-1 flex-shrink-0 w-5 h-5 rounded-full flex items-center justify-center"
                  style={{ background: 'rgba(16,185,129,0.12)', color: '#6ee7b7' }}
                >
                  <CheckCircle2 className="w-3 h-3" />
                </div>
                <span className="text-slate-300 text-sm leading-relaxed">{r}</span>
              </li>
            ))}
          </ul>
        </Card>
      </div>
    </section>
  );
}

function SalesApproachSection({ client }: { client: ProposalClientRecord }) {
  return (
    <section id="sales-approach" className="py-24 px-6 md:px-12">
      <div className="max-w-4xl">
        <SectionBadge>Your Team</SectionBadge>
        <SectionTitle>Recommended Approach for {client.companyName}</SectionTitle>
        <SectionSubtitle>
          Based on our conversation, your team handles both off-plan and secondary market.
          These are two different buyer journeys — and that distinction matters when working
          with off-plan investor leads specifically.
        </SectionSubtitle>

        {/* Off-plan focus recommendation */}
        <div
          className="p-6 rounded-2xl mb-6 flex gap-5"
          style={{ background: 'rgba(245,158,11,0.05)', border: '1px solid rgba(245,158,11,0.18)' }}
        >
          <AlertTriangle className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" />
          <div>
            <h3 className="font-heading font-bold text-white mb-2">
              Mixed-Market Focus Reduces Off-Plan Conversion
            </h3>
            <p className="text-slate-400 text-sm leading-relaxed">
              Agents who split their time between secondary and off-plan tend to convert
              off-plan leads at a lower rate — not because of the leads, but because the
              conversation structure, objection handling, and project knowledge required
              are genuinely different. This is not a criticism; it is a common pattern we
              see across brokerage teams.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          {[
            {
              icon: <UserCheck className="w-5 h-5" />,
              title: 'Dedicate 2–3 Agents to Off-Plan',
              body: 'Designate specific agents to handle these leads. They will build pattern recognition faster and close more consistently.',
              color: '#3b82f6',
            },
            {
              icon: <Timer className="w-5 h-5" />,
              title: 'Speed Is Your Biggest Lever',
              body: 'Responding within 2 hours of receiving a lead batch is the single most impactful thing your team can do. These leads are warm — not cold.',
              color: '#10b981',
            },
            {
              icon: <Brain className="w-5 h-5" />,
              title: 'Use the Enquiry as Your Opening',
              body: 'Every lead includes the original enquiry message. Agents who reference it in the first call convert significantly better than those who do not.',
              color: '#8b5cf6',
            },
          ].map((c, i) => (
            <div
              key={i}
              className="p-5 rounded-2xl"
              style={{ background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.06)' }}
            >
              <div
                className="w-9 h-9 rounded-xl flex items-center justify-center mb-4"
                style={{ background: `${c.color}15`, color: c.color, border: `1px solid ${c.color}25` }}
              >
                {c.icon}
              </div>
              <h3 className="font-heading font-bold text-white mb-2 text-sm">{c.title}</h3>
              <p className="text-slate-500 text-sm leading-relaxed">{c.body}</p>
            </div>
          ))}
        </div>

        <div
          className="p-5 rounded-xl text-sm text-slate-400 leading-relaxed"
          style={{ background: 'rgba(37,99,235,0.04)', border: '1px solid rgba(37,99,235,0.12)' }}
        >
          <span className="text-blue-400 font-semibold">Our recommendation: </span>
          Start with 2–3 of your agents dedicated to this pipeline. Get them comfortable
          with the off-plan conversation flow first. If results are strong, you can expand
          distribution across the full team in the next batch.
        </div>
      </div>
    </section>
  );
}

function PricingSection({ client }: { client: ProposalClientRecord }) {
  const volume = client.proposal?.packageVolume ?? 300;
  const pricePerLead = 125;
  const totalBase = volume * pricePerLead;
  const bufferMin = 30;
  const bufferMax = 40;

  return (
    <section id="pricing" className="py-24 px-6 md:px-12">
      <div className="max-w-4xl">
        <SectionBadge>Pricing</SectionBadge>
        <SectionTitle>Volume-Structured for Your Team</SectionTitle>
        <SectionSubtitle>
          Pricing for {client.companyName} is structured around your {volume}-lead requirement.
          This is not an off-the-shelf package — it is sized for your team and your pipeline.
        </SectionSubtitle>

        {/* Main pricing card */}
        <GoldCard className="mb-6">
          <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-8">
            <div className="flex-1">
              <p className="text-[10px] font-bold uppercase tracking-[0.25em] text-amber-500 mb-3">
                Custom Package — Noorzad Properties
              </p>
              <div className="flex items-baseline gap-3 mb-1">
                <span className="font-heading text-5xl font-black text-white">
                  {pricePerLead.toLocaleString()}
                </span>
                <span className="text-amber-400 font-bold text-lg">AED / lead</span>
              </div>
              <p className="text-slate-500 text-sm mb-5">
                {volume} leads ×{' '}
                <span className="text-white font-semibold">{pricePerLead} AED</span>
                {' = '}
                <span className="text-white font-semibold">{totalBase.toLocaleString()} AED total</span>
              </p>

              {/* Line items */}
              <div className="space-y-2">
                {[
                  { label: `${volume} AI-Qualified Off-Plan Leads`, value: `${totalBase.toLocaleString()} AED`, highlight: false },
                  { label: `Optional buffer (${bufferMin}–${bufferMax} additional leads)`, value: 'Available on request', highlight: false },
                  { label: 'Quality replacement guarantee', value: 'Included', highlight: true },
                  { label: 'Exclusive delivery (not shared)', value: 'Included', highlight: true },
                ].map((row, i) => (
                  <div
                    key={i}
                    className="flex items-center justify-between py-2.5 border-b"
                    style={{ borderColor: 'rgba(255,255,255,0.06)' }}
                  >
                    <span className="text-slate-400 text-sm">{row.label}</span>
                    <span
                      className="text-sm font-semibold"
                      style={{ color: row.highlight ? '#6ee7b7' : '#e2e8f0' }}
                    >
                      {row.value}
                    </span>
                  </div>
                ))}
              </div>
            </div>

            <div className="flex-shrink-0 flex flex-col gap-3">
              <div
                className="px-6 py-5 rounded-2xl text-center min-w-[160px]"
                style={{ background: 'rgba(245,158,11,0.08)', border: '1px solid rgba(245,158,11,0.25)' }}
              >
                <p className="text-[10px] font-bold uppercase tracking-widest text-amber-500 mb-1">Total</p>
                <p className="font-heading text-2xl font-black text-white">{totalBase.toLocaleString()}</p>
                <p className="text-amber-400 text-xs font-bold">AED</p>
              </div>
              <div
                className="px-6 py-4 rounded-2xl text-center"
                style={{ background: 'rgba(16,185,129,0.06)', border: '1px solid rgba(16,185,129,0.2)' }}
              >
                <p className="text-[10px] font-bold uppercase tracking-widest text-emerald-400 mb-1">Delivery</p>
                <p className="text-white font-bold text-sm">24–72 Hours</p>
              </div>
            </div>
          </div>
        </GoldCard>

        {/* Buffer note */}
        <div
          className="p-4 rounded-xl mb-6 flex items-start gap-3"
          style={{ background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.06)' }}
        >
          <Database className="w-4 h-4 text-slate-500 flex-shrink-0 mt-0.5" />
          <p className="text-slate-500 text-sm leading-relaxed">
            <span className="text-slate-300 font-semibold">Optional Buffer: </span>
            We can structure your package with {bufferMin}–{bufferMax} additional leads held in reserve.
            This accounts for any that fall below threshold after delivery, keeping your active
            pipeline at the full {volume}-lead count throughout.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[
            { icon: <Shield className="w-4 h-4" />, title: 'Quality Guarantee', body: 'Unreachable contacts replaced. You do not pay for leads you cannot use.' },
            { icon: <Zap className="w-4 h-4" />, title: '24–72h First Delivery', body: 'Leads in your team\'s hands within 24–72 hours of activation.' },
            { icon: <Star className="w-4 h-4" />, title: 'Exclusively Yours', body: 'These leads are not distributed to any other brokerage in Dubai.' },
          ].map((f, i) => (
            <Card key={i}>
              <div
                className="w-8 h-8 rounded-lg flex items-center justify-center mb-3"
                style={{ background: 'rgba(245,158,11,0.1)', color: '#fbbf24', border: '1px solid rgba(245,158,11,0.2)' }}
              >
                {f.icon}
              </div>
              <h3 className="font-semibold text-white text-sm mb-1">{f.title}</h3>
              <p className="text-slate-500 text-xs leading-relaxed">{f.body}</p>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}

function WhyUsSection() {
  const differentiators = [
    {
      icon: <Brain className="w-5 h-5" />,
      title: 'AI-Powered Qualification',
      body: 'Not a list broker. Every lead passes an intent-scoring and validation model before it ever reaches your team.',
      accent: '#8b5cf6',
    },
    {
      icon: <Shield className="w-5 h-5" />,
      title: 'Exclusive Distribution',
      body: 'We do not sell the same lead to 10 brokerages. When you receive a contact, it is yours.',
      accent: '#3b82f6',
    },
    {
      icon: <Target className="w-5 h-5" />,
      title: 'Off-Plan Specialist',
      body: 'Our entire pipeline is built around the off-plan investor and end-user market in Dubai. Depth over breadth.',
      accent: '#10b981',
    },
    {
      icon: <TrendingUp className="w-5 h-5" />,
      title: 'Conversion-Optimised',
      body: 'Our acquisition channels and qualification logic are tuned specifically for what makes a Dubai buyer actually transact.',
      accent: '#f59e0b',
    },
    {
      icon: <Building2 className="w-5 h-5" />,
      title: 'Market Experience',
      body: 'We understand Dubai\'s real estate dynamics — project launches, investor sentiment, and buyer profiles at a granular level.',
      accent: '#06b6d4',
    },
    {
      icon: <Zap className="w-5 h-5" />,
      title: 'Fast, Reliable Delivery',
      body: 'No waiting. First batch delivered within 24–72 hours of activation, with subsequent batches on a predictable schedule.',
      accent: '#ec4899',
    },
  ];

  return (
    <section id="why-us" className="py-24 px-6 md:px-12">
      <div className="max-w-4xl">
        <SectionBadge>Why Us</SectionBadge>
        <SectionTitle>Why Dubai Property Leads</SectionTitle>
        <SectionSubtitle>
          The difference is not just marketing — it is infrastructure, intent intelligence,
          and a distribution model built to protect your competitive edge.
        </SectionSubtitle>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {differentiators.map((d, i) => (
            <div
              key={i}
              className="flex gap-4 p-5 rounded-2xl transition-all"
              style={{ background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.06)' }}
            >
              <div
                className="flex-shrink-0 w-10 h-10 rounded-xl flex items-center justify-center"
                style={{ background: `${d.accent}15`, color: d.accent, border: `1px solid ${d.accent}25` }}
              >
                {d.icon}
              </div>
              <div>
                <h3 className="font-heading font-bold text-white mb-1.5">{d.title}</h3>
                <p className="text-slate-500 text-sm leading-relaxed">{d.body}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function NextStepsSection({ client }: { client: ProposalClientRecord }) {
  const ctaMessage = client.proposal?.ctaMessage;
  const steps = [
    { icon: <CheckCircle2 className="w-5 h-5" />, step: '01', title: 'Align on Terms', body: 'Confirm package volume, pricing, and delivery schedule during this session.' },
    { icon: <Calendar className="w-5 h-5" />, step: '02', title: 'Contract & Onboarding', body: 'Sign the service agreement and complete a brief onboarding call with our operations team.' },
    { icon: <Zap className="w-5 h-5" />, step: '03', title: 'First Delivery', body: 'First batch of qualified leads delivered to your team within 24–72 hours of activation.' },
    { icon: <TrendingUp className="w-5 h-5" />, step: '04', title: 'Ongoing Delivery', body: 'Regular batches delivered per the agreed schedule, with quality reporting and replacement process in place.' },
  ];

  return (
    <section id="next-steps" className="py-24 px-6 md:px-12">
      <div className="max-w-4xl">
        <SectionBadge>Next Steps</SectionBadge>
        <SectionTitle>Moving Forward</SectionTitle>
        <SectionSubtitle>
          {ctaMessage ?? `Everything discussed in this session — the process, the qualification model, the pricing, and the team structure — is ready to activate. The steps below are short and straightforward.`}
        </SectionSubtitle>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-10">
          {steps.map((s, i) => (
            <div
              key={i}
              className="p-6 rounded-2xl"
              style={{ background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.06)' }}
            >
              <div
                className="w-9 h-9 rounded-xl flex items-center justify-center mb-4"
                style={{ background: 'rgba(37,99,235,0.12)', color: '#93c5fd', border: '1px solid rgba(37,99,235,0.2)' }}
              >
                {s.icon}
              </div>
              <p className="text-[10px] font-black text-blue-400 uppercase tracking-widest mb-2">Step {s.step}</p>
              <h3 className="font-heading font-bold text-white mb-2">{s.title}</h3>
              <p className="text-slate-500 text-sm leading-relaxed">{s.body}</p>
            </div>
          ))}
        </div>

        {/* Contact block */}
        <div
          className="p-8 rounded-2xl"
          style={{
            background: 'linear-gradient(135deg, rgba(37,99,235,0.08) 0%, rgba(99,102,241,0.06) 100%)',
            border: '1px solid rgba(37,99,235,0.2)',
          }}
        >
          <h3 className="font-heading text-xl font-bold text-white mb-2">
            The pipeline can be live within 24–72 hours.
          </h3>
          <p className="text-slate-400 text-sm mb-6 max-w-lg">
            If the conversation today confirms this is the right fit, there is no reason
            to wait. Activation is straightforward — and your team can be working the
            first batch of leads before the week is out.
          </p>
          <div className="flex flex-wrap gap-4">
            <a
              href={`mailto:dubaipropertylead@gmail.com?subject=${encodeURIComponent(
                `Moving Forward — ${client.companyName} × Dubai Property Leads`
              )}&body=${encodeURIComponent(
                `Hi Dubai Property Leads Team,\n\nFollowing our meeting and reviewing the proposal, we are ready to move forward with the ${client.proposal?.packageVolume ?? 300}-lead package for ${client.companyName}.\n\nPlease send over the service agreement and confirm the next steps to activate our delivery.\n\nBest regards,\n${client.contactName}\n${client.role ?? ''}\n${client.companyName}${client.phone ? `\n${client.phone}` : ''}`
              )}`}
              className="inline-flex items-center gap-2 px-5 py-3 rounded-xl text-white font-bold text-sm transition-all"
              style={{ background: '#2563eb' }}
              onMouseEnter={(e) => (e.currentTarget.style.background = '#1d4ed8')}
              onMouseLeave={(e) => (e.currentTarget.style.background = '#2563eb')}
            >
              <Mail className="w-4 h-4" />
              Email Our Team
            </a>
            <a
              href="tel:+971558814207"
              className="inline-flex items-center gap-2 px-5 py-3 rounded-xl font-bold text-sm transition-all"
              style={{
                background: 'rgba(255,255,255,0.05)',
                border: '1px solid rgba(255,255,255,0.1)',
                color: '#cbd5e1',
              }}
            >
              <Phone className="w-4 h-4" />
              +971 55 881 4207
            </a>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-16 pt-8 border-t border-white/5 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div>
            <p className="font-heading font-black text-white text-sm tracking-tight">
              DUBAI<span className="text-blue-400 italic">LEADS</span>
            </p>
            <p className="text-xs text-slate-600 mt-1">
              Confidential — prepared exclusively for {client.companyName}
            </p>
          </div>
          <div className="flex items-center gap-4 text-xs text-slate-600">
            {client.officeAddress && (
              <span className="flex items-center gap-1.5">
                <MapPin className="w-3 h-3" />
                {client.officeAddress}
              </span>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}

// ── Sidebar nav ──────────────────────────────────────────────────

function ProposalNav({ active }: { active: string }) {
  const scrollTo = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <nav className="hidden xl:flex flex-col gap-1 w-48 fixed left-6 top-1/2 -translate-y-1/2 z-30">
      {NAV_SECTIONS.map((s) => (
        <button
          key={s.id}
          onClick={() => scrollTo(s.id)}
          className="group flex items-center gap-3 text-left py-1.5 transition-all"
        >
          <span
            className="flex-shrink-0 w-1 h-4 rounded-full transition-all duration-300"
            style={{
              background: active === s.id ? '#3b82f6' : 'rgba(255,255,255,0.1)',
              transform: active === s.id ? 'scaleY(1.5)' : 'scaleY(1)',
            }}
          />
          <span
            className="text-xs font-medium transition-colors duration-200"
            style={{ color: active === s.id ? '#e2e8f0' : '#475569' }}
          >
            {s.label}
          </span>
        </button>
      ))}
    </nav>
  );
}

// ── Root component ───────────────────────────────────────────────

export default function ProposalContent({ client }: Props) {
  const router = useRouter();
  const activeSection = useIntersect(NAV_SECTIONS.map((s) => s.id));
  const [logouting, setLogouting] = useState(false);

  async function logout() {
    setLogouting(true);
    await fetch('/api/proposals/auth/logout', { method: 'POST' });
    router.push('/proposals/login');
  }

  return (
    <div
      className="min-h-screen text-white relative"
      style={{ backgroundColor: '#05080f' }}
    >
      {/* Background grid */}
      <div
        className="fixed inset-0 pointer-events-none"
        style={{
          backgroundImage:
            'linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px)',
          backgroundSize: '80px 80px',
        }}
      />

      {/* Top bar */}
      <header
        className="fixed top-0 left-0 right-0 z-40 flex items-center justify-between px-6 py-4"
        style={{
          background: 'rgba(5,8,15,0.85)',
          borderBottom: '1px solid rgba(255,255,255,0.05)',
          backdropFilter: 'blur(20px)',
        }}
      >
        <div className="flex items-center gap-4">
          <span className="font-heading text-sm font-black text-white tracking-tight">
            DUBAI<span className="text-blue-400 italic">LEADS</span>
          </span>
          <span className="text-slate-700">×</span>
          <span className="text-sm font-semibold text-slate-400">{client.companyName}</span>
        </div>
        <button
          onClick={logout}
          disabled={logouting}
          className="flex items-center gap-1.5 text-xs text-slate-600 hover:text-slate-300 transition-colors"
        >
          <LogOut className="w-3.5 h-3.5" />
          {logouting ? 'Logging out…' : 'Logout'}
        </button>
      </header>

      {/* Sidebar nav */}
      <ProposalNav active={activeSection} />

      {/* Main content — offset for fixed header */}
      <main className="pt-16 xl:pl-60">
        <HeroSection client={client} />
        <AgendaSection client={client} />
        <ChallengeSection />
        <SolutionSection client={client} />
        <HowItWorksSection />
        <QualificationSection />
        <DeliverySection />
        <TeamFitSection client={client} />
        <SalesApproachSection client={client} />
        <PricingSection client={client} />
        <WhyUsSection />
        <NextStepsSection client={client} />
      </main>

      {/* Mobile bottom nav */}
      <div
        className="xl:hidden fixed bottom-0 left-0 right-0 z-40 py-3 px-4 overflow-x-auto"
        style={{
          background: 'rgba(5,8,15,0.95)',
          borderTop: '1px solid rgba(255,255,255,0.06)',
          backdropFilter: 'blur(20px)',
        }}
      >
        <div className="flex gap-2 min-w-max">
          {NAV_SECTIONS.map((s) => (
            <button
              key={s.id}
              onClick={() => document.getElementById(s.id)?.scrollIntoView({ behavior: 'smooth' })}
              className="flex-shrink-0 px-3 py-1.5 rounded-full text-xs font-medium transition-all"
              style={{
                background: activeSection === s.id ? 'rgba(37,99,235,0.2)' : 'rgba(255,255,255,0.04)',
                border: `1px solid ${activeSection === s.id ? 'rgba(37,99,235,0.4)' : 'rgba(255,255,255,0.07)'}`,
                color: activeSection === s.id ? '#93c5fd' : '#64748b',
              }}
            >
              {s.label}
            </button>
          ))}
        </div>
      </div>

      {/* Bottom padding for mobile nav */}
      <div className="xl:hidden h-16" />
    </div>
  );
}

```