# Narayanan & Kapoor, "AI as Normal Technology" (2025)

Status: agent-generated 2026-10-16, not yet reviewed by a human.
The summary agent had no project context; the relevance agent read the repo plus that summary and assessed it against the RCI-vs-RSI thesis.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### 1. Citation

Arvind Narayanan and Sayash Kapoor. 2025. "AI as Normal Technology." Knight First Amendment Institute at Columbia University, essay series "Essays and Scholarship", 25-09, April 14, 2025. Stable URL: https://knightcolumbia.org/content/ai-as-normal-technology (perma.cc/HVN8-QGQY, as given in the source's own "Cite as" line). The text shows no DOI.

License: the page shows only "© 2025, Arvind Narayanan and Sayash Kapoor". No open license is visible.

Author affiliations as listed: Narayanan is a professor of computer science at Princeton. Kapoor is a Senior Fellow at Mozilla, a Rockefeller Fellow at the Princeton Center for Human Values, and a Ph.D. candidate at Princeton CITP.

I did not run web searches. The citation details come from the page text itself.

### 2. Summary

The essay states a worldview and does not try to prove a single proposition. The authors call it "AI as normal technology." It is a description of current AI, a prediction about the foreseeable future, and a prescription for how to treat AI. "Normal" does not mean low impact. Electricity and the internet count as normal, transformative technologies. What the authors reject is treating AI as a separate species, an autonomous and possibly superintelligent agent. They present it as the alternative to the superintelligence worldview, and they say that worldview has become dominant in AI discourse.

Part I argues that economic and social impact will be slow, on the scale of decades. The authors split AI progress into four stages: invention (new methods), innovation (products and applications), adoption (an individual's or firm's decision to use something), and diffusion (the wider social process by which adoption spreads). Each stage has its own speed limits. Diffusion lags in safety-critical areas, and it is limited by how fast people, organizations and institutions can change. Application development is slowed by a "capability-reliability gap", by tacit organizational knowledge, and by the social cost of real-world experiments. Benchmarks measure methods, not real-world utility, so they overstate impact.

Part II reframes "intelligence" as capability versus power. The authors argue that human ability is extended by technology and is not capped by biology. They hold that "superintelligence" is incoherent as usually conceived. They predict that humans plus AI will remain in control, and that more and more jobs will consist of AI control and task specification. They also describe many forms of control other than model alignment or a human reviewing every decision.

Part III covers risks. Accidents and arms races are treated as old regulatory problems. Defenses against misuse belong downstream of models. Catastrophic misalignment is called a "speculative" risk. Systemic risks such as inequality and concentration of power matter more under the normal-technology view.

Part IV is policy. It recommends reducing uncertainty, resilience, value pluralism and robustness. It opposes nonproliferation, and it argues that realizing AI's benefits needs active policy support.

The evidence is mostly historical analogy, a few case studies, and the authors' own earlier work.

### 3. Key concepts

- **AI as normal technology** (Intro): AI viewed as a tool humans can and should control, with impacts shaped by institutions. It is a description, a prediction and a prescription, not a claim of low impact.
- **Invention / innovation / adoption / diffusion** (Part I, "The Speed of Progress"; Figure 1): invention is new AI methods, innovation is products and applications, adoption is an individual or firm's decision to use a technology, and diffusion is the social process that spreads adoption. Each stage has its own speed limit.
- **Ladder of generality** (Part I, "The External world puts a speed limit on AI innovation"; Figure 2): each rung of computing reduces the programmer effort needed for a new task. The authors argue this does not remove application-development effort in consequential real-world domains.
- **Capability-reliability gap** (Part I): systems that look capable in tests fail to be reliable in costly real-world settings. This slows both self-driving cars and AI agents.
- **Construct validity of benchmarks** (Part I, "Benchmarks do not measure real-world utility"): benchmarks and exam-based forecasts measure methods progress and narrow skills, not application utility. The authors say they lead to overestimating real-world impact.
- **Capability versus power; critique of "superintelligence"** (Part II, "Human ability is not constrained by biology"; Figures 3 to 5): "intelligence" is not one-dimensional. What matters is power, meaning the ability to modify one's environment. The authors hold that human plus AI teams are not meaningfully surpassed by AI alone.
- **Human-in-the-loop versus other control; AI control as work** (Part II, "Control comes in many flavors"): auditing, monitoring, fail-safes, least privilege, reversibility and hierarchical oversight. The authors predict that human work shifts toward AI control and specification.
- **Speculative risk** (Part III, "Catastrophic misalignment is a speculative risk"): a risk with epistemic uncertainty about whether the true risk is zero, as opposed to stochastic uncertainty. Catastrophic misalignment is classed here.
- **Resilience versus nonproliferation** (Part IV): resilience is the capacity to deal with harm and consists of "no regret" measures. Nonproliferation is the strategy of limiting who can obtain powerful AI. The authors argue it is infeasible and creates single points of failure.

