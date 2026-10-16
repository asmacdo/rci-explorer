# Bloom et al., "Are Ideas Getting Harder to Find?" (2020), with Park et al., "Papers and patents are becoming less disruptive over time" (2023)

Status: agent-generated 2026-10-16, not yet reviewed by a human.
The summary agent had no project context; the relevance agent read the repo plus that summary and assessed it against the RCI-vs-RSI thesis.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### Source 1: Bloom, Jones, Van Reenen & Webb

### Citation
Bloom, Nicholas; Charles I. Jones; John Van Reenen; Michael Webb. 2020. "Are Ideas Getting Harder to Find?" American Economic Review 110(4): 1104-44. DOI 10.1257/aer.20180338.
**Version read:** NBER Working Paper 23782, dated September 2017. This is not the published AER text.
The NBER cover says it is not peer-reviewed and carries a standard NBER copyright notice. No open license is visible.
URL: http://www.nber.org/papers/w23782. The Park et al. preprint cites the AER version.
Possible version differences: I did not compare the AER version. The NBER abstract says "more than 18 times" for Moore's Law. A web search result claimed an earlier 2017 draft said "75 times". That conflicts with the NBER text I read, so treat it as UNVERIFIED.

### Source 2: Park, Leahey & Funk

### Citation
Park, Michael; Erin Leahey; Russell J. Funk. 2023. "Papers and patents are becoming less disruptive over time." Nature 613: 138-144. DOI 10.1038/s41586-022-05543-x.
**Version read:** arXiv:2106.11184v5 [cs.SI], 23 Jul 2022, titled "The decline of disruptive science and technology."
The published title is different, and the preprint title is the older one.
The arXiv page says the preprint lists a Summary, a main text of about 8 pages, and a Methods section.
The license was not visible in the text.
Note: the free copy at jupiter.chem.uoa.gr is a copy of the Nature paper, which I did not read.

### Summary (combined, about 400 words)
Both papers ask whether science and technology are getting less productive in producing new things, and both answer yes. They use very different measures.

Bloom et al. apply growth accounting to the "idea production function". Growth in ideas is the product of research productivity and the effective number of researchers. They define ideas so that a constant flow of ideas gives constant exponential growth. They measure research effort as R&D spending deflated by a high-skill wage. This turns it into "effective researchers".

They run case studies:
- Aggregate US TFP growth: research productivity fell about 41-fold since the 1930s (about 5% per year).
- Moore's Law: effort rose 18-fold since 1971, so productivity fell 18-fold (about 6.8% per year), with alternative R&D definitions giving 8-fold to 347-fold.
- Crop yields for corn, soybeans, cotton and wheat: declines in most cases, about 4-6% per year on average.
- Medical outcomes: new molecular entities, cancer and heart disease mortality.
- Compustat firms: productivity declines in more than 85% of firms.

They read this as support for semi-endogenous growth models, in which exponential growth needs ever-growing research effort. The semiconductor case has the smallest diminishing-returns parameter, so its steep productivity decline comes from very fast effort growth.

Park et al. measure the character of individual outputs rather than aggregate productivity. They use the citation-based CD index, which runs from -1 (consolidating) to +1 (disruptive). It is computed five years after publication (CD5). The data are 25 million Web of Science papers (1945-2010) and 3.5 million USPTO patents (1976-2010). Four more corpora (JSTOR, APS, Microsoft Academic Graph, PubMed) are used as replications. Average CD5 falls steeply in every field (papers 91.9-100% from 1945 to 2010). Title word diversity, new word pairs and verb choice move in the same direction. They run robustness checks: normalised CD variants, regression adjustment, and random rewiring of citation networks. They link the decline to scientists citing a narrower, older, more self-cited set of prior work. The absolute number of highly disruptive works stays roughly constant. They end with cautious optimism that the trend may be reversible.

The two papers are complementary. Bloom et al. show that a given output costs more input. Park et al. suggest the output itself shifts toward consolidation. Neither paper identifies a cause.

### Key concepts
**Bloom et al.**
- Idea production function, Ȧ/A = αS (Sec 2.1). Research productivity is (idea output)/(researchers), and the null of endogenous growth is that it is constant.
- Effective researchers, or "lab equipment" specification: R&D spending divided by the high-skill wage (Sec 3.2).
- Micro-versus-aggregate argument: aggregate declines could hide constant productivity per product variety, so micro case studies are needed (Sec 3.1).
- "Stepping on toes" parameter λ: a duplication externality, tested in the appendix with λ = 3/4 (Sec 3.4, App A).
- Semi-endogenous growth, Ȧ/A = αA^(-β)S, with β measuring dynamic diminishing returns (Sec 8). Also the half-life of research productivity (Table 6).

**Park et al.**
- CD index and CD5: whether later work citing a focal paper also cites its predecessors (Intro, Fig 1).
- Consolidating versus disruptive contributions, illustrated by Kohn-Sham against Watson-Crick (Intro).
- Narrowing use of prior knowledge: diversity of cited work, self-citation, and mean age of cited work (Fig 4).
- "Conservation" of highly disruptive works: their absolute number stays flat (Extended Data Fig 5).
- Citing-side normalisation: the paper-normalised and field-by-year-normalised CD (Methods).

