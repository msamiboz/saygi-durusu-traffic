# Reading notes 04: inference in difference-in-differences with few treated units

Papers: conley2011, ferman2019, hagemann2019, mackinnon2017, mackinnon2018, mackinnon2020, alvarez2023.

Page numbers `(p. N)` are PDF pages as marked in `literature/txt/<key>.txt`. They are NOT journal pages.
Three things to know before citing anything from this file:

1. **The files on disk are not always the published versions.**
   - `conley2011.pdf` is the NBER Technical Working Paper 312 (2005), not the REStat 2011 article. In it, N0 = number of TREATED groups and N1 = number of CONTROL groups (the reverse of Ferman-Pinto and of most later papers). Sections that later papers attribute to "Conley and Taber (2011)" (the Gamma* procedure, Section III.A on heterogeneous effects, an appendix on heteroskedasticity and spatial correlation) are not in this file. I could not check them.
   - `ferman2019.pdf` is MPRA Paper 67665 (November 2015), not the REStat 2019 article. Numbers and wording may differ in print.
   - `hagemann2019.pdf` is arXiv:1803.02764v1; `mackinnon2017/2018/2020` are early-view / accepted / in-press versions; `alvarez2023.pdf` is arXiv v1.
2. **alvarez2023 is not a paper about spatial correlation.** It assumes independent units (Assumption 1, p. 4). The spatial-correlation paper is Ferman (2020), "Inference in differences-in-differences with few treated units and spatial correlation", which alvarez2023 only cites (p. 12). It is not in our library. None of the seven papers here handles dependence between the units of inference.
3. **hagemann2019 does not cover a single treated cluster.** Its adjusted test needs at least 2 treated and 2 control clusters (the variance formula divides by q1 - 1, p. 7), and at least 3 + 3 for any power at the 5% level (p. 9). The one-treated-cluster case is a different paper (Hagemann 2020, "Inference with a single treated cluster", cited in alvarez2023 p. 12; not in our library).

Our design in the vocabulary of this literature (my mapping, used throughout):
- "group" or "cluster" j = a calendar date; "individual" i = a geohash cell; the within-day contrast c = ln v(09h) - mean(ln v(08h), ln v(10h)) plays the role of the post-minus-pre difference W_j.
- Treated groups: 5 (Nov 10 in each of 2020-2024). Control groups: k same-weekday dates per year (k = 3 now; being widened).
- Date-level statistic: W_d = mean of c over the M_d cells observed on date d (M_d = 400-2300). Yearly DiD: D_y = W_{Nov10,y} - mean of control W_{d,y}. Estimate D = mean of D_y.
- Our test recomputes D under every assignment of one "treated" date per year (4^5 = 1024). In MacKinnon-Webb's terms this is a coefficient-based randomization test (RI-beta), stratified by year, with one treated cluster per stratum.

---

### conley2011 - Conley and Taber (2005 NBER TWP 312; published 2011), inference in DiD with a small number of policy changes

- **Question and setting.** How to do inference on a DiD coefficient when only a few groups change policy (possibly one) while many groups never change (p. 2-3). The usual asymptotics assume both numbers are large.

- **Data and method.**
  - Model at group x time level: Y_jt = alpha d_jt + X_jt' beta + theta_j + gamma_t + eta_jt, where eta_jt is a group x time shock (eq. 4, p. 8). With individual data, an individual error eps_i is added (eq. 1, p. 5; eq. 6, p. 11).
  - Asymptotic frame: number of treated groups and T fixed, number of controls goes to infinity (p. 9).
  - Assumption 1.1 (p. 8): the vector (eta_j1, ..., eta_jT) is i.i.d. across groups, independent of the treatment path d_j and of X, with bounded density and support. Correlation over time within a group is unrestricted (p. 8).
  - Proposition 1.1 (p. 10): beta-hat is consistent, but
    alpha-hat - alpha  ->p  sum_{treated j} sum_t (d_jt - dbar_j)(eta_jt - etabar_j) / sum_{treated j} sum_t (d_jt - dbar_j)^2.
    So the error of alpha-hat is a fixed linear combination of the TREATED groups' shocks. It does not vanish.
  - Procedure (p. 10-11): the same linear combination is computed from each control group's residuals. Its empirical distribution Gamma-hat(a) estimates the distribution of (alpha-hat - alpha). For one treated group:
    Gamma-hat(a) = (1/N_controls) sum_{c in controls} 1{ sum_t (d_1t - dbar_1) resid_ct / sum_t (d_1t - dbar_1)^2 < a }.
    Reject H0: alpha = alpha0 if alpha-hat falls outside the 2.5%-97.5% range of Gamma-hat shifted by alpha0; the confidence interval is obtained by test inversion (p. 11). Proposition 1.2: Gamma-hat converges uniformly to the true distribution as controls grow (p. 11).
  - Model 2 (p. 11-16): individual data with FIXED cell sizes |M(j,t)|. The cell sizes are assumed i.i.d. across control groups, and the treated groups' cell sizes may come from a different distribution (Assumption 2.5, p. 13). Because small cells are noisier, the authors do not reuse raw control residuals; they separately estimate the distributions of the group-time shock and of the individual error by deconvolution (Kotlarski result, sieve mixture estimator; p. 14-16) and then simulate the distribution of alpha-hat for the treated groups' own cell sizes.
  - Application (p. 16-17): effect of merit-aid programmes (Georgia HOPE; then all 10 adopting states) on college enrolment of 18-19 year olds, October CPS 1989-2000; 41 control units for HOPE (34,902 individuals), 51 units for all programmes (42,161).

- **Main findings.**
  - With a fixed number of treated groups, the DiD estimator is unbiased but not consistent, because the treated groups' shocks eta do not average out, however many individuals or control groups there are (p. 6-7; p. 10). In the authors' words, "point estimators of treatment effects should not be thought of as being consistent" (p. 2).
  - If the shocks are truly normal, standard methods with a degrees-of-freedom correction are fine; otherwise standard errors "may be very misleading" (p. 7).
  - HOPE alone (Table 1, p. 47): estimate 0.072. 95% CI clustered by state x year (0.025, 0.119); clustered by state (0.050, 0.094); Conley-Taber (-0.006, 0.212). The effect becomes marginally insignificant (p. 20-21). The estimated null distribution is clearly non-normal (Figure 1, p. 50; p. 20).
  - All 10 programmes (Table 2, p. 48): population-weighted estimate 0.034; cluster-by-state CI (0.008, 0.059); Conley-Taber (0.001, 0.095). The interval changes less with 10 treated states than with 1 (p. 21).
  - Cell sizes range from 15 (New Hampshire 1992) to 383 (California 1991), so the authors themselves warn that the effect's variance is larger for small states, "invalidating the previous exercise", and they redo the analysis with Model 2 (p. 21-22). Model 2 intervals (Table 3, p. 49): HOPE, change in attendance probability [-0.041, 0.222]; all programmes [-0.004, 0.092] at 95% and [0.008, 0.086] at 90%. A one-sided 5% test rejects for all programmes (p. 23).
  - Validation by placebo (p. 23; Figure 2, p. 51): each of the 41 control states is treated in turn as if it were Georgia. The 41 placebo p-values are spread over [0, 1], as they should be.

