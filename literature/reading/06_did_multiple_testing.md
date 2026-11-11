# 06 - DiD inference, pre-trends, and multiple testing with resampling

Reader notes for: bertrand2004, roth2023, romano2005a, romano2005b, list2019.
Page numbers are the `=== page N ===` markers of the text files (= PDF pages of the versions we hold).

**Versions we hold (matters for citing):**

| key | what the file actually is | published version |
|---|---|---|
| bertrand2004 | NBER WP 8841, March 2002 | QJE 119(1), 2004 |
| roth2023 | arXiv 2201.01194v3, Jan 2023 | J. Econometrics 2023 |
| romano2005a | "Stepwise Multiple Testing as Formalized Data Snooping", preprint Oct 2003 | Econometrica 73(4), 2005 |
| romano2005b | "Exact and Approximate Stepdown Methods for Multiple Hypothesis Testing", preprint Dec 2003 | JASA 100(469), 2005 |
| list2019 | NBER WP 21875, Jan 2016 | Experimental Economics 2019 |

Two warnings. (1) Our keys a/b for Romano-Wolf are the reverse of the labels List et al. use (their "2005a" is the JASA paper, our romano2005b). (2) All numbers below come from the working-paper versions; check them against the published versions before quoting them in the paper. For bertrand2004 this is not cosmetic, see its Caveats.

---

### bertrand2004 - Bertrand, Duflo & Mullainathan (2002 WP; QJE 2004), How much should we trust DiD estimates?

- **Question and setting.** Standard DiD regressions on many periods of a serially correlated outcome, with a treatment dummy that switches on once and stays on, give standard errors that are far too small. The paper measures how bad this is with placebo laws and compares fixes.

- **Data and method.**
  - Survey of 92 DiD papers in six journals, 1990-2000 (pp. 6-8, Table 1 p. 27).
  - CPS Merged Outgoing Rotation Group, women aged 25-50, 1979-1999, log weekly earnings; about 300,000 women with positive earnings, aggregated to 50 states x 21 years = 1,050 state-year cells (p. 8).
  - Placebo laws: draw a passage year uniformly from 1985-1995, pick 25 states at random, set T_st = 1 for those states after that year, estimate Y_st = a_s + g_t + beta*T_st + e_st by OLS, record whether |t| > 1.96. Repeat at least 200 times. A correct procedure rejects 5% of the time (p. 9).
  - Power: same exercise after adding a true effect of 0.02 log points to the treated observations (p. 9).
  - "Manufactured" data: normal AR(1) panels matched to the CPS variance decomposition, so that there is certainly no real law and no trend (p. 12).
  - Fixes compared: parametric AR(1) correction, block bootstrap, empirical covariance matrix, state-clustered ("arbitrary") covariance, collapsing to pre/post, and randomization inference (Section 4).

- **Main findings.**
  - Theory: with AR(1) errors (rho) and an AR(1) regressor (lambda), the ratio of the OLS-estimated variance to the true variance tends to (1 - rho*lambda)/(1 + rho*lambda) as T grows. No bias if the regressor is serially uncorrelated (lambda = 0); the bias grows with T (p. 6).
  - Survey: 69 of 92 papers use more than two periods; 65 have a potential serial-correlation problem; only 5 correct for it. Mean number of periods 16.5, median 11 (pp. 6-7, Table 1 p. 27). 80 of 92 have a grouped-error (Moulton) problem and only 36 deal with it (pp. 7-8).
  - CPS wage residuals: autocorrelations 0.51, 0.44, 0.33 at lags 1-3 (pp. 8-9).
  - Placebo rejection rates at nominal 5%: micro data, plain OLS 67.5%; micro data clustered at state-year 44%; aggregated state-year data, OLS 43.5% (pp. 10-11, Table 2 p. 28). The abstract summarises this as up to 45% (p. 2).
  - When the placebo law is switched on and off at 10 random dates, so the treatment variable is serially uncorrelated, rejection falls to 6% (p. 12, Table 2 row 4). This isolates serial correlation as the cause.
  - Size of the false "effects": about 0.02 in absolute value on average; roughly 60% lie between 1% and 2% (p. 13, Table 3 p. 29).
  - Outcome persistence matters: for change in log wage (first autocorrelation -0.046) the rejection rate is 0, i.e. OLS is conservative; in manufactured data rho = 0.2 gives 12.3%, rho = 0.4 gives 19%, rho = -0.4 gives 0.8% (p. 14, Table 4 p. 30).
  - Number of periods: 7 years 16%, 5 years 8% (CPS) or 17.5% (manufactured), 50 years about 50%. The number of states does not change over-rejection (p. 15, Table 5 p. 31).
  - Fixes: parametric AR(1) correction still 34.5% (p. 15); block bootstrap 35% in CPS, fine only with 400 states (p. 17, Table 7 p. 33); state clustering 6% with 50 states but 8.5% with 10 and 15% with 6 (pp. 18-19, Table 9 p. 35); collapsing to pre/post 6% with 50 states but residual aggregation gives 31.5% with 6 states (pp. 19-20, Table 10 p. 36).
  - Randomization inference (compare the actual estimate with the distribution of placebo-law estimates): size 6.5% with 51 states, 4.5% with 20, 5.5% with 10, 4% with 6. Power against a 2% effect: 23.5% with 51 states but only 10% with 20 and 7% with 6 (pp. 22-23, Table 11 p. 38). In manufactured data its power (30% AR(1), 84% iid) is close to the upper bound from the true covariance matrix (32%, 78%) (p. 22).
  - RI needs an assumption about the assignment process. Restricting placebo dates to a 5-year window, a 3-year window, or the same year gives nearly identical size and power (pp. 22-23), but the authors warn that this robustness to a wrong assignment model is a simulation finding and may not hold in general (fn. 35, p. 23).
  - Usual diagnostic checks do not rescue OLS inference: requiring no significant pre-trend still leaves rejection above 20%; adding a treatment-specific trend leaves 10.5-15% (p. 24, Table 12 p. 39).

