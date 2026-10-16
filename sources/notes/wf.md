# Weston & Foerster, "AI & Human Co-Improvement for Safer Co-Superintelligence" (2025)

Status: agent-generated 2026-10-16, not yet reviewed by a human.
The summary agent had no project context; the relevance agent read the repo plus that summary and assessed it against the RCI-vs-RSI thesis.
Each section ends with its own confidence notes; treat anything marked background knowledge or inference as unverified.

## Summary (context-free agent)

### 1. Citation
Jason Weston and Jakob Foerster (FAIR at Meta), "AI & Human Co-Improvement for Safer Co-Superintelligence", arXiv:2512.05356v2 [cs.AI], 14 Dec 2025. This is a 9-page position paper, and v2 is the latest version. The stable URL is https://arxiv.org/abs/2512.05356. The arXiv-assigned DOI is 10.48550/arXiv.2512.05356 (inferred from arXiv's standard pattern, not printed in the text). The extracted text shows no license, and I did not do a web check.

### 2. Summary
The paper is a position piece. It argues that the field's current goal of autonomous, self-improving AI is misguided on two grounds: it is not the fastest route to superintelligence, and it is not the safest. The authors propose "co-improvement" instead. Under co-improvement, researchers build AI whose specific skill is collaborating with human researchers on AI research, covering the whole pipeline from ideation to experiments. The claimed payoff is faster progress and more safety. Humans stay in the loop, which gives more transparency and steerability. The paper also argues that autonomous self-improvement risks goal misspecification, for example a system whose idea of "solving AI" ignores human needs.

The paper first surveys self-improvement (Table 2). It runs from classic parameter optimization, through self-training, self-play and synthetic data, and self-reward, to architecture or code self-modification and recursive self-improvement. Table 1 then lists the activities where co-improvement should be targeted. These are problem identification, benchmark creation, method ideation, experiment design, execution, error analysis, safety and alignment co-development, systems co-design, integration into real-world systems, scientific communication, and "collective intelligence & group research".

The proposed method is to build benchmarks for research-collaboration skills, then build training data and methods that improve on them. This mirrors how coding skills have been improved. The authors expect that over time AI will take on more of the workload. The end state is "co-superintelligence", where AI augments humans broadly.

The evidence is argumentative. It rests on examples of past AI paradigm shifts and on citations to related work. The paper reports no experiments, data, or prototype of its own.

### 3. Key concepts
- **Self-improvement**: AI that improves itself autonomously, "with no human in the loop". The paper breaks it into learnable axes (parameters, training data, objective, architecture, overall code). Sections "The quest for Self-Improving AI" and Table 2.
- **Co-improvement**: "bidirectional collaboration between humans and AI where each improves the other's ability & understanding over time". Humans build the first system, then collaborate with the AI on further improvement. Section "A better quest for humans" and the Figure 1 caption.
- **Co-superintelligence**: the end state in which both humans and AI have safer superintelligence through their symbiosis. It emphasizes "what AI can give back to humanity". Abstract and section "From co-improvement to co-superintelligence".
- **Research collaboration skills**: abilities of an AI to work with humans across the AI research pipeline, to be measured with new benchmarks and trained for directly. Sections "How do we do it?" and Table 1.
- **Table 1 categories**: collaborative problem identification, benchmark creation, method innovation, joint experiment design, collaborative execution, evaluation and error analysis, safety and alignment, systems co-design, integration into real-world systems, scientific communication, collective intelligence and group research, and bidirectional co-improvement.
- **Research quality vs. artifact production**: co-improvement aims to "improve research quality, rather than to accelerate research artifact production". This is the contrast with end-to-end AI scientist systems. Section "How do we do it?".
- **Managed openness**: reproducible, openly shared science, with openness limited only where needed to prevent harm. Section "Co-improvement and openness".

### 4. Evidence quality / nature of the argument
- This is a conceptual, programmatic position paper. The paper contains no experiments, data, or sample sizes.
- The claims that co-improvement is faster and safer are asserted, not demonstrated. The supporting reasoning is that humans in the loop allow steering, and that targeted skill-building has worked for coding.
- Some claims are speculative. Examples are "we may be able to develop systems that are super-human at ML theory, so we could have provably safe AI", and the hope that the same approach extends to other fields.
- The only limitations stated are that AI is "not mature enough yet to fully self-improve", that coding "isn't solved either", and the caveat "if done correctly". The paper does not discuss how humans could stay useful if AI far outpaces them. It also does not consider how collaboration itself could be misused or fail.
- The authors are from a lab that works on both self-improving and research-agent systems, and they cite their own earlier work. The paper says it was written with AI help.

