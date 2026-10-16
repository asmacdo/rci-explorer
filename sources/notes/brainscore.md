# Brain-Score (Schrimpf et al. 2018, 2020)

Status: agent-generated 2026-10-16, not yet reviewed by a human.
The summary agent had no project context; the relevance agent read the repo plus that summary.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### 1. Citation

- Brain-Score platform: https://www.brain-score.org/ (open source; docs at https://brain-score.readthedocs.io/).
- Schrimpf, M., Kubilius, J., Hong, H., Majaj, N. J., Rajalingham, R., Issa, E. B., Kar, K., Bashivan, P., Prescott-Roy, J., Geiger, F., Schmidt, K., Yamins, D. L. K., DiCarlo, J. J. (2018). Brain-Score: Which Artificial Neural Network for Object Recognition is most Brain-Like? bioRxiv. doi:10.1101/407007 (DOI confirmed via search; author list is from background knowledge, so check it).
- Schrimpf, M., Kubilius, J., Lee, M. J., Murty, N. A. R., Ajemian, R., DiCarlo, J. J. (2020). Integrative Benchmarking to Advance Neurally Mechanistic Models of Human Intelligence. Neuron 108(3). doi:10.1016/j.neuron.2020.07.040 (DOI confirmed via search; volume, issue and author list are from background knowledge).
- Schrimpf, M., Blank, I. A., Tuckute, G., Kauf, C., Hosseini, E. A., Kanwisher, N., Tenenbaum, J. B., Fedorenko, E. (2021). The neural architecture of language: Integrative modeling converges on predictive processing. PNAS 118(45). doi:10.1073/pnas.2105646118 (from background knowledge only; not verified in this session).
- I found no dedicated later platform paper ("Brain-Score 2.0") in search. Schrimpf's 2025 ICLR workshop talk describes more than 100 benchmarks. The MIT Quest page (https://sqi.mit.edu/research/platforms/brain-score) mentions Brain-Score 2.0 and Brain-Score Language.

### 2. Summary

Brain-Score scores how well machine-executable models match primate and human brain and behavior data. Vision (ventral stream neural recordings and behavior) was first. Language was added later, and the site now also lists fMRI and EEG benchmarks. A Benchmark runs an experiment on a model through a common BrainModel interface. A Metric compares the model's output to the data, and the raw score is divided by a data-derived ceiling, so 1 means the model matches the data to ceiling level (documented at readthedocs). Benchmark identifiers follow a data-metric pattern, for example Rajalingham2018-i2n. A benchmark version is bumped only when its scores change. The site states that models are ranked by their average score across all benchmarks. It does not explain how that average is built from sub-benchmarks or regions. Contributors follow tutorials for modelers and for experimentalists and use a Submit pathway. The MIT Quest page describes a modular plugin system for contributing data, metrics, benchmarks and models. The leaderboard shows the latest evaluations of every model on every benchmark, with per-model and per-benchmark detail. New benchmarks keep arriving over time, and recent additions include THINGS fMRI, NSD, TVSD and THINGS EEG2. Because the ranking is an average over the current benchmark set, adding benchmarks can change the ranking. I found no stated policy for how rankings are managed when benchmarks are added or versioned. The Neuron paper frames the platform as integrative benchmarking.

### 3. Design principles

