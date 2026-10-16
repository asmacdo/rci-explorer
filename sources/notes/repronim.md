# ReproNim, Center for Reproducible Neuroimaging Computation (repronim.org, fetched 2026-10-16)

Status: agent-generated 2026-10-16, not yet reviewed by a human.
The summary agent read 21 site pages (in `../originals/repronim.org/`) with no project context; the relevance agent read the repo plus that summary and assessed ReproNim through the RCI lens.
Each section ends with its own confidence notes; the loop mappings and B/C classifications are agent inference.

## Summary (context-free agent)

### 1. Citation

ReproNim: A Center for Reproducible Neuroimaging Computation. Website, https://repronim.org/ (21 pages read from a saved text copy, fetched 2026-10-16). Site gives no author byline, license, or version; pages are undated except where noted.
- Funder and mechanism (site, /about/): NIH, National Institute of Biomedical Imaging and Bioengineering (NIBIB), P41 program (National Center for Biomedical Imaging and Engineering). The site itself does not state the grant number.
- Grant details confirmed via the NIH RePORTER API (api.reporter.nih.gov, queried by appl_id 8999833, because the RePORTER web page is JavaScript-rendered and returned no content): core project P41EB019936. Appl 8999833 is 1P41EB019936-01A1, FY2016, $1,355,290. Contact PI David N. Kennedy, UMass Chan Medical School (Worcester, MA). Project start 2016-04-15. The current record (2P41EB019936-11, FY2026, $213,530 in that FY record) shows project end 2031-06-30, opportunity PAR-23-235.
- Mismatch to note: the site's collaborators page labels Phase 2 as "2021-2026", while RePORTER shows the project end as 2031-06-30. I do not know whether a renewal or a later phase is not yet reflected on the site. This is unresolved.

### 2. Summary

ReproNim describes itself as "a multi-site national center dedicated to developing tools and methodologies for reproducible neuroimaging computation", funded by NIBIB's P41 program. It says it was founded in 2016 and works across six sites (UMass Chan, MIT, Dartmouth, McGill, UC San Diego, UC Irvine). Its mission is to deliver tools, training, and principles for "rigorous, reproducible, and FAIR neuroimaging" (/about/).

