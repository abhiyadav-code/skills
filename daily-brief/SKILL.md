---
name: daily-brief
description: >
  Set up and run a personalized Daily Executive Brief — a rich HTML morning digest
  delivered to your email and pinned in your Cowork sidebar every weekday. The brief
  pulls from Gmail (urgent emails, recruiter outreach, overdue personal items), Google
  Calendar (today + tomorrow, conflict detection), Todoist (overdue tasks, this week's
  to-dos, job search pipeline), course calendars (deadlines and homework), and newsletters
  (Stratechery, a16z, Axios, Substack). Outputs a fully formatted, Gmail-safe HTML email
  with clickable action chips, colored priority order, and per-item dismiss buttons.

  Use this skill when the user says anything like: "set up a daily brief", "create a
  morning briefing agent", "I want a daily email summary", "build me a daily digest",
  "automate my morning routine", "set up a daily standup email", "create an executive
  brief agent", or "I want to get a summary of my emails and calendar every morning".
  Also trigger when the user asks to configure, update, or re-run their daily brief.
---

# Daily Executive Brief — Setup Guide

This skill configures a scheduled agent that generates a personalized morning brief
every weekday and delivers it to your inbox. It takes about 5 minutes to set up.

---

## What the brief includes

- 🎯 **Priority order** — top 5 things to do today, color-coded by urgency
- 🚨 **Overdue items** — emails where someone is waiting, tasks past due
- 📋 **Work to-do** — this week's Todoist tasks (optional)
- 📬 **Email action items** — filtered: real humans only, no spam/alerts
- 💼 **Job search pipeline** — recruiter outreach + LinkedIn roles to evaluate
- 📅 **Calendar** — today + tomorrow, conflict badges, RSVP reminders
- 🎓 **Course deadlines** — from imported course calendars
- 📰 **News & insights** — top newsletter takeaways (Stratechery, a16z, Axios, etc.)

---

## Required connectors

Before running setup, make sure these are connected in Cowork:

| Connector | Used for |
|-----------|----------|
| **Gmail** | Email action items, overdue personal emails, job search, newsletters |
| **Google Calendar** | Today/tomorrow events, conflict detection, course deadlines |
| **Todoist** *(optional)* | Overdue tasks, work to-do list, job search pipeline stages |

---

## Setup process

When the user triggers this skill, walk them through these steps:

### Step 1 — Collect configuration

Ask the user for the following. Explain each briefly so they know where to find it:

```
1. Your email address (for the Gmail draft recipient)
2. Your name (for the "Good morning, [Name]" greeting)
3. Your timezone (e.g. America/Los_Angeles, America/New_York)
4. Your city/region (shown in the brief header, e.g. "San Francisco Bay Area")
5. Output folder path — where to save the HTML files
   (Suggest: ~/Documents/DailyBrief/ or ask them to select a Cowork folder)
6. Todoist: are you using it? (yes/no)
   If yes: Job Search project ID, Work To-Do project ID (find in Todoist URL)
7. Course calendars: any imported course calendars in Google Calendar?
   If yes: collect the calendar IDs (found in Google Calendar Settings > each calendar > Calendar ID)
8. Newsletter filters: which newsletters do you subscribe to?
   (Default: Stratechery, a16z, Axios, Substack, StrictlyVC)
9. What topics/senders should ALWAYS be excluded?
   (Default excludes: shipping notifications, account statements, promotions, LinkedIn auto-alerts)
10. Preferred send time (default: 7:00 AM weekdays)
```

Be conversational — ask 2-3 questions at a time, not all 10 at once. Confirm the answers before proceeding.

### Step 2 — Create the dismissed items file

Create a `dismissed-items.json` file in their output folder:

```json
{
  "dismissed": []
}
```

Explain: "This file tracks items you've dismissed from the brief. When you tap × on an item in the Cowork view, it gets added here and won't appear in future briefs. You can also tell me to dismiss something anytime."

### Step 3 — Create the scheduled task

Using the collected config, build the scheduled task prompt by filling in the template from `templates/scheduled-prompt.md`. Then call `mcp__scheduled-tasks__create_scheduled_task` with:

- **description**: "[Name]'s Daily Executive Brief"
- **prompt**: the filled-in template
- **cronExpression**: convert their preferred time to a 5-field cron (e.g. `0 7 * * 1-5` for 7 AM Mon–Fri)

### Step 4 — Run it now

Offer to run the brief immediately so they can see what it looks like. Say:

> "Your brief is scheduled for [time] every weekday. Want me to run it right now so you can see the first one?"

If yes, execute the full scheduled task prompt inline (treat it as a regular task, not a scheduled one).

### Step 5 — Show them where to find it

After the first run, explain:
- **Email**: Check your Gmail Drafts — open the draft and tap Send to yourself, or set up auto-send via a Gmail filter
- **Cowork sidebar**: The "Daily Brief" artifact is pinned — click it any morning for the interactive version with dismiss buttons
- **To dismiss an item**: Tap × in the Cowork view, or tell Claude "dismiss [item]" in conversation

---

## Updating the brief

If the user asks to update, modify, or reconfigure their brief:

1. Call `mcp__scheduled-tasks__list_scheduled_tasks` to find the existing task
2. Read the current prompt from the task's `path`
3. Make the requested changes
4. Call `mcp__scheduled-tasks__update_scheduled_task` with the updated prompt

Common updates:
- "Add a new calendar" → add calendar ID to Step 4 (course deadlines)
- "Dismiss X forever" → add to dismissed-items.json with match_keywords
- "Remove the job search section" → remove Step 3 from the scheduled prompt
- "Change the send time" → update cronExpression
- "Add Todoist" → add Todoist project IDs and insert Step 1 into the prompt

---

## Dismissing items

When the user says "dismiss [item]" or "don't show me [X] anymore":

1. Read the current `dismissed-items.json`
2. Add a new entry:
```json
{
  "id": "kebab-case-id",
  "label": "Human-readable label matching what appears in the brief",
  "match_keywords": ["keyword1", "keyword2"],
  "dismissed_at": "YYYY-MM-DD",
  "reason": "user requested"
}
```
3. Write the file back
4. Confirm: "Done — [item] won't appear in future briefs."

---

## Template reference

See `templates/scheduled-prompt.md` for the full scheduled task prompt with placeholders.
See `templates/dismissed-items.json` for the dismissed items file structure.