### 4. Evidence quality / nature of the argument

- It is a conceptual, programmatic essay. The authors say it "has the unusual goal of stating a worldview rather than defending a proposition" and that they do not give a point-by-point response to counterarguments (Intro, "A note to readers").
- Their evidence is mostly illustrative. It includes the electrification-of-factories history (Paul David), the Epic sepsis tool, a roughly 50-application survey of predictive optimization from their earlier paper, the NBER adoption-study figures, self-driving company case studies, and phishing and fuzzing examples. There is no new dataset or experiment.
- Many forward claims are explicit predictions, not demonstrated results. Examples: AI will not meaningfully outperform trained humans at geopolitical forecasting or at persuasion against self-interest (Part II), and slow diffusion will continue in high-consequence tasks (Part I). The authors say they cannot be certain of their predictions and aim at "the median outcome". They have not tried to quantify probabilities (Intro). They also say more empirical work on the innovation-diffusion lag is needed (Part I).
- Stated limits: military AI is excluded (Part III). The essay does not say what comes after the Part II world: "We do not know" (Intro). The authors say the worldviews are unlikely to be resolved empirically (Part IV).

**Extra-requirement items, stated as precisely as the text allows**

*Recursive self-improvement / intelligence explosion*
- The text appears in Part I, "Speed limits to progress in AI methods". Part II, Figure 3, uses an intelligence-explosion figure ("Intelligence explosion through recursively self-improved AI is a common concern") to criticize the spectrum-of-intelligence picture.
- The authors do not rule recursive self-improvement out. They write: "It remains to be seen if AI-conducted AI research can offer a reprieve. Perhaps recursive self-improvement in methods is possible, resulting in unbounded speedups in methods."
- They then say "AI development already relies heavily on AI" and that "It is more likely that we will continue to see a gradual increase in the role of automation in AI development than a singular, discontinuous moment when recursive self-improvement is achieved." The support is a single citation to a blog post (Timothy B. Lee).
- Their main move is that even unbounded speedups in methods would not change their conclusion about impact. Quote: "Our argument for the slowness of AI impact is based on the innovation-diffusion feedback loop, and is applicable even if progress in AI methods can be arbitrarily sped up." They add that benefits and risks "arise primarily from AI deployment rather than from development", so "the speed of progress in AI methods is not directly relevant to the question of impacts."
- They say they "reject 'fast takeoff' scenarios" (Intro).
- On the broader notion of an intelligence explosion, they argue it is conceptually flawed. Intelligence "is not well defined, let alone measurable on a one-dimensional scale", and the relevant property is power. They say they do not think there is a useful sense in which "AI is more intelligent than people acting with the help of AI".
- They also say capabilities will probably "increase indefinitely (we do)" accept this. The dispute is whether capability turns into power and loss of control (Part II, Figure 5).