- **Usable for our paper.**
  - *Method.* Justification for doing inference at the level where treatment varies. The siren hits every cell at once, so cells within a date share the shock; this is the grouped-error problem (p. 4 fn. 5, pp. 10-11). Supports "effective sample = dates, not cells" and our averaging over cells before inference.
  - *Method.* Precedent for randomization inference over placebo treatment assignments in DiD, described as needing no assumption on the error term beyond the assignment model, and "valid for any sample size" (p. 21). Our 4^5 = 1024 enumeration is the exact version of their 400 random placebo draws (p. 22).
  - *Method.* RI can test a non-zero null and give a confidence interval under a constant-effect assumption: remove theta_0 from the treated observations and rerun the test (p. 21, fn. 33).
  - *Robustness.* The placebo exercise is a template: assign a fake siren to dates or hours where nothing happens and check that our test rejects about 5% of the time (p. 9); then add a synthetic effect of known size to measure power (p. 9).
  - *Robustness.* Their window comparison (pp. 22-23) is the analogue of our choice of control pool (three adjacent weeks versus all same-weekday dates). Report both.
  - *Results-Discussion.* Low power of RI with few units (Table 11 p. 38) is a fair warning for our 5-year design: a non-rejection in a speed class is weak evidence of no effect.
  - *Literature.* The first-difference result (p. 14): our within-day contrast c is a difference across adjacent hours, which removes much of the day-level persistence. This is the direction in which naive standard errors become conservative, not liberal.

- **Caveats.**
  - The file is the 2002 working paper. From memory (not verifiable from our file), the published QJE article reorganises Section 4 and does not present randomization inference as its preferred solution; it emphasises clustering, collapsing and, with enough states, the block bootstrap. Before citing "Bertrand et al. (2004)" for randomization inference, open the QJE version. If RI is not there, cite the NBER working paper explicitly, or cite roth2023 (p. 40-41) and the RI literature in other reading groups instead.
  - Their problem is a persistent treatment dummy over many periods. Our treatment is one date per year, on and then off. Their own row 4 (p. 12) shows that this configuration does not produce the serial-correlation over-rejection. So the paper does not say our design suffers from the 45% problem; it says the opposite for an on/off treatment. What remains for us is serial dependence of the outcome across adjacent weeks, which affects exchangeability of dates, not OLS standard errors.
  - RI validity rests on knowing how treatment was assigned (p. 22). Nov 10 is fixed by the calendar, not drawn at random. The paper offers simulations, not a theorem, for robustness to a misspecified assignment model (fn. 35, p. 23).
  - Their RI is two-sided with p/2 cut-offs (pp. 21-22); they say nothing on one-sided tests or on multiple outcomes.
  - All simulation cells use about 200 replications, so rejection rates have standard errors of 1-3 points (table notes).

- **Checks or analyses it suggests for us.**
  1. Placebo-siren size check: apply the full pipeline (within-day contrast, DiD, 1024-assignment test) to weekdays with no event, e.g. the same weekday in October or late November as fake "treated" dates, and to fake hours (08h or 11h as the "siren hour") on real dates. Report the share of placebo tests with p <= 0.05.
  2. Power check: add ln(1 - m/60) to ln v(09h) on the treated dates of a placebo configuration for m = 0.25, 0.5, 0.75, 1 minute and report the rejection rate of the 1024-assignment test.
  3. Report the autocorrelation of the date-level contrast c across consecutive same-weekday dates, by speed class. If it is near zero, exchangeability of adjacent weeks is more credible.
  4. RI confidence interval for D (and for minutes) by test inversion (p. 21), stated as valid under a constant effect.
  5. Show results with the narrow pool (Nov 3, 17, 24) and the wide pool side by side, as in their rows 2-5 of Table 11.

---

### roth2023 - Roth, Sant'Anna, Bilinski & Poe (2023), What's trending in DiD? A synthesis

- **Question and setting.** A review that states the canonical DiD assumptions and organises the recent literature by which assumption is relaxed: treatment timing, parallel trends, or the sampling framework for inference. It ends each part with recommendations and a practitioner checklist (Table 1, p. 47).

- **Data and method.** No data. Canonical model: two periods, treated and untreated populations, potential outcomes Y_it(0), Y_it(1). Target: ATT in period 2. Assumptions: parallel trends, E[Y_2(0) - Y_1(0) | D=1] = E[Y_2(0) - Y_1(0) | D=0] (p. 6); no anticipation, Y_1(0) = Y_1(1) for treated units (p. 7); SUTVA, which excludes spillovers (pp. 5-6); and for inference, iid sampling of many clusters (p. 8).

