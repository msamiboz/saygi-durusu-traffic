# 05 Synthetic control and placebo (permutation) inference

Reader notes for five papers: abadie2010, abadie2015, abadie2021, firpo2018, chernozhukov2021.
Page numbers are the `=== page N ===` markers of `literature/txt/<key>.txt`.
For chernozhukov2021 the file is the arXiv version (v10, 102 pages), so page N here is not a JASA page.
Read in full: abadie2010, abadie2015, abadie2021 (main text; reference list skimmed), firpo2018, chernozhukov2021 pp. 1-32 (main text), 40-48 (tables, appendices A-D), 54-56 and 97-102 (simulations). Skimmed only: chernozhukov2021 appendices E, F, H (stability conditions and proofs).

Labels used below: **[paper]** = stated in the paper; **[mine]** = my own mapping, algebra or inference, not in the paper.

Mapping vocabulary for our design **[mine]**:

| Synthetic-control term | Our design |
|---|---|
| treated unit | 10 November (one per year) |
| donor pool / placebo units | same-weekday dates of the same year (Nov 3, 17, 24; being widened) |
| post-intervention period | the 09h hour (or the 09:05-09:10 bins in the 5-minute index) |
| pre-intervention periods | the other hours of the same day (08h, 10h; more with the 5-minute index) |
| in-space placebo | pretend another date is the siren date |
| in-time placebo | pretend the siren sounded at another hour of 10 November |
| multiple treated units / pooled interventions | the five years 2020-2024 |

Note that "space" and "time" are swapped relative to everyday language: our dates play the role of units, our hours play the role of time.

---

### abadie2010 - Abadie, Diamond & Hainmueller (2010), Synthetic control methods and California's Proposition 99

- **Question and setting.** How much did California's 1988 tobacco control programme (Proposition 99) lower per-capita cigarette sales, and how can one do inference when one aggregate unit is treated and regression standard errors are uninformative?

- **Data and method.**
  - Annual state panel 1970-2000, 19 pre-intervention years (p. 6). Outcome: per-capita cigarette sales in packs. Donor pool: 38 states, after dropping states with their own tobacco programmes or tax rises of 50 cents or more, and DC (pp. 6-7).
  - Synthetic California = convex combination of donor states (weights >= 0, sum to 1) chosen to match pre-1988 predictors and lagged outcomes (pp. 3-4). The motivating factor model `Y^N_it = delta_t + theta_t Z_i + lambda_t mu_i + eps_it` nests difference-in-differences as the case of constant `lambda_t` (p. 3).
  - Inference (Section 2.4, pp. 4-5; Section 3.4, pp. 9-11): apply the same estimator to every donor state as if it were treated (California moves into the donor pool), and compare California's gap with the distribution of placebo gaps. Two ways to deal with badly fitted placebo units: (a) drop placebo states whose pre-period MSPE exceeds a multiple of California's; (b) use the ratio post-MSPE / pre-MSPE as the statistic, which needs no cut-off (p. 11).

- **Main findings.**
  - Sales about 26 packs per capita lower by 2000 (p. 1); on average almost 20 packs lower over 1989-2000, about 25% (p. 8); about 24 packs by 1997, against 14 in an earlier regression study (p. 9).
  - Pre-period MSPE: California about 3, donor median about 6, New Hampshire 3437 (pp. 9-10).
  - Trimming placebo states at 20x, 5x and 2x California's pre-MSPE leaves 34, 29 and 19 control states (pp. 10-11). With 19 controls California is the most extreme, so p = 1/20 = 5% (p. 11).
  - Post/pre MSPE ratio: California about 130, the largest of 39, so p = 1/39 = 0.026 (p. 11).

- **Usable for our paper.**
  - *Method:* the placebo procedure is the source to cite for "apply the identical estimator to each placebo unit and rank the treated unit" (pp. 4-5, 9). The paper calls it exact in the sense that the placebo distribution can always be computed, whatever the number of units or periods (p. 5).
  - *Method:* it equals classical randomization inference only if the intervention is randomly assigned, which the authors call restrictive; otherwise it answers whether the treated unit's estimate is large relative to the placebo distribution, and that is informative if, under no effect, the treated unit would not be expected to be unusual (p. 5). This is the honest wording for our test.
  - *Method / Introduction:* conventional standard errors in case studies measure only sampling noise in the aggregates and would be zero with complete aggregate data; the real uncertainty is whether the comparison group reproduces the counterfactual (pp. 4-5). This supports "effective sample = dates, not cells": the cell-level `se` we compute within a date is exactly the kind of standard error they call uninformative **[mine]**.
  - *Method:* the paper already mentions placebos along the time dimension for cases with very few comparison units, citing Bertrand, Duflo & Mullainathan (2004) and Heckman & Hotz (1989) (p. 5).
  - *Robustness:* the post/pre ratio as a statistic that removes the need to choose which placebo units to discard (p. 11).
  - *Data:* build the donor pool by excluding units hit by similar interventions; contaminated donors attenuate the estimate (pp. 6-7, 9). Our analogue: exclude dates with their own disruption (public holidays, school breaks, curfew days, other remembrance sirens) **[mine]**.
  - *Method:* design choices can be fixed without looking at post-intervention outcomes (p. 2), an argument for fixing the placebo-date pool before estimating.

