---
type: source
source_type: laptop
title: Desktop Captures — seed
slug: seed-2
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/prisma/seed.js
original_size: 1910
original_ext: .js
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# seed

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/prisma/seed.js` on 2026-05-14._

```javascript
const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

const sampleLeads = [
  {
    name: 'John Doe',
    phone: '+971 50 123 4567',
    email: 'john.doe@example.com',
    nationality: 'British',
    budget: '2M - 5M AED',
    propertyType: 'Off-plan Apartment',
    inquiryMessage: 'I am interested in Emaar Beachfront projects.',
  },
  {
    name: 'Sarah Ahmed',
    phone: '+971 52 987 6543',
    email: 'sarah.ahmed@example.com',
    nationality: 'Emirati',
    budget: '10M+ AED',
    propertyType: 'Luxury Villa',
    inquiryMessage: 'Looking for a 5-bedroom villa in Palm Jumeirah.',
  },
  {
    name: 'Michael Chen',
    phone: '+86 138 0013 8000',
    email: 'm.chen@example.com',
    nationality: 'Chinese',
    budget: '1M - 2M AED',
    propertyType: 'Studio/1BR',
    inquiryMessage: 'Interested in high-yield investments in Business Bay.',
  },
  {
    name: 'Elena Rossi',
    phone: '+39 333 123 4567',
    email: 'elena.rossi@example.com',
    nationality: 'Italian',
    budget: '3M - 7M AED',
    propertyType: 'Townhouse',
    inquiryMessage: 'Searching for a family home in Tilal Al Ghaf.',
  },
  // Add more to fulfill at least the starter package for testing
  ...Array(100).fill(null).map((_, i) => ({
    name: `Test Buyer ${i + 1}`,
    phone: `+971 55 ${Math.floor(1000000 + Math.random() * 9000000)}`,
    email: `buyer${i + 1}@test.com`,
    nationality: i % 2 === 0 ? 'International' : 'Resident',
    budget: '1.5M AED',
    propertyType: 'Apartment',
    inquiryMessage: 'General property inquiry.',
  }))
];

async function main() {
  console.log('Seeding leads...');
  for (const lead of sampleLeads) {
    await prisma.lead.create({
      data: lead,
    });
  }
  console.log('Seeding finished.');
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });

```