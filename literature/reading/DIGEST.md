# DIGEST of reading notes 01-12 (77 papers)

Built only from `01_*.md` to `12_*.md`. `[key p. N]` is the PDF page of the file on disk, as in the notes; often not the journal page (section 3). **OURS** marks a mapping, derivation, arithmetic or simulation by us or the note-writer: never attribute it to the paper. Nothing here is a direct quotation. Shorthand: c = date-level within-day contrast; D_y = yearly DiD; D = mean of D_y; K = 4^5 = 1024 assignments.

## 1. Citable claims by section of our paper

### 1.1 Introduction

- The vehicle stop is as old as the ritual: on 10 Nov 1939 Istanbul trams and vehicles stood still for five minutes at 09:05 (one source, Cumhuriyet) `[uzun2019 p. 8]`. The 1939 programme itself covered only party meetings, schools, press and radio `[uzun2019 pp. 6, 34-35]`.
- Horns with factory, ferry and ship sirens are first reported for 1950-60 `[uzun2019 p. 15]`, continue through 1960-88 `[uzun2019 pp. 21-22]` and on 10 Nov 1988, after official mourning ended `[uzun2019 pp. 24, 26-27]`.
- Life is described as almost stopping at that moment `[uzun2019 pp. 27-28]`, without obligation and by people's own will `[uzun2019 pp. 1, 27, 28]`. No rule obliging drivers is cited; a historian's assertion, not legal analysis.
- 1988 PİAR poll: 89.7% said a standing silence should be held at 09:05, 7.8% not necessary, 2.5% no opinion; sample and method unreported `[uzun2019 p. 25]`. A stated norm, not behaviour.
- The 9:05 standing is a repertoire known to all Turks `[goldman2018 pp. 2-4]`. A moment of silence recurs at the exact time of the event and is strongest when framed by a nationwide siren and a norm to stand still `[vinitzky2010 pp. 6-7]`; in Israel (one- and two-minute sirens) highway drivers are commonly seen stopping and standing by their cars `[vinitzky2010 p. 7]`.
- Gap: the leading economics paper on a national holiday had no attendance data and proxied participation with rain `[madestam2011 p. 4]`. **OURS**: none of the twelve commemoration and nationalism papers measures compliance with a siren.
- Shared national experiences have effects: -5.3 pp ethnic-over-national identification after a victory (SE 0.016, FDR p = 0.010); 8.6% fewer conflict events after qualification `[depetris2020 pp. 14-15, 26]`.
- Closest infrastructure analogue: Earth Hour; 274 reported demand changes (10 countries, 2007-2012) average a 4.0% reduction, median 2.6% `[meier2014 p. 5]`.
- A treatment imposed suddenly and short-lived is the favourable design case `[rosenbaum2002book pp. 350-351, 364-365]`. **OURS**: the siren is neither unexpected nor haphazard.
- Why exact inference: in 53 experimental papers randomization tests find 13-22% fewer significant coefficients and 33-49% fewer significant table-level joint tests `[young2019 p. 2; Tables V, VII pp. 41, 43]`; with few treated groups a DiD estimate is not consistent however many individuals are observed `[conley2011 pp. 2, 6-7, 10]`.

### 1.2 Literature

**(a) Commemorative silences and civil religion in Turkey**

- Five minutes in 1939 and in parliament in 1947 `[uzun2019 pp. 6, 13-14]`; Uzun's only present-day remark is one minute `[uzun2019 p. 3]`. Atatürk Haftası: 1960, schools 1963 `[uzun2019 pp. 18-21]`. Mourning rules lifted 1988 `[uzun2019 p. 24]`.
- Peer enforcement: in 1959 a crowd confronted a Greek freighter that did not join the sirens `[uzun2019 p. 18]`. Participation moves with the political atmosphere `[uzun2019 p. 28]`.
- Late-1990s Atatürk imagery was privatised; informants contrast the imposed 1980-83 campaign with freely chosen practice `[ozyurek2004 pp. 2, 6-7]`. Buyers: middle class, secular, long-settled urban, anti-Islamist `[ozyurek2004 p. 2]`. Claimed voluntariness masks state power `[ozyurek2004 pp. 4, 15]`. Nothing on 10 November.
- A record 1,089,615 visited Anıtkabir on 10 Nov 2013, over double the previous year `[goldman2018 pp. 14-15]`; after 15 July 2016 secularist and conservative participation blurred `[goldman2018 pp. 15-16]`.
- Civil religion: beliefs, symbols and rituals about sacred things, institutionalised in a collectivity, with an annual ritual calendar `[bellah1967 pp. 3, 7, 10]`; ritual is not mere ceremony `[bellah1967 p. 2]`; anticlerical France is the contrast `[bellah1967 p. 12]`. **OURS**: Kemalism fits the French case better; Bellah never mentions Turkey.
- Whether Kemalism is a civil or political religion is contested `[karakus2023 pp. 2-3, 7]`. Covers 1920-38 only.
- Silence typology: overt or covert, for memory or forgetting `[vinitzky2010 p. 6]`. Compliance is internalised without surveillance `[vinitzky2010 p. 7]`; estranged groups opt out `[vinitzky2010 pp. 8-9]`; norm-breakers provoke antagonism `[vinitzky2010 p. 15]`.

**(b) Collective behaviour measured in passive data**

- Standard counterfactual = same time slot in other weeks `[bagrow2011 pp. 2, 7; pinter2021 p. 3; ngeni2022 pp. 4, 6]`; on İBB speeds, the mean of the previous three same weekdays `[takak2021 pp. 8, 11]`.
- Inference there is weak or absent: z > 1.5 threshold `[bagrow2011 p. 7]`; eyeballed z bands `[pinter2021 pp. 5, 9]`; mean ± 1.96 SD/sqrt(n), n about 5 `[ngeni2022 p. 4]`; unweighted mean of reports `[meier2014 pp. 4-5]`. **OURS**: ngeni's band is about 3.5 times too narrow.
- Eclipse: interstate volume 7% and 19% below the upper band edge at 10:00 and 11:00, then 14-26% above it for four hours `[ngeni2022 pp. 6-7; Table 6 p. 9]`; confounded by inbound visitors.
- Matches: phone activity dips below baseline `[pinter2021 pp. 4-5]`.
- Head-counts need ground truth: attendance, N = 10, adjusted R² 0.771-0.937 `[botta2015 pp. 4-5]`.
- Baselines drive answers: Earth Hour figures use forecasts (196), "normal" demand (64), just-before (6), unknown (8); one prior-week comparison is called inadequate `[meier2014 pp. 4-5]`. Rebound: 3% dip at kick-off, about 7% surge after `[meier2014 p. 4]`.
- Madrid flags rose from 0.16 per street by about three (315 streets) `[dinas2024 pp. 6-7]`, about 40% closer together than random `[dinas2024 pp. 13-15]`. Barcelona: 2.6% of households display against 42.2% pro-referendum vote; 63% of block-days clustered against 50% expected `[parravano2015 pp. 6-7, 18]`. Direct observation avoids self-report bias `[parravano2015 p. 2]`.
- Self-reported flag display after 9/11: 74% of N = 605; patriotism .34, nationalism .05 (ns) `[skitka2005 pp. 5, 8, 11]`.
- Per rain-free 4 July at ages 4-18: +0.61 pp Republican identification (SE 0.30), +0.88 pp turnout `[madestam2011 pp. 19-21]`.

**(c) One-day event studies and their fragility**