- **Caveats.**
  - The statistic is the ratio of mean squared prediction errors (MSPE), not RMSPE; the square-root version appears in abadie2015 and abadie2021. The ranking, and so the p-value, is the same.
  - The p-value resolution is 1/(J+1). The paper's own two answers (0.05 after trimming, 0.026 with the ratio) show how much the pool definition matters.
  - No confidence intervals, no treatment of multiple outcomes, no formal validity result outside random assignment.
  - Our earlier note credits abadie2015 with introducing in-time placebos. This paper already points to them (p. 5). It does not use them.
  - The paper is about choosing weights for a counterfactual. We use equal weights over control dates, so only the inference part transfers directly.

- **Checks it suggests for us.**
  - Report the full placebo distribution (a plot of all date-level estimates with Nov 10 marked), not only the p-value, as in their Figures 4-8.
  - Build a ratio statistic per date: |09h contrast| divided by the RMS of the same contrast computed at non-siren hours of that date, then rank Nov 10 (details under abadie2021).
  - Do not trim placebo dates by hand after seeing results; if some dates are implausible controls, exclude them by a rule fixed in advance (holiday calendar), or use the ratio statistic.

---

### abadie2015 - Abadie, Diamond & Hainmueller (2015), Comparative politics and the synthetic control method

- **Question and setting.** Economic cost of the 1990 reunification for West Germany, used to present synthetic control and placebo studies to comparative-politics readers.

- **Data and method.**
  - Country panel 1960-2003, 30 pre-intervention years; donor pool of 16 OECD countries after excluding countries with structural shocks or atypical economies (p. 7 and footnote 14).
  - Predictor weights chosen by cross-validation: training 1971-80, validation 1981-90 (pp. 7-8).
  - RMSPE defined as the root of the mean squared gap between a unit and its synthetic control over a set of periods (footnote 16, p. 8).
  - Two placebo designs, named here (pp. 5-6): **in-time placebos** (reassign the intervention to a date when it did not happen) and **in-space placebos** (reassign it to donor units). A p-value is defined for the in-space version: the share of units whose effect is at least as large as the treated unit's (p. 6).

- **Main findings.**
  - GDP per capita lower by about 1,600 USD per year on average over 1990-2003, roughly 8% of the 1990 level; synthetic West Germany about 12% higher than actual in 2003 (pp. 2, 10).
  - In-time placebo: reunification reassigned to 1975 shows no divergence over 1975-90 (pp. 10-11); 1970 and 1980 give similar results (footnote 18, p. 11).
  - In-space placebo with post/pre RMSPE ratio: West Germany's ratio is about 16, the largest of 17, so p = 1/17, about 0.059 (p. 11).
  - Leave-one-out over donors with positive weight: smallest effect when the United States is dropped, about 630 USD per year, about 3% (p. 12).
  - Regression implicitly uses weights that sum to one but can be negative (four of 16 here), which is extrapolation (pp. 4-5, 8).

- **Usable for our paper.**
  - *Method:* the vocabulary "in-space" and "in-time" placebo (pp. 5-6). In our mapping, ranking Nov 10 against other dates is formally the in-space test (dates are the units); the siren-hour-versus-other-hours check on Nov 10 is the in-time placebo **[mine]**.
  - *Method:* the p-value definition and its interpretation without randomization: the probability of an estimate at least this large when the intervention is reassigned at random within the data (p. 6).
  - *Robustness:* in-time placebos need enough periods free of structural shocks (p. 5). For us: non-siren hours that are not themselves rush-hour transitions **[mine]**.
  - *Robustness:* RMSPE ratio avoids discarding badly fitted placebo units (p. 11, footnote 19); leave-one-out over comparison units (p. 12).
  - *Data:* rules for the donor pool: drop units affected by similar events, drop units with large idiosyncratic shocks, keep units similar to the treated one (p. 6). This is the reference for a principled holiday/exclusion rule when we widen the date pool.
  - *Method:* footnote 23 (p. 13) notes that a single-comparison version is close to a difference-in-differences design; our equal-weight control-date mean is the "simple average of the donor pool" case.

- **Caveats.**
  - The authors state that these procedures give no confidence intervals or posterior distributions and only address whether the effect is large relative to the placebo distribution (p. 6).
  - The in-time placebo here is a falsification check at one to three dates, read off a figure. No p-value is computed over time. Our earlier note says the in-time placebo is "what our placebo dates are" and that the rank p-value over dates "is the same logic". The logic is analogous, but a rank p-value over placebo dates is not something this paper does; the formal references for permuting over time are chernozhukov2021 and the Andrews-type test described in abadie2021 (p. 31).
  - They advise against the method when pre-period fit is poor or pre-periods are few (p. 6). With only 08h and 10h as "pre-periods" in the hourly data, any fit-based statistic would be weak **[mine]**.
  - Minimum p with 17 units is 0.059; the paper treats that as significant given the sample, which is a judgment, not a rule.