*Speed of diffusion versus invention versus innovation*
- Definitions come first (Part I). Invention is new methods. Innovation is products and applications built with them. Adoption is the decision to use. Diffusion is the broader social process, which "might require changes to the structure of firms and organizations, as well as to social norms and laws".
- The ordering of speeds is as follows. Invention (methods) can be fast: "technical advances in AI have been rapid." Innovation is slower where errors are costly: self-driving took "over two decades" versus AlphaZero's "few hours". Diffusion is slowest: "Diffusion occurs over decades, not years."
- Safety-critical areas: "AI diffusion lags decades behind innovation." Evidence is the predictive-optimization survey. Most such applications use decades-old regression-style models, and "modern methods, such as transformers, are nowhere to be found". The authors predict slow diffusion will continue in high-consequence tasks.
- Adoption data: 40% of U.S. adults used generative AI in August 2024, but this meant only 0.5% to 3.5% of work hours and a 0.125 to 0.875 percentage point labor productivity increase. The authors dispute the claim that generative AI is adopted faster than the PC, because the comparison ignores intensity of use and cost. They say it is "quite possible" adoption has been much slower than PC adoption, depending on measurement.
- Innovation and diffusion run in a feedback loop that took "several decades" for electricity, computers and the internet. They expect the same for AI.
- Ordering within impact: impact is realized only through innovation plus diffusion, "not when methods and capabilities improve" (Figure 1 caption).
- Policy consequence: the speed of adoption of new AI applications "will remain a key metric to track" (Part III). Diffusion is not automatic and has "many roadblocks" (Part IV).

*AI in scientific research*
- The essay has no dedicated section on AI in science. Three passages bear on it.
  - (a) Scientific knowledge as a speed limit. Part I, "The External world puts a speed limit on AI innovation", says "Some of our most valuable types of knowledge are scientific and social-scientific." For AI to push those boundaries, "It will likely require interactions with, or even experiments on, people or organizations, ranging from drug testing to economic policy." They say "there are hard limits to the speed of knowledge acquisition because of the social costs of experimentation", and "Societies probably will not (and should not) allow the rapid scaling of experiments for AI development." This is asserted without data.
  - (b) Research volume versus progress in AI methods, Part I, "Speed limits to progress in AI methods". AI/ML arXiv paper counts show a doubling time under two years. Volume does not clearly translate into progress. They cite Chu and Evans (2021), who analyzed over a billion citations in 241 subjects and found that in fields with higher paper volume, it is "harder, not easier, for new ideas to break through" ("ossification of canon"). The authors say "Perhaps this description applies to the current state of AI methods research." They note herding around popular ideas and that the transformer has been dominant for about a decade.
  - (c) AI-conducted AI research, covered above under recursive self-improvement.
- The essay says nothing on AI for discovery in other scientific fields, AI-driven lab automation, or AI as a research assistant for scientists generally. It also does not address autonomous research agents. I did not find these topics anywhere in the text.

### 5. Notable passages

- "We view AI as a tool that we can and should remain in control of, and we argue that this goal does not require drastic policy interventions or technical breakthroughs." (Intro)
- "Thus, the speed of diffusion is inherently limited by the speed at which not only individuals, but also organizations and institutions, can adapt to technology." (Part I, "Diffusion is limited by the speed of human, organizational, and institutional change")
- "It is more likely that we will continue to see a gradual increase in the role of automation in AI development than a singular, discontinuous moment when recursive self-improvement is achieved." (Part I, "Speed limits to progress in AI methods")

### 6. Confidence

I read the whole text, including all of Parts I to IV, the Final Thoughts and the Acknowledgments. This is the body from the top of the file through line 497 of the extracted text, which I read in chunks. I skimmed the footnote/reference list (lines 499 to 735) only to confirm what the cited sources are. I did not look up any cited papers. The page footer and boilerplate after the author bios were ignored.

Taken directly from the text: the definitions, the Part I figures and examples, the recursive self-improvement statements, the diffusion-timing claims, and the three science-related passages. The quotes above are verbatim from the extracted text.

Inferred by me:
- The "ordering of speeds" (invention fast, innovation slower, diffusion slowest) is my synthesis of Part I. The authors never state it as a single ranking.
- That the essay does not address AI-for-science broadly is based on reading the full text. I did not search the footnotes for such sources.