The stated problem (/about/why/) is a "reproducibility crisis" with two causes. One is poor design, including underpowered studies. The other is that results are very sensitive to small variations in computational environments, preprocessing, statistical models and analyses ("everything matters", citing the center's 2019 paper). The site narrows "reproducibility" to re-executability (same data, same methods, same results). It treats this as a first step, and full reproducibility also requires independent generalization.

The "ReproNim approach" (/about/principles/, /about/repronim-approach/) has four principles: planning, data and metadata management, software management, and publishing everything. Four "actions" implement them: use of standards, annotation and provenance, version control, and containers. The principles are described as a reformulation of an earlier "5 Steps". The site also points to STAMPED as a complementary checklist that builds on YODA.

The "Reprosystem" covers the full cycle of acquisition, analysis, and publication. Data and metadata (with provenance) stay linked. Machine-readable metadata sit in a local store (ReproPond) or a shared public one (ReproLake).

Tools (/resources/tools/):
- Standards: BIDS, NIDM.
- Core tools: DataLad, HeuDiConv, Neurobagel, Neurodocker, Nipoppy, PyNIDM, ReproSchema, ReproStim.
- Infrastructure: ReproLake (a public NIDM/BIDS-based triplestore, hosted on Stardog, queried through Neurobagel or SPARQL) and ReproNim/containers.
- Best practice: ReproIn.
- Many additional tools, for example BABS, con/duct, ReproMan, reprozip, testkraken.

Community and training:
- A modular curriculum with five modules.
- A Fellowship: ReproNim/INCF, a full-year train-the-trainer program, 33 graduates and 12 current Fellows. It is not running this year and is anticipated for 2027.
- Monthly "First Fridays" webinars and an External Advisory Board of 7 members.
- Tutorials, ReproRehab, ABCD-ReproNim, a ReproInventory catalog effort, monthly office hours, and a blog.

Structure: Collaborative Projects (CPs, "technology drivers, users, and testbeds") and Service Projects (SPs, "users of the well-developed and stable technologies"). Phase 2 (2021-2026) lists 10 CPs and 10 SPs. Phase 1 (2016-2021) lists 10 CPs and 8 SPs. The site says nothing about Technology and Research Development projects (TRDs) beyond the passing mention of "P41 Technology and Research Development projects" on the collaborators page. It does not describe a current phase beyond "Phase 2, 2021-2026".

### 3. Key concepts

- Four principles: (1) Study planning, (2) Data and metadata management, (3) Software management, (4) Publishing everything. Page: /about/principles/.
- Four actions: use of standards, annotation and provenance, implementation of version control, use of containers. Page: /about/principles/.
- Sub-steps. Planning 1a-1e: power and statistics, pre-existing data, DMSP, open consent, pre-registration (/about/principles/planning/). Data 2a-2c: standard formats, version control, standard annotation (/about/principles/data_management/). Software 3a-3f: released versions, version control, automated install, automated execution, annotated code, containers (/about/principles/software_management/). Publish 4a-4d: share plans, software, data, make all objects FAIR (/about/principles/publish_everything/).
- "5 Steps to Reproducible Neuroimaging": the earlier framework that the four principles reformulate. It is mentioned but not described on the pages read (/about/principles/).
- Re-executability: "the ability to obtain the exact same results when the same data is analyzed using the exact same analysis methods". A result is "fully reproducible when it can be re-executed and generalized independently" (/about/why/).
- Reprosystem, ReproPond (local/private metadata store), ReproLake (shared/public) (/about/repronim-approach/, /resources/tools/reprolake/).
- STAMPED: Self-contained, Tracked, Actionable, Modular, Portable, Ephemeral, Distributable, "a generalization of the earlier YODA Principles" (/about/principles/data_management/, /about/principles/).
- Collaborative Projects vs Service Projects (/about/collaborators/).
- Curriculum modules: ReproNim introduction, Reproducibility basics, FAIR data, Data processing, Statistics (/resources/training/).
- "Hidden variance" from software differences (/about/principles/software_management/).

### 4. Evidence quality

- The site is programmatic and promotional: it states principles and recommendations, and describes tools. There are no evaluations of the center's own impact and no adoption metrics beyond the Fellowship count (33 graduates, 12 current) and the lists of CPs and SPs.
- The ~100-item publication list (/about/publications/) is a bibliography of center-affiliated work. Some items are directly relevant evidence for the approach, for example Kennedy et al. 2019 "Everything Matters", Hodge et al. 2021 on re-executability of the autism neuroimaging literature, Botvinik-Nezer et al. 2020, and the ReproSchema evaluation (Chen et al. 2025). The site does not summarize their findings or link them to specific claims. Many listed papers are only loosely connected to reproducibility.
- Claims such as "Without rigorous software management ... even subtle differences in software can lead to significantly different results" are supported by a single citation (Kennedy et al., 2019). Most recommendations in the principle pages carry no citations or data.
- Getting-started personas ("Sarah", "Richard", "John", "Evelyn") are illustrative, AI-generated, and not user data. The site admits ReproNim "is not an end-to-end platform".
- RePORTER confirms funding but not outcomes.

### 5. Notable passages (verbatim)

- "ReproNim’s mission is to deliver effective tools, training, and principles to the neuroimaging community to support the entire neuroimaging workflow for rigorous, reproducible, and FAIR neuroimaging." (/about/)
- "Here, we use the term scientific reproducibility in general to mean re-executability , the ability to obtain the exact same results when the same data is analyzed using the exact same analysis methods." (/about/why/)
- "ReproNim provides the tools and best practices for using standards, annotating data and workflows and recording provenance, implementing version control and using containers ( the 4 actions ) to put these principles into practice." (/about/repronim-approach/)

### 6. Confidence

- Read in full: all 21 pages in the saved text (about, why, principles and its four sub-pages, approach, collaborators, EAB, publications, fellowship, home, news, participate, getting started, tools, ReproLake, training, resources, pond-lake tutorial). Directly taken from the text: the mission, principles, tools lists, project structure, and fellowship figures.
- The publication list was read quickly and not analyzed per item.
- Grant facts come from the RePORTER API, not the site. The funding-period interpretation (start 2016-04-15, end 2031-06-30) is the API's record. How it maps to the site's "Phase 2, 2021-2026" is not known.
- The saved text omits images and figures (the principles and approach figures are referenced but not described), and the "5 Steps" page was not among those read.
- No webinar, blog, or news content was read.

### Gaps

- No measure of whether ReproNim improves reproducibility in the field. There are no adoption counts for tools (BIDS and DataLad are widely used, but the site gives no numbers), no outcome evaluations, and no comparison against a baseline.
- No description of what Technology and Research Development projects (TRDs) are, who leads them, or how they map to the tools. Phase-2 CP/SP lists are given, but not the work plan or aims.
- No statement of current-phase goals, milestones, or plans beyond "2021-2026" and a 2027 fellowship restart. The grant end year (2031) is not mentioned on the site, and the funding amount is not on the site.
- No discussion of limits of the approach, cost and burden to adopters, or failure cases. No stated criteria for "reproducible" beyond re-executability, and no way to check compliance (STAMPED has a checklist, but its adoption is not reported).
- Governance: how CPs and SPs are chosen, what the EAB reviews, and whether its recommendations were acted on are not described.
- Sustainability: how tools and ReproLake (hosted on a commercial Stardog endpoint) will be maintained after funding.
- Relationship between the older "5 Steps" and the current four principles is stated but the mapping is not shown.

## Relevance to this project (repo-context agent)

1. **Tier**: HIGH. It is the target community and the home of the Phase 3 TRDs. Its self-description is the baseline against which any RCI contribution must be framed. Only the site summary was used; TRD plans were not seen.

2. **ReproNim through the RCI lens** (every mapping below is my inference, not ReproNim's claim)

(a) Mapping onto map.md:
- **Step 1:** Neurobagel and ReproLake (queryable BIDS/NIDM metadata), the ReproInventory catalog.
- **Step 3:** principle 1 (planning 1a-1e, including pre-registration). Training and the fellowship feed this step.
- **Step 4:** most of the toolset: BIDS, DataLad, containers, Neurodocker, ReproIn/HeuDiConv, ReproSchema, and the "4 actions" (standards, provenance, version control, containers).
- **Step 5:** only partly covered. "Re-executability" is the stated bar, and the OHBM challenge and Hodge et al. 2021 are re-execution studies. Compliance checking is not described, and there is no "ReproScore" on the site.
- **Step 6:** principle 4 (publish everything, FAIR) and ReproLake. This shares objects but keeps the gate model.
- **Step 2:** only the metadata that trust could be computed from (provenance).
- **Missing edges:** none are claimed. 5 -> 2 and 6 as a state are absent. Use as load is absent; ReproLake could host it but no usage counts are reported.
- **Community activities:** fellowship, training modules, First Fridays, office hours, CP/SP structure, EAB.

(b) Engelbart levels (via notes/engelbart.md; A/B/C is from the Institute page, not 1962):
- **B (improving the work):** nearly everything above, i.e. tools, standards, and principles.
- **C (improving how the community improves):** fellowship (train-the-trainer), CP/SP technology-driver/testbed structure, EAB, and STAMPED as a self-improving checklist. All are thin. Nothing measures whether B-level tools improved.

(c) NIC test (bryk.md): partial. ReproNim has a hub, a shared problem, shared framework and norms, and CPs/SPs as testbeds. The site gives no shared outcome measures, no tests-of-change cycles, no variation analysis, and no evidence of learning across sites. This is a hub-led standards and training center, not yet a NIC.

(d) Uncovered by the self-description: step 2 (trust), step 5 beyond re-run, 5 -> 2, 6 as a state, load, and allocation. It also shows no adoption or impact evaluation and no failure cases.

3. **Loop step(s)**: Step 4 and the adjacent steps (3, 6), plus norms through the principles. The loop as a whole, as a C-level question.

4. **What it gives this project**: A concrete B-level substrate (provenance, containers, queryable metadata) that makes steps 2 and 5 cheaper. Natural hooks for the "use as load" edge in ReproLake and Neurobagel. A real community with training channels. The site also cites STAMPED and calls it a generalization of YODA.

5. **Where it stops**: The site is promotional. It has no impact data and no limits discussion. Governance is undescribed. The TRD content is invisible. "Reproducible" means re-executable only. The site states nothing about AI.

6. **Bearing on repo claims**:
   - stamped.md, "Necessary, not sufficient": supported. The site itself says re-executability is only a first step.
   - map.md, step 4 "Provenance partial, environment unrecorded": ReproNim is the counter-program, but there is no adoption data.
   - cases.md TODO, an OpenNeuro reuse chain: ReproLake and OpenNeuro are candidate sites for checking whether load is visible.

7. **Links to existing entries**:
   - Bryk and Engelbart: NIC and B/C levels.
   - Hardt: shared protocol in place of artifact inspection, comparable to a standing default.
   - OHBM OSSIG challenge: the live step-5 mechanism.
   - Mycelium and Neurosynth Compose: neighbouring provenance substrate.

8. **One-line take**: ReproNim is a strong B-level substrate with thin C-level machinery, and it leaves steps 2 and 5, the 5 -> 2 edge and load unaddressed.

9. **Confidence**: The facts come from the summary. The mappings, the B/C classification, and the NIC verdict are my inference. The site pages for the TRDs, the "5 Steps", and the webinar content were not read. The Phase 2 end date (2026) conflicts with the RePORTER end date (2031).
