# 01 - Foundations of randomization (permutation) inference

Reader notes for: young2019, athey2017, ernst2004, hess2017.
All four text files were read in full (reference lists skimmed). The text extraction was clean for all four, so no PDF pages had to be read directly.

Page convention: `(p. N)` is the page marker `=== page N ===` in `literature/txt/<key>.txt`, i.e. the PDF page.
Offsets to the printed page numbers: ernst2004 PDF p. 1-10 = journal p. 676-685; hess2017 PDF p. 1-22 = Stata Journal p. 630-651; young2019 PDF p. N = manuscript p. N-1 (LSE accepted version, cover sheet is p. 1); athey2017 PDF p. N = manuscript p. [N-1] (arXiv v1, July 2016).

Lines marked **[our inference]** are my application of a paper's logic to our design; the paper does not say them.

---

### ernst2004 - Ernst (2004), Permutation methods: a basis for exact inference

- **Question and setting.** A teaching/review article in Statistical Science: why permutation methods give exact tests and intervals, under which probability model, and how to compute them. No new empirical question.

- **Data and method.**
  - Three small worked examples: 7 surgical recovery times split 4 new / 3 standard (all C(7,4) = 35 assignments enumerated, Table 1, p. 3); wing and antenna lengths for 9 + 6 midges (C(15,6) = 5005 divisions, p. 6); reading speed of 14 subjects in 3 typeface groups (252,252 arrangements, Monte Carlo with M = 9999, p. 9).
  - Two probability models are kept apart (p. 1): the *randomization model* (available units are randomly assigned; inference is limited to the units in the study, p. 2) and the *population model* (random samples from populations; H0: F = G; the test is conditional on the observed values, p. 5-6). The mechanics are identical; the justification differs.
  - The general recipe for other designs is to find "rearrangements of the data that are equally likely under the null hypothesis" (p. 8); unequal but known probabilities also work.

- **Main findings (methodological statements, with numbers from the examples).**
  - Exactness: an exact test has P(Type I error) = alpha; the t-test is exact only under normality (p. 2).
  - Randomization p-value, one-sided (p. 4): p = (number of assignments with t_i <= t*) / C(N,n), the observed assignment included. Example: t* = -9 days, p = 3/35 = 0.0857 (p. 4).
  - Discreteness: p is a multiple of 1/C(N,n), and not every multiple is achievable. If alpha is an achievable value the test is exact; otherwise P(Type I error) is the largest achievable value below alpha and the test is conservative (p. 4).
  - Test statistics: any statistic can be used (difference in means, medians, trimmed means). The sum of responses in one group and the pooled two-sample t are monotone functions of the difference in means, so they give the same test; the Wilcoxon rank-sum test is the same procedure applied to ranks (p. 4-5). In the example the median difference gives the same p = 3/35 (p. 4).
  - Confidence interval by test inversion (p. 5). Assume a constant additive effect Delta. Subtract Delta from the treated responses and rerun the test; the interval is the set of Delta not rejected. With p1(Delta) = P(T_Delta <= t*_Delta) and p2(Delta) = P(T_Delta >= t*_Delta): Delta_L = min{Delta: p2(Delta) > alpha}, Delta_U = max{Delta: p1(Delta) > alpha}. (-inf, Delta_U) and (Delta_L, inf) are one-sided (1-alpha) intervals; (Delta_L, Delta_U) is two-sided (1-2alpha). Exact if alpha is achievable, conservative otherwise. The randomization distribution has to be recomputed for every trial Delta. Example: one-sided 94.29% (= 1 - 2/35) interval (-inf, 2) days, which contains 0, in agreement with p = 3/35 > alpha (p. 5).
  - Two-sided p when the distribution is not symmetric: do not double one tail; use p = P(|T - tbar| >= |t* - tbar|), tbar = mean of the permutation distribution (p. 6-7). Example p-values 0.0719 (wing) and 0.0022 (antenna) (p. 7).
  - Monte Carlo version (p. 7): with M random rearrangements, p_hat = (1 + sum I(t_i >= t*)) / (M + 1); never below 1/(M+1); the test stays exact with a small loss of efficiency that falls with M (Dwass 1957, Jöckel 1986). p_hat is a binomial proportion, so a confidence interval for the exact p can be reported (p. 8); example p_hat = 0.0115 with 99.9% CI (0.0083, 0.0154) (p. 9).
  - Multiple comparisons (p. 9-10): choose the critical value C_alpha as the (1 - alpha) quantile of the randomization distribution of the *maximum* pairwise difference, so that P(max |Ybar_i - Ybar_j| >= C_alpha | H0) = alpha. This is an exact procedure for the family; the procedure adapts directly to a subset of comparisons or to one-sided comparisons (p. 10). Example: C_0.05 = 142.5, only one of three contrasts significant (p. 10).