Not checked: whether the text matches the PDF or any later revised or arXiv version.

## Relevance to this project (repo-context agent)

1. **Tier**: STRETCH. It is a policy and worldview essay with no treatment of science, verification or the research loop. Its one RSI passage argues impact is gated by diffusion, which is orthogonal to the repo's route question.

2. **Bearing on the RCI thesis**: BOTH, weakly. Supports: it argues that impact is gated by the innovation-diffusion loop of humans, firms and institutions ("applicable even if progress in AI methods can be arbitrarily sped up"). That is a structural cousin of "the community loop is the bottleneck, not a single system". It does not name RCI. It is also not about improving the loop; it is about why the loop is slow. Challenges: it explicitly leaves RSI open ("Perhaps recursive self-improvement in methods is possible") and calls it merely less likely than gradual automation. The only support is a blog post. It therefore gives no evidence that RSI is unnecessary, only that it would not matter for deployment. Its speed-limit argument also cuts against the repo: institutional slowness is treated as protective, whereas the repo treats loop friction as a thing to optimize.

3. **Loop step(s)**: The loop as a whole, plus norms. Step 6 and the 5 to 2 edge are touched only by analogy, via adoption and regulatory roadblocks. Nothing is specific to steps 1 to 6.

4. **What it gives this project**: (a) The invention / innovation / adoption / diffusion split, which could map onto a new method versus an application versus uptake in the body. This is my analogy, not theirs. (b) The capability-reliability gap and benchmark construct-validity point, consistent with Hardt and ARC-AGI-3. (c) Chu & Evans (2021) "ossification of canon" (cited secondhand): in larger fields, new ideas break through less easily. That is relevant to load and attention allocation. (d) The "control comes in many flavors" list (auditing, monitoring, least privilege, reversibility) as vocabulary for oversight beyond a human reviewing every decision. (e) The claim that experiments on people and organizations cannot be scaled quickly, which limits autonomous science.

5. **Where it stops**: No analysis of science, peer review, replication, trust or allocation. Evidence is analogy and prior work by the authors, with no new data. Its predictions are unquantified. The RSI discussion is a few sentences. Military AI is excluded. It says nothing about AI as critic or verifier.

6. **Bearing on repo claims**:
- ANNOTATED_BIB cross-cutting 4 (AI critics): complicated only slightly. The essay's "AI control as work" and auditing/monitoring agree that oversight stays human-and-tool, but give no numbers.
- `docs/ai-in-the-loop.md`, "find the loop with a verifier and iterate there": loosely supported by the capability-reliability gap and the benchmark validity argument.
- `CLAUDE.md`, "easier than RSI": not tested. The essay neither supports nor refutes it.
- `docs/ai-in-the-loop.md`, "Production cost → ~0": complicated. The essay predicts slow diffusion in consequential tasks, which argues against flood pressure, but its evidence is not about publishing.
- `docs/map.md`, "Hypothesis: 2 and 5 are where AI changes the numbers most": no bearing.

7. **Links to existing entries**:
- Hardt: shared point that benchmarks overstate real-world utility.
- ARC-AGI-3: benchmark validity and moving goalposts.
- Brain Researcher: capability-reliability gap, since the sign-blind error missed by automated review is an instance.
- Kuhn and Polanyi: institutional change as the rate limiter.
- Strevens/Longino: weak, via the idea that norms and institutions govern uptake.

8. **One-line take**: Context for why institutions gate AI impact; it is not about science, verification or allocation, and it leaves RSI open.

9. **Confidence**: The summary supplies the structure and quotes. I checked these against the full text: the RSI quote, the "innovation-diffusion feedback loop" quote, and the Chu & Evans passage including the "ossification of canon" wording. My knowledge of the repo comes from my reads of its files. The STRETCH call, the mappings in 4(a) and 6, and the "institutional slowness as protective" reading are my own inference. I did not verify Chu & Evans independently; I know the paper from background knowledge and it is as characterized. I did not read the full control section, only the summary's account of it, so the "control flavors" item rests on the summary.
