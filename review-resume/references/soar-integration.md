# SOAR Integration

Load this reference when the user has provided or referenced a SOAR-format accomplishment stories catalog. The catalog will typically be a document or set of documents with stories structured as Situation / Obstacle / Action / Result.

This skill uses the catalog as the source material for the **bullet rewrites** section of the evaluation output, and for any other section where a specific accomplishment would strengthen the resume.

## What SOAR is

The SOAR framework structures career accomplishments into four parts:

- **S — Situation**: What was the context, scope, or objective?
- **O — Obstacle**: What problem, constraint, or challenge had to be overcome?
- **A — Action**: What did the person specifically do? (Their action, not the team's.)
- **R — Result**: What was the outcome? Quantified where possible.

In a resume, only the **Action + Result** portion typically appears in a bullet. The S and O are kept in reserve for behavioral interviews. This is the right split: bullets should be tight, but the underlying stories should be rich enough to expand on demand.

## How to use the catalog in a review

### 1. Identify which JD requirements need bullet support

In the match assessment table, mark requirements as "Strong, under-shown" or "Unclear from resume" or "Weak as written." These are the requirements where a bullet from the catalog could change the assessment.

### 2. Find the best-matching stories in the catalog

For each under-shown requirement, search the catalog for stories whose Action + Result map to that requirement. Prefer stories that:

- Use language that maps to the JD's exact phrasing
- Have quantified results (numbers, percentages, dollars, users, time)
- Are from recent roles (more credible than ancient examples)
- Demonstrate the *implicit* requirement, not just the explicit one (e.g. for an OpenAI consumer-leaning role, prefer stories that show consumer-scale or user-facing work even if they're from a B2B role)

### 3. Transform Action + Result into a resume bullet

A SOAR story typically has more material than fits in a bullet. The transformation:

- **Lead with the Result** — outcome first, mechanism second
- **Compress the Action** — one verb phrase, not three
- **Include scale or validation** if it strengthens the claim and fits in 1–2 lines
- **Cut everything else** — situation and obstacle live in the behavioral interview, not the bullet

**Example transformation**:

SOAR story (full):
- S: At Google Cloud in 2019, the IAM team faced a strategic challenge: enterprise customers struggled with "least privilege" at scale. The recommendation product space was greenfield.
- O: No existing ML-based solution; petabyte-scale access logs to analyze; safety-critical (bad recommendations could break customer workloads).
- A: Led 0-to-1 launch of Policy Intelligence platform. Owned product vision for applying ML to access logs. Defined the safety thresholds for automated recommendations. Coordinated with eng, UX, and security teams over 14 months.
- R: 3,500 enterprise customers adopted in year one. 110M+ over-provisioned permissions safely removed. Cited by Forrester as "top-10 strength" and "breathtaking innovation." Zero documented incidents of recommendation-caused workload breakage.

Resume bullet (Action + Result, compressed):
- "Drove 0→3,500 enterprise adoption of Policy Intelligence in 12 months; safely removed 110M+ over-provisioned permissions with zero workload-breaking incidents. Cited by Forrester as 'breathtaking innovation.'"

### 4. Surface specific catalog stories in the rewrite section

In the "Concrete bullet rewrites" section of the evaluation output, when proposing a rewritten bullet, cite the source story by ID or title if the catalog has identifiers. Example:

> **Before**: "Owned product vision for applying ML to analyze petabyte-scale access logs..."
> 
> **After (from SOAR story #14 — "Policy Intelligence launch")**: "Drove 0→3,500 enterprise adoption of Policy Intelligence in 12 months..."

This helps the user trace which catalog stories they're drawing from and identify gaps in the catalog (requirements with no matching story).

### 5. Flag catalog gaps

If an under-shown requirement has *no* matching story in the catalog, flag it explicitly:

> "Requirement: 'consumer identity at scale.' No matching SOAR story in the catalog. Either the candidate has this experience and the catalog is incomplete (write a new story), or the candidate lacks this experience and needs a different bridging strategy."

This turns the resume review into a feedback loop that improves the catalog over time.

## What if the catalog doesn't exist yet?

If the user mentions they're working on a SOAR catalog but it isn't ready, or if no catalog is provided:

- Proceed with the evaluation normally
- In the bullet rewrites section, *invent* a SOAR-shaped story from the existing resume bullet (i.e. reverse-engineer the likely SOAR structure) and use that as the basis for the rewrite
- Note explicitly: "Proposed rewrite assumes [these specific details]. If accurate, use as-is. If not, adjust."
- At the end of the evaluation, suggest the user develop a SOAR catalog to make future rewrites faster and more accurate

## Quality bar for catalog stories

When the user is building or extending their catalog, the strongest stories share these traits:

- **Quantified result**: a number, percentage, dollar amount, user count, or time metric
- **Specific scope**: named product, team size, customer count, geographic scale
- **Single owner**: the action is unambiguously what *the candidate* did, not "the team" or "we"
- **Third-party validation if available**: customer quotes, Gartner/Forrester citations, internal awards
- **Recent or evergreen**: ideally <5 years old, or older if it's a defining career moment

Stories that lack quantification can still be useful for behavioral interviews but produce weaker resume bullets. Prioritize quantified stories for resume use.
