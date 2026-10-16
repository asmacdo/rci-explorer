# ARC Prize Foundation, ARC-AGI-3 (2026)

Status: agent-generated 2026-10-16, not yet reviewed by a human.
The summary agent had no project context; the relevance agent read the repo plus that summary.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### 1. Citation

- ARC Prize Foundation. *ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence* (technical report), dated April 22, 2026, 23 pages. https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf. The author is the "ARC Prize Foundation". The report lists a development team: lead environment designer Hunter Henry; engineers David Wexler and Derek Smith; Gregory Kamradt (president); Mike Knoop (co-founder); Francois Chollet (benchmark designer, co-founder). I found no arXiv entry for it.
- Benchmark page: https://arcprize.org/arc-agi/3 (page copyright 2026; no release date on the page).
- Chollet, F. (2019). *On the Measure of Intelligence*. arXiv:1911.01547 [cs.AI], submitted 5 Nov 2019, latest version v2 revised 25 Nov 2019.
- Per the report: ARC-AGI-2 launched March 2025. ARC Prize 2024 and 2025 competitions ran on ARC-AGI-1 and ARC-AGI-2 respectively. The ARC Prize Foundation was co-founded by Mike Knoop and Chollet.
- Secondary source only (not verified): a blog post (lilting.ch) gives a release date of March 24, 2026. The report's abstract says frontier scores were "as of March 2026".

### 2. Summary

ARC-AGI-3 is an interactive benchmark of novel, abstract, turn-based game environments. An agent gets no instructions, rules or stated goals. It must explore, infer the goal, build a model of the environment's dynamics, and plan actions. The tasks avoid language and external knowledge and rely only on Core Knowledge priors such as objectness. ARC-AGI-1 (2019) and ARC-AGI-2 (March 2025) were static grid tasks where the test taker infers a rule from a few input-output examples. ARC-AGI-3 instead measures action efficiency, meaning the number of moves needed to solve an environment on first contact. Scoring is called RHAE (Relative Human Action Efficiency). It compares per-level action counts to a human baseline (the upper-median best human), caps credit at 1.15x human efficiency, and squares the efficiency term.

On overfitting, the report says the private set is intentionally out-of-distribution from the public demo set. It has 25 public, 55 semi-private (for testing API models) and 55 fully private (for the competition) environments. The public set is meant as a demonstration and does not cover the private set's mechanics. The official leaderboard does not use task-specific harnesses.

History from the report: ARC-AGI-1 resisted pretraining scaling until OpenAI's o1 and o3 reasoning models showed non-zero performance. Test-time training reached 53.5% on the private ARC-AGI-1 set in the ARC Prize 2024 competition. In ARC Prize 2025 on ARC-AGI-2, the winner (NVIDIA's NVARC team) scored 24%. The report states humans solve 100% of ARC-AGI-3 environments while frontier AI scored below 1% as of March 2026.

### 3. Design principles

- **Novelty, no prior knowledge.** Environments use only Core Knowledge priors, with no language and no pre-loaded knowledge or hidden prompts.
- **Held-out private sets, deliberately out-of-distribution.** The private set has limited mechanic overlap with the public set. The public set is a demo, not a training resource, and the public-to-private ratio is inverted relative to ARC-AGI-2's roughly 10:1.
- **Human calibration.** Every environment is tested on human test-takers so it stays solvable. Scoring is anchored to a human action baseline rather than binary pass/fail.
- **Efficiency scoring that resists brute force.** Per-level action efficiency is squared, so wasteful solutions are penalized. A random-policy acceptance check requires that random play not solve a level more than 1 time in 10,000.
- **No harness on the official leaderboard.** The report argues that hand-built, task-specific harnesses inflate scores without measuring general ability. It notes that a hand-crafted harness lifted one model from 0.0% to 97.1% on one environment.
- **Expect to be superseded.** The report frames the series as measuring a moving "residual gap" to human-level AGI, so new versions are needed as capabilities advance.
- **Generated-task contamination.** The report argues ARC-AGI-1 and -2 are verifiable and so can be attacked by generating many similar tasks and training on them. It cites a Gemini 3 Deep Think reasoning trace that used the correct ARC color mapping without being told it. This motivates the out-of-distribution private set.

### 4. Confidence

- **Verified from the technical report PDF (read via pdftotext):**
  - Abstract, team list and date.
  - Lineage details (the ARC-AGI-1 and 2 descriptions, the 2020 Kaggle, 2024 and 2025 competitions, and their scores).
  - Dataset sizes and the public/private design.
  - RHAE scoring (upper-median human baseline, 1.15 cap, squaring).
  - The harness policy and the random-policy threshold.
  - The overfitting argument.