- **Usable for our paper.**
  - Method: definition of the exact randomization p-value with the observed assignment counted, and the statement that validity needs only the equal likelihood of assignments under H0 (p. 4, p. 8).
  - Method: our p-values are multiples of 1/1024; the smallest possible is 1/1024 = 0.00098, and an exact one-sided 5% test uses the cutoff 51/1024 = 0.0498 **[our inference from p. 4]**. The pilot p = 0.008 and 0.034 are consistent with 8/1024 and 35/1024 **[our inference]**.
  - Method / Results: confidence interval for the effect by inverting the test under a constant additive shift (p. 5). For us the shift is in log points on the contrast c; the endpoints convert to minutes through 60(1 - exp(D)) because the map is monotone **[our inference]**.
  - Method: one-sided test and one-sided interval are a matched pair (p. 5).
  - Robustness: alternative statistics (median across cells, ranks) change power, not validity (p. 4-5).
  - Robustness (multiple testing over 5 speed classes): max-statistic critical value from the same 1024 assignments gives exact familywise control, one-sided version allowed (p. 9-10).
  - Method (if controls are widened and enumeration becomes infeasible): the (1 + count)/(M + 1) formula and a binomial CI for the Monte Carlo error (p. 7-8).

- **Caveats.**
  - The randomization-model guarantee rests on a *physical* random assignment (p. 2). The date of 10 November is not randomly assigned. Our test therefore belongs to the family of equally-likely-rearrangement tests (p. 8), which is an exchangeability *assumption* about dates within a year, not a design fact. Ernst does not discuss time series, trends or serial correlation.
  - Inference under the randomization model extends only to the units actually studied (p. 2): our statements are about these 5 years of dates, not future years.
  - The interval by inversion needs a constant additive effect (p. 5). It is not an interval for an average of heterogeneous effects.
  - The paper gives no result on stratified (within-block) permutation beyond a pointer to Pitman (1938) for randomized blocks (p. 8). Do not cite Ernst for the blocked design itself.
  - No power analysis.

- **Checks or analyses it suggests for us.**
  1. Report the exact p as a fraction k/1024 next to the decimal, and state the minimum attainable p.
  2. Invert the test on a grid of Delta (log points) to get a one-sided 95% lower bound on the slowdown and a two-sided 90% interval; convert the endpoints to minutes.
  3. For any two-sided number, use the |T - tbar| form, not twice the one-sided p.
  4. Familywise test for the 5 speed classes: for each of the 1024 assignments compute the most extreme (most negative) of the 5 standardised class statistics; compare the observed minimum with that distribution.
  5. Re-run with a median-over-cells and a rank statistic.

---

### hess2017 - Heß (2017), Randomization inference with Stata: a guide and software (ritest)

- **Question and setting.** Explains how to run randomization inference when treatment assignment is stratified, clustered, pairwise or otherwise non-standard, and introduces the Stata command `ritest`, which extends `permute`.

- **Data and method.**
  - Replication of Fujiwara and Wantchekon (2013): village-level aggregates for 24 villages in 12 district pairs, one village treated per pair; 2^12 = 4096 equally likely assignments (p. 12, 14).
  - Simulation 1: 42 classes with sizes 20 or 100 linked to an unobserved class effect; half treated or only 10 treated; outcomes with and without an effect; compares RI (coefficient and t), cluster-robust, and wild bootstrap (p. 16-18).
  - Simulation 2: n = 24, two outcomes driven by the same unobservable with opposite signs, to show joint inference (p. 18-19).
  - Statistic: usually the coefficient or the t statistic from Y = tau*D + X'beta + eps (p. 4).

