# 07 - Event-day studies: control days, estimators, inference

Reader notes for the 10 November siren paper. Page numbers are PDF pages as marked
(`=== page N ===`) in `literature/txt/<key>.txt`. Where I add a remark that is mine and
not in the paper, it is labelled "(my remark)".

Quick comparison of the designs (details and page references in each section):

| Key | Event window | Control days | Estimator / inference | Headline |
|---|---|---|---|---|
| redelmeier2003 | Super Bowl Sunday, split before/during/after telecast | Sunday before and Sunday after (2 per event, 27 events) | Ratio of counts; test not named | +41% fatalities after telecast |
| redelmeier2008 | Election Tuesday, 8:00-19:59 local | Tuesday before and after (2 per event, 8 events) | Ratio of counts; binomial test | RR 1.18 (1.10-1.26) |
| redelmeier2012 | Tax day, whole day | Same weekday 1 week before and after (2 per event, 30 events) | Binomial test, two-tailed | OR 1.06 (1.03-1.10) |
| redelmeier2024 | 3 days centred on 21 Aug 2017 eclipse | Same 3 weekdays 1 week before and after (6 days, 1 event) | Negative binomial with weekday adjustment | RR 1.31 (1.15-1.49) |
| staples2018 | 20 April, 16:20-23:59 | 13 and 27 April, same hours (2 per event, 25 events) | Exact binomial test | RR 1.12 (1.05-1.19) |
| zhang2016 | Re-analysis of redelmeier2008 | Same statistic, but null built from 200 placebo Tuesdays | Empirical (placebo-date) null distribution | RR 1.17, p = 0.070; 24h RR 1.04 |
| harper2019 | Re-analysis of staples2018 | +/-7 days; then +/-7 and +/-14; then all other days | Poisson vs negative binomial / clustered / bootstrap; multilevel model | 1.12 -> 1.05 -> 0.98, all CIs include 1 |
| smith2016 | Days after DST transition | RD around the transition; day-of-year FE with dates that switch status | Local linear RD, placebo dates, permutation test | +5.6 to 6.5% fatal crashes, 6 days |
| card2011 | NFL Sundays, noon-midnight, 3-hour windows | Non-game Sundays; win vs loss conditional on betting spread | Poisson with agency FE, cluster team x season | Upset loss +10% |
| lindo2018 | College football game days (mostly Saturdays) | Non-game Saturdays and other days of the same agency-week | Poisson with agency x year x week FE, cluster by college | +28% reports on game days |
| gulek2024 | Ramadan and Qadr, 15:00-18:00 on working days | Non-Ramadan working days, with weekday/month/year FE | Poisson province panel; IBB traffic index as exposure check | Ramadan +3.5%, Qadr +21%, LATE 25% |

---

### redelmeier2003 - Redelmeier and Stewart (2003), Driving fatalities on Super Bowl Sunday

Only the letter on PDF pages 12-13 was read (the rest of the PDF is unrelated correspondence).

- **Question and setting**: Do fatal crashes in the United States rise on Super Bowl Sunday, and in which part of the day? NEJM letter (about one page plus one figure).
- **Data and method**
  - FARS (census of fatal crashes), all available years 1975-2001, 27 consecutive Super Bowl Sundays (p. 12).
  - Control days: for each Super Bowl Sunday, the Sunday immediately before and the Sunday immediately after, so 2 controls per event and 54 control days. The stated purpose is to hold season, weekday and calendar year fixed (p. 12).
  - Event hours: the time from kickoff to the end of the game defines three intervals (before, during, after the telecast). The same clock times are applied to the control Sundays, and times are converted to Greenwich Mean Time so that one interval definition works across time zones (p. 12).
  - Estimator: ratio of the average fatality count on event days to the average on control days, by interval. The letter reports P values and 95% CIs but does not name the statistical test.
- **Main findings**
  - After the telecast: 24.5 vs 17.3 fatalities on average, a 41% relative increase, P < 0.001 (p. 12).
  - Before the telecast: 68.9 vs 67.0, P > 0.20. During the telecast: 15.7 vs 17.7, P = 0.036, described as a marginal decrease (p. 12).
  - The post-telecast increase appeared in 21 of 27 years; about 7 extra deaths per Super Bowl Sunday (p. 12); 189 extra deaths over the 27 Sundays (figure legend, p. 13).
  - Larger in states of the losing team than neutral states than winning states: 68% vs 46% vs 6%, P = 0.003 (p. 12).
  - The figure repeats the before/after contrast for nonfatal injuries and by subgroup (sex, age, region, driver status, alcohol, within/beyond 1 hour of the telecast) (p. 13).
- **Usable for our paper**
  - Literature / Method: origin of the "same weekday one week before and one week after" double-control design that our Nov 3 / Nov 17 comparison follows (p. 12).
  - Method: precedent for defining the event by clock time and applying the identical clock window to the control days (p. 12). Our 09h contrast on control dates is the same idea.
  - Robustness: the before / during / after split is an in-built placebo (no effect before the event) and also shows a sign change within the day (fewer deaths during, more after) (p. 12). This supports reporting hours around 09h separately.
  - Results-Discussion: reporting "effect present in 21 of 27 years" is a simple sign-consistency statistic we can copy (k of 5 years).
- **Caveats**
  - The test behind P < 0.001 is not stated; later re-analyses of the same design (zhang2016, harper2019) show that count-based tests of this kind understate uncertainty. Do not cite the P value as evidence of strength.
  - Outcome is fatalities, not speed or flow; nothing here is about traffic speed.
  - A letter: no model, no robustness to the choice of control days.
- **Checks it suggests for us**
  - Report the Nov 10 vs control contrast separately for the hour before (08h), the event hour (09h) and the hour after (10h), in levels, not only the combined within-day contrast.
  - Count in how many of the 5 years the sign is negative, per speed class.

---

### redelmeier2008 - Redelmeier and Tibshirani (2008), Driving fatalities on US presidential election days

- **Question and setting**: Does the US presidential election, which mobilises about half the population, raise fatal crash involvement during polling hours? JAMA research letter.
- **Data and method**
  - FARS 1975-2006; all 8 presidential elections from 1976 to 2004 (p. 1).
  - Event hours: polling hours defined as 8:00 AM to 7:59 PM local time (p. 1).
  - Control days: the same hours on the Tuesday immediately before and the Tuesday immediately after each election, so 16 control days (p. 1). Expected count = total on control days divided by 2 (figure note, p. 2).
  - Outcome: number of individuals involved in fatal crashes (not all of them died) (figure note, p. 2).
  - Inference: confidence intervals from binomial tests (p. 1).
