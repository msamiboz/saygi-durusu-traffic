# 08 Traffic economics: how economists measure short-lived traffic shocks

Reader notes for five papers: anderson2014, bauernschuster2017, adler2021, hanna2017, yang2020.
All five text files were read in full (appendices and reference lists skimmed).
Page numbers `(p. N)` are the `=== page N ===` markers of `literature/txt/<key>.txt`.

Notes on versions and page numbering:

- anderson2014: the file is the NBER working paper w18757 (February 2013), not the AER 2014 print. Page numbers below are working-paper PDF pages. Check numbers against the AER version before quoting a page in our paper.
- adler2021: the file is the OUP advance article (2020, pp. 1-35, DOI 10.1093/jeg/lbaa037), not the final issue pagination 397-431.
- yang2020: PDF page N is journal page 417 + N.
- Lines marked "our conversion" or "our calculation" are arithmetic done by me from numbers in the paper. They are not statements of the paper.

---

### anderson2014 - Anderson (2013 NBER WP; AER 2014), Subways, Strikes, and Slowdowns

- **Question and setting.** Does public transit relieve road congestion? Uses the sudden 35-day Los Angeles MTA strike that began 14 October 2003 as a shock to freeway traffic (p. 4, p. 12).

- **Data and method.**
  - Source: Caltrans PeMS inductive loop detectors on all major LA freeways. PeMS builds hourly flow and hourly average speed per detector. Average detector spacing 0.6 miles (p. 14). Not probe data.
  - Unit: detector-by-hour. 178,549 observations in the main regression; about 640-720 detectors in service (p. 34, p. 35).
  - Outcome: average delay in minutes per mile relative to an assumed free-flow speed of 60 mph: delay = max(0, 60/speed - 1). Example: 40 mph gives 0.5 min/mile (p. 14-15). Results are stated to be robust to 55 or 65 mph and to using speed itself (p. 15).
  - Sample: weekdays only, no holidays; peak hours only, defined from the data as hours when the average speed was consistently below 60 mph before the strike: 7-10 a.m. and 2-8 p.m. (p. 15).
  - Estimator: sharp regression discontinuity in calendar date, local linear on each side, 28-day bandwidth (16 Sep to 10 Nov 2003):
    y_it = a + b*strike_it + c*date_it + d*date_it*strike_it + X_it'g + e_it,
    with day-of-week indicators and detector fixed effects in X (p. 15-16). Detector fixed effects are there because detectors go in and out of service (p. 15).
  - Weights: each detector weighted by pre-strike VMT = road length covered times average pre-strike flow. Unweighted regressions are reported to give similar results in qualitative terms (p. 16).
  - Inference: two-way clustering by day and by detector (Cameron-Gelbach-Miller), because errors are correlated over time and across detectors: "It is thus impossible to construct a single set of clusters" (p. 16).

- **Main findings.**
  - All freeways, all peak hours: delay rises 0.194 min/mile (SE 0.041, t = 4.7), which is 47% of the pre-strike mean delay of 0.409 min/mile (p. 17, Table 4 p. 35).
  - Morning peak only: +0.314 min/mile (SE 0.075), 67% of 0.472 (p. 18, Table 5 p. 36). Evening peak: +0.157 min/mile, 41% (p. 18, Table 6 p. 37).
  - Larger on freeways parallel to busy transit lines: US-101 +0.33 min/mile (90%); other freeways +0.125 (29%) (p. 17).
  - Raw VMT-weighted mean speed: 52.8 mph without strike, 48.3 mph during it (p. 15, Table 3 p. 34).
  - Detector occupancy share rises 1.3 percentage points (12%) (p. 18).
  - Peak-hour flow per lane FALLS by 31 vehicles/hour (2.2%), explained as throughput dropping when congestion rises. Over the whole day the flow effect is insignificant, 95% CI -1.3% to +1.0% (p. 19).
  - Falsification 1: neighbouring-county freeways more than 10 miles from the service area: +0.024 min/mile (12%), insignificant (p. 20, Table 9 p. 40).
  - Falsification 2: placebo strike one year later (12 Oct 2004): +0.06 min/mile (14%), insignificant (p. 20).
  - A simple before/after comparison on the control freeways gives a spurious +32.3% (t = 7.0); the RD gives 11.7% and insignificant (footnote 13, p. 14). Delays trend upward through October and November toward Thanksgiving even without a strike (p. 20).
  - Money value: 0.19 min/mile times 36 billion peak freeway passenger-miles = 114 million hours per year; at half the average hourly wage ($10.30) this is $1.2 billion per year; with a delay multiplier of 1.8 it is $2.1 billion (p. 21). Including arterials (70 billion passenger-miles): $2.3 to $4.1 billion (p. 21-22).
  - Speed-flow assumption taken from Parry and Small: delay = a * (traffic volume)^3.7 (p. 10, p. 23; exponent read from the PDF because the text file garbles it). Equivalent statement: the marginal effect of one more vehicle on total delay is 3.7 times the average delay (footnote 2, p. 5).
  - Value-of-time conventions: time valued at half the gross hourly wage, elasticity of value of time to the wage 0.8 (p. 9); time spent in congestion, waiting or walking gets a multiplier c = 1.8 (range 1.3 to 2.3 in sensitivity) (p. 7, p. 12, p. 44).

