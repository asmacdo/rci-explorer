# Meisler et al., "Highly replicable multisite patterns of adolescent white matter maturation" (2026)

Status: agent-generated 2026-10-16, not yet reviewed by a human.
The summary agent had no project context; the relevance agent read the repo plus that summary.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### 1. Citation

Meisler SL, Cieslak M, Bagautdinova J, Hendrickson TJ, Pandhi T, Chen AA, Hillman N, Radhakrishnan H, and others (about 50 to 60 authors; the two fetches gave different counts), ..., Satterthwaite TD. 2026. "Highly replicable multisite patterns of adolescent white matter maturation." bioRxiv preprint (New Results), v1. DOI: 10.64898/2026.04.18.719321. https://www.biorxiv.org/content/10.64898/2026.04.18.719321v1. Posted 2026-04-19 per the landing page. License: CC-BY-NC-ND 4.0 International, per the landing page. Corresponding authors: Meisler and Satterthwaite. The full author list is not captured here (the middle authors were not seen).

### 2. Summary

The paper asks whether white matter microstructure and its adolescent development can be measured consistently across the scanners and sites of the ABCD Study. It also releases the resource built to answer that: ABCC release 3.1.0, more than 24,000 processed ABCD diffusion MRI datasets with image quality metrics, microstructural maps and person-specific bundle tractography.

After quality control the sample is 24,178 dMRI datasets from 10,738 participants aged 8 to 17 at 21 sites. 33 trained raters manually scored 3,101 images, and a multivariate classifier extended those scores to the full cohort. Processing used QSIPrep and QSIRecon. The authors computed 40 automated image quality metrics and 33 microstructural maps (DSI Studio, DIPY, TORTOISE, AMICO), summarized over 67 bundles. The main analyses used 62 consistently resolved bundles and five measures: FA, MD, ICVF, RTOP and MKT.

Longitudinal nonlinear harmonization was applied by acquisition batch (scanner plus software version). Age and quality effects were fit with generalized additive mixed models, with effect size as ΔR²adj.

Operationally, the replicability evidence I could see is cross-vendor correspondence: the Spearman correlation of bundle-wise age effects between vendors. Batch explained up to 69.8% of variance before harmonization. After harmonization, mean cross-vendor rho was above 0.91. ICVF, MKT and RTOP were about four to five times as sensitive to development as FA, were highly intercorrelated (rho of 0.93 or more), and were robust to image quality. Head motion and manual ratings had smaller effects than dMRI contrast. Adding batch-structured quality metrics such as framewise displacement as covariates attenuated age effects on GE scanners.

### 3. Replication design

- Replication is within one cohort (ABCD), across vendors and software batches. I saw no independent replication cohort. HCP-D, HBN and PNC do not appear, and the text mentions combining with other cohorts only as future work.
- The paper's stated definition of "replicable" was not found. The closest operational measure is the cross-vendor Spearman correlation of age effects, before versus after harmonization.
- Shared, open pipeline: QSIPrep and QSIRecon container images are on DockerHub and run under Docker or Singularity/Apptainer. Analysis code and reproduction instructions are at GitHub PennLINC/Meisler_ABCD_dMRI. Manual-rating training material is on OSF.
- Data access is restricted. Raw ABCD Release 6.0 data and the ABCC derivatives are available via the NIH Brain Development Cohorts Data Hub (NBDC) to researchers with a Data Use Certification.

### 4. Confidence