- **Main findings.**
  - RI takes the sample as fixed and only the assignment as random; validity does not depend on sample size, the regression model, or the error distribution (p. 2-4).
  - The null is sharp: y_i(1) = y_i(0) for all i, which is stronger than, and implies, a zero average effect. Other sharp nulls y_i(1) = y_i(0) + alpha_i with specified alpha_i can also be tested (p. 5 and footnote 2).
  - The resampling must replicate the original assignment procedure. If assignment was by village, individual-level permutation is wrong (p. 6). "Otherwise, permutation test results are rendered meaningless." (p. 6)
  - Non-experimental regressors: RI is still possible when the distribution of the variable of interest is known or can be defended, but the permutation must respect the dependence structure. Example: permuting years of rainfall (not countries) keeps spatial correlation and destroys autocorrelation, so the reference distribution is the one that holds when there is no effect *and* no autocorrelation across years (p. 6).
  - Stratification: conventional tests that ignore strata are overly conservative; strata fixed effects are the usual parametric fix, but with pairs this means 24 observations for 12 intercepts plus one effect, so asymptotics are not credible (p. 5-6, p. 12).
  - p-values (p. 7): one-sided p_left = (1/M) sum 1(tau_m <= tau_hat); two-sided uses |tau_m| >= |tau_hat|. Ties are counted against the observed result, so p-values are marginally conservative (footnote 4). The rank-based p can mislead if the null distribution is multimodal (footnote 3).
  - Enumeration beats sampling when feasible: with 4096 assignments the exact p-values (col. 6) differ little from 1000-draw approximations (col. 4-5), e.g. clientelism index 0.024 / 0.012 / 0.020 (Table 1, p. 13); the author recommends the non-approximate version (p. 14).
  - Simulation 1: RI is well calibrated with either statistic; cluster-robust inference over-rejects strongly, more so with few treated clusters; the wild bootstrap also over-rejects with few treated clusters; RI has more power than the wild bootstrap in that DGP (p. 17-18; results are shown as histograms, no table of rejection rates).
  - With assignment at the cluster level and unequal cluster sizes, treatment is correlated ex post with cluster size and hence with unobservables (p. 16-17).
  - Multiple outcomes: permuting once and saving all statistics gives their joint null distribution, which supports Romano-Wolf or Young-type corrections and joint tests; Bonferroni ignores this dependence and is conservative (p. 7-8). In the Benin data two outcomes with marginal p = 0.045 and 0.154 are jointly far in the tail (p. 14-15).
  - Statistic choice: coefficient vs t can differ; each has most power against a different alternative; simulate to choose (p. 4).

- **Usable for our paper.**
  - Method: the closest published template for our design: few assignment units, stratified, one treated unit per stratum, all assignments enumerated (24 villages, 12 pairs, 4096 assignments; p. 12-14). Ours is 5 strata (years), one treated date of 4, 4^5 = 1024.
  - Method: assignment unit = permutation unit (p. 6). Our treatment varies by date, not by cell, so dates are permuted and cells are never permuted. This is the citation for "effective sample = dates".
  - Method / Threats: the rainfall example (p. 6) states precisely what our test assumes. Permuting which date is treated keeps all cells of a date together, so cross-cell (spatial) correlation is preserved; what is assumed away is systematic dependence across dates within a year (trend, autocorrelation) **[our inference from p. 6]**.
  - Method: sharp null and its relation to the average-effect null (p. 5).
  - Method: one-sided p-value definition and conservative tie handling (p. 7).
  - Robustness: joint null distribution of the 5 speed-class statistics from the same 1024 assignments, for a joint or stepdown test (p. 7-8, 14-15, 18-19).
  - Introduction / Literature: RI is used outside RCTs, e.g. regression discontinuity (Cattaneo, Frandsen and Titiunik 2015) and regression kink (Ganong and Jäger 2015) (p. 2).

- **Caveats.**
  - A software guide; the theory is a summary of Fisher, Rosenbaum, Imbens-Rubin and Young (2016 working paper). For theory cite those, not Heß.
  - The simulation evidence is one DGP each, shown graphically; no numerical rejection rates to quote.
  - The summary of Young on p. 3 (more than 10% of significant tests lose significance; over 30% of multi-treatment equations fail joint tests; fewer than half of the papers can maintain any effect) refers to the 2016 working paper. The last statement is **not** in the 2019 accepted version I read; do not attribute it to Young (2019).
  - Heß does not treat time-series placebo dates, and says explicitly that for non-experimental regressors the assumptions about the assignment distribution have to be defended (p. 3).
  - `ritest`'s p = rank/M differs from the (1 + count)/(M + 1) form in Ernst and Young; under full enumeration, with the observed assignment in the set, the two coincide **[our inference]**.

- **Checks or analyses it suggests for us.**
  1. Enumerate all 1024 assignments (already done) and store, for each, the vector of 5 speed-class statistics; reuse it for all multiple-testing procedures.
  2. Plot the null distribution with the observed value marked, per speed class, and one bivariate scatter for the two significant classes (as Figures 1, 2, 4).
  3. State in the Method section the exact exchangeability assumption, in the form of the rainfall example.
  4. Compare the coefficient statistic with a studentised statistic.
  5. Because ties count against us, check how many assignments tie with the observed one.

---

### young2019 - Young (2019), Channeling Fisher: randomization tests and the statistical insignificance of seemingly significant experimental results

- **Question and setting.** Do the significance results reported in published randomized experiments survive when the authors' conventional (mostly clustered/robust) inference is replaced by randomization tests, for single coefficients and for joint tests of all treatment effects in a regression or a table?