- **Checks it suggests for us.**
  - In-time placebo on Nov 10: run the full pipeline with the "event hour" set to hours other than 09h (for example 07h, 11h, 14h, 15h), each with its own neighbour-hour baseline. No effect should appear.
  - Leave-one-control-date-out and leave-one-year-out versions of the main estimate.
  - Report the count of years in which Nov 10 is the most extreme date, alongside the pooled p-value.

---

### abadie2021 - Abadie (2021), Using synthetic controls: feasibility, data requirements, and methodological aspects

- **Question and setting.** A practitioner's review: when synthetic control is credible, what the context and data must satisfy, how to do inference and robustness checks, and what the recent extensions are. Running example: German reunification.

- **Data and method (what the paper sets out).**
  - Estimator: `tau_hat_1t = Y_1t - sum_j w_j Y_jt`; equal weights `w_j = 1/J` give the simple-average comparison (eq. 4, p. 5).
  - Permutation inference (Section 3.5, pp. 13-15). For unit j and periods t1..t2:
    `R_j(t1,t2) = sqrt( (1/(t2-t1+1)) * sum_{t=t1}^{t2} (Y_jt - Yhat^N_jt)^2 )` (eq. 11),
    `r_j = R_j(T0+1, T) / R_j(1, T0)` (eq. 12),
    `p = (1/(J+1)) * sum_{j=1}^{J+1} 1{ r_j >= r_1 }` (p. 13).
  - One-sided version: replace the gaps in the post-period RMSPE by their positive or negative parts (p. 14).
  - Confidence intervals by test inversion, citing Firpo & Possebom (pp. 13-14).

- **Main findings / statements.**
  - The ratio `r_j` is introduced because a synthetic control may fit the treated unit well but fit some donor units badly; the alternative is to drop placebo runs with pre-period RMSPE much larger than the treated unit's (p. 13).
  - One-sided inference can raise power considerably, which matters in small samples (p. 14). Footnote 10 (p. 14): when the treated unit is part of a placebo unit's comparison group, a real effect pushes the placebo estimates the opposite way, which raises one-sided power.
  - The test equals Fisher randomization inference only under random assignment, described as improbable for aggregate units. In general it measures significance against a benchmark assignment distribution, uniform by default; departures from uniform can be explored as in Firpo & Possebom (p. 14).
  - In many case studies it is hard even to say what a placebo intervention would be, and the assignment mechanism cannot be estimated with one treated unit (p. 14).
  - The permutation test is design-based: it conditions on the sample and uses only variation from assignment; it does not approximate a sampling distribution (pp. 14-15).
  - Contextual requirements (pp. 18-22): the effect must be large relative to unit-specific volatility; volatility from common factors is differenced out by a good comparison (pp. 18-19). Averaging over many instances reduces volatility (footnote 13, p. 19). A comparison group free of similar interventions and of large idiosyncratic shocks (p. 19). No anticipation; backdating the intervention does not bias the estimate because effects may vary by period (pp. 19-20). No interference, with a tension between closeness and spillovers (p. 20). Differencing the outcome helps when levels cannot be matched but raises the noise variance if shocks are serially independent (pp. 21-22).
  - Diagnostics (pp. 24-25): backdating (the in-time placebo; reunification backdated to 1980 still shows the gap opening around 1990) and leave-one-out.
  - Several treated units (pp. 25-28): estimate unit by unit, then aggregate. Abadie & L'Hour's permutation test reassigns the set of treated units and uses the sum of the ranks of the treated units' statistics (p. 28).
  - Other inference (pp. 31-32): Andrews' end-of-sample instability test compares the post-period effects with the same quantity for every block of consecutive pre-periods of equal length; Chernozhukov, Wüthrich & Zhu permute residuals over time and estimate the weights under the null using all periods.
  - Results on sampling-based inference and sensitivity to model restrictions are described as scarce (p. 33).

- **Usable for our paper.**
  - *Method:* exact formulas for the RMSPE ratio and the p-value (p. 13); one-sided test by negative parts (p. 14). These justify our one-sided test and give the template for a ratio statistic.
  - *Method:* the "benchmark assignment distribution" reading (p. 14) is the wording to use instead of claiming that the siren date was randomized. Unlike the reunification example, our placebo intervention is easy to state (a siren at 09:05 on another same-weekday date), which is a point in favour of our design **[mine]**.
  - *Method:* design-based framing when the sample is the population (pp. 14-15): we observe essentially all cells of the city, so sampling-based standard errors over cells answer the wrong question.
  - *Results-Discussion:* "size of the effect and volatility" (pp. 18-19) is the reference for the hourly-dilution problem: a 1-2 minute stop inside a 60-minute mean is small relative to date-to-date noise, and is detectable only because noise is averaged over cells and years (footnote 13) **[mine for the application]**.
  - *Data / Robustness:* donor-pool rules (p. 19) and the in-time placebo / backdating and leave-one-out diagnostics (pp. 24-25).
  - *Method:* footnote 10 (p. 14) applies exactly to us. Our DiD for a placebo date uses Nov 10 as one of its controls. With 4 dates the four DiDs in a year sum to zero, so `DiD_d = (4/3)(c_d - cbar_year)` and the placebo DiDs are shifted by minus one third of the Nov 10 DiD. The pilot table confirms this: `placebo_mean = -did/3` in every class **[mine, checked against pilot/saygi/results_summary.csv]**. Consequences: (i) the permutation p-value is the same as ranking the raw contrasts `c_d`; (ii) for test inversion the hypothesized effect must be removed from the Nov 10 contrast before DiDs are recomputed, not subtracted from the DiD column.
  - *Method:* the rank-sum statistic for several treated units (p. 28) is an alternative to our equal-weight mean over years that is insensitive to one noisy year.
  - *Literature:* p. 31 is where to cite the link between ranking a period against other periods and Andrews' end-of-sample test.