- **Main findings**
  - 1265 individuals on 8 election days (158 per day, 13 per hour) vs 2152 on 16 control days (134 per day, 11 per hour); RR 1.18, 95% CI 1.10-1.26, P < .001 (p. 1).
  - Absolute excess 189 individuals over the study period (95% CI 104-280), about 24 per election (p. 1).
  - Placebo days: Monday before the election vs control Mondays, RR 0.97 (0.89-1.06); Wednesday after vs control Wednesdays, RR 1.03 (0.95-1.12) (p. 1).
  - Alternative hour definitions are in the figure: 7:00 AM-8:59 PM (1376 vs 2531) and 9:00 AM-6:59 PM (1073 vs 1810) (p. 2).
  - The authors note that a 4% rise in average speed could by itself produce an 18% rise in deaths (p. 1).
- **Usable for our paper**
  - Literature: second canonical example of the double-control design applied to a civic event with a fixed time window (p. 1).
  - Robustness: adjacent-day placebos (day before and day after the event, each compared with its own +/-1 week controls) (p. 1). Direct template for Nov 9 and Nov 11 placebos.
  - Robustness: varying the hour window (longer / shorter polling hours) (p. 2).
  - Introduction: the speed-to-fatality rule of thumb (4% speed, 18% deaths) is a compact way to say why small speed changes matter (p. 1). It is cited to Joksch (1993), so cite the original if used.
- **Caveats**
  - This is the result that zhang2016 re-analysed: the point estimate replicates but the binomial P value does not (see below). Cite the two together, never this one alone.
  - 8 events and 16 control days; the reported precision comes from treating individuals as independent draws.
- **Checks it suggests for us**
  - Run the full estimator on Nov 9 and Nov 11 as pseudo-event days.
  - Vary the within-day comparison hours (for example 07h and 11h instead of 08h and 10h).

---

### redelmeier2012 - Redelmeier and Yarnell (2012), Road crash fatalities on US income tax days

- **Question and setting**: Does the stress of the US tax filing deadline raise fatal crash involvement? JAMA research letter.
- **Data and method**
  - FARS 1980-2009, 30 tax days (p. 2).
  - Control days: the day one week before and the day one week after each tax day, so 60 control days. The authors say this holds year, month and weekday fixed and limits confounding from slow-moving factors such as vehicle technology and fuel prices (p. 2).
  - Event window: the whole day; time of day enters only as a subgroup (dawn, morning, afternoon, night in 6-hour blocks) (figure note, p. 2).
  - Inference: binomial tests, two-tailed, threshold P = .05; hypothesis described as prespecified (p. 2).
- **Main findings**
  - 19,541 individuals in fatal crashes: 6783 on 30 tax days (226 per day) vs 12,758 on 60 control days (213 per day); OR 1.06, 95% CI 1.03-1.10, P < .001 (p. 2).
  - Absolute excess 404 individuals over 30 years, about 13 per tax day (p. 2).
  - No subgroup showed a significant opposite effect; no accentuation at night (p. 2).
- **Usable for our paper**
  - Literature: one sentence that the double-control design has been applied repeatedly to fixed-calendar civic dates (p. 2).
  - Method: the explicit argument for why +/-1 week controls work (same year, month, weekday; slow confounders differenced out) (p. 2). This is the justification we give for Nov 3 and Nov 17.
- **Caveats**
  - A 6% effect with a CI of 1.03-1.10 from 30 event days is exactly the kind of precision that zhang2016 and harper2019 show to be overstated under binomial / Poisson assumptions. The letter itself has no placebo days.
  - Whole-day window; no information on timing.
- **Checks it suggests for us**
  - None beyond those listed under redelmeier2008; useful mainly as a citation.

---

### redelmeier2024 - Redelmeier and Staples (2024), Fatal traffic risks with a total solar eclipse in the US

The text file is a web-page print; the two figures are not readable in it.

- **Question and setting**: Was the 21 August 2017 total solar eclipse associated with more fatal crashes in the US? JAMA Internal Medicine research letter.
- **Data and method**
  - FARS; described as a matched case-control study (p. 2).
  - Event window: a 3-day exposure interval centred on the eclipse day, on the reasoning that much eclipse travel happened on adjacent days (p. 2).
  - Control days: 3-day intervals one week before and one week after, matched by day of week, so 6 control days for a single event (p. 2).
  - Timing: each crash is placed relative to the moment of maximal eclipse at its own latitude and longitude, using a US Navy calculator (p. 2).
  - Estimator and inference: negative binomial regression with adjustment for day of week; two-tailed P < .05 (p. 3). Note the move away from the binomial test of the earlier letters.
- **Main findings**
  - 741 individuals in fatal crashes in the 3 eclipse days (10.3 per hour) vs 1137 in the 6 control days (7.9 per hour); RR 1.31, 95% CI 1.15-1.49, P < .001 (p. 3).
  - About 1 extra crash-involved person every 25 minutes and 1 extra fatality every 95 minutes (p. 3).
  - Larger under clear weather; risk varied with time relative to the eclipse (figures, p. 3-4).
  - The authors do not attribute the excess to the darkness itself, noting that "the eclipse lasted less than 3 minutes in any one place" (p. 4); they point to extra travel, unfamiliar routes, speeding, distraction and roadside viewing (p. 5).
- **Usable for our paper**
  - Introduction / Literature: the closest example in this group of a very short event (under 3 minutes) studied through a much wider window; the authors explicitly separate the brief physical event from the surrounding behaviour (p. 4-5). Useful contrast: our siren effect is the brief event itself, measured in an hourly average.
  - Method: event time defined relative to a precisely known instant (p. 2), as we do with 09:05.
  - Method: same-weekday +/-1 week controls even with a single event (p. 2).
- **Caveats**
  - One event, six control days. The CI comes from the count model, not from variation across events.
  - The effect is a travel-volume story over three days; it says nothing about traffic stopping or slowing during the event.
- **Checks it suggests for us**
  - With the 5-minute IBB index (Oct-Nov 2026), plot the series in event time (minutes from 09:05) for Nov 10 against the same weekday +/-1 week, as their Figure 2 does for hours from the eclipse.

---

### staples2018 - Staples and Redelmeier (2018), The April 20 cannabis celebration and fatal traffic crashes

- **Question and setting**: Is the "4/20" cannabis celebration (mass consumption at 4:20 PM on 20 April) associated with more fatal crashes in the US? JAMA Internal Medicine research letter.
- **Data and method**
  - FARS, 25 years, January 1992 to December 2016 (p. 2).
  - Event hours: 4:20 PM to 11:59 PM on 20 April (p. 2).
  - Control days: the same hours on 13 April and 27 April of the same year, so 2 controls per event and 50 control days (p. 2). Because 20 April is a fixed calendar date, +/-7 days keeps the weekday; this is the same situation as 10 November.
  - Outcome: drivers involved in fatal crashes (p. 2).
  - Inference: exact binomial tests; prespecified stratified analyses (p. 2). The design rationale is stated as "This design controlled for weekday, season, and year" (p. 2).
