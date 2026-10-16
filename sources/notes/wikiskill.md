# Tang et al., "WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution" (2026)

Status: agent-generated 2026-10-16, not yet reviewed by a human.
The summary agent had no project context; the relevance agent read the repo plus that summary.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### 1. Citation

Tang, Liyan; Rashtchian, Cyrus; Ferng, Chun-Sung; Tomkins, Andrew; Juan, Da-Cheng; Vu, Tu (Google Research; Vu also Virginia Tech). 2026. "WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution." arXiv:2608.27454 [cs.AI] (secondary: cs.CL), v1, submitted 27 Aug 2026 (PDF header dated 2026-08-28). Preprint, no venue stated. License: CC BY 4.0 (per the arXiv abstract page; the PDF footer says "© 2026 Google. All rights reserved", so the two notices differ). DOI: https://doi.org/10.48550/arXiv.2608.27454. URL: https://arxiv.org/abs/2608.27454

### 2. Summary

The paper argues that insights guiding automated skill development are usually scattered across optimization histories, and that keeping them in a separate, persistent knowledge base improves skill evolution. WikiSkill organizes the agent workspace into three layers: immutable raw execution traces, a wiki of markdown "pattern" pages with an evolution log and a skill-impact tracker, and the active skills. Each iteration has four steps. An inference agent runs the training tasks with the current skills. A Wiki Maintainer agent turns up to 8 sampled traces into wiki updates. A ReAct-style Skill Proposer reads the wiki and traces and proposes one skill create or patch. A gate keeps the change only if validation score strictly improves. Skills roll back on rejection, but the wiki never does. Evaluation covers five benchmarks (LiveMathematicianBench, SealQA, SpreadsheetBench, OfficeQA, ALFWorld) and five models (Qwen3.5-4B and 9B, Qwen3.6-27B, Gemma-4-31B, Gemini-3.5-Flash), compared with no skills and with Trace2Skill, EvoSkill and SkillOpt. WikiSkill has the best average for every model (for example 68.1 vs 56.1 for the best baseline on Gemini-3.5-Flash). The authors also report that gains grow with model size, that skills transfer across models (sometimes beating self-evolved skills), and that removing wiki access for the proposer lowers the Gemini-3.5-Flash average from 63.7 to 48.7. They state limitations around retrieval, strict gating, wiki pruning and long-horizon tasks.

### 3. Key concepts

- **Three-layer architecture**: Raw Layer (raw/, write-once execution traces), Wiki Layer (wiki/, compounding structured knowledge, never reset), Skill Layer (skills/, reversible procedural knowledge; each skill has SKILL.md plus PURPOSE.md linking it to the wiki patterns that motivated it).
- **Wiki patterns and logs**: markdown pages in wiki/patterns/ documenting a failure mode or successful strategy with workarounds; index.md catalogs them; logs.md is a chronological evolution log written by the Wiki Maintainer.
- **skill-impact.md**: an audit trail written by the outer-loop harness, not an LLM. It records each proposal's diff, target skill, validation score and Accepted or Rejected outcome, so the proposer avoids repeating rejected changes.
- **Wiki Maintainer / Skill Proposer**: the maintainer does root-cause analysis on sampled failing and passing traces (at most 5 failing and 3 passing) and patch-edits the wiki. The proposer reads the wiki index and impact tracker, then pulls specific patterns and traces on demand with read_file. It must read at least 4 traces and emits one atomic proposal.
- **Gating and rollback (skills only)**: a candidate skill set is kept only if validation score is strictly greater than the best so far. The wiki persists regardless of the decision.
- **Wiki access ablation / full-injection**: the inference agent has no wiki access during training rollouts (default). Active skills are injected in full into the system prompt, so skill retrieval is not tested.

### 4. Evidence quality

- **Demonstrated (within the setup)**: Table 1 gives per-benchmark test scores for all method-model pairs. Each score averages 3 independent full evolution runs, with paired bootstrap tests (1,000 iterations, p < 0.05) used to mark bold best-tier entries. Splits and toolsets are said to match EvoSkill and SkillOpt. Test sets are small (LiveMath 124, SealQA 85, SpreadSheet 280, OfficeQA 172, ALFWorld 134), and train and validation sets are tiny (for example SealQA 16 train and 10 val; LiveMath 35 and 18). The authors acknowledge that small validation sets add noise to gating.
- **Not uniformly shown**: the claim of "consistent" wins is mixed in the tables. Per benchmark, WikiSkill is not best everywhere. For example, Qwen-3.5-4B on OfficeQA is below no-skill (28.5 vs 30.2), and Qwen-3.5-9B on LiveMath and SpreadSheet is below EvoSkill. Results are averages over 3 runs with no variance or confidence intervals reported in the tables. Gemini-3.5-Flash ALFWorld is identical across methods (85.9) because validation was already 100%, which inflates the "average" comparisons slightly in the other direction (a tie, not a win).
- **Ablation (Table 3) is narrow**: one model (Gemini-3.5-Flash), four benchmarks (ALFWorld omitted), unspecified number of runs. Removing proposer wiki access also removes the Wiki Maintainer, so it tests the whole wiki mechanism, not individual parts like logs versus patterns versus the impact tracker. The explanation for why wiki access hurts the inference agent is labeled a hypothesis. No tests isolate the skill-impact audit trail.
- **Stated limitations**: skills are fully injected, so retrieval and triggering are untested; strict improvement gating excludes neutral steps; no automated wiki pruning; no very long-horizon tasks. Cost: optimizer calls per iteration are 1 + T_ReAct (roughly 10 to 20 turns), which the authors say may cost more on some datasets; no measured dollar or token costs are given. Cross-model transfer claims and the "discovery vs. execution" interpretation rest on trajectory analysis described in prose, not controlled experiments. Baseline comparison uses the authors' own reimplementation or runs of EvoSkill, SkillOpt and Trace2Skill; the paper says EvoSkill and SkillOpt do best with minibatches, while WikiSkill uses full-batch.