- **Usable for our paper.**
  - Data: hourly detector-level speed is a standard outcome grain in this literature (p. 14). Section: Data.
  - Method: delay in minutes per distance relative to a free-flow benchmark, delay = 60/v - 60/v_ff, is the established unit; our full-stop-equivalent minutes can be presented beside it (p. 14-15). Section: Method.
  - Method / Robustness: inference must allow correlation both across locations within a day and within location over time (p. 16). This supports our statement that the effective sample is dates, not cells. Section: Method.
  - Robustness: the two falsification designs (unaffected locations; same calendar window in another year) and the documented failure of a naive before/after comparison (footnote 13 p. 14; p. 20). Section: Robustness.
  - Robustness: evidence that traffic drifts within October-November (p. 20) is a direct warning for our "Nov 10 is always the 2nd of 4 dates" problem. Section: Robustness.
  - Results-Discussion: money value template: hours lost times half the wage, optionally times 1.8 for congested time (p. 21). Section: Results-Discussion.
  - Results-Discussion: the finding that flow falls while delay rises (p. 19) is a reason not to use NUMBER_OF_VEHICLES as a simple proxy for demand. Section: Results-Discussion.

- **Caveats.**
  - The headline "47%" is a percentage of DELAY OVER FREE FLOW, not of travel time or speed. Our conversion from Table 4, assuming 60 mph free flow: travel time goes from about 1.41 to 1.60 min/mile, roughly +14% travel time or -12% speed. Only this is comparable with our log-speed effect.
  - Our conversion to metric: 0.194 min/mile = 0.12 min/km; morning peak 0.314 min/mile = 0.20 min/km.
  - The design is an RD in DATE on a 35-day shock. It contains no within-day contrast. `literature/review.md` line 90 calls it "a template for a time-of-day contrast"; that overstates it. It restricts to peak hours but never differences one hour against neighbouring hours.
  - Freeways only; arterial effects are assumed, not measured (p. 21).
  - Loop detectors measure spot speed at a point. Nothing in the paper speaks to probe/geohash data, to stopped vehicles, or to shocks of minutes.
  - The paper has no statement on how a brief capacity loss propagates or on queue discharge.