- **Data and method.**
  - 53 experimental papers (39 field, 14 lab) from AER, AEJ: Applied and AEJ: Micro up to March 2014, found by keyword search, with public data and Stata code (p. 7, 9, Table I p. 38). Natural experiments are excluded by construction (p. 7).
  - 1780 regressions (p. 10), 4044 reported treatment coefficients (Table V notes, p. 41), 922 regressions with more than one treatment coefficient (p. 42), 198 tables (p. 43). All summaries are averages across papers of within-paper rates (p. 10).
  - Null tested throughout: all randomized treatment effects are zero for every participant (p. 9, 17).
  - Re-randomization follows each paper's actual scheme, including strata; authors were contacted for strata and treatment construction (p. 9).
  - Exact p-value over the set Omega of M equally likely assignments (eq. 4, p. 15): p = (1/M) sum I(f(T_S) > f(T_E)) + U * (1/M) sum I(f(T_S) = f(T_E)), U uniform. With N random draws (eq. 5, p. 16): p = [sum I(>) + U * (1 + sum I(=))] / (N + 1); exact for any N; power rises with N; 10,000 draws used, no appreciable change beyond 2000 (p. 16). Unequal assignment probabilities are handled by duplicating assignments in proportion to their probability (footnote 10, p. 16).
  - Sharp null with a non-zero value beta_0: the counterfactual outcome under assignment T_S is y_S = y_E - T_E*beta_0 + T_S*beta_0 (p. 15).
  - Two statistics (p. 17-18): *randomization-t* compares Wald/squared-t statistics with the covariance re-estimated for every draw; *randomization-c* compares coefficients scaled by one fixed covariance (the covariance of the coefficient across Omega), which for a single coefficient is a comparison of squared coefficients.
  - Benchmarks: bootstrap-t, bootstrap-c, jackknife (= HC3) (p. 21).
  - Monte Carlo: n = 20, 200, 2000; binary treatment 50/50 or 10/90; fixed or heterogeneous (normal, chi-squared) effects; 10 independent equations for joint and Bonferroni tests (p. 21-23, Tables III-IV p. 39-40).

- **Main findings.**
  - Individual coefficients: with authors' methods 0.216 and 0.354 of coefficients are significant at .01 and .05; randomization-t finds 0.78 and 0.87 times as many, i.e. 22% and 13% fewer (abstract p. 2; Table V p. 41). The running text on p. 28 prints ".88" for the .05 ratio, the table and abstract give .87.
  - The gap is a leverage phenomenon: high-leverage third of papers 0.65 and 0.74; low-leverage third 0.96 and 0.98 (Table V, p. 41; p. 28). First tables and regressions without interactions are close to conventional results at .05 (0.97) (p. 28, 41).
  - Joint tests, regression level: authors' F/Wald rejects in 0.438 / 0.546 of regressions; randomization-t ratio 0.76 / 0.83; high leverage 0.42 / 0.58 (Table VI p. 42; p. 30).
  - Joint tests, table level (mean 19 effects per table, range 2-96): conventional 0.493 / 0.622; randomization-t ratio 0.51 / 0.67 (49% and 33% fewer); bootstrap-t 0.21 / 0.33; jackknife 0.77 / 0.84 (Table VII p. 43; p. 31).
  - Bonferroni at table level: randomization-t 0.61 / 0.81 of conventional; Westfall-Young with the randomization distribution 0.77 / 0.91, because results inside a table are highly correlated (p. 31-32; Table VII p. 43).
  - Joint tests reject at least as often as multiple-testing procedures: evidence against irrelevance sits in several moderate effects, not only in one extreme coefficient (p. 19, 29, 32; Figure II p. 46).
  - Reporting pattern: 0.60 of regressions have more than one treatment effect; given a .01-significant result, a regression reports on average 4.0 effects of which 1.6 are significant, a table 21.2 of which 5.0; only two papers report any joint F test, none at table level (p. 4).
  - Fragility: deleting one observation/cluster makes 0.35 of .01-significant results insignificant and 0.16 of insignificant ones significant; mean max-min delete-one p-value gap 0.23 (p. 11).
  - Leverage facts: mean share of the single most influential cluster/observation 0.058, 0.134 in the high-leverage third (Table II p. 38; p. 13). A regressor applied 25/75 puts 3/4 of leverage on 1/4 of observations (p. 14).
  - Simulated size at nominal .05 (Table III, p. 39): balanced design, all methods near .05. Unbalanced 10/90, n = 20, fixed effects: robust 0.241, randomization-t 0.046, randomization-c 0.048, jackknife 0.140. With heterogeneous effects in the unbalanced design: randomization-c 0.129-0.137 (normal) and 0.144-0.195 (chi-squared) at every n, randomization-t 0.089 at n = 20 then 0.051-0.065.
  - Simulated size, 10 equations (Table IV, p. 40): joint robust Wald 0.594 (balanced, n = 20) and 0.998 (unbalanced, n = 20); randomization-t 0.053 and 0.051; bootstrap-t 0.000. Bonferroni with robust p-values: 0.682 (unbalanced, n = 20).
  - Why dimension hurts: for multiple tests, tail errors grow proportionally at the smaller alpha/N cutoff; for joint tests, the Wald statistic is the maximum squared t over all linear combinations (eq. 8, p. 23-24).
  - Randomization-c in joint tests is not exactly exact because the covariance across Omega is approximated by sampled draws (0.060 and 0.058 at n = 20; p. 18, footnote 17 p. 23).
  - Power: where conventional size is correct, power of randomization-t and robust tests is essentially the same; where conventional tests over-reject, RI has lower raw power but a better power-to-size ratio (p. 26).
  - Agreement: randomization and conventional p-values nearly coincide when leverage is evenly spread (p. 6, 25-26, 34).
  - Level of randomization: in 12 papers that cluster below the treatment level, redoing both tests at the treatment level raises the share of .01-significant coefficients with randomization p > .10 from .000 to .186 (p. 10-11, 33-34).
  - Multi-treatment regressions: the p-value for one coefficient generally depends on the null assumed for the others (p. 16-17). Stepdown procedures need subset pivotality, which holds trivially when each test uses a single treatment measure, and can be secured by splitting into mutually exclusive samples (p. 20, 34-35).
  - Size of p-value changes (Table VIII, p. 44): for conventionally .01-significant single coefficients, randomization p stays below .01 in 0.752 of cases and exceeds .20 in 0.005; for table-level joint tests the figures are 0.477 and 0.217.