### 5. Confidence

- **Taken directly from the text**: authors, affiliations, dates, arXiv id, license (abstract page); architecture, loop, gating rule, Algorithm 1 (Sections 2, 3, Appendix A); benchmarks, splits, models, baselines, 3-run averaging and bootstrap procedure (Sections 4.1 and 4.2, Appendices B and C); all numbers in Tables 1 to 4 and the figures quoted in the Summary (Sections 4.2, 5.1, 5.2); limitations (Limitations section); optimizer call complexity (Appendix D); prompts (Appendix E).
- **Mild inference by me**: that the 3-run averages lack reported variance (I saw no spread in Tables 1 to 3, and none in the text I read); that the ablation number of runs is unspecified (the text I read does not state it, though Section 4.2 says all reported scores average three runs, so the ablation may also); that the 4B OfficeQA and 9B EvoSkill comparisons undercut a blanket "consistent" claim (read off Table 1). The "Evidence quality" bullets on small split sizes are my judgment applied to Table 6 numbers.
- **Not checked**: no external verification of the cited baselines, benchmarks, or whether code or prompts are released beyond what the paper shows. No direct quotes beyond the paper's own phrasing are used above.

## Relevance to this project (repo-context agent)

1. **Tier**: STRETCH. It is an agent self-improvement system, not about science's verification, trust or allocation. Its one on-point piece is a strict score-gate that accepts or rolls back changes.

2. **Loop step(s)**: Weakly step 4 (agent-produced procedural knowledge, i.e. skills). Gate-plus-rollback is a toy step-5 analogue. "Trust" only by analogy (impact tracker as per-proposal accept/reject record). Nothing on steps 1, 2, 3 or 6.

3. **What it gives this project**:
- A concrete worked instance of the "find the loop with a verifier and iterate there" claim in `docs/ai-in-the-loop.md`. The verifier is a held-out validation score.
- A mechanism split: skills are gated and reversible, while the wiki is ungated and never rolls back. That is a small example of different trust levels for different artifact layers.
- `skill-impact.md` is written by the harness, not an LLM, so the audit trail is not model-authored. This echoes the project's machine-auditable and "capture as side effect" language in `docs/stamped.md`.
- Raw traces are immutable and each skill links to its motivating patterns (PURPOSE.md). That is provenance by construction.
- Small gating sets (SealQA 16 train, 10 val) per the summary. Gate noise is an exhibit for "the grader may be lying."

4. **Where it stops**: The only verifier is a benchmark validation score, so Goodharting is unexamined. There is no human or community in the loop, no cost-of-verification accounting (dollar and token costs are unreported), no allocation of checking effort, no dependency or load notion, and no attribution of failure to a source. The ungated wiki is exactly the unverified accumulating knowledge the project worries about. The paper reports no wiki quality audit.

5. **Bearing on repo claims**:
- Supports (weakly) `docs/ai-in-the-loop.md`: "find the loop with a verifier and iterate there."
- Complicates `docs/cases.md` Goodhart exhibit ("any benchmark for autonomous science is a scalar"). Here the scalar gate works across five tasks, but those tasks have cheap, crisp scorers, unlike science.
- Complicates `docs/stamped.md` "Contingent benefit" and the sequencing claim "substrate → critics → generators". This system builds a generator-plus-gate directly, though at skill scale.
- Touches `docs/map.md` "5 → 2 ... needs an attribution rule". The impact tracker records which proposal caused which score change (credit assignment by design, one atomic change per iteration). That works only because changes are single and isolated. It does not carry over to the body of science.
- Does not touch the cross-cutting points "no source covers verification allocation" or "auditability is constitutive." Its audit trail is instrumental, which if anything weakly supports the instrumental reading.

6. **Links to existing entries**:
- Popper: the gate is a crude severe-test and keep-if-it-survives rule, with no severity concept.
- Lakatos: progressive versus degenerating programme resembles the accept/reject history, but only loosely.
- Kitcher: none real.

7. **One-line take**: A tidy example of a verifier-gated AI loop with a harness-written audit log; adjacent tooling, silent on science-scale trust or allocation.

8. **Confidence**:
- Rests on the summary: architecture, gate rule, impact tracker, small split sizes, benchmarks, mixed per-benchmark results. I did not read the paper.
- Rests on my background knowledge: Goodhart risk on small validation sets; the general pattern of verifier-gated self-improvement.
- My own inference (guesses): the wiki-versus-skill trust-layer parallel; the claim that credit assignment works only because changes are atomic; STRETCH versus HIGH is a judgment call.