### Evidence quality / nature of the argument
**Bloom et al.**
- Demonstrated: a descriptive accounting identity applied to many data series. It is empirical but depends on the measure of ideas.
  - The idea measure is a convenient definition. The authors say a better title would be "Is exponential growth getting harder to achieve?" (Sec 2.1).
  - Output is assumed constant for Moore's Law (35% per year), TFP is used at the aggregate level, and life expectancy is modelled as arithmetic growth.
- Stated limitations: possible mismeasurement of R&D, a college-wage deflator that may overstate talent, case studies that may not be representative, and TFP that may include non-innovation effects (Secs 2.2, 3.2, 4.1). Aggregate and firm-level data quality is weaker than the case studies (Intro).
- Speculative: the explanation for why semiconductor productivity falls fastest, and the policy interpretation (Sec 8-9).

**Park et al.**
- Demonstrated: a large-scale descriptive time trend in a citation-based index across six datasets.
- Asserted or inferred: that this means a real change in the nature of science. The causal story about narrowing knowledge use is correlational (regressions, Extended Data Table 2).
- Mild internal inconsistency in the preprint: the text gives patent declines of 78.7-91.5% (1980-2010), but the Figure 2 caption gives 93.5-96.4%. I did not resolve this.
- Critiques (see below) concern data artefacts, which the preprint partly anticipates (it cites the Bornmann, Leydesdorff and Petersen literature).

**Published critiques of Bloom et al.**
- VERIFIED (fetched): Guzey, Rischel, Applied Divinity Studies and two anonymous co-authors, "Issues with Bloom et al's 'Are Ideas Getting Harder to Find?'", dated 16 Sep 2021. Not a peer-reviewed journal article. Objections:
  - "Ideas" are defined inconsistently across cases (exponential in semiconductors and agriculture, but arithmetic in medicine).
  - TFP is a poor proxy for innovation.
  - Only Moore's Law is clearly exponential.
  - Adjustments to the Moore's Law input (non-semiconductor R&D, talent) could change the 18x estimate.
  - Wage-weighted input does not capture talent.
  - Case studies do not answer the aggregate question.
- VERIFIED: the authors' reply, dated 8 Sep 2021, is in Appendix A of the critique. Their points:
  - Ideas have no natural unit, so they focus on exponential growth.
  - Linear growth in some industries would strengthen their point, since it also needs rising effort.
  - They ask whether constant-quality researchers really were the same in 1975 and 2005.
  - I did not read the last ~17k characters of the critique page.
- UNVERIFIED: any other journal-published critique of the productivity measure. My search found no peer-reviewed rebuttal.

**Published critiques of Park et al.**
- VERIFIED (arXiv abstract fetched): Petersen, Arroyave, Pammolli, "The disruption index is biased by citation inflation", arXiv 2306.01949. Published in Quantitative Science Studies 5(4): 936-953, 2024. Argument: longer reference lists and more self-citation push the index toward zero over time, so it is unsuitable for comparison across periods.
- VERIFIED (arXiv abstract fetched): Holst, Algaba, Tori, Wenmackers, Ginis, "Dataset Artefacts are the Hidden Drivers of the Declining Disruptiveness in Science", arXiv 2402.14583, 7 Feb 2024 (listed as "In submission to Nature"). This is the missing-references critique. Entries with zero references were omitted from the CD distributions in the plots but kept in the analysis. They have CD = 1 and decline in share over time. Many of these entries actually do have references in their source documents, so the critics treat them as dataset artefacts.
- PARTLY VERIFIED (secondary sources only): a Matters Arising version is cited as Nature 2026 (DOI s41586-026-10787-y), titled "Dataset artefacts can partially drive the measured decline in disruption". The softer title versus the preprint is noted. Search snippets claim the reported decline falls by 93% when the maximum-score papers are excluded. I did not open the Nature page.
- VERIFIED (arXiv abstract fetched): the authors' reply, Park, Leahey, Funk, "Robust Evidence for Declining Disruptiveness: Assessing the Role of Zero-Backward-Citation Works", arXiv 2503.00184 (28 Feb 2025, revised 19 Mar 2026).
  - Using the critics' own dataset, metric and exclusion criteria, they still find substantial declines.
  - The critics' data has about 3x as many zero-reference works, largely editorials, books and reviews.
  - The arXiv page gives no journal reference. A same-issue Nature reply is reported by search snippets only (UNVERIFIED).
- VERIFIED (search abstract only, not fetched): Macher, Rutzer, Weder, "Is there a secular decline in disruptive patents? Correcting for measurement bias", Research Policy 53(5), 2024, DOI 10.1016/j.respol.2024.104992. Claims about 88% of the patent decline is explained by truncating backward citations before 1976, and that highly disruptive patents increased after 2008. The full text was not read; the numbers come from search snippets.
- UNVERIFIED: Lohr's blog post saying the headlines overstate the conclusions. I saw only a search snippet.