- **Main findings.**
  - With one common treatment date and a balanced panel, TWFE equals the simple DiD of means and is easy to interpret (p. 8; checklist p. 47). The negative-weight and forbidden-comparison problems arise only with staggered adoption and heterogeneous effects (pp. 12-15).
  - Baseline choice: using only the last pre-period (Callaway-Sant'Anna) needs parallel trends over a short horizon; averaging all pre-periods (Borusyak-Jaravel-Spiess) is more efficient when errors are not too serially correlated but needs parallel trends over the whole window, and its bias grows if trends diverge with distance (pp. 18-19).
  - Parallel trends depends on functional form: holding in levels generally means not holding in logs, and the reverse. It is invariant to transformations essentially only under (as-if) random assignment or a stable untreated distribution (p. 22).
  - Pre-trend tests: (i) parallel pre-trends do not guarantee parallel post-trends (p. 30); (ii) low power: a linear trend violation that a pre-test detects half the time also produces a spurious significant effect half the time, ten times the nominal 5% (p. 30); (iii) conditioning on passing the pre-test adds pre-test bias (p. 31); (iv) in Roth's calibrated simulations, violations detectable only 50% of the time often give bias as large as the estimated effect (p. 31).
  - Better diagnostics: power calculations for the pre-test against stated violations; non-inferiority tests with H0: max_{r<0} |beta_r| >= c (pp. 31-32).
  - Sensitivity analysis (Rambachan-Roth): bound the post-treatment violation by the pre-treatment ones, |delta_1| <= Mbar * max_{r<0} |delta_r|, or bound the deviation from a linear extrapolation of the pre-trend; report the breakdown Mbar at which the conclusion fails (pp. 32-33, 36).
  - Bracketing (Ye et al.): with two control groups a, b whose untreated trends bracket the treated one, min{Delta(a), Delta(b)} <= Delta(trt) <= max{Delta(a), Delta(b)}, the ATT is bounded by the two corresponding DiDs (p. 34).
  - Few clusters: cluster-robust inference fails because cluster-level shocks do not average out (p. 37). Model-based fixes (Donald-Lang, Conley-Taber, Ferman-Pinto, Hagemann) each need a homogeneity assumption (pp. 38-39). The wild cluster bootstrap also needs strong homogeneity and can do badly with few treated clusters (pp. 39-40).
  - Fisher randomization tests: exact in finite samples under the sharp null of no effect for any unit if treatment is randomly assigned; no restriction on heterogeneity of potential outcomes; but random assignment is often doubtful in DiD and the sharp null is less interesting than the weak null of no average effect. Recommended as a useful benchmark (pp. 40-41).
  - Alternative with few clusters: condition on the cluster-level shocks, treat them as a parallel-trends violation, and do sensitivity analysis benchmarked on pre-period violations (p. 40).
  - Design-based view (Rambachan-Roth): units fixed, assignment random. The DiD estimator is unbiased for a finite-population ATT if sum_i (pi_i - N_1/N) (Y_i2(0) - Y_i1(0)) = 0, i.e. treatment probabilities are uncorrelated with untreated trends (p. 42). Cluster-robust standard errors are then valid, possibly conservative, when clustering is at the assignment level (pp. 42-43).
  - Triple differences can be written as a DiD on a transformed outcome (p. 45).
  - Event-study plots should carry simultaneous, not pointwise, confidence bands (p. 35).

- **Usable for our paper.**
  - *Method.* State our identifying assumptions in their language: (a) parallel trends in the within-day contrast: absent the siren, the 09h-versus-08h/10h log-speed contrast on Nov 10 would equal its average on the control dates (p. 6); (b) no anticipation: 08h on Nov 10 is unaffected (p. 7); we also need no carry-over into 10h, which is our own addition and not in the paper; (c) SUTVA across dates (pp. 5-6).
  - *Method.* Common treatment date, so the staggered-adoption estimators are unnecessary; one sentence citing the checklist (p. 47) closes that question.
  - *Method.* Level of inference: "cluster at the level at which treatment is independently assigned" (p. 43). For us that level is the date. This is the cleanest citation for "effective sample = dates, not cells".
  - *Method.* Our transformed-outcome construction (contrast c first, then compare dates) matches their remark that a DDD is a DiD on a transformed outcome (p. 45).
  - *Method / Robustness.* Randomization tests as a benchmark with few clusters, with their stated price: an assignment assumption and a sharp null (pp. 40-41). Quote the limitation ourselves before a referee does.
  - *Robustness.* Functional form: we use ln v. Cite p. 22 and report the estimate in levels (km/h) as well, with a reason for preferring logs (proportional hour-of-day profile across cells of different speed).
  - *Robustness.* The trend threat (Nov 10 is always the 2nd of 4 dates) is a parallel-trends violation in their sense; the remedies they list are the sensitivity bound relative to a linear extrapolation (p. 33) and bracketing by an earlier and a later control (p. 34).
  - *Robustness.* The trade-off on pp. 18-19 applies directly to widening the control pool to all same-weekday dates of the year: more precision and a finer randomization distribution, at the cost of needing the same within-day profile over the whole year.
  - *Results-Discussion.* Do not present an insignificant placebo or pre-period test as proof of validity (pp. 30-31, 35).

- **Caveats.**
  - It is a review; the results belong to the cited papers. For anything load-bearing (design-based DiD, sensitivity bounds) cite the original as well.
  - The design-based results quoted are for the two-period model with many independently assigned units (p. 42). They do not cover one treated date per year among four.
  - The paper does not discuss multiple hypothesis testing across subgroups, nor high-frequency or within-day designs. Our mapping of "hours" to "periods" and "dates" to "groups" is our own.
  - It does not endorse randomization inference as generally valid for DiD; it calls it a benchmark and names its assumptions (p. 41).
  - On spillovers it only notes that the literature is young (pp. 44-45).

- **Checks or analyses it suggests for us.**
  1. Hour-level event study: estimate the Nov 10 minus control difference in ln v for each hour 06h-12h relative to a reference hour, plot with simultaneous bands. Hours before 09h are the pre-trend check; 10h and 11h show carry-over.
  2. Symmetric-control estimate: use only Nov 3 and Nov 17 as controls. With equally spaced dates this removes any linear week-to-week trend exactly (our arithmetic: with controls at positions 1, 3, 4 and treatment at 2, a linear slope s per week biases D by -0.67 s; with positions 1 and 3 the bias is 0). Compare with the three-control estimate.
  3. Bracketing bounds: DiD against Nov 3 only and against Nov 17 only; report the interval between them (p. 34).
  4. Sensitivity statement in the Rambachan-Roth spirit: how large would the Nov 10 violation have to be, as a multiple of the largest placebo-date contrast, to remove the effect (pp. 33, 36).
  5. Power of the placebo tests: state the smallest violation our placebo-date and placebo-hour tests could detect (pp. 31, 35).
  6. Levels versus logs (p. 22).
  7. Narrow versus wide control pool, discussed as the efficiency-versus-assumption trade-off of pp. 18-19; for the wide pool, check that the 08h-09h-10h profile is stable across seasons (school terms, daylight).

---

### romano2005a - Romano & Wolf (2003 preprint; Econometrica 2005), Stepwise multiple testing as formalized data snooping

- **Question and setting.** When K strategies are compared with a benchmark, which ones beat it, controlling the probability of any false rejection? White's bootstrap reality check only tests the best one. The paper gives a stepdown procedure (StepM) that uses the joint bootstrap distribution of the statistics.

- **Data and method.**
  - Hypotheses H_k: theta_k <= 0 versus theta_k > 0, k = 1..K, one-sided (p. 6). Error criterion: familywise error rate, FWE = P(reject at least one true H_k), with strong control, i.e. for every configuration of true and false nulls (p. 6).
  - Bonferroni: reject H_k if p_k < alpha/K (p. 7). Holm: order p_(1) <= ... <= p_(K); reject H_(k) if p_(j) < alpha/(K-j+1) for all j <= k (p. 7).
  - Basic StepM, Algorithm 3.1 (p. 10): order the statistics w_(1) >= ... >= w_(K). Step 1: let c_1 be the (1-alpha) quantile of max over all k of (w*_k - theta*_k) under the estimated distribution; reject every H_k with w_k - c_1 > 0. If none, stop. Otherwise recompute the quantile of the maximum over the not-yet-rejected hypotheses only, reject again, and repeat until no further rejection. Critical value definition, eq. (10) p. 10; bootstrap computation, Algorithm 3.2 p. 13 (same J bootstrap draws reused at every step; J >= 1000 recommended).
  - Studentized StepM, Algorithms 4.1-4.2 (pp. 14-15): same with z_k = w_k / sigma_k and max of (w*_k - theta*_k)/sigma*_k.
  - Theory: under bootstrap consistency for the joint distribution of sqrt(T)(W - theta), every false null is rejected with probability tending to one and limsup FWE <= alpha (Theorems 3.1 and 4.1, pp. 11, 14). No subset pivotality needed, unlike Westfall-Young (p. 11).
  - Simulations: K = 40, T = 100 (iid) or 200 (AR(1), coefficient 0.6), J = 200, 2,000 repetitions, alpha = 0.10 (pp. 19-21). Application: CAPM alphas of 100 stocks, 120 months, J = 1,000 (p. 22).

- **Main findings.**
  - Bonferroni and Holm are conservative because they guard against the worst-case dependence. With perfectly dependent p-values one could reject at p_k < alpha with no adjustment (p. 8). "the Holm method can also be very conservative" (p. 8).
  - The first step of StepM is the single-step max-statistic test (a modified reality check). Later steps use smaller critical values, so stepdown rejects at least as much. The gain over single-step is the analogue of Holm over Bonferroni (p. 9, fns. 9-10).
  - iid simulations, nominal FWE 10%: all methods control FWE (9.4-11.1% when few nulls are false). Average number of false nulls rejected, 40 false, cross-correlation 0.5: basic single-step 17.2, basic stepdown 23.3, studentized single-step 25.2, studentized stepdown 29.4 (p. 20, Table 1 p. 32). With only 6 false nulls the stepdown gain is small (1.1 versus 1.2) (Table 1).
  - Higher cross-correlation raises the number of rejections because the bootstrap picks up the dependence (p. 20).
  - Time-series simulations: the unstudentized method over-rejects (FWE about 15-18% at nominal 10% when few nulls are false), the studentized one does not (about 5-7%) (p. 21, Tables 3-4 pp. 34-35).
  - Studentizing is recommended for power, size, and balance: without it, statistics with small variance get little power and those with large variance dominate the maximum (pp. 15-16).
  - Application: single-step basic finds 3 stocks, stepdown basic 5, studentized 6 (p. 22).
  - Two-sided version: use max |w*_k - theta*_k| and order by |w_k| (p. 17).

- **Usable for our paper.**
  - *Method.* Definitions to cite: FWE and strong versus weak control (p. 6); Bonferroni and Holm rules (p. 7); why resampling the joint distribution gains power when statistics are positively dependent (p. 8). Our five speed classes share the same dates and citywide shocks, so positive dependence is expected.
  - *Method.* The StepM logic and the "same resamples at every step" rule (Algorithm 3.2, p. 13).
  - *Method.* Argument for putting the five class statistics on a common scale before taking the maximum (pp. 15-16).
  - *Literature.* The usual citation for "Romano-Wolf stepdown" in economics.

- **Caveats.**
  - Every guarantee in this paper is asymptotic in the number of observations T, with a consistent bootstrap. We have 5 years x 4 dates. The paper gives no finite-sample result and no permutation version; that is in romano2005b. Do not cite this paper for exactness of our procedure.
  - The gain of stepdown over single-step can be negligible when few nulls are false (Table 1 p. 32; conclusion p. 23). With five classes and perhaps two real effects, expect little difference.
  - Studentized is not uniformly more powerful than basic (Table 2 p. 33; p. 23).
  - The resampling here is centred at the estimate (w* - theta*), not imposed under the null. A permutation scheme works differently (it imposes the null), so Algorithm 3.2 cannot be copied literally for our 1024 assignments.

- **Checks or analyses it suggests for us.**
  1. Report single-step max-statistic and stepdown adjusted p-values side by side with Bonferroni and Holm.
  2. Put class statistics on a common scale (see the algorithm under romano2005b, variant B) and check that conclusions do not depend on the scale choice.
  3. Report the correlation matrix of the five class statistics across the 1024 assignments; it explains how far the resampling adjustment departs from Holm.

---

### romano2005b - Romano & Wolf (2003 preprint; JASA 2005), Exact and approximate stepdown methods

- **Question and setting.** What makes a stepdown procedure control the FWE, and how can it be built from resampling without Westfall-Young's subset-pivotality assumption? The answer is monotone critical values. This paper contains the finite-sample result for permutation and randomization tests, which is the one we need.

- **Data and method.**
  - k hypotheses H_j with statistics T_{n,j}, large values against H_j. I(P) = set of true nulls. For a subset K, c_K(1-alpha) is the (1-alpha) quantile of max_{j in K} T_{n,j} (eqs. 1-2, p. 3).
  - Idealized stepdown, Algorithm 2.1 (p. 4): order T_(r1) >= ... >= T_(rk). Step 1: K_1 = all; if T_(r1) <= c_{K_1}, accept all and stop, else reject H_(r1). Step j: K_j = hypotheses not yet rejected; if T_(rj) <= c_{K_j}, accept all remaining and stop, else reject H_(rj) and continue.
  - Randomization hypothesis (p. 9): under the null, the distribution of the data X is invariant under a finite group G of M transformations.
  - Single randomization test (pp. 9-10): order T(gx) over g in G as T^(1) <= ... <= T^(M); m = M - floor(M*alpha); the non-randomized test rejects if T(X) > T^(m). P-value: p = (1/M) * #{g : T(gX) >= T(X)} (eq. 16), with P(p <= u) <= u under the null (eq. 17). If G is sampled, with g_1..g_{B-1} drawn uniformly: p~ = (1/B) * [1 + #{i : T(g_i X) >= T(X)}] (eq. 18), still valid for any B (eq. 19).
  - Multiple testing with one common group G (p. 11): test H_K with T_K = max_{i in K} T_i; critical value c^_K = m-th ordered value of T_K(gX) (eq. 22); p-value p^_K = (1/M) * #{g : T_K(gX) >= T_K(X)} (eq. 23), or the sampled version (eq. 24).

- **Main findings.**
  - A stepdown that looks only at the current intersection hypothesis can have weak but not strong control (Example 2.1, pp. 4-5). Strong control holds if critical values are monotone: c_K >= c_I whenever I is a subset of K (eq. 4-5 and Theorem 2.1, p. 5).
  - Holm is the special case with statistics -p_i and critical values alpha/|K| (Example 2.4, p. 7). The general fix without monotonicity is the closure principle, i.e. taking the maximum critical value over all subsets, which is costly (Corollary 2.1, p. 7).
  - Theorem 3.1 (pp. 8-9): if the estimated critical values are monotone, then FWE <= P(max_{j in I(P)} T_j > c^_{I(P)}). So FWE control reduces to the level of one test, the test of the intersection of the true nulls.
  - With a common G, monotonicity is automatic, because for every g the maximum over a larger set is at least the maximum over a subset (eq. 21, p. 11). Hence Corollary 3.1: if the randomization hypothesis holds for G for every intersection hypothesis, the stepdown with critical values (22) controls the FWE in finite samples (p. 11). Corollary 3.2: the same with sampled transformations and the +1 p-value (24) (p. 11).
  - Hoeffding's exactness holds for any choice of test statistic (p. 10).
  - Example 3.1 (p. 12): k outcome variables, two samples. If T_j depends only on the j-th components, the randomization hypothesis holds for the reduced data X_K under H_K even when other hypotheses are false, and "the resulting procedure retains its finite sample property of controlling the FWE" (p. 12), provided the same set of g is used at every stage.
  - Example 3.2 (p. 13): several treatments against one control. The valid permutation group changes with K, monotonicity fails, and only the closure version or an asymptotic argument works.
  - Remark 3.2 (pp. 12-13): if the randomization hypothesis fails (e.g. the null is about means only), monotonicity still holds, so the problem is still reduced to the level of the single intersection test, which then is at best asymptotically right.
  - Simulation with bootstrap stepdown, 45 pairwise correlations, n = 100, B = 500, 5,000 repetitions: FWE 4.6% at 5% under the global null; with all correlations 0.3, single-step rejects 21.1 and stepdown 25.4 of 45 on average (p. 21, Table 1 p. 27). Real-data example: stepdown adjusted p-values are below Westfall-Young's independence-based ones, e.g. 0.1483 versus 0.1843 (Table 2 p. 28).

- **Usable for our paper.**
  - *Method.* The exact justification for a joint-permutation stepdown over our five speed classes: Theorem 3.1 (p. 9), Corollary 3.1 (p. 11), Example 3.1 (p. 12). Our setting has the structure of Example 3.1: each class statistic uses only that class's cells, and one assignment set serves every subset of classes.
  - *Method.* The p-value definitions with ">=" and with the observed assignment counted (eqs. 16, 23, pp. 10-11). With full enumeration the smallest possible p-value is 1/1024.
  - *Method.* If the control pool is widened so that enumeration is infeasible, sample assignments once, use the "+1" formula (eqs. 18, 24), and reuse the same draws for all classes and steps (pp. 10-12).
  - *Method.* One sentence worth making: the stepdown adds no assumption beyond those of the single-class randomization test, because FWE is bounded by the level of the intersection test (Theorem 3.1(i), p. 9; Remark 3.2, pp. 12-13).
  - *Results-Discussion.* Strong control lets us say which classes show an effect, not only that some class does (p. 3).

- **Caveats.**
  - Exactness needs the randomization hypothesis: under H_K, the joint distribution of the data of the classes in K must be invariant to which date in each year is labelled treated. That is exchangeability of the four dates within a year. A systematic date-position effect (Nov 10 always second) or differing variances across dates breaks it, and then Remark 3.2 applies: the size of the multiple test is whatever the size of the single test is.
  - The randomization hypothesis is a statement about the null of no effect on the distribution (p. 9). The paper does not discuss one-sided nulls theta_k <= 0 in the permutation section; one-sidedness enters only through using a signed statistic.
  - The preprint gives the stage rule (at stage j reject if the p-value of the current intersection hypothesis is <= alpha, p. 11) and reports adjusted p-values in Table 2 (p. 28) but does not print a formula for them. The running-maximum formula below is the standard implication of the stopping rule and agrees with list2019 Remark 3.6 (p. 11).
  - The preprint is not consistent on strict versus weak inequality for the critical-value rule: the sentence below eq. (22) on p. 11 uses a weak inequality, while p. 10 defines the non-randomized test with a strict one. Implement via the p-value form (23), which is unambiguous.
  - Section 4 onward (bootstrap, subsampling) is asymptotic and not relevant to our sample size.

#### Exact algorithm for our design (1024 joint assignments, 5 speed classes)

This is the paper's Algorithm 2.1 with the randomization critical values (22)/(23) (pp. 4, 11), written for our data. Items marked [ours] are implementation choices or derivations not printed in the paper.

**Inputs.**
- G = the M = 4^5 = 1024 assignments g = (g_2020, ..., g_2024), g_y in {1,2,3,4} = which same-weekday date in year y is labelled "treated". g_0 = the true one (Nov 10 in every year). g_0 is an element of G and is counted.
- For every g and every class k = 1..5, D_k(g) = the DiD estimate computed exactly as in the main analysis but with the dates in g as "treated".
- **Joint** means: one g is applied to all five classes at once, giving a 1024 x 5 matrix. Never permute classes separately. This is what carries the cross-class dependence (p. 12: the same set of transformations must be used throughout).
- Statistic, larger = more evidence of slowdown: T_k(g) = -D_k(g). (Any class-wise monotone transform such as minutes = 60(1 - exp(D_k)) gives the same single-class p-values but can change the max across classes; see variant B.)
- Because D is an equal-weight mean over years of year-specific contrasts, D_k(g) = (1/5) * sum_y a_{k,y}(g_y), so the matrix can be filled from a 5 x 4 x 5 array without recomputation [ours].

**Unadjusted p-values** (eq. 16):

    p_k = #{ g in G : T_k(g) >= T_k(g_0) } / M

**Variant A: max-T stepdown** (eqs. 20-23):

1. t_k = T_k(g_0). Order t_(1) >= t_(2) >= ... >= t_(5); let r_1..r_5 be the class labels in that order.
2. For j = 1..5 let K_j = {r_j, ..., r_5} (classes not yet rejected if all earlier ones were). Compute for every g

       m_j(g) = max_{k in K_j} T_k(g)

   and

       p^_j = #{ g in G : m_j(g) >= t_(j) } / M .

   (Note max_{k in K_j} T_k(g_0) = t_(j).)
3. Adjusted p-values: padj_(1) = p^_1; padj_(j) = max( padj_(j-1), p^_j ) for j >= 2. [running max: implied by the stopping rule; list2019 Remark 3.6]
4. Reject H_(j) at FWE level alpha iff padj_(j) <= alpha. Once one is not rejected, none after it is.

Equivalent critical-value form (eq. 15, 22): m = M - floor(M*alpha); for M = 1024, alpha = 0.05 gives m = 1024 - 51 = 973, alpha = 0.10 gives m = 922. c^_j = the m-th smallest of {m_j(g)}; reject H_(j) iff t_(j) > c^_j. With no ties this is the same as p^_j <= alpha, since t_(j) > c^_j means at most 51 of the 1024 values are >= t_(j).

**Single-step max-T** (first step only; romano2005a p. 9): for every class k,

    pss_k = #{ g in G : max_{all 5 classes} T_k'(g) >= t_k } / M .

Always padj <= pss.

**Variant B: min-p stepdown, balanced** [ours, by analogy with list2019 Algorithm 3.1 and Remark 3.3; valid by Corollary 3.1 because exactness holds for any statistic (p. 10) and the min over a larger set is <= the min over a subset]:

0. For every class k and every g, the within-class permutation p-value of that assignment:

       pi_k(g) = #{ g' in G : T_k(g') >= T_k(g) } / M .

   This is a rank transform of each column; no nested permutation is needed because the reference set G is the same for every g. pi_k(g_0) = p_k.
1. Order p_(1) <= ... <= p_(5), labels r_1..r_5.
2. For j = 1..5, K_j = {r_j..r_5}, q_j(g) = min_{k in K_j} pi_k(g), and

       p^_j = #{ g in G : q_j(g) <= p_(j) } / M .

3. Running maximum and decision as in A.

Properties of B [ours]: by the union bound p^_j <= |K_j| * p_(j), so B's adjusted p-values are never above Holm's; and each class has the same chance of producing the extreme value, which is the balance property of romano2005a pp. 15-16 and list2019 p. 7. A cheaper approximation to balance in variant A is to divide each column by the standard deviation of that column over G (a constant per class).

**Comparators on the unadjusted p-values** (romano2005a p. 7): Bonferroni padj_k = min(1, 5 p_k). Holm: with p_(1) <= ... <= p_(5), padj_(j) = max_{i <= j} min(1, (5 - i + 1) p_(i)).

**What to expect with the pilot numbers** [our arithmetic from BRIEF.md, not from the papers]: p = 0.008 (50-70 km/h) and 0.034 (30-50 km/h), other three classes large. Bonferroni: 0.040 and 0.170. Holm: 0.040 and 4 x 0.034 = 0.136. So at FWE 5% the 50-70 class survives even Bonferroni and the 30-50 class does not survive Holm. Under variant B the stepdown p-value of the 50-70 class lies between 0.008 and 0.040, and that of the 30-50 class between 0.034 and 0.136; where they land depends on how correlated the class statistics are across the 1024 assignments (perfect dependence gives the lower ends, the least favourable dependence the upper ends). These bounds are not guaranteed for variant A on raw statistics.

**If the pool is widened** (about 52 candidate dates per year): draw B - 1 assignments uniformly, once; replace every "#{...}/M" by "(1 + #{...})/B" (eqs. 18, 24); use the same draws for all classes and all steps (p. 12). B - 1 = 9,999 or more gives a p-value resolution of 0.0001.

- **Checks or analyses it suggests for us.**
  1. Implement variants A and B plus single-step, Bonferroni, Holm; one table with six p-value columns per class.
  2. Unit test: on a 1024 x 5 matrix with five identical columns, adjusted = unadjusted; with a single column, the procedure returns the usual RI p-value.
  3. Size check of the whole multiple-testing pipeline on placebo configurations (see bertrand2004 check 1): share of placebo runs with any class rejected at padj <= 0.05 should be about 5% or less.
  4. Count ties in T_k(g) and in the maxima; with ">=" ties make the test conservative.
  5. State the exchangeability assumption explicitly next to the result and link it to the trend checks under roth2023.

---

### list2019 - List, Shaikh & Xu (2016 WP; Exp. Econ. 2019), Multiple hypothesis testing in experimental economics

- **Question and setting.** Experimental papers routinely test several outcomes, subgroups and treatment arms without correction. The paper packages a bootstrap stepdown procedure (building on Romano and Wolf 2010) that covers all three cases, controls the FWER asymptotically, and is balanced across hypotheses.

- **Data and method.**
  - Units i = 1..n iid; outcomes Y_{i,k}; treatment D_i; baseline covariates Z_i defining subgroups (p. 6). Family of nulls indexed by s = (d, d', z, k): E[Y_k(d) - Y_k(d') | Z = z] = 0 (p. 7).
  - Assumptions: treatment randomly assigned given Z (2.1); finite positive variances (2.2); D and Z discrete, every (d, z) cell with positive probability (2.3) (pp. 7-8).
  - Statistic T_s = sqrt(n) |difference in subgroup means| (eq. 5, p. 9), optionally studentized (Remark 3.4, p. 11). Balance: reject for large J_n(T_s, s, P^_n) = one minus the unadjusted bootstrap p-value (eq. 7, p. 9).
  - Algorithm 3.1 (pp. 9-10): S_1 = all hypotheses. At step j, compare each J_n(T_s) with the (1-alpha) bootstrap quantile of max_{s in S_j} J_n(T~_s); reject those above; drop them; repeat until no rejection.
  - One set of B bootstrap resamples serves both the unadjusted p-values and the max distribution; no nested bootstrap (Remark 3.3, pp. 10-11).
  - Application: Karlan and List (2007) charitable-giving field experiment, 50,083 prior donors, 33,396 treated and 16,687 control (p. 12).

