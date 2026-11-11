# Reading notes 02: Rosenbaum (2002 article, 2002 book) and Abadie et al. (2020) - design-based inference

Page numbers `(p. N)` are PDF pages as marked in `literature/txt/<key>.txt`.
For rosenbaum2002, PDF p. N = journal p. 285 + N. For rosenbaum2002book, PDF p. N = printed p. N - 13.

---

### rosenbaum2002 - Rosenbaum (2002), "Covariance Adjustment in Randomized Experiments and Observational Studies" (Statistical Science 17(3), 286-327, with comments by Angrist & Imbens, Hill, Robins, and a rejoinder)

- **Question and setting.** How to combine covariance (regression) adjustment with exact randomization inference so that tests, point estimates and confidence intervals need no distributional assumption and no "correct" regression model; then how to carry the same machinery to observational studies, where assignment is not random and sensitivity to hidden bias has to be reported (p. 1-2).

- **Data and method.**
  - Framework (p. 3-4): n units, fixed potential responses (r_Tj, r_Cj) and fixed covariates x_j; the only random object is the assignment vector Z. Observed R_j = Z_j r_Tj + (1 - Z_j) r_Cj. Under an additive effect r_Tj - r_Cj = tau, the adjusted response R - tau Z = r_C is fixed.
  - Test of H0: tau = tau0 without covariates (p. 4): compute t(Z, R - tau0 Z) and compare with its randomization distribution. Confidence set = all tau0 not rejected (test inversion; Lehmann 1963, Moses 1965). Hodges-Lehmann (HL) estimate = the tau that makes t(Z, R - tau Z) equal to its null expectation (for the rank sum, m(n+1)/2; the solution is the median of all treated-minus-control pairwise differences).
  - Covariance adjustment (p. 4-5): pick any fitting algorithm eps~(.) (OLS, Huber M-estimation, rank regression, lowess). Under H0, e0 = eps~(R - tau0 Z) = eps~(r_C) is a fixed vector, so t(Z, e0) has a known exact randomization distribution. The fit is "a fit, not a model": it need not be correct, need not converge at root-n, and only affects power (p. 2, p. 5).
  - Exact link to OLS (p. 5): if residuals come from OLS with a constant and the statistic is the treated sum of residuals Z'e0, the HL estimate is the usual covariance-adjusted OLS coefficient, tau^ = Z'(I - H)R / Z'(I - H)Z, H = X(X'X)^{-1}X'.
  - Observational studies (p. 6-7): assignment probabilities pi_j are unknown. "Free of hidden bias" = pi_j depends only on observed x_j. Then a conditional permutation test given the sufficient statistic X'Z (logit model for pi_j) is valid; the plain residual-permutation test of Section 2.4 is justified only when assignment is equiprobable (p. 7).
  - Matched pairs (p. 8-10): differences Y_i, covariate differences d_i; regress Y - tau0 V on D without constant; Wilcoxon signed rank on residuals; null mean I(I+1)/4, variance I(I+1)(2I+1)/24.
  - Matched sets with more than two units (Section 7, p. 15-16): set i has n_i units, m_i treated; if assignment within a set is uniform over the C(n_i, m_i) possibilities, test H0: tau = tau0 by (i) forming R_ij - tau0 Z_ij, (ii) aligning = subtracting the set mean, (iii) aligning covariates the same way, (iv) regressing aligned adjusted responses on aligned covariates (robust regression allowed), (v) ranking residuals over all N units and summing treated ranks (Hodges-Lehmann 1962 aligned rank test). With OLS and raw residuals instead of ranks, the HL estimate equals the OLS coefficient in a regression with treatment dummy, set dummies and covariates (p. 16).
  - Sensitivity model (p. 10-11): within pair i, 1/Gamma <= pi_i1/pi_i2 <= Gamma. Gamma = 1 is the randomization distribution. For Gamma > 1 the null distribution of the signed rank statistic T is unknown but bounded stochastically by two known distributions T+ and T-: sums of I independent terms equal to q_i with probability Gamma/(1+Gamma) (resp. 1/(1+Gamma)) and 0 otherwise; E(T+) = Gamma/(1+Gamma) * sum q_i, var = Gamma/(1+Gamma)^2 * sum q_i^2. The same bounds apply to residuals from the covariance fit; bounds on HL estimates and CIs follow by inversion (p. 11).
  - Examples: 15 exposed vs 11 control workers, DNA adducts (p. 2-3); 66 matched NJ-PA restaurant pairs from Card and Krueger (p. 7-9).

- **Main findings.**
  - DNA-adduct example, log scale: unadjusted rank sum 242.5 vs null mean 202.5, variance 362.62, deviate 2.10; one-sided 95% CI tau >= 0.41, i.e. at least a 51% increase (p. 4). After robust regression on three covariates: rank sum 241, null variance 371.25, deviate 1.998; one-sided CI tau >= 0.29, at least 34% (p. 5-6). So adjustment did not sharpen inference here; it changed the interval.
  - Minimum wage, 66 pairs, covariance-adjusted: HL estimate +2.065 employees; 95% CI [-0.58, 4.81] (p. 10).
  - Sensitivity (Table 3, p. 12): Gamma = 1: tau^ = 2.06, P for H0: tau = -2 is 0.0021; Gamma = 1.5: minimum estimate 0.14, max P 0.069; Gamma = 2: minimum estimate -1.22, max P 0.29.
  - Permutation IV inference can return infinite intervals (weak instrument) or empty ones (model rejected) (p. 14-15).
  - Discussion. Angrist and Imbens: with large independent samples RI and model-based inference differ little; RI is most valuable when treatment varies at group level with few groups, because it avoids estimating the dependence structure (p. 21); they also say Rosenbaum-style sensitivity analysis is uncommon in economics and deserves wider use (p. 21). Robins: exact randomization inference for tau relies on additivity; in a two-unit counterexample with a shift but no additivity the Wilcoxon level is wrong, yet large-sample intervals computed under additivity are conservative when only the shift model holds (p. 27); Gamma's meaning depends on which covariates are conditioned on (p. 34); a simpler alternative is a mean-shift bias gamma*, which just moves estimate and interval by gamma* (p. 35). Rejoinder: an interval for an additive effect is informative through the values it excludes even if additivity is uncertain (p. 39-40); a sensitivity analysis is a computed fact about the study, not an expert opinion (smoking-lung cancer becomes sensitive near Gamma = 6, coffee-MI near 1.3) (p. 40).

- **Usable for our paper.**
  - Method: our inference is a randomization test on a stratified (blocked) design: block = year, n_i = 4 same-weekday dates, m_i = 1 "treated" date, 4^5 = 1024 assignments. This is exactly the matched-set structure of Section 7; cite for aligned statistics (subtract the year mean of the contrast before pooling) (p. 15-16).
  - Method: report a Hodges-Lehmann estimate and a test-inversion interval for the siren effect instead of only a p-value: for a grid of D0, subtract D0 from the treated date's contrast in each year, recompute the statistic, keep the D0 not rejected (p. 4, p. 10). Convert endpoints with 60*(1 - exp(D)).
  - Method/Robustness: weather or other date-level covariates (rain, temperature, school-holiday dummy) can be handled by regressing the year-aligned, D0-adjusted contrasts on aligned covariates and permuting the residuals; the inference stays exact under the assumed assignment, whatever the regression (p. 4-5, p. 16). With OLS and a mean statistic this reproduces the fixed-effects regression coefficient (p. 5, p. 16), which lets us show the regression DiD and the RI estimate are the same number.
  - Robustness: the date is not randomized, so Gamma = 1 is an assumption. Report the Gamma at which the one-sided p crosses 0.05 (p. 10-12). One short quote for motivation: randomization is the "reasoned basis for inference" (p. 1, Fisher via Rosenbaum).
  - Literature/Method: Angrist-Imbens comment supports RI when the treatment varies at an aggregate level (here: the date) and micro units (cells) are many but dependent (p. 21). Supports "effective sample = dates, not cells".
  - Results-Discussion: wording of intervals as "values rejected", not "values endorsed" (p. 39-40).