- **Verified from arcprize.org/arc-agi/3:**
  - Interactive format and the 100% score definition.
  - The "no pre-loaded knowledge or hidden prompts" and "novelty that prevents brute-force memorization" language.
  - The link to the technical report.
  - The page itself gives no authors, scores or release date.
- **Verified from arxiv.org/abs/1911.01547:** title, author, id and dates.
- **Not verified:**
  - The March 24, 2026 release date (blog only).
  - Any specific leaderboard model scores. A search snippet gave sub-1% figures for GPT-5.4, Gemini 3.1 Pro and Claude Opus 4.6, but that snapshot is undated and secondary, so I did not use it.
  - I did not read the report's full results section, so the "below 1%" figure comes from the abstract only.
  - I did not verify the ARC-AGI-1 o3 score history (for example the high o3 scores in late 2024) from a primary source. The report says only that o1 and o3 first showed non-zero fluid reasoning on ARC-AGI-1.
- No quotes are invented. The short quoted phrases come from the fetched pages and PDF.

## Relevance to this project (repo-context agent)

1. **Tier**: STRETCH. ARC-AGI-3 is a design for a capability benchmark on toy games. It has no science content, so it informs the "benchmarks as verifiers" angle only by analogy.

2. **Loop step(s)**: Trust and allocation, only by analogy. The report is about how a score is built to resist gaming. It does not touch steps 1-6 directly. The nearest tie is to how the project treats autonomous-science benchmarks, which sit at the generator stage (step 4, "substrate → critics → generators").

3. **What it gives this project**:
- A worked case of Goodhart defenses in a benchmark, which can sit beside the lee3j exhibit. The defenses are a held-out private set that is deliberately out-of-distribution, a squared efficiency term, a random-policy acceptance check (at most 1 in 10,000), and no task-specific harness on the official leaderboard.
- The harness figure (0.0% to 97.1% on one environment, per the summary) shows that scaffolding can move a score more than capability does. This is the "ran is not right" and imitation point in `docs/ai-in-the-loop.md`.
- The generated-task contamination argument says a verifiable task family can be attacked by generating many similar tasks and training on them. That is a mechanism for "a capable agent will do to [a benchmark] what this one did to STAMPED."
- The human-baseline anchor (upper-median human, 1.15x cap) shows a benchmark that scores efficiency rather than pass/fail, which is one way to encode a trade-off rather than a single axis.

4. **Where it stops**:
- It has no cost-of-verification, load or dependency accounting.
- Tasks have a crisp, internal win condition, so there is no analogue of a semi-trusted body of prior results.
- It says nothing about who audits the benchmark itself, or about retirement and re-checking.
- The report is by the benchmark's own authors. Its claim that humans solve 100% and AI scores below 1% is self-reported and unreplicated.

5. **Bearing on repo claims**:
- `docs/cases.md`: "any benchmark for autonomous science is a scalar". This is complicated. ARC-AGI-3 is a scalar (RHAE) that has deliberately added anti-gaming structure, so the claim is true but not the whole story.
- `docs/ai-in-the-loop.md`: "no verifier exists the way math has one." The report's point that ARC-1 and ARC-2 were verifiable and therefore attackable supports a tension the project has not named: having a verifier invites optimization against it.
- `CLAUDE.md`: "End-to-end autonomous-agent benchmarks start at step three." Weakly supported. ARC-AGI-3 is an end-to-end agent benchmark, and it keeps the verifier by using toy domains.
- `docs/prior-art.md` cross-cutting point 1 ("No source covers verification allocation"): unaffected.
- Points 2 and 3 (5 → 2 attribution; auditability is constitutive): unaffected.

6. **Links to existing entries**:
- Popper: held-out private tasks work like a severe test that cannot be tuned to in advance.
- Ioannidis: both are about selective filters and what gets reported, and held-out tests resist that.
- OSC: both measure whether a claimed result survives a fresh run, though the domains differ.
- Kitcher: no real connection.

7. **One-line take**: A well-built Goodhart-resistant benchmark on toy tasks: useful design analogy for benchmarks-as-verifiers, silent on verification cost, allocation and real science.

8. **Confidence**:
- Rests on the summary: the RHAE details, set sizes, the harness figure, the random-policy threshold, the contamination argument, and the claim that frontier AI scored below 1% (taken from the abstract only).
- Rests on my background knowledge: ARC-AGI-1/2 history and Chollet's 2019 framing of skill-acquisition efficiency. I have not re-verified these, and the summary did not cover Chollet 2019 in depth.
- My own inference: the Goodhart parallel to lee3j, the "verifier invites attack" tension, and the Popper and Ioannidis links. These are plausible but unchecked, and the links are loose.