- **Main findings**
  - 1369 drivers on 20 April vs 2453 on control days (7.1 vs 6.4 drivers per hour); RR 1.12, 95% CI 1.05-1.19, P = .001 (p. 2).
  - Placebos: no difference before 4:20 PM, and none on 18 April or 22 April against their own controls (p. 2).
  - Sensitivity: all crash-involved persons instead of drivers; window extended to 5:00 AM next day (p. 2).
  - By state: 30 states above 1, 18 below, 2 exactly 1 (figure note, p. 2).
- **Usable for our paper**
  - Method: closest formal analogue to our setup: fixed calendar date, event at a precise clock time, hours after it compared with the same hours 7 days earlier and later (p. 2).
  - Robustness: the two placebo types we should report: hours before the event on the event day, and nearby non-event dates (p. 2).
- **Caveats**
  - harper2019 shows the 12% result does not survive overdispersion-robust inference or a wider control pool (see below). Our earlier notes should not present staples2018 as an established finding; it is best cited as the design template and as the result that was challenged.
- **Checks it suggests for us**
  - Pre-event-hour placebo: apply the estimator to a contrast centred on 07h or 08h using only hours before 09:00.
  - Nearby-date placebo: Nov 8 and Nov 12 (two days away, as they used 18 and 22 April).

---

### zhang2016 - Zhang and Aronow (2016), Driving fatalities on US presidential election days: a reanalysis

- **Question and setting**: Is the election-day excess of redelmeier2008 statistically or substantively unusual once week-to-week noise is taken into account? BMC Research Notes short report.
- **Data and method**
  - Same FARS source, updated; elections 1980-2008 only, because the placebo window needs data 100 Tuesdays on each side (1976 and 2012 are dropped) (p. 2).
  - Test statistic kept identical to the original: RR = count in the window on the index Tuesday divided by the average of the same window on the Tuesdays one week before and one week after (p. 1).
  - How the control pool was widened: they did not change the comparison days inside the statistic. They computed the same RR for each of the 100 Tuesdays before and the 100 Tuesdays after election day, giving 200 placebo RRs, and used these as an empirical null distribution. Only Tuesdays are used, to condition on weekday (p. 2).
  - P value: two-tailed, the share of placebo RRs more extreme than the election-day RR (RR larger, or smaller than 1/RR). Null hypothesis: the election-day RR is a random draw from the distribution of Tuesday RRs (p. 2).
  - CI: Wald-type, using the standard deviation of the placebo distribution as the standard error (p. 2).
  - They also applied the original binomial test to every placebo Tuesday to measure its false rejection rate (p. 3).
  - Extra outcomes: non-election hours and the full 24 hours (p. 1). Robustness: placebo pools of 12, 25 and 50 surrounding Tuesdays (footnote 2, p. 3). They report that results are weaker still with number of crashes or number of fatalities as the outcome (footnote 1, p. 1).
- **Main findings**
  - Election hours: RR 1.17, non-parametric P = 0.070, 95% CI 0.99-1.35. The point estimate matches the original 1.18; the uncertainty is much larger (p. 3).
  - The binomial procedure rejects the null on 43% of ordinary Tuesdays (p. 3). In their words, "the binomial test may be anticonservative in this setting" (p. 3).
  - Non-election hours on election day: RR 0.83, P = 0.085, CI 0.60-1.06. Full 24 hours: RR 1.04, P = 0.570, CI 0.89-1.20 (p. 3).
  - With narrower placebo pools the election-hours P values are 0.04 (12 Tuesdays), 0.06 (25), 0.05 (50); full-day P values stay between 0.42 and 0.47 (footnote 2, p. 3).
  - Conclusion: a marginal election-hours increase that is offset by a decrease in the other hours of the same day (p. 3).
- **Usable for our paper**
  - Method (most important citation in this group): precedent for replacing a parametric count test with a placebo-date distribution built from same-weekday dates. This is the same logic as our randomization inference over which date is "treated", and it supports the statement that the effective sample is dates (p. 2-3).
  - Method: the 43% false rejection rate is the number to quote when explaining why we do not use cell-level standard errors (p. 3).
  - Robustness: reporting the P value for several placebo-pool sizes (12, 25, 50, 100) is a template for our widened control pool (footnote 2, p. 3).
  - Results-Discussion: within-day displacement. An effect in the event hours can be offset in other hours (p. 3). For us: check whether 10h (or later hours) is faster on Nov 10.
- **Caveats**
  - The null is an exchangeability assumption (the event day is like any other same-weekday day), not a design-based randomization. It needs the statistic to have a stable distribution across the placebo dates; the paper does not test for seasonality in the placebo RRs.
  - The paper does not say the original effect is zero; it says the evidence is weak (P = 0.07) and offset over the day.
  - Elections pooled (8 events); the paper does not spell out how the placebo RRs are pooled across election years. I assume summed counts at each week offset, but that is not stated.
  - Each placebo Tuesday is compared with its own neighbours, so adjacent placebo RRs share control days and are not independent; the paper does not discuss this.
- **Checks it suggests for us**
  - Build the Zhang-Aronow null for our statistic: for every same-weekday date in a window around Nov 10 (and in the whole year), compute the same DiD contrast against its own +/-7 day neighbours, pooled over the 5 years by offset; report the rank of Nov 10. Show P for several window sizes.
  - Apply our own test to every placebo date and report its rejection rate at 5%; this is a direct size check of our procedure.
  - Report the full-morning or full-day analogue (is time lost at 09h recovered later?).

---

### harper2019 - Harper and Palayew (2019), The annual cannabis holiday and fatal traffic crashes

The file is the accepted manuscript (dated 18 January 2019) of the Injury Prevention article, with appendix.

