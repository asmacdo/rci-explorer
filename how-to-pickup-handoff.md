# How to pick up and hand off

## Picking up

1. Read `HANDOFF.md`, then `CLAUDE.md`, then `sources/ANNOTATED_BIB.md` (cross-cutting section first).
2. Skim the latest `docs/session-*.md` for how the last session went; `git log` for detail.
3. Check `TODO.md` and the "Decisions waiting on the project lead" in `HANDOFF.md` before starting work that depends on them.
4. Need an original? `git annex get <file>` (from `hub-con`, or the registered web URL).

## Handing off

At the end of a session, or when asked to prepare a handoff:

1. **Write a session summary**: `docs/session-YYYY-MM-DD-<topic>.md`.
   What was done and decided, by whom (project lead vs agent), what was deliberately left undecided, caveats carried forward.
   Keep it short; link to files rather than restating them.
2. **Rewrite `HANDOFF.md`** to the current state: what exists, how trustworthy it is, decisions waiting on the project lead, next steps, repo mechanics.
   Current state only; no history (git and the session summaries hold that).
3. **Update `TODO.md`** and the layout in `CLAUDE.md` if files or directories changed.
4. **Commit and push** to `origin` and `hub-con` (`git annex copy --to hub-con` for new annexed content; if hub-con rejects the `git-annex` branch, `git fetch hub-con && git annex merge` and push again).
