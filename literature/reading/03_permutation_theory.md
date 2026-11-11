# 03 - Permutation and randomization-test theory

Reader notes for: chung2013, wu2021, caughey2023, ding2016, canay2017.
Page numbers are PDF pages as marked in `literature/txt/<key>.txt`.
All five text files were readable; no PDF fallback was needed. Appendices with proofs
(wu2021 pp. 34-47, caughey2023 pp. 34-47, chung2013 Section 5) were skimmed, not checked line by line.
The online supplements of canay2017 and chung2013 are NOT in our files (not read).

Notation used below for our design: year y = 2020..2024; date-level contrast
`c_{y,d}` = cell-average of `ln v(09h) - mean(ln v(08h), ln v(10h))` on date d;
year-level estimate `D_y = c_{y,Nov10} - mean_{controls} c_{y,d}`; overall `D = (1/5) sum_y D_y`.
Passages marked **[own]** are my derivations or simulations, not statements of the papers.

---

### canay2017 - Canay, Romano & Shaikh (2017), Randomization tests under approximate symmetry

- **Question and setting.** When the data can be split into a small, fixed number q of clusters,
  each with many observations, how can one test a parameter value without a cluster-robust
  variance estimator? Answer: apply a sign-change randomization test to the q cluster-level
  estimates; it is valid asymptotically if those estimates are jointly approximately symmetric (pp. 1-2).

- **Data and method (exact procedure).**
  1. Split the data into q clusters; estimate the parameter separately in each: `theta_hat_1..theta_hat_q` (p. 9).
  2. Form `S_j = sqrt(n) (theta_hat_j - theta_0)`, `S = (S_1..S_q)`. The `sqrt(n)` can be dropped
     because the statistics below are scale invariant (Remark 4.4, p. 10).
  3. Statistic (scalar case, eq. 17, p. 10): `T(S) = |mean(theta_hat) - theta_0| / (s / sqrt(q))`,
     with `s^2 = (1/(q-1)) sum_j (theta_hat_j - mean)^2`. Vector case: Wald statistic
     `T = q * Sbar' * Sigma_bar^{-1} * Sbar`, `Sigma_bar = (1/q) sum_j S_j S_j'` (eq. 16, pp. 9-10).
     One-sided version: the signed t-statistic, which gives the same test as using `sum_j S_j` (Appendix A, pp. 14-15).
  4. Group: `G = {-1,+1}^q`, acting by `gS = (g_1 S_1, ..., g_q S_q)`; `M = |G| = 2^q` (p. 4, p. 9).
  5. Compute `T(gS)` for all g, order them `T^(1) <= ... <= T^(M)`, set `k = ceil(M(1-alpha))`.
     Reject if `T(S) > T^(k)`; if `T(S) = T^(k)` reject with probability
     `a = (M*alpha - M+)/M0`, where M+ = number of values above `T^(k)`, M0 = number equal to it (eq. 13, p. 8).
     The non-randomized version (reject only if strictly greater) is level alpha but can be conservative (Remark 2.4, p. 4; Remark 3.6, p. 9).
  6. p-value: `p = (1/|G|) sum_g 1{T(gS) >= T(S)}` (eq. 9, p. 4; asymptotically valid by Remark 3.6, p. 9).
  A random subset of G that includes the identity may replace G (Remark 2.2, p. 4).

