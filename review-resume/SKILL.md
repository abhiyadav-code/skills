---
name: review-resume
description: Evaluate a resume against a specific job posting from a senior recruiter's perspective, producing a structured fit assessment with substantive match %, as-presented match %, percentile ranking, callback-killer issues, missing keywords, bullet rewrites, and a concrete action plan. Use this skill whenever the user asks to review, evaluate, score, assess, critique, or compare a resume against a job description, job listing, or specific role at a named company — even if they don't explicitly say "review." Also trigger when the user shares a JD URL alongside a resume, asks "how do I stack up for this role," asks for resume feedback for a specific application, wants to know why they didn't get a callback, asks to improve their match score, or wants to iterate on a resume rewrite and re-score it. Produces structured, comparable evaluations across multiple applications so the user can track which rewrites improve their fit.
---

# Review Resume

A skill for evaluating a resume against a specific job posting from a senior recruiter's perspective, producing a structured, comparable fit assessment with a numerical match score, percentile ranking, and concrete improvement guidance.

## What this skill produces

A single structured evaluation following the template in `references/output-template.md`. The evaluation is comparable across multiple roles (same shape every time) and re-runnable on resume rewrites so the user can see their match score and percentile climb iteration over iteration.

## When to skip this skill

- Generic resume advice not tied to a specific role
- "Write me a resume from scratch" (this is review, not authoring)
- LinkedIn profile reviews (different surface, different rules)

## Workflow

### Step 1 — Gather inputs

The user should provide:

- **Resume** (PDF, doc, or pasted text) — required
- **Job description** — required. Either a URL, pasted text, or a company + role title to search for
- **Hiring manager** — strongly preferred. LinkedIn URL or name; provides invaluable signal about what the role actually optimizes for vs. what the JD says
- **Company context** — optional but useful. Recent news, strategy shifts, layoffs, earnings, product launches. If not provided, search for it
- **Accomplishment stories catalog** — optional. If the user has a SOAR-format catalog of accomplishment stories (see `references/soar-integration.md`), reference it as source material for proposed bullet rewrites
- **Prior evaluation** — optional. If this is a re-evaluation after a rewrite, ask the user for the prior eval's % match and percentile so the comparison is explicit

If any of the required inputs are missing, ask once for them. Don't proceed without the JD and the resume.

### Step 2 — Research the role

Run these in parallel where possible:

1. **Fetch the full JD.** Use web_fetch on the URL. If the URL returns a JS-rendered page (e.g. ashbyhq.com pages often do), try mirror sites (jobs.thrivecap.com, jobright.ai, jobs at the company's careers page) via web_search. Extract: exact responsibilities, qualifications, compensation band (if listed, infers level), team mission, product surface area.
2. **Research the hiring manager.** Search for their LinkedIn profile (LinkedIn is robots-blocked for web_fetch, so use web_search snippets), prior companies, recent talks/posts, public artifacts (papers, conference talks, blog posts). What product domain do they come from? What do they emphasize publicly? This is the single highest-signal input for understanding what the role *actually* needs.
3. **Check company news.** Recent product launches, strategy shifts, public incidents, leadership changes, earnings or funding. This affects what skills are currently most valuable and what framing to avoid.
4. **Identify the implicit requirements.** The JD lists explicit requirements. The hiring manager's background + the team's product surface area imply additional ones. Surface these — they're usually the difference between "qualified" and "callback."

### Step 3 — Assess fit

Evaluate the resume against both explicit and implicit requirements. Use the scoring rubric in `references/scoring-rubric.md` to assign:

- **Substantive match %** — does the candidate's actual experience match the role? (Capped at 95% — never claim a perfect fit; recruiters distrust perfect.)
- **As-presented match %** — does the resume as written communicate that match? (This is usually lower than substantive — the gap is the rewrite opportunity.)
- **Percentile ranking** — where would this applicant rank in the realistic applicant pool for this role? Calibrate to the company tier (FAANG/frontier-lab roles attract a denser top decile than mid-tier companies).

### Step 4 — Identify callback killers

Top 3–7 most likely reasons this resume didn't (or won't) get a callback, ranked by probable impact. Be honest. Cover both substance (gaps in experience) and packaging (formatting, framing, keyword density, level signaling).

Common patterns to check for:
- Placeholder text (XX%, TBD, [number]) — single biggest credibility killer
- Framing mismatch (e.g. enterprise B2B framing for a consumer role)
- Formatting that breaks ATS parsing (multi-column layouts, photos, text in graphics)
- Weak top third (per Rechevskiy traps — see `references/senior-pm-traps.md` for senior PM roles)
- Responsibility-based bullets instead of outcome-based
- Long bullets (>2 lines) that get skipped
- Missing the hiring-manager-implicit keywords
- Level mismatch signals (titles, scope language)
- Cold-apply disadvantage vs. referral pathway

### Step 5 — Produce the structured output

Follow `references/output-template.md` exactly. Every evaluation should have the same shape so the user can compare across roles and track improvement across rewrites.

If the user asks about ATS specifically, load `references/ats-context.md` and include that section. Otherwise skip it — most reviews don't need the ATS primer.

If the role is senior/staff/principal PM or equivalent IC senior level, load `references/senior-pm-traps.md` and apply that lens.

### Step 6 — Tee up next steps

End with concrete, prioritized actions: "this week, do X, Y, Z" — not vague suggestions. Then offer the natural next move (rewrite a specific section, draft a referral message, prep for the screen).

## Tone

This is a senior recruiter at the target company, not a cheerleading career coach. Be direct about gaps. Push back on the user's self-assessment where warranted (especially "I was a strong candidate" claims — strong on substance doesn't mean strong on packaging). Acknowledge strengths, but don't soften weaknesses to be nice. The user is going to make 17 applications — accuracy matters more than encouragement.

When the user provides a "brain dump" of their take on the role, validate what's right and explicitly push back on what's missing or wrong. Don't just agree.

## Iteration mode

When the user returns with a rewritten resume and asks to re-score, do the following:
1. Compare against the prior eval's match % and percentile (ask the user to share these if not in context).
2. Score the new version using the same rubric.
3. Show the delta explicitly: "Substantive match: 85% → 89%. As-presented: 55% → 78%. Percentile: 35–60th → 75–85th."
4. Identify what specifically moved the needle and what's still leaving points on the table.
5. Re-run callback killer analysis — some old issues will be resolved, but new ones may have surfaced.

## References

Reference files in `references/`:

- **`output-template.md`** — the standardized evaluation output structure. Read this every time the skill runs. The user depends on this consistency.
- **`scoring-rubric.md`** — how to calibrate the % match scores and percentile rankings. Read this every time.
- **`senior-pm-traps.md`** — Alex Rechevskiy's framework for the 4 mistakes that cost senior PMs interviews. Read when evaluating senior/staff/principal PM roles or equivalent senior IC roles.
- **`ats-context.md`** — how ATS systems work, what triggers downranking, what parses badly. Read when the user asks about ATS, or when the resume has obvious parseability problems (multi-column, photos, graphics-heavy).
- **`soar-integration.md`** — how to use a SOAR-format accomplishment stories catalog as source material for proposed bullet rewrites. Read when the user has provided or referenced a SOAR catalog.