- **Main findings.**
  - Scale of the problem: with N independent true nulls at alpha = 0.05 the chance of at least one false rejection is 1 - 0.95^N = 0.226 for N = 5, 0.401 for N = 10 (p. 5).
  - Practice: 76% of 34 field-experiment articles in top journals do subgroup analysis and 29% look at ten or more subgroups, few with correction (Fink et al., cited p. 4). 84% of experimental papers test five or more outcomes and only 7% correct (Anderson, cited p. 4).
  - Theorem 3.1 (p. 10): under Assumptions 2.1-2.3 the procedure controls FWER asymptotically, limsup FWER <= alpha, and is asymptotically balanced: every true null has the same limiting rejection probability (eqs. 2-3, p. 7).
  - Bonferroni or Holm applied to the unadjusted p-values also control FWER but assume the least favourable dependence; the stepdown "will always reject at least as many null hypotheses as these procedures" (Remark 3.2, p. 10).
  - One-sided hypotheses: drop the absolute value in the statistic (Remark 3.5, p. 11). Adjusted p-value: smallest alpha at which the hypothesis is rejected by the algorithm (Remark 3.6, p. 11).
  - Subgroup example, four subgroups, outcome response rate (Table 2, p. 15): unadjusted p = 0.0003, 0.0503, 0.4560, 0.9920; stepdown 0.0003, 0.1427, 0.7017, 0.9920; Bonferroni 0.0013, 0.2013, 1, 1; Holm 0.0013, 0.1510, 0.9120, 0.9920. The marginal subgroup (0.05 unadjusted) is no longer significant after adjustment (p. 14).
  - Multiple outcomes (Table 1, p. 14): the outcome with unadjusted p = 0.05 moves to 0.0967 (stepdown), 0.10 (Holm), 0.20 (Bonferroni).
  - All 48 hypotheses together (4 outcomes x 4 subgroups x 3 arms): 21 rejected at 10% unadjusted, 13 after stepdown adjustment; one p-value goes from 0.0217 to 0.4597 (p. 16, Table 5 p. 17).
  - When the family is very large, FWER may be too strict; alternatives are k-FWER, false discovery proportion, FDR (Remark 2.2, p. 8).
  - Comparisons among several treatment arms can exploit transitivity for smaller critical values (Remark 3.7, pp. 11-12; Table 4 p. 16).