- **Required assumptions.**
  - Finite-sample exactness (Theorem 2.1, p. 3): the data distribution is invariant under G under H0,
    i.e. the `X_j` are independent and each symmetric about the null value (symmetric location example, p. 4).
    Then the rejection probability is exactly alpha for any statistic T.
  - Asymptotic version (Assumption 3.1 and Theorem 3.1, pp. 7-8): (i) `S_n -> S` in distribution;
    (ii) `gS` has the same distribution as S for all g; (iii) for distinct g, g' the values `T(gS)`, `T(g'S)`
    are either always equal or differ with probability one; T and g continuous. Then rejection probability -> alpha.
  - In the cluster application (eq. 15, p. 9): `sqrt(n)(theta_hat_1 - theta_0, ..., theta_hat_q - theta_0) -> N(0, Sigma)`
    with Sigma block-diagonal. So: dependence inside a cluster is free; variances may differ across clusters;
    dependence across clusters is allowed only if it vanishes in the limit (Remark 4.2, p. 10).
  - Normality is not required: it suffices that the limit is a product of q distributions symmetric about zero (Remark 4.3, p. 10).
  - Asymptotics are in the within-cluster sample size with q fixed; the randomization distribution does not
    converge to anything, unlike in Chung-Romano type results (Remark 3.5, p. 9).

- **Main findings.**
  - The sign-change test has limiting null rejection probability equal to alpha for any q and any alpha, which
    allows p-values; it also covers vector parameters (p. 2, p. 7).
  - Competing t-test of Ibragimov-Mueller: by Bakirov-Szekely it is valid under heterogeneous normal variances
    only for alpha <= 8.3% (any q >= 2) or alpha <= 10% with 2 <= q <= 14, and it can be very conservative (p. 5).
  - Monte Carlo (100,000 draws, q = 8 and 16, alpha = 5%): randomization test has size 5% at every degree of
    variance heterogeneity; t-test falls well below 5% when variances differ (p. 5, Fig. 1 p. 6). With equal
    variances the t-test is slightly more powerful; with strong heterogeneity (a = 0.1) the randomization test
    wins for mu below about 0.7 (p. 5).
  - When q is small, the t-test's rejection probability sometimes exceeds that of the non-randomized
    randomization test (p. 7).
  - Optimality: the one-sided sign-change test with the t-statistic is uniformly most powerful unbiased against
    normal alternatives with equal variances (Appendix A, pp. 14-15), and stays so if the null only requires
    symmetry about zero (Remark A.2, p. 15). It is non-randomized when alpha is a multiple of `1/2^q` (Remark A.1, p. 15).
  - Difference-in-differences application (Section 4.1, pp. 11-12): for each treated unit j,
    `theta_hat_j = Delta_j - mean_{k in controls} Delta_k`, with `Delta_k = mean_post Y_k - mean_pre Y_k` (eq. 19).
    Sufficient conditions: errors independent across units, control average negligible (eq. 20), and a CLT for the
    treated units' pre and post averages (eq. 21), which needs many pre and post periods.
  - Small-T escape (Remark 4.5, p. 12): the test stays valid with few periods if the pre-average and post-average
    of a unit's error are i.i.d., e.g. equal numbers of pre and post periods plus exchangeability over time. The
    authors call these assumptions strong, but note the cluster estimators "need not even be consistent" (p. 12).
  - Two-sample version of the Ibragimov-Mueller test: limiting size about 1% with 3+3 clusters and 3% with 8+8 at nominal 5% (Remark 4.11, p. 14).

- **How it applies with q = 5 (our five years).**
  - Mapping. Our design is eq. (19) with unit = date, period = hour: `Delta` is the within-day contrast c, the
    treated units are the five Nov 10 dates, the controls are the same-weekday dates, and `theta_hat_j` is `D_y`.
    Clusters are years; each year uses its own controls, so clusters are disjoint.
  - Procedure. Compute `D_2020..D_2024`. For a slowdown test set `S_y = -D_y`, statistic `T = sum_y S_y`
    (same test as the signed t). Evaluate T over all `2^5 = 32` sign vectors; `p = #{g: T(gS) >= T(S)} / 32`.
  - **Smallest attainable p-value [own, from eq. 9; the paper does not discuss q = 5]:**
    one-sided `1/32 = 0.03125`, reached if and only if all five `D_y` are negative. Two-sided with |t|:
    `2/32 = 0.0625`, because g and -g give the same |t|.
  - The one-sided p-value grid is 1/32, 2/32, 3/32, ... **[own, checked numerically]**: 0.0625 if the only
    wrong-signed year has the smallest |D_y|; 0.094 if it has the second smallest; 0.3125 if it has the largest.
  - At alpha = 5% one-sided the non-randomized test rejects only when all five years agree in sign; its exact
    size under symmetry is 3.1%. At alpha = 5% two-sided the non-randomized test can never reject **[own]**.
  - Consequence: the sign-change test cannot reproduce the pilot's p = 0.008 (= 8/1024 in the 4^5 placebo-date
    scheme, whose floor is 1/1024). With five speed classes and Bonferroni, 5 x 0.031 = 0.156, so no class can be
    significant at family-wise 5% by this test **[own]**.
  - The vector Wald statistic cannot test the five speed classes jointly: with d = q = 5 it equals q for every
    sign vector, so the test has no power; it needs d < q **[own, algebra and numerical check]**.
  - What must hold for us: (a) `D_y` independent across years (plausible; dates are a year apart);
    (b) each `D_y` symmetric about zero under H0. The within-year sample that drives any CLT is the number of
    dates and hours, not cells, because a date-level shock is common to all cells. With one treated date and one
    treated hour, eq. (21) gives no CLT; we are in the Remark 4.5 world, where symmetry is an assumption about
    the distribution of a single date's contrast shock.
  - **[own simulation]** With q = 5 and alpha = 5% the test is a sign test, so what matters is
    `P(D_y < 0) = 1/2` under H0. If date shocks are skewed and the control mean is precise, this fails:
    with exponential (right-skewed) shocks, the "all five negative" event has probability 3.0% with one control
    date, 6.2% with three, 9.7% with fifty (nominal 3.1%). Left-skewed shocks make the slowdown test conservative.
    With exactly one control date per year the difference of two exchangeable dates is exactly symmetric.

