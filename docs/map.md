# The loop (as-is)

A loop of contribution to "the body." Vague enough to be true at this level; each step
needs concretization below it. Actor and cost annotations are the point — that's the
allocation problem on one page.

| # | Step | As-is today (hypothesis, needs cases) | Actor | Cost |
|---|------|----------------------------------------|-------|------|
| 1 | Search existing | Keyword + citation chasing + who-you-know. Recall-limited; long tail invisible. | Human (AI entering) | Low, lossy |
| 2 | Evaluate trustworthiness of sources | Intuition, venue, author clout. Rarely updated after the fact. Almost never per-claim. | Human | Cheap, opaque |
| 3 | Create and iterate on a plan (perhaps preregistration) | In the researcher's head. Prereg is a minority practice, often decoupled from what's executed. | Human | Variable |
| 4 | Execute the plan, produce a research object | Scripts on laptop/cluster. Provenance partial, environment unrecorded. | Human (AI entering fast) | High |
| 5 | Research object gets evaluated | Peer review of the narrative, not the object. Reviewers read; they can't re-run. | Human | High, scarce |
| 6 | Research object joins the body | Binary gate via publication. Trust frozen at that moment. | Institutional | — |

## "Trust score"

Abstract, many implementations: impact factor, citations, author clout, strength of
evidence, transparency of the object, replication, intuition. We don't solve it. The map
only requires that a researcher assigns one, calculated or intuited.

One interface requirement if the loop is to learn: it has to accept updates. Intuition
updates slowly (reputation), mostly for famous results. Computed scores update explicitly
but are gameable (impact factor). That's a tuning, not a flaw. Intuited trust is
individual rigor; mark it as the unauditable implementation.

## Edges that exist in principle and barely in practice (draw dashed)

- **5 → 2: evaluation updates trust.** A failed evaluation should lower trust in the
  object's sources and in whoever last evaluated them. Without it, trust is a static label.
- **6 is a state, not a gate.** Objects should stay subject to step 5 forever
  (replication, downstream failure, retraction). The body cannot be evaluated; only
  pieces. *Which* pieces is the allocation problem: driven by load, suspicion, cheapness,
  randomness — each a tuning.
- **Use as the signal of load.** Your step 1 is someone else's step 6. Each
  search-and-build-on event is a dependency edge; the count is what makes an object
  load-bearing. Citations measure attention, not reliance. This quantity is what any
  allocation queue needs and the loop doesn't currently record it.

## Open

- These rows are my model, not observations. Trace real cases (see `cases.md`).
- Which steps are human-bound vs. already automatable, and where a cost drop changes the
  optimum. Hypothesis: 2 and 5 are where AI changes the numbers most — the argument against
  starting at 4.
