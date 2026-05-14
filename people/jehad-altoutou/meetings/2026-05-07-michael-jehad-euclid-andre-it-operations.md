---
type: source
source_type: meeting
title: "Michael, Jehad, Euclid, Andre IT Operations"
slug: 2026-05-07-michael-jehad-euclid-andre-it-operations
created: 2026-05-07
captured_by: jehad-altoutou
attendees: [michael-bruck, jehad-altoutou, euclid-wong, andrey-timokhov]
duration_min: 46
fireflies_id: 01KR0J82186X2H5MHF1WH48NY6
audience: "departments:ai-office,it-ops"
departments: [ai-office, it-ops]
dept_scope: [ai-office, it-ops]
sensitivity: dept
task_tracker: monday
parsed_at: "2026-05-14T09:51:32Z"
parser_version: 2
summary: "Michael convened Jehad and Euclid (with Andre / Speaker 1 present) to figure out where Janus should store its growing body of cross-departmental knowledge — staff manuals, HR policies, ISO docs, insurance, business licenses, brand guidelines — given that Google Drive is treated as 'a warehouse' and "
topics: [knowledge-management, google-shared-drives, google-groups, department-permissions, internal-portal, naming-conventions, ai-office-systems-of-record, wiki]
decisions: [2026-05-07-google-shared-drives-as-janus-doc-store-baseline, 2026-05-07-google-groups-drive-permissions, 2026-05-07-per-department-public-restricted-split, 2026-05-07-ai-office-and-it-as-shared-drive-pilot, 2026-05-07-contributor-default-not-manager]
action_items_count: 4
confidence_overall: high
---

# Michael, Jehad, Euclid, Andre IT Operations