- **Question and setting**: Does the 12% "4/20" effect of staples2018 hold up against other control periods, proper variance estimation, comparison with known risky days, and over time?
- **Data and method**
  - FARS 1975-2016; main window 1992-2016; drivers in fatal crashes between 16:20 and 23:59 (p. 4).
  - How the control pool was widened, in three steps (p. 5; appendix p. 14):
    1. Same weekday one week before and after (13 and 27 April): 3 days x 25 years = 75 observations.
    2. Same weekday one and two weeks before and after: 5 days x 25 years = 125 observations.
    3. All other days of the year: 9132 observations.
  - Model: daily count y_i with ln(mu_i) = alpha + beta x 1{4/20}, estimated as Poisson, negative binomial, Poisson with Pearson-scaled SEs, Poisson with SEs clustered by year, and Poisson with bootstrapped SEs (p. 5; appendix p. 14).
  - Benchmark: the same three control sets for 4 July, a day with established excess risk (p. 5).
  - "Every day as the event": a separate negative binomial regression for each day of the year against its own +/-7 day controls, 1992-2016 (p. 5-6).
  - Time variation: one multilevel Poisson model on all 1975-2016 days with year random intercepts and year-varying random slopes for 4/20, 4 July, Saturday before Labor Day, day before Thanksgiving, Christmas, New Year's Day; weakly informative priors, 4000 posterior draws (p. 5; appendix p. 14-15).
  - Data and code are public (OSF link, p. 5).
- **Main findings**
  - They reproduce the original: IRR 1.12 with Poisson CI 1.05-1.19 (Table 4, p. 18). With overdispersion handled, the same point estimate has CI 0.97-1.28 (negative binomial), 0.99-1.27 (clustered), 0.97-1.29 (bootstrap) (Table 4, p. 18).
  - Widening to +/-7 and +/-14 days: IRR 1.05. All other days: IRR 0.98, CI 0.88-1.10 (negative binomial) (abstract p. 2; Table 4, p. 18).
  - 4 July under the same three control sets: 1.39 (1.24-1.56), 1.34, 1.46 (1.31-1.63); about 40% whatever the controls (p. 6; Table 5, p. 18).
  - Day-by-day regressions: the 4/20 estimate sits within the bulk of ordinary daily variation. With +/-7 day controls, 16 days have CIs above 1 and 15 days have CIs below 1 (Table 8, p. 20). (My remark: 31 of about 365 days is 8.5%, above the nominal 5%. Some of the "less risky" days are mechanical: 27 June (0.80) and 11 July (0.83) each have 4 July as one of their two control days. A pseudo-event date that uses a true event day as its control is biased in the opposite direction, so such dates must be removed from any placebo distribution; smith2016 does exactly this.)
  - Multilevel model: average annual excess drivers on 4/20 is -3.44 (95% interval -7.93 to 1.37); 4 July +33.61; Saturday before Labor Day +26.59; day before Thanksgiving +23.22; Christmas -12.36; New Year's Day -21.64 (Table 9, p. 21). No growth of a 4/20 effect in recent years (p. 7, 9).
  - General message on the double-control design: "the choice of two days a week apart is arbitrary" (p. 5), and ignoring the stochastic and deterministic structure of daily counts degrades inference (p. 9).
- **Usable for our paper**
  - Method: justification for (a) reporting the estimate under several control sets and (b) not relying on Poisson-type cell-level variance (p. 5, 9; Table 4, p. 18).
  - Robustness: the three-tier control ladder (+/-7; +/-7 and +/-14; all days) is the template for our widening from {Nov 3, 17, 24} to all same-weekday dates (p. 5).
  - Robustness: the benchmark-day idea. A real effect (4 July) is stable across control sets; a fragile one (4/20) is not (p. 6). We need an analogous positive control.
  - Robustness: the "each day of the year as pseudo-event" plot (their Figure 2, p. 7) is the figure we should make for the within-day contrast.
  - Results-Discussion: a reliable national effect needs either a large relative risk or near-universal exposure (p. 9). The siren has near-universal exposure for vehicles on the road at 09:05, which is our argument for why a detectable effect is plausible despite its brevity.
- **Caveats**
  - As written in the appendix, the regression has only the event-day indicator (appendix p. 14). I could not find weekday, month or year controls in the "all other days" comparison. April is a below-average month and weekdays differ strongly (appendix Tables 1-2, p. 16), so the 0.98 is not a like-for-like comparison. The +/-14 result (1.05) is the cleaner widening. Do not cite 0.98 as "the" corrected estimate.
  - In Table 4 (p. 18) and the abstract (p. 2) the upper CI limits in the +/-14 column are identical to those in the +/-7 column (for example 0.92-1.28 next to 0.97-1.28). This looks like a table error in this manuscript version; check the published article before quoting the +/-14 intervals.
  - The paper's conclusion is "little evidence", not "no effect"; point estimates with +/-7 controls remain 1.12.
  - The hours window was kept at 16:20-23:59 for comparability; the authors note results for some days would change with other hours (p. 10).
- **Checks it suggests for us**
  - Control ladder: (i) Nov 3 and 17; (ii) Oct 27, Nov 3, 17, 24 (symmetric +/-7 and +/-14); (iii) all same-weekday dates in a window; (iv) all same-weekday dates in the year. Our pilot set {Nov 3, 17, 24} is asymmetric (-7, +7, +14), which is the source of the "Nov 10 is always 2nd of 4" trend threat; the symmetric set removes a linear trend by construction (my remark).
  - Positive control: run the identical pipeline on a date-hour where a slowdown is known (for example the first school day at 08h, or a known closure) and show it is recovered under all control sets.
  - Pseudo-event figure: estimate for every date of the year with its own +/-7 controls, Nov 10 highlighted. Drop or flag Nov 3 and Nov 17 as pseudo-events, because Nov 10 is one of their controls (see the 27 June / 11 July pattern in Table 8, p. 20).
  - Year-by-year estimates with intervals (5 points), in the spirit of their Figure 3.

---

### smith2016 - Smith (2016), Spring forward at your own risk: daylight saving time and fatal vehicle crashes

