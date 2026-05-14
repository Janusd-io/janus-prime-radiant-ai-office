---
type: source
source_type: laptop
title: page
slug: page-51
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/about/page.tsx
original_size: 11753
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# page

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/about/page.tsx` on 2026-05-14._

```tsx
import type { Metadata } from "next";
import Link from "next/link";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import {
  Building2,
  Target,
  Users,
  ShieldCheck,
  TrendingUp,
  Globe,
  Award,
  Handshake,
} from "lucide-react";

export const metadata: Metadata = {
  title: "About Us | Dubai Property Leads – Who We Are",
  description:
    "Learn about Dubai Property Leads — the team, mission, and technology behind the UAE's premier verified real estate buyer lead marketplace.",
  openGraph: {
    title: "About Dubai Property Leads",
    description:
      "The team and story behind the UAE's most trusted source of verified real estate buyer enquiries.",
    type: "website",
  },
};

const stats = [
  { value: "12,000+", label: "Verified Leads Delivered" },
  { value: "320+", label: "Active Brokerages" },
  { value: "97%", label: "Lead Authenticity Rate" },
  { value: "Instant", label: "Avg. Delivery Time" },
];

const values = [
  {
    icon: ShieldCheck,
    title: "Verified by Default",
    description:
      "Every lead goes through a multi-step verification process — phone, budget intent, and property type — before reaching your inbox. No guesswork, no wasted calls.",
  },
  {
    icon: TrendingUp,
    title: "Data-Driven Quality",
    description:
      "Our proprietary scoring engine ranks leads by conversion probability, so your agents spend time on the highest-value enquiries first.",
  },
  {
    icon: Handshake,
    title: "Partner-First",
    description:
      "We operate as an extension of your team. Our support team is available 7 days a week to ensure every batch of leads performs for your brokerage.",
  },
  {
    icon: Globe,
    title: "Global Reach, Local Expertise",
    description:
      "We capture enquiries from 40+ source countries — all pre-screened for Dubai-specific intent. Our team knows the UAE market inside out.",
  },
];

const team = [
  {
    name: "Jehad Altoutou",
    role: "Founder",
    bio: "A Dubai real estate operator with a sharp eye for what agents actually need to close deals. Jehad built Dubai Property Leads from the ground up after experiencing firsthand how broken the lead generation industry was — overpriced portals, unverified contacts, and zero accountability. He combined his deep market knowledge with modern technology to create the UAE's most transparent and results-driven lead marketplace. Every feature on this platform reflects a genuine pain point he's solved.",
    initials: "JA",
    color: "bg-blue-600",
  },
];