- **Usable for our paper.**
  - *Introduction / Method.* The 22.6% figure for five independent tests (p. 5) is exactly our case and motivates the adjustment in one sentence.
  - *Method.* Our five speed classes are their multiple-subgroups scenario (pp. 4, 14). Cite them for treating the classes as one family and reporting adjusted p-values.
  - *Method.* Subgroups are defined by baseline covariates Z_i (p. 6). Our speed classes must be defined from information not affected by the siren (e.g. typical speed on other days), and we should say so.
  - *Method.* Reporting template: unadjusted, stepdown, Bonferroni, Holm in adjacent columns (Tables 1-2, pp. 14-15).
  - *Method.* One-sided version (Remark 3.5, p. 11) and the definition of the adjusted p-value (Remark 3.6, p. 11).
  - *Method.* The p-value scale for balance (eq. 7, p. 9) motivates our variant B.
  - *Results-Discussion.* Their Table 2 is a close parallel for our pilot: one clear subgroup and one marginal subgroup that does not survive.
  - *Method (footnote).* Their footnotes 1-2 (p. 5) state that the finite-sample permutation stepdown of Romano and Wolf (their 2005a, our romano2005b) needs monotone critical values and that multiple treatment arms can break this. We have one treatment and several subgroups, the benign case.

- **Caveats.**
  - The guarantees are asymptotic in the number of independent units n with unit-level random assignment (Assumption 2.1; Remark 2.1, p. 8). Their example has n = 50,083. Our independent units are dates. Their bootstrap algorithm and their Stata/Matlab code are therefore not applicable to our data; we borrow the structure and use the permutation version from romano2005b.
  - The guidance for subgroup analyses in this paper amounts to: treat the subgroup tests as a family, use a dependence-aware stepdown, compare with Bonferroni and Holm. It does not discuss pre-registration, how to choose subgroups, or data-driven subgroup definitions. Do not attribute such advice to it.
  - The subgroup nulls are "no effect in subgroup z", one per subgroup (p. 7). The procedure does not test whether effects differ between subgroups. A statement like "the effect is larger in fast cells than in congested cells" needs its own test of a difference.
  - The at-least-as-many-rejections-as-Holm property is stated for their p-value-scale algorithm (Remark 3.2). It need not hold for an unbalanced max-T on raw statistics.
  - The family is whatever the researcher declares. If we also test several outcomes (average speed, minimum speed, vehicle counts) or several control pools, the family is larger than five, and their Table 5 shows how fast adjusted p-values grow (p. 17).