- **Caveats.**
  - The exact test is exact only under the stated assignment distribution. For a calendar-fixed date, uniform assignment over the 4 dates is an "as-if" assumption (equivalent to exchangeability of the untreated contrasts across the dates within a year), not something the paper grants us. Rosenbaum says the residual-permutation method of Section 2.4 is for randomized experiments; observational use needs "no hidden bias" plus a sensitivity analysis (p. 6-7).
  - HL estimates and inverted intervals assume a constant additive effect (here: the same log-point effect in every year). If the siren effect differs by year (e.g. 2020 pandemic traffic), exactness for the "average" effect is lost (Robins, p. 27; Hill, p. 23). The sharp null of no effect in any year is unaffected.
  - With 1 treated of 4 in 5 blocks the randomization distribution has at most 1024 points and the smallest attainable one-sided p is 1/1024 = 0.00098; ties make it coarser. The article's sensitivity formulas are written for pairs and signed ranks; the multi-control case is in the book (Section 4.4-4.5) and in Gastwirth, Krieger and Rosenbaum (2000), cited p. 16.
  - Covariance adjustment does not repair a time trend that is collinear with position (Nov 10 always the 2nd of 4 dates): adjustment helps precision, the validity still rests on the assignment assumption.
  - The article does not discuss spatial correlation, multiple testing, or time-series designs.

- **Checks or analyses it suggests for us.**
  1. Compute the HL point estimate and the inverted 90%/95% interval for D per speed class; report in minutes.
  2. Use year-aligned contrasts; compare mean statistic vs aligned-rank statistic (robust to one odd year).
  3. Residual-permutation version with weather covariates (precipitation, temperature) and show the estimate barely moves.
  4. Gamma sensitivity for the 1-of-4 design: worst-case probability that the treated date is the largest-slowdown date is Gamma/(Gamma+3); report the Gamma where p crosses 0.05 (formula from the book notes below).
  5. Placebo outcome in the spirit of the rejoinder (p. 37): hours that cannot be affected (e.g. 14h vs 13h/15h contrast) on the same dates.

---

### rosenbaum2002book - Rosenbaum (2002), Observational Studies, 2nd ed. (Springer, 386 pp.)

- **Question and setting.** A textbook on causal inference when the investigator does not assign treatment: what randomization buys (ch. 2), what adjustment for observed covariates can and cannot do (ch. 3), how to quantify sensitivity to hidden bias (ch. 4-5), and how to design a study so that hidden bias can be detected or made less plausible (ch. 6-9, 11-12).
- **How it was read.** Chapter 1 (p. 14-30), Chapters 2-3 (p. 31-117), Chapters 4-5 (p. 118-217) and Chapters 11-12 were read in full; Chapters 6-10 were searched and read selectively for our topics. Chapters 2-12 were read by delegated sub-readers working from the same brief, with formulas spot-checked against the text (e.g. the bound (4.17), p. 133-134). No direct quotations are used for the book.
- **Chapter 1 (motivation), main points.**
  - An observational study is about a treatment whose assignment the investigator does not control (p. 14-15).
  - Vitamin C and cancer: a matched observational study (100 treated, 10 historical controls each, P < 0.0001) was contradicted by a randomized trial; matching on a few variables does not make groups comparable, and control groups defined by a different process (records of the already dead) add bias (p. 15-17). Usable in Introduction/Method as the standard warning that a small p-value under a randomization model is not evidence of random assignment.
  - Elaborate theories: derive several distinct consequences of the causal hypothesis and check each (Fisher's advice via Cochran; Doll and Hill's coronary mortality gradient 2.12, 2.72, 2.81, 3.79 per 1000 for non-, light, moderate and heavy smokers) (p. 18-19). Usable in Method/Robustness: our pattern predictions (larger in free-flow cells, larger in minimum speed, absent in placebo hours and placebo dates).
  - DES and vaginal cancer: 7 of 8 case mothers exposed vs 0 of 32 referents; very insensitive to hidden bias despite n = 8 (p. 20-21). Small samples can still be insensitive if the effect is large.
  - The author of a study should list the alternative explanations himself; criticism should be tangible, i.e. a testable counter-hypothesis (p. 22-23). Usable in Robustness framing.

#### Chapters 2-3 (randomization inference; overt bias)

- **Data and method** (formal machinery)
  - *Setup.* N units in S strata built from pre-treatment covariates; n_s units in stratum s; Z_si = 1 if treated; m_s = sum_i Z_si. One treated unit plus one or more controls per stratum is called matching with multiple controls (p. 36). A unit is one opportunity to treat; a group can be a single unit (pp. 35-36).
  - *Assignment set.* With m_s fixed, Omega holds all K = prod_s C(n_s, m_s) vectors having m_s ones in stratum s. A *uniform randomized experiment* sets prob(Z = z) = 1/K on Omega; strata are then mutually independent (pp. 37-38). Each unit must have treatment probability strictly between 0 and 1 (p. 37).
  - *Sharp null.* No effect means every unit's response is identical under all assignments, so r is fixed and only Z is random (pp. 39-40). Exact one-sided level: `prob{t(Z,r) >= T} = sum_{z in Omega} [t(z,r) >= T] prob(Z = z)` (2.3); under uniform assignment `= |{z in Omega: t(z,r) >= T}| / K` (2.5) (pp. 40-41).
  - *Statistic classes.* Sum statistics t = Z'q, q a function of r: rank sum, stratified rank sum, aligned ranks (rank all responses after subtracting stratum means), median test, signed rank (pp. 44-47). Null moments (Prop. 2): `E = sum_s m_s qbar_s`; `var = sum_s [m_s(n_s - m_s)/(n_s(n_s - 1))] sum_i (q_si - qbar_s)^2` (p. 47). Sign-score statistics `sum_s d_s sum_i c_si Z_si`, c binary, are a subclass useful for Chapter 4; rank sums are outside it (pp. 47-48, 50). Arrangement-increasing: f(a, b_sij) >= f(a, b) whenever (a_si - a_sj)(b_si - b_sj) <= 0 (p. 48). Effect-increasing: t(z, r) <= t(z, r*) whenever (r*_si - r_si)(2 z_si - 1) >= 0 for all units (pp. 49-50).
  - *Effects.* No interference: a unit's response depends only on its own assignment, so R_si = Z_si r_Tsi + (1 - Z_si) r_Csi (p. 53). Additive effect: r_Tsi = r_Csi + tau, hence R - tau Z = r_C is fixed (pp. 54-55). Positive effect: r_T >= r_C, strict for at least one unit (p. 55).
  - *Test inversion.* H0: tau = tau_0 is tested by running the no-effect test on R - tau_0 Z (p. 56). The 1 - alpha confidence set collects every tau_0 with P-value >= alpha; coverage is at least 1 - alpha; for a two-sided test it is usually an interval located by line search (pp. 57-58). The example doubles for a two-sided level (p. 57).
  - *Hodges-Lehmann.* With tbar the null expectation, solve tbar = t(Z, R - tau Z); because of jumps the definition is `tau_hat = [ inf{tau: tbar > t(Z, R - tau Z)} + sup{tau: tbar < t(Z, R - tau Z)} ] / 2` (pp. 60-61). For effect-increasing statistics t(Z, R - tau Z) falls monotonically in tau (p. 60). The only closed form printed is for the single-stratum rank sum: the median of the m(N - m) treated-minus-control differences (p. 61). For the mean difference the text gives tbar = 0 (p. 60) and leaves the estimate as Problem 5 (p. 77).
  - *Observational model.* Independent assignment with unknown pi_j in (0,1) (3.1); the study is *free of hidden bias* when pi_j = lambda(x_j), a function of observed covariates alone (3.2) (p. 90). Overt bias is a recorded pre-treatment difference, hidden bias an unrecorded one (p. 83).

