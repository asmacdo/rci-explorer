# Tooling batch: ORINOCO-Lite, LinkML, Undata, Neurodesk, OHBM OSSIG Reproducibility Challenge, Neurosynth Compose

Status: agent-generated 2026-10-16, not yet reviewed by a human.
The summary agent had no project context; the relevance agent read the repo plus that summary.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### ORINOCO-Lite
- **Citation**: https://github.com/ORINOCO-Lite/ (GitHub org, 15 repos; no public members; no paper listed). Main repos: orinoco-lite-dev (engine, MIT), orinoco-lite-template (Copier template, MIT), psychoinformatics-downstream (MIT). Several repos are account mirrors of con/ and psychoinformatics.de repos (shacl-vue, dump-things-service, dump-things-pyclient, pool.psychoinformatics.de-ui). The page links a Distribits 2026 talk by @jsheunis as an introduction.
- **What it is**: A lightweight way for research groups to build linked-data knowledge bases that drive websites, CVs and project reports. Records live in GitHub repos, GitHub Actions provide ephemeral services, and GitHub Pages hosts the output, so no always-on infrastructure is needed. The README says it "helps research groups adopt the ORINOCO approach to structured, linked metadata and website generation." The engine is described as a content-neutral, deterministic runtime for metadata-driven sites. Note that the description "a formalization for research products" is not the org's own wording.
- **Verification/provenance angle**: Deterministic, git-tracked generation of sites from metadata records gives re-execution and history, but I saw no explicit claim-checking features.
- **Confidence**: Verified from the org page only. I did not open individual repos, so the license is known only for the repos listed above (MIT) and unknown for the rest. The "research products" framing is inferred.

### LinkML
- **Citation**: https://linkml.io/ . Paper: Moxon SAT, et al. "LinkML: an open data modeling framework." GigaScience 2026;15:giaf152, DOI 10.1093/gigascience/giaf152 (full author list not seen). License: Apache 2.0.
- **What it is**: An open framework for defining, validating and sharing structured data. You write schemas in YAML (classes, slots, enums, inheritance, pattern and logical constraints). Every element gets a URI/IRI, so models are FAIR and linkable. A generator framework produces 30+ artifacts, including JSON Schema, OWL, SHACL, RDF, SQL DDL, Pydantic, Python dataclasses, TypeScript, Java, Rust, plus docs. A runtime loads and dumps YAML, JSON, CSV and RDF. Schemasheets lets non-developers define models in spreadsheets. The ecosystem includes OntoGPT, schema-automator, DataHarmonizer, linkml-transformer and OAK.
- **Verification/provenance angle**: Supports checking data against a schema (validation) and stable resolvable identifiers (w3id.org), but it does not itself record execution provenance.
- **Confidence**: Verified from https://linkml.io/ (via fetch summary). The paper's author list and the DOI come from that page only and were not checked at the publisher.

