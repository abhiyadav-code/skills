# ATS Context

Load this reference when the user asks about ATS, or when the resume has obvious parseability issues (multi-column layouts, photos, text in graphics, decorative timeline elements, etc.).

## What ATS is

ATS = **Applicant Tracking System**. It's the database/workflow layer recruiters use to ingest, parse, store, search, and triage applications. It's not a single product — different companies use different ATS vendors. The major ones in tech:

- **Greenhouse** — common at mid-stage to public tech (Stripe, Airbnb)
- **Ashby** — common at frontier AI labs and modern startups (OpenAI, Anthropic, Ramp, Linear)
- **Lever** — common at mid-stage startups
- **Workday** — common at large enterprises (most Fortune 500), legacy and notoriously poor at parsing creative resumes
- **Taleo / iCIMS** — legacy enterprise ATS, similar parsing issues to Workday
- **Eightfold / Beamery** — AI-augmented ATS used by some large enterprises

**How to identify which ATS a company uses**: Look at the apply URL. `jobs.ashbyhq.com/{company}` = Ashby. `boards.greenhouse.io/{company}` = Greenhouse. `jobs.lever.co/{company}` = Lever. `{company}.wd1.myworkdayjobs.com` = Workday.

## How a resume actually moves through ATS

1. **Parsing.** The PDF is converted into structured fields: name, contact, work history (company, title, dates, bullets), education, skills. This is where most resumes fail first. Multi-column layouts, sidebars, photos, text-in-graphics, decorative timeline dots, and creative templates often parse out of order or drop content entirely.

2. **Keyword and semantic matching.** Modern ATS (Ashby, Greenhouse, Eightfold) use both literal keyword matching and embedding-based semantic similarity to score resumes against the JD. Recruiters can filter by keyword presence.

3. **Recruiter screen.** A human spends 7–10 seconds on a first pass. They scan the top third, recognized company names, and impact numbers. Resumes that look unfinished (placeholder text, formatting glitches from bad parsing) get a quick pass.

4. **Knockout filters.** Many ATS let recruiters filter by location, years of experience, work authorization, and specific keywords. Cold LinkedIn applies often enter at the bottom of the queue.

## What auto-rejects vs. what just downranks

**Hard auto-rejects** (varies by company, but common):
- Doesn't meet years-of-experience minimum (if recruiter has set the filter)
- Wrong location (if role isn't remote)
- Missing work authorization for the country
- Specific knockout questions answered wrong ("Do you have X years of Y?")

**Soft downranks** (the more common issue):
- Resume parses badly (sidebar contents misattributed, sections out of order)
- Low keyword density against the JD
- Generic resume not tailored to role
- Cold apply with no referral signal

Most ATS at modern tech companies (Ashby, Greenhouse, Lever) **don't aggressively auto-reject** on parsing or keyword density alone — but they rank applicants, and ranking determines who gets reviewed by a human. For hot roles at hot companies, recruiters never reach page 5.

## Parseability red flags to call out

When the resume has any of these, mention it explicitly:

- **Multi-column layout with sidebar** — content order frequently scrambled during parsing
- **Photo / headshot** — many U.S. tech recruiters flag this for bias-avoidance; it's also an "unfamiliar with norms" tell
- **Text inside graphics, icons, or images** — invisible to most parsers
- **Decorative timeline elements** (vertical lines with dots) — usually OK but can confuse parsers
- **Headers in the header/footer region of the PDF** — sometimes skipped
- **Tables for layout** (not data tables) — frequently scrambled
- **Non-standard fonts that don't embed cleanly** — can render as gibberish
- **Skills listed only as graphics or progress bars** — not extracted as keywords
- **Tiny font (<10pt) or unusual line spacing** — readability issues

## ATS-safe formatting recommendations

When the user asks for templates or formatting advice:

- **Single column** (or one-column-dominant with thin sidebar for contact only)
- **Standard fonts**: Arial, Calibri, Helvetica, Georgia, Garamond, Times
- **Font size**: 10–12pt body, 12–14pt headers, 16–20pt name
- **Section headers**: clearly labeled (Experience, Education, Skills) — don't get creative with names
- **Dates and titles**: in clear text, not graphics
- **No photo** for U.S. applications
- **No tables for layout** (data tables are fine where they make sense)
- **PDF, not docx**, in most cases — though some ATS prefer docx. When in doubt, PDF.
- **Filename**: `FirstName_LastName_Resume.pdf` — no version numbers, no dates

## How keyword density actually works

Don't keyword-stuff. Modern ATS use semantic matching, so synonyms count. But:

- The exact phrasing from the JD does help. If the JD says "authentication," using "authentication" beats only saying "SSO" or "login."
- Keywords matter more when they appear in bullets (where the recruiter reads) than in a skills/competencies section (which they skim).
- Repetition is fine — natural repetition. Stuffing "authentication, authentication, authentication" gets caught.

## What this means for the evaluation

When ATS is a factor in the evaluation:

- Note the specific ATS the company uses (look up by careers URL)
- Identify the top 3 parseability red flags if present
- Score the as-presented match % with parseability in mind — a resume that parses badly will get downranked even if its content is strong
- In the action plan, prioritize reformatting if parseability is a serious issue

But don't over-focus on ATS. For 80% of resumes, the bigger issue is *content* (placeholder text, weak top third, responsibilities instead of impact, framing mismatch), not ATS parsing. ATS is a real factor but not the primary one. Save the deep ATS discussion for resumes where the issues are genuinely formatting-driven.
