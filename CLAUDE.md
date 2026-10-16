# science-loop

Mapping how science actually functions as a recursive community improvement loop, so
we can see where AI (and STAMPED) can make it more efficient, more rigorous, faster.

## Stance

- **Descriptive first.** Map what is actually happening before proposing what should.
- **Rigor is a community property.** Unauditable work may be careful; it is not rigorous
  from the community's perspective. Auditability is constitutive, not instrumental.
- **"Recursive Community Improvement"** — easier than RSI, includes humans, and already
  exists. The problem is to optimize it, not invent it.
- **The body of science is semi-trusted.** Building on it is either risky (no
  verification) or expensive (verification). Once mapped, this is a resource allocation
  problem — and allocation is distributed, not decided centrally.
- **Don't pick an objective.** Name the axes (propagated error, throughput,
  time-to-correction, human hours, cost) and show the trade-offs of each tuning. The
  weighting is a values choice that belongs to the community.
- **Top-level map stays vague enough to be true, with ambiguity explicit.** Lower layers
  must get concrete enough to be wrong. Test: could two people read it and allocate
  differently? If no one can disagree, it isn't a map yet.
- **Sequencing:** substrate (STAMPED) → critics (verifiers) → generators (autonomous
  scientists). End-to-end autonomous-agent benchmarks start at step three.

## Working style

- Terse, precise. Poke holes. Update with visible reasoning rather than capitulate.
- Every claim about "how science works" needs a real case or a citation. Our own model is
  not an observation.
- Keep `docs/map.md` as-is only. Proposals go in `docs/proposals/`.

## Layout

- `docs/map.md` — the loop, as-is, with missing/dashed edges called out
- `sources/ANNOTATED_BIB.md` — highly relevant sources + cross-cutting synthesis
- `sources/STRETCH_ANNOTATED_BIB.md` — adjacent, background, tooling sources
- `sources/notes/<source>.md` — per-source summary (context-free agent) + relevance (repo-context agent)
- `sources/originals/` — openly licensed originals; `MANIFEST.md` lists the rest (gitignored)
- `gitignored/` — local-only material (meeting notes etc.), never committed
- `docs/cases.md` — real cases traced through the loop, incl. anti-patterns
- `docs/ai-in-the-loop.md` — where AI is already entering, observed effects
- `docs/stamped.md` — where STAMPED fits, the spectrum, the allocation question
- `TODO.md`