**Date:** 2026-05-07
**Attendees:** [[michael-bruck]], [[jehad-altoutou]], [[euclid-wong]], [[andrey-timokhov]]
**Duration:** 46 min
**Fireflies:** [original meeting](https://app.fireflies.ai/view/01KR0J82186X2H5MHF1WH48NY6)

---

## Summary

Michael convened Jehad and Euclid (with Andre / Speaker 1 present) to figure out where Janus should store its growing body of cross-departmental knowledge — staff manuals, HR policies, ISO docs, insurance, business licenses, brand guidelines — given that Google Drive is treated as 'a warehouse' and AI Office's current stack (Linear AIR, Monday projects, Notion log, Fireflies, Claude Cowork) is internal to AIO. Jehad walked Michael through the AIO systems-of-record map and confirmed he is already building a wiki to synthesise it. The group converged on a Google Shared Drives baseline organised per department, with a per-department public/restricted (or '<Dept>' and '<Dept> private') split, permissions wired via Google Groups so onboarding auto-adds members. Michael proposed AI Office + IT as the worked example for the rollout, and that Gemini be consulted for Google Workspace best practice. Naming conventions and calendar-invite naming were flagged as open follow-ups (Simon was previously tasked with naming conventions). The 'internal portal / wiki' layer above shared drives was agreed in principle but deferred behind the storage layer.

## Decisions

- [[2026-05-07-google-shared-drives-as-janus-doc-store-baseline]] — Google Shared Drives as the Janus document-store baseline, per department
- [[2026-05-07-google-groups-drive-permissions]] — Permissions on Shared Drives are wired through Google Groups, not individual users
- [[2026-05-07-per-department-public-restricted-split]] — Each department's Shared Drive has a restricted (internal) folder and a company-wide folder
- [[2026-05-07-ai-office-and-it-as-shared-drive-pilot]] — AI Office and IT Ops are the pilot departments for the Shared Drive convention
- [[2026-05-07-contributor-default-not-manager]] — Default Shared Drive role for department members is Contributor, not Manager

## Action items

- [ ] @euclid-wong Stand up the Google Shared Drive + Google Group pattern for IT Ops as the pilot, mirroring what AI Office is doing. (raised by @jehad-altoutou) — Monday
- [ ] @jehad-altoutou Set up the AI Office Shared Drive (with restricted internal and company-wide subfolders) and back it with a Google Group, as the worked example. — Monday
- [ ] @jehad-altoutou Ask Gemini for Google Workspace best practice on per-department Shared Drive + Group permissions, and bring the recommendation back. (raised by @michael-bruck) — Monday
- [ ] @euclid-wong Create per-department Google Groups (HR, Finance, Marketing, IT, AI Office, Office of CEO, Training) so drive permissions can be inherited from group membership. (raised by @michael-bruck) — Monday

## 🎯 This week

- @jehad-altoutou Continue building the wiki / knowledge overlay on top of Linear AIR, Monday projects, and the Notion log, so it is ready to migrate Michael's knowledge into once the Shared Drive layer is settled.
- @team Bake Shared Drive setup and per-department group membership into the employee onboarding procedure, so new joiners inherit drive access automatically. (raised by @jehad-altoutou)

## 🏔️ Long horizon

- Build an internal portal / wiki layer above the per-department Shared Drives that indexes and surfaces the right documents per role, similar to SharePoint-per-department at Jehad's previous law firm (could be Google Sites, custom-built, or AI-generated). (owner: @jehad-altoutou; horizon: quarter)
- Migrate the AIO/IT knowledge layer (Linear AIR, Monday, Notion log, Fireflies, Claude Cowork synthesis) into the company-wide knowledge structure once the Shared Drive baseline is set up and the wiki overlay is ready. (owner: @jehad-altoutou; horizon: quarter)
- Roll the Shared Drive + Groups + restricted/public convention out across all Janus departments (HR, Finance, Marketing, Office of CEO, Training, ISO) once the AIO and IT pilots prove it. (owner: @michael-bruck; horizon: quarter)
- Establish a Janus-wide naming convention for files, folders, and calendar invites (Simon was previously tasked with this; should be coordinated with the new IT-operator hires' background). (owner: @simon-tarskih; horizon: weeks)

## Findings

- The AI Office's knowledge stack today is: Linear AIR (AI tool registry, 'AI Arc'), Monday (projects), Notion (log / description / history), Fireflies (raw meetings), and Claude Cowork (the synthesis brain that maps transcripts into the three systems). (stated by @jehad-altoutou)
- Google Shared Drives are owned by the Google Workspace entity, not by any individual user — content survives the owner leaving the company, unlike personal My Drive folders. (stated by @michael-bruck)
- Google's permission model is coarser than Microsoft's — granular per-level access control is harder in Google than in SharePoint, which is part of why Microsoft has historically had stronger enterprise penetration. (stated by @jehad-altoutou; confidence: medium)
- Google Shared Drives can be desktop-synced (and Jehad sets this up by default on every Janus laptop), but heavy Excel sync — especially on Windows for the finance team — historically causes conflicts and corruption. (stated by @michael-bruck)
- Once a Google Group is granted access to a folder, IT cannot directly remove the group from the folder's access list without changing the role configuration — there are Google licensing / role limits on permission management surfaced live in the meeting. (stated by @jehad-altoutou; confidence: medium)
- Claude can write text into Slack Canvas but cannot create or edit tables there, which is why the AIO Canvas is updated manually and infrequently. (stated by @michael-bruck)
- Bonaventure is a member of every department's Google Group, so the CEO inherits read access to all department drives by construction. (stated by @jehad-altoutou)

## Open questions

- What is the canonical naming for each department's two folders — 'public/private', 'internal/external', '<Dept>' / '<Dept> restricted', or something else? 'External' was rejected because it implies outside the company; 'restricted' was tentatively adopted but not finalised. (raised by @jehad-altoutou)
- How should country structure (Singapore, UK, future offices) be reflected in the Shared Drive layout — sub-drives under each department, separate global drives, or central-by-default since HR / Admin / AI / IT are run as global functions? (raised by @jehad-altoutou)
- Who administers the eventual internal portal (the layer above the Shared Drives)? Each department curates its own page, but cross-department upkeep needs an owner. (raised by @michael-bruck)
- Should department heads be able to assign permissions on subfolders within their department's drive (e.g. project-specific access), or should every permission change route through IT? (raised by @jehad-altoutou)
- What is the right pattern for vendor / project-specific Shared Drive access — a third category beyond 'department-restricted' and 'company-wide'? (raised by @jehad-altoutou)

## Blockers

- Google's licensing or role configuration prevents IT from removing certain groups from a folder's access list, which complicates clean permission lifecycle on Shared Drives. (owner: @euclid-wong)
- Heavy Excel files (especially finance) corrupt or break on Windows desktop sync of Shared Drives, which blocks 'just turn on sync everywhere' as a recommendation. (owner: @euclid-wong)

## Tool mentions

- [[google-drive]] — primary candidate doc-store, both personal and shared-drive variants
- [[google-workspace]] — the underlying suite providing Groups, Shared Drives, and Sites
- [[google-groups]] — the permissioning primitive — drives are shared with groups, members are auto-mapped
- [[google-sites]] — potential platform for the internal portal layer above Shared Drives
- [[gemini]] — to be queried for Google Workspace permission best-practice guidance
- [[microsoft-sharepoint]] — comparison point — used at Jehad's previous law firm for per-department portals
- [[notion]] — AIO's current log / notebook surface; debated as a knowledge-store option for the company at large
- [[linear]] — system of record for the AI tools registry ('AI Arc')
- [[monday-com]] — system of record for AI Office projects
- [[fireflies]] — raw meeting transcripts feeding the Claude Cowork synthesis pipeline
- [[claude-cowork]] — the AIO synthesis brain that pulls Fireflies transcripts into Linear / Monday / Notion
- [[slack-canvas]] — current AI tool registry surface — Canvas can be written by Claude but only as text, not tables, so it is updated manually
- [[zendesk]] — example project AIO is building automation for, used to anchor what counts as a 'project'

## Topics

- knowledge-management
- google-shared-drives
- google-groups
- department-permissions
- internal-portal
- naming-conventions
- ai-office-systems-of-record
- wiki

## Related

- Project: [[janus-prime-radiant-build]] — Jehad's in-progress wiki is the synthesis layer that sits above the Shared Drive baseline discussed here
- Project: [[ai-registry-v2]] — Jehad walked Michael through the AI Tools Registry ('AI Arc') as one of the three AIO systems of record
- Concept: [[llm-wiki]] — Jehad described the wiki he is building as the cross-departmental knowledge layer above the drives
- Vendor: [[google-drive]] — primary doc-store decision
- Vendor: [[google-workspace]] — underlying platform for Groups, Drives, Sites
- Vendor: [[google-groups]] — permissioning primitive selected for per-department access
- Vendor: [[google-sites]] — candidate for the internal portal layer above the drives
- Vendor: [[gemini]] — to be consulted for Workspace best-practice guidance
- Vendor: [[microsoft-sharepoint]] — comparison case from Jehad's prior employer
- Vendor: [[notion]] — discussed as alternative knowledge surface; remains AIO's log
- Vendor: [[linear]] — AIO system of record for the AI registry
- Vendor: [[monday-com]] — AIO system of record for projects
- Vendor: [[fireflies]] — raw transcript layer feeding the synthesis pipeline
- Vendor: [[claude-cowork]] — the AIO synthesis brain
- Person: [[bonaventure-wong]] — named as automatic member of every department group (CEO)
- Person: [[andrew-soane]] — marketing example used to motivate the public-folder split (brand guidelines)
- Person: [[simon-tarskih]] — previously tasked with naming conventions; still pending
- Person: [[theresa-wong]] — named as an HR drive participant in the worked example
- Department: [[ai-office]] — pilot department for the Shared Drive + Group convention
- Department: [[it-ops]] — co-pilot department for the convention; owns the Workspace administration
- Department: [[hr]] — primary target of the policy / insurance / handbook storage question
- Department: [[finance]] — called out for the Excel-on-Windows sync problem
- Department: [[marketing]] — brand-guidelines example for the company-wide folder pattern
- Department: [[office-of-ceo]] — Bonaventure as group-member-of-everyone
- Department: [[training]] — named as an upcoming department that will need the same setup

---

## Transcript

See [[2026-05-07-michael-jehad-euclid-andre-it-operations.transcript|full transcript]]
