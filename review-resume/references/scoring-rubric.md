# Scoring Rubric

This rubric calibrates the three numerical outputs every evaluation produces. Without calibration, the scores drift and become meaningless across iterations. Use these anchors.

## The three scores

### 1. Substantive match %

Does the candidate's *actual* experience (regardless of how it's presented) match what the role needs?

- **95% (cap)** — Near-perfect fit across all explicit and implicit requirements; the candidate has done this exact job at a comparable company with quantified, named outcomes. Never go above 95% — recruiters distrust 100% matches as either inflated or candidates who'd be bored in the role.
- **85–94%** — Strong fit across nearly all requirements; minor gap in one explicit or implicit area (e.g. has enterprise identity experience but no consumer identity work, applying to a consumer-leaning role).
- **70–84%** — Solid fit, but a clear gap in one major requirement area or a clear domain-shift required (e.g. backend infra PM applying to a consumer product role).
- **55–69%** — Mixed fit. Could be a stretch hire if the candidate's strengths are exceptional and the gaps are learnable, but more likely passed over.
- **40–54%** — Stretch. The candidate's nearest-adjacent experience would have to be reframed compellingly to make this work.
- **<40%** — Wrong job. Tell the user this honestly. Don't waste their time.

Anchor against the years-of-experience requirement: a candidate with 2x the required experience in the right domain is at the top of the band; one with exactly the required experience but breadth is mid-band.

### 2. As-presented match %

Does the resume *as currently written* communicate the substantive fit? This is almost always lower than substantive match — that gap is where the rewrite opportunity lives.

Score this asking: "If a recruiter spent 7 seconds on this resume, would they see the fit?"

- Substantive – As-presented = **0–10 points**: well-tailored resume; small marginal gains possible
- Gap of **10–25 points**: typical for a generic resume submitted to a specific role; rewrite will produce a meaningful lift
- Gap of **25–40 points**: the resume is actively hiding the candidate's qualifications (e.g. enterprise framing for a consumer role, sidebar burying relevant skills, weak top third); rewrite is high-leverage
- Gap of **40+ points**: the resume is materially miscommunicating the candidate's fit; this is the most common case for unsuccessful cold applications by qualified people

When evaluating as-presented, specifically check:
- Does the top third (summary + first 2-3 bullets of most recent role) demonstrate the fit?
- Are the keywords from the JD present in bullet text (not just in sidebar/skills section)?
- Do bullets lead with outcomes that map to JD requirements?
- Is the framing aligned with the role (consumer vs. enterprise, IC vs. management, technical vs. business)?

### 3. Percentile ranking

Where would this applicant rank in the *realistic* applicant pool for this specific role at this specific company?

This requires calibrating to the company tier:

- **Frontier AI labs (OpenAI, Anthropic, DeepMind, xAI), top-tier FAANG IC roles, hot startups (Series C+) for senior roles**: extremely dense applicant pool. The top decile is ~10x stronger than median.
- **Big tech (most FAANG, Microsoft, Salesforce, etc.)**: strong applicant pool but more spread. The top decile is ~3-5x stronger than median.
- **Mid-tier tech, traditional enterprise, public sector**: more variable applicant pool. Top decile less dense.

Use this calibration:

- **Top 5%** — almost certain to advance to phone screen; recruiter will reach out unprompted. Reserve for candidates whose substantive fit is 85%+ AND whose resume clearly communicates it.
- **Top 10–15%** — strong candidate, very likely to advance. Substantive fit 80%+ AND resume reads cleanly.
- **Top 20–30%** — good candidate, likely to advance if the role has standard slate size. Substantive fit 70%+, packaging adequate.
- **Top 35–60th percentile** — middle of the pack. Advancing depends on slate size, referral status, and what else is in the pool. This is the typical fate of qualified-but-untailored cold applications.
- **Below 60th percentile** — unlikely to advance without intervention (referral, reapply with rewrite, etc.).

When the substantive match is high but as-presented is low, the percentile ranking should reflect the *as-presented* reality — because that's what the recruiter sees. But explicitly tell the user where they'd rank if they fixed the packaging: "Top 35–60th percentile today; top 10–15th with the fixes below."

## Calibration examples

These are reference points to anchor scoring:

### Example A — Strong fit, well-packaged
- 8+ years in the exact target domain
- 2+ companies on resume that the hiring manager would recognize as peers
- Quantified outcomes on every bullet
- Top third clearly signals the fit
- Has a referral pathway
- **Substantive: 90%. As-presented: 87%. Percentile: top 5–10%.**

### Example B — Strong fit, poorly packaged (the most common case for qualified-but-rejected)
- 8+ years in the exact target domain
- Strong companies on resume
- Mix of quantified and vague bullets, several placeholder values (XX%)
- Top third is generic
- Cold apply, no referral
- **Substantive: 85%. As-presented: 55%. Percentile: top 35–60th.**

### Example C — Adjacent fit, well-packaged
- 5 years in adjacent domain (e.g. backend infra PM applying to consumer infra)
- Brand-name companies
- Strong outcome bullets
- Top third honestly frames the adjacency as an asset
- **Substantive: 72%. As-presented: 70%. Percentile: top 25–35%.**

### Example D — Strong fit on paper, mismatch on framing
- Domain match by title and company
- But every bullet is framed for a different audience (e.g. enterprise sales when the role is consumer product)
- **Substantive: 80%. As-presented: 50%. Percentile: top 40–55%.**

## What NOT to do

- Don't anchor to "I want to encourage this person." Anchor to "what would the recruiter see in 7 seconds."
- Don't give round numbers when the data supports a tighter range. "Substantive: 85%" not "Substantive: 80–90%."
- Don't move the same resume's scores around without justification across iterations. If you scored a resume at 55% as-presented in iteration 1, only change that number if the resume changed or new information came in.
- Don't inflate the percentile based on the candidate's pedigree alone. A Stanford MBA at Google has lots of company; what differentiates them is the bullets.
