# Annotated bibliography: highly relevant

Status: agent pass, 2026-10-16, awaiting review.
No human has read any of these sources.
Peripheral sources are in [STRETCH_ANNOTATED_BIB.md](STRETCH_ANNOTATED_BIB.md).

**How these were made.**
Per source, one agent with no project context wrote the citation and summary; for the four 2026 papers and the Hardt book it read the full text, for the classics it relied mostly on background knowledge plus catalog checks.
A second agent read the repo plus that summary and wrote relevance (loop step, what it gives, where it stops, bearing on repo claims, tier).
Full outputs: `notes/<source>.md`.
Tiers for the eleven classic sources are the orchestrator's call from the relevance reports; tiers for the new sources are the relevance agent's, except where marked.
The cross-cutting section is orchestrator synthesis over agent outputs: inference over inference, not findings.

**Originals** are listed in [originals/MANIFEST.md](originals/MANIFEST.md); only openly licensed ones are committed.

## Entries

Each entry: loop step, one-line take, and the point that earned it a place here.
Read? stays ☐ until a human has read it.

### Hardt, *The Emerging Science of Machine Learning Benchmarks* (Princeton UP, 2026) ☐
[notes](notes/hardt.md) · https://mlbenchmarks.org · Steps 5, 2, 5 → 2, 6, trust, norms.
**Take:** Closest working model of a community verification loop; shows rankings survive Goodhart where absolute numbers fail, but only with shared data and cheap re-runs.
**Why here:** Builds on Strevens's iron rule as a mechanism, not just a norm.
Three replication bars (re-execution, similar conditions, different conditions).
Quantified adaptive-reuse failure (Ch 4-5) and why ImageNet survived it anyway (Ch 8, explanations labeled "emerging").
Aggregation into one score is a voting problem with Arrow-type limits (Ch 12).
LLM judges: debiasing gains at most ~2x effective sample size at the frontier; rankings can reverse when candidates beat the judge (Ch 14).

### Chen et al., Brain Researcher (arXiv:2608.19902, 2026) ☐
[notes](notes/brainresearcher.md) · Steps 4, 5, 3, trust.
**Take:** A working in-analysis critic with an audit bundle; shows both the promise and the leaky verifier, but not cross-body allocation.
**Why here:** Sealed commitment card (machine-enforced preregistration), six claim states (accepted, qualified, revised, blocked, rejected, deferred), audit bundle reopenable without re-execution.
Measured verifier weakness: automated review missed a sign-blind scoring error a human caught; verified grounding 22.0% (CI 16.8-27.2); LLM judges overlap with evaluated models.

### Open Science Collaboration, "Estimating the reproducibility of psychological science" (*Science*, 2015) and follow-ons ☐
[notes](notes/osc.md) · Steps 5, 6, 5 → 2, trust.
**Take:** Measured step-5/6 failure, contested by critics; shows re-evaluation is costly and cohort-sampled, not load-driven; no propagation data.
**Why here:** The empirical anchor for "6 is a state"; Hardt Ch 6 cites it and Ch 7 is its ML analogue.

### Kitcher, "The Division of Cognitive Labor" (*J. Phil.*, 1990) ☐
[notes](notes/kitcher.md) · Allocation, norms.
**Take:** Models incentive-driven spread of effort across rival research programmes; a template for allocation, but covers exploration, not verification of existing results.
**Why here:** Nearest prior formal treatment of allocation; its mismatch with the project's problem is itself informative.

### Longino, *Science as Social Knowledge* (1990) ☐
[notes](notes/longino.md) · Step 5, norms, trust.
**Take:** Objectivity as a community property under four conditions (venues, uptake, shared standards, tempered equality of authority); qualitative, silent on cost and allocation.
**Why here:** "Uptake" names the 5 → 2 edge; the strongest philosophical basis for "rigor is a community property", and a challenge to "auditability is constitutive".

### Ioannidis, "Why Most Published Research Findings Are False" (*PLoS Med*, 2005) ☐
[notes](notes/ioannidis.md) · Steps 5, 6, 3, trust.
**Take:** Theoretical PPV model (assumed inputs, contested) showing selective significance filters can yield mostly false claims; supplies priors, not measurement or dynamics.
**Why here:** A computable prior for a trust score, and six corollaries usable as allocation heuristics (untested as such).

### Strevens, *The Knowledge Machine* (2020) ☐
[notes](notes/strevens.md) · Norms, steps 5, 6.
**Take:** The iron rule restricts public argument to empirical evidence while private motives stay free; a norms account, silent on verification cost and allocation.
**Why here:** Promoted from the seed list because Hardt builds his whole account on it.
Two agents flagged Strevens 2003 ("The Role of the Priority Rule in Science") as likely more relevant to allocation; not yet assessed.

### Choudhury et al., Mycelium / "Networked Intelligence: Active Shared Context Graphs" (arXiv:2607.13220, 2026) ☐
[notes](notes/mycelium.md) · Steps 4, 1; trust as stated future work.
**Tier: contested.** The relevance agent said STRETCH (its one evaluation scores breadth of generated artifacts, not verification), noting a HIGH case exists. Placed here by the orchestrator because you flagged it and because it is the only source with a working substrate for the "use as load" edge. Your call.
**Take:** Provenance-graph substrate demo with typed lineage and supports/contradicts edges; attributes every claim to its source but explicitly applies equal epistemic weight and leaves contradiction resolution undone.
**Evidence caveat:** one case study, three researchers, one week, n=1 per condition, author-built unblinded rubric, mismatched conditions.