- **Usable for our paper.**
  - Method: definition and exactness of the randomization p-value, by enumeration (eq. 4) and by sampling (eq. 5) (p. 15-16). Under the sharp null RI is exact regardless of sample size, regression design, or error distribution (p. 14).
  - Method: the sharp null as a statement that treatment is irrelevant, "exact tests, but only of sharp nulls" (p. 5).
  - Method: nulls with a non-zero constant effect via y_S = y_E - T_E*beta_0 + T_S*beta_0 (p. 15); this is the device behind our confidence interval.
  - Method: permute at the level at which treatment varies; evidence on what happens otherwise (p. 10-11, 33-34). Supports "dates, not cells".
  - Method / Robustness: prefer a studentised statistic when effects may be heterogeneous and the design is unbalanced (p. 18, 22-23, Table III p. 39). Our design is unbalanced by construction (1 treated date of 4, and far more so once the control pool is widened) **[our inference]**.
  - Robustness (5 speed classes): (i) Bonferroni is valid but conservative under correlation (p. 19); (ii) Westfall-Young: use the alpha-quantile of the randomization distribution of the minimum p-value (p. 19-20); (iii) a joint randomization test of "no effect in any class" has different power, favouring several moderate effects (p. 18-19, 29). Stepdown is legitimate for us because each class is a mutually exclusive sample with one treatment measure (p. 20, 34-35) **[our inference on applicability]**.
  - Robustness: delete-one sensitivity as a diagnostic (p. 11). For us: leave-one-year-out and leave-one-control-date-out.
  - Results-Discussion: sub-sample splits are where conventional inference degrades (p. 4, 28); our speed-class split is such an exploration and should carry a family-level test.
  - Introduction / Literature: headline numbers (13-22% fewer individually significant results; 33-49% fewer in table-level joint tests) as motivation for exact inference with few effective observations (p. 2-3).

- **Caveats.**
  - The sample is randomized experiments only; natural experiments were dropped (p. 7). The paper gives no support for treating a fixed calendar date as randomly assigned. It supports the *machinery*, not our identifying assumption.
  - RI is not always more conservative. With balanced, low-leverage designs the two approaches agree (p. 6, 26, 34). Any earlier note saying that Young shows conventional inference over-rejects in general overstates.
  - Robustness to heterogeneous effects is shown by simulation for the randomization-t only, and only approximately (0.089 at n = 20, up to 0.105 for interaction terms; Table III p. 39). Asymptotic validity for average effects requires balance or studentisation (p. 5, citing Janssen 1997, Chung and Romano 2013). Our current statistic is a difference in means, i.e. a randomization-c type statistic **[our inference]**.
  - The reductions in significance are averages over papers and are attributed to leverage, not to wrongdoing; results are anonymised (p. 7).
  - Individual p-values in multi-treatment regressions are computed under the joint null of all effects zero (p. 17).
  - Figures are ratios to the authors' own methods, and Young deliberately picks the variants most favourable to authors (p. 33-34), so the published gaps are lower bounds on his alternatives.
  - The extracted text of p. 33 garbles two fractions; from Table VIII (p. 44) the share of table-level significance changes that land above p = .20 is roughly 0.27 to 0.61 **[my arithmetic from the table]**. Do not quote the garbled passage.
  - The claim that fewer than half of the papers retain any effect (as summarised in hess2017, p. 3) does not appear in this version.

