# Annotated bibliography: stretch

Status: agent pass, 2026-10-16, awaiting review.
Adjacent, background, analogy or tooling sources.
Method and caveats as in [ANNOTATED_BIB.md](ANNOTATED_BIB.md); full outputs in `notes/<source>.md`.
Read? stays ☐ until a human has read it.

## Classics (orchestrator tier calls)

### Popper, *Logic of Scientific Discovery* (1934/1959), *Conjectures and Refutations* (1963) ☐
[notes](notes/popper.md) · Step 5, norms.
**Take:** Corroboration-by-severe-test frames what step 5 should measure; silent on cost, allocation, objects-not-theories, and blame assignment for 5 → 2.
**Kept for:** Severity as a possible allocation axis; via Duhem-Quine, the source of the attribution problem.

### Lakatos, "Falsification and the Methodology of Scientific Research Programmes" (1970) ☐
[notes](notes/lakatos.md) · Step 5, trust.
**Take:** Appraisal belongs to programmes, not isolated claims; progressive vs degenerating is a retrospective trust-update signal, with no costs, actors or timescale.
**Kept for:** The other half of the attribution problem; "hard core" is not the same as dependency load.

### Merton, "The Normative Structure of Science" (1942) ☐
[notes](notes/merton.md) · Norms, trust.
**Take:** Four-norm ethos (universalism, communism, disinterestedness, organized skepticism) as ideal; contested as practice.
**Kept for:** Vocabulary for the norms layer; universalism names what step 2's "author clout" violates.

### Polanyi, "The Republic of Science" (1962) ☐
[notes](notes/polanyi.md) · Norms, allocation.
**Take:** Defends decentralized, peer-authority coordination; supports "distributed allocation" as description, but trust rests on tacit tradition, not auditability.

### Kuhn, *The Structure of Scientific Revolutions* (1962/1970) ☐
[notes](notes/kuhn.md) · Trust, norms.
**Take:** Community-level account of shared standards and wholesale shifts of trust; descriptive and macro, no per-object or cost mechanism.

### Latour & Woolgar, *Laboratory Life* (1979/1986) ☐
[notes](notes/latour.md) · Steps 6, 2, norms.
**Take:** Ethnography of one lab: claims shed hedges and provenance as they travel, and credit drives work. Describes trust freezing, not how to reverse it.
**Kept for:** Suggests "trust frozen at step 6" may be gradual and post-publication.

## RSI and AI-progress framings

### Narayanan & Kapoor, "AI as Normal Technology" (Knight First Amendment Institute, 2025) ☐
[notes](notes/nk.md) · The loop as a whole, norms. Thesis: BOTH, weakly.
**Take:** Impact is gated by an innovation-diffusion loop of people, firms and institutions "even if progress in AI methods can be arbitrarily sped up"; leaves RSI open and treats institutional slowness as protective, where the repo treats loop friction as something to optimize.

### Weston & Foerster, "AI & Human Co-Improvement for Safer Co-Superintelligence" (arXiv:2512.05356, 2025) ☐
[notes](notes/wf.md) · Steps 3-5. Thesis: BOTH, weakly.
**Take:** Position paper for human-AI co-improvement over autonomous RSI, scoped to AI research labs; concedes a self-improving endpoint and has nothing on communities, verification or allocation.

## Benchmarks and evaluation

### ARC Prize Foundation, ARC-AGI-3 (technical report, 2026) ☐
[notes](notes/arcagi3.md) · Trust, allocation (analogy only).
**Take:** A deliberately Goodhart-resistant benchmark on toy tasks: held-out out-of-distribution private set, squared efficiency scoring, no task-specific harnesses.
**Kept for:** Argues verifiable task families invite attack; a hand-built harness moved one score from 0.0% to 97.1%.

### Brain-Score (Schrimpf et al. 2018, 2020) ☐
[notes](notes/brainscore.md) · Step 5, norms.
**Take:** A live, re-scoring, community benchmark of models against brain data; ranking is an average over a growing benchmark set, with no documented re-ranking policy.

### Terminal-Bench (Merrill et al., ICLR 2026) and Terminal-Bench-Science ☐
[notes](notes/terminalbench.md) · Step 4, thin step 5.
**Take:** Admits only tasks with deterministic checkable outputs; verifier QA by repeated oracle runs and "task repair" PRs. Illustrates verifier-first sequencing; silent on allocation.

### Jev (TypeSafe AI, 2026) ☐
[notes](notes/jev.md) · Steps 5, 2 (as possible implementation).
**Take:** Cheap, opaque, calibrated classifier; usable only as a screening layer whose gap to re-execution is measured. Vendor claims only, no paper.

## Agent systems and skills

### Tang et al., WikiSkill (arXiv:2608.27454, 2026) ☐
[notes](notes/wikiskill.md) · Weak step 4, toy step 5.
**Take:** Verifier-gated self-improving agent loop with a harness-written audit log; skills gated and reversible, wiki ungated and permanent.

### K-Dense AI, Scientific Agent Skills (Kassis et al., arXiv:2609.00065, 2026) ☐
[notes](notes/kdense.md) · Step 4.
**Take:** Skill libraries ship structural QA but no correctness evaluation; substrate for step 4, not evidence on verification.

## Neuroscience and neuroimaging

### Meisler et al., "Highly replicable multisite patterns of adolescent white matter maturation" (bioRxiv, 2026) ☐
[notes](notes/meisler.md) · Step 4.
**Take:** Well-provenanced dMRI resource; "replicable" means cross-vendor consistency within ABCD, not independent replication. Candidate step-4 case.

### Fleming, "Towards an integrative neuroscience of metacognition" (*Nat Rev Neurosci*, 2026) ☐
[notes](notes/metacognition.md) · Trust (analogy).
**Take:** Local vs global confidence parallels per-claim vs venue trust; abstract-only summary, paywalled.

## Infrastructure

Details in [notes/tools.md](notes/tools.md).

- **Neurodesk** (Renton et al., *Nat Methods*, 2024) ☐ · Step 4. Versioned containers lower re-execution cost; no provenance capture.
- **LinkML** (Moxon et al., *GigaScience*, 2026) ☐ · Steps 4, 2. Schema validation checks form, not truth; could type dependency edges.
- **ORINOCO-Lite** ☐ · Steps 4, 6. Git-backed linked-metadata publishing; STAMPED-style substrate, no verification.
- **"Undata"** · Unresolved: no matching tool found. Needs a link or organization name.
