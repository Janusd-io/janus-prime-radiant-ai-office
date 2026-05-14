---
type: source
source_type: laptop
title: FAQ
slug: faq
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/FAQ.tsx
original_size: 7495
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# FAQ

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/FAQ.tsx` on 2026-05-14._

```tsx
'use client';

import { useState } from 'react';
import { ChevronDown, HelpCircle, MessageCircle, ShieldCheck, Wallet, Zap } from 'lucide-react';

const faqs = [
  {
    question: 'What is Dubai Property Leads?',
    answer: 'Dubai Property Leads is the premier B2B PropTech marketplace connecting real estate professionals with verified, high-intent buyer inquiries. We provide a streamlined, automated platform to acquire exclusive leads without the friction of cold calling.',
    icon: HelpCircle
  },
  {
    question: 'How can real estate agents buy buyer leads in Dubai?',
    answer: 'Agents can simply browse our verified lead packages on the website, select the bundle that fits their team\'s capacity (Starter, Growth, or Pro), and complete the purchase via our secure checkout. Once purchased, high-intent buyer inquiries are instantly allocated and delivered to your inbox.',
    icon: Zap
  },
  {
    question: 'Where can brokers get off-plan property leads?',
    answer: 'Right here. We specialize in off-plan buyer inquiries generated through targeted multi-channel marketing campaigns. Brokers can access exclusive leads interested in specific off-plan developments across Dubai, delivered as soon as the inquiry is verified.',
    icon: MessageCircle
  },
  {
    question: 'How much do Dubai real estate leads cost?',
    answer: 'We offer transparent, tiered pricing based on the volume and exclusivity of the leads. Packages start with our Starter Pack for those beginning their pipeline build, up to our Pro Pack for high-volume brokerages. Check our Pricing section for current rates and bundle discounts.',
    icon: Wallet
  },
  {
    question: 'How are the leads verified?',
    answer: 'Every inquiry undergoes a multi-layer verification process. We filter for valid contact details, check for genuine purchase intent, and ensure the lead is a fresh 24-48 hour signal before it enters our delivery system.',
    icon: ShieldCheck
  },
];

export default function FAQ() {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  const toggleFAQ = (index: number) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <section id="faq" className="py-24 bg-slate-50/50">
      <div className="container mx-auto px-4 max-w-5xl">
        <div className="text-center mb-16">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-100 text-blue-600 text-xs font-bold uppercase tracking-wider mb-4">
            Direct Answers
          </div>
          <h2 className="font-heading text-4xl md:text-5xl lg:text-6xl font-bold mb-6">
            Frequently Asked <span className="gradient-text">Questions</span>
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
            Everything you need to know about scaling your real estate business with our premium buyer inquiries.
          </p>
        </div>

        <div className="grid lg:grid-cols-12 gap-12 items-start">
          {/* Left Side: Visual/Text */}
          <div className="lg:col-span-4 space-y-6">
            <div className="p-8 rounded-3xl bg-white border border-slate-200 shadow-xl shadow-blue-500/5 relative overflow-hidden group">
              <div className="absolute top-0 right-0 w-32 h-32 bg-blue-500/5 rounded-full -mr-16 -mt-16 transition-transform group-hover:scale-110 duration-700"></div>
              <h3 className="text-2xl font-bold mb-4 relative z-10">Still have questions?</h3>
              <p className="text-slate-600 mb-8 relative z-10">Can't find the answer you're looking for? Reach out to our specialist team for immediate assistance.</p>
              <a 
                href="mailto:dubaipropertylead@gmail.com" 
                className="inline-flex items-center gap-2 text-primary font-bold hover:gap-3 transition-all underline underline-offset-4"
              >
                Get in touch today
                <Zap className="w-4 h-4 fill-current" />
              </a>
            </div>
            
            <div className="flex items-center gap-4 p-6 rounded-2xl bg-emerald-50 border border-emerald-100 italic text-sm text-emerald-800">
              <div className="flex-shrink-0 w-10 h-10 rounded-full bg-emerald-500 flex items-center justify-center text-white">
                <ShieldCheck className="w-5 h-5" />
              </div>
              "Every lead is verified for quality and intent."
            </div>
          </div>

          {/* Right Side: Accordion */}
          <div className="lg:col-span-8 space-y-4">
            {faqs.map((faq, index) => (
              <div 
                key={index} 
                className={`
                  group rounded-2xl border transition-all duration-300
                  ${openIndex === index 
                    ? 'bg-white border-blue-200 shadow-xl shadow-blue-500/5 ring-1 ring-blue-50' 
                    : 'bg-white/60 border-slate-100 hover:border-blue-100 hover:bg-white'}
                `}
              >
                <button
                  onClick={() => toggleFAQ(index)}
                  className="w-full flex items-start gap-5 p-6 text-left focus:outline-none"
                >
                  <div className={`
                    flex-shrink-0 w-12 h-12 rounded-xl flex items-center justify-center transition-colors
                    ${openIndex === index ? 'bg-primary text-white' : 'bg-slate-100 text-slate-400 group-hover:bg-blue-50 group-hover:text-primary'}
                  `}>
                    <faq.icon className="w-6 h-6" />
                  </div>
                  
                  <div className="flex-grow pt-2.5">
                    <span className={`
                      text-lg font-bold transition-colors
                      ${openIndex === index ? 'text-slate-900' : 'text-slate-700 group-hover:text-primary'}
                    `}>
                      {faq.question}
                    </span>
                    
                    <div className={`
                      grid transition-all duration-300 ease-in-out
                      ${openIndex === index ? 'grid-rows-[1fr] opacity-100 mt-4' : 'grid-rows-[0fr] opacity-0'}
                    `}>
                      <div className="overflow-hidden">
                        <p className="text-slate-600 leading-relaxed pb-2">
                          {faq.answer}
                        </p>
                      </div>
                    </div>
                  </div>
                  
                  <div className={`
                    flex-shrink-0 pt-3 transition-transform duration-300
                    ${openIndex === index ? 'rotate-180 text-primary' : 'text-slate-300'}
                  `}>
                    <ChevronDown className="w-5 h-5" />
                  </div>
                </button>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Structured Data for FAQPage */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faqs.map((faq) => ({
              "@type": "Question",
              "name": faq.question,
              "acceptedAnswer": {
                "@type": "Answer",
                "text": faq.answer,
              },
            })),
          }),
        }}
      />
    </section>
  );
}

```