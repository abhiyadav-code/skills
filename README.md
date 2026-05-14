# Claude Skills

A collection of custom Claude skills built with the [skill-creator](https://claude.ai) tool.

## What are Claude Skills?

Skills are reusable instructions that extend Claude with specialized capabilities. Each skill is a folder containing a `SKILL.md` (the main skill definition) and optional `references/` files.

## Skills in this repo

| Skill | Description |
|-------|-------------|
| [review-resume](./review-resume/) | Evaluate a resume against a job posting from a senior recruiter's perspective. Produces a structured fit assessment with match %, percentile ranking, callback-killer issues, and an action plan. |

## How to use a skill

### On Claude.ai (web)
1. Download the `.skill` file from the [Releases](../../releases) page
2. Go to **Settings → Capabilities → Skills**
3. Click **Install Skill** and upload the `.skill` file

### On Claude Code / Claude Desktop
1. Clone this repo or download the skill folder
2. Copy the skill folder to `~/.claude/skills/<skill-name>/`
3. The skill is available immediately — no restart needed

## Contributing / Feedback

These skills are shared as-is. If you find them useful or have suggestions, open an issue.