- **Checks or analyses it suggests for us.**
  1. Westfall-Young min-p adjustment over the 5 speed classes using the 1024 assignments; report next to Bonferroni. Bonferroni alone gives 5 x 0.008 = 0.040 and 5 x 0.034 = 0.17, so only the 50-70 km/h class survives at 5% **[my arithmetic]**.
  2. A joint randomization test of no effect in any class (e.g. sum of squared standardised class effects, or a one-sided sum), with the covariance taken over the full enumeration so that the statistic is a fixed function of the assignment **[our inference: enumeration removes the approximation problem of footnote 17]**.
  3. A studentised version of the statistic (yearly DiD divided by a within-year dispersion of the control-date contrasts) and a comparison with the unstudentised result.
  4. Leave-one-year-out and leave-one-control-date-out p-values, in the spirit of Figure I.
  5. Keep each speed class as a separate, mutually exclusive sample so stepdown remains valid.
  6. If the control pool is widened and enumeration is replaced by sampling: at least 2000 draws, preferably 10,000, with eq. 5.

---

### athey2017 - Athey and Imbens (2017), The econometrics of randomized experiments

(Text is the arXiv version of July 2016; published 2017 in the Handbook of Economic Field Experiments. Page numbers below are those of the arXiv PDF.)

- **Question and setting.** A handbook chapter on how to analyse and design randomized experiments, built on randomization-based (design-based) rather than sampling-based inference: Fisher exact tests, Neyman's repeated-sampling analysis, regression, stratified, paired and clustered designs, non-compliance, heterogeneous effects, interference.

- **Data and method.**
  - Illustrations: Lalonde/NSW job-training data (445 individuals, 185 treated; p. 15); Duflo-Hanna-Ryan teacher data (54 control, 53 treated; p. 27-28); Children's Television Workshop, 8 classroom pairs (p. 34).
  - Framework: potential outcomes fixed, assignment random; SUTVA; the assignment mechanism p(W | Y(0), Y(1), X) is known and free of potential outcomes in an experiment (p. 10-12). Completely randomized, stratified, paired and clustered mechanisms are written out (p. 12-14).