- **Main findings**
  - Validity rests on the assignment distribution only: units need not be homogeneous, sampled from a population, or independent; the Lady's eight judgements are dependent (p. 35).
  - Lady tasting tea: K = C(8,4) = 70; all correct P = 1/70 = 0.014; six or more correct P = 17/70 = 0.24 (pp. 41-42).
  - Prop. 4: an effect-increasing statistic yields a test unbiased against positive effects and grows with larger effects, without additivity (p. 56). Prop. 5 extends this to partially ordered (multivariate or censored) outcomes through statistic (2.8), within-stratum treated-control comparisons won minus lost (pp. 64-66).
  - Table 2.5 (N = 8, m = 4, true tau = 7): testing tau_0 = 1 gives rank sum 26, one-sided P = 1/70, two-sided 0.028 (p. 57). Table 2.6: tbar = 18; the statistic is 19 at tau = 5 and 17 at tau = 6, so tau_hat = 5.5 (p. 61).
  - Mean difference, and direct adjustment `sum_s (n_s/N)[treated mean_s - control mean_s]` (2.6), are unbiased for the average effect on the study's N units under no interference alone (pp. 58-59).
  - Discreteness and computation: K almost doubles per added unit; the standard remedy is a moment-based large-sample approximation; alternatives are exact FFT algorithms or designs whose Omega has 10,000-100,000 elements, where direct enumeration handles any statistic (pp. 46-47). With fewer than 20 assignments nothing reaches 0.05 (p. 99). Monte Carlo sampling of assignments is absent from these chapters.
  - Ties: average ranks; tied pairs add nothing to the signed rank (pp. 44-45).
  - Core Chapter 3 result: if free of hidden bias and strata are exactly homogeneous in x (or in lambda(x)), then prob(Z = z | m) = 1/K, the uniform-experiment distribution, although lambda is unknown (pp. 91-92, 95). The author warns that this follows from a premise that is rarely well supported and must be probed (p. 92); without randomization, equal probabilities are an assumption open to dispute (p. 42).
  - Lead example, 33 matched pairs: signed rank one-sided P < 0.0001; HL estimate 15 microg/dl; 95% interval (9.5, 20.5), conditional on no hidden bias (p. 93).
  - Section 3.4: under log[lambda_s/(1 - lambda_s)] = beta'x_s, mbar = sum_s m_s x_s is sufficient, and Z is uniform on the larger set of assignments reproducing mbar; usable even when n_s = 1 (pp. 98-99). PACCO: |Omega| = 12 versus 28 in the enlarged set; P = 8/28 = 0.29 (pp. 100-102).
  - Section 3.5 (large samples): fit a logit of Z on x and scores q(R), test the q coefficient; intervals come from q(R - tau_0 Z) (pp. 102-103). Benzene: 58 exposed, 20 controls, z = 2.18; additivity is judged misleading there owing to many zero responses (pp. 103-104).
  - Section 3.6: pairs inexactly matched on a few discrete covariates are grouped by imbalance pattern and one conditions also on the per-class count of first-unit-treated pairs; Ktilde = 2^{n_0} prod_c C(n_c, m_c) (pp. 108-109); pooling over matched covariates needs the additive logit model (3.13) (p. 107). Vasectomy: 36 discordant pairs, observed 20, adjusted expectation 19.015 (unadjusted 18), deviate 0.186 (p. 110).
  - Chapter 3 Problem 1: over Omega, the permutation P-value of the least-squares covariance-adjusted estimate (covariates constant within strata) equals that of the unadjusted treated total (p. 112).

- **Usable for our paper**
  - Method: our design is matching with multiple controls, m_s = 1, so K = prod_s n_s = 4^5 = 1024 and the smallest attainable P is 1/1024 (pp. 36-37, 41); with Omega this small, direct enumeration is feasible for any statistic (p. 47).
  - Method: dates are the units because treatment is applied per date; grouped units and dependent responses are permitted (pp. 35-36), which addresses cell-level spatial correlation.
  - Method: our mean-contrast statistic (sign flipped) is effect-increasing, so Prop. 4 applies without a constant-effect assumption (p. 56).
  - Method/Results: interval = all tau_0 not rejected when the test is rerun on R - tau_0 Z (pp. 56-58); HL definition with inf/sup averaging (p. 61).
  - Method/Results-Discussion: the 1/K distribution holds only if, within a year, same-weekday dates were equally likely to be treated given covariates (pp. 91-92); this is an assumption, not a design fact (pp. 42, 92).
  - Robustness: weather is a legitimate covariate because treatment cannot alter it, like Cox's factory-humidity case (p. 85); adjusting for treatment-affected quantities can erase part of the effect (pp. 85-86).
  - Results-Discussion: conclusions are specific to these units, times and circumstances: internal, not external, validity (pp. 51, 58).
  - Robustness: ten baseline tests with one significant is what chance produces (pp. 32-33), supporting a multiplicity caveat for five speed classes.

- **Caveats**
  - The model requires 0 < pi < 1 for each unit (p. 90). A calendar-fixed date is deterministic; neither chapter covers that case, so our test rests on an as-if premise the book does not endorse.
  - Absent: time series, before-after designs, trends, serial correlation, treatments fixed by date. Closest items: interference violations are illustrated, not analysed, and no interference is called often implausible for repeated measures on one subject (p. 54); Problem 2 poses a longitudinal design with carry-over, R_si - R_s,i-1 = eta_si + Delta Z_si, and asks, unanswered, whether inference survives through adjusted changes (p. 76); calendar time appears only as a matching variable (p. 104).
  - HL estimates and intervals presuppose additivity (pp. 56-59). One-sided confidence bounds are not described separately. No closed form is printed for our statistic (our own derivation: t(Z, R - tau Z) = t - tau and tbar = 0, so tau_hat is the observed statistic).
  - Sections 3.4-3.6 model assignment through a logit, not the outcome; regressing outcomes on covariates and permuting residuals does not appear. Section 3.6 treats pairs only; 3.5 needs N large relative to dim(x) (p. 103).

- **Checks or analyses it suggests for us**
  - After widening controls, recompute K = prod_s n_s and report 1/K as the smallest possible P.
  - Invert the exact test over a tau_0 grid; report the HL estimate and a two-sided interval.
  - Add a rank statistic (aligned ranks or stratified rank sum, p. 45) beside the mean contrast.
  - Weather: restrict controls to dates in the same coarse weather class as that year's 10 November (exact stratification on x, p. 91); strata left without a control contribute nothing (p. 99).
  - One joint test over speed classes with the partial-order statistic (2.8) (pp. 64-65).
  - Follow with Chapter 4 sensitivity analysis, the book's response to the untestable premise (p. 92).