- **Usable for our paper.**
  - Method / Robustness: a second inference procedure whose assumption (independent, symmetric year-level
    estimates) differs from the placebo-date exchangeability assumption; it tolerates different variances across
    years (p. 2, Remark 4.2 p. 10). Relevant because 10 Nov 2024 was a Sunday while 2020-2023 were weekdays, and 2020 was a pandemic year **[own, calendar fact]**.
  - Method: effective sample size is the number of years (clusters), consistent with our statement that cells are not the unit of inference (pp. 1-2).
  - Robustness: cite the Bakirov-Szekely / Ibragimov-Mueller t-test with q - 1 = 4 degrees of freedom as a
    companion (p. 5); it gives a continuous p-value. Two-sided 5% critical value is 2.776; by symmetry a
    one-sided test at 2.5% uses the same value **[own]**.
  - Results-Discussion: report "all five years negative: sign-change p = 0.031" as the most assumption-light statement, if true.

- **Caveats.**
  - The theorems are asymptotic in within-cluster size; nothing in the main text shows performance at q = 5
    (simulations shown use q = 8, 16; supplement not read).
  - Symmetry about the null is assumed, not delivered, in our one-treated-date setting. Averaging over thousands of cells does not help.
  - A trend in c across November weeks biases every `D_y` in the same direction, which breaks symmetry; the test does not fix the "Nov 10 is always 2nd of 4" threat.
  - Coarse p-values: nothing below 0.031.
  - Splitting a year into sub-clusters (districts, speed classes) to raise q is not allowed: they share the date shock, so Sigma is not diagonal (Remark 4.2, p. 10).

- **Checks or analyses it suggests.**
  1. Table of the five `D_y` with signs; report sign-change p (one-sided) and the t(4) statistic next to the 1024-assignment p.
  2. Placebo symmetry check: for every non-event same-weekday date compute its deviation from the year's control mean; report the share negative (should be near 0.5) and skewness.
  3. Paired variant with exact symmetry: Nov 10 against one control date per year (Nov 3 or Nov 17); and a trend-robust variant `c_Nov10 - (c_Nov3 + c_Nov17)/2`, noting that the latter needs symmetric shocks.
  4. If the 2026 city-wide index can be put on the same contrast scale, add it as a sixth cluster (floor 1/64 = 0.016); heterogeneous clusters are permitted **[own suggestion]**.

---

### chung2013 - Chung & Romano (2013), Exact and asymptotically robust permutation tests

- **Question and setting.** Two independent i.i.d. samples (sizes m, n) from P and Q. A permutation test is exact
  for H0: P = Q. Is it valid for the weaker H0: theta(P) = theta(Q) (equal means, medians, ...)? Generally no;
  the paper shows studentizing the statistic restores asymptotic validity while keeping exactness when P = Q (pp. 1-4).

- **Data and method.** Theory plus Monte Carlo. Estimators are assumed asymptotically linear (eqs. 2.2-2.3, p. 6).
  The key device: the permutation distribution behaves as if all N observations were i.i.d. from the mixture
  `Pbar = pP + (1-p)Q`, `p = lim m/N` (p. 5; coupling argument pp. 15-19).

