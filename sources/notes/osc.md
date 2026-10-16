# Open Science Collaboration, "Estimating the reproducibility of psychological science" (2015)

Status: agent-generated 2026-10-16, not yet reviewed. Nobody in this pipeline read the primary text.
The summary was written by an agent with no project context; the relevance section by a second agent that read the repo and that summary.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### Citation

Open Science Collaboration [Nosek, B. A., and 269 other co-authors, credited as a group author]. (2015). Estimating the reproducibility of psychological science. *Science*, 349(6251), aac4716. Published 28 August 2015. DOI: 10.1126/science.aac4716 (https://www.science.org/doi/10.1126/science.aac4716).

Follow-on projects cited in the entry:
- Klein, R. A., et al. (2014). Investigating variation in replicability: A "Many Labs" replication project. *Social Psychology*, 45(3), 142-152.
- Camerer, C. F., et al. (2018). Evaluating the replicability of social science experiments in Nature and Science between 2010 and 2015. *Nature Human Behaviour*, 2, 637-644. DOI: 10.1038/s41562-018-0399-z. (Volume and pages are from background knowledge; the DOI is in a FLoRA URL I saw.)
- Errington, T. M., et al. (2021). Investigating the replicability of preclinical cancer biology. *eLife*, 10, e71601. DOI: 10.7554/eLife.71601 (DOI from background knowledge).

### Summary

The Open Science Collaboration, a large volunteer team coordinated by Brian Nosek and the Center for Open Science, tried to replicate 100 experimental and correlational studies published in 2008 in three psychology journals.
Replication teams used the original materials where possible and generally ran larger samples.
Each replication protocol was reviewed and registered before data collection.
The project asked how often the original results could be reproduced and how replication success relates to features of the original study.
Almost all of the original studies (97%) reported statistically significant results, while only about 36% of the replications did.
Replication effect sizes averaged about half the originals.
About 47% of original effect sizes fell within the 95% confidence interval of the replication, and 39% of replications were subjectively rated by the teams as having replicated.
Combining original and replication data, 68% of effects were significant, assuming the originals were unbiased.
Success was better predicted by the strength of the original evidence (for example, smaller p-values and larger effects) than by the characteristics of the original or replication teams.
The authors say no single indicator settles reproducibility, and that a failed replication does not by itself show the original was false.

Follow-on large replication projects: Many Labs 1 (Klein et al., 2014) tested 13 effects across 36 samples and found 10 replicated consistently.
Camerer et al. (2016) replicated 18 economics experiments, and Camerer et al. (2018) replicated 21 social science experiments from Nature and Science (2010-2015), with about 62% replicating in the original direction at about five times the original sample sizes.
The Reproducibility Project: Cancer Biology (Errington et al., 2021) repeated 50 experiments from 23 papers, with replication effects a median of about 85% smaller than the originals for positive effects.
Further Many Labs rounds (2 in 2018, 3 in 2016) also followed.

### Well-known critiques

- Gilbert, King, Pettigrew and Wilson (2016, *Science* comment) argued the 36% figure is misleading because of sampling error, power, and differences between original and replication protocols ("infidelity").
  They said that once these are accounted for, the data are consistent with a high true reproducibility rate.
  The OSC authors replied (Anderson et al., 2016) that this reading was not supported by the data.
- Related to the above, critics noted that "significant versus not significant" is a weak criterion for replication, since a difference between significant and non-significant is not itself significant.
  Other critics noted the sample came from only three journals and one year, so generalizing to "psychology" is limited.
- Hidden moderators and context sensitivity: some original authors and commentators argued that differences in populations, setting or timing, rather than false originals, could explain some failures.

### Confidence

Verified through web search results (not the primary page, since the Science site returned 403 to fetch):
- OSC (2015): volume, issue, article number, date, DOI, 100 studies, 97% vs 36%, 47% CI coverage, 39% subjective, 68% combined, effect-size halving, predictor finding. Sources: search result mirrors such as https://pureportal.coventry.ac.uk/en/publications/estimating-the-reproducibility-of-psychological-science-2/ and https://dare.uva.nl/id/2ef85c77-615c-4684-a434-34feb81db3dc.
- Camerer 2018: 21 studies, 2010-2015, about 5x sample size, about 62% (13 studies), effect sizes about half. Source: https://authors.library.caltech.edu/91063/.
- Errington 2021: 50 experiments from 23 papers, 158 effects, 85% median smaller, 46% combined success (positive and null effects together; do not conflate with the 85% figure). Sources: https://elifesciences.org/articles/71601.pdf and https://pmc.ncbi.nlm.nih.gov/articles/PMC8651289.
- Klein 2014: Social Psychology 45(3) 142-152, 13 effects, 36 samples, 6,344 participants, 10 replicated. Source: https://pure.psu.edu/en/publications/investigating-variation-in-replicability-a-many-labs-replication-/.

From background knowledge only (not checked this session):
- The "270 authors" count was given by a search summary, but the "Nosek and 269 others" phrasing is mine.
- The "2008, three journals" detail (JPSP, Psychological Science, JEP:LMC); one search summary explicitly declined to confirm 2008, so treat as probable.
- The Camerer 2018 volume and pages, the eLife DOI, and the Camerer 2016 economics project (18 studies, *Science*) and the Many Labs 2 and 3 dates.
- All three critique bullets, including the Gilbert et al. and Anderson et al. exchange, were not checked this session. I am confident of the exchange itself but not of exact wording; I have given no quotes or page numbers.

## Relevance to this project (repo-context agent)

1. **Loop step(s)**: Step 5 (evaluate), with step 6 and the dashed 5 → 2 edge: OSC is a bulk, post-hoc re-evaluation of objects already in the body. Secondarily "trust", as calibration data for step 2's venue/clout heuristics.

2. **What it gives this project**:
- Measured, non-anecdotal evidence that step 6 "joins" are not final: 97% of originals significant vs ~36% of replications; effect sizes about half.
- A worked case of "6 is a state, not a gate": objects selected and re-evaluated, sampled by cohort rather than by load.
- Predictors of failure available before replication (original p-value, effect size) are a cheap static signal. This parallels the "static grader vs executed re-run" calibration idea in stamped.md.
- Camerer 2018 and Errington 2021 add a design: preregistered replication protocols, plus a gap between prediction and result.
- Cost data for an allocation queue: hundreds of authors, years of work, for 100 studies. Gives a real "cost to retire" number to put against "production near-free."

3. **Where it stops**:
- Sampling was by journal/year cohort, not by dependency load. It says nothing about which objects the community should check.
- No propagation measured: did the 5 → 2 edge fire, did dependents change? Nothing on the "use as signal of load" gap.
- Verdict criterion is contested (significance, CI coverage, subjective rating all disagree: 36%/47%/39%). So "replicated" is not a clean verifier.
- Re-collection of data, not re-execution of a research object; little on STAMPED-style artifact auditability.
- Nothing on AI.

4. **Bearing on repo claims**:
- prior-art.md row: "Measured replication rates; our real-cases source, already traced." Partly inaccurate. It is measured evidence, not a traced case (cases.md TODO still lists "A replication attempt (did 5 → 2 propagate?)" as untraced), and "Read?" is unchecked. Not a case source for the loop.
- map.md "Peer review of the narrative, not the object" and "Trust frozen at that moment": supported.
- map.md "no verifier exists" analogy (ai-in-the-loop.md): complicated; replication is the verifier, contested and expensive.
- Gilbert et al. critique complicates any use of 36% as "the loop's failure rate": hidden moderators, power, protocol fidelity.
- stamped.md "necessary, not sufficient": OSC's fidelity disputes support transparency, but replication here needed materials sharing, not machine auditability.

5. **Suggested one-line take**: Measured step-5/6 failure, contested by critics; shows re-evaluation is costly and cohort-sampled, not load-driven; no propagation data.

6. **Confidence**:
- Rests on summary: headline figures (97/36/47/39/68%), follow-on counts, critique existence.
- Rests on my background knowledge: OSC was cohort-sampled and did not track downstream citation effects; the Gilbert/Anderson exchange; replication verdict ambiguity.
- Own inference (guess): that OSC's per-study cost can seed a retirement-cost estimate; that its predictors are usable as a static grader analogue. Neither is supported by the source directly.