### Undata
- **Citation**: Not found.
- **What it is**: I could not identify a tool called "Undata" that is a schema and data element repository with translation. Searches returned only UNdata (the UN Statistics Division data portal, whose terms allow free copying with citation, and a third-party repo yuiseki/undata-sdmx), which does not match. Neighbouring candidates seen in results, none confirmed as what you meant: INCF Neuroshapes (https://github.com/INCF/neuroshapes, open schemas for FAIR neuroscience data) and Allen Institute biodata-schema. The name may be wrong (possibly a variant spelling, or a translation-oriented schema registry under another name).
- **Verification/provenance angle**: None evident, because the item was not identified.
- **Confidence**: Not found. The UNdata and Neuroshapes mentions are only from search result snippets, and I judge them unlikely matches. A link or organization name from you would let me retry.

### Neurodesk
- **Citation**: https://www.neurodesk.org/ . Paper: Renton AI, Dao TT, Johnstone T, Civier O, Sullivan RP, White DJ, Lyons P, ... Narayanan A, Bollmann S (corresponding). "Neurodesk: an accessible, flexible and portable data analysis environment for reproducible neuroimaging." Nature Methods 21(5):804-808, 2024 (online 8 Jan 2024), DOI 10.1038/s41592-023-02145-x. 45 listed authors. License: not stated on the site; the preprint is on bioRxiv (10.1101/2022.12.23.521691) and PMC10055538.
- **What it is**: A platform that gives consistent, containerized neuroimaging and biomedical tools across computing systems. It has 100+ tools. Access is through Neurodesktop (a browser or desktop environment), Neurocontainers (individual versioned containers), and Neurocommand (a command-line manager). The aim is that the same software versions run on a laptop, a cloud machine or an HPC cluster, so analyses are portable and reproducible.
- **Verification/provenance angle**: Enables re-execution by pinning tool versions in containers; I saw no automatic provenance capture.
- **Confidence**: Site and DOI verified from neurodesk.org; author list, volume and pages from search result snippets (Macquarie, CSHL records), not the Nature page. License not found.

### OHBM Open Science SIG (OSSIG) Reproducibility Challenge
- **Citation**: https://ossig.netlify.app/challenge/ ; repo https://github.com/KMarshallX/ossig-reprochallenge (search result title: "2026 OHBM-OSSIG Reproducibility Challenge"; another result named ohbm/ossig-reprochallenge). Earlier flyer: https://humanbrainmapping.org/files/2025-%20Brisbane/challenge2pgs_(002).pdf . No paper. License: not stated.
- **What it is**: The 2026 edition (source work must be an OHBM 2026 abstract; results presented at OHBM 2027). Teams of two: a source party supplies code and data description, a reproducing party re-runs the analysis with at most one intro meeting. It covers reproducibility (same data) and replicability (independent data). Open code is mandatory. Registration is by a GitHub issue, and OSSIG matches teams. Output is a joint abstract and possibly an Open Science Room talk. Judging looks at fidelity to the original, openness of the source, and extra outputs; failed attempts are not penalized. The flyer says it was inspired by the ISMRM RRSG challenge. No fixed deadlines were given.
- **Verification/provenance angle**: It directly supports checking published claims by independent re-execution, but it is a community process and does not record provenance by itself.
- **Confidence**: Verified from the ossig.netlify.app page (via fetch summary). The repository owner name is uncertain (two variants in search results). The 2025 flyer was seen only as a search snippet.

### Neurosynth Compose
- **Citation**: https://neurosynth-compose.org (platform; URL not fetched, from memory, treat as inferred). Paper: Kent JD, et al. "Neurosynth Compose: A web-based platform for flexible and reproducible neuroimaging meta-analysis." Imaging Neuroscience, published 27 Jan 2026, DOI 10.1162/IMAG.a.1114, PMC12849227. Open access, CC BY 4.0 (paper). A PubPub version also exists, DOI 10.21428/8e6ba8ef.ad3a3f80. Software license not checked.
- **What it is**: A web platform for building neuroimaging meta-analyses without hand-assembling data. Curation and annotation tools follow PRISMA. It draws on NeuroStore, a database of 30,000+ studies with pre-extracted coordinates. Meta-analysis specifications are defined with the NiMADS standard and executed with the NiMARE Python library, either locally or in the cloud, and results return to the platform for review and sharing. A 2024 conference abstract appeared in Biological Psychiatry 95(10).
- **Verification/provenance angle**: Records the full meta-analysis specification and curation steps in a shareable, re-runnable form (NiMADS plus NiMARE), which supports reproducing and auditing a meta-analytic claim.
- **Confidence**: Paper details verified from search result snippets (PMC12849227, FIU and Oxford ORA listings), not by opening the paper. The full author list was not seen. Platform URL and software license not verified.

## Relevance to this project (repo-context agent)

### ORINOCO-Lite
**Tier**: STRETCH. Site-generation tooling; the summary shows no claim-checking or verification features.
**Loop step(s)**: 4 and 6, as a substrate for publishing git-tracked metadata about research products.
**What it gives / where it stops**: A pattern for deterministic, git-backed, linked-metadata generation with ephemeral CI services. This fits the STAMPED substrate idea (docs/stamped.md: "capture as a side effect of execution"). It stops at presentation. It has no evaluation, trust-update or load signal. The summary is org-page only, so repo-level features are unknown.
**Bearing on repo claims**: None real.
**One-line take**: Cheap STAMPED-style publishing substrate; says nothing about verifying or allocating trust.

### LinkML
**Tier**: STRETCH. Schema and validation tooling, not a verification-allocation account.
**Loop step(s)**: 4 (typed research objects), 2 (machine-readable metadata a critic could consume).
**What it gives / where it stops**: Schema-level validation and stable identifiers make objects "machine-auditable" in the narrow sense of docs/stamped.md. Any dependency or "use as load" edge could be modelled in a schema. It checks form, not truth. It records no execution provenance and covers no cost or trust model. Static conformance is the cheap, gameable grader tier ("Static ... gameable").
**Bearing on repo claims**: Mildly complicates "Makes objects machine-auditable": schema-valid is not claim-valid.
**One-line take**: Useful vocabulary for typing objects and load edges; validates structure only, never correctness.

### Undata
**Tier**: STRETCH. Not identified, so nothing to assess.
**Loop step(s)**: None assignable.
**What it gives / where it stops**: The summary found no matching tool. UNdata and Neuroshapes were seen only as unconfirmed snippets. Nothing here can be used until the item is identified.
**Bearing on repo claims**: None.
**One-line take**: Unresolved; need a link or organization name before any assessment.

### Neurodesk
**Tier**: STRETCH. Environment-portability tooling, with no provenance capture seen.
**Loop step(s)**: 4, as pinned and portable execution.
**What it gives / where it stops**: Versioned containers improve the "environment unrecorded" row of docs/map.md and lower the cost of re-execution. That cost is the variable the project says drives verification spend. It stops at the environment. It records no analysis provenance, executes no claim check, and has no allocation or trust layer. The same container can still be used badly.
**Bearing on repo claims**: Supports "STAMPED ... lowers cost to retire and cost to build on" at the portability tail. It also fits the closing-holes-gets-costlier point in docs/stamped.md.
**One-line take**: Concrete example of a falling re-execution cost; the verification question stays untouched.

### OHBM OSSIG Reproducibility Challenge
**Tier**: HIGH. A live community mechanism that re-executes published work, which is step 5 in practice and a candidate case for docs/cases.md.
**Loop step(s)**: 5, with a possible 5 → 2 test; also norms and allocation, since pairing is decided by organizers.
**What it gives / where it stops**: A real case: source and reproducing parties, fidelity judging, failed attempts not penalized. Selection is by volunteer and OHBM abstract, which is the cohort-sampled, non-load-driven re-evaluation that docs/prior-art.md flags in OSC. It supports "Reviewers read; they can't re-run" by showing a separate channel for re-running. It stops at one event. It has no trust-update feed, no dependency-load targeting, and no outcome data yet.
**Bearing on repo claims**: Supports "Cases: replication attempt" as a traceable case. Whether 5 → 2 fires is untested, and the process notes nothing about it. The summary names no output that updates trust.
**One-line take**: Best case-trace candidate in this batch; check whether any result ever updates trust in the source.

### Neurosynth Compose
**Tier**: HIGH. Step 1 and 5 infrastructure for neuroimaging claims, and a plausible target for critic agents.
**Loop step(s)**: 1 (search and curation), 4 and 5 (re-runnable meta-analysis specification).
**What it gives / where it stops**: Meta-analysis specs (NiMADS) plus execution (NiMARE) are stored in re-runnable, shareable form. That is an executed-grader candidate in the docs/stamped.md sense. It also aggregates across studies, so it could in principle expose dependency counts, which docs/map.md says the loop does not record. It stops at the meta-analysis unit. It makes no claim about trust scoring, update propagation or allocation. The extracted coordinates may be noisy, and that is unverified here.
**Bearing on repo claims**: Complicates "The loop doesn't currently record" use as load: aggregation by study is a partial exception. Supports "machine-auditable" for meta-analytic claims.
**One-line take**: Re-runnable meta-analysis is a real verifier-adjacent artifact; check whether study reuse counts are exposed.

## Confidence
- Rests on the summary: all descriptions of each tool. The summary is search-snippet and fetch-summary level, and no repo or paper was opened. The Neurosynth Compose platform URL and the licenses are unverified.
- Rests on my background knowledge: little. I relied on general familiarity with LinkML and NiMARE and did not use it to add facts.
- My inference: the tier calls and the loop mappings. The claim that Neurosynth Compose could expose reuse counts, and the OHBM challenge's lack of a trust-update output, are guesses from what the summary does not mention. The summary may simply not have covered them.
- Undata: no assessment is possible.