- **Main findings.**
  - Unstudentized statistic `T = sqrt(N)(theta_hat_m - theta_hat_n)`: its permutation distribution converges to
    `N(0, tau^2)` with `tau^2 = sigma^2(Pbar) / (p(1-p))` (Theorem 2.1, eq. 2.5, pp. 6-7), while the true
    sampling variance under equal parameters is `sigma^2(P)/p + sigma^2(Q)/(1-p)` (eq. 2.6, p. 7).
  - For means the two agree only if p = 1/2 or the variances are equal (Example 2.1, p. 7). Otherwise the
    rejection probability can be far above or below nominal, including wrong-direction (type 3) errors (p. 3).
  - Studentized statistic `S = T / V`, `V^2 = (N/m) sigma_hat_m^2 + (N/n) sigma_hat_n^2` (eq. 2.8, p. 8): the
    permutation distribution converges to N(0,1), the same limit as the true sampling distribution (Theorem 2.2,
    eq. 2.9, p. 8). For means this is the Welch-type t (Example 2.1 continued, p. 9).
  - Here "first order accuracy can fail without studentization" (p. 4), unlike in the bootstrap where studentizing buys only higher-order accuracy.
  - No first-order power loss from using permutation critical values (Remark 2.3, p. 9).
  - k samples: a studentized quadratic statistic (eq. 3.3, p. 11) has permutation limit chi-square(k-1) (Theorem 3.1, p. 12).
  - Simulation, one-sided median test at 5%, equal medians but different shapes (Table 1, p. 13): unstudentized
    rejection rates about 0.18-0.23 at m, n >= 101 in three of the four pairs; studentized about 0.05-0.08 there.
    At small sizes even the studentized test over-rejects in those pairs: 0.07-0.08 at m = n = 5 and 0.12-0.16 at (13, 21).
  - Guiding principle: use a statistic that is asymptotically pivotal (p. 10, p. 23).

- **Usable for our paper.**
  - Method: justification for reporting a studentized statistic alongside the raw DiD mean in the permutation test (pp. 3-4, Theorem 2.2 p. 8).
  - Method: explains what our raw-statistic p-value does and does not test: it is exact for "Nov 10 contrasts
    have the same distribution as control-date contrasts", not for "same mean" (pp. 2-3).
  - Robustness: our treated share is far from 1/2 (1 of 4 dates; about 1 of 52 after widening), exactly the
    unbalanced case where unequal variances distort the unstudentized test (Example 2.1, p. 7).
    **[own, applying eqs. 2.5-2.6]** If the Nov 10 contrast has twice the standard deviation of control dates,
    a nominal 5% one-sided unstudentized test has asymptotic size about 11% at p = 1/4 and about 20% at p = 1/52;
    if it has half the standard deviation, about 1% at p = 1/4.
  - Literature: one sentence linking Neuhaus/Janssen/Chung-Romano studentization to Wu-Ding's design-based version (p. 4).

- **Caveats.**
  - The model is two independent i.i.d. samples with m, n -> infinity. Ours has 5 treated dates, blocked by
    year, with serial and spatial dependence. The theorems do not cover this; treat them as motivation only.
  - With one treated date per year a within-year treated variance cannot be estimated, so the eq. (2.8)
    studentization is infeasible year by year; one must pool across years or studentize across years as in canay2017.
  - Table 1 concerns medians with a bootstrap variance; the paper reports no small-sample numbers for means.
  - The paper does not address one treated unit, clustered assignment, or multiple testing (the last is named as future work, p. 24).

- **Checks it suggests.**
  1. Compare the variance of `c` on the five Nov 10 dates (after removing year means) with control dates; a ratio far from 1 signals that the raw-statistic p-value is not a test of means.
  2. Re-run the 1024-assignment test with a studentized statistic (see wu2021 and synthesis) and report both.
  3. When widening the control pool to all same-weekday dates, do not read the tiny attainable p-values as accuracy; imbalance grows and the Example 2.1 problem gets worse.

---

### wu2021 - Wu & Ding (2021), Randomization tests for weak null hypotheses

- **Question and setting.** Design-based (fixed potential outcomes, random assignment) experiments with J arms.
  Can the Fisher randomization test (FRT), exact under a sharp null, also test the weak null that average
  effects are zero when unit effects are heterogeneous? (pp. 1-3)

- **Data and method.**
  - Weak null `H0N: C Ybar = x` for a contrast matrix C (eq. 1, p. 5). Sharp null: every unit's effects equal the hypothesised values (eq. 2, p. 5).
  - Procedure FRT-1 to FRT-4 (p. 6): compute T; impute missing potential outcomes under a sharp null compatible
    with the weak null; recompute T over permutations of assignment; p = share of `T_pi >= T`.
  - Recommended statistic: `X^2 = N (C Ybar_hat - x)' (C D_hat C')^{-1} (C Ybar_hat - x)`,
    `D_hat = N diag(S_hat(j,j)/N_j)` (eq. 5, p. 9). Two arms: `X^2 = t^2` with
    `t = tau_hat / sqrt(S1/N1 + S2/N2)` (Corollary 3, eq. 10, p. 12).
  - Finite-population asymptotics, N -> infinity with every arm share in (0,1) and N_j >= 2 (pp. 4, 7).

