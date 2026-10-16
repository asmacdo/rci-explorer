# Where STAMPED fits

STAMPED increases transparency and lowers repro* barriers: versioned data, recorded
commands tied to versioned inputs/outputs, modularity, portability. It is a decent first
pass at "how reproducible is this."

## Role in the loop

- **Necessary, not sufficient, for rigor** — where rigor is the community's ability to
  check, not the individual's care. A wrong model that is STAMPED is at least transparent;
  future researchers (or critics) can spot and correct it.
- **Lowers cost to retire and cost to build on.** It does not touch production cost, which
  AI collapsed. STAMPED is the counterweight restoring a filter on the other side of the
  asymmetry (see anti-pattern in `cases.md`).
- **Makes objects machine-auditable.** The "future researcher" who spots the error can be
  a critic agent run at scale. That's what turns transparency from a passive virtue into an
  active loop.
- **Contingent benefit.** Cheaper verification only helps if verification spend rises.
  Hence: drive STAMPED's up-front cost toward zero so adoption doesn't depend on realized
  benefit — option value. Practically: capture as a side effect of execution, never as a
  human task.

## The spectrum

STAMPED is a soft spectrum, minimal → ideal. Closing holes gets increasingly expensive
(canonical example: reproducible image builds — must we also vendorize every library that
went into the image?).

That's where STAMPED itself becomes a resource allocation question:

- Marginal cost rises steeply at the tail; marginal benefit scales with load.
- So it's a cutoff per object, not one cutoff — and the input that sets it is the
  dependency count the loop doesn't record (see `map.md`).
- **Lazy preservation:** record enough now (lockfiles, hashes, digests) that the expensive
  step stays possible; let load trigger it later. Cost is bounded as long as closability is
  preserved.
- **The frontier moves:** Software Heritage, content-addressed stores, Nix-style builds
  keep making the tail cheaper. Treat hole-closing costs as time-varying.

## Grader

- Static (provenance present) vs. executed (re-run reproduces). Static is cheap and gives
  a gradient; also gameable and loosely correlated with actual reproduction.
- Calibrate: grade everything statically, re-execute a sample, track the gap. The gap is
  the number that says whether the grader is lying.
- Every layer that's cheap to capture can be captured hollowly (or optimized for
  literally — see lee3j case). Reproducible ≠ rigorous; keep the scores separate.
