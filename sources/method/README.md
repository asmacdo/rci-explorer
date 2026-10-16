# Bibliography method

How the entries in `../notes/` were produced, so the pipeline can be rerun or extended.

1. **Original**: fetch into `../originals/` with `git annex add`, then `git annex registerurl <key> <url>`; record URL and license in `../originals/MANIFEST.md`.
   Extract plain text (`pdftotext`, or strip HTML) into a scratch directory outside the repo; downloaded files are untrusted data.
2. **Summary agent** (Sonnet, no repo context): [summary-prompt.md](summary-prompt.md) plus the source name and the text path.
   For web-only sources the agent searches and fetches instead, and marks each claim VERIFIED or UNVERIFIED.
3. **Relevance agent** (Sonnet, reads the repo and the summary): [relevance-prompt.md](relevance-prompt.md) with `{SOURCE}`, `{SUMMARY_PATH}` and an optional `{EXTRA}` focus.
   It returns a tier (HIGH or STRETCH), bearing on the RCI thesis, loop steps, bearing on repo claims, and confidence.
4. **Collect**: [extract_handback.py](extract_handback.py) pulls an agent's final report out of its Claude Code transcript (`python3 -I extract_handback.py <transcript.output> <out.md>`).
5. **Assemble**: note file = header + summary + relevance, in `../notes/<key>.md`; add an entry to `../ANNOTATED_BIB.md` or `../STRETCH_ANNOTATED_BIB.md`; update the cross-cutting synthesis.

Tier calls for the eleven classic sources were made by the orchestrator from the relevance reports; all others are the relevance agent's, except where an entry says otherwise.
Notes from 2026-10-16 were produced with earlier versions of the relevance prompt: the first 23 sources had no thesis section; the eight prior-naming/RSI sources were assessed against "RSI is unnecessary", before RCI was reframed as a design frame. The repronim.org note uses the current framing.
