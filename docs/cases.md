# Cases

Real projects traced through the loop, to stretch the map. Anti-patterns included.

## Anti-pattern: unverifiable slop (human or AI)

Contributes only uncertainty and "debt." Slop was always possible; AI made it near-free to
produce while leaving it expensive to retire. The loop's economics assumed production cost
was a filter. It isn't anymore.

Name it as a ratio, not as AI-specific: **uncertainty introduced per cost to retire.** By
the community-rigor standard much pre-AI literature is also slop; AI moved the ratio.

## Case: lee3j's autonomous STAMPED skill loop / scientist / benchmarker

Agent given STAMPED ideals as objective did complex analysis in "pure Python" — no
pandas/numpy — to minimize dependencies.

What happened:
- Succeeded at the objective given. Fewer deps scores higher on the spectrum; it climbed
  the spectrum. Missing input: the other side of the ratio (what the extra reproducibility
  was worth for *this* object). No agent capability supplies that; it wasn't in the task.
- Worse: hand-rolled numerics are almost certainly *less* reproducible in the sense anyone
  cares about — nothing to check against a known library. Score up, proxy down.

Lessons:
- Exhibit for the benchmark discussion: any benchmark for autonomous science is a scalar;
  a capable agent will do to it what this one did to STAMPED. Map first, so the benchmark
  encodes trade-offs rather than one axis.
- Caution: single anecdote, and the spec was arguably the bug. Present as "the spec was
  easy to get wrong," not "agents can't allocate."

### How/what should a spec balance? Is human intuition better, for now?

- **How:** specs are bad at weighing, good at excluding. Constrain obvious failure modes
  ("use the field's standard libraries, pinned"); give the agent the cost side explicitly
  (budget + load); for genuinely two-sided calls, route the decision rather than make it.
  A spec that balances is a spec that says who balances.
- **What:** depth on the STAMPED spectrum vs. cost; minimal deps vs. checkability against
  known tools (these pull opposite ways; the spec named only one); effort now vs. option
  value later; all scaled by load; plus what the object is *for* (methods paper vs. pilot).
- **Intuition, for now:** better at the empirical half — a trained prior on what the field
  builds on, what rots in three years — and that advantage erodes as the map makes load
  and cost explicit. The other half (cost vs. rigor weighting) is a values choice: belongs
  to the community, and humans are accountable for it. Humans Goodhart too
  (p < 0.05 is pure Python with a lab coat); the difference is consequences, and the loop
  corrects through them. Until an agent is embedded in that correction, weighing stays
  human for structural, not cognitive, reasons.

## TODO: cases to trace

- A typical neuroimaging paper end to end (which edges actually fired?)
- A replication attempt (did 5 → 2 propagate? to dependents?)
- A retraction (did anything downstream change?)
- An OpenNeuro dataset reuse chain (is load visible anywhere?)