- Integrative benchmarking: many experiments from many labs are pooled into one suite, so models are tested against a whole domain rather than one dataset (Neuron 2020 framing, from the paper's abstract as returned by search).
- Standard interface: models are tested only through the BrainModel interface, and benchmarks are paired Data and Metric objects (readthedocs).
- Ceiling normalization: each score is divided by the benchmark's ceiling, which estimates the signal in the data (readthedocs).
- Open and community-driven: the code is open source, there are plugins and tutorials for contributing, and a public leaderboard exists (brain-score.org, MIT Quest page).
- Simple aggregation: the overall ranking is the average score across benchmarks (brain-score.org).

### 4. Known critiques/limitations

- Feather, Khosla, Wang et al. have argued that brain scores can mislead (arXiv 2406.01538, "What Are Large Language Models Mapping to in the Brain? A Case Against Over-Reliance on Brain Scores"). A trivial feature encoding temporal autocorrelation beat LLMs under shuffled train-test splits, so some language brain scores may reflect data structure. I only saw the search summary of this paper, and its author list is not verified. It targets brain-score-style evaluations in general, not Brain-Score specifically.
- Other work questions the discriminative power and robustness of model-brain alignment rankings. Examples are a 2026 ICLR paper and "NeuroAI for AI Safety" (arXiv 2411.18526), which notes that vision models occupy a low-dimensional manifold. I did not read these papers, and they are not specific to Brain-Score.
- A 2019 paper (arXiv 1909.06161, Kubilius et al., CORnet) reported a possible disconnect between ImageNet performance and Brain-Score, with one state-of-the-art model scoring poorly on brain measures.
- Background knowledge only: the average-of-benchmarks ranking depends on which benchmarks are included, and aggregation is not fully documented.

### 5. Confidence

- Verified by fetching https://www.brain-score.org/: the platform description, ranking by average score, tutorials and Submit links, and recent benchmark additions.
- Verified by fetching https://brain-score.readthedocs.io/en/latest/modules/benchmarks.html: the Benchmark, Metric and ceiling definitions, the normalization wording, the identifier format and the versioning rule. That page says nothing about aggregation.
- Verified by search results only: the bioRxiv DOI (https://www.biorxiv.org/content/10.1101/407007), the Neuron DOI, the MIT Quest page description (https://sqi.mit.edu/research/platforms/brain-score), the ICLR 2025 talk's ">100 benchmarks" claim, and the critique papers' arXiv IDs. I did not open the papers themselves.
- Background knowledge only, not checked this session: the PNAS 2021 DOI, all author lists, and the Neuron volume and issue.
- Not found: a formal later platform paper and any documented policy for re-ranking when benchmarks are added.

## Relevance to this project (repo-context agent)

1. **Tier**: STRETCH. Brain-Score is a worked example of a community-maintained benchmark acting as a shared verifier for models. It says nothing about verifying the existing body of results or about allocating verification effort.

2. **Loop step(s)**: 5 (evaluation done by a standing, re-runnable artifact instead of reviewers) and "norms" (community-governed benchmark contribution). It touches 6 weakly, since a model's leaderboard standing changes over time. It does not touch 2 directly.

3. **What it gives this project**:
- A concrete benchmark-as-verifier instance in a domain with real data, which is relevant to docs/ai-in-the-loop.md ("find the loop with a verifier").
- Mechanisms: a standard interface (BrainModel), ceiling normalization (a data-derived noise ceiling), benchmark versioning that bumps only when scores change, and a plugin pathway for contributors.
- A re-evaluation edge that actually fires. Scores are recomputed when benchmarks are added or versioned, so trust in a model is not frozen.
- Evidence for the Goodhart worry. Benchmark average ranks depend on benchmark composition, and a 2019 CORnet-era report suggests ImageNet performance and Brain-Score can diverge. Feather et al. (per the summary) show a trivial feature beating LLMs under some splits.

4. **Where it stops**:
- It evaluates models against data, not papers, claims or datasets.
- Nothing on load or dependency counts, cost to retire, or who decides what gets re-checked.
- No documented aggregation or re-ranking policy (per the summary).
- It does not cover attribution when a score drops (5 → 2).
- It is neuroscience-specific, so generalization is the project's inference.

5. **Bearing on repo claims**:
- docs/ai-in-the-loop.md, "no verifier exists the way math has one": complicates it. A partial verifier exists here, with a ceiling-normalized score against data.
- docs/cases.md, "any benchmark for autonomous science is a scalar; a capable agent will do to it what this one did": supports it. The average-score ranking is a scalar, and benchmark-set dependence is a gameability surface.
- docs/map.md, "6 is a state, not a gate": mildly supports it. Leaderboard standing is revisable.
- docs/map.md, 5 → 2: complicates it. Re-scoring exists, but the summary shows no rule for propagating a failure to a model's sources.
- docs/prior-art.md cross-cut 1, "no source covers verification allocation": supports it. The summary shows no allocation policy.
- docs/prior-art.md cross-cut 3, auditability as constitutive: weak support at most. The platform is open and re-runnable, but that is design, not a constitutive claim.

6. **Links to existing entries**:
- Longino: open submission and public leaderboard resemble venues and shared standards. Whether uptake occurs is unknown.
- Ioannidis and OSC: benchmark scoring contrasts with one-off significance filtering and cohort replication, because re-evaluation here is routine.
- Merton: the open code and data fit "communism" (sharing).

7. **One-line take**: A live, re-scoring benchmark verifier with partial scalar-gaming evidence, but no account of what to verify or how often.

8. **Confidence**:
- Rests on the summary: the interface, ceiling and versioning mechanics, the average-score ranking, the undocumented aggregation, and the critiques. The summary read only abstracts for the critique papers, and the platform page for the rest.
- Rests on my background knowledge: that Brain-Score has been used as an optimization target in model-development work.
- My own inference (flagged as guesses): that the platform generalizes as a template for other domains, and that benchmark-set dependence is a Goodhart risk comparable to lee3j. The 2019 ImageNet divergence is a single report, not a settled finding.
