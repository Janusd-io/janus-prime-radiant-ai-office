---
type: source
source_type: laptop
title: IMS Enrolment - Start Here
slug: ims-enrolment-start-here
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Desktop/IMS Enrolment - Start Here.md
original_size: 2123
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:42Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "Public welcome doc for /ims-enrolment skill — dept-shareable onboarding pointer."
---

# IMS Enrolment - Start Here

_Extracted from `Desktop/IMS Enrolment - Start Here.md` on 2026-05-14._

# IMS Enrolment — Start Here

The `/ims-enrolment` skill is now installed in your Claude Desktop.

## How to use it

1. Open Claude Desktop
2. Type one of these trigger phrases:
   - `/ims-enrolment`
   - *"Enrol [my department] into the IMS"*
   - *"Help [my team] document our processes for ISO"*
3. Claude walks you through a guided interview (Phases 1-5)

## What you'll end up with

A folder on your Desktop called **`<Your Department> - IMS Enrolment`** containing:

- Process documents (parent + sub-processes) in the ISO 9001 Figure 1 shape
- ChatGPT prompts you can paste to generate polished diagrams
- First Voice questionnaire for each person in your department
- A `HANDOVER-BUNDLE.docx` ready to send to Simon (ISO Lead)
- All Word doc exports for sharing outside Claude

## What you need

- **Claude Desktop** (already installed, you're reading this)
- **pandoc** (for Word doc export — install via `brew install pandoc` on Mac if missing)
- **30-60 min per department head interview** (Phase 2), **20-30 min per sub-process** (Phase 3)
- **A folder of patience** — the first run feels long because the skill is teaching you the structure. The second department goes 3× faster.

## Help, verify, update

| What | Command |
|---|---|
| Verify the skill is installed | `~/Documents/janus-puls-onboarding/install.sh --check` |
| Update to latest version | `cd ~/Documents/janus-puls-onboarding && git pull && ./install.sh` |
| Uninstall the skill | `~/Documents/janus-puls-onboarding/install.sh --uninstall` |
| Read the full install docs | `~/.claude/skills/ims-enrolment/INSTALL.md` |

## Worked example

If you get stuck during the interview, the skill ships with the **AI Department fully documented** as a reference:

`~/.claude/skills/ims-enrolment/examples/ai-department/`

That's a complete enrolment showing what every section should look like.

## Owner / contact

Jehad — AI Operations Engineer · jehada@janusd.io

---

*This file is dropped here once by `install.sh`. Feel free to delete it after reading — the skill itself doesn't need it. Re-running the installer won't overwrite it.*