- Double control (same weekday ±1 week, same clock window): Super Bowl, 27 events, +41% fatalities after telecast, in 21 of 27 years `[redelmeier2003 p. 12]`; elections, 8 events, RR 1.18 (1.10-1.26) `[redelmeier2008 p. 1]`; tax day, 30 events, OR 1.06 (1.03-1.10) `[redelmeier2012 p. 2]`; 4/20, 25 years, RR 1.12 (1.05-1.19) `[staples2018 p. 2]`; eclipse, one event, RR 1.31 (1.15-1.49) `[redelmeier2024 pp. 2-3]`. Rationale: weekday, season, year fixed `[redelmeier2012 p. 2; staples2018 p. 2]`.
- Against 200 placebo Tuesdays the election result is RR 1.17, p = 0.070, CI 0.99-1.35; the binomial test rejects on 43% of ordinary Tuesdays; 24-hour RR 1.04 (p = 0.570) `[zhang2016 pp. 2-3]`. Pools of 12, 25, 50 Tuesdays: p = 0.04, 0.06, 0.05 `[zhang2016 p. 3 fn 2]`.
- 4/20: IRR 1.12 has Poisson CI 1.05-1.19 but 0.97-1.28 negative binomial; ±7 and ±14 controls give 1.05; all other days 0.98 (0.88-1.10); 4 July stays near 1.4 `[harper2019 pp. 2, 6; Table 4 p. 18]`. Two days a week apart is called arbitrary `[harper2019 p. 5]`.
- DST: spring RD +6.5% (0.0649, SE 0.0231), placebo dates 0.0005, permutation p = 0.007 with contaminated dates excluded `[smith2016 pp. 13-14, fn 28]`; light only reallocates crashes within the day `[smith2016 Table 3 p. 16]`.
- Timing specificity: upset loss +10% (0.112, SE 0.034) in the window at game end, clustered by team x season `[card2011 pp. 25-28]`; game days +28% (0.283, SE 0.045), non-game Saturdays -0.027 (SE 0.075) `[lindo2018 p. 15; Table 6 p. 39]`.
- Turkey: Ramadan working days +3.5% accidents at 15-18h (0.0355, SE 0.0121); Qadr about 21%, on 7 Qadr working days `[gulek2024 pp. 7-8; Table A.1 p. 14]`. A naive Ramadan gap in the İBB index vanishes with weekday, month and year effects `[gulek2024 Fig. A.5 p. 16]`.
- Drift: before/after on unaffected freeways gave a spurious +32.3% (t = 7.0); delays rise through October-November `[anderson2014 p. 14 fn 13; p. 20]`.

**(d) Traffic shocks in economics**

- LA strike, 35 days: delay +0.194 min/mile (SE 0.041), 47% of delay over free flow; hourly loop data; two-way clustering by day and detector `[anderson2014 pp. 14-17; Table 4 p. 35]`. **OURS**: about +14% travel time.
- 71 German one-day strikes: probe index, morning peak +0.123 (SE 0.051, p = 0.07) on 1.47, +8.4%; 5 city clusters `[bauernschuster2017 pp. 12, 15, 21-22]`.
- Rome: a 10-point transit cut raises morning-peak travel time 1.6% (-0.160, SE 0.031), 0.024 min/km; log travel time `[adler2021 pp. 11, 15; Table 4 p. 16]`. Hourly data ignore within-hour variation; spot speeds miss time stopped at lights `[adler2021 p. 6 fn 12; p. 7]`.
- Jakarta: +0.98 min/km (SE 0.07, +46%) morning, +2.48 (+87%) evening; Google times every 10 minutes; no change at 6-7 a.m. or night `[hanna2017 pp. 1, 3-4]`.
- Beijing: IV speed-density slope -1.098 km/h per vehicle per lane-km (SE 0.044); OLS -0.67 to -0.75 `[yang2020 Tables 6, 8 pp. 18, 20]`.
- **OURS** (note 08): no paper studies a shock shorter than hours or differences an hour against adjacent hours.

**(e) Traffic-flow theory and probe measurement**

- v_t = v_s + sigma_s²/v_s exactly `[wardrop1952 pp. 5-7, 32]`; with CV 0.25-0.35 the time-mean is 6-12% higher `[wardrop1952 p. 7]`. Space-mean = vehicle-miles/vehicle-hours `[wardrop1952 p. 29]`; running speed excludes stops `[wardrop1952 p. 31]`.
- Measured gap: 1-5% typically, 10-30% in congestion `[rakha2005 p. 3]`; space/time ratio about 0.56-0.67 near 20 km/h, near 1 above 70-100 km/h `[knoop2009 p. 4]`.
- Probes: temporal versus spatial sampling `[herrera2010 p. 6]`; time sampling returns more slow observations in congestion `[herrera2010 p. 15]`; crossing-triggered readings are time-mean speeds `[herrera2010 pp. 17, 20]`; 2-3% penetration sufficed on one freeway-day `[herrera2010 pp. 22-23]`.
- Point-stop discharge and clearing times `[lighthill1955 p. 24; richards1956 p. 9]`; lost time 5-10 s per start `[lighthill1955 p. 27]`. Measured backward waves about 20 km/h `[knoop2009 p. 5]`; -15.6 and -3.6 mph `[herrera2010 pp. 27-28]`.
- GPS measures routinely drop trips with stops `[kreindler2024 p. 13]`.

### 1.3 Data: what is and is not known about the İBB data

Known:

- Columns: DATE_TIME, LONGITUDE, LATITUDE, GEOHASH, MINIMUM_SPEED, MAXIMUM_SPEED, AVERAGE_SPEED, NUMBER_OF_VEHICLES `[utku2023 p. 5; tanberk2023 Fig. 1, PDF p. 3]`. Six-character geohashes appear only in that screenshot.
- Unit counts disagree: 2,321 points, Jan-May 2021 `[utku2023 p. 5]`; 2,451 "sensors" over four years `[olug2024 pp. 1-2]`; 14,183,614 rows for Jun 2020-May 2021 and "more than 7 thousand" points `[tanberk2023 pp. 1, 4]`; 1,455 sensors in an IMM product `[energies2021 p. 6]`.
- About 2.5% of hours missing in 2022, no systematic pattern `[ozkurt2025 p. 6]`.
- NUMBER_OF_VEHICLES is read as hourly vehicles passing, never with a source `[utku2023 p. 5; ozkurt2025 p. 6; olug2024 p. 2]`.
- Rows show a 177 km/h maximum and a one-vehicle hour with min = max = mean; unit km/h `[ozkurt2025 p. 5]`. MINIMUM_SPEED = 1 occurs in May 2021 `[tanberk2023 Fig. 1, PDF p. 3]`.
- Monthly city mean speed 55.2-59.0 km/h, Jan-May 2020 `[energies2021 p. 8]`; one-hour-ahead MAE about 4 km/h at the busiest cell `[utku2023 p. 10]`; same-weekday MAPE 20-29% at volatile sites, worse in December and on Fridays `[takak2021 p. 10]`; locations sit on busy roads `[energies2021 pp. 8, 11]`.
- İBB holds a fixed-sensor database (2017: 7,000 sensors, one-minute, directional) `[takak2021 p. 2]`; link to the open file unknown.
- Index: 1-99, higher is more congested, hourly `[alcan2022 p. 2]`; elsewhere 0-100, built from camera-measured average speeds on main roads, hourly from 2012 `[gulek2024 p. 4, fn 11]`. 2020: about 30 in January-February, 10 in April `[alcan2022 pp. 4-5]`.

Not known:

