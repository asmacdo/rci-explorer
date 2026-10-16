# Choudhury et al., "Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science" (Mycelium, 2026)

Status: agent-generated 2026-10-16, not yet reviewed by a human.
The summary agent had no project context; the relevance agent read the repo plus that summary.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### 1. Citation

Choudhury, S., Czajka, J. J., Monteiro, L. M. O., Bredeweg, E., McDermott, J., Wolf, K., Beliaev, A., Elmore, J., Piehowski, P., Tate, K., Gao, Y., Bilbao, A., Stratton, K., Baker, S., Bardhan, J. P., Burnum Johnson, K., Oehmen, C., Rallo, R. (2026). *Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science.* arXiv:2607.13220 [cs.AI] (cross-lists cs.CE, cs.HC). All authors are at Pacific Northwest National Laboratory (PNNL), Richland, WA.
- Versions: v1 submitted 14 Jul 2026, v2 16 Jul 2026, v3 29 Jul 2026. The PDF is dated July 31, 2026. This entry covers v3.
- Venue: preprint, no peer-reviewed venue stated.
- License: CC BY 4.0 (orchestrator checked the license link on the arXiv abs page; the summary agent could not see the license name).
- DOI: https://doi.org/10.48550/arXiv.2607.13220. URL: https://arxiv.org/abs/2607.13220

### 2. Summary

The paper argues that AI-for-science work mostly scales a single reasoner (bigger models, longer contexts, one-user co-scientists). It proposes instead scaling the connections among humans, agents and instruments, which it calls "networked intelligence". Its system, Mycelium, keeps an "active context graph": a shared, provenance-tracked project state made of typed entries (observations, hypotheses, findings, open questions, experiment proposals). Users reach it through ordinary Claude chat clients over MCP. A server-side runtime runs sandboxed, code-generating analyses and writes results back to the graph. Four protocols govern the graph: logging with provenance, bounded proactive execution between sessions, asynchronous routing of relevant findings to other participants, and grounding of every write in existing graph nodes. The evidence is one week-long case study on a Pseudomonas putida multi-omics campaign (gluconate accumulation). Three domain experts worked asynchronously. The authors say routed context linked a regulatory anomaly, proteomic evidence and an HPLC phenotype constraint into a mechanistic model and an experiment proposal. They compared Mycelium with two single-agent autonomous baselines on 26 expert-defined "scientific artifacts" scored 0 to 4. Mycelium surfaced 25 artifacts, against 17 and 18 for the baselines, with a breadth-weighted score of 2.62 against 1.62 and 1.81. Specificity of surfaced artifacts was similar across the three. A supplementary note frames routing as sparse conditional computation and states when a large single model would suffice and when it would not.

### 3. Key concepts

- **Networked intelligence**: scaling the connections between humans, agents, instruments and robots, so a result from one context reaches whoever can act on it. The paper presents it as complementary to model scaling, not a replacement.
- **Active context graph (ACG)**: a directed graph of typed, provenance-bearing entries. Edges are lineage (derived_from, generated_by, uses) and epistemic (supports, contradicts). "Active" means the runtime evolves and evaluates it, unlike a passive graph database.
- **State-routing ("pollination")**: asynchronous scoring and delivery of new entries to participants whose analysis they affect. It is described as a message-passing step that keeps disagreement in separate threads instead of merging it.
- **Bounded autonomy**: the runtime runs exploratory analyses between user sessions and surfaces results at the next session. The paper reports about 18% of system actions were self-initiated (peak 37%).
- **Grounding**: write-time validation that each entry cites existing graph nodes such as datasets, tool outputs or parent entries.
- **Routing value**: Δ(v→j) = V_j(H_j ⊕ v) − V_j(H_j), the gain in a receiver's expected decision utility. A "critical edge" is one where Δ exceeds a threshold τ. The paper says estimating it needs an implementation-specific model.

### 4. Evidence quality

- **Demonstrated**: a single case study with 3 researchers, one week, 4,495 proteins across 62 samples, 48 HPLC measurements, and 4 strains. The routing episodes are narrated and traced in Fig. 4 and Fig. S2. The artifact scoring is tabulated per item in Table 3.
- **Evaluation design**: there is one run per condition (Mycelium, baseline B team-framed, baseline C unframed), so no variance or significance testing is reported. The 26 artifacts and the 0 to 4 rubric are authored by the study team, and the paper does not say who scored the traces or whether they were blinded. The artifact set appears to be built from the pooled traces ("global set of 26 unique artifacts"), so Mycelium's lead may partly reflect how the set was defined. The conditions are also not matched: Mycelium involved three humans over a week, with the model at "high" effort, while the baselines were single agents at "xhigh" effort. All used Claude Opus 4.8. The authors describe the audit as covering explicit evidence-to-action coverage only, not latent capability.
- **Asserted or illustrative**: the claim that the work compresses a "four-to-six-month" human iteration cycle into a sprint has no comparison data in the paper. The sparse-computation framework (Claims 1 and 2, Q3) is argued informally, and the authors say it illustrates the mechanism and does not establish a universal separation. Routing value is defined but not measured. No ablation isolates the graph from simply having three human experts.
- **Stated limitations**: this is a preliminary test in one domain. Reliability across multi-lab, multi-month work is untested. The current system gives all claims equal epistemic weight. Resolving conflicting routed signals and the loss of meaning across disciplines are open problems. The authors note proactivity must be tuned to avoid overwhelming users.