- **Caveats.**
  - The paper does not use the word "studentization". The stated purpose of the ratio is to handle placebo units with poor pre-period fit (p. 13). Calling it studentization is our gloss; say "scaled by pre-period fit".
  - Our earlier note says the paper "suggests normalizing by the RMS of non-siren-hour contrasts". It does not; that is our analogue of `R_j(1,T0)`.
  - The paper is frank that random assignment is not credible in typical applications. We should not cite it for exactness of our p-value under a "random date" story without the benchmark qualification.
  - Bias results (pp. 9-11) concern estimated weights under a factor model and are not relevant to an equal-weight contrast.
  - The warning that a larger donor pool raises over-fitting risk (p. 11) is about weight estimation. It does not argue against widening an equal-weight pool of dates, but the similarity requirement (p. 19) does limit how far from November we should go **[mine]**.

- **Checks it suggests for us.**
  - Ratio statistic: for each (year, date), `r = neg_part(DiD at 09h) / RMS over placebo hours h of DiD at h`, where each placebo hour uses its own neighbour-hour baseline; rank Nov 10 within year and combine over years. With the 5-minute index, use `R(post)` over the 09:05-09:10 bins and `R(pre)` over, say, 07:00-09:00.
  - Rank-sum over years: statistic = sum over years of the within-year rank of Nov 10's contrast; permutation distribution over the same 4^5 (or wider) assignments. Compare with the mean-based p-value.
  - Backdating analogue: shift the "event hour" to 08h (one hour early). The estimate at 08h should be nil and the effect should still appear at 09h.
  - Leave-one-date-out and leave-one-year-out.
  - State the exclusion rule for the widened pool before computing (holidays, eve of holidays, school breaks, 2020-21 curfew days, days with missing hours).

---

### firpo2018 - Firpo & Possebom (2018), Synthetic control method: inference, sensitivity analysis and confidence sets

- **Question and setting.** Extends the Abadie et al. placebo test in three directions: sensitivity of the p-value to unequal assignment probabilities, tests of any sharp null with confidence sets by inversion, and versions for several outcomes or several treated units. Illustrated with the Basque Country terrorism data.

- **Data and method.**
  - Baseline: statistic `RMSPE_j` = post-period mean squared gap over pre-period mean squared gap (eq. 4), `p = (1/(J+1)) sum_j 1{RMSPE_j >= RMSPE_1}` (eq. 5), null of no effect for any unit in any period (eq. 6) (p. 6).
  - **Sensitivity analysis** (Section 3, pp. 6-8). General p-value `p = sum_j pi_j 1{RMSPE_j >= RMSPE_1}` (eq. 7) with parametric weights
    `pi_j(phi, v) = exp(phi * v_j) / sum_j' exp(phi * v_j')`, `phi >= 0`, `v_j in {0,1}` (eq. 8).
    `phi = 0` is the equal-weight benchmark. Worst case after a rejection: set `v_j = 1` for every assignment whose statistic is at least as large as the observed one, and find the `phi` at which the p-value reaches the significance level `gamma` (step 6, p. 7). Best case after a non-rejection: the reverse (step 7, pp. 7-8). A unit with `v = 1` then has weight `exp(phi)` times that of a unit with `v = 0`; the paper reports this as a percentage increase (`phi = 0.495` read as 64% larger, p. 21). Modelled on Rosenbaum and on Cattaneo et al. (p. 2).
  - **Sharp nulls and confidence sets** (Section 4, pp. 8-11). Null `Y^I_jt = Y^N_jt + f(t)` for all units (eq. 11). Statistic `RMSPE^f_j` subtracts `f(t)` from the gap (eq. 12); p-value `p^f(phi, v)` (eq. 13). Confidence set `CS = { f : p^f(phi, v) > gamma }` (eq. 14). Practical subsets: constant effect `c * 1(t > T0)` (eqs. 15-16) and linear effect `c~ * (t - T0)` (eqs. 17-18).
  - **Other statistics and Monte Carlo** (Section 5, pp. 11-16). Five statistics: mean absolute post gap; RMSPE ratio; a t-type statistic on the post-period gaps; difference in means; permuted DiD coefficient. Design: J+1 = 20, T = 25, T0 = 15, 3,000 data sets for each of 7 effect sizes, 10% level (pp. 12-13).
  - **Several outcomes** (Section 6.1, pp. 16-18): a familywise-error procedure adapted from Anderson, based on the permutation distribution of the minimum p-value across outcomes, with a monotonicity step (eq. 24). Each post-period can be treated as an outcome.
  - **Several treated units** (Section 6.2, pp. 18-19): G interventions, each with its own `J_g + 1` units; pooled effect = average over g; a placebo assignment picks one unit in each intervention, giving `Q = prod_g (J_g + 1)` assignments; weights and p-value over these Q assignments (eq. 26).