**Required comparison points**

*How co-improvement differs from self-improvement (precisely):*
- **Loop membership.** Self-improvement "seeks to eliminate humans from the loop as quickly as possible". Co-improvement keeps human researchers in the loop at each step.
- **Direction of benefit.** Self-improvement is "autonomous model updates". Co-improvement is "joint progress", where "humans help the AI achieve greater abilities, while the AI augments human cognition, research progress, and general capabilities outside of research". Improvement is meant to flow both ways.
- **Starting point and endpoint.** Both start from a human-built seed system. The paper expects the end state of both to be a superintelligent system that can self-improve. The claimed difference is that humans are present at every step, so there are more chances to steer.
- **Targeted skill.** Co-improvement makes research collaboration with humans the explicit training target, not the model's own autonomous gains.
- **Objective.** Co-improvement aims at research quality, not at paper production by full automation.
- **Not a rejection of the self-improvement methods.** Table 2 techniques are presented as the existing landscape, not rejected one by one. The paper never says which of those techniques co-improvement would keep or drop.

*Scope: AI research only, or science generally?*
- The primary, stated scope is AI research. Sections "A better quest for humans" and "From co-improvement to co-superintelligence" give the "first goal" as improving our ability to research improving AI, and Table 1 is entirely about AI development activities.
- The paper then says the goals "could shift" toward "co-improvement on all kinds of research or important topics to humanity".
- The openness section says co-improvement could help "any other field of science as well".
- The societal section mentions helping "with many other societal issues".
- The generalization is a stated vision with no mechanism, no examples, and no evidence. The paper presents it as a later step, not a developed claim.
- The paper contrasts itself with the AI co-scientist system (biomedical domain) as a related practical system, but not for AI research.

*Communities and institutions, or only human-AI pairs or teams?*
- The paper does not address institutions. It names no funders, journals, labs-as-organizations, peer review, or governance structures, and it has no model of the scientific community.
- The unit of analysis is mostly human researchers collaborating with AI, in pairs or teams. This is implied by terms like "work with human researchers" and "human-AI collaboration", and by examples such as co-drafting and co-running experiments.
- The only group-level element is one row in Table 1, "Collective intelligence & group research" (multi-human and AI collaboration to aggregate viewpoints, structure debate, and synthesize consensus). It is a one-line mechanism description, not developed.
- The societal section repeats this idea at the society level: "Multi-human and AI collaboration could help aggregate viewpoints, structure debate and help humans come to positive conclusions".
- The openness section touches the scientific community in one respect. It endorses reproducible, openly disseminated science and "managed openness". It notes that some industrial labs are shifting away from openness. This is the closest the paper comes to an institutional claim. It is a normative aside, and the proposal is not built on it.

### 5. Notable passages
- "We advocate that a more achievable and better goal for humanity is to maximize co-improvement: collaboration between human researchers and AIs to achieve co-superintelligence." (Abstract)
- "This is distinct from the goal of self-improving AI, which seeks to eliminate humans from the loop as quickly as possible, where AI performs its own research and learning autonomously." (A better quest for humans)
- "Crucially, in contrast to recent end-to-end AI scientist approaches [11, 15] the goal is to improve research quality, rather than to accelerate research artifact production (such as papers) via full automation." (How do we do it?)

### 6. Confidence
I read the whole paper, including the tables and the reference list. The extraction of the figure was garbled, so I relied on its caption.
- The following come directly from the text:
  - The framing, definitions, and Table 1 and Table 2 contents (sections "The quest for Self-Improving AI" through "Conclusion").
  - The self-improvement contrast (Figure 1 caption and "A better quest for humans").
  - The AI-research scope and its extension to other fields ("From co-improvement to co-superintelligence", "Co-improvement and openness").
  - The group-level mentions (Table 1 and the societal-harms section).