- Verified from the .full URL (https://www.biorxiv.org/content/10.64898/2026.04.18.719321v1.full), read through character 200000 of 217033 by a summarizing fetch tool: title, DOI, datasets and N, methods, results numbers, data and code availability, containers. The last 17k characters (probably references or supplement) were not read.
- Verified from the landing page (.../719321v1): posting date, CC-BY-NC-ND 4.0 license, first authors.
- The .full fetch said the license was not stated, and the landing page gave CC-BY-NC-ND. I trust the landing page.
- Both fetches paraphrased through an intermediate model. No exact quotes were obtained, and numbers should be spot-checked against the paper before being cited in anything formal.
- Not found: a text definition of "replicable", the exact author count, and the middle authors. The claim of no independent replication sample is based on the fetched text not naming one, which is an absence of evidence from a summarizer, not a confirmed negative.
- The web search did not surface the preprint page itself. It only confirmed, via Stanford profile listings, that the title and authors exist.

## Relevance to this project (repo-context agent)

1. **Tier**: STRETCH. A neuroimaging data and pipeline resource paper whose "replicable" is within-cohort cross-vendor consistency; it carries no verification, trust or allocation content.

2. **Loop step(s)**: Step 4 (execute, produce a research object) as a well-recorded example. Step 5 only weakly, since batch effects and QC are verifier-like checks inside the pipeline. Not 2, not trust, not allocation.

3. **What it gives this project**:
- A concrete step-4 object that is close to STAMPED: containerized QSIPrep/QSIRecon, public analysis code (PennLINC/Meisler_ABCD_dMRI), an OSF rater-training archive. Useful as a "good provenance" exemplar.
- A mechanism case for hidden environment effects: batch (scanner plus software) explained up to 69.8% of variance before harmonization. This shows a result can look robust or fragile depending on a processing choice, which bears on how a static STAMPED grade relates to rigor.
- Harmonization's side effect: adding batch-structured QC covariates attenuated age effects on GE scanners. A small illustration of "cheap checks can change the answer".
- A word-meaning case: the title says "replicable", the operational measure is a correlation between vendors.

4. **Where it stops**: No independent replication cohort seen. No stated definition of "replicable". No downstream-use, load, or dependency data. No cost accounting. Data access is restricted (DUC), so audit by outsiders is partial. Nothing on how a failed check would update trust in the object.

5. **Bearing on repo claims**:
- `docs/stamped.md`: "Reproducible ≠ rigorous; keep the scores separate." Supported. The pipeline is open and re-runnable, yet "replicable" is shown only as cross-vendor agreement within ABCD.
- `docs/stamped.md`: "Static (provenance present) vs. executed (re-run reproduces)." Complicated. Restricted data means static provenance is public but execution is gated.
- `docs/map.md`: "Reviewers read; they can't re-run." Weakly complicated: code and containers are released, though the review status of a preprint is unknown.
- `docs/prior-art.md` point 3 ("auditability is constitutive has no support"): no effect.
- `docs/prior-art.md` point 1 ("no source covers verification allocation"): no effect.

6. **Links to existing entries**: OSC is the only real link, on what "replication" means. OSC re-ran studies independently. This paper replicates across vendors within one cohort, a narrower claim.

7. **One-line take**: Well-provenanced dMRI resource; "replicable" means cross-vendor consistency within ABCD, not independent replication. Good for a step-4 or vocabulary case, not for the core problem.

8. **Confidence**:
- Rests on the summary: all paper specifics (numbers, design, code and data availability). The summary came from a fetch tool that paraphrased through a model, last 17k characters unread, "no independent cohort" is an absence-of-evidence claim.
- Rests on my background: the general point that cross-vendor harmonization consistency is not replication (standard in neuroimaging). Did not independently know this paper.
- My inference (guesses): that the title's "replicable" is meant as multisite consistency; that this suits only a modest case.

**Case assessment (docs/cases.md)**: Usable as a small, honest step-4 case, but not the replication-attempt case on the TODO list. It illustrates the vocabulary gap ("replicable" as cross-site consistency vs independent replication) and a good-provenance object. Before tracing, someone should read the full paper to confirm the missing definition, the absence of any other cohort, and what the last 17k characters hold. It also has no step 5 to 2 events to trace, so most of the loop edges would stay empty. Better paired later with a true replication of the same finding in HCP-D or similar, if one exists (I do not know of one).