- **Main findings.**
  - All five permutation statistics have correct size 0.10 (Table 1, p. 13).
  - Power at effect sizes 0.05 to 2.0: RMSPE ratio 0.32-0.77; permuted DiD 0.18-0.70; difference in means 0.20-0.65; mean absolute gap 0.19-0.68; t-type statistic 0.63-0.95 (Table 1, p. 13). The t-type statistic loses power if effects of opposite sign cancel over time (p. 14).
  - Dropping placebo units with pre-MSPE above 5x the treated unit's changes size: 0.13 for the mean absolute gap, 0.06 for the ratio and t-type statistics, and lowers the ratio's power (Table 2, pp. 14-15).
  - Average worst-case `phi` after a rejection: 0.38 under a true null, 0.60-0.75 under alternatives for the ratio and t-type statistics (Table 3, p. 16). The t-type statistic behaves badly in the best-case analysis (p. 15).
  - Basque application (J+1 = 17, pp. 19-23): one-sided t-type statistic gives p = 3/17; keeping units with good pre-fit gives p = 2/14; worst-case `phi = 0.495` at level 3/14, judged small against 0.995 from a simulation matched to that design (pp. 16, 21). One-sided 12/14 confidence sets, because a 90% set needs at least 20 units (footnote 30, p. 21). A quadratic effect path is not rejected (p = 6/14, `phi = 1.905`, p. 22). Year-by-year familywise p-values of 4/14 in the 1980s (p. 23). Overall verdict: a negative, marginally significant effect that is neither robust nor permanent (p. 23).
  - Discreteness means usual levels may be unattainable, so the level must be chosen and reported with care (footnote 8, p. 6).

