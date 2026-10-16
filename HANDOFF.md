# Handoff

Self-contained: read this, then `CLAUDE.md`, then `sources/ANNOTATED_BIB.md`, then `docs/`.

## What this is

A map of science as a recursive community improvement (RCI) loop, to see where AI and STAMPED can make it more rigorous and faster.
Thesis: science already is a working self-improving loop of humans, institutions and tools; single-AI recursive self-improvement (RSI) is unnecessary for better science; improve the existing loop instead.
Stance and working rules: `CLAUDE.md`.

## State

- **Model** (`docs/`): the 6-step loop with its missing edges (`map.md`), STAMPED's role (`stamped.md`), cases incl. the lee3j Goodhart exhibit (`cases.md`), AI-in-the-loop table, all TODO (`ai-in-the-loop.md`).
  All of it is our model, not observation; nothing has been traced through a real case yet.
  Session summaries: `docs/session-2026-10-16.md` (the original chat) and `docs/session-2026-10-16-lit-review.md` (this bibliography work).
- **Bibliography** (`sources/`): 31 notes (one covers a batch of six tools), each with a context-free agent summary and a repo-aware agent relevance report in `sources/notes/`.
  `ANNOTATED_BIB.md` (high tier, 16 entries, plus 13 cross-cutting points) and `STRETCH_ANNOTATED_BIB.md` (the rest).
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

## Decisions waiting on the project lead

These are positioning calls about the thesis, deliberately not made by an agent (also in `TODO.md`):

1. How to position RCI against Engelbart / Drexler / Nielsen & Qiu / Bryk (cross-cutting 10).
2. Whether "already works" survives, or splits into "the research loop runs; the loop that changes the loop is slow" (11).
3. Humans as constituents of the loop or as overseers of it (13).
4. Mycelium's tier (agent said STRETCH; placed in the high tier pending your call).

## Next steps

1. Review the bibliography; read the high-tier sources, starting with Hardt and Engelbart.
2. Trace real cases through the loop (candidates in cross-cutting 9: OHBM OSSIG challenge, Brain Researcher's sign-blind error, Darwin Gödel Machine App. H, Meisler).
3. Evidence for AI already in the loop (`docs/ai-in-the-loop.md`).

## Repo mechanics

- Remotes: `origin` (GitHub, public; no annex content) and `hub-con` (hub.centerforopenneuroscience.org, private; holds annex content).
  After pushing to hub-con, the server records receipts on its `git-annex` branch, so the next push may need `git annex merge` first.
- Large and binary files go in git-annex (`.gitattributes`); `git annex get <file>` fetches from hub-con or the registered URL.
- `gitignored/` is local only: ReproNim meeting notes (internal, never commit) and NotebookLM bundles (`gitignored/notebooklm/episode-NN-*/`, each with a `PROMPT.md`).
- Git is the history; files describe current state only.
