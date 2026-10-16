# Hardt, The Emerging Science of Machine Learning Benchmarks (2026)

Status: agent-generated 2026-10-16, not yet reviewed by a human.
Five summary agents (no project context) each read one chapter group in full from https://mlbenchmarks.org; Ch9 is not on the site.
One relevance agent read the repo plus all five summaries.
Each section ends with its own confidence notes; treat anything marked inference as unverified.

## Summary (context-free agents)

### Part A: Preface, Prologue, Ch 1-3

#### 1. Citation details found

- From the text (Ch 1, 2, 3 headers, all identical): "@book{hardt2026emerging, title = {The Emerging Science of Machine Learning Benchmarks}, author = {Moritz Hardt}, publisher = {Princeton University Press}, year = {2026}}". Each chapter PDF carries "Preprint available at https://mlbenchmarks.org".
- Preface and Prologue pages (web text): "© 2025–2026 Moritz Hardt. All rights reserved." Preface "Last update: Thu May 21 06:42:03 CEST 2026"; Prologue "Last update: Sat Mar 7 09:03:08 CET 2026". So the online text is a copyrighted preprint with no open license stated in my part, and it is a moving draft, not the print edition.
- Preface acknowledgments: Hallie Stabbins of Princeton University Press advised on publishing. Author taught a one-semester course at the University of Tübingen (Fall 2024 and 2025). The preface says a full set of homework exercises will be available online. It also says ChatGPT, Claude, and Gemini assisted with spelling, grammar, coding, and matplotlib/tikz figures.
- Web search (not from the text): Princeton University Press hardcover ISBN-13 978-0691284293 (ISBN-10 0691284296), about 376 pages, listed publication date October 6, 2026 (retailer and press listings). The De Gruyter eBook ISBN is 9780691284309. An Amazon Kindle listing gives 978-0691298818, which conflicts with De Gruyter, so check the eBook ISBN before citing it. The search was one query. I did not open the listings, so the publication date and page count are search-snippet level.
- Edition: no edition statement found in my part.

#### 2. Per-chapter summary