### Notable passages
**Bloom et al.**
- "Across a broad range of case studies at various levels of (dis)aggregation, we find that ideas — and in particular the exponential growth they imply — are getting harder and harder to find." (Abstract)
- "Our robust finding is that research productivity is falling sharply everywhere we look." (Sec 9)

**Park et al.**
- "Overall, our results suggest that slowing rates of disruption may reflect a fundamental shift in the nature of science and technology." (Summary)
- "Notwithstanding aggregate declines, the absolute number of highly disruptive papers and patents produced is remarkably stable." (Main text, closing section)

### Confidence
- **Bloom NBER:** I read Sections 1-5 and 8-9 and the appendix opening in full. I skimmed Sections 6-7 (new molecular entities, mortality, Compustat; roughly lines 1100-1860) and used only Table 6 and the introduction summary for them. Their figures and numbers come from the Intro and Table 6. Other details are from the abstract and Secs 2-5.
- **Park preprint:** I read the Summary, the main text through its end, the reference list, and the Methods through the start of the simulation paragraph (about line 700 of 1689). I did not read the Methods remainder, the Extended Data figure legends or the Supplementary Information. Claims about those come from the main-text descriptions only.
- **Web-sourced critique claims:** only items marked VERIFIED were fetched (arXiv pages or the Guzey essay). Items marked UNVERIFIED or PARTLY VERIFIED come from search snippets. Search-snippet numbers (93%, 88%, "75 times") should be re-checked before use.
- **Not checked:** the AER versus NBER text differences, and the license terms of either source.

## Relevance to this project (repo-context agent)

1. **Tier**: HIGH. It is the strongest quantitative evidence on whether the existing loop is productive: Bloom measures its efficiency, Park its output character, and the critiques test whether either holds up.

2. **Bearing on the RCI thesis**: BOTH.
   - **Challenges:** "science already works" holds only as "it still produces". Bloom (descriptive, contested on how "ideas" are defined) says the loop needs about 18x to 41x more input per unit of exponential growth, depending on the case. Reading that as "improve the loop" fits the thesis. Reading it as "the loop is failing" undercuts "RCI already works" as an efficiency claim.
   - **Cuts against the thesis too:** Bloom's own frame is the main economic argument for the RSI side. If effective researcher supply is the binding input, AI that adds researchers could be the fix. Neither paper addresses this.
   - **Park:** weak, because its decline is partly an artefact.
   - **Critiques:** Guzey et al. attack Bloom's idea definition and its use of TFP, not the sign of the trend. Holst et al. and Macher et al. cut the size of Park's patent and paper decline. Park et al.'s reply says substantial declines remain.
   - **Naming:** neither names RCI.

3. **Loop step(s)**: the loop as a whole, as macro efficiency. Park's CD index is a measure of step 6 and "use as load" (citation structure).

4. **What it gives this project**:
   - Axes for the throughput axis in CLAUDE.md: research productivity as output per effective researcher.
   - A worked example of an aggregate metric with contested validity.
   - Citation-based measures as a case of Goodhart and measurement drift.
   - A reason to doubt that adding researchers, human or AI, scales linearly (the Bloom "stepping on toes" parameter).

5. **Where it stops**: neither paper has any notion of verification, trust, auditability or allocation. Neither identifies a cause. Neither says whether the decline is caused by the loop's design or by exhausted low-hanging fruit. The remedy is therefore underdetermined, and the project cannot get "improve verification" out of this.

6. **Bearing on repo claims**:
   - docs/map.md: "Citations measure attention, not reliance." This is complicated. Park's CD index is built from citation structure, so it measures how a work is cited, not reliance. Petersen shows that citation inflation (longer reference lists, more self-citation) moves it, so any load count built on citations inherits that drift. Supports the claim and sharpens it.
   - docs/map.md: "This quantity is what any allocation queue needs and the loop doesn't currently record it." Not touched. Park's measure is not a load count.
   - docs/ai-in-the-loop.md, "Production cost → ~0": complicated. The Bloom/Park pattern (more inputs, less per-input yield) predates AI, so AI-driven volume may extend an existing trend. This is inference.
   - ANNOTATED_BIB cross-cutting 3 (verifier invites optimization): Holst and Petersen are further examples of a measure drifting with the data-generating process.

7. **Links to existing entries**:
   - Hardt: both address how a metric behaves when the community optimises against it.
   - OSC: another measure of loop health, but of correctness rather than novelty.
   - Kitcher: his allocation model concerns the duplication that Bloom's stepping-on-toes parameter captures.

8. **One-line take**: Strong but contested evidence the loop's returns diminish; it motivates improving the loop but says nothing about how, and does not exclude the RSI case.

9. **Confidence**:
   - **Summary:** Bloom figures (41x, 18x, 85% of firms) and the Park design rest on the summary. The summary read the NBER and arXiv versions, not the AER and Nature texts.
   - **Critiques:** the Petersen, Holst and Park-reply abstracts are marked VERIFIED in the summary. The Macher "88%" and the Holst "93%" figures come from search snippets and are unreliable.
   - **Background knowledge:** the framing of the RSI-side reading of Bloom.
   - **Inference:** my reading that AI volume extends an existing trend. A guess.