- **Usable for our paper.**
  - *Method:* Section 6.2 (pp. 18-19) is a published statement of exactly our assignment space: one treated unit per intervention, placebo assignments formed by choosing one unit in each, `Q = prod (J_g + 1)`. With 5 years and 4 dates this is 4^5 = 1024. Cite it (with their source, Cavallo et al.) for the stratified structure and the pooled mean statistic.
  - *Method / Results:* confidence sets by test inversion under a constant effect (eqs. 15-16, p. 10), one-sided upper bound as in their application (p. 20, footnote 26).
  - *Robustness:* the sensitivity analysis. From eq. 9, if k of N assignments have a statistic at least as extreme as the observed one (k includes the observed), the worst-case p-value is `p(phi) = k e^phi / (k e^phi + N - k)`, so the tilt that brings it to level gamma is `e^phi = gamma (N - k) / (k (1 - gamma))` **[mine; reproduces the paper's Basque value: N = 14, k = 2, gamma = 3/14 gives phi = 0.49, and its simulation cap: N = 20, k = 1, gamma = 0.1 gives 0.747]**.
    Applied to the pilot **[mine]**:

    | Class | k / 1024 | phi to lose 5% | phi to lose 1% (Bonferroni over 5) |
    |---|---|---|---|
    | 50-70 km/h | 8 | 1.90 (odds 6.7) | 0.25 (odds 1.28) |
    | 30-50 km/h | 35 | 0.40 (odds 1.49) | already above 1% |
    | all cells | 56 | not rejected at 5%; best-case phi = 0.10 would reject | - |

    So the 50-70 result is robust as a single test but fragile once multiplicity is imposed.
  - *Robustness:* Section 6.1 (pp. 16-18) gives a permutation min-p familywise procedure that can be run on our speed classes with the same 1024 assignments, and notes that a single summary statistic has more power than the familywise route (p. 18). It also recalls that validity needs the statistic to be chosen before seeing the data (p. 16).
  - *Method:* Table 2 (p. 14) is evidence against trimming placebo units by fit after the fact; use a ratio statistic instead.
  - *Robustness:* Table 1 (p. 13): a permuted DiD statistic (ours) has correct size but less power than fit-based statistics in their design. This motivates trying a ratio or synthetic-weight statistic, not a claim that ours is invalid.

- **Caveats.**
  - The sensitivity analysis is a device, not a theorem; the paper gives no validity result for the weighted p-value and no guidance on what `phi` is plausible beyond design-specific simulations (pp. 15-16).
  - Benchmarks for a "large" `phi` do not transfer. In their N = 20 design `phi` cannot exceed 0.747 at the 10% level; with N = 1024 much larger values are attainable **[mine]**.
  - The tilt applies to the set of assignments at least as extreme as the observed one. In the pooled case these are whole assignment vectors (p. 19), not "Nov 10 is more likely in each year". Our earlier note describes the check as "how much more likely Nov 10 would have to be selected"; that per-year, Rosenbaum-style version is an adaptation of ours, not the paper's procedure.
  - Eq. 12 subtracts `f(t)` from the gap of whichever unit is treated as the event unit. The paper does not spell out re-imputing the actual treated unit's outcome when it serves as a control in a placebo run. For our design the clean Fisher version is to subtract the hypothesized effect from the Nov 10 contrast and then recompute everything **[mine]**.
  - Confidence sets assume an effect that is constant across units (for us: across years) and of a chosen shape in time; attainable confidence levels are limited to multiples of 1/N.
  - Monte Carlo design: autoregressive data with time-varying coefficients and an effect growing linearly in time, random assignment. Power rankings need not carry over to a one-hour effect on a within-day contrast.
  - Nothing here addresses serial dependence across dates or permutation over time.

- **Checks it suggests for us.**
  - Report `phi` (and `exp(phi)`) for each headline p-value, at 5% and at the multiplicity-adjusted level, with the p(phi) curve as in their Figure 2.
  - Also compute a per-year tilt: give Nov 10 probability `G/(G+3)` in each year instead of 1/4, recompute the p-value as a weighted sum over the 1024 assignments, and report the G at which significance is lost. Label it as our adaptation.
  - Invert the test over a grid of constant log-contrast effects; report the one-sided 95% upper bound in full-stop-equivalent minutes via `60(1 - exp(tau))`; repeat at the worst-case `phi`.
  - Test the sharp nulls "effect equals a 1-minute stop" (`tau = ln(59/60) = -0.0168`) and "2-minute stop" (`-0.0339`).
  - Run the min-p familywise procedure over speed classes; pre-declare one summary statistic as primary.
  - A small simulation calibrated to our date-level data to see what `phi` values arise under no effect (as they do on p. 16).

---

### chernozhukov2021 - Chernozhukov, Wüthrich & Zhu (2021), An exact and robust conformal inference method for counterfactual and synthetic controls

- **Question and setting.** Inference on the effect of an intervention on a single treated unit observed for T0 periods before and T* periods after, by permuting residuals over time instead of permuting treatment over units.

- **Data and method.**
  - Model (Assumption 1, pp. 8-9): `Y^N_1t = P^N_t + u_t`, `Y^I_1t = P^N_t + theta_t + u_t`, `E u_t = 0`, with `{u_t}` stationary and its distribution unaffected by the intervention. `P^N_t` is a counterfactual proxy from any of several models: difference-in-differences `P_t = mu + (1/J) sum_j Y_jt` (p. 12), synthetic control, constrained lasso, factor models, or a pure time-series model with no control units (pp. 16-17).
  - Sharp null `theta = theta^0` over the post period (p. 10). Impose it (subtract `theta^0_t` from the treated outcomes), estimate `P^N` on all T periods, form residuals `u_hat`.
  - Statistic `S_q(u_hat) = ( T*^{-1/2} sum_{t > T0} |u_hat_t|^q )^{1/q}`; q = 1 used in the application; large q for short-lived effects (pp. 10-11). Other statistics are allowed (Remark 1, p. 11).
  - Permutations (p. 11): all permutations ("iid", `Pi_all`), or moving-block permutations `Pi_->`, which are the T cyclic shifts `pi_j(i) = i + j (mod T)`. Shuffling of non-overlapping blocks is mentioned only in footnote 6.
  - p-value `p_hat = 1 - F_hat(S(u_hat))`, `F_hat(x) = |Pi|^{-1} sum_pi 1{ S(u_hat_pi) < x }` (eq. 2, p. 12). Pointwise confidence intervals by inversion over a grid (Algorithm 1, p. 12).
  - Extensions: average effects by collapsing into non-overlapping blocks of length T*, with effective sample T/T* (pp. 42-43); several treated units by averaging them (pp. 43-44); placebo tests that treat the last tau pre-periods as post (pp. 44-45).

- **Main findings.**
  - Exactness (Theorem D.1, p. 47): if the data are iid or exchangeable under the null and the estimator does not depend on the order of the data, the residuals are exchangeable and `P(p_hat <= alpha) <= alpha`, with `alpha - 1/|Pi| <= P(p_hat <= alpha)` under continuity. This holds whatever the model, including misspecified ones. Order-invariance holds for regression-type proxies (DiD, synthetic control) when the null is imposed, and can fail for autoregressive models.
  - Approximate validity 1 (Theorem 1, p. 19): with consistent estimation of the proxy and shocks that are iid (for `Pi_all`) or stationary and strongly mixing (for `Pi_->`), `|P(p_hat <= alpha) - alpha| <= C( (T*/T0)^{1/4} log T + delta_T + sqrt(delta_T) + gamma_T )`. T0 must be large relative to T*.
  - Approximate validity 2 (Theorem 2, p. 22): with a misspecified but stable estimator, valid for `Pi_->` if the data themselves are stationary and beta-mixing.
  - Limits: the shock process may be conditionally but not unconditionally heteroskedastic; otherwise standardize first (Remark 2, p. 19). "allowing for both unrestricted patterns of non-stationarity and misspecification is not possible in general" (p. 23).
  - Identification rests on the shock distribution not changing with the intervention; if it does, the test is a structural-break test of "no change at all" (pp. 9, 45-46), or the sets are prediction sets for a random effect (pp. 46-47).
  - Simulations (pp. 54-56, 97-100), nominal 10%, T* = 1, moving-block permutations: iid data give 0.09-0.11 in every design, including misspecified ones (Table I.1); AR(0.6) errors give 0.09-0.13 (Table I.2); with a trending factor, correctly specified models stay near 0.10 but misspecified DiD rejects 0.33-0.97 of the time and misspecified synthetic control up to 0.98 (Tables I.3-I.4). Estimating the proxy on pre-period data only, without imposing the null, distorts size at T0 = 19 (Figure 1, pp. 4, 101).
  - Application (Rhode Island, T0 = 19, T* = 6, J = 50; pp. 31-32, 40-41): zero-effect null p = 0.08 / 0.04 / 0.08 with moving blocks and 0.01 / 0.03 / 0.01 with iid permutations for DiD / synthetic control / constrained lasso (Table 2). Pre-period placebo tests cast doubt on the DiD proxy (p = 0.03 at tau = 3 with iid permutations, Table 1).
  - iid permutations give finer p-values and allow lower levels than moving blocks (p. 11). With T = 25 the moving-block floor is 1/25 = 0.04, which is the synthetic-control value reported **[mine]**.
  - The authors recommend always running the placebo tests, and note that these cannot check invariance of the shocks to the intervention (pp. 44-45).

- **Usable for our paper.**
  - *Method:* an alternative justification for ranking Nov 10 among placebo dates that does not need an "as if random date" story: treat the within-year sequence of same-weekday contrasts as a time series, model `c_t = P_t + u_t`, and require the shocks to be stationary and weakly dependent and unaffected by the siren (pp. 8-9, 18-19).
  - *Method:* with one treated period (T* = 1), `S` under any cyclic shift or any permutation is just `|u_hat_t|` for some date t, so the p-value is the rank of Nov 10's absolute residual among all dates' residuals, with floor 1/T. In this case moving-block and iid permutations give the same p-value, and the test coincides with our "rank against all same-weekday dates of the year" design **[mine]**.
  - *Method:* our estimator already "imposes the null" in their sense. `DiD_d` is proportional to the date's deviation from the year mean of all dates including Nov 10, an order-invariant estimator, so Theorem D.1 (p. 47) gives exact size if the dates of a year are exchangeable under the null **[mine]**. Their Figure 1 (p. 4) is the citation for why not to estimate the baseline from control dates only and then permute.
  - *Robustness:* the threat "Nov 10 is always the 2nd of 4 dates (trend)" is, in their terms, non-stationary shocks under a misspecified proxy, the one combination their theory excludes (p. 23) and their Tables I.3-I.4 show failing badly for DiD (p. 99). This is the strongest argument for either a symmetric window around Nov 10 or an explicit seasonal term in the proxy when the pool is widened.
  - *Robustness:* Remark 2 (p. 19): if date-level variance differs across the year (winter weather, school terms), standardize residuals or narrow the window before permuting.
  - *Robustness:* placebo tests on the pre-period (pp. 44-45) correspond to running the same rank test with other dates as pseudo-events; the resulting p-values should look uniform.
  - *Results:* confidence interval by inversion (Algorithm 1, p. 12), the same construction as Firpo & Possebom but justified over time.
  - *Literature:* p. 5 gives a clear contrast between permuting over units (needs an assignment model, or a good model for every unit) and permuting over time (needs many pre-periods and invariant shocks).

- **Caveats.**
  - Our earlier notes describe the method as "moving-block permutation over the weekly series, an alternative to exchangeability" and "permute in blocks". Precisely: the moving-block set is the T cyclic shifts of the whole residual series, so there are only T distinct values; and when exchangeability fails, validity is approximate and asymptotic in T0, under consistency or stability conditions. It is not a small-sample exact method for dependent data.
  - The treated period sits at the end of the sample in the paper; ours is in the middle of the year. Cyclic shifts handle this mechanically, but the paper does not discuss an interior treated period **[mine]**.
  - The paper's statistics use absolute residuals (two-sided). A signed, one-sided statistic is permitted by Remark 1 in spirit but is not analysed.
  - The paper has one time series. Our five years are five short series with one treated period each. Neither the multiple-unit extension (averaging units over a common time index, pp. 43-44) nor the average-effect extension (pp. 42-43) covers this; stacking years is our construction.
  - With about 52 same-weekday dates per year the per-year p-value floor is about 0.02, and `(T*/T0)^{1/4} log T` is not small at T0 of about 50, so the asymptotic bound is loose for us. Exchangeability within a narrow window remains the main justification.
  - Within-year dates are 7 days apart; the paper's weak-dependence conditions are plausible but untested for our contrasts.
  - The pure time-series (AR) proxy is not order-invariant, so exactness is lost if we use it (p. 47).

- **Checks it suggests for us.**
  - For each year, compute the city-level (or class-level) contrast for every same-weekday date, fit `c_t = mu + u_t` under the null, and report (a) the rank p-value of Nov 10, (b) the residual series plot, (c) autocorrelation of residuals at lags 1-4 weeks.
  - Repeat with a proxy that includes a smooth seasonal term (linear or quadratic in week of year, or sunrise time), estimated under the null on all dates. If the p-value moves a lot, the stationarity assumption is doing the work.
  - Pseudo-event tests: apply the same test to each non-event date in turn and check that rejection frequency at 10% is near 10%.
  - Symmetric-window version: use the k same-weekday dates before and k after Nov 10 (k = 1, 2, 3, 4) so that a linear trend cancels; show how the estimate and p-value change with k.
  - Combine years with a pre-specified rule (mean of signed residuals, or sum of within-year ranks) and permute within year, which stays exact under within-year exchangeability.

---

## Corrections to earlier notes (`literature/notes/randomization_inference.md`, `literature/review.md`)

1. abadie2015 did not introduce in-time placebos; abadie2010 already mentions them (p. 5). abadie2015 names and applies them, as a visual falsification check without a p-value (pp. 5, 10-11).
2. In the papers' own terms, ranking Nov 10 against other dates is the in-space test (dates are units). The in-time placebo is the other-hours check. A rank p-value over time periods is supported by chernozhukov2021 and by the Andrews-type test summarized in abadie2021 (p. 31), not by abadie2015.
3. abadie2021 does not speak of studentization and does not suggest scaling by non-siren-hour contrasts; the ratio is motivated by poor pre-period fit of placebo units (p. 13). The hour-based scaling is our analogue.
4. firpo2018's sensitivity parameter tilts the weight of the set of assignments at least as extreme as the observed one; it is not literally the odds that the treated unit is selected, and its benchmarks for "large" are specific to small N.
5. chernozhukov2021's moving-block permutations are cyclic shifts with a p-value floor of 1/T, and validity under dependence is approximate for large T0, with the requirement that shocks are stationary and unaffected by the event.
6. All three Abadie papers state that the permutation p-value is classical randomization inference only under random assignment, and call that restrictive or improbable (abadie2010 p. 5; abadie2015 p. 6; abadie2021 p. 14). The suggested wording "we treat the date as if randomly assigned ... the p-value is exact" should be reframed as significance against a uniform benchmark over same-weekday dates, plus the sensitivity analysis.

---

## Cross-paper synthesis

1. Our test is the Abadie et al. placebo test with dates as units and years as pooled interventions; firpo2018 Section 6.2 (pp. 18-19) describes the same product assignment space, `prod (J_g + 1)`, which is our 4^5 = 1024.
2. None of the papers lets us claim literal randomization. Present the p-value as significance against a uniform benchmark over same-weekday dates (abadie2021 p. 14) and back it with a sensitivity parameter (firpo2018 pp. 6-8).
3. A second, independent justification comes from permuting over time: with one treated period the chernozhukov2021 test is the rank of Nov 10 among the year's dates, exact under within-year exchangeability because our baseline is already estimated with the null imposed (p. 47).
4. That justification breaks under trend or seasonality with a too-simple baseline (chernozhukov2021 p. 23, Tables I.3-I.4). The "Nov 10 is always 2nd of 4" problem is this case; use symmetric windows or a seasonal term, and show both.
5. The p-value floor is 1/(number of assignments). Widening the pool is the only way to gain resolution, but the donor rules (abadie2015 p. 6; abadie2021 p. 19) require excluding shocked dates by a rule fixed in advance and staying close to November.
6. Do not trim placebo dates by fit after the fact; it distorts size (firpo2018 Table 2, p. 14). Use a ratio statistic scaled by each date's non-siren-hour variability (abadie2010 p. 11; abadie2021 p. 13), one-sided via negative parts (abadie2021 p. 14).
7. Because each placebo DiD uses Nov 10 as a control, placebo estimates are shifted by minus one third of the effect (abadie2021 footnote 10). Ranking is unaffected, but test inversion must adjust the Nov 10 contrast first.
8. Confidence sets: invert the permutation test under a constant effect (firpo2018 eqs. 15-16; chernozhukov2021 Algorithm 1), report a one-sided upper bound in stop-minutes, and test the 1-minute and 2-minute stop nulls directly.
9. Multiplicity over speed classes: run firpo2018's permutation min-p procedure on the same assignments (pp. 16-18). By my arithmetic the 50-70 km/h result tolerates a tilt of odds 6.7 as a single test but only 1.28 at a Bonferroni level, so pre-declare one primary statistic.
10. Always show the diagnostics these papers treat as standard: the whole placebo distribution, other-hour (in-time) placebos, pseudo-event dates, leave-one-date-out and leave-one-year-out, and the cell-level standard errors only as descriptive, since they do not measure the relevant uncertainty (abadie2010 pp. 4-5).