- **Main findings.**
  - A statistic is called proper if its randomization distribution asymptotically dominates its sampling distribution under the weak null (Proposition 4, pp. 8-9).
  - Theorem 1 (p. 9): under the weak null `X^2 -> sum_j a_j xi_j^2` with `a_j in [0,1]`; its randomization
    distribution -> chi-square(m). So the FRT with X^2 is asymptotically conservative for the weak null and exact for the sharp null.
  - Unlike the i.i.d. case, the test is conservative, not asymptotically exact, because arm means stay correlated in a finite population (p. 9).
  - "Barring studentization, the FRT may not control type I error even asymptotically" (p. 3). The classical F,
    the Box-type statistic and |difference in means| are not proper in general (Theorems 2-3, pp. 10-11).
  - Two arms: |tau_hat| is fine only if N1 = N2 or the two potential-outcome variances are equal (Corollary 3, p. 12).
    With more than two arms even balance does not save F (p. 13, p. 24).
  - One-sided weak null `C Ybar >= x`: use `t+ = max(t, 0)`; `t -> N(0, a)`, `a <= 1`, randomization limit N(0,1)
    (Corollary 5, p. 16). The untruncated t also works for p-values up to 0.5 (p. 16).
  - Clustered assignment: analyse cluster-level aggregates and treat clusters as the units (Section 4.8, p. 16).
  - Stratified experiments: weighted statistic (eq. 13) with within-stratum permutations (Theorem 4, p. 18);
    requires N_[h]j >= 2 and large strata, H fixed. Many small strata are explicitly not covered (p. 18).
  - Multiple components: Bonferroni over one-sided components (p. 16); closure procedure mentioned without detail (p. 21).
  - Confidence sets by inverting the FRT are asymptotically conservative (Corollary 4, p. 15).
  - Simulations (pp. 21-24): with 5 units per arm the p-value distribution is far from the asymptotic regime;
    with 20 per arm it is close (p. 23). FRT with F over-rejects at small p-values at every sample size (p. 24).
  - Applications (Tables 1-2, pp. 26-27): FRT and chi-square p-values with X^2 nearly coincide (e.g. 0.27% vs
    0.25%); F-based and X^2-based p-values can differ by a factor of several (1.59% vs 0.27%).

- **Usable for our paper.**
  - Method: vocabulary and citation for sharp vs weak null. Our raw-statistic p-value tests the sharp null "the siren changed nothing on any date"; a statement about the average effect needs a studentized statistic (pp. 2-3, Theorem 1 p. 9).
  - Method: the date is the unit of assignment and cells are a cluster within it; aggregate to date level before permuting (p. 16). Supports "effective sample = dates".
  - Method: one-sided testing with the studentized t is covered (Corollary 5, p. 16; trend tests p. 13).
  - Method: permute within year only, as in a stratified design (p. 18).
  - Robustness / Results: Bonferroni across the five speed classes is the fallback the paper itself names (p. 16).
    **[own arithmetic]** 0.008 x 5 = 0.04 survives; 0.034 x 5 = 0.17 does not.
  - Results-Discussion: confidence intervals from test inversion with the studentized statistic have an average-effect interpretation only asymptotically (Corollary 4, p. 15).

- **Caveats.**
  - Assumes physical randomization. Nov 10 is not randomly chosen; our "assignment" is an exchangeability assumption, so none of the design-based guarantees transfer automatically.
  - Requires N_j >= 2 per arm and stratum (p. 4, p. 17). We have one treated date per year: the within-year
    treated variance does not exist, and the paper says small-strata designs are outside its theory (p. 18).
  - Asymptotic in the number of units; with 20 date-units (5 treated) we are at or below the "5 per arm" case the paper shows to be unreliable (p. 23).
  - Covariate adjustment is not covered (p. 28).
  - The paper does not claim the studentized FRT is exact for the weak null in finite samples.

- **Checks it suggests.**
  1. Studentize across years, the only feasible way with one treated date per year:
     `t = mean_y(D_y) / (sd_y(D_y)/sqrt(5))`, recomputed under each of the 1024 placebo assignments; one-sided p. Report with the raw-statistic p.
  2. Pooled Welch-type alternative: remove year means from c, then `t = (mean_T - mean_C)/sqrt(S_T/5 + S_C/15)`; permute within year.
  3. Report both the sharp-null wording and the average-effect wording explicitly in the Method section.
  4. Holm/Bonferroni over the five speed classes; pre-specify the 50-70 km/h class as primary if defensible.

---

### caughey2023 - Caughey, Dafoe, Li & Miratrix (2023), Randomization inference beyond the sharp null

