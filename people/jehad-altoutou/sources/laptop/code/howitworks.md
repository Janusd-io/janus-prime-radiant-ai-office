---
type: source
source_type: laptop
title: HowItWorks
slug: howitworks
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/HowItWorks.tsx
original_size: 2206
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# HowItWorks

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/HowItWorks.tsx` on 2026-05-14._

```tsx
import { ClipboardCheck, Database, Filter, Send } from 'lucide-react';

const steps = [
  {
    title: 'Acquisition',
    description: 'Buyers submit property inquiries through our highly targeted marketing campaigns across Google and Meta.',
    icon: Database,
  },
  {
    title: 'Verification',
    description: 'Each enquiry is verified, filtered, and checked for valid contact information and intent.',
    icon: Filter,
  },
  {
    title: 'Storage',
    description: 'Leads are prepared and stored in our secure buyer enquiry database, ready for distribution.',
    icon: ClipboardCheck,
  },
  {
    title: 'Delivery',
    description: 'When you purchase a package, the required leads are instantly allocated and emailed to you in CSV format.',
    icon: Send,
  },
];

export default function HowItWorks() {
  return (
    <section id="how-it-works" className="py-24 bg-slate-50">
      <div className="container mx-auto px-4">
        <div className="max-w-3xl mx-auto text-center mb-16">
          <h2 className="font-heading text-3xl md:text-5xl font-bold mb-4">How It Works</h2>
          <p className="text-muted-foreground text-lg">
            A fully automated pipeline designed to deliver high-quality buyer signals directly to your team.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {steps.map((step, index) => (
            <div key={index} className="relative p-8 rounded-2xl bg-white border border-border shadow-sm hover:shadow-md transition-all">
              <div className="w-14 h-14 rounded-2xl bg-blue-50 flex items-center justify-center text-primary mb-6">
                <step.icon className="w-7 h-7" />
              </div>
              <h3 className="text-xl font-bold mb-3">{step.title}</h3>
              <p className="text-sm text-muted-foreground leading-relaxed">
                {step.description}
              </p>
              
              {index < steps.length - 1 && (
                <div className="hidden lg:block absolute top-[60px] -right-4 w-8 h-px bg-slate-200 z-10"></div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

```