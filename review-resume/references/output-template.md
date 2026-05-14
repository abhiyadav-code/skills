# Output Template

Every resume review follows this exact structure. The user is applying to many roles and needs comparable evaluations across them. Do not invent a new shape per role.

## Required sections (in this order)

### 1. One-line verdict

A single sentence with the substantive match %, as-presented match %, and percentile ranking. Example:

> "Substantive match: ~85%. Resume-as-presented match: ~55%. Percentile in realistic applicant pool: 35–60th today, 75–90th with the fixes below."

If this is an iteration, also include the delta from the prior eval:

> "Substantive match: 85% → 89% (+4). As-presented: 55% → 78% (+23). Percentile: 35–60th → 75–85th. The packaging fixes are doing the work."

### 2. Match assessment table

A markdown table with one row per explicit JD requirement plus one or two implicit requirements you've inferred from the hiring manager / company context. Columns:

| Requirement | Fit | Notes |
|---|---|---|

For Fit, use: **Exceeds**, **Strong**, **Strong, under-shown**, **Adequate**, **Weak**, **Weak as written**, **Unclear from resume**, **Gap**. The "under-shown" and "as written" qualifiers are important — they distinguish substance gaps from packaging gaps and tell the user what's fixable with a rewrite vs. what requires a different application strategy.

### 3. Top callback killers

Numbered list, 3–7 items, ordered by probable impact (most damaging first). For each:
- State the issue concretely
- Explain why it matters to *this* recruiter / hiring manager
- Specify the fix

Don't pad. If there are only 3, list 3.

### 4. Missing / under-represented keywords

Pull from the JD and from the hiring manager's public emphasis. Distinguish between:
- Keywords completely missing
- Keywords present but buried (in sidebar/competencies, not in bullets)
- Keywords present but with wrong framing (e.g. "enterprise customer" when the role wants "user")

Tell the user explicitly: "Don't keyword-stuff. Work these in where they're truthful."

### 5. Validating / pushing back on user's brain dump

Only include this section if the user provided their own read on the role. Don't fabricate a brain dump to push back on. When present:
- State 2–3 things they got right
- State 1–3 things they're missing or getting wrong
- Be direct. Agreement-with-the-user is not the goal; accuracy is.

### 6. Strengths to lean into harder

3–5 items. These are real strengths the resume has but isn't surfacing enough. Tell the user *where* in the resume to amplify them (top-third anchor, lead bullet of most recent role, summary line, etc.).

### 7. Concrete bullet rewrites

2–3 before/after examples. Pick bullets from the resume that are highest-impact-if-rewritten. For each:
- Show the original bullet exactly
- Show a rewritten version
- Briefly explain what changed (one line)

Pattern to follow: outcome first, mechanism second, validation last. Lead with the result, then how, then any third-party validation or scale.

If the user has provided a SOAR-format accomplishment stories catalog, source the rewrite content from the Action + Result portions of those stories (see `soar-integration.md`).

### 8. Other unforeseen issues

Things the user might not have anticipated. Examples:
- Title/level signaling mismatches
- Stale certifications that have been "in progress" too long
- Photo / multi-column layouts breaking ATS
- Cold-apply queue position vs. referral pathway
- Compensation band signaling a different level than the user assumes
- Cultural or company-specific signals (e.g. consumer-vs-enterprise framing for an OpenAI consumer team)
- Industry standards / certifications that would help

3–6 items typically.

### 9. This-week action plan

Numbered, concrete, prioritized. Each action should be doable in <2 hours. Lead with the highest-leverage action.

Common items:
1. Fix placeholder values
2. Reformat to ATS-parseable layout
3. Rewrite top third
4. Rewrite N most-recent bullets
5. Reframe at least one bullet to address the implicit requirement (e.g. consumer framing)
6. Get a referral
7. Write a 4-sentence "why this role" note for the application

### 10. Offer of next step

Close with a specific offer: "Want me to draft the rewritten top third?" or "Want me to write the referral DM to [hiring manager]?" — not a generic "let me know how I can help."

## Style rules for the output

- Use markdown headers for the section titles. Sections 2 and 7 benefit from tables and code-style examples; the rest is mostly prose with minimal bullets.
- Don't use emojis.
- Don't soften with hedges like "you might consider" — say "do X" or "rewrite to Y."
- One section per topic — don't repeat the same point across multiple sections.
- Aim for 800–1500 words total. Longer than that, the user won't act on it.

## What to skip when

- Skip ATS context section unless the user asks or the resume has obvious parseability issues.
- Skip "brain dump validation" if the user didn't provide their take.
- Skip senior PM traps unless the role is senior/staff/principal or equivalent IC senior.
- Skip the iteration delta line if this is the first evaluation of this resume against this role.