- **Usable for our paper.**
  - Method / Introduction: the core reason our effective sample is dates, not cells. A date-level shock (weather, an accident, a school event) hits all cells of that date and is not reduced by having 400 or 2300 cells (p. 6-7, p. 10). Cite for "more cells do not buy consistency; only more dates do".
  - Method: the idea of taking the null distribution from untreated units (p. 10-11) is the model-based counterpart of our placebo-date distribution. The paper itself links this to earlier "placebo law" exercises of Bertrand, Duflo and Mullainathan and to the Anderson-Meyer comparison of one state's change with the distribution of other states' changes (p. 4).
  - Method: explicit analogy to end-of-sample structural-break tests (Andrews 2003; Dufour, Ghysels and Hall 1994), where the null distribution of a statistic for a short final stretch is learned from the long earlier stretch of TIME (p. 5). This is the closest precedent in the paper for using dates as the units.
  - Method: a one-sided test is used and defended as "most interesting" when the direction is known (p. 23).
  - Robustness: the placebo-in-space calibration of Figure 2 (p. 23, p. 51) is a template for our "treat every control date as Nov 10" check.
  - Results-Discussion: for one treated state the interval is "about 3" times wider than the cluster-robust one by the authors' description (p. 20); from Table 1 (p. 47) the width is 0.218 against 0.094 (state x year clustering) or 0.044 (state clustering). Useful when explaining why our p-values are modest despite hundreds of thousands of cell-hours.

- **Caveats.**
  - Validity is asymptotic in the number of CONTROLS. With 3 control dates per year the Conley-Taber approximation does not apply; what justifies our 1024-assignment test is finite-sample exchangeability, not this paper. With the widened pool (about 50 same-weekday dates per year) the argument becomes relevant.
  - The key assumption is i.i.d. shocks across groups and independence between shocks and treatment (p. 8). For us: date-level contrasts must be i.i.d. across dates within a year and unrelated to "being Nov 10". A seasonal trend in the contrast, or serial correlation between adjacent weeks, violates this. The paper gives no remedy.
  - "Arbitrary correlation over time within a group" (p. 8) maps to arbitrary correlation across hours within a date. It does not license correlation across dates.
  - The working paper has no treatment of spatial correlation, and nothing on dependence across groups.
  - Earlier notes say the method "assum[es] the errors are identically distributed across units". Confirmed (p. 8), and note it is stronger than that: i.i.d. and independent of treatment.

- **Checks it suggests for us.**
  1. Placebo calibration (p. 23): for every control date in the widened pool, run the full procedure with that date as "treated" and the other dates as controls; plot the placebo p-values. They should be uniform.
  2. Plot the empirical distribution of control-date contrasts W_d (after removing year means). Report skewness and tails; this is our Figure-1 analogue and shows why normal critical values are not used (p. 20, p. 50).
  3. Report cell counts M_d for Nov 10 and each control date. Conley and Taber treat unequal cell sizes as a threat serious enough to change method (p. 21-22).
  4. Invert the test to get a confidence interval for D (p. 11): subtract a hypothesised effect delta0 from the Nov 10 contrast in each year and find the set of delta0 not rejected.

---

### ferman2019 - Ferman and Pinto (2015 MPRA version; published 2019), few treated groups and heteroskedasticity

- **Question and setting.** Methods built for few treated groups (Conley-Taber, Donald-Lang, residual bootstrap) take the treated group's error variance from the controls. What happens when group x time averages are built from different numbers of observations, so that the treated group's error variance differs from the controls'? (p. 2, p. 4-5)

