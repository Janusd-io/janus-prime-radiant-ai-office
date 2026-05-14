---
type: source
source_type: laptop
title: layout
slug: layout-3
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/layout.tsx
original_size: 3491
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# layout

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/layout.tsx` on 2026-05-14._

```tsx
import type { Metadata } from "next";
import { Inter, Outfit } from "next/font/google";
import "./globals.css";

const inter = Inter({
  variable: "--font-sans",
  subsets: ["latin"],
});

const outfit = Outfit({
  variable: "--font-heading",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  metadataBase: new URL("https://dubaipropertyleads.ae"),
  title: "Dubai Property Leads | Premium Real Estate Buyer Inquiries & Enquiries",
  description: "Access high-intent Dubai real estate investor and end-user enquiries. Verified property buyer leads delivered directly to agents and brokerages daily.",
  keywords: [
    "Dubai real estate leads",
    "Dubai property buyer leads",
    "off plan leads Dubai",
    "Dubai investor leads",
    "premium real estate inquiries",
    "verified property leads UAE",
    "real estate marketing Dubai",
    "property leads in dubai",
    "real estate leads in dubai",
    "real estate lead generation in dubai",
    "dubai property leads database",
    "off plan lead generation"
  ],
  openGraph: {
    title: "Dubai Property Leads | High-Conversion Real Estate Enquiries",
    description: "Start receiving hot buyer inquiries today. The premier source for verified Dubai property leads.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": ["Organization", "RealEstateAgent"],
    "name": "Dubai Property Leads",
    "url": "https://dubaipropertyleads.ae",
    "logo": "https://dubaipropertyleads.ae/logo.png",
    "description": "The premier B2B PropTech platform for verified Dubai real estate buyer enquiries and investor leads.",
    "sameAs": [
      "https://www.instagram.com/dubaipropertyleads",
      "https://www.linkedin.com/company/dubai-property-leads"
    ],
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Dubai",
      "addressCountry": "AE"
    },
    "contactPoint": {
      "@type": "ContactPoint",
      "email": "dubaipropertylead@gmail.com",
      "contactType": "sales",
      "areaServed": "Dubai",
      "availableLanguage": ["English", "Arabic"]
    },
    "hasOfferCatalog": {
      "@type": "OfferCatalog",
      "name": "Dubai Real Estate Lead Services",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Service",
            "name": "Verified Dubai Property Leads",
            "description": "High-intent buyer enquiries captured through targeted marketing and manual verification."
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Service",
            "name": "Off-Plan Investor Leads",
            "description": "Exclusive enquiries from international and local investors looking for off-plan property opportunities in Dubai."
          }
        }
      ]
    }
  };

  return (
    <html lang="en" className="scroll-smooth">
      <head>
        <link rel="alternate" type="text/plain" href="/llms.txt" />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body
        className={`${inter.variable} ${outfit.variable} font-sans antialiased selection:bg-blue-100 selection:text-blue-900`}
      >
        {children}
      </body>
    </html>
  );
}

```