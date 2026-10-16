# Session 2026-10-16: first lit review (Claude Code)

Second session of the project, following the claude.ai chat in `session-2026-10-16.md`.
Driven by the project lead; the agent orchestrated Sonnet subagents and consolidated.

## Repo setup

- Imported the chat's seed bundle; its history was unrelated to the GitHub initial commit, so it was merged with `--allow-unrelated-histories`.
- Set up git-annex for originals and binaries, and `gitignored/` for local-only material.
- Added a second remote, `hub-con` (private, holds annex content); GitHub holds git only.
- Rule adopted: git is the history, files describe current state only.

## Bibliography, round 1: the seed reading list

- Eleven classics from the chat's list (Popper, Merton, Kitcher, Polanyi, Longino, Ioannidis, OSC 2015, Latour & Woolgar, Kuhn, Lakatos, Strevens).
- Method chosen by the project lead: per source, one agent with no project context writes a summary, a second agent with repo context assesses relevance; the orchestrator consolidates.
- Result: every relevance agent reported that no source covers allocating verification across the existing body of results; several seed one-line takes were corrected (e.g. Kitcher allocates exploration, not verification; Ioannidis is a model, not a measurement).

## Bibliography, round 2: ReproNim Phase 3 kickoff sources

- Sources pulled from the 2026-09-24 ReproNim AllCall notes (kept in `gitignored/`, never committed): Mycelium, Brain Researcher, WikiSkill, Hardt's benchmarks book (five agents by chapter group), ARC-AGI-3, Brain-Score, Terminal-Bench-Science, Jev, K-Dense skills, the Fleming metascience review, Meisler et al., and a tooling batch.
- Bibliography split into `ANNOTATED_BIB.md` (high) and `STRETCH_ANNOTATED_BIB.md`.
- New hypotheses: rankings, not scalars, may be the right shape for a trust score (Hardt); a verifier invites optimization against it; AI critics are cheap but measurably bounded (Hardt Ch 14, Brain Researcher).

## Bibliography, round 3: RSI and prior names for RCI

- The project lead's framing: RSI is unnecessary because science already is a working improvement loop; and "RCI" has probably been named before.
- Two scouting agents, then full treatment of Engelbart 1962, Bryk et al. NICs, Drexler 2019, Nielsen & Qiu 2022, Darwin Gödel Machine, Bloom/Park (high), Narayanan & Kapoor, Weston & Foerster (stretch).
- Result: the concept is not new (Engelbart's bootstrapping is closest; the A/B/C levels are later Institute material, not 1962); "already works" is contested; RSI works given a cheap verifier and then attacks it.
- These are recorded as cross-cutting points 10-13.

## Reframing (project lead)

- RCI is a design frame, the mental model of what we can build; RSI is out of scope rather than a rival; prior art is built on, not out-claimed.
- Practical goal: contributions to the ReproNim Phase 3 TRDs. RCI was arguably ReproNim's goal all along, half-unspoken; the term earns its place if it changes how the TRDs are thought about. Skills and autonomous agents are one part of a larger strategy still to be fleshed out.
- repronim.org added as a source and read through that lens (agent inference): strong B-level substrate, thin C-level machinery, no public measure of its own effect; steps 2 and 5, the 5 → 2 edge and load are not covered by the site.

## Other outputs

- NotebookLM bundle for "Episode 1: Getting Started with Lit Review" in `gitignored/notebooklm/`.
- `sources/method/`: the agent prompts and transcript extractor, so the pipeline can be rerun.
- `HANDOFF.md` rewritten; `how-to-pickup-handoff.md` added.

## Caveats carried forward

- Nothing in the bibliography has been read by a human.
- Roughly 60 subagent runs; each note keeps its agent's own confidence section, which is the only record of what was verified versus recalled.
