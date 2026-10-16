# Ioannidis, "Why Most Published Research Findings Are False" (2005)

Status: agent-generated 2026-10-16, not yet reviewed. Nobody in this pipeline read the primary text.
The summary was written by an agent with no project context; the relevance section by a second agent that read the repo and that summary.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### Citation

Ioannidis, John P. A. (2005). "Why Most Published Research Findings Are False." *PLoS Medicine* 2(8): e124. Published 30 August 2005. English original. DOI: https://doi.org/10.1371/journal.pmed.0020124 (open access at https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124).

A correction was later issued: Ioannidis JPA (2022), *PLoS Medicine* 19(8): e1004085.

### Summary

Ioannidis argues that a published claim is more likely false than true in many research settings. The argument is a Bayesian calculation of the positive predictive value (PPV) of a "significant" finding. PPV depends on the pre-study odds that a tested relationship is real (the ratio of true to null relationships in a field), the statistical power of studies, the significance threshold, and a bias term for the share of analyses that become "positive" through flexible design, analysis or selective reporting. The essay also adds the effect of multiple independent teams testing the same question. From the model he draws six corollaries. Findings are less likely to be true when:

- studies are small;
- effect sizes are small;
- many relationships are tested with little preselection;
- designs, definitions and analyses are flexible;
- financial or other interests and prejudice are stronger;
- more teams chase the same question.

He concludes that, in many fields, reported findings may largely reflect prevailing bias. He closes with implications for how research is conducted and interpreted, including the value of larger studies, better preselection of hypotheses, and replication.

### Well-known critiques

- Steven N. Goodman and Sander Greenland (2007), "Why Most Published Research Findings Are False: Problems in the Analysis," *PLoS Med* 4(4): e168. They say the model is partly circular and that it treats a result only as "significant or not" rather than using the actual P-value or data. They argue it therefore understates the evidence a study can give, and cannot count as a proof that most claims are false. Ioannidis replied in 2007 that the methods and results are practically identical and that he never claimed no study can be convincing.
- Jager and Leek (2014), "An estimate of the science-wise false discovery rate and application to the top medical literature," *Biostatistics*. They estimated the false discovery rate in top medical journals at about 14%, far below "most". This is from my background knowledge only.
- Related general point: the model's inputs (pre-study odds, bias) are assumed, not measured, so the headline conclusion depends on those assumptions. This is my summary of a common objection, not tied to one named critic.

### Confidence

Verified from sources:
- The citation details (DOI, volume, issue, date, 2022 correction) and the six corollaries, from the PLoS Medicine article page: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124
- The Goodman and Greenland critique and Ioannidis's reply, including the citation e168 and the circularity and "not a proof" points, from search results. These included the PMC copy (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1855693/) and the PLoS DOI https://doi.org/10.1371/journal.pmed.0040168. I did not read the full critique text myself.

From background knowledge, not checked in this session:
- The description of the PPV model's parameters (pre-study odds R, power, alpha, bias u).
- The Jager and Leek 14% figure and its citation details.

Unsure:
- The exact wording of the Ioannidis reply and its precise citation.
- The exact form of the 2022 correction (I did not check what it changed).

I give no page numbers or quotations.

## Relevance to this project (repo-context agent)

1. **Loop step(s)**: Steps 5 and 6 (evaluation, joining the body), plus step 3 (flexible design/analysis is a bias input) and "trust" (it gives a prior for how much to trust a published claim). Mainly it is a model of the filter at 5 to 6 failing.

2. **What it gives this project**:
- A quantitative frame: PPV = f(pre-study odds, power, alpha, bias, number of teams). That turns "trust score" (map.md) into a computable prior per field/claim type.
- Six corollaries are testable axes for allocation: where to spend verification (small effects, flexible analyses, hot fields, conflicted interests).
- Bias term u maps onto step 3/4 flexibility. STAMPED/prereg-style capture plausibly shrinks u, a concrete mechanism for "necessary, not sufficient."
- Multi-team corollary: more chasers raise false positives, and publication selects positives. This is a mechanism for why a binary gate at 6 degrades the body.

3. **Where it stops**:
- Treats a claim as significant/not at one moment; no dynamics, so nothing on the 5 -> 2 update edge, retraction, or downstream propagation.
- No dependency or load concept. It cannot say which claims to re-check.
- Says nothing on verification cost, auditability, or who verifies; "replication" is an exhortation.
- Silent on AI and on production-cost collapse (though it predicts more tests with low pre-study odds yield more false positives).
- Inputs are assumed, not measured.

4. **Bearing on repo claims**:
- prior-art.md: "Empirical failure of the as-is loop." Inaccurate. It is a theoretical model with assumed inputs, not an empirical measurement; per the summary, Goodman and Greenland call it partly circular, and Jager and Leek (~14%, background) contradict "most." Empirical failure belongs to the Open Science Collaboration row.
- map.md: "Binary gate via publication. Trust frozen at that moment." Supported in spirit (selection on significance), though not argued by the source.
- cases.md: "By the community-rigor standard much pre-AI literature is also slop." Complicated: Ioannidis supports it only with his assumptions; the "most" magnitude is contested.
- map.md "Edges that exist in principle": the source is silent on them.

5. **Suggested one-line take**: Theoretical PPV model (assumed inputs, contested) showing selective significance filters at 5-6 can yield mostly false claims; supplies priors, not measurement or dynamics.

6. **Confidence**:
- From the summary: citation, six corollaries, Goodman/Greenland critique, no-measurement caveat.
- From my background knowledge: PPV parameters; it is the field's canonical exemplar; Jager and Leek's ~14% (the summary also marks this as background); the 2022 correction detail is unchecked.
- My inference: the mappings to u and step 3, and the "no dynamics, no load" gaps. I have not read the paper itself. Guess: its corollaries are likely usable as allocation heuristics, but that is untested.