- The following are my inference:
  - "Pairs or teams" as the implied unit of collaboration. The text never states this.
  - The absence of institutional analysis. This is a negative finding from reading the paper, not a statement the paper makes.
  - My characterizations of the authors' lab context.
  - The DOI pattern.
- I skimmed the reference list for content and used it only to identify cited positions. I did not verify any cited work.

## Relevance to this project (repo-context agent)

1. **Tier**: STRETCH. It is a 9-page programmatic position paper with no data. Its scope is AI-research labs, and it says nothing about verification, trust, auditability or allocation.

2. **Bearing on the RCI thesis**: BOTH, weakly. It SUPPORTS the "RSI unnecessary" half, because it argues against autonomous self-improvement and keeps humans "at each step of the loop". It does not name RCI. The nearest it gets is the "bidirectional co-improvement" and "collective intelligence & group research" rows of Table 1, and the societal-harms line about aggregating viewpoints. The unit is the human-AI researcher pairing and the lab, not the community or its institutions, so it is far from RCI. It also CHALLENGES the thesis. Its stated end state "will be a superintelligence system with ability to self-improve", so it concedes the RSI endpoint and argues only about the path. It cites no evidence that the collaboration route beats autonomy. Its "faster and safer" claims are asserted, and the authors work at a lab that builds research agents.

3. **Loop step(s)**: Mostly steps 3 and 4, with some step 5, since Table 1 covers ideation, experiment design and execution, and error analysis. Beyond these, the openness paragraph touches "norms". The authors' scope is AI research, and the extension to all science is an unelaborated aside.

4. **What it gives this project**:
- A citable prior framing of "humans stay in the loop" as the safer design. It is a useful foil for the project's sequencing (substrate, then critics, then generators).
- The "research quality, not artifact production" contrast with end-to-end AI-scientist systems, which parallels the project's concern about end-to-end benchmarks.
- A taxonomy of self-improvement axes (Table 2) that could name what "RSI" means in the repo.

5. **Where it stops**:
- No verification, trust, cost or allocation analysis.
- No institutions, peer review, or funders (this is the summary's negative finding; the full text is consistent with it).
- No mechanism for keeping humans useful if AI outpaces them.
- No analysis of collaboration failing, being gamed, or producing slop.
- The generalization to other sciences is one sentence with no mechanism.

6. **Bearing on repo claims**:
- `CLAUDE.md` "easier than RSI, includes humans": supported only in spirit. The paper is about AI development, and its human-in-loop is individual researchers.
- `CLAUDE.md` "Sequencing: substrate (STAMPED) → critics → generators": complicated. The paper's targets are collaborators and generators, with no verifier layer.
- `docs/ai-in-the-loop.md` "find the loop with a verifier": untouched. The paper names no verifier.
- ANNOTATED_BIB cross-cutting 3 (a verifier invites optimization): not engaged. Its "if done correctly" and goal-misspecification worry gesture at the same risk but are not developed.
- ANNOTATED_BIB cross-cutting 7 (auditability is constitutive): weakly gestures at it, since "reproducible science with openly disseminated results, so others can verify or build on them" is a norm statement only.

7. **Links to existing entries**:
- Hardt: contrast between its measured community loop and this paper's asserted lab-level collaboration.
- Brain Researcher: it is a concrete human-in-loop critic and audit bundle, where this paper only advocates the principle.
- Longino and Strevens: the community-level treatment this paper lacks.
- ARC-AGI-3 and the lee3j case: a Goodhart risk on its proposed "research-collaboration benchmarks", which the paper does not note.

8. **One-line take**: Position paper arguing human-AI co-improvement over autonomous RSI; useful as a named foil, empty on community, verification and allocation.

9. **Confidence**:
- Resting on the summary and full-text check: the AI-research scope, the lack of experiments, the quoted passages, the openness and collective-intelligence mentions, the end state quote, and the absence of institutional content. I grepped the full text for "institution", "peer review" and "community" and found nothing substantive.
- Resting on background knowledge: that the authors are from FAIR and the field context.
- My inference, so guesses: that "pairs or teams" is the unit, that the paper has no verifier layer, and that the Goodhart risk applies to its proposed benchmarks. The STRETCH tier is a judgment call. A HIGH case could be made on the prior-naming criterion, but I think the paper is too distant from RCI for that.