- **Checks or analyses it suggests for us.**
  - Placebo year/date: run the full estimator with a fake "treated" date in each year (already implicit in the randomization inference) and also on a non-November month, to show the 09h contrast is flat when nothing happens.
  - Report a vehicle-weighted estimate (weights = each cell's NUMBER_OF_VEHICLES at 08-10h averaged over control dates) beside the equal-weight one, as Anderson reports VMT-weighted and unweighted.
  - Keep a fixed set of cells within each year (cell fixed effects or a balanced panel), since sensor composition changes can bias means (p. 15).
  - Robustness to functional form: repeat with the outcome in delay units, 60/v - 60/v_ff, with v_ff set per cell (for example a high percentile of that cell's speed), and with speed in levels.
  - Because of the Oct-Nov drift, add a linear date trend across the control dates or use symmetric controls (Nov 3 and Nov 17 only).

---

### bauernschuster2017 - Bauernschuster, Hener and Rainer (2017), When Labor Disputes Bring Cities to a Standstill

- **Question and setting.** What do one-day public transit strikes do to car traffic, travel times, accidents, pollution and health? 71 strikes of one day or less in the five largest German cities, 2002-2011 (p. 3, p. 10).

- **Data and method.**
  - Traffic volume: official BASt automatic counters, hourly car counts, 43 monitors on commuter routes (27 freeway, 16 federal road), 2002-2011 (p. 11).
  - Travel time: TomTom GPS probe speeds matched to road segments, delivered as a city-level congestion index CI = T / T0 (actual travel time over free-flow travel time at posted limits). Available daily, for a morning and an evening peak hour, and separately for freeways and city streets, 2010-2011 only (p. 12). The morning peak index is the single hour 8-9 a.m. (footnote 19, p. 12). Means: daily 1.31, morning peak 1.47, evening peak 1.49 (p. 12).
  - Sample: workdays only; weekends, public holidays and carnival days dropped (p. 11). 17 multi-day strikes dropped from the main sample (footnote 14, p. 10).
  - Estimator: generalized difference-in-differences with fixed effects, not matched comparison days:
    y = a + b*STRIKE_cd + (hour-of-day x day-of-week FE) + week-of-year FE + year FE + monitor FE + controls + e (eq. 1, p. 14).
    Preferred specification interacts all time fixed effects and weather with city indicators (p. 15). Controls: school holidays, temperature, precipitation, wind, snow (p. 14).
  - Weights: each city gets equal weight (p. 15).
  - Inference: standard errors clustered by city (5 clusters), p-values from t(G-1); checked with wild cluster bootstrap (Rademacher) and a multi-point version following Webb (p. 15, p. 28-30).

- **Main findings.**
  - Car volume, morning peak 6-10 a.m.: +131.6 cars/hour on a mean of 5,240 on freeways (+2.5%); +77.7 on 1,790 on federal roads (+4.3%) (Table 1 p. 16, p. 17). Evening peak: a little under 2% (p. 17).
  - Hour-by-hour: the largest effect is 6-7 a.m., +7.7% on freeways and +9.4% on federal roads; outside the peaks "strikes in public transportation leave traffic volumes virtually unaffected" (p. 17).
  - Travel time: morning-peak CI rises by 0.123 (SE 0.051, p = 0.07) on a mean of 1.47, i.e. +8.4% travel time. Evening peak +0.062 (about 4%). All-day +0.050 on 1.30 (3.8 to 4.3%, significant at 1%). City streets and freeways are almost identical (Table 3 p. 22, p. 21). Only 26 strikes and 2,454 city-days enter these regressions (p. 22).
  - Total car hours in the morning peak: +11 to 13% (p. 22).
  - Placebo: assigning the strike to cities not on strike gives small, insignificant volume effects (p. 19-20, Table 2 p. 20). Placebo pollutant SO2 shows no effect (p. 23-24).
  - Mass events (55 events, 1,094 city-days) added as a control change nothing (p. 27-28).
  - Duration: one hour less strike reduces the morning-peak travel-time effect by 7.8% (unreported regression, p. 32).
  - Money value: per city, 486,000 car commuters with a 27-minute one-way trip and 445,000 transit commuters with 37 minutes; a 6.3% rise in peak travel time gives about 62,000 extra hours per strike day, or 1,550 full-time work weeks; at GDP per hour worked of EUR 52 this is EUR 3.2 million per strike, EUR 228.9 million for the 71 strikes (p. 30-31). Accident and health costs are below 0.5% of this (p. 32).

- **Usable for our paper.**
  - Literature: the closest economics precedent for a ONE-DAY shock measured against the same clock hours on other days. Section: Literature.
  - Data: precedent for a commercial GPS-probe index expressed as actual over free-flow travel time at the city level, including a one-hour morning-peak version (p. 12). Supports using the İBB city-wide index as a second source. Section: Data.
  - Method: hour-of-day x day-of-week fixed effects are how this literature builds "same hour, same weekday" counterfactuals (p. 14). Our same-weekday control dates do the same thing non-parametrically. Section: Method.
  - Method: with very few clusters, use t(G-1) and wild cluster bootstrap (p. 15, p. 28-30). Our randomization inference over dates is a stricter answer to the same problem. Section: Method.
  - Robustness: placebo treatment assignment (p. 19-20) and the mass-event control (p. 27-28). 10 November has official ceremonies and road closures, so the mass-event concern applies to us. Section: Robustness.
  - Results-Discussion: money value by commuters x trip time x percent change x value per hour, with GDP per hour worked as the price (p. 30-31). Section: Results-Discussion.

- **Caveats.**
  - The speed outcome is a city-day (or city-peak-hour) index, 2 years, 5 cities, 26 strikes; the headline 8.4% has p = 0.07. It is not an hourly panel of road segments.
  - The paper gives the percent change in travel time but no free-flow speeds, so minutes of delay per km cannot be computed from it. I did not find a min/km figure.
  - `literature/notes/probe_data_methods.md` describes the design as "event-day vs. comparison-day DiD ... differenced against other hours". The paper does not difference the strike hour against other hours of the same day; identification is from fixed effects across days and cities. Strike days are whole days, so there is no within-day contrast.
  - The EUR 3.2 million is per city per strike day (our reading: 71 strike events x 3.2 = 228.9).
  - The value of time is GDP per hour worked, which is much higher than the half-wage convention in anderson2014 and yang2020. The choice matters a great deal for any money value.
  - No statement on the speed-density relationship or on propagation of a brief stop.

- **Checks or analyses it suggests for us.**
  - Plot the hour-by-hour (and for the 2026 index, 5-minute) treatment effect across the whole day with confidence bands, as in their Figure 3 (p. 18). Effects should be zero away from 09:05.
  - Control for school holidays. To verify against the official calendars (from my memory, not from this paper): the Turkish November mid-term school break has fallen in the week after 10 November in several sample years, so the Nov 17 control date may be a school-holiday day. If so, drop or flag those control dates.
  - The papers in this group all restrict to workdays. From the calendar, 10 Nov 2024 was a Sunday. Show the estimate with and without 2024, and by weekday/weekend.
  - Add hourly rain and temperature as covariates, or show robustness to dropping years with rain on the morning of Nov 10 or of a control date.

---

### adler2021 - Adler, Liberini, Russo and van Ommeren (2021), The congestion relief benefit of public transit: evidence from Rome

- **Question and setting.** How much does public transit supply reduce road travel time for cars and for buses? Uses 43 partial transit strikes in Rome with hourly variation in the share of scheduled service that actually ran (p. 2, p. 8-9).

- **Data and method.**
  - Source: loop detectors of Rome's Mobility Agency (footnote 12, p. 6). This settles the open question in our earlier notes: sensors, not probes.
  - Unit: road-by-hour. 33 measurement points, 5 a.m. to midnight, 769 workdays from 2 Jan 2012 to 22 May 2015; 422,691 observations, about 23,000 during strikes (p. 5-7).
  - Outcome: travel time in min/km, obtained by inverting the hourly average spot speed. Flow is hourly count converted to per minute assuming it is constant in the hour: "we ignore within-hour variation" (footnote 12, p. 6). Density is computed as flow times travel time (p. 6).
  - The speed is instantaneous at the detector and excludes waiting at traffic lights, so it is far above trip speed (mean 1.33 min/km = 46 km/h) (p. 7).
  - Cleaning: drop travel time above 5 or below 0.4 min/km and flow of zero or above 2,100 veh/hour; keep only hours with at least 20 of 33 locations reporting (footnote 13, p. 6).
  - "Heavily congested" hour: speed below 60% of free-flow speed, with free flow = 95th percentile of that road's speed distribution (p. 7).
  - Estimator: log T_it = road FE + psi_n * S_t + controls + e_it, where S_t in [0,1] is the city-wide share of scheduled transit running in hour t, and n indexes morning peak, afternoon peak, off-peak (eq. 4, p. 11). Controls: hour-of-the-week dummies, week-of-the-year dummies, rain, temperature, strike type (p. 11).
  - Weights: proportional to each road's average hourly flow, to represent the average traveller (p. 12).
  - Inference: standard errors clustered by hour (p. 12). Robustness with day fixed effects, clustering by location, by location and week-of-year (two-way), and by day; results change little (Table B1, p. 31-32).
  - Theory used: Underwood form T = b * exp(a * D), with density D = F * T (eq. 1, p. 3). Hypercongestion (flow falling as density rises) occurs in fewer than 1.5% of hours and is ignored (p. 4).

- **Main findings.**
  - A 10-percentage-point cut in transit supply raises motor-vehicle travel time in the morning peak by about 1.6% (coefficient -0.160, SE 0.031), about 0.024 min/km. Afternoon peak 0.67% (0.01 min/km). Off-peak 0.39% (0.0065 min/km). Peak average 0.017 min/km (p. 15, Table 4 p. 16).
  - Heavily congested roads, morning peak: about 3% (coefficient -0.293), 0.052 min/km. One-lane central roads: 0.7%, 0.013 min/km (p. 15-16).
  - Flow rises by 0.6 to 0.8% per 10 points, less on heavily congested roads (p. 16, Table 5 p. 17).
  - The marginal effect is about constant over the range of supply; a constant effect cannot be rejected, with low power at the extremes (p. 16, footnote 31).
  - Placebos: night hours show identical travel times on strike and non-strike days (footnote 29, p. 15); cancelled strikes have no effect (p. 12); buses on dedicated lanes show no effect (p. 18-19).
  - Peak versus off-peak in levels: travel time, flow and density are 13%, 38% and 50% higher in the peak (p. 10).
  - Bus travel time rises 1.95% per extra vehicle per lane-km of density (IV; 1.6% OLS) on mixed-traffic roads (Table B3, p. 33).
  - Money value: a 10-point cut costs motorists 3.8 million hours a year, EUR 59.5 million at a value of time of EUR 15.59/hour; with bus users (valued at EUR 9.54/hour) the total is EUR 75 million a year (p. 20-21). Extrapolated full shutdown: 38 million hours, EUR 595 million, flagged by the authors as less reliable (p. 21).
  - Marginal external congestion cost of a vehicle-km in Rome: EUR 0.29 in the peak (0.21 on other motorists plus 0.08 on bus riders) and EUR 0.13 off-peak (p. 23, Table 8 p. 24).
  - Transit as a whole lowers morning-peak motor-vehicle travel time by roughly 15% (p. 24).

- **Usable for our paper.**
  - Method: direct precedent for log travel time (= minus log speed) as the outcome in an hourly road panel (eq. 4, p. 11). Section: Method.
  - Method: hour-of-the-week plus week-of-the-year fixed effects as the counterfactual; day fixed effects as a robustness check (p. 11-12, p. 31). Section: Method / Robustness.
  - Data: explicit acknowledgment that hourly data hide within-hour variation (footnote 12, p. 6) and that spot speeds miss time spent stopped at lights (p. 7). Both parallel our hourly dilution and MINIMUM_SPEED >= 1 km/h problems. Section: Data.
  - Robustness: placebo hours (night), placebo events (cancelled strikes) and a placebo outcome (dedicated lanes) (p. 12, p. 15, p. 19). Section: Robustness.
  - Robustness: an operational definition of congested road-hours relative to a road-specific free-flow percentile (p. 7), an alternative to our fixed km/h speed classes. Section: Robustness.
  - Results-Discussion: benchmark effect sizes in min/km and a European value of time (EUR 15.59/hour for car users) (p. 15, p. 20). Section: Results-Discussion.

- **Caveats.**
  - Small inconsistencies inside the paper: the morning-peak effect is given as 0.024 min/km (p. 15) and elsewhere as 0.027 (p. 17); Appendix B1 describes a white-strike coefficient of 0.021 as an increase of about 0.2% and 0.032 min/km, which do not agree with each other (p. 31). Quote the main Table 4 numbers only.
  - The paper does not report the estimated parameter a of T = b*exp(a*D) for motor vehicles. I could not find it, so we cannot take a speed-density elasticity for cars from this paper.
  - Demand shock via mode switching over whole hours, with strikes announced days ahead (p. 8). Not a capacity interruption of minutes.
  - Our earlier note says "hour-of-day x day fixed effects". The main specification uses hour-of-the-week and week-of-the-year dummies; day fixed effects are only in the sensitivity table.
  - Effects are LARGER on heavily congested roads. This is the opposite gradient from our pilot (no effect in congested cells). The mechanisms differ (extra cars versus a brief stop), so the paper does not contradict us, but it gives no support for a null in congested cells either.
  - 33 points chosen by the agency; not a network-wide sample.

- **Checks or analyses it suggests for us.**
  - Redefine speed classes relative to each cell's own free-flow speed (for example 95th percentile of its hourly speeds): congested = below 60% of free flow at 09h on control dates. This gives one pre-specified split instead of five absolute classes and reduces the multiple-testing burden.
  - Placebo hours: apply the same contrast to every hour h of 10 November, c_h = ln v(h) - mean(ln v(h-1), ln v(h+1)), and show that only h = 09 stands out.
  - Apply a cleaning rule of the same kind (drop implausible speeds; require a minimum share of cells reporting in each date-hour) and state it.
  - Report the estimate also in min/km: delta T = (60/v0) * (exp(-D) - 1) at the class baseline speed v0.

---

### hanna2017 - Hanna, Kreindler and Olken (2017), Citywide effects of high-occupancy vehicle restrictions: "three-in-one" in Jakarta

- **Question and setting.** What happened to traffic when Jakarta abruptly dropped its 3+ occupancy rule on central roads in April 2016? (p. 1).

- **Data and method.**
  - Source: Google Maps API "live" travel times (from Android phone traces), queried for each route every 10 minutes, 24 hours a day, starting two days after the announcement (p. 1). DOI 10.1126/science.aan2747 (p. 5).
  - Outcome: delay in minutes per kilometre, where "delays are defined as the inverse of speed" (p. 2). So "delay" here is total travel time per km, not excess over free flow.
  - Unit: route segment x direction x date x departure time. Phase 1: one former HOV road and two alternates, with 2.5 weekdays of pre-period; phase 2 (from 28 April): two HOV roads and eight alternates, with no pre-period (p. 1-2).
  - Two counterfactuals: (a) the 2-3 pre-period weekdays; (b) Google's own "predicted" trip duration for the same route, weekday and departure time under typical traffic, which had not yet absorbed the policy change (p. 1, p. 4).
  - Estimator: for each road and time window, delay_idh = a + b*post_d + g*northbound_i + e (p. 3). A before/after difference per window, not a difference-in-differences.
  - Inference: standard errors clustered by date x direction; figures use local linear regression on departure time (Epanechnikov kernel, 0.2-hour bandwidth) with pointwise bootstrap 95% bands clustered the same way (p. 2).

- **Main findings.**
  - Former HOV road, morning peak 7-10 a.m.: +0.98 min/km (SE 0.07), +46% on a base of 2.14; speed from 28 to 19 km/h (p. 3, Table 1).
  - Evening peak 4:30-7 p.m.: +2.48 min/km (SE 0.30), +87% on 2.84; speed from 21 to 11 km/h (p. 3).
  - Never-restricted hour 7-8 p.m.: +1.98 min/km (+55%); midday +0.55 min/km (p. 3-4).
  - No change 6-7 a.m. (-0.00) or at night (+0.05) (Table 1 p. 3, p. 4).
  - Never-restricted alternate road: evening +0.60 min/km (14%), midday +0.71, 7-8 p.m. +1.32 (Table 1 p. 3, p. 4).
  - With the Google-predicted counterfactual: HOV roads +0.88 (morning) and +2.29 (evening, nearly 70%); eight alternate routes +0.64 midday (21%), +1.06 evening (29%), +1.10 at 7-8 p.m. (34%) (Table 2 p. 4).
  - Benchmarks the authors give: London congestion charge about -0.6 min/km; Anderson's strike +0.2 to 0.4 min per mile; Delhi odd-even about -0.2 min/km (p. 5).
  - Mechanism discussion: lifting the rule may have pushed the main road into hypercongestion (higher density lowering throughput), forcing traffic elsewhere, or congestion may have spilled back through the network; the data cannot separate these (p. 4).

- **Usable for our paper.**
  - Data: the main precedent for phone-probe travel times at sub-hourly resolution as a causal outcome (p. 1). Supports our use of the 5-minute İBB index. Section: Data.
  - Method: a provider's "typical traffic" profile by weekday and time of day is an accepted counterfactual (p. 1, p. 4). For the 2026 index the analogue is the same weekday x 5-minute slot average. Section: Method.
  - Method: reporting in minutes per km and the plot of delay against time of day with pointwise bands (Fig. 2, p. 2). Section: Method / Results.
  - Robustness: hours where nothing should change (6-7 a.m., night) as built-in placebos (p. 4). Section: Robustness.
  - Results-Discussion: table of benchmark magnitudes for policies (p. 5). Section: Results-Discussion.
  - Results-Discussion: one of the few statements in this group that a local disruption can spread across the network and over later hours through spillback or hypercongestion (p. 4). Use only as a possibility. Section: Results-Discussion.

- **Caveats.**
  - "Delay" means min/km of travel time. It must not be mixed with Anderson's delay (excess over free flow).
  - The shock is permanent, the comparison is before/after with 2.5 pre-period weekdays, so the number of pre-period clusters is very small. The predicted-counterfactual check is what carries the paper.
  - Our earlier note calls the design "DiD on routes x time of day"; it is a per-road, per-window before/after difference. The earlier note's "every ~20 min" is 10 minutes in the published paper (p. 1). The 46% and 87% figures are confirmed (p. 3).
  - A handful of chosen routes, not a network sample. Welfare is explicitly not evaluated (p. 5).
  - No value of time, no cost of delay, no speed-density estimate.
  - Effects are huge in an already very congested city, again the opposite gradient to our null in congested cells.

- **Checks or analyses it suggests for us.**
  - For the 5-minute index: plot 10 Nov 2026 against the mean of same-weekday control days by 5-minute slot, local-linear smoothed, with bootstrap bands clustered by date; then estimate the dip and its duration around 09:05 and integrate it to get index-minutes lost.
  - Use the 5-minute dip to calibrate the hourly dilution: what share of the 09h mean does a dip of that shape and length represent?
  - Check for after-effects: test 10h and 11h on 10 Nov against controls. If a queue-discharge effect persists into 10h, our contrast (which uses 10h as a control hour) is biased toward zero.

---

### yang2020 - Yang, Purevjav and Li (2020), The Marginal Cost of Traffic Congestion and Road Pricing: Beijing

- **Question and setting.** What is the causal speed-density relationship on Beijing's major roads, and what marginal external cost of congestion and optimal charge follow from it? (p. 1, p. 3). Now verified: AEJ: Economic Policy 12(1): 418-453, DOI 10.1257/pol.20170195 (p. 1).

- **Data and method.**
  - Source: 1,528 roadside microwave traffic sensors on freeways and expressways (no secondary roads), recording speed and volume every 2 minutes in 2014; aggregated to road segment x hour, about 12.1 million observations (p. 9). Not probe data.
  - Density is computed as volume divided by speed per lane (p. 10). Means: speed 67.3 km/h (SD 14.5), volume 565 veh/hour/lane, density 9.55 veh/km/lane (Table 2, p. 12).
  - Model: linear Greenshields relation, Speed_it = alpha + beta * Density_it + weather + month, hour, day-of-week, holiday FE + road FE + ring-road x hour FE + e (eq. 3 p. 6; eq. 5 p. 11-12).
  - Identification: density and speed are jointly determined (accidents, events, roadworks lower both), so OLS is biased toward zero. Instrument: days on which plates ending in 4 or 9 are banned. Few plates end in 4 (about 14% of cars are in the (4,9) pair against 20-22% for other pairs), so more cars are on the road on those days; interacted with ring road and hour (p. 13-17, Table 4 p. 15).
  - Inference: standard errors clustered by road segment (p. 17). First-stage F = 53 in the preferred specification (Table 7 p. 19).
  - Marginal external cost of congestion per vehicle-km:
    MECC = o * VOT * T * eps / (1 - eps), with eps = -beta * D / S the elasticity of speed to density, T = 1/S, o = occupancy (eq. 2 p. 6; eq. 7 p. 21).
  - Travel time as a function of volume under ordinary congestion: T(V) = (2/alpha) / (1 + sqrt(1 - V/V_m)), with capacity V_m = -alpha^2 / (4*beta) (eq. 4, p. 6).
  - Parameters: occupancy 1.34; value of time 50% of the market wage, the wage being CNY 62.98/hour (p. 21).

- **Main findings.**
  - OLS slope: -0.67 to -0.75 km/h per vehicle per lane-km (Table 6, p. 18). IV slope: -1.098 (SE 0.044) in the preferred specification, intercept 77.9 km/h; 1.6 times the OLS slope (Table 8, p. 20).
  - On (4,9) days density inside the third ring road is about 1.5 vehicles per lane-km higher, mostly in peak hours (p. 17).
  - MECC: about CNY 0.30 per vehicle-km at 1,000 veh/lane-hour (speed about 60 km/h); CNY 1.98 (USD 0.30) inside the second ring road in the evening peak (about 1,200 veh/lane-hour, 29 veh/lane-km); OLS would give 1.2 (p. 21).
  - On arterials at the reported 23 km/h peak speed, the implied MECC is about CNY 7.4 (USD 1.16) per vehicle-km (p. 22).
  - Aggregated over 6 a.m.-11 p.m.: city-wide average MECC CNY 0.15 per vehicle-km; 0.82 inside the third ring in the peak; 0.06 outside the fifth ring off-peak (Table 9, p. 26).
  - Total value of time lost to congestion relative to free flow: nearly CNY 10 billion in 2014, about half a percent of Beijing's GDP (p. 26-27).
  - Optimal charges CNY 0.05 to 0.39 per km; speed inside the third ring up 11% (p. 27, Table 10 p. 28).
  - The estimated relation implies an exponent of about 7.6 in the BPR travel-time formula T - T_f = a * V^b, against the conventional 4 (range 2.5 to 5) (footnote 13, p. 20-21).
  - Hypercongestion is set aside because of the "dynamic, local, and transient nature of hyper-congestion" (p. 5); after averaging to ring road x period it is not observed (p. 25).
  - Sensor speeds are higher than taxi-GPS speeds in official reports, partly because sensors sit on less congested segments (footnote 15, p. 22).

- **Usable for our paper.**
  - Method / Results-Discussion: the only causal speed-density estimate in this group: one more vehicle per lane-km lowers speed by about 1.1 km/h on major roads (p. 20). Section: Results-Discussion.
  - Method: the argument that unobserved events lower density and speed together, biasing naive speed-density slopes toward zero (p. 13, p. 20). Relevant if we relate our speed effect to NUMBER_OF_VEHICLES. Section: Method.
  - Data: precedent for aggregating 2-minute sensor data to the road-hour and for clustering by road segment (p. 9, p. 17); also a published acknowledgment that sensor and probe (taxi GPS) speeds differ (p. 22). Section: Data.
  - Results-Discussion: the money-value convention, value of time = half the wage and occupancy 1.34 (p. 21), and the scale benchmark "half a percent of GDP" for all congestion (p. 26-27). Section: Results-Discussion.
  - Results-Discussion: the authors say the framework can be moved to another city by adjusting alpha to local free-flow speed, with caution (p. 23, footnote 16). Section: Results-Discussion.

- **Caveats.**
  - Our calculation, not in the paper: with alpha = 77.9 and beta = -1.098 the fitted line implies capacity of about 1,380 veh/hour/lane, reached at about 35 veh/km/lane and about 39 km/h (alpha/2), and jam density of about 71 veh/km/lane. In a Greenshields world, cells below roughly half of free-flow speed are on the hypercongested branch, where this paper's formulas do not apply.
  - Our check: the reported CNY 0.30 and 1.98 are reproduced with a value of time of about CNY 31.5/hour (half of 62.98). The sentence on p. 21 is ambiguous on whether 62.98 is the wage or the value of time; the arithmetic says it is the wage.
  - MECC is the cost one extra vehicle-km imposes on others in steady ordinary congestion. A simultaneous 1-2 minute stop is a direct time loss for everyone on the road, not a marginal vehicle-km. MECC is therefore not the right price for the stop itself; it would only apply to any induced extra congestion afterwards.
  - Two different "average MECC" numbers appear: CNY 0.46 per vehicle-km (p. 21) and CNY 0.15 (Table 9, p. 26). They come from different aggregation levels. Do not quote one as "the" Beijing average without saying which.
  - Standard errors are clustered by road segment only, which ignores correlation across segments within an hour or day. Not a model for our inference.
  - Hourly averages of a static relation; nothing on shockwaves, queue discharge or a brief capacity loss. Expressways only.
  - Earlier notes listed this paper as [UNVERIFIED] with "road-segment speed data"; it is verified and the data are fixed microwave sensors.

- **Checks or analyses it suggests for us.**
  - Descriptive speed-density plot for Istanbul cells (AVERAGE_SPEED against NUMBER_OF_VEHICLES per cell, 08-10h on control dates) to see which cells sit on the congested branch; use it to motivate the speed classes.
  - Test NUMBER_OF_VEHICLES at 09h on 10 Nov with the same contrast. Under a pure stop (no demand change) the count should not move much; a change would signal a demand or sampling effect (for example ceremony traffic, or stopped vehicles dropping out of the sample).
  - Money value of the stop as a direct time loss (see the template below), with value of time at half the Istanbul hourly wage and a sensitivity range (x1.8 delay multiplier; GDP per hour worked as an upper case).

---

## Effect sizes in comparable units

| Paper | Shock and length | Data grain | Effect as reported | Approx. % travel time | min/km |
|---|---|---|---|---|---|
| anderson2014 | full transit strike, 35 days | detector-hour, loop | +0.194 min/mile delay, +47% of delay (p. 17) | about +14% (our conversion) | 0.12 (our conversion) |
| anderson2014, a.m. peak | same | same | +0.314 min/mile, +67% of delay (p. 18) | about +21% (our conversion) | 0.20 (our conversion) |
| bauernschuster2017 | partial strike, 1 day | city-day index, GPS probe | CI +0.123 on 1.47, 8-9 a.m. (p. 21-22) | +8.4% | not reported |
| adler2021 | 10-point transit cut, hours | road-hour, loop | log T +0.016, a.m. peak (p. 15) | +1.6% | 0.024 |
| adler2021, full shutdown | extrapolated | same | 0.17 min/km peak (Table 7, p. 22) | about +15% a.m. (p. 24) | 0.17 |
| hanna2017, a.m. | HOV rule lifted, permanent | 10-min API queries | +0.98 min/km (p. 3) | +46% | 0.98 |
| hanna2017, p.m. | same | same | +2.48 min/km (p. 3) | +87% | 2.48 |
| ours, 50-70 km/h cells | 1-2 min stop | cell-hour | 0.73 full-stop-equivalent min | +1.2% over the hour | about 0.012 at 60 km/h |
| ours, 30-50 km/h cells | 1-2 min stop | cell-hour | 0.45 full-stop-equivalent min | +0.8% over the hour | about 0.011 at 40 km/h |

Rows for "ours" are our conversions: D = ln(1 - m/60), travel-time change = exp(-D) - 1, and min/km = (60/v0) * (exp(-D) - 1).
Read this way, our hourly effect is about one tenth of a one-day strike effect and one hundredth of the Jakarta effect per km driven. If the whole loss falls inside one 5-minute window, the within-window slowdown is about 12 times larger (roughly 15%), the size of a full transit shutdown but lasting minutes.

Money-value template assembled from these papers (the formula is ours; the conventions are theirs):

cost = (vehicles on the road at 09:05) x (occupancy) x (full-stop-equivalent minutes / 60) x (value of time per hour)

- Occupancy: 1.34 (Beijing, yang2020 p. 21); 1.4 in the peak (Rome, adler2021 p. 5-6).
- Value of time: half the gross hourly wage (anderson2014 p. 9, p. 21; yang2020 p. 21); EUR 15.59/hour for car users (adler2021 p. 20); GDP per hour worked, EUR 52 (bauernschuster2017 p. 31).
- Optional multiplier of 1.8 for time lost in congestion (anderson2014 p. 7, p. 21).
- None of the five papers gives a value of time for Turkey. It has to come from Turkish wage data.

What I could not find in any of the five papers: a study of a shock shorter than several hours; any treatment of vehicles that are stopped and missing from speed data; any model of how a brief capacity loss propagates (shockwave, queue discharge); any within-day hour-against-neighbouring-hours contrast. These remain our contribution and need support from the traffic-engineering group of readings.

## Cross-paper synthesis

1. Hourly location-level speed or travel time is the normal grain (anderson2014, adler2021, yang2020); only hanna2017 goes below the hour. All shocks studied last hours to weeks, so hourly dilution of a 1-2 minute event is a problem none of them faced and we must handle ourselves with the 5-minute index.
2. The counterfactual everywhere is "same clock hour and weekday on other days", built with hour-of-week and week-of-year fixed effects or an RD in date. Nobody differences against adjacent hours of the same day; our within-day contrast is new and needs its own placebo hours.
3. Outcome units are log travel time (adler2021), min/km or min/mile (anderson2014, hanna2017) or a travel-time index (bauernschuster2017). Report ours in log speed, in min/km and in full-stop-equivalent minutes. Never compare with Anderson's 47%, which is a share of delay over free flow; the comparable figure is about 14% of travel time.
4. Inference: errors are correlated across locations within a day and over time within a location. Anderson clusters two-way by day and detector; Bauernschuster uses city clusters with wild bootstrap. Clustering by road only (yang2020) is not adequate for us. Randomization inference over dates is consistent with the stricter practice.
5. Every credible paper shows placebos: unaffected places, the same dates in another year, cancelled events, hours where nothing should happen, a placebo outcome. We should show placebo hours on 10 Nov, placebo dates, and a placebo outcome (vehicle counts).
6. Seasonal drift in Oct-Nov made a naive before/after comparison show a false +32% in Anderson's control area. Our fixed position of Nov 10 among the control dates needs a trend check, symmetric controls, and a check of school-holiday and weekend status of each date.
7. Weighting changes the estimand: flow or VMT weights give the average driver (anderson2014, adler2021); equal weights give the average location. Report both.
8. In all demand-shock papers the effect is larger where and when roads are more congested. Our pilot shows the reverse. This is most likely measurement (stopped vehicles excluded, speeds already low) or the different nature of a stop, and it has to be explained, not just reported.
9. Money value: hours lost times value of time, with half the wage as the conservative convention, a 1.8 multiplier or GDP per hour as upper cases, and occupancy near 1.3-1.4. Marginal external cost per vehicle-km (EUR 0.29 peak in Rome; CNY 0.15 to 1.98 in Beijing) prices an extra vehicle, not a stop, and should not be used for the stop itself.
10. Speed-density: yang2020 gives a causal linear slope of -1.1 km/h per vehicle per lane-km and stresses that naive slopes are biased toward zero; anderson2014 and adler2021 use power and exponential forms. None says how a brief capacity loss propagates; hanna2017 only raises spillback and hypercongestion as possibilities.