- **Data and method.**
  - Individual model Y_ijt = alpha d_jt + theta_j + gamma_t + nu_jt + eps_ijt (eq. 6, p. 9). Aggregating, eta_jt = nu_jt + (1/M(j,t)) sum_i eps_ijt (eq. 8, p. 10).
  - For W_j = post-minus-pre average of eta_jt, with M_j constant over time: var(W_j) = A + B / M_j, for constants A (group-time shock part) and B (individual part), whatever the serial correlation of nu (p. 10).
  - If A > 0 and M -> infinity, var(W_j) -> A for all j and the problem disappears. If A = 0, the RATIO var(W_j)/var(W_j') stays at M_j'/M_j however large M is, so the aggregate model stays heteroskedastic (p. 10-11).
  - Correction (p. 11-12). Assume (eta_j1, ..., eta_jT) independent across j and identically distributed up to a variance parameter, and var(W_j) = G(M_j) = A + B/M_j. (i) Regress squared control residuals W-hat_j^2 on a constant and 1/M_j to get G-hat. (ii) Rescale each control residual: W-tilde_j = W-hat_j * sqrt( G-hat(M_1) / G-hat(M_j) ). (iii) Apply Conley-Taber with the rescaled residuals. Only group x time data plus the counts M are needed (p. 12).
  - Small number of controls: residual bootstrap of the studentised statistic s = alpha-hat / sqrt(var-hat(alpha-hat)), with var(alpha-hat) = G(M_1) + (1/N0^2) sum_controls G(M_j) (eq. 10, p. 12-13).
  - Monte Carlo (p. 15-16): one treated group, T = 2; total groups 50, 100, 400 (25 in the bootstrap table); intra-group correlation rho = 0.01%, 1%, 4%; M drawn uniformly from [50, 200], [200, 800] or [50, 950]; 40,000 replications; 10% tests.
  - Placebo simulations on real data (p. 20-21): American Community Survey 2005-2013, women 25-50, placebo "interventions" on one PUMA (5,188 regressions; mean cell 730, 10th-90th percentile 171-1,337) or one state (408 regressions; mean cell 10,138, 10th-90th percentile 1,250-21,099; Table 6, p. 32).

- **Main findings.**
  - Cluster-robust SEs cannot work with one treated group: the treated group's variance component is estimated as exactly zero (p. 3, p. 8).
  - Conley-Taber has the right AVERAGE rejection rate but the wrong conditional one. With 400 groups, M in [50, 200], rho = 0.01%: rejection (10% test) is about 22% when the treated group is in the smallest size quintile and about 4% in the largest (p. 16). Above-minus-below-median difference: -0.111 (Table 1, p. 27). Donald-Lang behaves the same way (p. 16-17).
  - The distortion shrinks as intra-group correlation rises: with rho = 4% the quintile rates are 11.8% vs 8.5% (p. 17), difference -0.022 (Table 1, p. 27).
  - Larger M helps only if rho is not tiny. M in [200, 800]: difference -0.004 at rho = 4%, -0.021 at rho = 1%, but still -0.107 at rho = 0.01% (Table 1, p. 27; p. 17-18).
  - More dispersion in M makes it worse: M in [50, 950], rho = 0.01%: -0.159 (Table 1, p. 27).
  - Real data: with states (mean cell above 10,000), Conley-Taber rejects 21% of the time when the placebo state is below median size and 2% when above (employment outcome; p. 22; Table 7, p. 33: difference -0.192). A large number of observations per group is therefore not a defence by itself (p. 5, p. 21-22).
  - Few controls: Conley-Taber also over-rejects on average, about 11% with 100 groups and 12.5% with 50 (10% test), even when all its assumptions hold (p. 18 and footnote 14). The corrected method without refinement inherits this (12-13% at 50 groups, Table 3, p. 29).
  - The corrected method removes the size dependence (differences within +/-0.005 at 400 groups, Table 1, p. 27). The bootstrap refinement brings average rejection to 11.1% at 25 groups, 10.7% at 50, 10.6% at 100, against 14.1%, 12.2%, 11.4% without refinement (p. 19; Table 4, p. 30). On ACS states: mean rejection 0.103, difference -0.016 (Table 7, p. 33).
  - The MacKinnon-Webb t-statistic permutation test "collapses" to Conley-Taber when there is one treated group, because the cluster-robust variance of the treated group is zero (p. 4, p. 13).
  - Synthetic control: the Abadie et al. post/pre RMSPE-ratio test corrects for this heteroskedasticity only if at least one pre-period is left out of the weight estimation (p. 14-15, p. 20; Table 5, p. 31).

- **Usable for our paper.**
  - Method: the decomposition var(W_d) = A + B/M_d (p. 10) is exactly our date-level variance: A = city-wide date x hour shock, B/M_d = averaging noise over the M_d cells of that date. Cite to define what "heteroskedastic dates" means.
  - Method: direction of the bias (p. 10, p. 16). If the treated date's mean rests on FEWER cells (or noisier cells) than the placebo dates, a placebo test over-rejects; if on more, it under-rejects.
  - Robustness: justification for a balanced cell panel within each year (same cells on Nov 10 and on every control date), which makes M_d equal by construction; and for reporting M_d by date.
  - Robustness: the regression of squared placebo deviations on 1/M (p. 12) as a diagnostic and, in the widened pool, as a correction.
  - Results-Discussion: "many observations per group does not make group averages homoskedastic" (p. 5, p. 21-22), to pre-empt the reaction that 400-2300 cells per date is plenty.

- **Caveats.**
  - The concern is about the treated GROUP (date) differing from control groups in M. It is not about geohash cells differing among themselves. `notes/rituals_big_data.md` says "Geohash cells differ in observation counts, so the heteroskedasticity concern applies directly"; that overstates it. What matters is whether Nov 10 has a different cell count, vehicle count or noise level than the control dates OF THE SAME YEAR, because our permutation is within year.
  - `review.md` links the 400 vs 2300 range across YEARS to this problem. Differences across years do not break a within-year permutation test. They affect how much each year contributes to D and to its permutation distribution (power and weighting), not size.
  - Which regime are we in? The paper's results depend on rho, the share of cell-level variance that is common to the date. With rho of a few percent and M in the hundreds, the distortion is negligible (p. 17-18); with rho near zero it never vanishes. We do not know our rho. City-wide shocks suggest it is not tiny, but this must be estimated, not assumed.
  - The variance model assumes the individual errors are uncorrelated within the group ("for ease of exposition", p. 9). Our cells are spatially correlated, so the averaging term falls more slowly than B/M (roughly B/M_eff with M_eff < M; my inference, not in the paper). The functional form in 1/M may then fit poorly. alvarez2023 (p. 9) states that the published Ferman-Pinto shows the A + B/M form holds under a wide range of within-unit spatial and serial correlation; I could not verify that in the MPRA version on disk.
  - The correction needs many controls to estimate G(M). With 15 control dates it is not feasible; with the widened pool it is.
  - The reported 11-12.5% over-rejection with 50-100 groups concerns residual-based Conley-Taber, where controls' residuals stand in for the treated unit's error. Our test recomputes the full statistic for every assignment and includes the actual assignment in the reference set, which is the construction MacKinnon and Webb find exactly sized with homogeneous clusters (mackinnon2020 p. 8, p. 10). The paper does not analyse that construction.

- **Checks it suggests for us.**
  1. Table of M_d (cells) and total NUMBER_OF_VEHICLES at 08h, 09h, 10h for Nov 10 and each control date, by year and speed class. Flag any year where Nov 10 is outside the range of its controls.
  2. Estimate rho: one-way variance decomposition of cell contrasts c into a date component and a cell-within-date component, within year and speed class. Compare with the paper's 0.01% / 1% / 4% grid.
  3. In the widened pool: regress (W_d - year mean)^2 on a constant and 1/M_d. If the slope B is material relative to A, apply the rescaling sqrt(G-hat(M_Nov10)/G-hat(M_d)) to placebo deviations and recompute the p-value (p. 12).
  4. Balanced-panel version of the main estimate (cells present at 08h, 09h, 10h on all dates of the year), so that M is identical across dates.
  5. Placebo rejection rate by size, as in their Table 7: among placebo dates, compare rejection rates for dates with below- and above-median M.

---

### hagemann2019 - Hagemann (2019), placebo inference with a small number of large clusters

- **Question and setting.** A Fisher-style permutation ("placebo") test for the absence of a cluster-level binary treatment effect when there are very few clusters, each large, and the effect is identified only between clusters (p. 1-2). Clusters may be "counties, regions, schools, firms, or stretches of time" (p. 4).

- **Data and method.**
  - Each cluster k yields its own estimate theta-hat_k, computed from that cluster's data only. Treated clusters estimate theta1 = theta0 + beta, untreated ones theta0 (p. 4-5). In the DiD example theta-hat_k is the cluster's own post-minus-pre coefficient (Example 2.4, p. 6).
  - Statistic: difference of means, T = mean of theta-hat over the q1 treated clusters minus mean over the q0 untreated (eq. 2.3, p. 6).
  - Two-sample variance function (p. 7): S^2(x) = [1/(q1(q1-1))] sum_treated (x_k - xbar_treated)^2 + [1/(q0(q0-1))] sum_untreated (x_k - xbar_untreated)^2.
  - Adjusted placebo statistic for a relabelling pi (eq. 2.4, p. 7): T(pi) = Tbar(pi) * S(original) / S(pi).
  - Algorithm 2.5 (p. 8): compute T; compute T(pi) for all C(q, q1) choices of placebo-treated clusters; reject beta = 0 against beta > 0 if T exceeds the 1 - alpha quantile. p-value = share of pi with T(pi) >= T (eq. 2.5, p. 8). If q1 = q0 the adjustment factor can be dropped (Remark i, p. 8). Left-sided and two-sided versions in Remark iii (p. 8).
  - Assumption 3.1 (p. 10): nu_n (theta-hat_k - theta) = Z_k + R_k with nu_n -> infinity; min(q1, q0) -> infinity (slowly) and q1/q -> lambda in (0, 1); Z_k mean zero, independent ACROSS clusters, uniformly bounded p-th moment for some p > 2, average variance bounded away from zero; remainders small. Variances may differ across clusters and need not be estimated (p. 10-11).
  - Within-cluster dependence is allowed if short-range: clusters are modelled as stationary random fields in time (d = 1) or space with summable dependence ("p-stability", p. 14). The condition fails if, for example, series contain unit roots (p. 11). For least squares the condition on the number of clusters is sqrt(q)/min cluster size -> 0 (p. 16).
  - Theorem 3.3 (p. 11): under Assumption 3.1 the adjusted test has asymptotic size alpha and power 1. Corollary 3.4 (p. 12): with q1/q -> 1/2 the unadjusted test is valid.
  - Fixed number of clusters (p. 12-13): (a) with independent normal limits of arbitrary variances, numerical worst-case size at nominal 5% is about 0.077 for q1 = q0 = 5 and at most 0.065 for q1 = q0 = 7, reached with near-zero and near-infinite variances; imbalance makes it worse. (b) Theorem 3.6: if the limits Z_k are i.i.d. and continuous, the unadjusted test is asymptotically conservative (lim sup size <= alpha).
  - Monte Carlo (p. 18-24): clusters of 15-25 observations with h-dependence (h = 10) and different error variances in treated and control clusters; probit design; CPS placebo DiD (1989-1991, 86,006 observations, about 573 women per state-year, p. 23). Application: Dal Bo and Frechette lab sessions, 3 treated vs 3 control sessions per comparison, 37,042 games (p. 24-25).

- **Main findings.**
  - If the cluster estimates were permutation-invariant under the null, the (randomised) permutation test would be exact in finite samples (Remark v, p. 9). The contribution is asymptotic validity when they are NOT invariant because variances differ.
  - Number of permutations bounds power: the test cannot reject if C(q, q1) < 1/alpha. At alpha = 0.05 one needs at least 3 treated and 3 untreated clusters (C(6,3) = 20) (Remark vi, p. 9).
  - Simulated size at nominal 5% (p. 21): q1 = q0 = 3: placebo 5.35%, Ibragimov-Mueller 2.2%, wild cluster bootstrap 8.55%, cluster-robust t 16.05%. q1 = 2, q0 = 6: placebo 1.65% (conservative). q1 = 6, q0 = 2: placebo 5.30%, wild bootstrap 9.05%. q1 = q0 = 6: all similar; t test 9.50%.
  - Size of the placebo test is insensitive to the strength of within-cluster dependence; the t test and wild bootstrap deteriorate with it (p. 21).
  - CPS placebo DiD: the placebo test is essentially exact and more powerful than the alternatives at 3 + 3 clusters (p. 24).
  - Application: all seven comparisons keep their sign and lose one significance level relative to cluster-robust probit (Table 1, p. 25).

- **Usable for our paper.**
  - Literature / Method: a formal statement that assigning placebo treatments to untreated clusters yields a valid test, with clusters allowed to be periods of time (p. 2, p. 4).
  - Method: exactness under permutation invariance (p. 9) is the property our within-year test relies on.
  - Method: the "at least 1/alpha permutations" rule (p. 9). For us: one year with 4 dates has only 4 assignments, so no single-year test is possible at 5%; pooling 5 years gives 1024.
  - Method: the test is developed one-sided (p. 8), matching our one-sided alternative.
  - Robustness: when clusters have different variances and the design is unbalanced, a permutation test on the raw difference of means is not valid in general and must be studentised with a variance recomputed under each relabelling (p. 7, Theorem 3.3 p. 11). This is the rationale for a studentised version of our statistic.
  - Results-Discussion: worst-case numbers for a fixed small number of heterogeneous clusters (0.077 at 5 + 5, p. 12-13) give a sense of how wrong a nominal 5% could be.

- **Caveats.**
  - The asymptotics require each cluster's estimate to converge to a COMMON theta0 as the cluster grows (nu_n -> infinity, Assumption 3.1, p. 10). A date-level common shock that hits all cells does not average out within the date, so this assumption fails for us in exactly the way the unit-root example fails (p. 11). In our setting the date shock is the main source of noise (the Conley-Taber view). So Theorem 3.3 cannot be invoked for our design; only the exactness-under-invariance remark (p. 9) applies. `review.md` calls this paper the "formal justification for treating placebo dates as placebo clusters"; that is too strong.
  - One treated cluster per year: not covered. The adjusted statistic is undefined for q1 = 1.
  - Stratification by year: not covered. The paper has a single pool of clusters with a common theta0. If we pooled 5 treated and 15 control dates into one Hagemann test (C(20,5) = 15,504 relabellings), year-specific levels of the contrast would have to be removed first, which makes the date estimates dependent within year; the paper does not treat this.
  - Independence across clusters is required (p. 10). For dates one week apart this is plausible but untested.
  - Our design is unbalanced (1 treated to k controls). Corollary 3.4 does not apply, and the paper's own simulations show the test turning conservative at 2 + 6 (1.65%, p. 21).

- **Checks it suggests for us.**
  1. A studentised pooled statistic recomputed under each of the 1024 assignments: t(a) = mean_y D_y(a) / [sd_y(D_y(a)) / sqrt(5)]. Report its permutation p-value next to the unstudentised one. (My adaptation of the adjustment on p. 7 to our stratified design; with 5 years the denominator is noisy, so expect lower power.)
  2. Report the number of distinct assignments and the smallest attainable p-value for every specification (main: 1/1024; leave-one-year-out: 1/256; single year: 1/4).
  3. Test independence across dates in the widened pool: lag-1 (one week) autocorrelation of the date-level contrast within year.
  4. Variance heterogeneity across dates within a year: with the widened pool, compare the dispersion of W_d in November with other months.

---

### mackinnon2017 - MacKinnon and Webb (2017, online 2016), wild bootstrap inference for wildly different cluster sizes

- **Question and setting.** How reliable are cluster-robust t tests and the wild cluster bootstrap when cluster sizes are very unequal, and when only a few clusters are treated? (p. 1-2)

- **Data and method.**
  - Cluster-robust variance estimator (CRVE) with t(G-1) critical values; t(G*-1) with the Carter-Schnepel-Steigerwald "effective number of clusters" G*; restricted (null-imposed) and unrestricted wild cluster bootstrap with Rademacher weights (p. 3-4).
  - Monte Carlo with continuous regressors: 2,000 observations, 50 or 100 clusters, equal-sized or proportional to US state populations (4 to 242 observations), 400,000 replications (p. 5-7).
  - Monte Carlo for DiD: 50 clusters, G1 treated clusters from 1 to 49, intra-cluster correlation 0.05 (p. 7-8).
  - Analytical explanation in a pure treatment model (Section 6, p. 10-15).
  - "Placebo laws" on CPS earnings of women 25-50, 1979-1999: 547,518 observations, 51 states, G1 from 1 to 51; micro data and state-year aggregates (p. 15-18).
  - Example: Angrist and Kugler (2008), 32 and 38 Colombian departments (p. 19-20).

- **Main findings.**
  - The "rule of 42" fails with unbalanced clusters: 50 state-sized clusters give CRVE rejection rates (nominal 5%) from 0.057 to 0.107 (Table II, p. 6-7). The wild cluster bootstrap stays within 0.0497-0.0528 (p. 7).
  - With few treated clusters every method fails: "all the methods fail badly when the number of treated clusters is small" (p. 2).
  - Why (p. 11-12): with G1 fixed, the coefficient is inconsistent; its noise is dominated by the treated clusters. With G1 = 1 the treated cluster's residuals sum to zero, so the CRVE term that should measure the treated cluster's variance is exactly zero.
  - Size of the failure: with 50 equal clusters and G1 = 1, the 0.975 quantile of the t statistic is 14.226 instead of 2.010, and the CRVE t test rejects 77.75% of the time at the 5% level (p. 13).
  - Restricted wild cluster bootstrap with G1 = 1: bootstrap t statistics are bimodal around +/- the actual t, so the test never rejects at conventional levels (p. 12-13). Unrestricted version: over-rejects severely, and more so as G grows (p. 14-15). The key quantity is G1, not the share treated (p. 14).
  - Rule of thumb for DiD with equal-sized clusters: wild cluster bootstrap probably safe for 7 <= G1 <= G - 7, seriously misleading for G1 < 4 or G1 > G - 4; more treated clusters needed if sizes vary or variances differ between treated and untreated (p. 15).
  - Placebo laws, micro data: heteroskedasticity-robust t tests always reject more than 50% of the time although the estimated intra-state correlation is only about 0.031 (p. 17). CRVE rejects 6.3-7% or more for larger G1 and severely for small G1 (p. 17).
  - State-year aggregates (balanced clusters): CRVE works for most G1 but still over-rejects severely for very small G1; the restricted wild cluster bootstrap "performs extremely well" for G1 >= 5 (p. 18). Aggregation can raise standard errors substantially (p. 19, p. 21).

- **Usable for our paper.**
  - Method: why we do not report cluster-robust (by date) or heteroskedasticity-robust standard errors as the main inference. A within-cluster correlation as small as 0.03 produced rejection rates above 50% for robust SEs (p. 17). Our cells within a date are far more correlated than that.
  - Method: the mechanical reason cluster-robust variance fails with one treated cluster (residuals of the treated cluster sum to zero, p. 12). In a single year we have one treated date, so a date-clustered SE for that year's DiD is degenerate.
  - Method: the wild cluster bootstrap is not a way out with one treated date per year (p. 12-15).
  - Robustness: as a contrast only, we can report the naive cell-level t statistic and say, citing p. 13 and p. 17, by how much such statistics over-reject in comparable designs.

- **Caveats.**
  - The paper is about regression t tests and the wild bootstrap. It does not study randomization or placebo inference; it only points to Conley-Taber and to MacKinnon-Webb (2016/2020) for few treated groups (p. 9).
  - `review.md` uses it to motivate a leave-one-year-out check "on influential clusters". The paper does not discuss influence or leave-one-out analysis. Its point is size distortion from unequal cluster sizes and few treated clusters. Leave-one-year-out is a sensible check but should not be attributed to this paper.
  - The G1 >= 5 result for aggregates (p. 18) comes from 51 states x 21 years. Our pooled date-level data would have 5 treated and 15 control dates with ONE observation per date, where a "cluster-robust" variance is just a heteroskedasticity-robust one. The result does not transfer.

- **Checks it suggests for us.**
  1. One table row labelled "naive": cell-level OLS DiD with heteroskedasticity-robust and date-clustered SEs, shown only to document the gap to the randomization p-value.
  2. If a regression-based p-value is wanted for the pooled design (G1 = 5 of G = 20 dates), note that 5 is below the "probably safe" threshold of 7 (p. 15) and treat any wild-bootstrap p-value as unreliable.

---

### mackinnon2018 - MacKinnon and Webb (2018), the wild bootstrap for few (treated) clusters

- **Question and setting.** Can a wild bootstrap that resamples at a FINER level than the clustering (down to single observations) rescue inference when few clusters are treated? (p. 1-2)

- **Data and method.**
  - Pure treatment model y_ig = beta1 + beta2 d_g + eps_ig; CRVE t statistic (p. 2-3).
  - "Subcluster wild bootstrap": the test statistic still uses the cluster-robust SE, but bootstrap signs are drawn per subcluster or per observation ("ordinary wild bootstrap"), restricted (WR) or unrestricted (WU) (p. 7).
  - Conditions for the ordinary wild bootstrap to match the variance of the actual t statistic with G fixed (p. 9): (1) equal cluster sizes; (2) cluster covariance matrices equal up to a scalar, Omega_g = lambda_g * Omega-bar; (3) small average intra-cluster correlation when G1 is small.
  - Simulations with G = 14 clusters of 200 observations, rho from 0 to 0.20 (Figures 1-2, p. 6, p. 12), varying cluster sizes (Figure 3, p. 14); example with 8 schools and 255 students from Angrist and Lavy (p. 17-19). Most simulation detail is in an online appendix that is not in our file.

- **Main findings.**
  - Restates why CRVE and the wild cluster bootstrap fail with few treated clusters (p. 3-6). At G = 14, G1 = 1, the restricted wild cluster bootstrap almost never rejects and the unrestricted one over-rejects very severely (p. 6).
  - The ordinary wild bootstrap with a cluster-robust t statistic works "extraordinarily well" except when G1 = 1 (or G - 1) and rho > 0.02, or G1 = 2 and rho = 0.20 (p. 12).
  - When condition (3) fails with G1 = 1, the restricted version under-rejects and the unrestricted over-rejects, like the cluster versions (p. 11). Practical diagnostic: trust the result only when WR and WU p-values are close (p. 11, p. 20).
  - Unequal sizes: under-rejection when treated clusters are smaller than untreated ones, over-rejection when larger (p. 13). "The key requirement is that all cluster sizes, regardless of treatment, should be similar" (p. 1).
  - Averaging to a balanced panel does not help if the original sample is unbalanced, because averages over different numbers of observations have different covariance structures (p. 14).
  - The argument does not carry over to DiD regressions, where only part of each treated cluster is treated; under-rejection is the likely outcome (p. 14-15, p. 20).
  - The authors set randomization inference aside because it "fails when cluster sizes vary" or with heteroskedasticity of unknown form, and cannot be used with very few clusters (p. 2).
  - Example: with 2 effective treated schools the CRVE p-value is 0.003; after dropping one treated school, restricted and unrestricted bootstrap p-values diverge sharply, which exposes the fragility (p. 17-19).

- **Usable for our paper.**
  - Method: a second reason not to replace the randomization test with a bootstrap over cells. The ordinary wild bootstrap is valid with one treated cluster only if within-cluster correlation is very small (rho of about 0.02 or less at G = 14; p. 11-12). Our cells share date-wide shocks and spatial correlation, so the condition fails.
  - Robustness: the "restricted vs unrestricted p-values should agree" diagnostic (p. 11, p. 20), if a referee asks for a bootstrap.
  - Results-Discussion: the statement that aggregation to group x period means does not remove heteroskedasticity when the underlying counts differ (p. 14) supports reporting M_d and using a balanced panel; it agrees with Ferman-Pinto.

- **Caveats.**
  - Our contrast c is itself a within-date difference (09h against 08h and 10h), so in regression form our design is a DiD, the case for which the authors say their main result does not apply (p. 14-15).
  - The paper's dismissal of randomization inference (p. 2) is about conditional size with heterogeneous clusters, the topic of mackinnon2020; it is a one-paragraph remark, not an analysis.
  - Earlier notes summarise the paper as "do not substitute a wild bootstrap over cells or days for the RI". Correct as a conclusion for us, but the paper's own message is more positive: the observation-level wild bootstrap often works with 2 or more treated clusters of similar size (p. 2, p. 12).

- **Checks it suggests for us.**
  1. Optional appendix item: cell-level restricted and unrestricted wild bootstrap p-values with date-clustered SEs. A large gap between them (expected) documents that the bootstrap is uninformative here (p. 11).
  2. Estimate the within-date correlation of cell contrasts (same quantity as rho in the Ferman-Pinto check) and compare with the 0.02 threshold on p. 12.

---

### mackinnon2020 - MacKinnon and Webb (2020), randomization inference for DiD with few treated clusters

- **Question and setting.** Two randomization-inference procedures for DiD with very few treated clusters and a reasonable number of controls: one based on the coefficient (RI-beta) and one based on the cluster-robust t statistic (RI-t). When does each fail? (p. 1-2). Intended scale: viable for G1 = 2 and G0 = 21, not for G1 = 3 and G0 = 3 (p. 2).

- **Data and method.**
  - RI-beta (p. 5): estimate beta; re-assign treatment to every other set of G1 clusters (all C(G, G1) - 1 of them, or a random subset), re-estimate each time; compare beta-hat with the placebo betas. Close to Conley-Taber's procedure but uses re-estimated coefficients, not control residuals (p. 5).
  - p-values (p. 5): p* = (1/S) sum_r 1{|beta*_r| > |beta-hat|} over the S re-randomizations excluding the actual one; alternative p*' = (S p* + 1)/(S + 1), which counts the actual sample and is never less conservative. Exact size needs alpha (S + 1) to be an integer (footnote 5, p. 6). One-tailed versions are allowed (p. 5).
  - RI-t (p. 11): same, with the cluster-robust t statistic recomputed in every re-randomization. Motivation: in the two-sample (Behrens-Fisher) problem, permuting a difference of means is invalid unless sample sizes or variances are equal, whereas permuting a t statistic is asymptotically valid (Romano 1990) (p. 11).
  - Three assumptions behind RI (p. 6): random assignment; homogeneous groups; and whether the analyst knows which groups were treated (conditional vs unconditional inference). Re-randomization should respect everything known about how treatment was assigned (p. 5).
  - Monte Carlo (p. 7): DiD with 20 "years", treatment starting between years 6 and 16, random-effects errors with intra-cluster correlation rho (mostly 0.05); N = 4,000 in G = 40 clusters with sizes from 32 to 246 (gamma = 2), or N = 5,000 in G = 20 with a largest/smallest ratio up to about 47 (gamma = 4: 20 to 935); 100,000-400,000 replications; 5% tests.
  - Example (p. 13-15): Bailey (2010), early repeal of pill sales bans in 2 of 47 states; S = 1,080.

- **Main findings.**
  - Cluster-robust t tests can reject more than 80% of the time at the 5% level with one treated cluster; the standard error is often too small by a factor of five or more (p. 3-4).
  - RI-beta is exactly sized UNCONDITIONALLY (treated clusters drawn at random from all clusters) and when clusters are homogeneous (gamma = 0) (p. 8-10).
  - RI-beta, conditional on which clusters are treated: over-rejects when the treated clusters are smaller than typical and under-rejects when they are larger, because beta-hat then comes from a more (less) dispersed distribution than the placebo betas (Figures 1-2, p. 7-9). The distortion barely changes as G1 goes from 1 to 8 (p. 9), and can be somewhat worse for G1 = 2 than for G1 = 1 (p. 10). It grows with size dispersion (p. 10) and shrinks as intra-cluster correlation or observations per cluster increase (Figure 5, p. 10-11): the standard deviation of beta-hat lies between O(N1^(-1/2)) with no intra-cluster correlation and O(1) with a large correlated treated cluster (p. 11).
  - Even so, for G1 <= 2 RI-beta "works very much better" than CRVE or either wild cluster bootstrap; for G1 >= 4 the restricted wild cluster bootstrap is typically better (p. 9).
  - RI-t with G1 = 1 and unequal sizes: no better than RI-beta in kind. The conditional distributions of the t statistic differ as much as those of beta-hat (Figure 6a, p. 12), and rejection rates are U-shaped in the size rank of the treated cluster: over-rejection for very small or very large treated clusters, under-rejection in between (Figure 8a, p. 12). Reason: with one treated cluster the CRVE is badly behaved, so dividing by it does not standardise (p. 11-12).
  - RI-t with G1 >= 2: much better than RI-beta under the null; it mostly UNDER-rejects (conservative), sometimes noticeably (Figures 7-8, p. 12-13). It is asymptotically valid only when G1 and G grow together (p. 11), and G "may have to be quite large" (p. 15).
  - Power: RI-beta has substantially more power than RI-t and than the restricted wild cluster bootstrap, even with 80 clusters (Figure 9, p. 13-14).
  - Both procedures work well with approximately homogeneous clusters even when G1 is extremely small (second conclusion, p. 15). Neither works well with one atypical treated cluster (first conclusion, p. 15).
  - Aggregating to cluster x period cells weakens but does not remove the homogeneity requirement: differences in observations per cell, in regressors, or in error variances can still invalidate RI (p. 7; cites Ferman-Pinto).
  - Example (Table 1, p. 14-15): cluster-robust t = -5.43; restricted wild cluster bootstrap p = 0.546; RI-beta p = 0.063; RI-t p = 0.056. The first two are "wildly contradictory" and predictable in advance; the RI values are not.

- **Usable for our paper.**
  - Method: names and defines our procedure. Our test is RI-beta with one treated cluster per stratum; the p-value should be the p*' form that counts the actual assignment (p. 5). With 1024 assignments, p = 0.008 means roughly 8 of 1024 assignments (the actual one included) are at least as extreme.
  - Method: the three assumptions (p. 6) give the structure for our identification paragraph. Nov 10 was not randomly assigned. The paper is blunt: without random assignment "it is not appropriate to use randomization inference" (p. 6), and it treats random assignment as a maintained assumption in DiD (p. 6). So our test must be presented as a placebo/permutation test resting on within-year exchangeability of date-level contrasts, not as a design-based randomization test.
  - Method: "re-randomize only among units that share the known characteristics of the treated unit" (p. 5) supports restricting placebo dates to the same weekday and the same year, and excluding holidays.
  - Method / Robustness: conditional versus unconditional size (p. 6-9). We know exactly which date is treated and can observe its cell and vehicle counts, so the relevant question is conditional: is Nov 10 a typical date in M_d and in noise? Over-rejection if smaller/noisier, under-rejection if larger/quieter.
  - Robustness: the homogeneity requirement is the binding one. With homogeneous clusters RI-beta is exact for any G1 (p. 10, p. 15), which is the argument for a balanced cell panel and same-weekday, same-year controls.
  - Results-Discussion: RI-beta is the more powerful of the two (p. 13), which justifies keeping the coefficient-based test as the headline and the studentised one as a robustness row.

- **Caveats.**
  - Earlier notes (`notes/randomization_inference.md` line 39, `review.md` lines 112 and 250) say that studentised RI "is more robust" or "safer" and that this "applies directly". The paper supports this only for G1 >= 2. For ONE treated cluster with unequal sizes, RI-t is not reliable either (p. 12, p. 15). Within a year we have exactly one treated date. The paper's message for that case is: make clusters homogeneous, or accept that nothing works well.
  - The "studentisation" proposed in earlier notes (divide each year's DiD by the SD of that year's four date contrasts, a permutation-INVARIANT scale) is not RI-t. RI-t recomputes the variance in every re-randomization (p. 11). An invariant scale only reweights years; it does not address heterogeneity between the treated date and its controls. It is a legitimate precision-weighting, but should not be cited to this paper.
  - The simulated heterogeneity is in cluster SIZE with equicorrelated errors, and (Appendix C, not in our file) cluster-level heteroskedasticity. Nothing on serial dependence between clusters, on trends, or on stratified designs.
  - The 400 vs 2300 range across years is not the heterogeneity this paper warns about, as long as permutation stays within year. `review.md` line 112 conflates the two; the earlier note at `notes/randomization_inference.md` line 56 has it right.
  - Results are for G0 around 19-39 controls. Nothing is said about 3 controls per treated unit.

- **Checks it suggests for us.**
  1. Size-rank diagnostic: for each year, the rank of Nov 10 among its dates in M_d, in total vehicles, and in the cross-cell SD of c. If Nov 10 is consistently lowest (highest), expect over-(under-)rejection (p. 8-10).
  2. Empirical conditional-size check in the widened pool: among placebo dates, compute the placebo rejection rate separately for dates with low and high M_d (their Figures 2 and 4).
  3. Pooled RI-t analogue: across-year t statistic recomputed per assignment (same statistic as in the Hagemann check). Here the "treated clusters" number 5, the regime where the paper finds RI-t conservative (p. 12-13).
  4. Report both p* and p*' (p. 5), or simply p*'; note that 0.05 x 1024 is not an integer, so the attainable level just below 5% is 51/1024 = 0.0498.
  5. Keep the coefficient-based test as headline for power (p. 13); present the studentised version as a robustness row.

---

### alvarez2023 - Alvarez and Ferman (2023), extensions for inference in DiD with few treated clusters

- **Question and setting.** A short methodological note (16 pages, no simulations, no application). It extends Conley-Taber and Ferman-Pinto to (i) staggered adoption with heterogeneous treatment effects and (ii) uniform confidence bands for event-study plots, with few treated units and many controls (p. 1-2).

- **Data and method.**
  - Potential outcomes y_jt(0) = theta_j + gamma_t + eta_jt, y_jt(1) = alpha_jt + y_jt(0). Treatment effects alpha_jt and treatment assignment are FIXED; uncertainty comes only from the shocks eta (p. 3).
  - Assumption 1 (p. 4): the units' shock vectors (eta_1, ..., eta_N) are mutually independent with finite second moments.
  - Target: a chosen linear combination of the realised effects on the treated units, alpha-bar = sum_j sum_t w_jt alpha_jt (p. 3).
  - Estimator (p. 4-5): build a simple 2x2 DiD for each treated unit and period against never-treated units (eq. 2-4), then aggregate with known matrices B_j A_j. Assumption 2: parallel trends in the specific combination used (p. 5).
  - Proposition 1 (p. 7): the estimator is "unbiased, albeit inconsistent" (p. 7): alpha-hat ->p alpha-bar + sum_{treated j} B_j A_j eta_j as controls grow.
  - Assumption 3 (p. 9): for each treated j and every unit i in {j} or the controls, B_j A_j eta_i = H_j(Z_i; delta_j) xi_ij, with H a KNOWN function of observed Z_i (for example group size) up to a finite parameter, and xi_ij identically distributed across i with a continuous distribution. With H = identity this is Conley-Taber's i.i.d. case (p. 9).
  - Leading case (p. 9; Appendix A, p. 13-14): outcomes are averages over Z_i individuals, and the variance has the form delta0 + delta1/Z_i (matrix version Lambda0 + Lambda1/Z_i).
  - Algorithm (p. 9): (1) compute control "residuals" W-hat_i(j) = B_j A_j (Y_i - control mean); (2) estimate delta_j from them (least squares on outer products, Remark 2, p. 10); (3) normalise W-tilde_i(j) = H_j(Z_i; delta-hat)^(-1) W-hat_i(j); (4) B times: draw one control per treated unit with replacement and form e_b = sum_j H_j(Z_j; delta-hat) W-tilde_{i_b(j)}(j).
  - Proposition 2 (p. 10): the simulated distribution converges to that of the estimation error. Confidence interval: alpha-hat +/- q, q = 1 - alpha quantile of |e_b|. Uniform band over K parameters: alpha-hat_s +/- iota_s * q with q = 1 - alpha quantile of max_s |e_b,s / iota_s| (iota_s = 1 or the simulated SD) (p. 11; Corollary 1).

- **Main findings (all theoretical).**
  - With few treated units the DiD estimator is unbiased but neither consistent nor asymptotically normal; clustering at the unit level can give rejection rates above 60% for a 5% test in some examples (citing Ferman 2019; p. 2).
  - The control-residual approach extends to aggregated heterogeneous effects and to joint inference; critical values for uniform bands are non-standard and come from the resampling algorithm (p. 2, p. 11).
  - Estimating each alpha_jt separately and then aggregating avoids the negative-weight problems of two-way fixed effects (p. 4).

- **Usable for our paper.**
  - Method: our estimand. In their framing, the object is the average REALISED effect over the treated unit-periods actually observed (p. 3): for us, the mean effect over the five Nov 10 mornings of 2020-2024, not a population parameter for "all sirens". Uncertainty is about what those five mornings would have looked like without the siren.
  - Method: "estimate each year separately, then average with stated weights" (p. 4-5) is what we do (year-level DiD, equal weights). Cite for that structure.
  - Method: inconsistency with a fixed number of treated units (Proposition 1, p. 7) in a modern potential-outcomes notation; shorter to cite than Conley-Taber.
  - Robustness (multiple testing / event study): the max-statistic construction on p. 11. Applied to our permutation distribution it gives a familywise-valid test across the 5 speed classes, or a uniform band over an hour-by-hour profile: for each assignment compute max over classes of |D_s(a)| / iota_s; the adjusted p-value of class s is the share of assignments whose maximum is at least |D_s| / iota_s. (The paper does this with draws from control residuals; using our 1024 assignments instead is my adaptation.)
  - Robustness: the parametric heteroskedasticity model delta0 + delta1/Z (p. 9) restates the Ferman-Pinto correction and shows how to apply it when several years are aggregated (one H_j per treated unit).

- **Caveats.**
  - The task description and `review.md` treat this as a spatial-correlation reference or as support for "permutation over asymptotics" when pooling years. It is neither. Units are assumed independent (p. 4). Spatial correlation appears only (a) in footnote 7 (p. 8), which says Conley-Taber's appendix has an alternative allowing heteroskedasticity and spatial correlation under normality and a parametrised distance model, and (b) in the remark that the A + B/Z variance form survives a wide range of spatial and serial correlation WITHIN a unit (p. 9). The paper does not propose permutation of treatment labels; it resamples rescaled control residuals and is valid as the number of controls goes to infinity.
  - No simulations and no empirical example: there is no evidence in the paper on how the procedure performs with, say, 15 or 50 controls.
  - "Staggered adoption" does not describe our design. Our five treated dates are five separate one-off events with their own control dates; there is no adoption that persists. The relevant part is only the aggregation of several 2x2 estimates.
  - For our data the spatial question is different from Ferman (2020)'s anyway (my reading): treated and control "units" are dates observed on the SAME cells, so spatial correlation is within unit. Dependence between units would be temporal (week-to-week), which none of these papers treats.

- **Checks it suggests for us.**
  1. Max-statistic adjusted p-values for the 5 speed classes from the joint permutation distribution (p. 11).
  2. Uniform band for an event-study profile (contrast at each hour 06h-12h relative to neighbours, or the 5-minute index), using the same max-statistic quantile.
  3. Report year-specific D_y with the weights used to aggregate, and show an alternative weighting (by cells or vehicles) (p. 3-5).
  4. If the widened pool shows var(W_d) depending on M_d, use the rescaled-residual algorithm (p. 9) as a model-based cross-check of the permutation p-value.

---

## Cross-paper synthesis (10 lines)

1. All seven papers agree on the starting point: with a fixed, small number of treated units the DiD estimate is unbiased but not consistent, its noise is the treated units' own group-level shocks, and cluster-robust or cell-level standard errors are useless (conley2011 p. 6-10; mackinnon2017 p. 11-13; alvarez2023 p. 7). For us the unit is the date; 400-2300 cells do not reduce date-level shocks.
2. Placebo or permutation inference over untreated units is the accepted answer, but it is valid only if the treated unit's noise is distributed like the placebo units' noise: i.i.d. shocks across units, unrelated to treatment (conley2011 p. 8), or exchangeability (hagemann2019 p. 9; mackinnon2020 p. 5-6).
3. Nov 10 is not randomly assigned, so by mackinnon2020 (p. 6) we should not call the test "randomization inference" in the design-based sense; it is a placebo test under within-year exchangeability of date contrasts. The fixed second-of-four position and any November trend are violations that no paper here repairs.
4. The best-documented failure is heteroskedasticity from unequal counts: var(W_d) = A + B/M_d (ferman2019 p. 10). A treated unit with fewer observations gives over-rejection, with more gives under-rejection (ferman2019 p. 16; mackinnon2020 p. 8-10); large M does not help when within-unit correlation is near zero (ferman2019 p. 17-18, p. 22).
5. Because we permute within year, the relevant comparison is Nov 10 versus its own year's control dates, not small years versus large years. First-order checks: cell and vehicle counts by date, a balanced cell panel, and an estimate of the within-date correlation rho.
6. Coefficient-based RI (what we do) is exact with homogeneous units and has the most power; t-based RI helps only with two or more treated clusters and is unreliable with one (mackinnon2020 p. 12-15). Earlier notes overstated "studentised RI is safer" for our one-treated-per-year design.
7. A defensible studentised robustness row is the across-year t statistic recomputed under every one of the 1024 assignments (5 treated dates in the pool), in the spirit of hagemann2019's adjustment (p. 7); expect it to be conservative and less powerful.
8. hagemann2019 needs 2+ treated clusters, C(q, q1) >= 1/alpha permutations, independence across clusters and within-cluster noise that averages out (p. 9-11); it supports the placebo logic and the "at least 1/alpha assignments" rule but not our exact procedure. Wild bootstraps are ruled out by mackinnon2017 (p. 12-15) and mackinnon2018 (p. 11-12).
9. Widening the control pool moves us from a pure permutation argument (3 controls) towards the Conley-Taber / Ferman-Pinto large-control regime, where the 1/M variance regression, the rescaling correction and a placebo-p-value uniformity plot become feasible (conley2011 p. 23; ferman2019 p. 12).
10. Gaps: none of the seven papers covers dependence between units (serial correlation across weeks), stratified one-treated-per-stratum designs, or spatial correlation across units. alvarez2023 is not a spatial paper; Ferman (2020) and Hagemann (2020, single treated cluster) are the missing references. For multiple testing, alvarez2023's max-statistic band (p. 11) adapts directly to our 5 speed classes.