- **Question and setting.** Randomized experiment, two arms, fixed potential outcomes. Is a one-sided
  randomization test informative beyond the sharp null? Yes: for many statistics the same p-value is exactly
  valid for a bounded (one-sided) null with arbitrary heterogeneity, and test inversion gives intervals for the
  maximum effect and for effect quantiles (pp. 1-5).

- **Data and method.**
  - Sharp null `H_delta: tau = delta`; bounded null `H_{<=delta}: tau_i <= delta_i for all i` (eqs. 1, 7; pp. 7, 11).
  - p-value with imputed control outcomes: `p = sum_a Pr(A=a) 1{ t(a, Y - Z*delta) >= t(Z, Y - Z*delta) }` (eq. 4, p. 8).
  - Statistic properties (p. 9): effect increasing (raising treated outcomes or lowering control outcomes never lowers t);
    differential increasing; distribution free.
  - Class 1: `t = sum_i z_i psi_1i(y_i) - sum_i (1-z_i) psi_0i(y_i)` with increasing psi; includes the difference
    in means; it is effect increasing and differential increasing (eq. 5, Proposition 1, p. 10).
  - Class 2: rank-score statistics `sum_i z_i phi(rank_i)`; effect increasing, and distribution free under
    exchangeable assignment with random tie-breaking (eq. 6, Proposition 2, p. 10). Stephenson ranks weight large outcomes (pp. 10-11).

- **Main findings.**
  - Theorem 1(a) (p. 12): if t is effect increasing or differential increasing, the sharp-null p-value satisfies
    `Pr(p <= alpha) <= alpha` under the bounded null, in finite samples. Stated to hold for general assignment
    mechanisms, including blocking (p. 12).
  - Theorem 1(b) (p. 12): the p-value is monotone in delta if t is differential increasing, or effect increasing and distribution free.
  - Corollary 1 (p. 13): inverting constant-effect tests gives a one-sided confidence interval `[c, inf)` for the
    maximum unit effect. Without a constant-effect assumption, that is the valid reading of the usual inverted interval (p. 3).
  - Same results for statistics computed on observed outcomes `t(Z, Y)` (the usual way a difference in means is
    used), provided t is effect increasing (Theorem A1 and Corollary A1, p. 33). For the no-effect null the two p-value constructions coincide (p. 33).
  - Opposite direction: flip the sign of outcomes or swap labels; two-sided via Bonferroni (p. 19).
  - Quantiles: with exchangeable assignment (complete or Bernoulli randomization) and a rank-score statistic,
    `H_{k,c}: tau_(k) <= c` has the closed-form valid p-value of eq. 13 (Theorem 3, p. 15); intervals for all
    quantiles are simultaneously valid without multiplicity correction (Theorem 5, p. 18).
  - Effect range: combining a lower limit for the max and an upper limit for the min, each at level alpha/2,
    gives a valid test of a constant effect (Theorem 6, p. 19).
  - Simulations (n = 120, alpha = 0.1): difference in means and Wilcoxon have almost no power to detect a
    positive maximum effect when the average effect is not positive; Stephenson ranks do (pp. 20-21). s = 6 is suggested as a default (p. 23).
  - Application (164 treated, 69 control): 90% interval says at least 88 of 233 units (37.8%) had positive
    effects with Stephenson s = 6; Wilcoxon gives 59 (25.3%) (p. 24). The effect-range interval was uninformative there (p. 24).

- **Usable for our paper.**
  - Method: our statistic D is of class (5): `psi_1 = y/5` on Nov 10 dates, `psi_0 = y/15` on controls, so it is
    effect increasing **[own check against Proposition 1]**. With signs flipped for a slowdown, the one-sided
    placebo-date p-value is exactly valid, under the randomization model, for the bounded null
    "the siren did not reduce the contrast on any Nov 10 (effects may differ by year and may be positive)" (Theorem 1(a) p. 12; Theorem A1 p. 33; sign flip p. 19).
  - Method: blocking by year is allowed for this result (p. 12).
  - Results-Discussion: rejecting means "in at least one year the siren slowed traffic" (p. 12). This needs no asymptotics and no constant-effect assumption, which suits 20 date-units.
  - Results-Discussion: an interval obtained by inverting the test over constant shifts is an interval for the largest year-level slowdown, not for the average (Corollary 1, p. 13; p. 3).
  - Literature: positions the bounded null between the sharp null and the weak null; cites Chung-Romano and Wu-Ding as the studentization route (p. 2).

