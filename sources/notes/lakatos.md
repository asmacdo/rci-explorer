# Lakatos, "Falsification and the Methodology of Scientific Research Programmes" (1970)

Status: agent-generated 2026-10-16, not yet reviewed. Nobody in this pipeline read the primary text.
The summary was written by an agent with no project context; the relevance section by a second agent that read the repo and that summary.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### Citation

Lakatos, Imre. 1970. "Falsification and the Methodology of Scientific Research Programmes." In *Criticism and the Growth of Knowledge*, edited by Imre Lakatos and Alan Musgrave, 91-196. Cambridge: Cambridge University Press. English original. The volume is the proceedings of the International Colloquium in the Philosophy of Science, London, 1965 (vol. 4).

- DOI of the book contents page: https://www.doi.org/10.1017/CBO9781139171434.009
- Cambridge Core chapter page: https://www.cambridge.org/core/books/abs/criticism-and-the-growth-of-knowledge/falsification-and-the-methodology-of-scientific-research-programmes/B1AAD974814D6E7BF35E6449691AA58F
- Page range: Cambridge gives 91-196. One PhilArchive record gives 91-195.

Related but distinct: "Criticism and the Methodology of Scientific Research Programmes," *Proceedings of the Aristotelian Society* 69 (1968-69): 149-186. It is an earlier version of the argument.

The chapter is reprinted, with some changes, in Lakatos, *The Methodology of Scientific Research Programmes: Philosophical Papers Volume 1*, ed. J. Worrall and G. Currie (Cambridge University Press, 1978). I am citing that reprint from background knowledge.

### Summary

Lakatos reviews three positions on how science should be judged: dogmatic (naive) falsificationism, Popper's methodological falsificationism, and his own alternative. He argues that naive falsificationism fails as history and as logic. Theories are never tested alone, because they come with auxiliary assumptions and ceteris paribus clauses. Lakatos therefore takes the unit of appraisal to be a research programme, a sequence of theories that share a "hard core" and a "protective belt" of auxiliary hypotheses. The core is shielded by a negative heuristic: do not direct refutations at it. A positive heuristic suggests how to modify and extend the belt. A programme is progressive if its changes predict novel facts and some of those predictions are corroborated. It is degenerating if it only patches itself after the fact (ad hoc adjustments). Competing programmes are compared over time, and rejecting a programme is rational only when a rival is progressive relative to it. Lakatos argues that this matches how science actually proceeds, and he presents it as a normative methodology of "sophisticated falsificationism". He also proposes that the history of science be rationally reconstructed by such a methodology, with remaining history placed in external footnotes.

### Well-known critiques

- Paul Feyerabend (for example *Against Method*, 1975) argued that Lakatos's standards give no actual guidance. Since a degenerating programme may later revive, the methodology cannot say when to abandon one, so it amounts to "anything goes" in disguise.
- Thomas Kuhn (in correspondence and later remarks) argued that Lakatos's rational reconstructions impose a norm on history, and that his account still leaves theory choice resting on community judgment, much like Kuhn's own.
- Larry Laudan and others argued that the notion of "novel fact" is ambiguous, and that the criterion is only retrospective. It also gives no timescale for judging when a programme is degenerating.

### Confidence

Verified from sources:
- Publisher, editors, book title and year, and the chapter page range 91-196 (with 91-195 appearing in one record). Source: search results pointing to Cambridge Core, https://www.cambridge.org/core/books/abs/criticism-and-the-growth-of-knowledge/falsification-and-the-methodology-of-scientific-research-programmes/B1AAD974814D6E7BF35E6449691AA58F, and PhilArchive, https://dc2.philarchive.org/rec/LAKFAT.
- The Aristotelian Society paper's volume and pages, from the same search results. I did not open the pages themselves.

From background knowledge, not checked online:
- The summary and the critiques.
- The 1978 reprint details.
- The colloquium year and volume number.

Uncertain:
- The exact DOI for this single chapter. The DOI above is the one the search returned for the book contents page, and I did not confirm it resolves to this chapter specifically.
- The Kuhn and Laudan points are paraphrased from memory with no specific work cited. Check them before quoting. I give no page numbers or quotes.

## Relevance to this project (repo-context agent)

1. **Loop step(s)**: Step 5 (evaluation) and "trust" (step 2). Lakatos's unit of appraisal is a programme over time, not a single object, which bears on how trust in a body of claims should be assigned and updated.

2. **What it gives this project**:
- Argument that evaluation is never of one claim alone: auxiliaries and ceteris paribus clauses travel with it. This is a mechanism for why a failed replication (5 -> 2) does not cleanly lower trust in a specific source.
- Progressive vs degenerating as a trust-update signal: novel corroborated predictions raise trust, post hoc patching lowers it. This is a candidate computed "trust score" component beyond citations.
- Hard core / protective belt maps loosely to what is shielded from retesting. Candidate analogue: the shared pipeline or dataset core that dependents rarely re-examine.
- Comparative rule: reject only relative to a rival. Relevant to allocation, since verification effort is justified by an alternative, not by a lone anomaly.

3. **Where it stops**:
- Retrospective and gives no timescale (Laudan, Feyerabend, per summary), so it cannot drive an allocation queue.
- No costs, no actors, no dependency counts, no auditability. Nothing on who checks or how often.
- Programme-level, theory-centric. The loop's objects are scripts, datasets and results.
- Its normative stance (rational reconstruction) is at odds with "descriptive first."

4. **Bearing on repo claims**:
- map.md: "A failed evaluation should lower trust in the object's sources." Complicates: Duhem-Quine means blame is underdetermined; the edge needs an attribution rule.
- map.md: "6 is a state, not a gate." Supports, with the caveat that Lakatos says retirement waits for a rival.
- CLAUDE.md: "Every claim about 'how science works' needs a real case." Lakatos's descriptive claims are contested (Kuhn critique), so treat him as a model, not an observation.
- prior-art.md seed "research programmes as load-bearing cores": partly accurate (hard core) but "load-bearing" conflates the core's immunity with dependency load. The core is protected by convention, not by being relied upon. Also "how the body's trust structure shifts" is better attributed to Kuhn; Lakatos is about appraisal, not trust.

5. **Suggested one-line take**: Appraisal belongs to programmes, not isolated claims; progressive vs degenerating is a retrospective trust-update signal, with no costs, actors or timescale.

6. **Confidence**:
- Rests on summary: core concepts, critiques (Feyerabend, Kuhn, Laudan), citation details.
- Rests on my background knowledge: Duhem-Quine link, the normative/descriptive tension, that Lakatos's "novel fact" was later refined (Zahar, Worrall).
- My inference, guesses: the hard-core analogy to shared pipelines; use as a trust-score component. Unverified; I have not read the primary text.
