---
type: skill
tags: [skill, frontend, creative]
command: /creative-dev
path: ~/.claude/commands/creative-dev.md
---

# /creative-dev

Build immersive web experiences — scroll-triggered animations, 3D objects, interactive storytelling.

## Uses
- [[creative-dev-stack]]
- [[design-systems|A DESIGN.md]] (required)
- [[creative-dev-libraries]]

## Typical Flow
1. Check for DESIGN.md → if missing ask user to pick from [[design-systems]]
2. Install: react-three-fiber, gsap, lenis, motion, zustand
3. Scaffold: `canvas/`, `animations/`, `providers/`, `hooks/`, `shaders/`
4. Wire Lenis + GSAP single-RAF loop
5. Server Components for SEO, Client Components for visuals

## Related Skills
- [[nextjs-app]]
- [[ui-build]]
- [[react-patterns]]
- [[scaffold]]

## 🛠️ Build from scratch
Deepen this skill by re-creating the tech yourself: [[build-your-own-3d-renderer|3D Renderer]], [[build-your-own-augmented-reality|Augmented Reality]], [[build-your-own-game|Game]], [[build-your-own-physics-engine|Physics Engine]], [[build-your-own-uncategorized|Uncategorized]], [[build-your-own-voxel-engine|Voxel Engine]], [[build-your-own-web-browser|Web Browser]] — see [[build-your-own-x|Build Your Own X]].