export default function AboutPage() {
  return (
    <>
      <Navbar />

      <main className="pt-20">
        {/* Hero */}
        <section className="relative py-28 overflow-hidden bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900">
          <div className="absolute inset-0 opacity-20"
            style={{
              backgroundImage:
                "radial-gradient(circle at 20% 50%, #2563eb 0%, transparent 50%), radial-gradient(circle at 80% 20%, #3b82f6 0%, transparent 40%)",
            }}
          />
          <div className="relative container mx-auto px-4 text-center text-white">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-500/20 border border-blue-400/30 text-blue-300 text-sm font-semibold mb-8">
              <Building2 className="w-4 h-4" />
              Our Story
            </div>
            <h1 className="text-5xl md:text-7xl font-heading font-black tracking-tight mb-6">
              Built by Real Estate
              <br />
              <span className="text-blue-400">Professionals, for Them.</span>
            </h1>
            <p className="text-lg md:text-xl text-slate-300 max-w-2xl mx-auto leading-relaxed">
              We started Dubai Property Leads after years of struggling with low-quality, unverified leads from generic portals. We built the platform we always wished existed.
            </p>
          </div>
        </section>

        {/* Stats bar */}
        <section className="bg-white border-b border-slate-100 py-12">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
              {stats.map((stat) => (
                <div key={stat.label}>
                  <p className="text-4xl font-heading font-black text-blue-600 mb-1">
                    {stat.value}
                  </p>
                  <p className="text-sm text-slate-500 font-medium">{stat.label}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Mission */}
        <section className="py-24 bg-slate-50">
          <div className="container mx-auto px-4">
            <div className="grid md:grid-cols-2 gap-16 items-center max-w-5xl mx-auto">
              <div>
                <div className="flex items-center gap-3 mb-6">
                  <div className="w-10 h-10 rounded-xl bg-blue-600 flex items-center justify-center">
                    <Target className="w-5 h-5 text-white" />
                  </div>
                  <span className="text-sm font-bold text-blue-600 uppercase tracking-widest">Our Mission</span>
                </div>
                <h2 className="text-4xl font-heading font-black text-slate-900 mb-6 leading-tight">
                  Close more deals. Waste less time.
                </h2>
                <p className="text-slate-600 text-lg leading-relaxed mb-6">
                  The Dubai real estate market moves fast. Agents and brokerages can't afford to chase cold, unverified leads. We exist to bridge the gap between genuine property buyers and the professionals best positioned to serve them.
                </p>
                <p className="text-slate-600 text-lg leading-relaxed">
                  Our platform combines targeted digital marketing, manual verification, and AI-powered lead scoring to deliver only the most qualified enquiries — packaged cleanly and delivered instantly.
                </p>
              </div>
              <div className="space-y-5">
                {[
                  "We never resell a lead more than 3 times",
                  "Each lead includes full contact details & intent notes",
                  "Budget, nationality, and property type pre-filtered",
                  "Replacement guarantee on invalid or duplicate leads",
                  "RERA-compliant data handling across all markets",
                ].map((point) => (
                  <div key={point} className="flex items-start gap-3 p-4 rounded-xl bg-white border border-slate-100 shadow-sm">
                    <div className="w-5 h-5 rounded-full bg-blue-600 flex items-center justify-center flex-shrink-0 mt-0.5">
                      <svg className="w-3 h-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={3}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                      </svg>
                    </div>
                    <p className="text-slate-700 font-medium text-sm">{point}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* Values */}
        <section className="py-24 bg-white">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-50 border border-blue-100 text-blue-600 text-sm font-semibold mb-6">
                <Award className="w-4 h-4" />
                What We Stand For
              </div>
              <h2 className="text-4xl font-heading font-black text-slate-900">
                Our Core Values
              </h2>
            </div>
            <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-6xl mx-auto">
              {values.map((value) => {
                const Icon = value.icon;
                return (
                  <div
                    key={value.title}
                    className="p-6 rounded-2xl border border-slate-100 bg-slate-50 hover:border-blue-200 hover:shadow-md transition-all group"
                  >
                    <div className="w-12 h-12 rounded-xl bg-blue-600 flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
                      <Icon className="w-6 h-6 text-white" />
                    </div>
                    <h3 className="text-lg font-bold text-slate-900 mb-3">{value.title}</h3>
                    <p className="text-slate-500 text-sm leading-relaxed">{value.description}</p>
                  </div>
                );
              })}
            </div>
          </div>
        </section>

        {/* Team */}
        <section className="py-24 bg-slate-50">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-50 border border-blue-100 text-blue-600 text-sm font-semibold mb-6">
                <Users className="w-4 h-4" />
                The Team
              </div>
              <h2 className="text-4xl font-heading font-black text-slate-900">
                The Person Behind the Platform
              </h2>
              <p className="text-slate-500 mt-4 max-w-xl mx-auto">
                Built by someone who lived the problem — a Dubai real estate professional who got tired of paying for leads that went nowhere.
              </p>
            </div>
            <div className="flex justify-center">
              {team.map((member) => (
                <div
                  key={member.name}
                  className="bg-white rounded-2xl border border-slate-100 p-10 text-center shadow-sm hover:shadow-md transition-shadow max-w-lg w-full"
                >
                  <div className={`w-24 h-24 rounded-2xl ${member.color} flex items-center justify-center text-white text-3xl font-black mx-auto mb-6`}>
                    {member.initials}
                  </div>
                  <h3 className="text-2xl font-bold text-slate-900">{member.name}</h3>
                  <p className="text-blue-600 text-sm font-semibold mb-5 mt-1">{member.role}</p>
                  <p className="text-slate-500 leading-relaxed">{member.bio}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* CTA */}
        <section className="py-24 bg-gradient-to-br from-blue-600 to-blue-800">
          <div className="container mx-auto px-4 text-center text-white">
            <h2 className="text-4xl font-heading font-black mb-6">
              Ready to fill your pipeline?
            </h2>
            <p className="text-blue-100 text-lg mb-10 max-w-xl mx-auto">
              Join 320+ Dubai brokerages already receiving verified buyer leads every week.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                href="/#pricing"
                className="px-8 py-4 bg-white text-blue-700 rounded-full font-bold text-base hover:bg-blue-50 transition-all shadow-lg"
              >
                View Pricing
              </Link>
              <Link
                href="mailto:dubaipropertylead@gmail.com"
                className="px-8 py-4 bg-white/10 text-white border border-white/30 rounded-full font-bold text-base hover:bg-white/20 transition-all"
              >
                Contact Us
              </Link>
            </div>
          </div>
        </section>
      </main>

      <Footer />
    </>
  );
}

```