#### Chapters 4-5 (sensitivity to hidden bias; non-additive effects)

- **Data and method**
  - *Model.* Units j, k with equal observed x may differ in treatment probability, but only up to an odds ratio: `1/Gamma <= pi_j(1-pi_k) / [pi_k(1-pi_j)] <= Gamma`, Gamma >= 1 (eq. 4.1, p. 119). Equivalent form: `logit(pi_j) = kappa(x_j) + gamma*u_j`, `0 <= u_j <= 1`, `Gamma = exp(gamma)` (eq. 4.2, p. 119). Proposition 12: both give the same family of assignment distributions, so the logit shape and the bounded u add no assumption; u can be taken binary (p. 120).
  - *Assignment distribution* with m_s treated of n_s: `Pr(Z=z|m) = prod_s exp(gamma z_s'u_s) / sum_{b in Omega_s} exp(gamma b'u_s)`, Omega_s = the C(n_s, m_s) possible vectors (eq. 4.6, p. 121). kappa(x) cancels, u does not. Uniform (randomization) when Gamma = 1 or u is constant within strata (p. 121). One treated per set: `Pr(Z=z|m) = prod_s exp(gamma sum_i z_si u_si) / sum_i exp(gamma u_si)` (eq. 4.15, p. 133).
  - *Pairs, sign-score statistics* `T = sum_s d_s sum_i c_si Z_si` (c binary): independent terms worth d_s with probability p_s, `1/(1+Gamma) <= p_s <= Gamma/(1+Gamma)` in discordant pairs (p. 123). Proposition 13: `Pr(T+ >= a) >= Pr(T >= a|m) >= Pr(T- >= a)`, sharp, reached at u_si = c_si or 1 - c_si, a u that predicts the outcome sign almost perfectly (p. 123). `E(T+) = sum d_s p_s+`, `var(T+) = sum d_s^2 p_s+(1-p_s+)` (eq. 4.9, p. 124). McNemar: Binomial(discordant pairs, Gamma/(1+Gamma)) (p. 125). Signed rank, no ties: `E(T+) = p+ S(S+1)/2`, `var(T+) = p+(1-p+) S(S+1)(2S+1)/6` (eq. 4.11, p. 126).
  - *One treated, n_s - 1 controls, sign scores.* `p_s = sum_i c_si exp(gamma u_si) / sum_i exp(gamma u_si)` (4.16), bounded by `c_s+ / [c_s+ + (n_s - c_s+)Gamma] <= p_s <= Gamma c_s+ / [Gamma c_s+ + n_s - c_s+]`, c_s+ = sum_i c_si (eq. 4.17, p. 133). Proposition 14 gives exact stochastic bounds for every sign-score statistic (p. 132); deviate `(T - sum d_s p_s+) / sqrt(sum d_s^2 p_s+(1-p_s+))` (p. 134).
  - *One treated per set, arbitrary fixed scores* (section 4.5.2), `T = sum_s sum_i Z_si q_si`: two bounding distributions are not available in general (p. 148). Large-S approximation: with u = 0 on the a lowest scores of the set and u = 1 on the rest, `mu_sa = [sum_{i<=a} q_si + Gamma sum_{i>a} q_si] / [a + Gamma(n_s - a)]`, `nu_sa^2 = [sum_{i<=a} q_si^2 + Gamma sum_{i>a} q_si^2] / [a + Gamma(n_s - a)] - mu_sa^2`; `mu_s = max_{0<a<n_s} mu_sa`, nu_s^2 the largest variance among maximisers; upper bound on `Pr(T >= t)` is about `1 - Phi[(t - sum mu_s)/sqrt(sum nu_s^2)]` if t > sum mu_s, else at least 1/2 (p. 149-150). It converges to the sharp bound as S grows; for finite S maximising the mean first may be wrong (p. 148). The label asymptotic separability appears only in the cited paper's title (p. 176). For within-set ranks with n_s = 4, Gamma = 2: mu_s = 17/6, nu_s^2 = 41/36 (Table 4.14, p. 151). Lower tail: Problem 11 (p. 173).
  - *Hodges-Lehmann (HL) and intervals,* additive effect tau: apply the test to R - tau0*Z. Pairs: equate the statistic to the extreme null expectations `p- S(S+1)/2` and `p+ S(S+1)/2` (p. 128-129). Sensitivity interval = union over u of the confidence intervals (p. 130). Multiple controls: equate T to sum mu_s for the minimum estimate; invert the approximate test (p. 150).
  - *Section 4.6, two unmatched groups (S = 1).* For a sum statistic the maximising u changes with the cut-off but always has ones on the k largest scores; search k = 0..n with exact or approximate moments (p. 152-156). Appendix Proposition 19 covers strata: for any arrangement-increasing function, including the tail indicator of a sum statistic, the extreme is reached at a binary u ordered within each stratum like the scores (p. 164-166). Proposition 18: monotone in each coordinate of u (p. 165).
  - *Chapter 5, dilated effects.* `r_T = r_C + Delta(r_C)`, Delta nonnegative, nondecreasing (p. 185). With rho the k-th control order statistic, `sign(R - Z*Delta(rho) - rho) = sign(r_C - rho)` (Prop. 21, p. 188); test Delta(rho) = Delta0 by counting treated adjusted responses at or above the k-th adjusted order statistic; under Gamma the count is bounded by sums of extended hypergeometrics, strata allowed (p. 188-189); inversion gives intervals and estimates (p. 190). Delta at the median is the median unit effect (p. 186). Upper quantiles, where effects are larger, are less sensitive (p. 191-192).
  - *When additivity fails.* If treated responses are higher and more dispersed, the book calls the additive model inapplicable and switches method (p. 184); it does not say the additive HL estimate keeps a meaning.
  - *Attributable effects, displacements, quantiles* (single stratum). `A = sum Z_i delta_i` for binary responses is random; test by shifting A in the 2x2 table (p. 201-203). Displacement: a unit carried across a control quantile theta; if A = a then `R_(k+1-a) > theta > R_(k-a)` (Prop. 22, p. 205). `[R_T(a), R_T(b)]` covers r_T(k) with probability at least `Y(n,m,k,a,1/Gamma) - Y(n,m,k-1,b,Gamma)`, Y the extended hypergeometric tail (p. 208).
  - *Instrumental variable.* `r_T - r_C = beta(d_T - d_C)`; test beta0 on R - beta0*D with Chapter 4 tools (p. 192-198).

- **Main findings** (upper bound on the one-sided p-value)
  - Smoking and lung cancer, 122 discordant pairs: 0.0036 at Gamma = 4, 0.03 at 5, 0.1 at 6 (p. 125-126).
  - Lead in children, 33 pairs: 0.0018, 0.0136, 0.0388, 0.0468, 0.074 at Gamma = 2, 3, 4, 4.25, 5 (p. 127); HL 15, range 10.25-19.5 at Gamma = 2 (p. 129); 95% interval (9.5, 20.5), then (4.5, 27.5) at Gamma = 2 (p. 130).
  - Vitamin C, 18 sets of 1 + 10: 0.019 at 2, 0.082 at 3 (p. 135); with another statistic 0.045 at Gamma = 10, yet a randomized trial contradicted it (p. 135).
  - DES, 8 cases each with 4 referents (case-referent bound 4.19, p. 137): 0.0004, 0.012, 0.038, 0.054 at Gamma = 2, 4, 6, 7 (p. 139). Endometrial cancer 0.068 at 4; ectopic pregnancy 0.0668 at 4; herniated disc 0.093 at 2 (p. 140). Coffee and infarction: 0.0038 at Gamma = 1, above 0.05 from 1.3 (p. 140-141).
  - Allopurinol: 0.036 at 2, 0.30 at 3 (p. 143). Asbestos miners: deviate 2.27 at 3, 0.73 at 4 (p. 146). Methylmercury: blood mercury 0.0179 at Gamma = 35; chromosome damage 0.0375 at 2, 0.10 at 3 (p. 159).
  - Minimum wage, beta = -1: 0.004 at 1, 0.0506 at 1.34 (p. 200). Cadmium, no effect at median versus upper quartile: 0.051 versus 0.0023 at Gamma = 2; the quartile test crosses 0.05 between 4 and 5 (p. 192).

