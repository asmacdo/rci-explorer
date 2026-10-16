# Handoff

Self-contained: read this, then `SOUL.md`, then `CLAUDE.md`, then `sources/ANNOTATED_BIB.md`, then `docs/`.

## What this is

Exploration of science, neuroimaging first, as a recursive community improvement (RCI) loop: some loop already exists, and we look for how AI and STAMPED could iterate on it.
What we are for, scope and how agents should think: `SOUL.md`. Working rules: `CLAUDE.md`.
Context: the project lead works on ReproNim TRD3; Phase 3 is the P41's last phase, but the community it serves outlives the grant. If something sharable emerges (e.g. for the TRDs), new goals follow; it is not the goal yet.

## State

- **Model** (`docs/`): the 6-step loop with its missing edges (`map.md`), STAMPED's role (`stamped.md`), cases incl. the lee3j Goodhart exhibit (`cases.md`), AI-in-the-loop table, all TODO (`ai-in-the-loop.md`).
  All of it is our model, not observation; nothing has been traced through a real case yet.
  Session summaries: `docs/session-2026-10-16.md` (the original chat) and `docs/session-2026-10-16-lit-review.md` (this bibliography work).
- **Bibliography** (`sources/`): 32 notes (one covers a batch of six tools; one is repronim.org itself), each with a context-free agent summary and a repo-aware agent relevance report in `sources/notes/`.
  `ANNOTATED_BIB.md` (high tier, 17 entries, plus 13 cross-cutting points) and `STRETCH_ANNOTATED_BIB.md` (the rest).
  **Unreviewed.** No human has read any source; summaries of the classics rest mostly on model background knowledge; read the confidence section of each note before relying on it.
  How it was made, and how to extend it: `sources/method/README.md`.
- **Originals**: `sources/originals/` in git-annex with web URLs registered; licenses in `MANIFEST.md`.
  Missing: Bryk et al. 2011 "Getting Ideas into Action" (Carnegie blocks scripted fetches; a manual download would let it be read in full).

## What the bibliography says (hypotheses, not findings)

The cross-cutting section of `sources/ANNOTATED_BIB.md` is the thing to read; the headline points:

- No source covers allocating verification across the existing body of results; that may be the project's actual contribution.
- RCI is not a new concept: Engelbart 1962 (bootstrapping), Drexler 2019 (systemic recursion in AI R&D), Nielsen & Qiu 2022 (metascience), Bryk NICs. The combination may be new.
- "Already works" is contested: Nielsen & Qiu (institutional stasis), Bloom/Park (diminishing returns, contested).
- RSI works where a cheap trusted verifier exists, and the verifier then gets attacked (Darwin Gödel Machine, lee3j, ARC-AGI-3).
- Hardt's benchmark book is the closest working model of community verification: rankings survive Goodhart, scalars do not.

## Decided by the project lead

- RCI is a frame for iterating on a loop that already exists, not a claim to defend against RSI; RSI is out of scope; prior art is built on, not out-claimed. Cross-cutting 10-12 remain useful as context.
- "Auditability is constitutive" is a working assumption (a definition of "rigorous"), not a finding.
- Open problems are named in `SOUL.md` and deliberately left open: measurement, Goodhart, scope, humans' role.

## Waiting on the project lead

- Mycelium's tier (agent said STRETCH; placed in the high tier pending your call).

## Next steps

Top down, per `SOUL.md`: how does science progress, and how could AI improve that?

1. Trace real cases through the loop to ground the model (candidates in cross-cutting 9: OHBM OSSIG challenge, Brain Researcher's sign-blind error, Darwin Gödel Machine App. H, Meisler).
2. Review the bibliography; read the high-tier sources, starting with Hardt and Engelbart.
3. Explore the measurement subproblem: how could the community tell whether it is improving, given an unknown baseline?
4. Evidence for AI already in the loop (`docs/ai-in-the-loop.md`).
5. If something sharable emerges, map it onto the TRD questions (benchmark suite, ReproScore, skill validation and trust, claim re-executability), TRD3 first.

## Repo mechanics

- Remotes: `origin` (GitHub, public; no annex content) and `hub-con` (hub.centerforopenneuroscience.org, private; holds annex content).
  After pushing to hub-con, the server records receipts on its `git-annex` branch, so if a push of `git-annex` is rejected, run `git fetch hub-con && git annex merge` and push again.
- Large and binary files go in git-annex (`.gitattributes`); `git annex get <file>` fetches from hub-con or the registered URL.
- `gitignored/` is local only: ReproNim meeting notes (internal, never commit) and NotebookLM bundles (`gitignored/notebooklm/episode-NN-*/`, each with a `PROMPT.md`).
- Git is the history; files describe current state only.