### 5. Confidence

- **Taken directly from the text**: authors, versions and dates (abs page and title page). Architecture, entry vocabulary and the four protocols (Sec. 2, Table 1). The case-study setup and routing narrative (Sec. 3.1, 3.2). The baseline design and Table 2 and Table 3 numbers (Sec. 3.3, Supplementary Methods S1 and S2). Proactivity figures (Sec. 4.1). The routing-value formula and the two-regime argument (Supplementary Note). Stated limitations (Sec. 4.1, 4.4).
- **Inferred**: that the artifact set was pooled from the traces. That scorer identity and blinding are unreported (I found no description, so this is an absence in the text I read, not a confirmed absence in the paper's supplements or code). That there is no variance estimate. That the effort-setting mismatch could confound the comparison. The ablation gap. These are my reading and not statements by the authors.
- **Unverified**: the paper's bibliography is not used here beyond naming the lab. I made no direct quotes beyond the single term "networked intelligence". I did not check any released harness or code mentioned in S1.

## Relevance to this project (repo-context agent)

1. **Tier**: STRETCH. It is a tooling and architecture paper on shared provenance-tracked project state. Its one evaluation scores generation breadth, not verification, trust updating, or allocation.

2. **Loop step(s)**: Mainly 4, because it runs analyses and writes results with provenance. It also touches 1, since routing is a form of search. It touches 2 only as a stated future need: attribution is built, epistemic weighting is not. "Allocation" appears only inside a project, as routing value.

3. **What it gives this project**:
- An existence proof of a live, typed, lineage-bearing graph with epistemic edges (supports, contradicts). That is a possible substrate for the "use as signal of load" dependency edge in `docs/map.md`. The paper does not count reliance.
- Write-time grounding, meaning every entry must cite existing nodes. This is a cheap, capture-as-side-effect provenance mechanism, which fits `docs/stamped.md` ("capture as a side effect of execution").
- Routing value, Δ = V_j(H_j ⊕ v) − V_j(H_j), a formal receiver-side utility gain. It is unmeasured, but it is a template for a load or value quantity.
- The design choice to keep disagreement in separate threads rather than merge it.
- Stated limitation, checked in the full text (Sec. 4.1): "attributes every propagated claim to its source but applies equal epistemic weight". It names differential weighting and surfacing contradictions as future work.
- A proactivity calibration tradeoff: too little drops links, too much overwhelms human oversight.

4. **Where it stops**: No re-verification, retraction, staleness or invalidation propagation, and no trust update. Contradiction edges exist but are not resolved. Scope is one team, one week, one domain, with no cross-lab body of science. The evaluation has n=1 per condition, unblinded author-built rubric, an artifact set apparently pooled from the traces, and mismatched conditions (3 humans vs single agents, different effort levels). It is not a benchmark of correctness.

5. **Bearing on repo claims**:
- Supports "Makes objects machine-auditable" (`docs/stamped.md`), as a capability demo only.
- Complicates "Use as the signal of load ... the loop doesn't currently record it" (`map.md`). A graph can record dependency edges, but only inside one project.
- Supports "5 → 2 needs an attribution rule" (`prior-art.md`) in part. Attribution is implemented, but weighting is explicitly unsolved, so the rule is still missing.
- Weakly supports "production near-free, retirement still expensive" (`ai-in-the-loop.md`). Its lead is in surfacing artifacts, and it has no retirement cost.
- Does not touch "Auditability is constitutive". It treats audit as an engineering feature.
- Consistent with "no source covers verification allocation".

6. **Links to existing entries**: Longino: "uptake" and routing of criticism are loosely analogous, but it is routing to collaborators, not a public critical community. Kitcher: its routing-as-allocation is of information, not effort, across programmes, a thin link only. Latour & Woolgar: provenance preserved on every claim runs against hedges being shed in transit.

7. **One-line take**: Useful provenance-graph substrate demo; its own evaluation scores generation breadth, and it explicitly leaves trust weighting and contradiction resolution undone.

8. **Confidence**:
- Rests on the summary: architecture, protocols, case-study numbers, evaluation-design weaknesses.
- Checked in the full text: the equal-epistemic-weight limitation and the proactivity tradeoff (Sec. 4.1, lines ~405-418). A keyword grep for verif, replicat, retract, stale and invalidat found no retraction or invalidation machinery; the matches are about audit and verifying data structures.
- My background knowledge: none material.
- My inference: that the graph could serve as a load-recording substrate. That is a guess, since the paper does not count downstream reliance.
- My inference: that STRETCH is right. A HIGH argument exists, because it builds the "critic over auditable objects" substrate, but no verification is evaluated.