- **Usable for our paper**
  - Method: define Gamma by (4.1)-(4.2), (4.15); Gamma = 1 is our randomization test (p. 119-121, 133).
  - Method: the claim is correct. With one treated among n_s, (4.15) gives a unit probability exp(gamma u_i)/sum_j exp(gamma u_j), at most `Gamma/(Gamma + n_s - 1)`, at least `1/(1 + Gamma(n_s - 1))`; this is (4.17) with c_s+ = 1 (p. 133); the DES example uses 2/(2+4) = 0.33 (p. 138).
  - Robustness: report p-value range, HL range and sensitivity interval on a Gamma grid, plus the Gamma where the upper p-value crosses 0.05 (p. 125-130, 161).
  - Results-Discussion: benchmarks. The book calls a crossing at 1.3 sensitivity to fairly small bias (p. 141), crossings between 1.5 and 3 sensitivity to moderate bias (p. 159, 200, 204), and 6 a high degree of insensitivity (p. 126).
  - Results-Discussion: the analysis shows how much bias would be needed, not whether it exists (p. 135-136); sensitivity is no fault, insensitivity no achievement, and a small study can be insensitive if the association is strong (p. 141).

- **Caveats**
  - For a sum of arbitrary scores with one treated unit per set, the book gives only the large-S Normal approximation (p. 148-150); exact bounds are for sign-score statistics (p. 132). Five strata are far from that limit.
  - The model treats assignment as random with unknown unequal probabilities. I found nothing in either chapter on a treatment fixed by the calendar, on serial dependence, or on a trend inside the window.
  - The worst case needs a u that nearly determines the response ordering (p. 123, 126); Gamma alone says nothing on plausibility. A two-parameter extension is only cited (p. 170).
  - The choice of statistic changes the answer; the book offers little firm advice (p. 136).
  - HL estimates and inverted intervals assume additivity (p. 128, 150). Attributable effects, displacements and quantile intervals are developed for one stratum only (p. 200, 204, 207).

