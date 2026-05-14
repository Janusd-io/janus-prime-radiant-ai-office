---
type: source
source_type: laptop
title: LeadQuality
slug: leadquality
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/LeadQuality.tsx
original_size: 6159
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# LeadQuality

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/LeadQuality.tsx` on 2026-05-14._

```tsx
import { BadgeCheck, Calendar, DollarSign, Mail, MapPin, MessageSquare, Phone, User } from 'lucide-react';

const leadFields = [
  { label: 'Full Name', icon: User },
  { label: 'Phone Number', icon: Phone, verified: true },
  { label: 'Email Address', icon: Mail, verified: true },
  { label: 'Nationality', icon: Globe },
  { label: 'Buyer Budget', icon: DollarSign },
  { label: 'Property Type Interest', icon: MapPin },
  { label: 'Inquiry Message', icon: MessageSquare },
  { label: 'Timestamp', icon: Calendar },
];

function Globe(props: any) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
      <line x1="2" y1="12" x2="22" y2="12" />
      <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
    </svg>
  );
}

export default function LeadQuality() {
  return (
    <section id="leads" className="py-24 bg-white">
      <div className="container mx-auto px-4">
        <div className="flex flex-col lg:flex-row gap-16 items-center">
          <div className="lg:w-1/2">
            <h2 className="font-heading text-3xl md:text-5xl font-bold mb-6 italic">High-Intent <span className="text-primary not-italic">Buyer Signals</span></h2>
            <p className="text-lg text-muted-foreground mb-8">
              We don't sell cold lists. Every lead is a <span className="font-bold text-foreground">Verified Buyer Enquiry</span>—someone who has actively seen a property and requested more information through our live delivery system.
            </p>
            
            <div className="space-y-4">
              <div className="flex gap-4 p-4 rounded-xl bg-slate-50 border border-slate-100 italic font-medium text-slate-700">
                "Each lead represents a real buyer who submitted a property inquiry."
              </div>
              <div className="flex items-center gap-3 text-sm font-semibold text-emerald-600">
                <BadgeCheck className="w-5 h-5" />
                Verified contact information guaranteed.
              </div>
            </div>
          </div>
          
          <div className="lg:w-1/2 w-full max-w-xl mx-auto lg:mx-0">
            <div className="relative group">
              <div className="absolute -inset-1 bg-gradient-to-r from-primary/20 via-emerald-500/20 to-blue-500/20 rounded-3xl blur-xl opacity-50 group-hover:opacity-100 transition duration-1000 group-hover:duration-200"></div>
              
              <div className="relative bg-slate-900/90 backdrop-blur-xl rounded-2xl p-5 md:p-6 shadow-2xl border border-white/5 overflow-hidden">
                {/* Decorative background elements */}
                <div className="absolute top-0 right-0 w-24 h-24 bg-primary/10 blur-3xl -mr-12 -mt-12"></div>
                <div className="absolute bottom-0 left-0 w-24 h-24 bg-emerald-500/10 blur-3xl -ml-12 -mb-12"></div>
                
                <div className="flex justify-between items-center mb-6">
                  <h3 className="text-white font-heading text-lg font-bold">Data points you receive</h3>
                  <div className="flex items-center gap-2">
                    <span className="relative flex h-1.5 w-1.5">
                      <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                      <span className="relative inline-flex rounded-full h-1.5 w-1.5 bg-emerald-500"></span>
                    </span>
                    <div className="px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 text-[9px] font-bold uppercase tracking-wider border border-emerald-500/20">
                      LIVE FEED
                    </div>
                  </div>
                </div>
                
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                  {leadFields.map((field, idx) => (
                    <div 
                      key={idx} 
                      className="group/item flex items-center gap-3 p-3 rounded-xl bg-white/5 border border-white/5 hover:border-white/10 hover:bg-white/[0.08] transition-all duration-300"
                    >
                      <div className="flex-shrink-0 w-8 h-8 rounded-lg bg-slate-800 flex items-center justify-center border border-white/5 text-primary group-hover/item:scale-105 group-hover/item:text-white transition-all">
                        <field.icon className="w-4 h-4" />
                      </div>
                      
                      <div className="flex flex-col">
                        <span className="text-white font-semibold text-xs leading-tight">{field.label}</span>
                        <div className="flex items-center gap-2 mt-1">
                          <div className="h-1 w-10 bg-white/10 rounded-full overflow-hidden">
                            <div className="h-full bg-primary/40 rounded-full w-full opacity-50"></div>
                          </div>
                          {field.verified && (
                            <div className="flex items-center gap-1 text-[7px] font-bold text-emerald-400 uppercase tracking-tighter">
                              <BadgeCheck className="w-2 h-2" />
                              VERIFIED
                            </div>
                          )}
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
                
                <div className="mt-6 pt-4 border-t border-white/5">
                  <div className="flex items-center justify-between text-[8px] font-bold uppercase tracking-widest text-white/30">
                    <span>SECURITY: AES-256</span>
                    <span>GDPR COMPLIANT</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

```