- **Checks or analyses it suggests for us.**
  1. Fix and state the family before the final run: five classes x one outcome (ln average speed) x one control pool as the primary family; everything else labelled secondary/exploratory.
  2. Table in the List format: class, D, minutes, unadjusted p, stepdown (A and B), Bonferroni, Holm.
  3. A separate randomization test of heterogeneity: statistic = D(fast classes) - D(congested classes) over the same 1024 assignments.
  4. Also report the pooled all-cells estimate with its single unadjusted RI p-value; a single pre-specified pooled test needs no multiplicity adjustment (Remark 3.1, p. 10).
  5. Document that class membership of a cell is fixed from non-event data.

---

## Cross-paper synthesis

1. Inference must sit at the level where treatment varies. BDM's grouped-error point (bertrand2004 pp. 10-11) and the design-based rule in Roth et al. (roth2023 p. 43) both lead to dates, not cells, as the effective sample.
2. BDM's 45% over-rejection concerns a persistent treatment dummy over many periods; for an on/off treatment their own simulation gives 6% (p. 12). Our one-date-per-year design is not exposed to that specific failure; do not cite BDM as if it were.
3. Randomization over placebo assignments is the small-sample tool both BDM (WP pp. 20-23) and Roth et al. (pp. 40-41) point to, and both name its price: an assumption about how the treated date was "chosen", and a sharp null. For us that assumption is exchangeability of the candidate dates within a year.
4. The always-second-of-four position of Nov 10 is a parallel-trends violation in Roth's sense and at the same time a violation of the randomization hypothesis in Romano-Wolf's sense (romano2005b p. 9). One fix serves both: symmetric controls (Nov 3 and 17), bracketing bounds (roth2023 p. 34), and a sensitivity statement (pp. 33, 36).
5. Placebo and pre-trend checks have low power and passing them proves little (roth2023 pp. 30-31; bertrand2004 p. 24). Report their power, and run BDM-style placebo-siren simulations for both size and power of our exact pipeline.
6. Five one-sided class tests carry up to a 22.6% familywise error if independent (list2019 p. 5). The classes are a subgroup family in List et al.'s sense and need adjusted p-values.
7. The correct reference for an exact adjustment with our 1024 joint assignments is romano2005b (Theorem 3.1, Corollary 3.1, Example 3.1): one common assignment set for all classes gives monotone critical values and finite-sample FWE control. romano2005a and list2019 are asymptotic bootstrap results and only supply the concept, the balance idea and the reporting format.
8. The stepdown adds no assumption beyond those of the single-class randomization test (romano2005b p. 9, pp. 12-13): if the single test is credible, so is the family; if not, neither.
9. Implementation rules that matter: apply each assignment to all classes jointly, count the observed assignment, use ">=", take the running maximum, put classes on a common scale (min-p or per-class standardisation), and report single-step, stepdown, Holm and Bonferroni together.
10. Expected outcome on pilot numbers: the 50-70 km/h class survives any correction (Bonferroni 0.040); the 30-50 km/h class sits between its unadjusted 0.034 and Holm's 0.136 and should be described as suggestive unless the joint-permutation p-value falls below 0.05. Widening the control pool (trade-off in roth2023 pp. 18-19) is the main lever for both resolution and power.