**Preface.** Hardt opens with the "one simple trick" of ML: split data into train and test, allow anything on the training set, rank models on the test set. He grants the standard critiques (narrow objectives, gaming, Goodhart's law, overfitting to artifacts, poor transfer, bias, exploited annotator labor, industry advantage) and says "All of this is true." His claim is that the scientific case for benchmarks is much less clear than the case against them. Benchmarks drove progress (ImageNet, MMLU, DeepSeek R1 vs o1) without scientific principles, and practice contradicted the statistical advice to keep test sets in a vault. He then previews the book. Part 1 (ImageNet era) covers the holdout method, adaptivity, Freedman's paradox, and the replication crisis. It reports three empirical facts: accuracies do not replicate across datasets, rankings do, and rankings often replicate even under different conditions. Part 2 (LLM era, from Ch 10) covers training-data contamination, multi-task aggregation and social choice, performativity, and LLM judges. He also gives audience and scope notes and acknowledgments.

**Prologue.** A short anecdote from summer 2015. A new Google hire gets 15 minutes with Ilya Sutskever and asks what learning rate he uses. Sutskever answers ".1", seriously and without elaboration. The text sets the scene with Google Brain, the NaN failures of too-large learning rates, the wasted runs of too-small ones, and researchers trading heuristics "like Pokémon cards". The Noogler never learns what was meant, but later decides the secret was not the learning rate, the optimizer, or the architecture, and that "the lesson was something else." The lesson is left unstated. The reader is meant to infer, in light of the rest of the book, that what mattered was the shared evaluation setup, not any particular knob (my inference).

**Ch 1 Introduction.** Opens with Feyerabend's "anything goes" and argues early pattern recognition (Rosenblatt's perceptrons, Hayek's influence) and today's ML both embrace it. Researchers are unconstrained in method, so a science of what practitioners do is hard to build. The "tragedy of anything goes" was that in the early field it became hard to tell what worked best. The fix was empirical, quantitative testing on held-out data, which is an instance of Strevens's "iron rule". The ImageNet era section covers ImageNet and CIFAR-10 (more than 15,000 papers on PapersWithCode), ImageNot, and the stability of model rankings, where accuracies move erratically but rankings hold. The LLM era section covers next-token training, scaling laws, alignment and post-training, task plurality, multi-task aggregation, MMLU, benchmaxxing, performativity, dynamic benchmarks, and LLM judges. The chapter closes with the call for a science of benchmarks.

**Ch 2 Populations and predictions.** Background chapter. It frames ML through Hacking's "astronomical conception of society", meaning populations treated as probability distributions, and notes that this is false of the real, dynamic world. "Distribution shift" starts "from a wrong premise". It defines prediction, the data-generating distribution, classification and regression, accuracy, and the accuracy-maximizing predictor (the most likely label given x, Prop 1). It covers the regression function as the minimizer of mean squared error (Prop 2), calibration and group calibration (Def 3, Fact 1), loss functions and risk (Def 4), and the optimal binary predictor under a general loss (Prop 3). It then covers base rates, the confusion matrix, precision/recall/F1/ROC, and model training. Empirical risk minimization, the generalization gap, and cross-entropy loss (Prop 4) are touched lightly because the book is about evaluation, not training. Model builders are treated as a given "computational resource". Examples use the 2018 California ACS census data and a streaming watch-time recommender. The chapter flags the self-fulfilling prophecy, where predictions influence targets, as a limit of the formalism, to be handled in Ch 13.

**Ch 3 Detecting differences.** Starts from the claim that benchmarking is fundamentally about comparing two models, and rankings are built from such comparisons. It reduces comparison on a test sample to distinguishing a fair coin from an epsilon-biased coin under the iid assumption. A mean-based test succeeds with n much greater than 1/eps^2 (Chebyshev, then the sharper Chernoff and Hoeffding bounds). A lower bound via total variation and Hellinger distance shows n of at least about 1/(2 eps^2) is necessary, with a special-case exception (a perfect predictor needs only about 1/eps samples). Back in benchmarking terms, the chapter derives that a difference of eps needs about 1/eps^2 test points, and that estimation error shrinks as 1/sqrt(n). Paired comparison of similar models needs only n much greater than delta/eps^2, where delta is the disagreement rate. Comparing k models costs only a log k factor (union bound or Bonferroni). Notes point to concentration inequalities, McDiarmid, and Le Cam.

#### 3. Key concepts

- **Anything goes**: Feyerabend's slogan ("The only principle that does not inhibit progress is: anything goes"), applied to ML. Method, architecture, optimizer, and tweaks are all unconstrained (Ch 1).
- **Tragedy of anything goes**: early pattern recognition produced many claimed advances shown in eclectic demos, and nobody could tell what worked best (Ch 1).
- **Iron rule**: Strevens's term; all disputes between scientists are settled by competitive empirical testing. Scientists may think and do whatever they like, but follow the rules of the competition. Benchmarking is ML's version: "Anything goes on the training set, competitive ranking on the test set" (Ch 1).
- **Benchmark**: a train/test split plus a ranking of models by test performance, which model builders compete over (Preface, Ch 1).
- **Crisis**: Hardt applies the word to the statistical sciences (failed replication, false discovery, p-hacking, Freedman's paradox; Preface) and to LLM-era evaluation (Ch 1). He argues ML's preconditions for crisis exist but ImageNet-era rankings thwarted it (Preface). He does not define "crisis" formally in my part.
- **Stability / replication of model rankings**: accuracies change from benchmark to benchmark, but "if one model beats another in one benchmark, it's likely to beat the same model in a different context" (Ch 1). The ImageNot experiment is the main example. The Preface states three empirical facts (accuracies do not replicate, rankings do, rankings show external validity).
- **No second-guessing guarantee**: a good ranking tells you the top model is the best starting point, so you need not try the other models (Ch 1).
- **Holdout method / adaptivity**: the train/test split; adaptivity is the feedback loop from repeated use that invalidates classical analysis (Preface).
- **Goodhart's law; researcher degrees of freedom**: statistical measures break down under competitive pressure (Preface).
- **Benchmaxxing**: choosing training data that best anticipates the test set, since LLM-era benchmarks usually have no shared training set (Ch 1).
- **Multi-task benchmark / aggregation**: combining many task rankings into one, a social-choice problem with no perfect solution. Preface claim: more task diversity means more sensitivity to irrelevant changes, such as adding weak models.
- **Performativity**: deployed models influence future data, so there is no model-independent ground truth (Preface, Ch 1).
- **Dynamic benchmarks**: benchmarks that evolve as models improve, trying to make a virtue of feedback loops.
- **LLM-as-judge**: biased toward itself. Preface claim: at the evaluation frontier, optimal debiasing is no better than collecting twice as many ground-truth labels.
- **Astronomical conception of society** (Hacking): populations as probability distributions. Hardt says there is "no distribution to begin with" and that "distribution shift" begins from a wrong premise (Ch 2).
- **Model builders**: Hardt's term for those who do training, treated as given (Ch 2).
- **Risk / empirical risk / generalization gap**: expected loss over the population; sample-average loss; the difference between them (Ch 2).
- **Calibration**: among instances with predicted probability p, a p fraction are positive. It is unrelated to accuracy (Ch 2).
- **iid assumption**: sample points are independent draws from one distribution. Hardt says it is a lesser stretch than the earlier leap of treating the world as a distribution, and is justified by utility (Ch 3).
- **Quadratic sample law**: detecting a difference eps needs about 1/eps^2 samples. It is necessary and sufficient up to constants (Ch 3).
- **Disagreement rate delta(f,g)**: the fraction of test cases where exactly one of two models errs. Paired comparison needs n much greater than delta/eps^2 (Ch 3).

#### 4. Thesis threads

- Benchmarking is ML's version of Strevens's iron rule and works as a social and empirical practice that arose without theory. The book's aim is to explain why and when it works, not to defend or attack it. The critiques are conceded and the scientific case is the open question.
- The main export of benchmarks is model rankings, not accuracy numbers (Preface). Rankings replicated surprisingly well in the ImageNet era, which Hardt calls partly luck. The Preface also argues community norms matter, and that the holdout method has strong guarantees if the community only cares about the best model.
- The LLM era threatens this stability through five pressures: uncontrolled training data, task plurality and aggregation, performativity, saturation and weak human evaluators, and LLM judges. Ch 1 poses the question of whether the iron rule will "grind to a halt".
- Method is theory plus observation. Ch 2 and 3 set up a deliberately conventional supervised-learning foundation (populations, risk, iid, concentration bounds), while Ch 2 and 3 openly flag that the underlying assumptions are idealizations. The quantitative lesson to carry forward is the 1/eps^2 sample-size law, which sets how large a test set must be.

#### 5. Confidence

Directly from the text:
- Citation block and "Preprint available at https://mlbenchmarks.org": Ch 1, 2, 3.
- Copyright line, last-update dates, and the AI-assistance disclosure: Preface and Prologue web pages.
- The definitions of anything goes, iron rule, and the ImageNet/LLM framing: Ch 1. The Strevens quote "unreasonable on the face of it" is in Ch 1 (paraphrased there, so not safe as a direct quote).
- Verbatim quote: "Benchmarks are the mistake that made machine learning." (Preface).
- Verbatim quote: "Anything goes on the training set, competitive ranking on the test set." (Ch 1).
- Verbatim quote: "model rankings—rather than model evaluations—are the primary scientific export of machine learning benchmarks" (Preface; the exact wording is "Summarizing these lessons, model rankings—rather than model evaluations—are the primary scientific export of machine learning benchmarks").
- Verbatim quote: "sample requirements grow quadratically in the inverse of the difference we try to detect" (Ch 3).
- All Ch 2 and 3 definitions, propositions, and bounds are from the text.

Preview claims, not shown in my part: the Preface's claims about the holdout method's guarantees, the social choice result, the debiasing result ("no better than collecting twice as many ground truth labels"), and the performativity and replication results are previews. The evidence and proofs are in later chapters I did not read.

My inference:
- The Prologue's unstated lesson. The text says only "The lesson was something else."
- That "crisis" in the LLM era means chiefly the stability of rankings. The text names an "evaluation crisis" without defining it.
- The remark that Ch 2 and 3 conventionality is deliberate is supported by the Preface ("I stick closely to the canon"), but the reading of why is mine.

Not verified: publication date, page count, and ISBNs (web search snippets only).

### Part B: Ch 4-6

#### 1. Per-chapter summary

**Ch 4, The holdout method.** Hardt argues that you cannot test on the training set, because a model fit to a sample S makes the empirical risk R_S(f) a biased estimate of true risk R(f). His examples are a lookup-table predictor and the nearest neighbor classifier, which both get zero training error. The holdout recipe is to split data at random, train on one part, and test on the other, with "anything goes" on training and an "iron rule" on testing. For a fresh iid test set, the error is about 1/sqrt(n). Hoeffding's bound and a union bound for k candidate models give error of about sqrt(log k / n), so many models can be compared cheaply. The catch is the "iron vault": the guarantees hold only for a fresh test set. Duda and Hart (1973), Torralba and Efros (2011), Francis Bach and Hastie et al. are quoted warning against reuse. Hardt says this is incompatible with benchmarks. He separates three uses of a holdout set (development signal, ranking, capability measurement), covers Kaggle's three-way split, k-fold cross-validation, error bars, the Bootstrap, and internal versus external validity.

**Ch 5, Test set reuse.** This chapter models how people actually use test sets, which is repeatedly and adaptively. Evaluations inform the next model, which forms a feedback loop ("adaptive data analysis"). An analyst is represented as a data-independent tree of depth k and degree n+1. Applying the Ch 4 union bound to that tree gives an adaptive bound of about sqrt(k log n / n), versus sqrt(log k / n) non-adaptively. That is exponentially worse in k. A lower bound shows this is tight: "overfitting by ensembling" picks k random predictors, keeps those that beat chance on the test set, and takes a majority vote. This forces a gap of order sqrt(k/n), about 10% after 1000 queries at n = 10,000, with a proof sketch in three steps. Noise addition based on differential privacy improves the dependence to about k^(1/4), allowing roughly n^2 queries, and quadratic is the limit. Hardt then covers Freedman's 1983 paradox (selecting variables with p < 1/4, then running an F-test, biases p-values downward), which is related to p-hacking. The Notes cite the Heritage Health Prize attack (rank 146 to 6 in 700 queries) and Blum and Hardt's Ladder.

**Ch 6, Scientific crisis.** The chapter turns to the replication crisis in the statistical sciences, as a lesson for ML. It starts from a primer on p-values as tail probabilities, with significance level, power and false positives. It then cites the Open Science Collaboration (2015) study of 100 psychology studies, where only 36% of replications reached p < .05 and 47% of original effect sizes fell inside the replication's 95% interval. Hardt walks through Ioannidis's Bayes-rule calculation (PPV 0.64 at alpha 0.05, power 0.8 and prior 0.1, falling to 0.48 with publication bias u = 0.05). He covers Meehl's argument about auxiliary assumptions, Simmons, Nelson and Simonsohn's "researcher degrees of freedom", and Gelman and Loken's "garden of forking paths". He covers Bonferroni correction and pre-registration, and notes Tukey and Box supported adaptive analysis. He closes with Goodhart's law: p-values pile up just below 0.05 across Scopus-indexed papers (de Winter and Dodou). He says the law should also apply to benchmark numbers such as ImageNet accuracy.

#### 2. Key concepts

- **Risk R(f) / empirical risk R_S(f):** population expected loss, and its average over a sample.
- **Training set vs test (holdout) set:** the test set must be independent of how f was built.
- **Generalization gap:** Delta_S(f) = R(f) - R_S(f). Overfitting is the loose term for a large gap.
- **Holdout method:** random train/test split. Gives an unbiased estimate with error of about 1/sqrt(n). Needs n of about 1/eps^2 for eps accuracy.
- **Model selection bound:** with k fixed candidates, error grows like sqrt(log k / n) (union bound).
- **Iron vault:** the textbook rule of using the test set once, at the end.
- **Three uses of a holdout set:** development signal (least demanding), ranking, and capability measurement (most demanding, needs construct validity).
- **Three-way split / k-fold / leave-one-out CV:** variants. A validation set is still subject to selection bias, and k-fold variance gains are heuristic.
- **Confidence interval / error bars / Bootstrap:** quantify sampling noise only. They measure internal validity, not external validity.
- **Internal vs external validity:** generalization to more of the same vs to different populations.
- **Adaptive data analysis / adaptive analyst:** queries chosen depending on earlier answers, as opposed to non-adaptive.
- **Overfitting by ensembling:** attack that boosts weak random predictors using only test-set scores.
- **Reusable holdout / differential privacy:** noisy answers that allow about n^2 queries.
- **Freedman's paradox / inference after selection:** selecting variables and then testing on the same data biases p-values.
- **p-value, null model, significance level, power, PPV:** p-value is a tail probability under the null. Power is the true positive rate. PPV is the post-study probability that a finding is true.
- **Publication bias:** results get published regardless of truth with probability u.
- **Researcher degrees of freedom / p-hacking / HARKing / garden of forking paths:** flexible analysis choices, including ones made without conscious fishing.
- **Pre-registration:** forces a non-adaptive analysis.
- **Goodhart's law:** a statistical regularity tends to collapse once it is used for control. Related: Campbell's law.

#### 3. Thesis threads

- **Benchmarks violate the textbook rule.** Ch 4 sets the rule: iid fresh test set, use once. A benchmark by definition reuses the test set, so classical guarantees do not apply. Ch 4 also frames the log k bound as the optimistic yardstick.
- **Theory gives a best case and a worst case.** Ch 5 supplies the pessimistic adaptive bound (sqrt(k)) plus a concrete attack. Hardt says both are useful and sets up the puzzle that benchmarking "seems to successfully avoid the worst-case bounds", with explanations promised in Ch 8.
- **Adaptivity is also a feature.** Ch 5 and 6 both note that incremental, adaptive work is needed for science (Tukey, Box, Gelman and Loken). Pre-registration is "a non-starter" in ML, so ML cannot cut researcher degrees of freedom.
- **Competition and incentives erode metrics.** Ch 6 uses the replication crisis and Goodhart's law to argue ML should expect trouble, which Ch 7 then tests against how ML actually fared.

#### 4. Confidence

**Directly from the text:**
- Ch 4: the lookup table and nearest neighbor examples, the 1/sqrt(n) and sqrt(log k / n) results, the vault quotes (Hastie et al., Bach, Duda and Hart, Torralba and Efros), the three uses of a holdout set, the Kaggle split, the CV discussion, confidence interval methods, and the internal/external validity distinction.
- Ch 5: the adaptive bound, the lower bound (Prop. 2), the figure of "A thousand queries force a generalization gap of 10%", differential privacy and the quadratic limit, Freedman's paradox, and the Heritage Health Prize rank 146 to 6 in 700 queries (Notes).
- Ch 6: the OSC 36% and 47% figures, the Ioannidis PPV values 0.64 and 0.48, the Meehl, Simmons et al. and Gelman and Loken arguments, and Goodhart's law with the p-value discontinuity.

**My inference or paraphrase:**
- The thesis-thread framing is my synthesis. For example, I link Ch 5 and 6 on adaptivity myself, though Ch 6 does say Tukey and Box advocated adaptivity "in the previous chapter".
- The labels "optimistic" and "pessimistic" bounds are close to Hardt's wording, but "best case and worst case" is my paraphrase of the passage "One tells us the best that we can hope for. The other shows the worst that could happen."
- I did not verify the cited studies or numbers beyond what the chapters state. The Ioannidis inputs (prior 0.1, u = 0.05) are explicitly "a guess" in the text.
- I did not read any material from the rci-explorer project.

### Part C: Ch 7-8

#### 1. Per-chapter summary

**Ch 7, Replication in machine learning.** Hardt first grants that the preconditions for a replication crisis exist in ML. Papers appear in huge volume. Peer review is noisy: in the 2014 NeurIPS experiment, 166 papers went to two independent panels, and only about half of the papers one panel accepted would have been accepted by the other. Researcher degrees of freedom are extreme, there is no preregistration, and test sets like CIFAR-10 and ImageNet are reused in data-dependent ways. He then separates three replication bars: code re-execution (reproducibility), replication in similar conditions (internal validity), and replication in different conditions (external validity). Absolute accuracy numbers fail the external bar. Torralba and Efros (2011) showed that benchmarks are easy to tell apart, and accuracy drops across datasets are typically double digit. This is distribution shift. DomainBed and WILDS show that nothing beats plain empirical risk minimization. Rankings fare much better. The Recht et al. ImageNet and CIFAR-10 test set reconstructions, Yadav and Bottou's MNIST lost digits, and a Kaggle public/private leaderboard meta-study all show accuracy dropping while rankings hold ("on the line"). Kornblith et al. (transfer to other benchmarks), ObjectNet, and the ImageNot toy dataset (same model ranking as ImageNet) suggest rankings also have some external validity. Hardt's explanation is that cardinal measurement breaks under competitive pressure (Goodhart's law) while ordinal ranking survives.

**Ch 8, Forces against crisis.** The chapter asks why a decade of heavy ImageNet test set use did not wreck the benchmark, given the adaptive overfitting results of earlier chapters. The answer is mainly social and psychological, not statistical. First, the community focuses on beating the previous best, which fixes test set, metric and protocol and cuts researcher freedom. The Ladder mechanism (Blum and Hardt) reports a new score only when it beats the best so far by a margin. It has leaderboard error O(log^(1/3)(kn)/n^(1/3)), proved by a tree-compression argument, and researchers' "SOTA psychology" acts as a social version of it. Second, cognitive biases (anchoring, recency, availability) limit information flow from the test set, per Zrnic and Hardt's contractive analyst model. Third, Arora and Zhang's Rip Van Winkle argument bounds the ResNet-152 overfit at about 5% from roughly 1032 bits. Fourth, many classes (ImageNet's 120 dog breeds) make test set attacks harder (Feldman, Frostig, Hardt). Fifth, code and dataset sharing raises model similarity, which acts like evaluating fewer models, and Donoho's "frictionless reproducibility" speeds iteration. Kaggle and the Netflix Prize contrast productivity with science. The chapter ends with two conditions for good benchmark design: one interesting solution exists, and leaderboard climbing tracks real risk reduction.

#### 2. Key concepts

- **Code re-execution / reproducibility**: rerunning released code and data in essentially identical conditions. A minimal bar only.
- **Internal validity (Hardt's pragmatic sense)**: a claim holds when generalizing to more of the same population, e.g. a fresh ImageNet-style test set.
- **External validity**: a claim holds under different populations or conditions.
- **Dataset bias / distribution shift**: each benchmark has a recognizable "fingerprint", so models drop accuracy, often by double digits, across datasets or small changes. Related remedies: domain adaptation, domain generalization, transfer learning.
- **Benchmarks for shift**: DomainBed (Colored and Rotated MNIST) and WILDS (10 real-world shift datasets).
- **Sutton's bitter lesson**: more data and bigger models usually beat clever algorithm design.
- **Label-noise point**: replacing 20% of labels with random ones maps accuracy A to 0.8A + 0.2/C, giving the same comparisons, so absolute accuracy has little meaning alone.
- **On the line phenomenon**: models cluster on a line when plotting old versus new test accuracy. A positive slope implies preserved rankings. Slope above 1 is evidence against strong adaptive overfitting. It breaks when models train on different data (CLIP is "off the line").
- **ImageNot**: toy 1000-class web-crawled dataset (LAION-5B, no annotators) used to stress-test ranking stability.
- **Cardinal versus ordinal measurement**: absolute numbers lack validity under competition, rankings are more robust.
- **Leaderboard error**: the max over time of the gap between the reported score and the best true risk seen so far.
- **Ladder mechanism**: report a new best only if it beats the previous best by margin η. Otherwise repeat the old score.
- **SOTA psychology / social algorithm**: the community's habit of caring only about beating the previous best acts like the Ladder.
- **Bounded rationality, cognitive biases**: Simon and Kahneman/Tversky ideas, here used to model analysts that leak less test set information.
- **Compression argument**: B bits revealed about the test set means at most 2^B functions are reachable, so gap is about sqrt(B/n).
- **Rip Van Winkle's replication problem**: counts how many bits about the test set are needed to rebuild a modern model from 2012 knowledge.
- **Model similarity**: highly similar models behave like fewer models, which gives better holdout bounds.
- **Frictionless reproducibility (Donoho)**: easy datasets, code re-execution, and challenges.
- **Benchmark design conditions**: at least one interesting solution exists, and climbing the leaderboard corresponds to lowering risk.

#### 3. Thesis threads

- ML has the statistical Achilles heel but did not suffer the same crisis. The book's distinction is that accuracy numbers do not replicate while model rankings do, which supports the "iron rule" (settle disputes by competitive empirical testing) as a valid ranking tool.
- Ch 7 gives empirical evidence for internal validity, plus limited and incompletely understood external validity, of rankings. Ch 8 gives theory and sociology for why, extending the holdout analysis of earlier chapters (Chs 4 and 5).
- Resilience is explained by community norms (SOTA chasing, biases, code sharing, quirky benchmark design), so the metascience of benchmarking is not purely statistical.
- Resilience is not sufficient: benchmarks can fail if no good solution exists (Fragile Families) or leaderboard climbing diverges from the task. Ch 8 sets up the failure modes in Part II (Ch 10 onward) and the caveat about models trained on different data (Chs 10 and 11).

#### 4. Confidence

**Directly from the text:**
- Ch 7: the 2014 NeurIPS experiment (166 papers, about half agreement), the three replication bars, Torralba and Efros, DomainBed and WILDS findings, the 0.8A + 0.2/C formula, the Recht et al. results (accuracy drops, rankings preserved, ImageNet slope 1.11, CIFAR slope 1.69 per the figure), MNIST lost digits, Kaggle meta-study, Kornblith et al., ObjectNet, ImageNot (identical ranking of 9 architectures), the NeurIPS 2019 reproducibility challenge (173 papers claimed), and the Notes on Henderson, Kapoor and Narayanan, etc.
- Ch 8: Ladder definition and Theorem 1, the table of rates (2/5 exponent for a randomized Ladder), SOTA psychology, bias discussion, Rip Van Winkle (about 1032 bits, about 5%), the multiclass attack (3% gap with 5000 queries), model similarity, Donoho, Kaggle versus science, and the two conditions for benchmark design.
- Short quotes: "When a measure becomes a target, it ceases to be a good measure" (Ch 7, Strathern paraphrase); "Scientists hold the steering wheel" (Ch 8).

**My inference (not stated this way in the text):**
- The reading that Part II (Ch 10 onward) addresses the "different training data" caveat is partly inferred from forward references (Chs 9, 10, 11 are mentioned).
- Framing the two chapters as one combined "rankings versus numbers, then why" argument is my synthesis.
- The text says "We don't fully understand why" rankings hold. The Ch 8 explanations are described as "emerging", so they are candidate explanations, not established causes.
- The Ladder-as-description-of-community claim is Hardt's modeling stance (a "social algorithm"), not an empirically tested result in these chapters.

### Part D: Ch 10-11

#### 1. Per-chapter summary

**Ch 10, Generative models.** Hardt argues that the ImageNet era ended when attention moved to transformer language models trained on internet text, and that this changed benchmarking. The chapter starts with why RNNs were hard to scale and how the 2017 transformer ("Attention Is All You Need") fixed that, helped by a lot of "alchemy" (Uszkoreit, Pavlick quotes). It then explains language modeling: tokenization, next-token probabilities, the negative log-likelihood loss, and perplexity. Perplexity is hard to interpret, depends on the tokenizer, and has a weaker concentration guarantee than accuracy. Bits-per-byte is the alternative, but it confounds tokenizer and model. Perplexity was still trusted because it tracked downstream results (the BLEU scatterplot from the transformer paper; Gadre et al. 2024). Section 10.2 covers scaling (BERT, GPT-1 to GPT-4, Common Crawl filtering, data scarcity and lawsuits). It gives the Kaplan and Chinchilla scaling laws, with C = 6ND and L = E + A·N^-α + B·D^-β, and the compute-optimal result of about 20 tokens per parameter. Hardt cautions that these laws are statistical regularities, citing Clauset, Shalizi and Newman on power laws and MacKenzie on Black-Scholes. They are also self-fulfilling and hold for loss, not necessarily downstream tasks. Section 10.3 reviews NLP's older benchmark culture (ATIS, TREC, Penn Treebank, MUC, CoNLL, WMT). It covers SQuAD, SNLI/MultiNLI, the Winograd Schema Challenge and Winogrande, LAMBADA, and GLUE/SuperGLUE, ending with Bowman and Dahl on saturation. Section 10.4 covers CLIP and LAION. CLIP appears robust out of domain, but "domain contamination" (Mayilvahanan et al.) means evaluators cannot know what a web-trained model has seen.

**Ch 11, Evaluating language models.** Hardt's claim is that alignment and post-training break the evaluation tools that worked for base models, and that direct evaluation of LLMs is confounded. Base models ramble (Llama-2 on "capital of France"), while aligned ones answer. Section 11.1 explains the post-training pipeline: supervised fine-tuning and instruction tuning (Alpaca), Bradley-Terry reward models, KL-regularized RLHF, DPO, SimPO, and verifiable-reward methods (best-of-N, RLVR, GRPO). Section 11.2 covers three protocols. Multiple choice is illustrated by MMLU and by TruthfulQA, where Turner and Kuzeja found simple tricks reach 73%, so the odd answer out gives it away. Human evaluation is illustrated by Chatbot Arena, which uses Elo, a special case of Bradley-Terry. It is open to System 1 judgments, sycophancy and overreliance, and Hardt calls it a "vibe check". Automated evaluation is LLM-as-a-judge and answer matching. Section 11.3 gives the central argument, from Dominguez-Olmedo, Dorner and Hardt: newer models beat older ones at equal pretraining compute on MMLU and GSM8k because they were trained on the test task. Giving all models the same fine-tuning removes the gap and the apparent emergence. The proposed fix is tune-before-test. The section also covers data contamination. Section 11.4 lists five evaluation modes (direct, prepared model, architecture, dataset, algorithm) and shows that Kendall's tau ranking agreement across benchmarks rises after tune-before-test (Zhang et al.). Performance then becomes close to one-dimensional.

#### 2. Key concepts

- **Language model**: a probability distribution over token sequences, factored by the chain rule into next-token probabilities (Ch 10).
- **Tokenization / vocabulary size**: splitting text into chunks (tokens). The choice affects both training and evaluation (Ch 10).
- **Perplexity**: exp of the negative average log-likelihood, the effective number of choices per token. Lower is better. It is tokenizer-specific, unbounded, and insensitive to task hardness (Ch 10).
- **Bits-per-byte**: a compression-based alternative to perplexity that confounds tokenizer quality with model quality (Ch 10).
- **Zero-shot, few-shot, in-context learning**: abilities that emerged with scale (GPT-2, GPT-3) (Ch 10).
- **Scaling law**: an empirical power-law fit predicting loss from parameters N, data D and compute C (C = 6ND). Chinchilla gives about 20 tokens per parameter (Ch 10).
- **Self-fulfilling prophecy**: following a model (scaling law, Black-Scholes) makes it more true (Ch 10).
- **Domain contamination vs sample contamination**: a test domain's style or content appears in training data, versus exact duplicates of test items (Ch 10).
- **Post-training / pretraining / base model**: the cultural split between broad next-token training and use-case-targeted, benchmark-aware fine-tuning (Ch 11).
- **SFT / instruction tuning**: fitting prompt-completion pairs by negative log-likelihood (Ch 11).
- **Bradley-Terry preference model, reward model**: P(y1 beats y2) = sigmoid of the reward difference (Ch 11).
- **RLHF, DPO, SimPO, RLVR, GRPO, best-of-N**: preference and reward optimization methods (Ch 11).
- **Shortcut learning**: answering without doing the intended task, as in TruthfulQA's odd-one-out (Ch 11).
- **Chatbot Arena / Elo**: pairwise human votes turned into online ratings (Ch 11).
- **LLM-as-a-judge, answer matching**: models scoring other models' outputs (Ch 11).
- **Emergent ability**: performance that jumps at some scale and cannot be extrapolated from smaller models (Ch 11).
- **Training on the test task**: adding task-relevant data (formats, instructions) to training. This is distinct from training on the test set and is generally not considered cheating (Ch 11).
- **Tune-before-test / prepared model evaluation**: give every model the same task adaptation before comparing, so the comparison is "net-of-effort" and "regret-free" (Ch 11).
- **Direct model evaluation**: black-box evaluation of models as they are, controlling only for test inputs (Ch 11).
- **Five evaluation modes**: direct, prepared model, architecture, dataset (DataComp) and algorithm (Ch 11).
- **Kendall's tau**: a rank-agreement measure used for ranking agreement across benchmarks (Ch 11).
- **Intrinsic vs extrinsic evaluation**: Galliers and Spärck Jones's distinction, discussed in the notes (Ch 11).

#### 3. Thesis threads

- **The holdout method's control assumption breaks.** In the ImageNet era all models shared training data, so test-set rankings had external validity. With internet-scale pretraining and opaque post-training, training data becomes a competitive variable (CLIP in Ch 10, MMLU in Ch 11). Comparisons are then confounded.
- **Perplexity and scaling laws were the stable signal; downstream benchmarks are not.** Ch 10 shows that perplexity tracked downstream gains and supported scaling laws, but that laws for downstream tasks do not hold. Ch 11 argues that apparent emergence partly reflects uneven task preparation, and that tune-before-test restores agreement between perplexity and downstream rankings.
- **Benchmarks as measurement of latent constructs tend to fail.** Winograd/WSC, GLUE/SuperGLUE saturation, TruthfulQA shortcuts, and Arena's reliance on human heuristics all show benchmarks intended to measure reasoning or truthfulness being solved or gamed by other means. Incentives and Goodhart-style optimization drive this.
- **A constructive methodological response.** Hardt proposes controlling for more of the pipeline (tune-before-test, prepared and dataset evaluation) and checking ranking agreement, rather than abandoning benchmarks. The chapters point ahead to Ch 12 (one-dimensional benchmark performance), Ch 13 (feedback loops) and Ch 14 (LLM judges).

#### 4. Confidence

**Directly from the text**
- Ch 10: the RNN-to-transformer history, the definitions of perplexity and bits-per-byte, the scaling-law formulas and Chinchilla constants, the dataset sizes, the CLIP and LAION account, the cited studies, and the statement that scaling laws are self-fulfilling and not physical laws.
- Ch 11: the post-training methods and derivations, TruthfulQA (22.4% to 41.3% accuracy for GPT to InstructGPT; 73% from tricks per Turner and Kuzeja), the Arena/Elo discussion, the MMLU and GSM8k regression story, the tune-before-test findings, the five evaluation modes, and the Kendall-tau results.
- Ch 11 states that, after tune-before-test, the first principal component explains "almost all variance in benchmark performance".
- Ch 11 states that evidence against reliable downstream scaling laws comes from the cited studies (Ch 10 notes).

**My inference or compression**
- The framing of the "holdout method's control assumption breaks" thread is my synthesis. The text states the pieces (Ch 11 §11.4) but not as one slogan.
- Calling the Goodhart-style incentives a theme is my reading. The text uses "incentivized" and "iron rule" language but does not name Goodhart in these chapters.
- The forward pointers to Ch 12 to 14 are partly my reading. The text says "next chapter" (Ch 10 to 11, and Ch 11 on one-dimensionality) and names Ch 13 and Ch 14 explicitly for feedback loops and LLM judges. The description of Ch 12's content is inferred from "The next chapter develops this point in greater depth."
- Some section-level Ch 10 material was condensed heavily (the pre-transformer benchmark history), so named items beyond those listed are omitted rather than denied.

Short verbatim quotes: "Hallucination is the default rather than the exception." (Ch 11); "Training on the test task is a problem that is also its own solution." (Ch 11); "The older model isn't worse, it was just less prepared." (Ch 11).

### Part E: Ch 12-15

#### 1. Per-chapter summary

**Ch 12, The problem of aggregation.** Multi-task benchmarks bundle many tasks into one leaderboard because the community wants "one number" (the chapter quotes Jason Wei on single-number metrics). The chapter treats this as a voting problem: tasks are voters, models are candidates, and a benchmark is a voting system. Examples of aggregation: BIG-Bench (204 tasks, dynamic range normalization, subsets BBL and BBH), the Hugging Face OpenLLM leaderboard (v1 summed accuracies, v2 normalized above random; the Qwen1.5-32B-Chat ranking jumped from 57 to the top 10; retired March 2025), HELM (mean win rate, later replaced by mean score because win rate depends on which models are present), and Chatbot Arena (Elo as ranking aggregation). Social choice results follow: Condorcet's paradox, Borda count (equivalent to mean win rate), Arrow's theorem, Gibbard-Satterthwaite, and a water-filling model of strategic effort allocation. Empirically (Zhang and Hardt), diversity (1 minus Kendall's W) trades off against sensitivity to irrelevant models or metric transforms. The benchmark-model score matrix is near low rank, and PC1 tracks pretraining FLOPs.

**Ch 13, When the model moves the data.** Models deployed at scale change the data they are later evaluated on (performativity), which undermines the "astronomical conception" of a fixed distribution. The chapter opens with Oskar Morgenstern's 1928 argument that forecasts invalidate their own empirical base. It then gives the Grunberg-Modigliani and Herbert Simon fixed-point counterpoint (continuity of the response function guarantees a self-consistent prediction). It formalizes performative prediction with a distribution map, performative stability and optimality, and "learning versus steering." It lists five consequences for evaluation: no model-independent ground truth, static benchmarks may not transfer, random guessing can look accurate, human baselines are disrupted, and small A/B tests can mislead. A theorem on repeated risk minimization (with Jiduan Wu) shows convergence needs a stable signal. Feedback-loop stories (recommenders, predictive policing, lending, model collapse, bias amplification) are tempered by a warning from 1970s system dynamics (World3, Forrester). Dynamic benchmarks (Dynabench) are analyzed: Shirali et al. show progress can stall after three rounds in the worst case, and Bowman and Dahl warn of reduced diversity.

**Ch 14, Evaluation at the frontier.** Human annotation cannot keep up with frontier models, so models increasingly judge other models (a modern descendant of BLEU-style automatic evaluation). Judge bias is defined formally. Rankings stay correct only if bias is small and not model-dependent. Reported biases include verbosity, self-preference, and error oversight, and prompt injection can fool judges. Judge accuracy or agreement is not enough: with reference score 0.9 and agreement 0.9, bias can be plus or minus 0.1. If evaluated models are strictly better than the judge, rankings can fully reverse (MMLU with GPT-4 labels; Llama-3 70B labels on HELM models). Prediction-powered inference (PPI) debiases using a few reference labels. Dorner, Nastl and Hardt prove tuned PPI is optimal but gains at most a factor of 2 in effective sample size at the frontier. Restricted protocols follow: answer matching (MMLU-Pro example), rubrics (HealthBench), and verification (SWE-bench, GSM8k, FrontierMath, PutnamBench). "Real-world" benchmarks (SWE-Lancer, GDPval) are critiqued, as are simulation (Vending-Bench) and A/B tests.

**Ch 15, Epilogue.** The epilogue frames ML benchmarking as an engineering science. Vincenti's "experimental parameter variation" (Durand and Lesley's 1916 propeller tests) and Strevens' "iron rule" of competitive empirical testing are the touchstones. ML benchmarks lack physics as a guardrail and rest on statistics, which Goodhart's law says should break under competition. ML escaped this because it depends on rankings rather than absolute numbers, and rankings survive competitive pressure. The real threat to rankings is inequality: unequal preparation, opaque black-box APIs, and unclear start and finish lines. Hardt rejects both abandoning benchmarks and the idea that real-world agents will make them obsolete. He cites Spendolini's management definition of benchmarking as a continuous process, and expects benchmarking to spread into the sciences (protein structure, weather, Open Catalyst). He closes by quoting Strevens' plea not to meddle with the knowledge machine.

#### 2. Key concepts

- **Multi-task benchmark / aggregation problem:** combining per-task rankings (ranking aggregation) or scores (rating aggregation) into one overall ranking.
- **Tasks as voters, models as candidates:** the mapping that lets social choice theory apply to benchmarks.
- **Incommensurability:** task metrics have different units and different random-guess floors, so averaging them has no clean meaning.
- **Mean win rate / Borda count:** a rank-quantile average (equivalent to Borda up to scaling). It depends on which models are present.
- **Condorcet paradox / Condorcet winner:** majority preference can cycle, so there may be no winner.
- **Arrow's theorem:** with 3+ candidates, unanimity plus independence of irrelevant alternatives forces a dictatorship, i.e. a single-task benchmark in disguise.
- **Gibbard-Satterthwaite:** non-dictatorial voting systems with 3+ alternatives invite strategic behavior. Its benchmark analogue is strategic effort allocation.
- **Diversity (1 minus Kendall's W) vs. sensitivity ((1 minus tau)/2):** the empirical trade-off. More diverse benchmarks are more sensitive to irrelevant models and metric rescalings.
- **Performativity:** a model's predictions causally affect the outcomes it predicts, so there is no model-independent ground truth.
- **Distribution map D(theta):** the distribution that results from deploying model theta.
- **Performative stability vs. optimality; performative risk:** stable means optimal on its own induced distribution. Optimal means minimal risk after deployment.
- **Learning vs. steering:** two ways to lower performative risk. One fits current data, the other moves the data.
- **Repeated risk minimization / stable signal:** retraining converges if a deployment-invariant signal exists.
- **Data feedback loop / model collapse / bias amplification:** data and model co-evolve over time.
- **Dynamic benchmark:** a benchmark that adds the failures of current best models to its data (Dynabench).
- **LLM-as-a-judge; judge bias JB; agreement AG:** a model produces proxy scores. Bias is the expected proxy minus reference score. Agreement is how often they match.
- **Prediction-powered inference (PPI) and sample efficiency factor:** it uses a few reference labels to correct many proxy scores. The factor is the variance ratio relative to using the reference labels alone.
- **Restricted evaluation protocols:** answer matching, rubrics, and verification.
- **Iron rule (Strevens); experimental parameter variation (Vincenti):** the epilogue's frame. Competitive empirical testing settles disagreements and builds engineering knowledge without needing theory.

#### 3. Thesis threads

- **Rankings, not numbers, are the currency.** Ch 12 shows that even aggregating rankings is hard (Arrow, sensitivity). The epilogue says ML survives Goodhart's law because valid rankings are resilient to competition, while absolute scores mean little.
- **Equalization is the condition for valid rankings.** The epilogue's "inequality is the real threat" generalizes the book's earlier treatment of training on the test task. Ch 12 refers back to Ch 11's tune-before-test (near rank-1 under tune-before-test). Ch 14 names training on the test task as the confounder that defeats even "real-world" benchmarks like GDPval.
- **The evaluation frontier erodes the assumptions of static, fixed-ground-truth benchmarks.** Ch 13 (performativity, no model-independent truth) and Ch 14 (judges weaker than candidates, a factor-2 debiasing limit, benchmarks not equal to the real world) each show a limit. None leads Hardt to abandon benchmarking. Benchmarks and online experiments are described as complementary.
- **Benchmarking as an ongoing social process.** The epilogue draws on Spendolini and Strevens to say the iron rule should be maintained, not tampered with. The book is offered as a manual for "future engineers of science."

#### 4. Confidence

**Directly from the text:**
- Ch 12: the voting analogy; the BIG-Bench, OpenLLM v2 (rank 57 to the top 10; shut down March 2025), HELM win-rate vs. mean-score and Chatbot Arena descriptions; Condorcet, Borda, Arrow, and Gibbard-Satterthwaite; the water-filling effort model; the diversity-sensitivity regression figure; the low-rank matrix (70% and 86% variance on PC1 for direct and tune-before-test, from the figure); PC1 correlating with pretraining FLOPs. The notes credit Zhang and Hardt (ICML 2024) and Anthropic's remark that BIG-Bench was "unwieldy."
- Ch 13: Morgenstern (1928 habilitation); Grunberg-Modigliani and Simon; the definitions (distribution map, stability, optimality, performative risk); the five evaluation consequences; Claims 1 to 3 (credited to joint work with Jiduan Wu); the feedback loop stories; the system dynamics/World3 digression; Dynabench; Propositions 1 and 2 on the O(eps^2) stall (credited to Shirali, Abebe and Hardt).
- Ch 14: the judge setup, JB and AG definitions; Propositions 1 to 3; Theorem 1 (tau at most 2 when 0.5 <= AG <= b); the examples (MMLU with GPT-4 labels; Llama-3 70B 79% vs. GPT-4 84%; MT-Bench 85% agreement; MMLU-Pro air-mass question; HealthBench rubrics; SWE-bench; GSM8k; FrontierMath; PutnamBench; SWE-Lancer going offline; GDPval reaching a 70.9% win-or-tie rate for GPT-5.2). Notes credit Dorner, Nastl and Hardt (ICLR 2025) and Chandak et al. for answer matching.
- Ch 15: Durand and Lesley, Vincenti, Strevens, Spendolini, the rankings-over-numbers argument, the inequality point, and the closing quote ("Do not, then, meddle with the iron rule...").

**My inference or paraphrase:**
- The thesis threads are my synthesis. The text does not label them that way.
- "Equalization generalizes train-before-test" connects the epilogue to Ch 11 content that is only referenced in these chapters, not shown. Ch 12 does mention tune-before-test and the near rank-1 matrix.
- "Benchmarks and A/B tests are complementary" is stated in Ch 14 ("complementary tools... Neither is a substitute"). My claim that Hardt does not abandon benchmarking is from the epilogue's overall tone.
- I counted the epilogue's "Trojan horse" and "future engineers of science" lines as concluding statements. The text states them, but the weight I give them is my reading.
- The Ch 12 sensitivity-diversity relation is described by the text as empirical, "not a theorem."

## Relevance to this project (repo-context agent)

1. **Tier**: HIGH. It is the only source so far with a worked, evidenced account of a community that runs verification as a shared, cheap, competitive loop (the benchmark as a standing step 5), and it quantifies where that breaks.

2. **Loop step(s)**: 5 (benchmark as evaluation of an object), 2 and 5 → 2 (rankings as a trust signal that updates), 6 as a state (performativity, saturation), trust, norms (iron rule). Step 4 only indirectly. Steps 1 and 3 not covered.

3. **What it gives this project**
- Ch 1, 15 (iron rule): Hardt uses Strevens's rule as the normative core ("anything goes on the training set, competitive ranking on the test set"). It is a concrete instance of a norms layer with a verifier attached, so it extends the Strevens entry from philosophy to a working mechanism. Ch 15 adds the concern that the rule must be maintained, not meddled with.
- Ch 7 (replication): three bars (code re-execution, similar conditions, different conditions) give a vocabulary to split "reproducible" from "replicated". Evidence: accuracies fail to replicate, rankings mostly do ("on the line", ImageNot).
- Ch 7, 15 (rankings vs numbers): ordinal outputs survive Goodhart where cardinal ones do not. This is a design hint for a trust score: publish ranks or comparisons, not scalars.
- Ch 4, 5, 8 (adaptive reuse): sqrt(log k/n) non-adaptive vs sqrt(k/n) adaptive, with an attack. Ch 8 offers explanations for why ImageNet survived (SOTA psychology as a social Ladder, model similarity, bounded analysts). This turns "Goodhart" from anecdote into a quantified, mechanism-specific failure.
- Ch 12: aggregating into one number is a voting problem (Arrow, diversity vs sensitivity). Directly relevant to any single trust score.
- Ch 13 (performativity): deployed models move the data, so no model-independent ground truth.
- Ch 14: judge bias, a factor-2 limit on debiasing at the frontier, and rankings that reverse when candidates beat the judge. Restricted protocols (verification, answer matching) are the cases that work.

4. **Where it stops**
- ML only: shared data, cheap re-evaluation, a single scalar objective. Most science lacks all three.
- No treatment of verification cost allocation across a built-upon body, or dependency load.
- No attribution rule for blame after a failed evaluation.
- Ch 9 is absent from the summaries and the text files, so contamination is not assessed here.
- The explanations in Ch 8 are "emerging", not established.

5. **Bearing on repo claims**
- docs/prior-art.md, "No source covers verification allocation": largely stands. Hardt allocates nothing; but benchmarks are a standing allocation by default (everyone evaluates the same set), which complicates "allocation is distributed, not decided centrally".
- map.md "Binary gate... Trust frozen": complicated. Leaderboards are re-evaluation as a state, but only for a narrow class.
- map.md "6 is a state, not a gate": supported in spirit (Ch 13: no fixed ground truth), but performativity is a different mechanism from replication or retraction.
- CLAUDE.md "Auditability is constitutive": no support. Hardt's rankings rely on a shared protocol, not on inspecting artifacts.
- cases.md lee3j ("any benchmark for autonomous science is a scalar; a capable agent will do to it what this one did"): supported and sharpened. Ch 6 and 7 Goodhart, plus Ch 5's attack, show why scalars fail. It complicates the anecdote too: ML rankings survived heavy optimization, so the claim is "cardinal scalars", not "benchmarks".
- ai-in-the-loop.md "no verifier exists the way math has one": Ch 14 supports. Verification-based benchmarks (SWE-bench, FrontierMath) are the verifier cases; "ran ≠ was right" matches the judge limits.
- ai-in-the-loop.md step 5 ("evaluation cost → ~0, quality unknown"): Ch 14 gives a quantified caution for LLM critics.

6. **Links to existing entries**
- Strevens: Hardt adopts the iron rule as his framework; his treatment of it as a maintainable social contract is a usable extension.
- OSC: Ch 6 cites the 36% and 47% figures; Ch 7 is an ML analogue measuring replication directly.
- Ioannidis: Ch 6 reproduces the PPV calculation (0.64, 0.48) and says the inputs are guesses, which matches the repo's "assumed inputs".
- Popper: severe test is echoed by the held-out test, with the added point that reuse erodes severity.
- Kuhn/Longino/Merton: Ch 8's norms-over-statistics explanation echoes community standards; no direct citation seen.

7. **One-line take**: Closest working model of a community verification loop; shows rankings survive Goodhart where scalars fail, but only with shared data and cheap re-runs.

8. **Confidence**
- Summary: chapter content, figures, and quotes above. Ch 6/7 numbers and the Strevens usage I spot-checked in the chapter texts.
- Background: Arrow, Condorcet, and Goodhart framing.
- Inference: the link to the lee3j case, the trust score design hint, and "benchmarks as standing allocation". The mapping of tune-before-test to "equalizing preparation" is my guess. Whether Hardt discusses retraction or dependency anywhere is unchecked beyond a keyword count.
