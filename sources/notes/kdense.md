# K-Dense AI, Scientific Agent Skills (2026)

Status: agent-generated 2026-10-16, not yet reviewed by a human.
The summary agent had no project context; the relevance agent read the repo plus that summary.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### 1. Citation

- Repo: K-Dense-AI/scientific-agent-skills, https://github.com/K-Dense-AI/scientific-agent-skills (formerly "Claude Scientific Skills"). Org: K-Dense (K-Dense-AI).
- License: MIT for the repo. Each skill also carries its own `license` field in its SKILL.md, which may differ. The docx/pdf/pptx/xlsx skills were vendored from anthropics/skills and removed in v2.72.0.
- Size: the README claims 177 skills (version badge 2.72.0) and 100+ scientific databases. The paper counts 163 skills across 16 areas, so the two counts differ, probably because the repo grew after the paper.
- Paper: Kassis, Agarwal, He, Patel, Brueckner, "Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents", arXiv:2609.00065 (cs.CL), v1 30 Aug 2026, v2 2 Sep 2026. The repo ships a CITATION.cff.
- Format it builds on: Agent Skills, https://agentskills.io/. Anthropic originally developed it and released it as an open standard, and many agent products have adopted it.

### 2. Summary

The repo is a library of "skills" that give coding or research agents field-specific procedures for scientific work. Domains include bioinformatics and genomics, cheminformatics and drug discovery, proteomics, clinical research, medical imaging and microscopy, neuroscience, machine learning, materials science, physics and simulation, geospatial science, lab automation, research methodology and regulatory standards, and scientific communication. Many skills wrap specific Python packages or databases. The "Database Lookup" skill documents 80 databases.

Structure follows the Agent Skills format. A skill is a folder with a required `SKILL.md` (YAML frontmatter with at least `name` and `description`, then instructions). It can also hold `scripts/`, `references/` and `assets/`. Agents load skills in three stages: only name and description at startup, the full SKILL.md when a task matches, and bundled files or code on demand. K-Dense's frontmatter also carries a quoted `metadata.version`. The repo root has a `plugin.json`, a `skills/` directory and an `AGENTS.md` with frontmatter rules.

Quality control is mostly structural. A `tests/_meta` guard checks the skill contract, coverage, the plugin.json schema and version sync with pyproject. Skills that ship scripts have tests under `tests/<skill-name>/`. CI runs the contract and standard-library-only suites. The full scientific-dependency sweep is not run in CI. Skills are scanned weekly with the Cisco AI Defense Skill Scanner, with results in `docs/security-report.md`. Versioning is per skill plus repo release tags, and installs can be pinned to a tag or SHA. The paper evaluates only documentation size (context cost), not task performance.

### 3. Validation and trust

- There is no task-level evaluation in the paper. The authors report no measurement of whether an agent picks the right skill or gets correct scientific results. Their only reported numbers are context cost: descriptions of all 163 skills use 7.1% of a 200k-token window, the median workflow uses 23.9%, and 29 of 46 workflows would overflow if every reference file loaded.
- Repo tests cover structure (frontmatter, schema, version sync) and script behavior for skills that ship scripts. They do not check that a skill's scientific advice is correct. The README itself says local tests, live-service checks and illustrative examples have different coverage.
- Provenance and review are asserted, not demonstrated. K-Dense-authored skills went through internal review, and community contributions were reviewed "to the best of our ability". The README tells users to review skills before installing. Security scanning (Cisco Skill Scanner, weekly) targets malicious or unsafe content, not correctness.
- The README links blog posts reporting benchmarks (a 250-run pyOpenMS study, a 98-run lab-hardware-cad evaluation). I did not read these or verify their figures, and they are not part of the repo's tests. Treat them as vendor-reported.

### 4. Confidence