- **Main findings.**
  - Definition: an experiment requires that assignment does not depend on unit characteristics and that the researcher controls it; otherwise the study is observational (p. 5, 10).
  - Design-based uncertainty exists even when the whole population is observed, because only one potential outcome per unit is seen (p. 8-9).
  - Fisher exact p-value (p. 15-16): sharp null H0: Y_i(0) = Y_i(1) for all i lets all missing potential outcomes be imputed; for any statistic T(W, Y_obs, X) the exact null distribution follows from the known assignment distribution; p = Pr(|T(W, Y_obs, X)| >= |T(W_obs, Y_obs, X)|). Lalonde: difference in means 1.79 (thousand USD), exact p = 0.0044; rank statistic p = 0.01 (p. 16); Neyman/normal-approximation p = 0.0076 with se 0.671 (p. 20).
  - Statistic choice is the main decision. Ranks raise power with outliers and thick tails and are described as less arbitrary than a log transform (p. 16-17).
  - Multiple outcomes: either one combined statistic (an F-type quadratic form) with an exact Fisher p-value, or p-value adjustments; Bonferroni is the traditional bound and tighter ones exist (p. 17).
  - Confidence intervals from exact tests: by inverting rank tests under a common effect (Rosenbaum; Hodges-Lehmann) (p. 17).
  - Neyman (p. 18-19): tau_hat = Ybar_t - Ybar_c is unbiased for the sample average effect; V(tau_hat) = S_c^2/N_c + S_t^2/N_t - S_tc^2/N; the estimator V_neyman = s_c^2/N_c + s_t^2/N_t drops the last term and is conservative unless effects are constant or the target is a super-population average. Confidence intervals need a large-sample approximation (p. 19).
  - Regression: OLS on a treatment dummy equals the difference in means; randomization implies heteroskedasticity, so robust standard errors are needed, and the EHW estimator is biased when one arm is small (N_t = 4, N_c = 54: 0.1215 vs Neyman 0.1400; p. 27-28). The authors advise caution with regression adjustment in general (p. 24-25).
  - Stratified experiments (p. 31-32): tau_hat = sum_g (N_g/N) tau_hat_g, V_strat = sum_g (N_g/N)^2 (s_tg^2/N_tg + s_cg^2/N_cg). With equal treatment shares it equals the pooled difference in means, and the unstratified variance is conservative.
  - Paired experiments (p. 33-34): within-stratum variances cannot be estimated with one treated and one control unit; use V = [1/((N/2)(N/2 - 1))] sum_g (tau_hat_g - tau_hat)^2 (eq. 6.1), conservative for the sample average effect. Example: tau_hat = 13.4, se_pair = 4.6 vs se_neyman = 7.8 (p. 34).
  - Design advice: stratify as far as possible but keep at least two treated and two control units per stratum, because variances cannot be estimated otherwise (p. 4, 34). In expected squared error, stratification with equal treatment shares is never worse than complete randomization: V_C - V_S = (1/(4N))[(mu_fc - mu_mc)^2 + (mu_ft - mu_mt)^2] >= 0 (p. 40). Unstratified experiments still give exact p-values; stratification adds precision, not validity (p. 37).
  - Re-randomization: an exact p-value requires the exact distribution of the assignment vector, so any restriction on admissible assignments must be fully specified; ignoring it gives conservative p-values (p. 42).
  - Clustered assignment (p. 42-47): "We recommend in general to focus on cluster-level analyses as the primary analyses." (p. 4-5) Aggregating to cluster means lets all completely-randomized methods apply directly (p. 44). Two estimands: tau_pop (unit-weighted) and tau_C = (1/G) sum_g tau_g (cluster-weighted); tau_C is often far more precise when cluster sizes differ; for testing whether there is any effect, an unweighted cluster statistic is as valid as a weighted one (p. 44-45). Cluster-level estimator and variance: tau_hat_C = mean of treated cluster means minus mean of control cluster means, V = s_Cc^2/G_c + s_Ct^2/G_t (p. 45). Unit-level analysis needs Liang-Zeger clustered errors (p. 46). Unit-level covariates typically add little precision over cluster averages (p. 43).
  - Interference: with spillovers between units, even a well-run experiment may lack internal validity at the unit level (p. 6-7); cluster-level assignment is one answer (p. 14, 43). Exact p-values can be built for nulls about spillovers by redefining the experiment on a subset of focal units (p. 15, 71-72).
  - Subgroups: subgroup effects chosen ex post raise multiple-testing concerns; remedies are pre-analysis plans or corrections; Bonferroni is too conservative when test statistics are correlated (p. 58-59).

- **Usable for our paper.**
  - Method: formal statement of the sharp null and of the Fisher exact p-value (eq. 4.1-4.3, p. 15-16).
  - Method: design-based uncertainty when the full population is observed (p. 8-9). We observe every monitored cell in Istanbul; the uncertainty is about what the other dates would have looked like under treatment, not about sampling cells.
  - Method: unit of analysis. Treatment (the siren) is assigned to a date, and every cell on that date is treated. This is a clustered assignment with date as the cluster, and the recommended primary analysis is on cluster aggregates (p. 4-5, 43-45) **[our inference on the mapping]**. Averaging the contrast over cells within a date, then testing over dates, is exactly this.
  - Method: stratified structure. Years are strata; the stratified estimator is the weighted average of within-year contrasts (p. 31-32). With one treated date and equal numbers of dates per year, equal weights over years coincide with N_g/N weights **[our inference]**.
  - Method / Data: cell weighting. Equal weight over cells vs vehicle-weighted is the tau_C vs tau_pop choice one level down; the chapter says both are legitimate for testing and suggests reporting both (p. 44-45) **[our inference on the mapping]**.
  - Method: why no conventional standard error is available inside a year: with a single treated unit per stratum the within-stratum variance is not estimable (p. 4, 33). A year-level analogue of eq. 6.1, V = [1/(G(G-1))] sum_g (D_g - Dbar)^2 with G = 5 yearly DiD values, gives a conservative conventional check with 4 degrees of freedom **[our inference: the paper states eq. 6.1 for pairs only]**.
  - Robustness: rank-based statistic (p. 16-17); combined statistic or adjusted p-values for multiple outcomes/subgroups (p. 17, 58-59).
  - Results-Discussion: confidence intervals by test inversion under a common effect (p. 17); Neyman-type intervals need large samples (p. 19), which we do not have with 5 years.
  - Threats: interference between cells (queues spilling into neighbouring cells) does not break a date-level test, because all cells are treated together; the estimand is then the total effect on a cell when the whole city is treated **[our inference from p. 14, 43]**.
  - Literature: Freedman's dictum quoted by the authors, that experiments should be analysed as experiments (p. 3).