- **Question and setting**: Does the transition into daylight saving time (DST) raise fatal crashes in the US, and is the channel sleep loss or the shift of daylight? AEJ: Applied Economics.
- **Data and method**
  - FARS 2002-2011, five years each side of the 2007 change in DST dates; continental US without Arizona and Indiana (p. 7). Historical extension 1976-2001 (p. 22).
  - Unit: national daily count; dependent variable ln(fatal crashes per day). Aggregated to the national level because crashes are rare and to smooth local shocks such as weather (p. 7-8). FARS-designated holidays are dropped (p. 7).
  - Transition-day length handled by counting the 3-4 am hour twice in spring and halving the 1-2 am hour in fall; robust to 24/23 and 24/25 scaling or to dropping the day (p. 7, 13).
  - How the recurring calendar shock is identified, strategy 1 (RD in event time) (p. 9):
    - First demean ln(crashes) by day-of-week and year.
    - ln Fatals_dy = b0 + b1 DST_dy + f(DaysToTran_dy) + f(DST_dy x DaysToTran_dy) + e_dy, with DaysToTran centred on each year's transition date; local linear, uniform kernel, CCT bandwidth (IK and CV as alternatives).
  - Strategy 2 (day-of-year fixed effects) (p. 10):
    - ln Fatals_dy = b0 + b1 SpDST_dy + b2 FaDST_dy + DayofYear_d + DayofWeek_dy + Year_y + e_dy.
    - Identified only by calendar dates that are DST in some years and standard time in others (the 2007 extension plus the "second Sunday" rule moving the date between 8 and 14 March) (p. 10; Figure 3, p. 11). Day-of-year dummies are month/day combinations, not day counts (footnote 25, p. 10).
  - Placebo dates: assign the post-2007 transition date to 2002-2006 and the pre-2007 date to 2007-2011, where no clock change happened on those dates (p. 10, 12-13).
  - Permutation test: re-estimate the baseline RD at every pseudo-transition date relative to the true one; dates within the first two weeks of DST, or whose 27-day bandwidth would include them, are excluded so the true effect does not enter the null (p. 13 and footnote 28).
  - Alternative standard errors because crash risk may be serially correlated: other clustering schemes, Newey-West with several lag lengths, CCT robust intervals (footnote 27, p. 12).
  - Mechanism tests use hours: morning = +/-2 hours around local sunrise, evening = +/-2 hours around local sunset, and the remaining "least light impacted" hours (p. 15-16 and footnote 31).
- **Main findings**
  - Spring RD: b1 = 0.0649 (SE 0.0231), about 6.5%; 0.0499 (IK) and 0.0626 (CV). By sub-period: 0.0941 (2002-2006) and 0.0375, not significant (2007-2011). Placebo dates: 0.0005 (SE 0.0225). RD samples are 550 to 966 days (Table 1, p. 13).
  - Permutation P value for the 6.5% jump: 0.007 (p. 14; Figure 5).
  - Fall RD: 0.0011 (SE 0.0236), no change (Table 2, p. 15). The fall placebo is marginally significant at 0.0361 (p. 14-15), which the author treats as not robust.
  - Light reallocates crashes within the day with zero net effect: leaving DST gives morning -0.115, evening +0.187, least-light-impacted hours -0.0134 (Table 3, p. 16).
  - Day-of-year FE: first six days of DST +0.0565 (SE 0.0231); next eight days +0.0254 (ns); remainder of spring +0.0142 (ns); whole spring switching period +0.0319; 3,341 day observations (Table 5, p. 19).
  - Preferred number: 5.6% more fatal crashes for six days, over 30 deaths a year, about $275 million (p. 4, 25).
  - 1976-2001: a net light benefit of -3.9% existed historically and masked the sleep effect (first six days +0.0164 ns; difference to remainder of spring implies +5.5%) (Table 7, p. 23).
- **Usable for our paper**
  - Method: residualise by day-of-week and year before comparing dates (p. 9). For our widened pool this is the minimal adjustment; add a smooth function of calendar time for season.
  - Method: aggregate to one number per day before inference, because the shock is common to all units on a date (p. 7-8). Supports "average over cells in a year, effective sample = dates".
  - Robustness: permutation over pseudo-event dates with contaminated dates excluded (p. 13, footnote 28). Our randomization inference is the same idea; cite Smith for the P = 0.007 precedent in an economics journal.
  - Robustness: Newey-West / alternative clustering for daily series (footnote 27, p. 12), in case we report a regression version.
  - Robustness: holidays dropped from the sample (p. 7). Our all-year control pool should drop public holidays and their neighbours.
  - Results-Discussion: within-day reallocation with no net effect (Table 3, p. 16) is the cleanest published example of why an hourly contrast and a daily total can disagree.
  - Results-Discussion: lower-bound language. Fatal crashes are described as a lower bound on all crashes (p. 8), parallel to our "stopped vehicles excluded" lower bound.
- **Caveats**
  - The day-of-year FE strategy needs dates whose treatment status changes across years. Nov 10 at 09:05 is treated in every year of our data, so a date fixed effect would absorb our effect; this strategy is not available to us. Our identifying variation is across dates within a year (and across hours within the date).
  - The RD estimates a level shift that persists for days; our event is a one-hour pulse, so an RD in days is not the right tool. What transfers is the demeaning, the placebo dates and the permutation test.
  - The six-day window was chosen after looking at the residual plot (footnote 34, p. 19); the author says so. It is a reminder to fix our windows in advance.
  - The 2007-2011 half-sample estimate is not significant on its own (Table 1, p. 13).
- **Checks it suggests for us**
  - Regression version on all days: c_dy = a + tau x 1{Nov 10} + DayofWeek + Year (+ week-of-year or smooth season) + e, with the randomization P value as the primary inference and Newey-West as a secondary one.
  - Permutation distribution over all non-holiday same-weekday dates, excluding dates used as controls for Nov 10, with a density plot and the true estimate marked (their Figure 5).
  - Hours-based placebo: the same date-level DiD for contrasts centred on hours with no siren (for example 11h, 14h, 16h).
  - Check 08h and 10h for reallocation (drivers timing trips around 09:05), since they are our within-day controls (my remark).

---

### card2011 - Card and Dahl (2011), Family violence and football: the effect of unexpected emotional cues on violent behavior

Tables are images in the text file; Table IV numbers below were read from the PDF (p. 25-26).

- **Question and setting**: Do unexpected losses of the local NFL team trigger intimate partner violence (IPV) at home? QJE. Not a traffic paper; relevant for how a recurring, scheduled, same-weekday shock is identified with hourly timing.
- **Data and method**
  - NIBRS police reports, 1995-2006, 763-764 city and county agencies in states matched to 6 NFL teams (p. 12, 26). 866 regular-season Sunday games (p. 20).
  - Sample restricted to the 17 Sundays of each regular season, because violence varies strongly by weekday and almost all games are on Sunday (p. 9, 21). A "day" is noon to 11:59 PM Eastern Time (p. 9, 26). Unit: agency-day; 79,386 observations (p. 26).
  - Poisson count model: log(mu_jt) = theta_j + X_jt gamma + g(S_jt, y_jt; lambda), with agency fixed effects theta_j, controls X (season, week-of-season, holiday dummies, weather; Nielsen rating in one column), and g = dummies for three ranges of the pregame point spread interacted with win/loss. Base category: non-game Sundays (p. 22-24).
  - Identification: conditional on the betting spread, the game outcome is as good as random, so loss-vs-win differences are causal (p. 7, 23). Poisson is used because fixed effects create no incidental-parameters problem and consistency needs only a correct conditional mean (p. 23-24).
  - Inference: standard errors clustered by team x season, 62 clusters (p. 26); that is, at the level at which the shock is common, not at the agency level.
  - Timing test: separate models for 3-hour windows (noon-3, 3-6, 6-9, 9-midnight), with separate coefficients for 1 PM and 4 PM games (p. 27-28).
  - Other checks: negative binomial, date fixed effects, team-specific linear trends, treatment of zero-report days (p. 37).
