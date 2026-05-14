---
type: source
source_type: laptop
title: easter-eggs
slug: easter-eggs
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/easter-eggs.ts
original_size: 2681
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# easter-eggs

_Extracted from `[[assessify|assessify]]/src/lib/easter-eggs.ts` on 2026-05-14._

```typescript
// ─── Easter Egg Definitions ─────────────────────────────────
// DO NOT expose this file to the client bundle.

export const EGGS = {
  egg_1: {
    id: "egg_1",
    difficulty: "easy",
    value: "egg{curiosity_is_the_first_step}",
    name: "The Source Seeker",
    description: "Found by inspecting the page elements",
    hints: [
      "Great explorers always check what is beneath the surface.",
      "The browser sees more than your eyes do. Try inspecting the page elements.",
      "Open DevTools, look at the Elements tab on the thank-you page. Some elements are hidden but still there.",
    ],
  },
  egg_2: {
    id: "egg_2",
    difficulty: "medium",
    value: "egg{headers_speak_louder_than_words}",
    name: "The Network Whisperer",
    description: "Found by inspecting HTTP response headers",
    hints: [
      "Data travels in more ways than what you see on screen.",
      "HTTP has a lot to say, if you listen to its headers.",
      "Open your browser's Network tab and inspect the response headers on API calls. Some headers aren't standard.",
    ],
  },
  egg_3: {
    id: "egg_3",
    difficulty: "hard",
    value: "egg{the_key_was_inside_you_all_along}",
    name: "The Vault Cracker",
    description: "Found by decoding a hex console message and using it to unlock a hidden API",
    hints: [
      "Some systems are chatty when no one's watching. Open the console.",
      "Numbers can be letters in disguise. Think hexadecimal.",
      "Decode the runtime ID from the console, then try knocking on /api/easter/vault with the decoded key.",
    ],
  },
  egg_4: {
    id: "egg_4",
    difficulty: "impossible",
    value: "egg{the_impossible_is_just_the_untried}",
    name: "The Impossible Find",
    description: "Found through robots.txt, a hidden API, and ROT13 decryption",
    hints: [], // No hints. The aria-label is the only breadcrumb.
  },
} as const;

export type EggId = keyof typeof EGGS;

export function validateEgg(eggValue: string): EggId | null {
  for (const [id, egg] of Object.entries(EGGS)) {
    if (egg.value === eggValue) return id as EggId;
  }
  return null;
}

export function getHint(eggId: EggId, hintLevel: number): string | null {
  const egg = EGGS[eggId];
  if (!egg || !egg.hints.length) return null;
  const idx = Math.min(hintLevel, egg.hints.length - 1);
  return egg.hints[idx] ?? null;
}

// ROT13 for the impossible egg
export function rot13(str: string): string {
  return str.replace(/[a-zA-Z]/g, (c) => {
    const base = c <= "Z" ? 65 : 97;
    return String.fromCharCode(((c.charCodeAt(0) - base + 13) % 26) + base);
  });
}

```