- **Caveats.**
  - Everything is derived for assignment mechanisms that are known and controlled by the researcher (p. 5, 10-12). By the chapter's own definition our study is observational: the date is fixed by the calendar. The chapter does not discuss placebo-date or in-time permutation tests, event studies, or difference-in-differences. It cannot be cited as justification for treating Nov 10 as one of four exchangeable dates.
  - The only pointer to time series is a one-line reference to Angrist and Kuersteiner (2011) (p. 6).
  - The Fisher test is for sharp nulls; the chapter's preferred tool for average effects is Neyman's, which needs many units (p. 19). With 5 years we cannot lean on it.
  - The chapter advises against pairs / single-treated strata because variance estimation fails (p. 4, 34). Our design is of that discouraged kind; the exact test remains valid, but conventional standard errors are not available.
  - The chapter says little about one-sided tests; its p-value is written two-sided (eq. 4.3, p. 16).
  - Small inconsistencies in the text: control group size 260 on p. 15 but 240 on p. 16; on p. 41 the inequality V(V_S) < V(V_C) contradicts the sentence before it (the stratified variance estimator is the noisier one). Do not quote these lines.
  - Sections 9-10 (non-compliance, machine-learning heterogeneity) are not relevant to us.

- **Checks or analyses it suggests for us.**
  1. Collapse to one number per date (mean over cells of c), then one DiD per year; run every test on these 5 x 4 date-level values. Report the cell-level regression only as a secondary result with date-clustered errors.
  2. Report both equal-cell-weighted and vehicle-weighted versions.
  3. Stratified rank statistic: rank of Nov 10 among the dates of its year, summed over years. With 4 dates per year, lowest rank in all 5 years gives p = (1/4)^5 = 1/1024; in at least 4 of 5 years gives 16/1024 = 0.016 **[my arithmetic]**.
  4. Conventional cross-check: t-test on the 5 yearly DiD values using the eq. 6.1 analogue (4 d.f.).
  5. When the control pool is widened to all same-weekday dates, each year becomes a stratum with 1 treated and about 50 control dates; keep permuting within year and keep year as the stratum.
  6. State the assignment mechanism we assume, explicitly, as the chapter requires for exact p-values (p. 42).

---

## Cross-paper synthesis (what jointly matters most for our design)

1. All four papers agree on the core object: under a sharp null and a known set of equally likely assignments, the p-value is the share of assignments with a statistic at least as extreme as the observed one, and it is exact for any sample size (ernst p. 4; hess p. 2-4; young p. 14-16; athey p. 15-16).
2. None of the four justifies our assignment model. They all assume physical randomization (young excludes natural experiments, p. 7; athey calls anything else observational, p. 5). Our test is exact only under an assumed exchangeability of the candidate dates within a year; say so plainly, in the form of hess p. 6 and ernst p. 8.
3. The known threat "Nov 10 is always the 2nd of 4 dates" is a failure of exactly that assumption, and no reshuffling repairs it. Use trend-symmetric controls (Nov 3 and 17 only), a within-year detrended contrast, and the widened control pool as separate checks **[our inference]**.
4. Permute at the level at which treatment varies, and analyse aggregates at that level: dates, not cells (athey p. 4-5, 43-45; hess p. 6; young p. 33-34). Cell-level standard errors are not evidence.
5. Our design is stratified with one treated unit per stratum, like the 12-pair Benin example with 4096 assignments (hess p. 12-14). Enumeration is right; within-stratum variances are not estimable (athey p. 33), so the randomization test is the primary inference and a 5-year t-test is only a cross-check.
6. Discreteness: p-values are multiples of 1/1024, minimum 0.00098; report fractions (ernst p. 4).
7. Statistic: the difference in means is valid under the sharp null but is the less robust "randomization-c" type when effects differ across years and the design is unbalanced (young p. 18, 22-23, Table III). Add a studentised and a rank statistic (athey p. 16-17; ernst p. 5).
8. Confidence interval: invert the test under a constant log-point shift, y_S = y_E - T_E*b + T_S*b (young p. 15; ernst p. 5; athey p. 17), one-sided to match the one-sided test, then map endpoints to minutes. It is an interval for a constant effect, not for an average.
9. Five speed classes: reuse the 1024 assignments for a max-statistic or Westfall-Young min-p adjustment and for one joint test (ernst p. 9-10; young p. 19-20, 29; hess p. 7-8; athey p. 17). Plain Bonferroni keeps only the 50-70 km/h class (0.040) and drops 30-50 km/h (0.17).
10. Correction to carry forward: Young (2019) does not show that conventional inference is always too liberal, only that it is in high-leverage designs and high-dimensional tests (p. 26, 34, Tables V-VII); and the fewer-than-half-of-papers line belongs to the 2016 working paper as reported by Heß, not to the 2019 text.