### OHBM OSSIG Reproducibility Challenge (2026 edition) ☐
[notes](notes/tools.md#ohbm-open-science-sig-ossig-reproducibility-challenge) · Step 5, possibly 5 → 2, norms.
**Take:** A live community mechanism that re-executes published work; the best candidate here for a traced case in `docs/cases.md`.
**Open question:** does any challenge result ever update trust in the source?

### Kent et al., Neurosynth Compose (*Imaging Neuroscience*, 2026) ☐
[notes](notes/tools.md#neurosynth-compose) · Steps 1, 4, 5.
**Take:** Meta-analyses stored as re-runnable specifications (NiMADS + NiMARE); a verifier-adjacent artifact, and a possible partial record of study reuse.
**Open question:** are study reuse counts exposed?

## Cross-cutting (orchestrator synthesis, unverified)

Patterns across all 23 relevance reports (11 classics, 12 new).
Each is only as strong as the agent outputs under it.

1. **Still no source covers verification allocation across the existing body.**
   Every relevance agent reported this gap again.
   Brain Researcher covers verification inside one analysis; Hardt shows benchmarks act as a *standing default* allocation (everyone evaluates the same set), which complicates `CLAUDE.md` "allocation is distributed, not decided centrally".
   Kitcher remains the nearest formal model and is about exploration.
2. **Rankings, not scalars, may be the right shape for a trust score.**
   Hardt: absolute numbers do not replicate under competition; rankings mostly do.
   Hardt Ch 12: collapsing many signals into one number is a voting problem with impossibility results.
   This bears directly on the "trust score" in `docs/map.md`, which is currently scalar-shaped.
3. **A verifier invites optimization against it.**
   ARC-AGI-3 argues its own earlier versions were attackable *because* they were verifiable; Hardt Ch 5 gives the quantified attack; lee3j is the in-repo exhibit.
   This is in tension with `docs/ai-in-the-loop.md` "find the loop with a verifier and iterate there", and the repo does not yet name it.
4. **AI critics at step 5: cost near zero, quality bounded and measured.**
   Hardt Ch 14: judge debiasing caps near 2x; rankings reverse when candidates exceed the judge.
   Brain Researcher: automated review missed an error a human caught; grounding 22%.
   This turns the `ai-in-the-loop.md` row "evaluation cost → ~0, quality unknown" into "quality bounded, with numbers".
5. **The 5 → 2 edge still lacks an attribution rule.**
   Popper and Lakatos (Duhem-Quine) say blame is underdetermined.
   Mycelium attributes claims to sources but weights them equally; WikiSkill's credit assignment works only because each change is single and isolated; Brain Researcher does not propagate across claims.
6. **Substrate for "use as load" exists inside projects, not across the body.**
   Mycelium's lineage graph and Neurosynth Compose's study aggregation could record dependency; neither counts reliance across papers.
7. **"Auditability is constitutive" still has no support.**
   Hardt's rankings rest on a shared protocol, not on inspecting artifacts; Longino requires criticizability plus uptake; Brain Researcher treats audit as a design goal.
   It remains the project's own position.
8. **"Replication" needs the vocabulary split.**
   Hardt's three bars, OSC's independent re-runs, and Meisler's "replicable" (cross-vendor consistency within one cohort) are three different claims under one word.
9. **Candidate cases for `docs/cases.md`:**
   OSSIG challenge (does 5 → 2 fire?); Brain Researcher's NeuroMark sign-blind error (critic failure caught by a human); Meisler (well-provenanced step-4 object).

## Candidates to add (unverified)

Named by agents from background knowledge; citations not checked.

- Strevens, "The Role of the Priority Rule in Science" (*J. Phil.*, 2003).
- Weisberg & Muldoon, "Epistemic Landscapes and the Division of Cognitive Labor" (*Phil. Sci.*, 2009).
- Solomon, *Social Empiricism* (2001).
- Recht et al. ImageNet/CIFAR-10 test-set reconstructions (cited in Hardt Ch 7).
- Blum & Hardt, the Ladder mechanism (cited in Hardt Ch 5, 8).
- Dorner, Nastl & Hardt (ICLR 2025) on LLM-judge limits (cited in Hardt Ch 14).
- Feather et al., arXiv:2406.01538, on over-reliance on brain scores.
- Gilbert et al. (2016) / Anderson et al. (2016): the OSC exchange.
- Goodman & Greenland (2007); Jager & Leek (2014): critiques of Ioannidis.

## To add (from seed)

- Metascience on AI in the loop (LLM-written reviews, hallucinated citations, paper-mill volume); see `docs/ai-in-the-loop.md`
- Reproducibility infrastructure: Software Heritage, DataLad, Nix/Guix reproducible builds, Research Objects (RO-Crate)
- Technical-debt literature as analogy for "verification debt"