- Verified from https://github.com/K-Dense-AI/scientific-agent-skills (WebFetch summary, first 100,000 of about 108,900 characters): license, 177-skill claim, version 2.72.0, domains, structure, tests, CI, Cisco scan, versioning, provenance statements, blog benchmark mentions, citation pointer. The summary came through a small model, and I did not read the last ~8,900 characters or the raw repo files (tests, AGENTS.md, skills).
- Verified from https://arxiv.org/abs/2609.00065 (abstract page only): title, authors, dates, 163 skills / 16 areas, and the context-cost numbers and "no task-level evaluation" statement. I did not read the full paper.
- Verified from https://agentskills.io/: the SKILL.md folder format, optional directories, progressive disclosure, Anthropic origin, open standard. I did not fetch the full specification page, so the exact frontmatter field rules are not confirmed here.
- Inferred: the 177 vs 163 discrepancy is likely repo growth after the paper. Star and fork counts from the page (51.3k stars, 4.5k forks) were seen but are not needed and may change.

## Relevance to this project (repo-context agent)

1. **Tier**: STRETCH. It is tooling and packaging of procedural knowledge for agents. The summary reports no task-level evaluation, no correctness checking and no verification allocation, only structural tests and context-cost numbers.

2. **Loop step(s)**: 4 (execute), because skills are procedures that agents run to produce research objects. Weakly "trust", because the summary's validation section shows how an agent-facing artifact is vetted.

3. **What it gives this project**:
- A real-world exhibit of the "spec names one axis" pattern. Skills encode procedure, and the repo's quality gates (frontmatter, schema, version sync, security scan) are cheap static checks of the kind `docs/stamped.md` calls a grader.
- Evidence that static gates and scientific correctness are decoupled. The summary reports tests for structure and script behavior, not for scientific advice. This is a vendor-side instance of "grade statically, re-execute a sample, track the gap", with the gap unmeasured.
- A possible substrate component: versioned, SHA-pinnable, per-skill-licensed procedure bundles are STAMPED-adjacent (pinned procedure as part of the environment record at step 4).
- Progressive disclosure (name and description, then full text, then files) as a cost-control design for critic agents.

4. **Where it stops**: No task-level evaluation of correctness (the authors say so), no per-claim provenance, no load or dependency signal, no re-check allocation, no attribution when a skill gives wrong advice (5 → 2). The vendor benchmarks the summary mentions were unread. Review is asserted ("to the best of our ability").

5. **Bearing on repo claims**:
- `docs/ai-in-the-loop.md` row "4 Execute | AI-generated analysis code | Provenance unrecorded; environment unpinned": partially complicates it. Skills add pinning at the procedure level, but the summary shows nothing about recording which skill version an analysis ran under.
- `docs/ai-in-the-loop.md` "no verifier exists the way math has one": supports it. Nothing here supplies one.
- `docs/stamped.md` "Reproducible ≠ rigorous; keep the scores separate": supports it. Passing the contract tests says nothing about scientific correctness.
- `docs/prior-art.md` cross-cutting 1 ("no source covers verification allocation"): consistent, no counterexample, but this source is not on that topic.
- `docs/cases.md` lee3j case: weak analogy. A skill that points agents to standard libraries would be the "constrain obvious failure modes" spec, but nothing in the summary shows that.
- Cross-cutting 3 (auditability constitutive): no support.

6. **Links to existing entries**:
- Ioannidis and OSC: only as a reminder that unmeasured correctness is the default. The link is thin.
- No real connection to the other nine.

7. **One-line take**: Agent-skill libraries package procedures with structural QA but no correctness evaluation, so they are substrate for step 4, not evidence on verification.

8. **Confidence**:
- Rests on the summary: all repo facts, the absence of task-level evaluation, the context-cost numbers. The summary itself is a small-model web summary, partly unverified (last ~8,900 characters unread, paper abstract only, blog benchmarks unread).
- Rests on my background knowledge: Agent Skills is Anthropic's open format. I cannot independently confirm the 2026 paper or repo details.
- My inference (guesses): that skills would suit a "standard libraries" spec for the lee3j case; that versioned skills could be recorded in provenance. Neither is stated in the summary. The tier call rests on absence of evidence in a summary that did not read the paper body.
