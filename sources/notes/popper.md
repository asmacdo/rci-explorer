# Popper, The Logic of Scientific Discovery / Conjectures and Refutations

Status: agent-generated 2026-10-16, not yet reviewed. Nobody in this pipeline read the primary text.
The summary was written by an agent with no project context; the relevance section by a second agent that read the repo and that summary.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### Citation

- Popper, Karl R. (1935 imprint; written 1934). *Logik der Forschung: Zur Erkenntnistheorie der modernen Naturwissenschaft*. Vienna: Julius Springer. The title page is dated 1935, but the book is usually cited as 1934.
- Popper, Karl R. (1959). *The Logic of Scientific Discovery*. London: Hutchinson. Popper's own revised translation of the German original, with new appendices. Reissued by Routledge (London and New York) as Routledge Classics, 2002.
- Popper, Karl R. (1963). *Conjectures and Refutations: The Growth of Scientific Knowledge*. London: Routledge and Kegan Paul. Later Routledge reprints exist, and some catalogues list 1965 for the New York issue.
- No DOI. Stable overview: https://plato.stanford.edu/entries/popper/ and https://en.wikipedia.org/wiki/The_Logic_of_Scientific_Discovery

### Summary

Popper takes on the problem of demarcation: how to tell empirical science from non-science and pseudo-science. He rejects inductivism and the idea that theories are verified by accumulating confirming observations. Instead, a theory counts as scientific if it is falsifiable, meaning it forbids some possible observations and so can be tested and refuted. Science proceeds by bold conjectures followed by severe attempts at refutation, a method he calls critical rationalism. Theories that survive tests are "corroborated", which is not the same as being confirmed or made probable. He treats basic statements (singular observation reports) as fallible and accepted by convention. He also discusses probability and the simplicity and content of theories. *Conjectures and Refutations* is a collection of essays and lectures. It applies these ideas to the growth of knowledge, to the history of science, to critiques of Marxism and psychoanalysis as unfalsifiable, to truth-likeness (verisimilitude), and to social and political thought. Its central themes are that knowledge grows by error-elimination and that all knowledge is conjectural.

### Well-known critiques

- Thomas Kuhn (*The Structure of Scientific Revolutions*, 1962): actual science mostly consists of "normal science" within paradigms, and paradigms are not simply abandoned on a single refutation. Rival paradigms are incommensurable.
- Imre Lakatos ("Falsification and the Methodology of Scientific Research Programmes", 1970): naive falsification fails because failed predictions can be blamed on auxiliary assumptions. He proposed research programmes as the unit of appraisal, and argued that Popper's later position is a more sophisticated falsificationism.
- Pierre Duhem and W. V. O. Quine (the Duhem-Quine thesis) and Hilary Putnam ("The 'Corroboration' of Theories", 1974): theories are tested only together with auxiliary hypotheses, so a failed test does not show which part is wrong. Putnam also argued that corroboration without induction cannot guide practical reliance on theories. The Duhem-Quine point is from background knowledge; the SEP fetch did not cover it.
- Paul Feyerabend (*Against Method*, 1975) is another common critic, arguing that no single methodology fits science. This is from background knowledge.

### Confidence

Verified from sources:
- Edition and publisher data (Springer 1935; Hutchinson 1959; Routledge Classics 2002; Routledge 1963 for *Conjectures and Refutations*) was checked via the Stanford Encyclopedia of Philosophy (https://plato.stanford.edu/entries/popper/) and a web search that surfaced Wikipedia (https://en.wikipedia.org/wiki/The_Logic_of_Scientific_Discovery).
- The Kuhn, Lakatos and Putnam bibliographic details also come from the SEP page.

Stated from background knowledge:
- The summary of the argument and the critique content, including the Duhem-Quine and Feyerabend points. The SEP fetch did not describe these, and I did not read the last ~24 characters of the page.

Unsure:
- Whether the first publication year is best given as 1934 or 1935. The imprint says 1935.
- The 1963 versus 1965 date for *Conjectures and Refutations*. One search result (PhilPapers) lists 1965 for the New York issue; I did not resolve this with a library catalogue.
- Exact publisher wording ("Routledge and Kegan Paul" for 1963) is from memory.
- I give no page numbers or quotes.

## Relevance to this project (repo-context agent)

1. **Loop step(s)**: Step 5 (evaluate), plus "norms". Popper supplies the criterion for what an evaluation should test, and (in C&R) the social "critical tradition" claim. Weakly step 2, via corroboration as a trust input.

2. **What it gives this project**:
- Corroboration vs confirmation: a survived severe test is not a probability. This is a vocabulary for the "trust score" that avoids citation-count reading.
- Severity of test: not all evaluations carry equal information. This gives a principled axis for allocation (test where a failure would be most informative).
- Basic statements are fallible and accepted by convention. This matches "6 is a state, not a gate": acceptance is revisable.
- All knowledge is conjectural, so "semi-trusted body" is Popperian by default.

3. **Where it stops**:
- No actor, cost, frequency or who-checks model, so no allocation. This is the seed's point and it holds.
- Deals with theories, not research objects (code, data, pipelines). Reproducibility is not falsification; a failed re-run is not a refuted theory.
- Duhem-Quine: a failed test cannot say which part broke. This bears on 5 → 2, since blame propagation to sources is underdetermined.
- Lakatos/Kuhn: refutation is not applied mechanically, which complicates any automated critic.
- Putnam: corroboration cannot guide practical reliance, which is exactly what "load" is about.

4. **Bearing on repo claims**:
- docs/prior-art.md seed ("Falsifiability is a criterion, not a process; says little about who checks or how often"): accurate but incomplete. C&R does address process (conjecture then refutation, criticism as a social tradition). The gap is cost and allocation, not process.
- docs/map.md "A failed evaluation should lower trust in the object's sources": complicated by Duhem-Quine.
- docs/map.md "Citations measure attention, not reliance": supported in spirit (corroboration is not confirmation), but Popper says nothing on reliance.
- CLAUDE.md "Rigor is a community property": mildly supported (critical tradition), but Merton and Longino fit better.
- Row labels Popper "5 (evaluate claims)". Also relevant to norms. Minor fix.

5. **Suggested one-line take**: Corroboration-by-severe-test frames what step 5 should measure; silent on cost, allocation, objects-not-theories, and Duhem-Quine blame assignment for 5 → 2.

6. **Confidence**:
- From the summary: edition data, the falsifiability/corroboration/conjecture core, and the Kuhn/Lakatos/Putnam critiques.
- From my background knowledge: the "critical tradition" social emphasis in C&R, severity of tests, Popper's own Duhem-Quine response (conventionalist stratagems), and the Merton/Longino comparison. Fairly confident.
- My inference (guesses): that severity maps onto allocation, and that Duhem-Quine undermines 5 → 2 blame. Both are plausible, not established. The summary has no quotes or page numbers, so nothing here is checked against the text.
