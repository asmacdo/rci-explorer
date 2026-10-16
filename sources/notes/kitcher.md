# Kitcher, "The Division of Cognitive Labor" (1990)

Status: agent-generated 2026-10-16, not yet reviewed. Nobody in this pipeline read the primary text.
The summary was written by an agent with no project context; the relevance section by a second agent that read the repo and that summary.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### Citation

Kitcher, Philip. 1990. "The Division of Cognitive Labor." *The Journal of Philosophy* 87(1): 5-22. DOI: [10.2307/2026796](https://doi.org/10.2307/2026796). The paper was written in English and there is no other edition. A closely related book-length treatment is Kitcher, *The Advancement of Science* (Oxford University Press, 1993), chapter 8. I cite that book from background knowledge and did not check it.

### Summary

Kitcher asks how a scientific community should spread its effort across rival methods, theories or research programs, and whether the individual incentives of scientists can produce that spread. He starts from the observation that if every scientist followed the single method that looks best on the evidence, the community would put all its effort into one line of work. That is probably a poor outcome for the community. He builds simple mathematical models in which each method has a probability of success that depends on how many scientists work on it, and he compares the allocation that is best for the community with the allocation that individuals would choose. He argues that scientists who care about personal credit and recognition, as well as truth, can end up spreading across programs in a way close to the community optimum. Scientists who are purely "sullied" by such motives can therefore serve cognitive goals better than purely truth-seeking ones. He concludes that the traditional picture of the ideal, wholly impartial scientist is not clearly right for communal inquiry, and that the social structure of science is a legitimate target of epistemological analysis.

### Well-known critiques

- Michael Strevens ("The Role of the Priority Rule in Science," *Journal of Philosophy*, 2003) proposed an alternative account. He argued that the priority rule, which gives all the credit to whoever publishes first, explains the division of labor better than Kitcher's credit-seeking motive does. I am recalling this from background knowledge.
- Michael Weisberg and Ryan Muldoon ("Epistemic Landscapes and the Division of Cognitive Labor," *Philosophy of Science*, 2009) argued that the models of Kitcher and Strevens are not robust. Weakening two key idealizations changes the predictions, sometimes to the opposite of the original result. They also argued that the models ignore how scientists use evidence about what others are doing.
- Alexander, Himmelreich and Thompson (*Philosophy of Science*, 2015) criticized Weisberg and Muldoon in turn. This is a critique of a follow-up model, so it should not be read as a critique of Kitcher directly.

### Confidence

**Verified from sources:** the citation details (journal, volume, issue, pages 5-22) and the DOI, from a web search whose results cite them. The sources were a philosophy-of-science mailing list reference list (lists.philo.at), a Cambridge Core reference list, and other citing pages. I did not open the DOI page or JSTOR directly. I also verified that Weisberg and Muldoon (2009, *Philosophy of Science*) criticize the Kitcher and Strevens models and that Alexander, Himmelreich and Thompson (2015) respond to them. The sources for this were Weisberg's [project page](https://web.sas.upenn.edu/weisberg/?p=106) and the [LSE repository entry](https://researchonline.lse.ac.uk/id/eprint/60256).

**From background knowledge, not checked:** the summary, which I wrote from memory of the paper. The Strevens 2003 citation and the claim that Kitcher's 1993 book is a related treatment are also from memory.

**Unsure:** I have not confirmed the exact wording of Kitcher's framing, such as his terms for the types of scientist. I give no page numbers or quotes for that reason.

## Relevance to this project (repo-context agent)

1. **Loop step(s)**: Allocation (primary), plus norms. It is about spreading community effort across rival programs and how individual incentives (credit) produce that spread. It touches no numbered step directly; nearest is the "which pieces get step 5" question in map.md.

2. **What it gives this project**:
- Precedent for treating effort distribution as a community-level optimization with a formal model (success probability as a function of N workers on a method, marginal returns diminishing).
- The contrast "community-optimal allocation vs. what individual incentives yield" gives a template for asking whether load-driven re-checking emerges from incentives or needs engineering.
- Evidence that "sullied" motives (credit, priority) can be functional, relevant to STAMPED adoption: incentives may do more than virtue.
- Legitimizes social structure as an epistemological target, supporting the "rigor is a community property" stance.
- Follow-on literature (Strevens 2003 priority rule, Weisberg and Muldoon 2009 landscapes) supplies robustness warnings and alternatives.

3. **Where it stops**:
- Allocates across rival theories at the frontier, not across verification of existing results. Nothing on re-checking, retirement, or the semi-trusted body.
- No cost side (verification cost, production cost collapse), no dependency or load signal, no trust-update edge (5 to 2).
- Idealized agents with fixed success functions; no auditable objects, no AI actors.
- Weisberg and Muldoon show its results are fragile to idealizations, so it is a source of concepts, not of evidence.

4. **Bearing on repo claims**:
- docs/prior-art.md row "The resource-allocation framing almost exactly. Read first." Overstated. Same word, different problem: Kitcher allocates exploration among rivals; the repo allocates verification across a built-upon body. Complicates rather than supports.
- CLAUDE.md "allocation is distributed, not decided centrally": supported in spirit (individual incentives approximating community optimum), but Kitcher also argues for central-style analysis of the optimum, and shows the match depends on model assumptions.
- CLAUDE.md "Don't pick an objective": Kitcher fixes one objective (community success probability). Complicates.
- map.md "Use as the signal of load": no counterpart in Kitcher; his success functions are exogenous.
- Seed take accuracy: partly wrong, as above.

5. **Suggested one-line take**: Models incentive-driven spread of effort across rival research programs; useful template for allocation, but covers exploration, not verification or retirement of existing results.

6. **Confidence**:
- Rests on summary: thesis, credit-motive result, critiques (Strevens, Weisberg and Muldoon, Alexander et al.). The summary itself is from memory except the citation details.
- Background knowledge: Kitcher's models use diminishing marginal returns; the 1993 book extends them. I believe this but did not check.
- My inference: the exploration vs. verification mismatch. It is strong for the paper as summarized, but I have not read the paper. Whether verification could be recast as a "rival program" (replicate vs. build on) is a guess worth testing.