- **Main findings**
  - Upset loss (home team favoured by 4+ points and lost): +10% at-home male-on-female IPV; coefficient 0.112 (SE 0.034) with agency FE only, 0.100 (0.032) with date and weather controls (Table IV, p. 25; text p. 27). Stable across columns.
  - Close loss: 0.032 (0.024), not significant. Upset win: 0.016 (0.027), not significant; symmetry rejected, P = 0.00 to 0.02 (Table IV, p. 25-26).
  - Timing: nothing in noon-3 PM (outcomes unknown); effect for 1 PM games appears in 3-6 PM; for 4 PM games in 6-9 PM (+31%); nothing after 9 PM. The rise is "concentrated in a narrow time window surrounding the end of the game" (p. 28). Only 16 upset losses and 13 upset wins among 4 PM games (p. 28).
  - Larger for salient games: 13% when still in playoff contention, 20% vs 8% rival vs non-rival, 17% for highly salient games and about zero otherwise (p. 32).
  - Benchmarks from an all-days model with agency FE, weekday, month, year, holiday and weather dummies: Christmas +18%, Thanksgiving +20%, Memorial Day +30%, New Year's Day +31%, New Year's Eve +22%, 4 July +29%; hot day +8% (p. 38).
- **Usable for our paper**
  - Method: restricting the comparison to the same weekday within the season, with non-event days of that weekday as the base, is the regression form of our control-date design (p. 9, 21-22).
  - Method: cluster at the level of the common shock (team x season), not the reporting unit (p. 26). Supports treating dates, not cells, as the sample.
  - Robustness: the shifted-timing test (1 PM vs 4 PM games move the effect window by three hours) is the model for an hour-specificity check: effect in the event hour, none in hours before it (p. 27-28).
  - Robustness: stability of the coefficient as controls are added is used as evidence that treatment is orthogonal to covariates (p. 27).
  - Results-Discussion: sizing an effect against known calendar effects estimated in the same data (holidays, hot days) (p. 38). We can size the siren against, for example, the Monday-vs-Friday or rain-vs-dry difference in the same 09h contrast.
- **Caveats**
  - Identification rests on within-event random outcomes (win vs loss given the spread). We have no such second layer: the siren happens every Nov 10. The paper supports our timing and clustering choices, not our main identifying assumption.
  - The timing estimates are imprecise and the authors say so (p. 28).
  - Outcome is police reports of violence; nothing on traffic.
- **Checks it suggests for us**
  - Report the estimate with progressively richer controls (none; weekday and year; plus season/weather) and show it is stable.
  - Hour-by-hour event-day vs control-day differences for 06h-12h in one figure.
  - Benchmark table: effect of weekday, rain, school holiday on the same contrast, next to the Nov 10 effect.
  - Heterogeneity fixed in advance (speed class is our "salience"), with a joint test rather than five separate ones.

---

### lindo2018 - Lindo, Siminski and Swensen, College party culture and sexual assault

The PDF is the NBER working paper 21828 (December 2015, revised October 2016), not the published 2018 article. Check numbers against the published version before citing.

- **Question and setting**: Do Division 1 college football game days raise reports of rape with college-aged victims? Relevant here for identifying a recurring shock that almost always falls on one weekday.
- **Data and method**
  - NIBRS 1991-2012; 138 campus and municipal agencies matched to 96 universities (p. 8). Agency-by-day panel, 425,190 observations; 43,793 Saturdays without games, 17,062 Saturdays with games, only 1,128 games on other weekdays (p. 9).
  - A day runs 6:00 AM to 5:59 AM so late-night incidents attach to the right event (p. 8). 1 June-31 August excluded (p. 9).
  - Poisson: E[R_act] = exp(beta x Gameday_ct + theta_a + gamma X_t), plus one-day lead and lag of game day; X = day-of-week FE, holiday indicators, year FE (p. 11). Percent effect = (e^beta - 1) x 100 (footnote 29, p. 15).
  - Fixed effects are made progressively richer: agency; agency x month-of-year; agency x week-of-year; agency x year x month; agency x year x week. In the richest version the game day is compared with the other days of the same agency-week, net of the usual weekday pattern (p. 12).
  - Identifying assumption, stated explicitly: the weekday pattern in weeks without games is the right counterfactual for the game day (p. 11). Saturdays and game days are separately identified because most Saturdays have no game; within the season, through bye weeks and off-day games (p. 12).
  - Inference: sandwich SEs clustered by college (p. 11).
  - Hourly version (2001 on): day-of-week x hour-of-day FE, with indicators for before / during / after the game and day vs night on adjacent days (p. 16).
- **Main findings**
  - Game day: +28%; beta = 0.283 (SE 0.045) with agency FE, 0.247 (0.052) with agency x year x week FE; estimates move little across the five specifications (p. 15; Table 3, p. 36).
  - Home games +41% (0.343), away games +15% (0.136); day before a home game +19%, day after +13% (p. 15; Table 3, p. 36).
  - Robust to using only September-December, only the regular season, or dropping any one month (p. 17; Table 4, p. 37).
  - Placebo: in-season Saturdays without a game show no deviation, -0.027 (SE 0.075); same for bye weeks (p. 19; Table 6, p. 39).
  - No offsetting effects in nearby agencies or adjacent days (p. 18-19). The authors note that scattered significant spillover estimates are no more frequent than chance under multiple testing (p. 18).
  - Larger for prominent teams, rivalry games and "party schools" (70% vs 30% for home games) (p. 22-24).
- **Usable for our paper**
  - Method: a clear statement of the identifying assumption for a weekday-bound recurring event (p. 11). Our analogue: the 09h-vs-08h/10h pattern on same-weekday control dates is the counterfactual for Nov 10.
  - Method: unit x year x week fixed effects (p. 12) correspond to our within-day contrast per cell and year: the comparison is made inside a narrow cell-time block so that slow cell-specific changes drop out.
  - Robustness: showing that the estimate barely moves from the simplest to the richest fixed effects (Table 3, p. 36).
  - Robustness: lead and lag days as built-in placebos / spillover tests (p. 11, 15).
  - Robustness: "non-event same-weekday dates inside the season show nothing" (Table 6, p. 39).
  - Robustness: redefining the day boundary to fit the event (p. 8). For us: consider whether the hourly bin 09:00-09:59 is the right bin or whether data stamps are hour-ending.
  - Results-Discussion: honest multiple-testing language for secondary estimates (p. 18).
