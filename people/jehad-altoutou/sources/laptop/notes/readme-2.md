---
type: source
source_type: laptop
title: README
slug: readme-2
created: 2026-04-24
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/assessify/skills/assessify-hr/README.md
original_size: 3922
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:33Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "Internal install guide for HR — operational"
project: assessify

---

# README

_Extracted from `[[assessify|assessify]]/skills/assessify-hr/README.md` on 2026-05-14._

# Assessify HR Skill for Claude Desktop

This folder contains a Claude skill that turns Claude Desktop into an Assessify HR assistant. Paired with the MCP connector already set up at `https://assessify.janusd.io/api/mcp`, Claude can browse assessments, draft new ones with weighted sections and questions, send candidate invites, and activate/deactivate assessments — all from plain-English requests.

## What's inside

- **`SKILL.md`** — the instructions Claude follows. Describes the 12 MCP tools, mandatory rules (search before create, confirm before publish/delete, email only when asked), common HR workflows, and style guidance.

## How to install (for Mariam)

Claude Desktop uses **Projects** to load custom instructions. The skill is just the `SKILL.md` file pasted into a Project's custom instructions.

### Step-by-step

1. **Open Claude Desktop** and confirm the Assessify connector is connected:
   - Settings → Connectors → you should see **Assessify** with a green "Connected" indicator.
   - If it's red / disconnected, click it and re-approve the OAuth screen (Jehad or an admin needs to be signed in to `assessify.janusd.io/admin` in a browser when you do this).

2. **Create a new Project in Claude Desktop:**
   - Click the **Projects** tab (left sidebar).
   - Click **New project**.
   - Name it: `Assessify HR`.
   - Description: `HR assistant for the Janus Digital hiring platform.`

3. **Add the skill as custom instructions:**
   - Open the project.
   - Click **Instructions** (sometimes labelled "Custom instructions" or the ⚙️ icon in the project panel).
   - Open `SKILL.md` from this folder in any text editor (TextEdit, VS Code, whatever).
   - Copy the entire contents **below the `---` frontmatter block** (everything from `# Assessify HR Assistant` to the end of the file).
   - Paste into the Instructions field.
   - Save.

4. **Attach the Assessify connector to this project:**
   - In the project's Tools panel, enable the **Assessify** connector.
   - That's it. Future chats inside this project will automatically use both the skill instructions and the Assessify tools.

5. **Test:**
   - Start a new chat inside the `Assessify HR` project.
   - Type: *"Show me all active assessments in Operations."*
   - Claude should call `list_departments` + `search_assessments` and reply with a table.

## Updating the skill later

When this `SKILL.md` is updated in the repo:
1. Pull the latest from [[github|GitHub]] (or Jehad sends you the new file).
2. Go back into the `Assessify HR` project → Instructions.
3. Replace the pasted content with the new `SKILL.md` body.

## Troubleshooting

| Symptom | Fix |
|---|---|
| "I don't have access to Assessify tools" | Connector isn't attached to the project — enable it in the project's Tools panel. |
| Connector shows disconnected | Reconnect via Settings → Connectors → Assessify. May need Jehad signed in to the admin panel during OAuth. |
| Claude invents assessment IDs or department names | The skill tells it to fetch IDs via `list_*` / `search_*` first. If it skips, reply: "Please search first — don't guess IDs." |
| Candidate got an email you didn't want sent | The skill defaults `sendEmail=false`. Only say "email" / "send" / "dispatch" when you actually want one sent. |
| A created assessment isn't visible to candidates | It's in draft by default. Say "publish it" or "activate the ⟨title⟩ assessment". |

## Scope

The skill only covers the 12 MCP tools the Assessify server exposes. These tasks still need the portal (`https://assessify.janusd.io/admin`):
- Editing existing questions, reordering sections, changing weights on a live assessment
- Reviewing candidate responses, session scores, analytics
- Leave requests, HR forms, easter eggs
- Team management (inviting admins)

Ask Claude for the direct admin URL if you're unsure where to go — the skill tells it to surface those links automatically.