- **Caveats.**
  - The paper is not about average effects, "nor is it a substitute for average treatment effect estimation" (p. 25).
    Our headline 0.73 full-stop-equivalent minutes is an average; the bounded-null result supports existence and direction, not that magnitude.
  - Validity is shown for effect-increasing statistics such as the raw difference in means. The paper does not
    show that a studentized t is effect increasing. So the bounded-null guarantee (raw statistic) and the
    weak-null guarantee (studentized statistic) come from different statistics **[own observation]**.
  - Quantile and count results (Theorems 3-5) are stated for exchangeable assignment across all units and
    rank-score statistics (pp. 14-18). One treated date per year is blocked, not exchangeable; these results
    do not carry over as stated. With 5 treated units they would be nearly uninformative anyway (Remark 2, p. 16).
  - Assumes genuine randomization and no interference; ours is as-if randomization over calendar dates.
  - Units are dates. At cell level the assignment is clustered, which the paper does not treat.

- **Checks it suggests.**
  1. State both nulls in the Method section: sharp (no effect on any date) and bounded (no slowdown in any year).
  2. Invert the one-sided test over a constant shift on the log scale and report the bound as "largest year-level slowdown is at least c" with its minute equivalent `60(1 - exp(c))`.
  3. Rank-based robustness: Wilcoxon-type rank-sum of date contrasts within year (stratified ranks), still effect increasing.
  4. Do not present inverted-test intervals as intervals for the mean effect unless a constant effect is assumed and said.

---

### ding2016 - Ding, Feller & Miratrix (2016), Randomization inference for treatment effect variation

- **Question and setting.** Randomized experiment with binary treatment. Test whether unit-level effects vary
  beyond a constant, or beyond what a specified model with covariates or subgroups explains, without modelling
  assumptions (pp. 1-2).

- **Data and method.**
  - Null of constant effect `H0C: Y_i(1) - Y_i(0) = tau for all i, some tau` (eq. 1, p. 3). Not sharp because tau is unknown; tau is a nuisance parameter.
  - Statistics: variance ratio (p. 4); shifted Kolmogorov-Smirnov `t_SKS = max_y |F0_hat(y) - F1_hat(y + tau_hat)|` (p. 5); quantile-process statistics (p. 5).
  - Known tau: impute all potential outcomes and run the FRT (steps a-e, p. 6).
  - Unknown tau, plug-in (FRT-PI): impute with tau_hat. For this, "there are no general theoretical guarantees from such a procedure" (p. 6).
  - Unknown tau, confidence-interval method (FRT-CI, after Berger-Boos): `p_gamma = sup_{tau' in CI_gamma} p(tau') + gamma`,
    with CI_gamma a (1 - gamma) interval for tau; valid in finite samples (Proposition 1, p. 7; proof p. 22). They use gamma = 0.001 (p. 11).
  - Beyond a model: `H0W: Y_i(1) - Y_i(0) = beta'W_i` (eq. 4, p. 9); statistic = KS on residuals from regressing Y on W, Z, W x Z; maximise p over a confidence region for beta (p. 9).
  - Subgroups: `H0joint: Y_ik(1) = Y_ik(0) + tau_k` in group k (p. 9); statistics pool or weight group-wise recentred CDFs, e.g. `t_WSKS = sum_k (n_k/n) t_SKS,k` (p. 10).

- **Main findings.**
  - Comparing the plug-in KS statistic with standard KS critical values is invalid; its null limit depends on the outcome distribution (p. 5; Theorem 4, p. 20).
  - Size at nominal 5% (Table 1, p. 12): FRT-PI 11.3% (exponential) and 15.1% (log-normal) at n = 100;
    FRT-CI between 1.9% and 5.0% everywhere; a pooled-residual bootstrap 5.0-9.3%; naive plug-in from 0% to 44.7%.
  - Power (Table 2, p. 13): normal outcomes, sigma_tau = 0.5: FRT-CI 23.1% at N = 100, 93.0% at N = 400;
    log-normal: 19.3% and 70.5%, well above subsampling (5.9%, 32.9%).
  - Illustration with two subgroups: constant-within-group null not rejected (p = 0.46; 0.43 with known effects;
    0.39 plug-in), single constant effect rejected (p < 0.005). Reading: the grouping accounts for the heterogeneity (p. 10).
  - Head Start (2,238 treated, 1,348 control): p = 0.033 without covariates; 0.005, 0.005, 0.003 with covariates and subgroup-varying effects (Table 3, p. 14).
  - Whether an effect is constant depends on the outcome scale; constant in levels is not constant in logs (pp. 3-4).
  - The test is omnibus; rejection does not identify the source of variation (p. 1). The FRT respects stratified or paired designs automatically (p. 2).