- How the open geohash data are produced: no İBB paper mentions probes, GPS, providers, sensor technology, or what AVERAGE_SPEED averages (reader's finding, note 10).
- A citable definition of the 5-minute index; a primary source for who sounds today's siren and for how long (the earlier two-minute figure came from news sites).
- **OURS**, not citable: NUMBER_OF_VEHICLES looks like a sample (about 1,350 per hour at the busiest junction, figure in `utku2023` p. 6); olug's "sensors" are probably cell centroids; the MINIMUM_SPEED floor may have been 6 km/h in June 2020 and 1 by May 2021 (ten rows, `tanberk2023` Fig. 9); if stationary pings are dropped AVERAGE_SPEED is a running speed.
- To verify: 10 Nov fell Tue 2020, Wed 2021, Thu 2022, Fri 2023, Sun 2024 (reader's arithmetic); the school break may cover the +7 control (reader's memory). Other ritual-day shocks: 09:05 school and office ceremonies `[uzun2019 pp. 6, 21]`; travel to Dolmabahçe `[goldman2018 p. 12]`.

### 1.4 Method

**Randomization/placebo inference with few treated units**

- The DiD error is a fixed combination of the treated groups' own shocks `[conley2011 p. 10; alvarez2023 p. 7]`; a single treated cluster contributes zero to the cluster-robust variance `[ferman2019 pp. 3, 8; mackinnon2017 p. 12]`.
- CRVE t-tests reject 77.75% at 5% with one treated of 50 clusters `[mackinnon2017 p. 13]`; robust tests reject over 50% at intra-state correlation about 0.031 `[mackinnon2017 p. 17]`. Wild cluster bootstrap with G1 = 1 never rejects (restricted) or over-rejects (unrestricted) `[mackinnon2017 pp. 12-15]`; the ordinary wild bootstrap fails at G1 = 1 with rho > 0.02 `[mackinnon2018 p. 12]`.
- Conley-Taber takes the null from control residuals: HOPE CI (0.025, 0.119) clustered against (-0.006, 0.212); needs shocks i.i.d. across groups, independent of treatment, many controls `[conley2011 pp. 8-11; Table 1 p. 47]`; analogy to end-of-sample break tests `[conley2011 p. 5]`.
- RI-beta is exact unconditionally and with homogeneous clusters; over-rejects when the treated cluster is smaller than typical; RI-t is no better with one treated cluster; RI-beta has more power `[mackinnon2020 pp. 5, 8-13, 15]`.
- Placebo-law RI: size 4-6.5% with 6-51 states; power against a 2% effect 23.5% (51 states), 7% (6) `[bertrand2004 pp. 22-23; Table 11 p. 38]`.
- Placebo clusters may be stretches of time; exact under permutation invariance; no rejection possible if C(q, q1) < 1/alpha `[hagemann2019 pp. 4, 9]`.
- Our assignment space in print: Q = prod(J_g + 1) `[firpo2018 pp. 18-19]`; one village per pair, 2^12 = 4096 enumerated `[hess2017 pp. 12-14]`; K = prod C(n_s, m_s) `[rosenbaum2002book pp. 36-38]`.
- Unit = assignment level `[hess2017 p. 6; athey2017 pp. 4-5, 44; wu2021 p. 16; roth2023 p. 43; young2019 pp. 33-34]`; RI is most valuable with few groups (Angrist-Imbens comment) `[rosenbaum2002 p. 21]`.
- Uncertainty remains with the whole population observed `[abadie2020 pp. 19-20; athey2017 pp. 8-9; abadie2010 pp. 4-5]`. Same-weekday placebo-date null `[zhang2016 pp. 2-3]`.

**Exact conditions**

- p = share of equally likely assignments at least as extreme, observed included; exact for any sample size under the sharp null `[ernst2004 p. 4; young2019 pp. 14-16; athey2017 pp. 15-16; rosenbaum2002book pp. 40-41; romano2005b p. 10]`.
- It rests on known physical randomization `[ernst2004 p. 2; athey2017 pp. 5, 10-12; young2019 p. 7]`; without it the name randomization inference is inappropriate `[mackinnon2020 p. 6]` and equal probabilities are a disputable assumption `[rosenbaum2002book pp. 42, 90, 92]`.
- Wording: significance against a uniform benchmark assignment distribution; Fisher inference only under random assignment, called restrictive or improbable `[abadie2010 p. 5; abadie2015 p. 6; abadie2021 p. 14]`; a benchmark priced by an assignment assumption and a sharp null `[roth2023 pp. 40-41]`.
- Permuting a non-experimental regressor gives the distribution under no effect and no dependence along the permuted dimension `[hess2017 p. 6]`. **OURS**: date permutation keeps cross-cell correlation, assumes away within-year trend.
- Time-series route: exchangeable data and an order-invariant estimator with the null imposed give P(p <= alpha) <= alpha `[chernozhukov2021 p. 47]`; non-stationarity with a misspecified proxy is excluded `[chernozhukov2021 p. 23]`; misspecified DiD then rejects 0.33-0.97 at nominal 10% `[chernozhukov2021 Tables I.3-I.4, p. 99]`.
- Re-randomize only among units sharing the treated unit's known characteristics `[mackinnon2020 p. 5]`.
- Homogeneity: var(W_j) = A + B/M_j; a treated group with fewer observations over-rejects (about 22% against 4% across size quintiles, 10% test); large M does not help when within-group correlation is near zero `[ferman2019 pp. 10, 16-18, 22]`.
- Raw-statistic permutation tests are exact for equal distributions, not equal means; studentizing restores asymptotic validity `[chung2013 pp. 2-3, 7-8]`; design-based version needs 2+ units per arm and stratum `[wu2021 pp. 4, 9, 12, 18]`.
- Bounded null: for effect-increasing statistics (difference in means included) the one-sided sharp-null p-value is finite-sample valid for "no unit's effect exceeds delta", blocking allowed `[caughey2023 pp. 10, 12, 33]`; also `[rosenbaum2002book p. 56]`.
- DiD language: parallel trends, no anticipation, SUTVA `[roth2023 pp. 5-7]`; one common date avoids staggered-adoption problems `[roth2023 pp. 8, 47]`; functional-form dependence `[roth2023 p. 22]`.

**Statistics**

- Any statistic is valid; choice changes power `[ernst2004 pp. 4-5; romano2005b p. 10]`; ranks `[athey2017 pp. 16-17]`; aligned ranks `[rosenbaum2002 pp. 15-16]`.
- Unbalanced 10/90, n = 20, nominal .05: robust 0.241, randomization-t 0.046, randomization-c 0.048; with heterogeneous effects randomization-c 0.129-0.195 `[young2019 Table III p. 39]`.
- Power at 10% in a synthetic-control Monte Carlo: permuted DiD 0.18-0.70, RMSPE ratio 0.32-0.77, t-type 0.63-0.95; trimming placebos by fit moves size to 0.13 or 0.06 `[firpo2018 Tables 1-2 pp. 13-15]`.
- Ratio statistic r_j = R_j(post)/R_j(pre), p = (1/(J+1)) sum 1{r_j >= r_1}, one-sided via negative parts `[abadie2021 pp. 13-14]`; California p = 1/39 `[abadie2010 p. 11]`; West Germany 1/17 `[abadie2015 p. 11]`.
- One-sided tests `[conley2011 p. 23; abadie2021 p. 14; hagemann2019 p. 8; wu2021 p. 16; list2019 p. 11]`.
- Discreteness: p is a multiple of 1/K `[ernst2004 p. 4]`; under 20 assignments nothing reaches 0.05 `[rosenbaum2002book p. 99]`; ties count against the result `[hess2017 p. 7]`. **OURS**: floor 1/1024; 5% cutoff 51/1024; pilot values about 8 and 35 of 1024.
- Sampled assignments: p = (1 + count)/(M + 1), valid for any M `[ernst2004 p. 7; young2019 p. 16; romano2005b pp. 10-11]`.
- Estimand: average realised effect on the observed treated unit-periods, estimated separately then aggregated `[alvarez2023 pp. 3-5]`; cluster- and unit-weighted estimands both legitimate `[athey2017 pp. 44-45]`; flow weights `[anderson2014 p. 16; adler2021 p. 12]`.
- Scale: log travel time or speed `[adler2021 p. 11; akbar2023 pp. 14, 16]`; constant in levels is not constant in logs `[ding2016 pp. 3-4]`; test on speeds, report journey time `[wardrop1952 pp. 9, 29]`.

**Intervals**

- Invert the test under a constant additive effect `[ernst2004 p. 5; rosenbaum2002 p. 4; rosenbaum2002book pp. 56-58; young2019 p. 15; firpo2018 p. 10; chernozhukov2021 p. 12; bertrand2004 p. 21 fn 33; conley2011 p. 11]`. Hodges-Lehmann estimate `[rosenbaum2002book pp. 60-61]`; with OLS residuals it equals the fixed-effects coefficient `[rosenbaum2002 pp. 5, 16]`.
- Without constant effects the inverted one-sided interval bounds the maximum unit effect `[caughey2023 p. 13]`; intervals inform through excluded values `[rosenbaum2002 pp. 39-40]`; studentized inversion is asymptotically conservative for the average `[wu2021 p. 15]`.
- One treated per stratum: within-stratum variance not estimable; pair formula V = [1/((N/2)(N/2-1))] sum (tau_g - tau)² `[athey2017 pp. 33-34]`. **OURS**: year-level analogue, 4 d.f.
- Covariates: permute residuals of aligned, tau0-adjusted responses; exact whatever the fit `[rosenbaum2002 pp. 4-5, 15-16]`.

**Multiple testing**

- Five independent true nulls at 5%: 22.6% chance of a false rejection `[list2019 p. 5]`; subgroups are a family defined by baseline covariates `[list2019 pp. 6-7]`.
- FWE, strong control, Bonferroni, Holm; conservative under positive dependence `[romano2005a pp. 6-8]`.
- Exact stepdown: with one common transformation group, max-statistic critical values are monotone and FWE is controlled in finite samples, bounded by the level of the intersection test `[romano2005b pp. 9, 11, 12]`.
- Related: max-statistic `[ernst2004 pp. 9-10; alvarez2023 p. 11]`; Westfall-Young min-p `[young2019 pp. 19-20, 34-35]`; permutation min-p `[firpo2018 pp. 16-18]`; joint null from one run `[hess2017 pp. 7-8]`; FDR `[depetris2020 p. 11]`.
- Parallel: a subgroup at unadjusted 0.0503 becomes 0.1427 (stepdown), 0.1510 (Holm), 0.2013 (Bonferroni) `[list2019 Table 2 p. 15]`. **OURS**, pilot: Bonferroni 0.040 and 0.170; Holm 0.040 and 0.136.

**Sign-change test**

- Procedure in section 2.3 `[canay2017 pp. 3-4, 7-10]`. DiD form valid with few periods only under strong i.i.d. assumptions on pre- and post-average errors `[canay2017 pp. 11-12]`; competing t-test valid for alpha <= 8.3% and possibly very conservative `[canay2017 p. 5]`; simulations at q = 8, 16 only.
- **OURS**, q = 5: one-sided floor 1/32 = 0.031, only if all five D_y are negative; two-sided floor 0.0625; no multiplicity-adjusted claim possible; skewed date shocks with a precise control mean break symmetry (simulated 6.2% with three controls, 9.7% with fifty, nominal 3.1%).

### 1.5 Robustness: each check and the paper that motivates it

1. Control-pool ladder: `[harper2019 p. 5; Table 4 p. 18; zhang2016 p. 3 fn 2; meier2014 p. 5; bertrand2004 pp. 22-23; roth2023 pp. 18-19]`.
2. Symmetric controls, bracketing, trend: `[anderson2014 p. 14 fn 13; roth2023 pp. 33-34, 36; rosenbaum2002book pp. 276-277, 280; chernozhukov2021 p. 23]`. **OURS**: controls at positions 1, 3, 4 around 2 bias D by -0.67 s for weekly slope s; positions 1 and 3 by 0.
3. Pseudo-event dates, uniform placebo p-values, contaminated dates excluded: `[conley2011 p. 23; harper2019 pp. 5-6; Table 8 p. 20; smith2016 p. 13 fn 28; chernozhukov2021 pp. 44-45]`.
4. Adjacent days: `[redelmeier2008 p. 1; staples2018 p. 2; lindo2018 pp. 11, 15; gulek2024 Table 1 p. 8]`; joint test `[madestam2011 pp. 20-21]`.
5. Placebo hours, timing specificity: `[redelmeier2003 p. 12; card2011 pp. 27-28; adler2021 p. 15 fn 29; hanna2017 p. 4; abadie2015 pp. 5-6, 10-11; abadie2021 pp. 24-25]`; a quiet placebo does not reduce sensitivity `[rosenbaum2002book pp. 229-232]`.
6. Displacement and a contaminated 10h reference: `[zhang2016 p. 3; smith2016 Table 3 p. 16; meier2014 p. 4; ngeni2022 pp. 7, 9; lighthill1955 p. 24; rosenbaum2002book pp. 232, 363-365]`.
7. Placebo outcome (vehicle counts): `[bauernschuster2017 pp. 23-24; adler2021 pp. 18-19; dinas2024 p. 8]`; flow can fall while delay rises `[anderson2014 p. 19]`.
8. Size and power by simulated sirens: `[bertrand2004 p. 9]`; pre-tests are weak `[roth2023 pp. 30-31]`.
9. Heteroskedastic dates (counts by date, balanced panel, regression on 1/M): `[ferman2019 pp. 10, 12, 16; mackinnon2020 pp. 8-10; mackinnon2018 p. 14; conley2011 pp. 21-22; anderson2014 p. 15]`.
10. Studentized and rank rows: `[chung2013 p. 8; wu2021 p. 9; young2019 p. 18; hagemann2019 p. 7; athey2017 pp. 16-17]`; coefficient test stays headline for power `[mackinnon2020 p. 13]`.
11. Sign-change and t(4) on five D_y: `[canay2017 pp. 4-5, 9-10]`.
12. Sensitivity to non-uniform assignment: `[rosenbaum2002 pp. 10-12, 21; rosenbaum2002book pp. 119-121, 133; firpo2018 pp. 6-8]`.
13. Leave-one-out: `[abadie2015 p. 12; abadie2021 pp. 24-25; young2019 p. 11; botta2015 p. 5; depetris2020 p. 16 fn 11; lindo2018 Table 4 p. 37]`. Not `mackinnon2017`.
14. Weather: `[rosenbaum2002book p. 85; rosenbaum2002 pp. 4-5, 16; bauernschuster2017 p. 14; madestam2011 pp. 19, 41]`.
15. Donor-pool rules fixed in advance (holidays, school breaks, curfews, mass events): `[abadie2010 pp. 6-7; abadie2015 p. 6; abadie2021 p. 19; smith2016 p. 7; gulek2024 p. 4; bauernschuster2017 pp. 11, 27-28]`.
16. Without 2024 (Sunday) and without 2020: `[akbar2023 p. 19; alcan2022 pp. 4-5; energies2021 p. 8]`.
17. Vehicle-weighted beside equal-weighted: `[athey2017 pp. 44-45; anderson2014 p. 16; adler2021 p. 12]`.
18. Functional form and class definition: `[roth2023 p. 22; anderson2014 pp. 14-15; adler2021 p. 7; olug2024 p. 5]`.
19. No trimming by fit; ratio statistic: `[firpo2018 Table 2 pp. 14-15; abadie2010 p. 11; abadie2021 p. 13]`.
20. Positive control and benchmark effects: `[harper2019 p. 6; card2011 p. 38]`.
21. Serial dependence: persistent treatment over-rejects (up to 67.5%), on/off treatment gives 6% `[bertrand2004 pp. 10-12]`; `[hagemann2019 p. 10; smith2016 p. 12 fn 27; kreindler2024 p. 15]`.
22. Specification ladder: `[card2011 p. 27; lindo2018 Table 3 p. 36; rosenbaum2002book pp. 362-364; gulek2024 Fig. A.5 p. 16]`.
23. Coherence across classes: separate p 0.023 and 0.057, combined 0.0073; coherent biases also cohere `[rosenbaum2002book pp. 289-298]`.
24. Naive SE row as contrast: `[mackinnon2017 pp. 13, 17; zhang2016 p. 3]`.
25. Heterogeneity: FRT-CI `[ding2016 p. 7]`; plug-in tests over-reject, 11.3-15.1% `[ding2016 Table 1 p. 12]`; subgroup nulls do not test differences `[list2019 p. 7]`.
26. Averaging-rule diagnostics (section 2.2): **OURS**.

### 1.6 Discussion

**Norm-driven participation**

- Social norm (Bicchieri): a rule followed if one believes enough others follow it and think it should be followed `[dinas2024 p. 3]`.
- Non-obligatory and self-sustained `[uzun2019 pp. 1, 27, 28]`; internalised without surveillance, with antagonism toward breakers `[vinitzky2010 pp. 7, 15]`.
- National days reconfirm commitments and create common knowledge (Chwe) `[madestam2011 p. 7, fn 4]`; possible social multiplier `[madestam2011 p. 12 fn 15]`.
- Mass symbolic acts track solidarity more than hostility `[skitka2005 pp. 11, 14]`.
- Cautions: public behaviour moved while private preferences did not `[dinas2024 pp. 10-11, 15]`; most holders of a preference do not act, and national-day acts may be tradition `[parravano2015 pp. 6-7, 14]`; conformity unmeasured `[skitka2005 p. 15]`; voluntariness can mask state power `[ozyurek2004 pp. 4, 15]`.
- Gradient: secular middle-class profile `[ozyurek2004 p. 2]` against blurred lines after 2016 `[goldman2018 pp. 15-16]`; political climate `[uzun2019 p. 28; goldman2018 p. 14]`; local majority stimulates, minority inhibits `[parravano2015 pp. 7, 22-23]`.
- **OURS**: a stopped car stops those behind, so clustering cannot identify social influence; in the flag papers the act was counter-normative or costly, here stopping is the norm; vehicles in a cell are not residents; s = m/T (0.73 at T = 1 minute, 0.37 at T = 2) is rough and uncalibrated, unlike `[botta2015 pp. 4-5]`.

**Benchmarks and value-of-time conventions**

- Sizes: Israeli sirens one and two minutes `[vinitzky2010 p. 7]`; Earth Hour 4.0% `[meier2014 p. 5]`; holidays 0.5-4.5% `[akbar2023 pp. 11-12]`; lockdown moved monthly mean speed up to 7% `[energies2021 pp. 8, 12]`; London charge about -0.6 min/km `[hanna2017 p. 5]`.
- Value of time: half the gross wage `[anderson2014 pp. 9, 21; yang2020 p. 21]`; multiplier 1.8 (1.3-2.3) for congested time `[anderson2014 pp. 7, 12]`; EUR 15.59/hour `[adler2021 p. 20]`; GDP per hour worked, EUR 52 `[bauernschuster2017 pp. 30-31]`. Occupancy 1.34 `[yang2020 p. 21]`; 1.4 in the peak `[adler2021 pp. 5-6]`.
- Totals: $1.2-2.1 billion a year `[anderson2014 p. 21]`; EUR 3.2 million per strike `[bauernschuster2017 pp. 30-31]`; EUR 59.5 million a year per 10-point cut `[adler2021 pp. 20-21]`; Beijing congestion about half a percent of GDP `[yang2020 pp. 26-27]`.
- **OURS**: cost = vehicles on the road x occupancy x (minutes/60) x value of time. Marginal external cost per vehicle-km prices an extra vehicle, not a stop. No Turkish value of time in the set. Our hourly effect is about +1.2% travel time in 50-70 km/h cells, about a tenth of a one-day strike.

**Limits**

- Internal, not external validity `[rosenbaum2002book pp. 51, 58; ernst2004 p. 2; abadie2020 p. 20]`.
- Sensitivity analysis says how much bias is needed, not whether it exists `[rosenbaum2002book pp. 135-136, 141]`; crossing at 1.3 is sensitive, 1.5-3 moderate, 6 highly insensitive `[rosenbaum2002book pp. 126, 141, 159]`.
- Non-rejection is weak evidence with few units `[bertrand2004 Table 11 p. 38]`.
- Dilution: the effect must be large relative to unit volatility; averaging over instances helps `[abadie2021 pp. 18-19, fn 13]`.
- Lower-bound language `[smith2016 p. 8; madestam2011 p. 15]`. **OURS**: our bound depends on the unknown averaging rule (section 2.2).
- Demand-shock effects are larger on congested roads `[adler2021 pp. 15-16; hanna2017 p. 3]`; a point-stop model predicts delay rising toward capacity `[richards1956 p. 9]`. **OURS**: the pilot shows the reverse; measurement limit, overlap with existing stops and low baseline speed cannot be separated.
- Spillback is only a possibility `[hanna2017 p. 4]`; wording for secondary estimates `[lindo2018 p. 18]`; near-universal exposure makes small effects detectable `[harper2019 p. 9]`.

## 2. Formulas we need

### 2.1 Wardrop: time-mean and space-mean speed `[wardrop1952 pp. 4-7, 32]`

```
k_i = q_i / v_i                                  (eq. 1)
v_t = sum(q_i v_i) / Q                           time-mean, flow-weighted (eq. 2)
v_s = sum(k_i v_i) / K ;  Q = K v_s              space-mean, concentration-weighted (eqs. 3, 5)
v_t = v_s + sigma_s^2 / v_s = v_s (1 + c_s^2)    (eqs. 6, 8)
sigma_s^2 = sum(k_i (v_i - v_s)^2) / K           variance of the SPACE distribution (eq. 7)
```

Proof (Appendix II, p. 32): put q_i = k_i v_i into eq. 2 and expand around v_s. Exact, so v_t >= v_s. From spot speeds v_s = n/sum(1/v); from an instantaneous sample v_t = sum(v²)/sum(v) (p. 6). Approximate inverse: u_S ≈ u_T - sigma_T²/u_T `[rakha2005 p. 3]`.

### 2.2 What 60(1 - e^D) returns for a k-minute stop (note 09; entirely OURS)

Set-up: one cell, one 60-minute hour, baseline speed v_0. A complying vehicle brakes linearly for t_d, stands for s, accelerates linearly for t_a. Distance lost is v_0 k*, with

```
k* = s + (t_d + t_a)/2        true full-stop-equivalent minutes
```

A share pi complies. A simultaneous stop leaves the number of vehicles in the cell unchanged. D = ln(hourly mean with the stop / v_0).

| Scheme behind AVERAGE_SPEED | Hourly mean | 60(1 - e^D) returns |
|---|---|---|
| A. Fixed-interval pings, all kept | v_0 (1 - pi k*/60) | pi k*, exact |
| B. Fixed-interval pings, stationary dropped | v_0 (60 - pi k*)/(60 - pi s) | about pi (t_d + t_a)/2; s disappears |
| C. Distance- or crossing-triggered spot speeds | sum(v²)/sum(v) | about pi (t_d + t_a)/6; s disappears |
| D. One speed per traversal, mean over vehicles | v_0 [1 - (tau/60) pi k*/(tau + k*)] | pi tau k*/(tau + k*), below both tau and k* |
| D'. Distance / total time per traversal | v_0 (1 - pi k*/60) | pi k* |

tau = free traversal time of the cell (geohash-6 is roughly 0.6-1 km across: 0.6-1 minute at 60 km/h).

Why each row holds:

- A: ping counts are proportional to vehicle-time, so the mean is total distance / total time (Edie's definition, `[herrera2010 p. 15]`): v_0(60 - pi k*) over 60. No "present all hour" condition is needed; with mixed speeds replace v_0 by v_s.
- B: the same distance over moving time 60 - pi s, so 1 - ratio = [pi (t_d + t_a)/2]/(60 - pi s). This is Wardrop's running speed `[wardrop1952 p. 31]`.
- C through Wardrop's identity: over the hour the space distribution has mass p = s/60 at zero and 1 - p at v_0, so v_s = v_0(1 - p), sigma_s² = v_0² p(1 - p), and v_t = v_s + sigma_s²/v_s = v_0. A flow-weighted mean is exactly blind to a full stop; only the ramps register. [Check added in this digest: with linear ramps sum(v²)/sum(v) = v_0 [60 - s - (2/3)(t_d + t_a)]/[60 - s - (t_d + t_a)/2], a loss of about (t_d + t_a)/6.]
- D [check added in this digest]: a share tau/60 of the hour's traversals meets the stop, each at speed v_0 tau/(tau + k*).
- The bias does not difference out: ln v_t = ln v_s + ln(1 + c_s²), and the stop raises c_s² in the treated hour only.
- Rakha-Zhang's correction cannot repair B or C: stopped time never enters sigma_T.

Numerical benchmarks:

- Transient: t_d + t_a = v_0(1/b + 1/a) for braking rate b and acceleration a, so under B measured minutes are proportional to baseline speed. With 5-10 s lost per start `[lighthill1955 p. 27]` and a similar braking loss (assumed), B returns roughly 0.15-0.35 minutes at full compliance, whatever s is.
- Pilot under A: pi k* = 0.73; with k* of 1-2 minutes the compliance-equivalent is 37-73%.
- Pilot under B: 0.73 exceeds 0.15-0.35, so stationary pings are only partly removed, or the platoon transient is longer, or the scheme is not B.
- Pilot under D: tau of 0.6-1 and k* of 1-2 give 0.4-0.7 minutes, near the pilot level.
- Gradient: A predicts equal minutes across classes; B predicts minutes proportional to v_0 (60 against 40 km/h gives 1.5; pilot 0.73/0.45 = 1.6); D predicts more minutes in slower cells. The level looks like A or D, the gradient like B: unresolved.

Queueing:

- Universal simultaneous stop: the density profile is frozen and released; no shock, no discharge period. After-effects are restart lost time and a restart wave of about 20-25 km/h through platoons.
- Point stop with continuing arrivals (partial compliance, blocked lane): queue grows at q/(k_j - q/v) `[wardrop1952 p. 19]`; discharge T_f = q k/(q_m - q) `[lighthill1955 p. 24; richards1956 p. 9]`; total delay (1/2) q k²/(1 - q/q_m); mean delay per affected vehicle k/2. With k = 2: T_f = 8 minutes at q/q_m = 0.8, 18 at 0.9; it reaches the 10h hour only above about 0.96. An upper-end scenario.
- Overlap: a siren stop coinciding with a red phase adds less than k; under B the baseline already excludes standing time.

Diagnostics that separate the schemes:

1. NUMBER_OF_VEHICLES at 09h on 10 Nov: falls about pi s/60 (1.7-3.3% for 1-2 minutes) under B with ping counts; unchanged under A or device counts.
2. Effect against baseline speed: flat in minutes (A), proportional (B), decreasing (D).
3. MINIMUM_SPEED: a 1 km/h floor in all hours rules out A with raw zeros, unless the field is floored or per-vehicle.
4. The 5-minute index at 09:05-09:10: fall of order k/5 (20-40%) under A, small under B or C.
5. MAX - MIN in the treated hour: unchanged under B.

### 2.3 Canay-Romano-Shaikh sign-change test `[canay2017 pp. 3-4, 8-10]`

```
1. q clusters; theta_hat_j in each.  S_j = theta_hat_j - theta_0   (sqrt(n) drops out)
2. T(S) = |mean(S)| / (s/sqrt(q)),  s^2 = (1/(q-1)) sum (S_j - mean)^2     (eq. 17)
   one-sided: signed t, the same test as sum_j S_j                         (Appendix A)
3. G = {-1,+1}^q,  gS = (g_1 S_1, ..., g_q S_q),  M = 2^q
4. p = (1/M) #{ g : T(gS) >= T(S) }                                        (eq. 9)
5. Level-alpha rule: k = ceil(M(1-alpha)); reject if T(S) > T^(k);
   if T(S) = T^(k) reject with probability (M alpha - M+)/M0              (eq. 13)
```

Exact if the S_j are independent and each symmetric about zero under H0 (Theorem 2.1, p. 3). Asymptotically: cluster estimates jointly normal, block-diagonal covariance, variances may differ, q fixed. **OURS**: S_y = -D_y, T = sum S_y, 32 sign vectors.

### 2.4 Romano-Wolf stepdown on one joint assignment set `[romano2005b pp. 4, 10-12]`

G = the M joint assignments (observed g_0 included); T_k(g) = -D_k(g); one g applied to all classes at once.

```
Unadjusted:  p_k = #{ g : T_k(g) >= T_k(g_0) } / M                         (eq. 16)

max-T stepdown
  order t_(1) >= ... >= t_(5), labels r_1..r_5;  K_j = {r_j, ..., r_5}
  m_j(g) = max_{k in K_j} T_k(g)
  phat_j = #{ g : m_j(g) >= t_(j) } / M                                    (eq. 23)
  padj_(1) = phat_1;  padj_(j) = max(padj_(j-1), phat_j)
  reject H_(j) iff padj_(j) <= alpha; stop at the first non-rejection

Single-step: pss_k = #{ g : max over all classes of T(g) >= t_k } / M      (padj <= pss)
Sampled G:   (1 + #{...})/B in place of #{...}/M, same draws throughout    (eqs. 18, 24)
```

Finite-sample FWE control under the randomization hypothesis (Theorem 3.1, Corollary 3.1, Example 3.1). The running maximum is implied by the stopping rule and matches `[list2019 p. 11]`. **OURS**: a min-p variant replaces T_k(g) by its rank p-value pi_k(g) = #{g': T_k(g') >= T_k(g)}/M and counts min over K_j of pi_k(g) <= p_(j); it is never above Holm. Comparators `[romano2005a p. 7]`: Bonferroni min(1, 5 p_k); Holm padj_(j) = max_{i<=j} min(1, (5 - i + 1) p_(i)).

### 2.5 Rosenbaum sensitivity bound, one treated among n_s `[rosenbaum2002book pp. 119-121, 133, 149-150]`

```
Model:  1/Gamma <= pi_j(1-pi_k)/[pi_k(1-pi_j)] <= Gamma;  logit(pi_j) = kappa(x_j) + gamma u_j,  0 <= u_j <= 1,  Gamma = e^gamma   (4.1-4.2)
One treated per set:  Pr(Z = z | m) = prod_s exp(gamma sum_i z_si u_si) / sum_i exp(gamma u_si)        (4.15)
A given unit is the treated one with probability in [ 1/(1 + Gamma(n_s - 1)),  Gamma/(Gamma + n_s - 1) ]   (4.17 with c_s+ = 1)
Sign scores:  c_s+/[c_s+ + (n_s - c_s+)Gamma] <= p_s <= Gamma c_s+/[Gamma c_s+ + n_s - c_s+]           (4.17)
Arbitrary scores, large S:  mu_sa = [sum_{i<=a} q_si + Gamma sum_{i>a} q_si]/[a + Gamma(n_s - a)],  mu_s = max_a mu_sa,
   upper bound on Pr(T >= t) ≈ 1 - Phi[(t - sum mu_s)/sqrt(sum nu_s^2)]
```

**OURS** for 5 x (1 of 4): each assignment has probability at most [Gamma/(Gamma+3)]^5, so worst-case p <= k [Gamma/(Gamma+3)]^5 with k assignments at least as extreme. k = 8 stays below 0.05 up to Gamma = 1.70; k = 35 up to about 1.11; k = 1 crosses at 3.66, the design's ceiling. Exact version: maximise over binary u with ones on the k_s highest scores per year, 3^5 = 243 cases (Proposition 19, pp. 164-166). Companion tilt on whole assignments `[firpo2018 pp. 6-8]`: weights proportional to exp(phi v_j); **OURS**, p(phi) = k e^phi/(k e^phi + N - k); the 50-70 class loses 5% at phi = 1.90 and 1% at phi = 0.25.

### 2.6 Ferman-Pinto variance form `[ferman2019 pp. 10-13]`

```
eta_jt = nu_jt + (1/M(j,t)) sum_i eps_ijt        (eq. 8)
var(W_j) = A + B/M_j                             W_j = post-minus-pre average of eta
Correction: regress squared control residuals on a constant and 1/M_j -> Ghat(M);
            Wtilde_j = What_j sqrt( Ghat(M_1)/Ghat(M_j) );  then Conley-Taber on Wtilde
var(alpha_hat) = G(M_1) + (1/N0^2) sum_controls G(M_j)      (eq. 10)
```

If A = 0 the ratio var(W_j)/var(W_j') stays M_j'/M_j however large M is. Same form, delta0 + delta1/Z_i, in `[alvarez2023 p. 9]`. **OURS**: A is the city-wide date shock, B/M_d cell-averaging noise.

### 2.7 Hodges-Lehmann and test inversion

```
Under r_T = r_C + tau,  R - tau Z = r_C is fixed                           [rosenbaum2002 pp. 3-4]
Test H0: tau = tau0 by the no-effect test on R - tau0 Z                    [rosenbaum2002book p. 56]
Confidence set = { tau0 : p(tau0) >= alpha }                               [rosenbaum2002book pp. 57-58]
HL: tau_hat = [ inf{tau : tbar > t(Z, R - tau Z)} + sup{tau : tbar < t(Z, R - tau Z)} ] / 2   [rosenbaum2002book pp. 60-61]
Counterfactual under beta0:  y_S = y_E - T_E beta0 + T_S beta0             [young2019 p. 15]
OLS residuals, treated-sum statistic:  tau_hat = Z'(I-H)R / Z'(I-H)Z       [rosenbaum2002 p. 5]
```

**OURS**: for the mean statistic t(Z, R - tau Z) = t - tau and tbar = 0, so the HL estimate is the observed statistic. With 4 dates DiD_d = (4/3)(c_d - cbar_year), so placebo DiDs are shifted by minus one third of the Nov 10 DiD (logic of `abadie2021` p. 14 fn 10): subtract tau0 from the Nov 10 contrast first, then recompute all DiDs. Convert endpoints by 60(1 - exp(tau)); 1-minute stop tau = ln(59/60) = -0.0168, 2-minute -0.0339. Without constant effects read the bound as the largest year-level slowdown `[caughey2023 p. 13]`.

## 3. Corrections and cautions

Versions on disk (page numbers refer to these):

- `conley2011`: NBER TWP 312 (2005); N0 = treated, N1 = control; the Gamma* procedure and spatial appendix of the 2011 article are absent.
- `ferman2019`: MPRA 67665 (2015). `hagemann2019`, `alvarez2023`: arXiv v1. `mackinnon2017/2018/2020`: early-view, accepted, in-press.
- `bertrand2004`: NBER WP 8841 (2002); the QJE version may not present RI as preferred (reader's memory, unverified).
- `roth2023`: arXiv v3. `list2019`: NBER WP 21875. `romano2005a/b`: 2003 preprints; our a/b labels reverse List et al.'s.
- `abadie2020`: arXiv v2. `athey2017`: arXiv v1. `young2019`: LSE accepted version. `chernozhukov2021`: arXiv v10.
- `anderson2014`: NBER w18757. `adler2021`: OUP advance article. `lindo2018`: NBER WP 21828. `harper2019`, `akbar2023`: accepted manuscripts. `depetris2020`: September 2019 version. `madestam2011`: unreviewed working paper. `herrera2010`: 2009 Berkeley working paper. `goldman2018`: online-first, volume unconfirmed. `bellah1967`: 2005 reprint; cite the 1967 original.
- `kreindler2024`: only the supplement; equation 6, Table III, Figure 4 unseen; "roughly linear" and any magnitude unconfirmed.
- `redelmeier2003`: only PDF pp. 12-13 are the letter. `redelmeier2024`: web print, figures unreadable.
- `rosenbaum2002book`: chapters 2-12 read by sub-readers, 6-10 selectively.
- `meier2014`: authors are Olexsak and Meier. `pinter2021`, `olug2024`: preprints.
- Not read: supplements of `canay2017` and `chung2013`; Appendix C of `mackinnon2020`.
- Printed page = PDF page plus: `wardrop1952` 324; `lighthill1955` 315; `richards1956` 40; `knoop2009` 350; `rakha2005` 37; `yang2020` 417; `rosenbaum2002` 285; `ernst2004` 675; `hess2017` 629; `uzun2019` 134; `ozyurek2004` 373; `karakus2023` 110; `vinitzky2010` 1102; `bellah1967` 39; `dinas2024` 487; `skitka2005` 1994; `carter2011` 1010; `meier2014` 157; `utku2023` 1583; `ozkurt2025` 182; `takak2021` 567. Minus 1: `young2019`, `athey2017`, `abadie2020`, `goldman2018`, `depetris2020`, `akbar2023`, `botta2015`. Minus 2: `madestam2011`, `herrera2010`. `rosenbaum2002book`: minus 13 (about minus 12 in chapter 6, minus 9 in chapter 11).

Earlier claims overstated or wrong:

- `young2019` shows over-rejection only in high-leverage and high-dimensional cases; "fewer than half of papers keep any effect" belongs to the 2016 working paper, via `hess2017` p. 3.
- "Studentized RI is safer" holds only for 2+ treated clusters `[mackinnon2020 pp. 12, 15]`; dividing by a permutation-invariant scale is not RI-t.
- `hagemann2019` is not the formal justification for placebo dates: it needs 2+ treated clusters and noise that averages out within clusters.
- `alvarez2023` is not a spatial-correlation paper; Ferman (2020) and Hagemann (2020) are missing from the library.
- Ferman-Pinto heteroskedasticity concerns the treated date against same-year controls, not cells differing among themselves or years differing in size.
- `mackinnon2017` does not discuss leave-one-out. `mackinnon2018` is more positive than "never bootstrap" for 2+ treated clusters.
- `bertrand2004`'s 45% concerns a persistent treatment; an on/off treatment gives 6%.
- `abadie2010`, not `abadie2015`, first mentions in-time placebos; ranking dates is the in-space test; `abadie2015` computes no p-value over time.
- `abadie2021` never says studentization. `firpo2018`'s phi tilts whole assignment sets, not per-year odds; its benchmarks for a large phi do not transfer.
- `chernozhukov2021` moving blocks are T cyclic shifts, floor 1/T; validity under dependence is asymptotic.
- "The date is as if random, the p-value is exact" must become "significance against a uniform benchmark".
- The 10h reference hour is post-treatment; show a 08h-only contrast.
- `romano2005a` and `list2019` are asymptotic bootstrap results; exactness comes from `romano2005b`.
- `anderson2014`'s 47% is a share of delay, not travel time; no within-day contrast. `bauernschuster2017` does not difference against other hours. `hanna2017` is a per-road before/after (queries every 10 minutes); its "delay" is min/km. `adler2021` uses loop detectors. `yang2020` is verified; fixed sensors.
- "60(1 - e^D) needs space-mean speed" is our claim, not Wardrop's. Knoop's factor four is an extreme. The (MAX - MIN)/4 proxy is ours. "8 minutes at q/C = 0.8" rests on a point-stop model. `herrera2010` says nothing on arterials or Wardrop bias.
- `uzun2019`: horns and sirens date to the 1950s, not the 1940s, and are factory, ferry and ship sirens; printed pages: trams 142, freighter 152, 1988 day 160-161.
- `ozyurek2004` and `goldman2018` do not show stronger participation among CHP voters. `karakus2023` does not apply Bellah.
- `madestam2011` effects are 0.61, 0.85, 0.88 percentage points at ages 4-18, not "2%, 4%, 0.9%".
- `dinas2024`: "about three" flags per street; display was reputationally costly. `parravano2015`: units are districts and facades; social influence is not mechanical blocking. `skitka2005` is self-report.
- `meier2014` compiles reported reductions; it does not estimate 4%.
- `staples2018` and `redelmeier2008` are challenged results; cite with `harper2019` and `zhang2016`. `redelmeier2003` does not name its test; do not cite its P value.
- `roth2023` is a review: cite originals for load-bearing claims. `list2019` gives no advice on pre-registration or choosing subgroups.
- The bounded-null guarantee (raw statistic, `caughey2023`) and the weak-null guarantee (studentized statistic, `wu2021`) come from different statistics (**OURS**).

Do not quote (problems inside the papers):

- `young2019` p. 28 prints .88 (table .87); p. 33 garbled. `athey2017` pp. 15-16, 41.
- `harper2019`: the all-other-days 0.98 has no weekday or season controls; ±14 CI upper limits in Table 4 look mis-printed.
- `gulek2024`: stars disagree between text and Table 1; LATE rests on an assumed 84%.
- `adler2021`: 0.024 against 0.027 min/km. `yang2020`: two "average" MECC figures (0.46, 0.15).
- `ngeni2022`: quote Table 6, not the abstract. `tanberk2023`: "7 thousand" points conflicts with other counts. `ozkurt2025`: target variable undefined.
- `parravano2015`: I_SI = 0.81 does not follow from its inputs (0.66). `madestam2011`: draft inconsistencies. `rakha2005` places I-880 in Los Angeles.
- `carter2011`: possibly failed replication (reader's memory, unverified).
- `romano2005b`: strict versus weak inequality inconsistent; use the p-value form.

## 4. Per-key one-liners

- `ernst2004` Ernst (2004) - permutation tutorial - exact p, test inversion, max-statistic; not for blocked designs.
- `hess2017` Heß (2017) - ritest guide - permute at the assignment level; 4096-assignment paired template.
- `young2019` Young (2019) - RI re-analysis of 53 experiments - 13-22% fewer significant coefficients, driven by leverage.
- `athey2017` Athey & Imbens (2017) - handbook chapter - analyse cluster aggregates; one treated per stratum leaves variance inestimable.
- `rosenbaum2002` Rosenbaum (2002) - covariance adjustment with RI - HL estimate, residual permutation, Gamma sensitivity.
- `rosenbaum2002book` Rosenbaum (2002) - Observational Studies - bound Gamma/(Gamma + n_s - 1); bracketing; coherence.
- `abadie2020` Abadie, Athey, Imbens & Wooldridge (2020) - design-based uncertainty - remains at rho = 1; theorems need independent assignment.
- `canay2017` Canay, Romano & Shaikh (2017) - sign-change test - with q = 5 the floor is 1/32.
- `chung2013` Chung & Romano (2013) - robust permutation tests - unstudentized tests fail under imbalance; motivation only.
- `wu2021` Wu & Ding (2021) - FRT for weak nulls - studentize; needs 2+ units per arm, not our strata.
- `caughey2023` Caughey, Dafoe, Li & Miratrix (2023) - beyond the sharp null - one-sided p valid for "no slowdown in any year".
- `ding2016` Ding, Feller & Miratrix (2016) - effect variation - FRT-CI device; near powerless at our sample size.
- `conley2011` Conley & Taber (2005/2011) - few policy changes - estimator inconsistent; null from controls.
- `ferman2019` Ferman & Pinto (2015/2019) - heteroskedasticity - var(W) = A + B/M; smaller treated group over-rejects.
- `hagemann2019` Hagemann (2019) - placebo inference - 1/alpha permutations rule; not for one treated cluster.
- `mackinnon2017` MacKinnon & Webb (2017) - wild bootstrap - CRVE rejects 77.75% with one treated cluster.
- `mackinnon2018` MacKinnon & Webb (2018) - subcluster bootstrap - fails at G1 = 1 with rho > 0.02.
- `mackinnon2020` MacKinnon & Webb (2020) - RI-beta and RI-t - names our test; exact only with homogeneous clusters.
- `alvarez2023` Alvarez & Ferman (2023) - extensions note - realised-effect estimand, max-statistic bands; no simulations.
- `abadie2010` Abadie, Diamond & Hainmueller (2010) - Proposition 99 - placebo ranking, p = 1/39; cell-level SEs uninformative.
- `abadie2015` Abadie, Diamond & Hainmueller (2015) - German reunification - in-space and in-time vocabulary; donor-pool rules.
- `abadie2021` Abadie (2021) - practitioner review - benchmark-assignment wording; RMSPE ratio; one-sided test.
- `firpo2018` Firpo & Possebom (2018) - sensitivity, confidence sets - Q = prod(J_g + 1) is our assignment space.
- `chernozhukov2021` Chernozhukov, Wüthrich & Zhu (2021) - conformal inference over time - exact under exchangeability; trend plus misspecification fails.
- `bertrand2004` Bertrand, Duflo & Mullainathan (2002/2004) - placebo laws - on/off treatment gives 6%; RI has low power with few units.
- `roth2023` Roth, Sant'Anna, Bilinski & Poe (2023) - DiD synthesis - cluster at assignment level; pre-tests weak; bracketing.
- `romano2005a` Romano & Wolf (2005) - StepM bootstrap - FWE and Holm definitions; asymptotic only.
- `romano2005b` Romano & Wolf (2005) - exact stepdown - finite-sample FWE with one common permutation set.
- `list2019` List, Shaikh & Xu (2016/2019) - multiple testing - 22.6% for five tests; reporting format.
- `redelmeier2003` Redelmeier & Stewart (2003) - Super Bowl - origin of the ±1 week double control.
- `redelmeier2008` Redelmeier & Tibshirani (2008) - election day - RR 1.18; adjacent-day placebos; cite with zhang2016.
- `redelmeier2012` Redelmeier & Yarnell (2012) - tax day - OR 1.06; marginal, citation only.
- `redelmeier2024` Redelmeier & Staples (2024) - eclipse - under-3-minute event studied over 3 days.
- `staples2018` Staples & Redelmeier (2018) - 4/20 - closest design template; result challenged.
- `zhang2016` Zhang & Aronow (2016) - election re-analysis - placebo-date null; binomial rejects 43% of Tuesdays.
- `harper2019` Harper & Palayew (2019) - 4/20 re-analysis - control ladder 1.12, 1.05, 0.98; positive control.
- `smith2016` Smith (2016) - DST and crashes - permutation p = 0.007, contaminated dates excluded.
- `card2011` Card & Dahl (2011) - football and violence - timing specificity; cluster at the shock level.
- `lindo2018` Lindo, Siminski & Swensen (2015/2018) - game days - lead/lag and non-event placebos.
- `gulek2024` Gulek (2024) - Ramadan and accidents - published use of the İBB index; 7 Qadr days.
- `anderson2014` Anderson (2013/2014) - LA strike - +0.194 min/mile; two-way clustering; autumn drift.
- `bauernschuster2017` Bauernschuster, Hener & Rainer (2017) - one-day strikes - +8.4% peak travel time, p = 0.07.
- `adler2021` Adler, Liberini, Russo & van Ommeren (2021) - Rome strikes - log travel time; 1.6% per 10 points.
- `hanna2017` Hanna, Kreindler & Olken (2017) - Jakarta HOV - sub-hourly probe times; +46%, +87%.
- `yang2020` Yang, Purevjav & Li (2020) - Beijing congestion cost - value of time half the wage; occupancy 1.34.
- `wardrop1952` Wardrop (1952) - traffic theory - v_t = v_s + sigma_s²/v_s; running versus journey speed.
- `knoop2009` Knoop, Hoogendoorn & van Zuylen (2009) - mean speeds in loop data - gap concentrated at low speed.
- `rakha2005` Rakha & Zhang (2005) - time-mean to space-mean - gap 1-5%, 10-30% in congestion; cannot recover stops.
- `herrera2010` Herrera, Work, Herring, Ban & Bayen (2009/2010) - Mobile Century - temporal versus spatial sampling.
- `lighthill1955` Lighthill & Whitham (1955) - kinematic waves - T_f = q_i T_r/(q_m - q_i); 5-10 s lost per start.
- `richards1956` Richards (1956) - shock waves - closed-form clearing time; point-stop model only.
- `akbar2023` Akbar, Couture, Duranton & Storeygard (2023) - Indian city speeds - holidays move speed 0.5-4.5%.
- `kreindler2024` Kreindler (2024) - supplement only - drops trips with stops; marginal until the article is read.
- `bagrow2011` Bagrow, Wang & Barabási (2011) - calls in emergencies - same-time-of-week baseline; no formal test.
- `botta2015` Botta, Moat & Preis (2015) - crowd size - calibration needs ground truth; contrast case.
- `meier2014` Olexsak & Meier (2014) - Earth Hour compilation - mean 4.0%, median 2.6%; baseline matters.
- `pinter2021` Pintér & Felde (2021) - CDRs, Euro 2016 - synchronized dip; descriptive, marginal.
- `ngeni2022` Ngeni, Mwakalonge & Siuhi (2022) - eclipse traffic - hourly dip then surge; naive bands.
- `utku2023` Utku (2023) - LSTM on one İBB cell - column list; 2,321 points.
- `ozkurt2025` Özkurt, Kala, Konuk & Saylam (2025) - fuzzy model - 2.5% hours missing; otherwise marginal.
- `tanberk2023` Tanberk & Can (2023) - forecasting app - screenshot: six-character geohash, MINIMUM_SPEED = 1.
- `olug2024` Olug, Kaya, Tugay & Gunduz Oguducu (2024) - graph benchmark - 2,451 locations; not evidence of physical sensors.
- `energies2021` Alemdar, Kaya, Canale, Çodur & Campisi (2021) - COVID traffic - mean speed 55-59 km/h; not the geohash file.
- `takak2021` Takak, Görmez, Türkmen & Güvensan (2021) - İBB sensor forecasts - 7,000 one-minute sensors; same-weekday baseline.
- `alcan2022` Alcan & Kaçar (2022) - 2020 traffic index - index 1-99, hourly; 2020 distorted.
- `uzun2019` Uzun (2019) - 10 Kasım ceremonies 1939-88 - vehicles stopped in 1939; non-obligatory; 89.7% poll.
- `ozyurek2004` Özyürek (2004) - privatised Atatürk imagery - profile of voluntary Kemalists; nothing on the silence.
- `goldman2018` Goldman (2018) - privatised commemoration - 9:05 standing known to all; lines blurred after 2016.
- `karakus2023` Karakuş (2023) - civil or political religion - marginal; cite for the debate only.
- `vinitzky2010` Vinitzky-Seroussi & Teeger (2010) - silence typology - siren-framed silence; Israeli drivers stop.
- `bellah1967` Bellah (1967) - civil religion - origin of the concept only.
- `depetris2020` Depetris-Chauvin, Durante & Campante (2020) - football and nation-building - shared experiences matter; FDR adjustment.
- `madestam2011` Madestam & Yanagizawa-Drott (2011) - Fourth of July - participation unobserved, proxied by rain.
- `dinas2024` Dinas, Martinez & Valentim (2024) - Madrid flags - norm, not preference; Bicchieri definition.
- `parravano2015` Parravano, Noguera, Hermida & Tena-Sanchez (2015) - Barcelona flags - display depends on neighbours.
- `skitka2005` Skitka (2005) - post-9/11 flags - self-report; patriotism, not nationalism.
- `carter2011` Carter, Ferguson & Hassin (2011) - flag priming - peripheral; cite sparingly if at all.