- **Caveats**
  - Thousands of event days across 96 schools with staggered schedules, so date effects can be separated from event effects. We have 5 event days common to every cell; none of their statistical power transfers.
  - Clustering by college with common national calendar shocks is adequate there because game dates differ across schools; it would not be adequate in our setting.
  - Outcome is reported crime, with reporting-rate caveats discussed at length (p. 13); not relevant to traffic.
- **Checks it suggests for us**
  - Add Nov 9 and Nov 11 (lead and lag) to the main table.
  - Show the estimate under: no adjustment; weekday and year adjustment; within-week comparison only.
  - Leave-one-year-out estimates (their leave-one-month-out, Table 4).
  - Placebo on same-weekday November dates that are neither Nov 10 nor its controls.

---

### gulek2024 - Gulek (2024), Driving while hungry: the effect of fasting on traffic accidents

Closest paper to ours: Turkey, a ritual with fixed clock timing, and the IBB traffic density index used directly.

- **Question and setting**: Does hunger from Ramadan fasting raise the probability of a crash, conditional on driving? Journal of Development Economics 168, 103260.
- **Data**
  - Accidents: daily police records of accidents with injury or death in metropolitan areas, by province (81 provinces), 2000-2018, with hour of day; 1,949,204 accidents (p. 4). Deaths are counted only if they occur at the scene, so 1.5% of accidents are "deadly" (p. 4). Gendarmerie areas (intercity roads) are not covered (footnote 10, p. 4). Data cannot be shared (p. 14).
  - Traffic: Istanbul Metropolitan Municipality traffic density index, hourly (value at the beginning of each hour), from 2012, on a 0-100 scale. Built by IBB from average speeds on main roads measured by traffic cameras, as a weighted average of congestion on different roads (p. 4 and footnote 11; Figure 2 note, p. 6). Istanbul is described as the only province with multi-year traffic density records before 2018 (footnote 12, p. 4).
  - Also: Ramadan dates, sunrise/sunset times, daily maximum temperature by province (p. 4).
  - Working days are defined carefully: a central-bank trading day, not a half day, and not an "effective religious vacation" day (official holiday, government extensions, and bridge days people typically take off) (p. 4).
- **Identification from ritual and rush-hour timing**
  - Three channels link Ramadan to accidents: (1) lower driving ability from hunger, (2) fewer trips because of fatigue, (3) lower traffic around sunset because of iftar (Figure 1, p. 5). Only (1) is of interest.
  - Turkey does not change working hours in Ramadan, so the same commuters are on the road in the afternoon rush hour. The author therefore uses accidents between 15:00 and 18:00 on working days (p. 2, 4-5).
  - Exposure check with the IBB index: 24 separate regressions, one per hour, TI_d^h = b0 + b1 Ramadan_d + weekday + month + year FE + other-religious-day indicator, separately for working days and vacations (Figure 2, p. 6). Result: density falls during Ramadan at most hours, but "Ramadan does not affect traffic density during the rush hours of working days" (p. 5). On vacations it does fall at 15-18h (p. 5).
  - From Figure 2 (p. 6; my reading of the plot, approximate): on working days the Ramadan coefficient is about -6 index points around 08-09h, near 0 at 15-18h, and about -14 around 21h (iftar); on vacations about -10 in mid-afternoon and about -19 around 21h. The morning rush-hour drop is not explained by the author (footnote 17, p. 5).
  - To keep iftar (channel 3) out of the 15-18h window, the main sample is 2009-2018, when sunset in Ramadan was always after 18:00 everywhere in Turkey (p. 5; Figure 3, p. 6).
  - The lunar calendar moves Ramadan about 11 days earlier each Gregorian year, which separates Ramadan from season over the sample (p. 2, 5).
  - Dose: Qadr (27th night) is assumed to be the day with the highest fasting rate. Wald/LATE: reduced-form Qadr effect divided by an assumed 84% fasting rate (survey share who fast at all), under three stated assumptions (p. 6).
- **Estimator and inference**
  - Poisson, province-day panel, working days: log E[RTA_{p,d}^{15-18h}] = b0 + b1 Ramadan_d + b2 Qadr_d + Gamma W_{p,d}; W = weekday, month, year, religious-day and province fixed effects. g1 = (exp(b1) - 1) x 100; g2 = (exp(b1 + b2) - 1) x 100; LATE = g2 / 0.84 (eq. 1, p. 6).
  - Standard errors clustered by province in the panel; heteroskedasticity- and autocorrelation-robust in the Istanbul time series (Table 1 note, p. 8).
  - N = 202,176 province-days (panel) and 2,496 days (Istanbul) (Table 1, p. 8).
- **Main findings**
  - Average Ramadan working day: +3.5% accidents at 15-18h (b = 0.0355, SE 0.0121) (p. 7; Table 1, p. 8).
  - With a Qadr indicator: ordinary Ramadan day 0.0290 (SE 0.0117), Qadr additional 0.164 (SE 0.0379); total Qadr effect about 21%; LATE 25% (p. 7; Table 1, p. 8).
  - Istanbul only: Ramadan 0.0916 (about 10%), Qadr additional 0.304, total about 47% (p. 7; Table 1, p. 8).
  - Placebos: day before Qadr -0.0002 (SE 0.0388); on vacation days Ramadan 0.0202 (ns) and Qadr 0.0694 (ns) (Table 1, p. 8).
  - Raw means, Turkey 2009-2018, working days, 15-18h: 72.88 accidents on non-Ramadan days, 88.51 on Ramadan days, 106 on Qadr days. There are only 7 Qadr working days in that sample (and 196 Ramadan working days) (Table A.1, p. 14).
  - Temperature interaction is zero (-0.0011, SE 0.0009), so dehydration is ruled out as the main channel (p. 8).
  - More religious provinces have larger effects: one SD of AKP vote share adds 8% (p. 8; Figure 4, p. 9).
  - RD at the fall clock change: accidents at 14:30-15:30 jump only in 2004-2005, when the change fell inside Ramadan and lengthened the fast before rush hour; nothing in 2000-2003 or 2006-2015. The author warns the test is underpowered and that the 0.3 coefficient should not be taken at face value (p. 9 and footnote 28).
  - Spring clock change: no effect at 15-17h, +5.9% at 18-21h and +6.3% at 21-24h (p. 11).
  - Window robustness: 15-17h, 16-18h, 17-18h, 17-19h give the same qualitative result with less precision (p. 11; Table B.2, p. 18).
  - Fatal accidents only: +18% on an average Ramadan day, Qadr not significant (p. 11).
  - Specification matters for the traffic index: a simple OLS difference shows Ramadan lowering the index by roughly 4 to 6.5 points at 15-18h; the difference disappears once vacations are dropped and weekday, month and year effects are added (Figure A.5, p. 16; magnitudes are my reading of the plot).