- **Checks or analyses it suggests for us**
  - Exact worst-case p-value for 5 x (1 of 4). From the book: (4.15) (p. 133) and Proposition 19: the maximum of Pr(T >= t) is at a binary u with ones on the k_s highest scores of each year (p. 165-166). My derivation: scores q_si = year-mean-aligned responses, negated so slowing is the upper tail; for each (k_1..k_5) in {1,2,3}^5 (243 cases; k_s = 0 or 4 is uniform) weight date i in year s by `Gamma/(k_s Gamma + 4 - k_s)` if among the top k_s, else `1/(k_s Gamma + 4 - k_s)`; add the product weights of the assignments, among the 1024, with T >= t_obs; take the maximum over cases. Repeat on a Gamma grid.
  - My derivation, quick bounds: each assignment has probability at most `[Gamma/(Gamma+3)]^5`, so with K assignments at least as extreme, worst-case p <= K[Gamma/(Gamma+3)]^5. K = 8 (p = 0.008) stays below 0.05 at least up to Gamma = 1.70; K = 35 (p = 0.034) up to about 1.11. The most extreme possible outcome (p = 1/1024) crosses 0.05 at Gamma = 3.66, so this design cannot show insensitivity beyond about 3.7.
  - About 50 dates per year: 49^5 cases are too many to enumerate; use the mu_s, nu_s^2 approximation (p. 149) and check it by a coordinate-wise search over k_s (my suggestion, motivated by Proposition 18, p. 165). The cap becomes `[Gamma/(Gamma+49)]^5` (0.05 at Gamma near 60), but Gamma then compares two of 50 dates, so values are not comparable across designs.
  - Report worst-case HL estimate and sensitivity interval by applying the same test to responses with tau0 removed from 10 Nov (p. 130, 150).
  - Trend: position in the window is one admissible u; also rerun with scores detrended within year (my suggestion, not the book's).


#### Chapter 5, Sections 5.5-5.9 (attributable effects, displacements, quantiles)

- **Data and method**
  - Read PDF pp. 201-216 (5.5.1 opens on p. 200, outside this range). Setting: n units, m treated, no strata; effects of one sign, $r_{Ti} \ge r_{Ci}$ (pp. 202, 204). No constant effect is assumed.

- **Main findings**
  - Binary case: $\delta_i = r_{Ti} - r_{Ci} \in \{0,1\}$; attributable effect $A = \sum_i Z_i \delta_i$, the number of treated responses caused by treatment. A depends on Z, so it is an unobserved random quantity, not a parameter (p. 201).
  - Test of $H_0: \delta = \delta_0$: reject outright if incompatible with the data (a treated unit with R = 0, or a control with R = 1, must have $\delta_i = 0$). Otherwise set $A_0 = \sum Z_i \delta_{0i}$, move $A_0$ from the treated-response cell to the treated-nonresponse cell, and apply Fisher's exact test (p. 202).
  - Confidence statement: if the test rejects exactly when $A_0 < a$, then with the stated confidence at least a treated responses are attributable to treatment (pp. 202-203).
  - Underground example (16/21 dead without pit, 14/32 with): one-sided P = 0.0193 for A = 0, 0.0439 for A = 1, 0.0875 for A = 2, so at 95% at least 2 of 30 deaths (6.7%). At $\Gamma = 1.5$ the upper bounds are 0.0885 (A = 0) and 0.1634 (A = 1) (pp. 203-204).
  - Displacement: fix k and $\theta$ with $r_{C(k+1)} > \theta > r_{C(k)}$; unit i is displaced if $r_{Ti} > \theta > r_{Ci}$; again $A = \sum Z_i \delta_i$ (p. 204). Proposition 22: if $a = \sum_i Z_i \delta_i$ then $R_{(k+1-a)} > \theta > R_{(k-a)}$. So for hypothesised $A_0$, dichotomise observed responses at $R_{(k-A_0)}$ and use the binary method; reject with certainty if $R_{(k+1-A_0)} = R_{(k-A_0)}$ (p. 205).
  - Benzene example (58 exposed, 20 controls, k = 39): P < 0.00001 for A = 1, P < 0.000025 for A = 19, P = 0.219 for A = 25; for $A_0 = 19$ the bounds at $\Gamma$ = 1, 2, 3, 4 are 0.000025, 0.0027, 0.020, 0.058 (pp. 206-207).
  - Quantile: $[\tilde R_{T(a)}, \tilde R_{T(b)}]$ (treated order statistics) covers $r_{T(k)}$ with probability at least $\Upsilon(n,m,k,a,1/\Gamma) - \Upsilon(n,m,k-1,b,\Gamma)$; for controls replace m by n-m (p. 208). Mercury medians (23 vs 16): treated [100,196], [70,236], [69,270]; control [6,11], [6,12], [4,15] at $\Gamma$ = 1, 2, 5 (p. 209).

- **Usable for our paper**
  - Method: A is a valid target without additivity, needing only one-signed effects (pp. 202, 204).
  - Method: the confidence statement inverts the same exact randomization test (pp. 202-203).
  - Robustness: bounds for A come from extended hypergeometric distributions with $\Gamma$ and $1/\Gamma$ (pp. 203, 206).
  - Results-Discussion: report a count of displaced treated dates (p. 204).

- **Caveats**
  - Absent here: any stratified or matched-set version of attributable effects or displacements; 5.6 is stated for no strata, 5.7 for one stratum (pp. 204, 207). The source cited is Rosenbaum (2001) (p. 210).
  - Absent: point estimates, two-sided statements for A, power, mixed-sign effects.
  - $\Upsilon$ is defined in Chapter 4 (Corollary 15), not here. The tail value printed as 0.25 on p. 209 looks like a misprint for 0.025.
  - Our effect is negative; applying the method to the sign-flipped contrast is our adaptation.

- **Checks or analyses it suggests for us**
  - Pool the 20 dates, set k at the control median, test $A_0 = 0, 1, \dots$. Our arithmetic: with n = 20, m = 5, k = 10 the smallest attainable P for $A_0 = 0$ is 252/15504 = 0.016, so only a weak bound is possible.
  - Consult Rosenbaum (2001) before claiming a stratified version.
  - Problem 4 points to additive-effect intervals from differences of order statistics (p. 211).


#### Chapters 6-12 (detecting hidden bias, coherence, planning) - targeted skim

Coverage. Read in full: §6.1-6.6 (pp. 217-238), §8.1-8.4 (pp. 265-281), §9.1-9.2, 9.3.1, 9.4-9.6 (pp. 288-298), all of ch. 11 (pp. 342-369), all of ch. 12 (pp. 376-378). Skimmed: problems of ch. 6, 8, 9. Keyword search only: ch. 7, ch. 10. Not read: lines 8292-8950, which are the end of ch. 5 (pp. 201-216); ch. 6 starts at p. 217. Pages are PDF page markers (printed page is about N-12 in ch. 6, N-9 in ch. 11, not N-13).

- **Data and method**
  - Textbook. Absence of hidden bias = assignment Z uniform over allowed assignments within strata; hidden bias = the ch. 4 model where an unobserved u tilts assignment odds by exp(gamma*u), Gamma = exp(gamma) (pp. 229, 231). Ch. 6-8 detect hidden bias; ch. 9 coherence; ch. 11-12 design advice from three example studies (pp. 345-347).

- **Main findings**
  1. A treated-control difference in an outcome the treatment cannot move, or a difference between two control groups, can only be bias. Small biases are nearly undetectable, large ones detectable; this complements sensitivity analysis (pp. 217-218).
  2. Unaffected outcome y: compute T* = t*(Z, y) and its randomization p-value; a small p is evidence against uniform assignment (p. 226). Power under the bias model: beta(y,u) = sum_z [t*(z,y) >= a] exp(gamma z'u) / sum_b exp(gamma b'u). Proposition 23: power rises as y and u are more strongly ordered alike. So choose a y closely tied to the specific u you fear; y says nothing about u's it does not track (pp. 229-230).
  3. Failure to detect is weak. Not rejecting Gamma = 1 does not reduce the sensitivity of the primary result; one must test, with y, the worst-case point (Gamma, u0) that would overturn the primary finding, and only its rejection helps (pp. 230-231). In the worked example y fitted both no bias and the damaging bias; the ideal y is unaffected yet strongly correlated with the primary response, like a baseline measure (p. 232). Unaffected outcomes should not be adjusted for like covariates (pp. 232-233).
  4. Known direction: if the effect on Y can only be >= 0, a T* in the lower tail of its no-bias null distribution signals bias (pp. 233-234; Proposition 24, p. 235).
  5. Bias of known direction: if bias can only inflate the estimate, a small estimate cannot be blamed on it; the knowledge helps only for claims opposite to the bias. Carries over to confidence intervals and Hodges-Lehmann estimates (pp. 236-238).
  6. Precedents: Athens earthquake, mortality just after the event vs just before and vs the same periods in adjacent years, cancer deaths as unaffected outcome (p. 223); case-crossover, hazard window vs same hours the previous day, with an unaffected control measure (pp. 224-225).
  7. Two control groups. Definition: a unit's response would be the same in either control group (p. 279). Comparing them is a level-alpha test of no hidden bias, with power only if the groups differ systematically in u (delta_j != delta_k), and most power when u is strongly related to control responses (p. 280). Systematic variation: choose control groups that sharply vary the suspected u (p. 276). Bracketing: delta_j > delta_treated > delta_k, one control group above and one below the treated group in u, so effect and bias give different patterns (pp. 276-277, 280). Two control groups help little if plausible biases mimic an effect in both (p. 266). Agreement is only consistent with u not mattering (p. 276); in small samples non-significance means little (p. 272).
  8. A second control group kept out of the first analysis partially replicates an unanticipated pattern, because a theory compatible with many patterns is weakly corroborated by one; only the control half is replicated (pp. 274-275).
  9. Coherence: a detailed pattern of associations matching the treatment theory at many points; unlike detection it targets no specific bias (p. 289). Coherent signed-rank statistic, K outcomes, S pairs: T = sum_k T_k; with w_s = sum_k (c_s1k - c_s2k) q_sk, E(T) = (1/2) sum_s w_s + L and var(T) = (1/4) sum_s w_s^2 under no bias (pp. 291-292). Sensitivity bound: p_s = Gamma/(1+Gamma) if w_s >= 0, else 1/(1+Gamma); E = sum p_s w_s + L, var = sum p_s(1-p_s) w_s^2 (p. 292). Example: separate one-sided p's 0.023 and 0.057, with bounds 0.073 and 0.149 at Gamma = 1.5; coherent test 0.0073, bound 0.026 at Gamma = 1.5 and 0.052 at Gamma = 2 (p. 294). Gains are largest when outcomes are affected similarly and weakly correlated (p. 296).
  10. Limits: coherent biases yield coherent patterns; the combined test is silent on individual outcomes, so per-outcome results and active detection remain necessary (pp. 297-298).
  11. Ch. 11. Pick a setting where the theory acts in isolation, e.g. treatment imposed suddenly at a discrete moment, not influenced by the units (pp. 350-351). Without a control group, state and defend what controls would have looked like; high/low-exposure groups in place of treated/control invite inconsistencies (pp. 351-353). Treatments should be sharply distinct and haphazardly assigned, yet haphazard is not random (pp. 353-354). Use a competing theory to find outcomes where predictions diverge (pp. 356-359). Internal replication: the same treatment delivered by different assignment mechanisms should show similar effects (pp. 360-361). Nondose nonresponse: undelivered potential doses among controls should not predict responses (pp. 361-362). Stability analysis: redo with discrete, innocuous-looking analytic choices changed; adjusting for post-treatment variables can remove effect or add bias; simple designs need fewer such analyses (pp. 362-364). Preferred treatment: single, abrupt, unexpected, short-lived, large; known-in-advance treatments can show effects early (pp. 364-365). Natural blocks pair units alike in unmeasurable ways (pp. 366-367).
  12. Ch. 12: design over elaborate analysis; simple comparisons of comparable units; sensitivity analysis (pp. 377-378).

- **Usable for our paper**
  - Introduction: an abrupt, minutes-long, externally imposed treatment is the favourable case (pp. 351, 365).
  - Method: same cell, year, weekday as natural blocks (pp. 366-367); before and after control dates as bracketing control groups for a monotone trend (pp. 276-277, 280); earthquake and case-crossover designs as precedents (pp. 223-225).
  - Robustness: placebo hours as unaffected outcomes (p. 226); 09h speed-up as known-direction check (pp. 233-235); speed-class gradient on control dates as nondose nonresponse (pp. 361-362); stability analyses (pp. 362-363).
  - Results-Discussion: coherence across speed classes and outcomes strengthens evidence without excluding a coherent bias (pp. 289, 297-298); a quiet placebo is not proof (pp. 230-232); attenuation as bias of known direction, by analogy only (pp. 236-238).

- **Caveats**
  - Absent from ch. 6-12 (searched): multiple testing, pre-specified analysis plans, the term placebo, interrupted time series, time-trend modelling. Before/after appears only in examples and as baseline measures (pp. 219, 297, 353).
  - Nothing new on permutation tests with covariates or covariance adjustment (ch. 10: reference-list entries only). Hodges-Lehmann/confidence intervals: only the p. 238 remark, a problem on p. 239, and p. 293 (no interval for a K-vector from the scalar coherent statistic; test tau = tau0 on R - tau0*Z).
  - Our siren is neither unexpected nor haphazard, so the p. 365 ideal is only partly met. The formal known-direction result concerns assignment bias, not measurement attenuation. Formulas assume independent pairs or strata.

- **Checks or analyses it suggests for us**
  - Choose placebos sharing the feared u (date-specific morning-peak shape): 09h contrast on untreated same-weekday dates, other morning hours; afternoon placebos probably have little power (pp. 229-232).
  - Test before-controls against after-controls (p. 280); report low power.
  - Keep the widened control pool as a held-out second control group (pp. 274-275).
  - Baseline-only contrast ln v(09h) - ln v(08h), since 10h is post-treatment (pp. 232, 363-364); inspect 08h for anticipation (p. 365).
  - One coherent statistic across speed classes or outcomes instead of five tests, plus per-class results (pp. 291-292, 298).
  - Treat any significant 09h speed-up as a bias signal (pp. 233-235).
  - Reader's note, not from the book: check whether 17 Nov controls fall in the school autumn break.


---

### abadie2020 - Abadie, Athey, Imbens and Wooldridge (2020), sampling-based vs design-based uncertainty

Version note: the file in `literature/` is the arXiv v2 working paper (June 2019), not the typeset Econometrica article. Page numbers below are PDF pages of that file (printed page = N - 1); journal pagination differs.

- **Question and setting**
  - What do regression standard errors mean when the sample is a large share of, or the entire, population (all 50 US states, all visits to a website)? The paper's answer: for a causal estimand uncertainty remains, because each unit reveals only one of its potential outcomes, and it derives the large-sample variance of OLS when both sampling and assignment are random (pp. 1-4).

- **Data and method**
  - Theory plus Monte Carlo. This version contains no empirical illustration.
  - Framework: finite population of n units; sampling indicator R_i; potential outcomes Y*_i(.) and attributes Z_i are fixed numbers; only R_i and the cause (X_i, or U_i in the general case) are random (pp. 5-6, 11). A regressor is "causal" if it generates potential outcomes and an "attribute" if held fixed in the repeated-sampling thought experiment; the researcher chooses the designation and the variance depends on it (pp. 10-11).
  - Sampling-based uncertainty = randomness of R; design-based uncertainty = randomness of X (p. 7).
  - Estimands, binary case (p. 6): theta_descr = difference of realized population means by X; theta_causal,sample = (1/N) sum_i R_i [Y*_i(1) - Y*_i(0)]; theta_causal = (1/n) sum_i [Y*_i(1) - Y*_i(0)]. A descriptive estimand is known exactly once all units are observed; a causal one is not (p. 14).
  - Assumptions. Simple example: random sampling, Pr(R = r) = 1/C(n,N), and completely randomized assignment, Pr(X = x | R) = 1/C(n,n_1) (p. 7). General case: A3, assignments jointly independent across units and independent of R, not necessarily identically distributed (p. 11); A4, Bernoulli sampling with rate rho_n -> rho in [0,1] and n*rho_n -> infinity (p. 12); A5, 4+delta moments (p. 13); A7, E[U_i] = B_n Z_i, i.e. mean assignment linear in attributes, automatic under random assignment with an intercept (pp. 15-16); A8, Y*_i(u) = u'theta_i + xi_i, unit-specific (heterogeneous) effects (p. 16); A10, constant effects theta_i = theta (p. 21). Results are asymptotic in n, except the exact binary example.

- **Main findings**
  - Exact variances, binary case (p. 8), with S_x^2 the population variance of Y*(x) and S_theta^2 that of unit effects:
    - V_total = S_1^2/N_1 + S_0^2/N_0 - S_theta^2/(n_0 + n_1) (Neyman's variance)
    - V_sampling = (S_1^2/N_1)(1 - N_1/n_1) + (S_0^2/N_0)(1 - N_0/n_0)
    - V_design = S_1^2/N_1 + S_0^2/N_0 - S_theta^2/(N_0 + N_1)
    - Setting N = n in these formulas gives V_sampling = 0 and V_total = V_design (our substitution).
  - The degrees-of-freedom-adjusted EHW estimator equals Neyman's S-hat_1^2/N_1 + S-hat_0^2/N_0; its expectation is the infinite-population sampling variance, so it overstates the true variance by S_theta^2/n, which cannot be estimated because both potential outcomes are never seen for one unit (pp. 9-10). A simple finite-population correction exists for descriptive but not for causal estimands (p. 5).
  - Theorem 1 (p. 17): under A3-A8 the regression causal estimand is a weighted average of unit effects theta_i with weights E[X_i X_i']. Without A7 it can be nonzero when every unit effect is zero (pp. 17-18).
  - Theorem 3 (p. 19). With Gamma = lim Omega_n^{XX}, Delta_cond = lim (1/n) sum var(X_i e_i), Delta_ehw = lim (1/n) sum E[e_i^2 X_i X_i'], Delta_mu = Delta_ehw - Delta_cond = lim (1/n) sum E[X_i e_i]E[X_i e_i]' >= 0:
    - sqrt(N)(theta-hat - theta_causal) -> N(0, Gamma^{-1}[rho Delta_cond + (1 - rho) Delta_ehw]Gamma^{-1})
    - sqrt(N)(theta-hat - theta_causal,sample) -> N(0, Gamma^{-1} Delta_cond Gamma^{-1})
    - sqrt(N)(theta-hat - theta_descr) -> N(0, (1 - rho) Gamma^{-1} Delta_ehw Gamma^{-1})
    - EHW exceeds the causal variance by rho Gamma^{-1} Delta_mu Gamma^{-1}: exact at rho = 0, conservative for rho > 0 (p. 19).
  - rho = 1 (whole population): the descriptive variance is zero, the causal variance is Gamma^{-1} Delta_cond Gamma^{-1}; here "a descriptive perspective would suggest the standard errors should be zero" (p. 20).
  - Theorem 4 (pp. 21-22): with constant effects the residuals are non-stochastic, Delta_mu = 0, and EHW is correct for theta-hat whatever rho is. The paper calls this the correctly specified case.
  - Corrected estimator (pp. 23-24): X-hat_i = U_i - Lambda-hat Z_i; G-hat = coefficients from regressing X-hat_i e-hat_i on Z_i; Delta-hat_Z = (1/N) sum R_i (X-hat_i e-hat_i - G-hat Z_i)(X-hat_i e-hat_i - G-hat Z_i)'; V-hat_causal,sample = Gamma-hat^{-1} Delta-hat_Z Gamma-hat^{-1}; V-hat_causal = rho-hat V-hat_causal,sample + (1 - rho-hat) V-hat_ehw, rho-hat = N/n (population size must be known). Lemma 3: Delta_cond <= Delta_Z <= Delta_ehw, so it is never larger than EHW and still conservative; it gains only if attributes linearly predict X_i e_i. With stratum dummies as attributes it reduces to within-stratum demeaning (p. 25).
  - Simulations (pp. 25-26, table on p. 40): one normal cause, effects theta_i ~ N(Z_i'psi, sigma_theta^2); Gamma = 1, Delta_ehw = 1 + 3(psi'psi + sigma_theta^2), Delta_cond = 1 + 2(psi'psi + sigma_theta^2), Delta_Z = 1 + 2 psi'psi + 3 sigma_theta^2; 50,000 replications. Whole-population design (n = 1000, rho = 1, psi'psi = 4, sigma_theta^2 = 1): true sd of theta-hat around the causal estimand 0.100, around the descriptive estimand 0.000; mean EHW s.e. 0.121 (coverage 0.982), bootstrap 0.122, corrected s.e. 0.104 (coverage 0.957). Base design (rho = 0.01, E[N] = 1000): sd around causal-sample estimand 0.105, EHW 0.125 (coverage 0.980), corrected 0.108 (0.956). Constant effects: all about 0.032, coverage 0.95.

- **Usable for our paper**
  - Method: observing every cell does not remove uncertainty. The siren effect is a causal estimand: the no-siren 09h contrast on 10 November is unobserved, so the randomness comes from assignment, not sampling (pp. 3-4, 7, 14, 20).
  - Method: name the estimand as the effect for the observed cells and dates (causal-sample type); the paper advises this when the link to a wider population is unclear (p. 20), and separates internal from external validity (p. 9).
  - Method / Robustness: design-based inference rests on the process generating the assignments (p. 3); in our design that process operates on dates, so dates carry the information (our inference from the framework, not a statement in the paper).
  - Robustness: conventional robust standard errors are conservative for causal estimands at rho = 1 and exact under constant effects (pp. 19, 22), valid only under independent assignment across the units used.
  - Literature: design-based uncertainty underlies randomization inference in experiments but is rarely acknowledged in observational regressions (p. 2).

- **Caveats**
  - Every theorem needs assignment independent across units (A3). Our assignment is one draw per date shared by all cells, so the formulas do not apply at cell level. On clustering the paper has one sentence saying such dependence could be allowed, pointing to Abadie et al. (2017); no clustered variance is derived (p. 11).
  - Assignment must be random, or have mean linear in attributes (A7); internal validity is said to rest on random assignment (p. 9). Our date is fixed by the calendar; treating it as drawn among same-weekday dates is our assumption, not something this paper supports.
  - No Fisher sharp-null tests, permutation p-values or comparison of Fisher and Neyman approaches: only Neyman-type variances. The conclusion leaves other settings and hypotheses to future work (p. 27).
  - Nothing on panels, time series, difference-in-differences, serial correlation or interference between units. I could not find any of these.
  - Asymptotic in the number of independently assigned units; no guidance for 5 treated dates.

- **Checks or analyses it suggests for us**
  - Collapse to one observation per date (cell-averaged contrast) and compute the date-level Neyman variance S-hat_1^2/N_1 + S-hat_0^2/N_0 with year dummies as attributes (p. 25); compare with the randomization p-value. With one treated date per year the treated variance must be pooled across years (our remark).
  - Report the naive cell-level robust s.e. next to the date-level one to show how much ignoring the shared assignment understates uncertainty.
  - Check effect heterogeneity across years: under constant effects the Neyman/EHW variance is exact (p. 22), otherwise conservative (p. 19).
  - State explicitly that sampling uncertainty is zero (rho = 1) and that reported uncertainty is conditional on the assumed assignment mechanism.


---

## Cross-paper synthesis (what jointly matters most for our design)

1. Our test is a blocked randomization test in Rosenbaum's sense: years are strata, one of n_s dates is treated, K = prod C(n_s, 1) = 4^5 = 1024 assignments, exact p = (number of assignments with statistic >= observed)/K (book p. 37, 41; article p. 15-16). It is exact only if assignment within a year is uniform. Smallest attainable p is 1/1024.
2. That uniformity is an assumption for us, not a fact: the date is fixed by the calendar, and the book's model needs 0 < pi < 1 (book p. 90). We should state the premise as "untreated contrasts are exchangeable across the candidate dates within a year" and say that a within-window trend (Nov 10 always 2nd of 4) is precisely a violation of it. None of the three sources treats calendar-fixed treatments, trends or interrupted time series.
3. Report an effect size with the test: Hodges-Lehmann estimate and test-inversion interval (book p. 56-61; article p. 4, 10), converted to minutes. Both assume a constant additive log-point effect across years. If the effect varies by year the sharp-null test stays valid; attributable-effect statements need only one-signed effects but the book gives them for unstratified designs only (book p. 201-207).
4. Weather adjustment: align by year, subtract the hypothesised effect, regress on aligned covariates, permute residuals (article p. 4-5, 16). With OLS and a mean statistic this equals the fixed-effects regression coefficient. Adjustment buys precision, never validity. Book Sections 3.4-3.6 adjust by modelling assignment instead, which is not our case.
5. Sensitivity analysis is the honest answer to non-random dates. With one treated among n_s the worst-case chance that a given date is the treated one is Gamma/(Gamma + n_s - 1) (book (4.17), p. 133). For 5 x (1 of 4) the worst-case p is at least (Gamma/(Gamma+3))^5, so nothing survives beyond Gamma = 3.66 (own derivation); a crude union bound guarantees robustness up to Gamma = 1.70 for p = 0.008 and 1.11 for p = 0.034 (own derivation; exact values need enumeration). Benchmarks: coffee-infarction sensitive at 1.3, smoking-lung cancer near 6 (book p. 125-126, 140-141; article p. 40). Widening the control pool raises the attainable Gamma.
6. Observing every Istanbul cell does not remove uncertainty (abadie2020): with sampling fraction rho = 1 the remaining variance is design-based, and robust standard errors are conservative unless effects are constant (their Theorems 3-4, p. 19-22). But their theorems need assignment independent across units; ours is one assignment per date shared by all cells. So the paper supports "uncertainty remains" and "dates are the units", not cell-level standard errors.
7. Detecting bias: a placebo outcome only detects biases it tracks, and a quiet placebo does not reduce sensitivity (book p. 229-232); control dates before and after 10 Nov bracket a monotone trend and comparing them is a valid, low-power bias test (book p. 276-280); a coherent pattern across outcomes can be less sensitive to bias than separate tests (book p. 291-298).
8. Correction to our design notes: the 10h hour in the reference mean is post-treatment (queues may persist), so a baseline-only contrast ln v(09h) - ln v(08h) should be shown, and 08h checked for anticipation (book p. 232, 363-365).
9. Not covered by this group and needed elsewhere: multiple testing over 5 speed classes, spatial correlation of cells (handled here only by aggregating to dates), trend modelling. The Angrist-Imbens comment (article p. 21) is the only support in this group for randomization inference with few aggregate treated units.
10. Reporting plan: (i) exact p with K stated, (ii) HL estimate and inverted interval in minutes, (iii) residual-permutation with weather, (iv) Gamma table with benchmarks, (v) before-vs-after control comparison and baseline-only contrast, (vi) explicit statement of the exchangeability premise.
