# Handoff — 2026-10-16

From a claude.ai chat session (mobile) to Claude Code in asmacdo/RCI-explorer.
Self-contained: read this, then `CLAUDE.md`, then `docs/`.

## Where we are

- One conversation distilled into a seed repo. Nothing in `docs/` is verified against
  sources; it is a model to be tested, not findings.
- Full turn-by-turn record: `docs/session-2026-10-16.md`.
- Stance and working style: `CLAUDE.md`. Descriptive first; rigor is a community property;
  don't pick an objective, name the axes; top map vague enough to be true, ambiguity
  explicit; substrate → critics → generators.
- The loop and its missing edges: `docs/map.md`.
- STAMPED's role, spectrum, and the allocation question: `docs/stamped.md`.
- Cases incl. the lee3j Goodhart exhibit and the spec-balancing questions: `docs/cases.md`.
- Bibliography: `sources/ANNOTATED_BIB.md` (with cross-cutting synthesis) and `sources/STRETCH_ANNOTATED_BIB.md`; agent-generated, unreviewed, no source read by a human yet.
- AI-in-the-loop table (all TODO): `docs/ai-in-the-loop.md`.

## Immediate next steps (see TODO.md)

1. Review the agent bibliography; read the high-tier sources.
2. Trace real cases through the loop; stretch the map.
3. Evidence for AI already in the loop.

## Repo mechanics

- Large files are in git-annex; `git annex get <file>` fetches from the registered web URL.
- The chat session could not push (no Claude GitHub App on the asmacdo org). Install it
  if future cloud sessions should push directly.