- **Usable for our paper.**
  - Method / Results: citation for the logic "is there heterogeneity beyond a single effect, and do the speed classes account for it?" via the two nulls H0C and H0joint (pp. 3, 9-10).
  - Method: the FRT-CI device (maximise p over a confidence set, add gamma) for any test with a nuisance effect size (p. 7).
  - Method: scale argument for analysing log speed (pp. 3-4). **[own]** If every vehicle loses the same s minutes
    in the hour, hourly mean speed falls by the factor (1 - s/60) at every base speed, so the effect is constant
    on the log scale. Differences across speed classes in D are then differences in stopping behaviour or
    measurement, not an artefact of scale. This depends on how İBB averages speeds, which we do not know.
  - Robustness: warning against plug-in heterogeneity tests with skewed outcomes (Table 1, p. 12).

- **Caveats.**
  - The paper tests idiosyncratic variation across units. It does not develop a test of equal average effects
    across pre-defined groups; our "do classes differ?" question is adjacent, not identical.
  - Simulations start at N = 100 and power is low there. With 20 date-units a distributional (KS) heterogeneity test across dates is close to powerless.
  - Rejecting H0C on the CDF scale formally rejects a constant unit effect, not a parallel shift of marginals; the authors treat the two as practically the same (p. 3).
  - Randomization is assumed; discrete or bounded outcomes make a constant-effect null implausible (p. 14). Our MINIMUM_SPEED is never below 1 km/h, so a similar boundary issue may apply.

- **Checks it suggests.**
  1. **[own adaptation]** Triple-difference permutation test for two speed classes a and b: on each date form
     `W_d = c_{a,d} - c_{b,d}`. Under "equal effect in a and b in every year" the common effect cancels, so the
     null is sharp for W and no nuisance step is needed. Statistic: `mean_y [W_{y,Nov10} - mean_controls W_{y,d}]`; same 1024 assignments.
  2. Omnibus version over five classes: statistic = between-class variance (or range) of class-level D; impute
     under a common effect tau', maximise p over a 99.9% interval for tau', add 0.001 (FRT-CI, p. 7). Permute dates, never cells.
  3. Two-step reading as on p. 10: test a single common effect, then test "constant within speed class" at cell level with date-level permutation.
  4. Report heterogeneity results as exploratory given 5 events.

---

## Cross-paper synthesis (what jointly matters for our design)

1. None of the five papers covers our exact case: non-random, calendar-fixed treatment; one treated date per year; five years. Every guarantee below is conditional on an as-if-random or symmetry assumption that we must state and probe.
2. Our raw-statistic placebo-date p-value (floor 1/1024) tests the sharp null; by caughey2023 it is also exact for the bounded null "no slowdown in any year". Claim existence and direction from it, not the average size.
3. A claim about the average effect needs studentization (chung2013, wu2021). With one treated date per year this can only be done across years: `t = mean(D_y)/(sd(D_y)/sqrt(5))`, permuted over the 1024 assignments. Report it beside the raw statistic.
4. Imbalance makes the unstudentized test fragile to unequal variances (chung2013 Example 2.1); widening the control pool to about 52 dates increases imbalance. Check the Nov 10 vs control variance ratio.
5. The canay2017 sign-change test on the five `D_y` is the natural second procedure: 32 sign vectors, one-sided floor 1/32 = 0.031, attained only if all five years are negative; two-sided floor 0.0625. It cannot support multiplicity-adjusted claims for five speed classes.
6. That test needs independent years and `D_y` symmetric about zero (in practice median zero). Skewed date shocks with a precise control mean break it; a one-control paired version is exactly symmetric. Run the placebo sign-share check.
7. Asymptotic results need sample sizes we do not have: wu2021 shows 5 per arm is far from the limit, chung2013 shows over-rejection at m = n = 5. Prefer finite-sample statements (points 2 and 5) for headline inference.
8. Inference units are dates (wu2021 cluster section; canay2017 clusters). Sub-dividing a date into cells or regions adds no independent information because they share the date shock.
9. Speed-class heterogeneity: use a difference-between-classes statistic so the common effect cancels and the null is sharp; treat ding2016's FRT-CI as the tool when a nuisance effect remains. Label as exploratory.
10. Neither permutation scheme repairs the trend threat (Nov 10 always 2nd of 4): a November trend violates exchangeability and symmetry alike. A symmetric-neighbour contrast (Nov 3 and Nov 17) or the widened pool with a trend term is a design fix, not an inference fix.