- **Usable for our paper**
  - Introduction / Literature: the one published economics paper that links a Turkish ritual with fixed clock timing to road traffic outcomes, and that documents a ritual (iftar) visibly emptying Istanbul roads at a specific hour (p. 5; Figure 2, p. 6).
  - Data: published precedent for the IBB traffic index and a description of how it is built (camera-measured average speeds on main roads, weighted across roads, hourly from 2012) (p. 4, footnote 11). Cite when describing our second data source; our 5-minute series is a finer version of the same family of index, but confirm with IBB that the construction is unchanged.
  - Method: hour-by-hour regressions of the index on an event indicator with weekday, month and year effects (Figure 2 note, p. 6). This is the regression counterpart of our date-level DiD by hour.
  - Method: separating working days from vacations and defining "effective" holidays (p. 4). Needed for our all-year control pool.
  - Robustness: Figure A.5 (p. 16) as a cautionary example: naive event-vs-other-days differences in the Istanbul index can be entirely composition.
  - Robustness: lead-day placebo (day before Qadr) and vacation-day placebo (p. 7; Table 1, p. 8).
  - Robustness: window-definition table (p. 11).
  - Results-Discussion: Fig. A.4 (p. 16) shows the average working-day index peaking near 08h and again near 18h (my reading: about 46 at 08h, about 40 at 09-10h, about 57 at 18h). The siren hour sits on the falling shoulder of the morning peak.
- **Caveats**
  - The outcome is accidents; traffic density appears only as a check that exposure is constant at 15-18h. The paper does not estimate a speed or delay effect of any ritual, and has no minute-level event.
  - The key "dose" day rests on 7 Qadr working days. Treatment is national and common to all provinces on a date, while standard errors are clustered by province; the paper does not discuss common date shocks. (My remark: this is the same "effective sample is dates" problem as ours, so the Qadr standard error is probably too small; the Istanbul time-series column with HAC errors is the more comparable one.)
  - Significance stars in Table 1 (p. 8) and the text disagree slightly: the text calls the 3.5% effect significant at 1% (p. 7), the table gives it two stars under a legend where two stars means 5%.
  - The 25% LATE depends on the assumed 84% fasting rate on Qadr (p. 6); the reduced-form numbers are the ones safe to quote.
  - Traffic density evidence is Istanbul only; the accident panel is all Turkey (p. 7).
- **Checks it suggests for us**
  - Estimate hour-by-hour Nov 10 coefficients for all 24 hours (or 06h-12h) with weekday/month/year effects on the hourly cell data and on the IBB index, and plot them as in Figure 2.
  - Split by working day vs weekend. (My remark: 10 November fell on Tue 2020, Wed 2021, Thu 2022, Fri 2023 and Sun 2024, so one of our five event days is a Sunday with very different 09h traffic; report with and without 2024, or weekday-only.)
  - Build an "effective working day" flag for control dates. (My remark, not from the paper and to be verified against the MEB calendars: since 2019 the school mid-term break falls in the week containing or following 10 November in several years, which would put the +7 control date inside a school holiday and change the 08-09h profile.)
  - Dose-response: larger effect where compliance is plausibly higher or roads freer (our speed classes), tested as a pre-specified ordered hypothesis rather than five separate tests.
  - Reproduce the Figure A.5 exercise for our contrast: raw difference, then adding weekday and year adjustment, to show how much is composition.

---

## Cross-paper synthesis (what jointly matters most for our design)

1. The "same weekday, one week before and one week after" double control is the standard design for a fixed-date event (redelmeier2003 p. 12, 2008 p. 1, 2012 p. 2, 2024 p. 2; staples2018 p. 2). All use exactly 2 control days per event day and the identical clock window on control days. Our Nov 3 / Nov 17 pair is this design; Nov 24 is an extra, one-sided control.
2. Its usual inference (binomial or Poisson on pooled counts) is badly anticonservative: 43% false rejections on placebo Tuesdays (zhang2016 p. 3), and a CI of 1.05-1.19 becomes 0.97-1.28 once day-to-day overdispersion is allowed (harper2019 p. 18). Inference must treat dates as the sample; our randomization test over dates is in the family that the critics recommend.
3. Widening the control pool is the decisive robustness test: 4/20 goes 1.12 -> 1.05 -> 0.98 while 4 July stays near 1.4 (harper2019 p. 18); the election effect keeps its size but P rises to 0.07 against 200 placebo Tuesdays (zhang2016 p. 3). We should show the ladder (+/-7; symmetric +/-7 and +/-14; window; all year) and a positive-control event.
4. Widening without adjusting for season and weekday trades variance for bias (harper2019 appendix p. 14 has no such controls). Demean by weekday and year and handle season (smith2016 p. 9), drop holidays and bridge days (smith2016 p. 7; gulek2024 p. 4).
5. Use the same statistic on every pseudo-event date and show where the true date falls (zhang2016 p. 2; harper2019 Fig. 2, p. 7; smith2016 p. 13-14, permutation P = 0.007), excluding dates contaminated by the true event (smith2016 footnote 28).
6. Common shocks require aggregation or clustering at the shock level: national daily series (smith2016 p. 7-8), team x season clusters (card2011 p. 26). Province clustering with a national day-level treatment (gulek2024 p. 8) is the pattern to avoid.
7. Timing specificity is the strongest causal evidence available without randomization: no effect before the event, effect in the event window, window shifts when the event shifts (redelmeier2003 p. 12; staples2018 p. 2; card2011 p. 28; lindo2018 p. 16). Report 08h, 09h, 10h and non-event hours separately, plus Nov 9 and Nov 11 (redelmeier2008 p. 1; lindo2018 p. 15).
8. Check for displacement into neighbouring hours, since effects can net to zero over the day (zhang2016 p. 3; smith2016 p. 16); this matters doubly for us because 08h and 10h are our within-day controls.
9. Several headline results rest on very few event days (8 elections; 1 eclipse; 7 Qadr working days, gulek2024 p. 14). Five Nov 10 mornings is not unusual for this literature, but it is the reason the surviving results are the large ones (4 July, DST); our 0.45-0.73 minute estimates across 5 speed classes need a multiplicity-aware, pre-specified presentation (lindo2018 p. 18 for wording).
10. gulek2024 gives the Turkish precedent: the IBB index as a published data source (p. 4), ritual timing visibly moving Istanbul traffic (iftar, Fig. 2, p. 6), working-day vs vacation splits, and a warning that naive index comparisons vanish with weekday/month/year controls (Fig. A.5, p. 16). It does not measure a speed effect of a ritual; that gap is ours.
