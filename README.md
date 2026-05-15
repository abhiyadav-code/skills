# Skills by Abhi

A personal collection of AI agent skills — built by hand, with Claude's skill-creator, or adapted from other sources.

## What are skills?

Skills are reusable instruction sets that extend AI assistants with specialized capabilities. Each skill lives in its own folder with a `SKILL.md` (the main definition) and an optional `references/` directory for supporting context.

## Skills in this repo

| Skill | Source | Description |
|-------|--------|-------------|
| [review-resume](./review-resume/) | Claude skill-creator | Evaluate a resume against a job posting from a senior recruiter's perspective. Produces a structured fit assessment with match %, percentile ranking, callback-killer issues, and an action plan. |
| [pm-twin](./pm-twin/) | Hand-crafted | Acts as a high-level Tech Chief of Staff for PMs. Synthesizes meeting transcripts and chat discussions into product artifacts (PRDs, strategy docs). Search-first, zero-manual-registry. |

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
