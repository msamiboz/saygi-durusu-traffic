# Group 10 - Collective events in passive data (Focus A) and İBB traffic data (Focus B)

Reader notes for: bagrow2011, botta2015, meier2014, pinter2021, ngeni2022 (Focus A);
utku2023, ozkurt2025, takak2021, alcan2022, olug2024, tanberk2023, energies2021 (Focus B).

Conventions
- `(p. N)` is the page marker in `literature/txt/<key>.txt` (PDF page). Where the journal page differs it is given once per paper.
- "Not stated" means I read the whole text and could not find it.
- Lines starting with **[my inference]** or **[my calculation]** are mine, not the paper's. Do not cite the paper for them.
- Some facts for tanberk2023, utku2023 and olug2024 come from figures (screenshots of data frames, plots) that are not in the text file. I read them from the PDF page and say so.

---

## Focus A - collective events in passive data

### bagrow2011 - Bagrow, Wang & Barabási (2011), Collective response of human populations to large-scale emergencies (PLoS ONE 6(3): e17680)

- **Question and setting.** How do calling and mobility patterns change in real time around emergencies (bombing, plane crash, earthquake, blackout, storms) compared with planned mass events (concerts, festivals)? One western European country, mobile phone billing records.
- **Data and method.**
  - About 10 million subscribers of one operator with roughly one quarter of the market; each record has caller, callee, tower, time (p. 1, p. 6). The media scan for events covers January 2007 to January 2009 (p. 1); the Methods say the records cover 3 years (p. 6).
  - 16 events: 8 emergencies and 8 planned non-emergencies (Table 1, p. 2). About 30% of media-reported events were dropped because coverage was sparse or few users were active at that hour (p. 1).
  - **Baseline.** Expected call volume is the mean over "normal" periods that are the same time of the week, shifted by whole weeks from the event (weekly periodicity). Series are binned to 5-10 minutes (p. 7). How many normal weeks are averaged is not stated in the main text (it refers to File S1).
  - **Signal to size.** Excess volume ΔV(t) = V_event(t) - <V_normal>(t), reported as the relative excess ΔV/<V_normal> (p. 2). A standardised version z(t) = ΔV(t)/σ(V_normal)(t) defines the event window as the longest contiguous run with z(t) > z_thr, with z_thr = 1.5 for all events (p. 7).
  - **Decomposition.** The excess is split into change in calls per user and change in number of active users (Fig. 1C, p. 3).
  - **Spatial extent.** Excess volume integrated over time in concentric shells; fitted ΔV(r) ~ exp(-r/r_c) (p. 2).
- **Main findings.**
  - Emergencies produce an immediate jump followed by decay lasting three to five hours; planned events build up gradually over seven or more hours (p. 2).
  - The excess comes mainly from people who would not normally be calling at that time, not from more calls per active user (p. 2, Fig. 1C p. 3).
  - Spatial decay length r_c is 2 km (bombing) to 10 km (plane crash), about 110 km for the earthquake, and below 2 km for all planned events (p. 2; Table 1 p. 2).
  - Event populations range from 750 users (bombing) to 84,751 (blackout) (Table 1, p. 2).
- **Usable for our paper.**
  - Literature / Method: the standard passive-data counterfactual is the same time slot in other weeks, i.e. our same-weekday control dates. "average call activity during the same time period of the week" (p. 2).
  - Method: excess over baseline, relative to baseline, as the size measure (p. 2). Our D is the log version of this on speed.
  - Introduction: phones as in-situ sensors of a population-wide reaction to a shock, observable at short time scales (p. 1, p. 6).
  - Results-Discussion: an intensive vs extensive margin split (more participants vs more activity per participant) is informative (p. 2-3); our analogue is "more vehicles stopping" vs "longer stops", which hourly means cannot separate.
- **Caveats.**
  - No formal inference. The z > 1.5 rule is a descriptive threshold on a per-bin standard deviation; no p-values, no confidence intervals, no correction for scanning many time bins. Do not cite it as a test.
  - Event sample is selected on detectability (30% of events dropped, p. 1).
  - Unplanned shocks, one occurrence each. Our event is scheduled, known in advance and repeated annually, which is closer to their "non-emergency" class in predictability but has a sharp onset like their emergencies.
- **Checks it suggests for us.**
  - Report a standardised effect per year: D_year divided by the standard deviation of the same contrast across control dates.
  - Spatial profile: does the contrast vary with cell type (arterial vs local), in the spirit of their r_c analysis? With a city-wide siren we expect no distance decay, so a flat spatial profile is itself a prediction that separates the siren from a local incident.

### botta2015 - Botta, Moat & Preis (2015), Quantifying crowd size with mobile phone and Twitter data (R. Soc. Open Sci. 2: 150162)

Page note: text page 1 is the repository cover sheet; the article starts on text page 2.

- **Question and setting.** Can phone and Twitter activity estimate how many people are in a bounded place? Two Milan cases: San Siro stadium and Linate airport, 1 November to 31 December 2013.
- **Data and method.**
  - Telecom activity (calls, SMS, internet connections) at 10-minute granularity on a grid of 10,000 cells of 235 m x 235 m; geolocated tweets (p. 3).
  - Stadium: official attendance for 10 matches (p. 4). For each match they take the **maximum** of the activity spike and regress attendance on it by OLS (p. 4).
  - Airport: no head count. Proxy = number of flights departing in the next 2 hours or arriving in the previous hour, built from one week of May 2014 schedules and assumed constant; compared with mean activity per hour-of-week over eight weeks, N = 168 (p. 5).
  - **Baseline.** None is subtracted. The size measure is the raw peak level, not an excess over a counterfactual.
  - **Inference.** OLS with p-values and Spearman rank correlations; leave-one-out prediction with 95% prediction intervals (p. 4-5).
- **Main findings.**
  - Stadium, N = 10: adjusted R² = 0.771 (calls and SMS), 0.937 (internet), 0.855 (Twitter), all p < 0.001; Spearman ρ = 0.927, 0.976, 0.924 (p. 4-5).
  - Leave-one-out with internet activity: actual attendance lies inside the 95% prediction interval for all 10 matches (p. 5).
  - Airport, N = 168: adjusted R² = 0.175 (calls and SMS), 0.143 (internet), 0.510 (Twitter) (p. 5-6).
- **Usable for our paper.**
  - Literature: example of converting a passive signal into a head-count through a calibration against ground truth (p. 4-5).
  - Results-Discussion (limits): they can calibrate because attendance is known. We have no ground truth for the share of drivers who stop, so our "full-stop-equivalent minutes" is a scale transformation, not a calibrated participation rate. This paper is the right contrast to cite when saying so.
  - Robustness: leave-one-out as a small-N check (p. 5); our analogue is leave-one-year-out on the five-year average.
- **Caveats.**
  - N = 10 matches from one stadium over two months. The linear fit is strong but the sample is tiny.
  - They note the phone data "may be affected by capacity constraints, such as signal truncation" (p. 5). The same kind of ceiling/floor problem applies to our MINIMUM_SPEED floor.
  - The airport result is weak and the "truth" is itself a proxy.
  - The paper says nothing about counterfactual construction; do not cite it for baselines.
- **Checks it suggests for us.**
  - Leave-one-year-out estimates of D and of the randomization p-value.
  - If any external ground truth exists for one year (for example a video count of stopped vehicles on one arterial, or the 5-minute city index in 2026), calibrate the hourly contrast against it once and say that the mapping is from a single calibration.

### meier2014 - Olexsak & Meier (2014), The electricity impacts of Earth Hour (Energy Research & Social Science 2: 159-182)

The repository key says meier2014; the authors are Sarah J. Olexsak and Alan Meier, and the citation should be Olexsak & Meier (2014). Text page N = journal page 157 + N (text p. 2 = journal p. 159).

- **Question and setting.** How much does electricity demand fall during Earth Hour, a voluntary one-hour coordinated switch-off? A compilation of reported demand changes, not an analysis of load data.
- **Data and method.**
  - **Number of observations: 274** reported demand changes, 10 countries, six years 2007-2012 (p. 5). Sources are system operators, utilities and distributors, press reports citing them, and personal communication (p. 4). Reported MW changes were converted to percentages (p. 4).
  - The sample is very uneven: Canada 231, Australia 18, United States 8, New Zealand 5, Israel 4, Indonesia 3, Sweden 2, Ireland 1, Qatar 1, UAE 1 (Table 1, p. 5).
  - **Baselines used by the reporting entities** (p. 4, repeated p. 5): 196 cases compare observed demand with a forecast; 64 with a "normal" or average demand; 6 with the time immediately before Earth Hour; 8 have no method available. Method known for 266 of 274 (97%).
  - Examples of baselines (p. 4-5): Ausgrid (Sydney CBD) fits demand against a temperature index using all Saturdays in March and April over three years and predicts the Earth Hour Saturday from actual temperature; Transpower (NZ) uses commercial forecasting software weighting similar past days (previous day, week, month, year) and adjusting for temperature and cloud cover; Essential Energy compares with the same period one week earlier; PLN (Jakarta) with the same period two weeks earlier.
  - **Inference.** None. No standard errors, tests or intervals. The headline is an unweighted mean of heterogeneous reports.
- **Main findings.**
  - **Average effect: 4.0% reduction; median 2.6%** (p. 5; Table 1 p. 5).
  - Range: from an increase of about 2% (New Zealand; Table 1 gives -2.1) to a 28% reduction (Canada) (p. 5).
  - Country means: Australia 6.6%, Canada 3.9%, Indonesia 3.9%, Israel 5.3%, New Zealand 3.6%, Sweden 2.3%, United States 1.8% (Table 1, p. 5).
  - **What the paper says about baselines.** The preferred method compares observed demand with a projected demand from system-operator forecasting tools that use equivalent days and adjust for temperature, cloud cover, major weather events and holidays; comparing with "the same date one week or one-year prior is not adequate" (p. 5). The organiser (WWF) itself says electricity savings are a poor indicator because weather and other factors affect them, especially when a single historical period is the comparison (p. 3). Methods differed between entities and changed from year to year within the same entity; one utility issued an estimate (5%) and two days later a revised one (7%) after changing method (p. 5; refs. 37-38, p. 25).
  - Other synchronised-behaviour examples: TV pickup in Ireland, a 6% demand dip during an Olympic boxing final, and a 3% dip at the start of a Euro 2012 match followed by roughly a 7% surge at the end (p. 4); Juneau, Alaska cut demand by 25% after an avalanche (p. 4); an Iranian protest tried to synchronise appliance use (p. 4).
  - One cited study found that conservation calls shifted consumption within the day with little net reduction (p. 4).
- **Usable for our paper.**
  - Introduction: a short, scheduled, voluntary collective act that is visible in infrastructure data at system level (p. 2, p. 5). Earth Hour is the closest published analogue to the siren stop: fixed clock time, about an hour or less, annual, participation is voluntary.
  - Literature: order of magnitude for comparison, a 4% mean and 2.6% median reduction over one hour (p. 5). Our pilot effect is on a different quantity (speed, about 0.75% to 1.2% of an hour in stop-equivalent minutes), so compare with care.
  - Method / Robustness: the paper is direct support for (a) not relying on a single comparison date and (b) the sensitivity of estimates to baseline choice (p. 3, p. 5). This backs our move from three control dates to all same-weekday dates, and a weather adjustment.
  - Results-Discussion: displacement and release (TV pickup, p. 4) and intra-day shifting (p. 4) are the electricity versions of our within-hour rebound: vehicles that stop at 09:05 may drive faster or bunch afterwards, which pulls the hourly mean back.
- **Caveats.**
  - This is a compilation of self-reported figures, 84% from Canada (231 of 274), with mixed baselines. "Average 4%" is not a population-weighted or precision-weighted estimate, and has no uncertainty attached.
  - Likely reporting selection (entities that publish a number are those that looked for one); the paper does not discuss this.
  - Internal count inconsistency: 64 cases published with a method plus 203 obtained by personal communication is 267, but the paper says methods were available for 266 (p. 4, p. 5). Minor; cite 274 total and the 196/64/6/8 split.
  - The paper recommends forecast-based baselines but does not test whether they give different answers from simple ones.
  - If earlier notes describe this paper as "estimating" a 4% effect, soften to "compiling reported reductions averaging 4%".
- **Checks it suggests for us.**
  - Baseline sensitivity table: D under (i) Nov 3/17/24 controls, (ii) all same-weekday dates, (iii) weather-adjusted or regression-forecast counterfactual. Report all three, as the paper's main lesson is that the answer depends on this.
  - Report the median across years as well as the mean, since one year can dominate (their mean 4.0 vs median 2.6).
  - Look for a rebound signature in the 5-minute city index (Oct-Nov 2026): dip at 09:05-09:10 followed by an overshoot.

### pinter2021 - Pintér & Felde (2021), Analyzing the behavior of soccer fans from a mobile phone network perspective: Euro 2016 (arXiv:2108.09291, preprint)

- **Question and setting.** Do Call Detail Records in Budapest reflect fans' behaviour during Hungary's four Euro 2016 matches played in France, and the street celebration after the Portugal match?
- **Data and method.**
  - Vodafone Hungary CDRs for June 2016, Budapest and agglomeration: 2,291,246,932 records from 2,063,005 SIM cards; operator market share 25.3%; activity type (call, SMS, data) is not distinguished (p. 2). 665 sites after merging cells by base station, Voronoi polygons for coverage (p. 4).
  - Window: match time plus two hours before and after (p. 4).
  - **Baseline.** Average activity of the same day type: weekday average for weekday matches, weekend average for weekend matches (p. 3). The description is not consistent: the Fig. 4 legend says the reference is the previous and following two days (p. 4); for the Saturday match the text says the weekday average is the reference while the Fig. 5 caption says weekends (p. 4-5).
  - **Signal to size.** Visual comparison of the match-day curve with the reference curve. For the map, a z-score per site, z = (x - μ)/σ, at 5-minute aggregation, with ad hoc categories: below -5 low, -5 to 5 average, 5 to 30 high, above 30 very high (p. 5, p. 9).
  - **Inference.** None. "Significant" is used descriptively. The reference is built from at most a handful of days in one month.
- **Main findings.**
  - Activity falls below the reference during matches, rises at half-time, and spikes right after Hungarian goals; opponents' goals produce little or nothing (p. 4-5).
  - After the Portugal match, sites along the celebration route show activity far above average at 20:20 (p. 5; Fig. 8 p. 7).
  - Context numbers: TV audiences of about 1.734, 1.976 and 2.318 million for the three group matches (p. 1); almost 10 thousand SIMs seen at the fan-zone site between 17:00 and 20:00 (p. 5).
- **Usable for our paper.**
  - Literature: a nation-wide synchronised pause in ordinary activity shows up as a dip below a same-day-type baseline, even when the triggering event is remote (p. 7-8). The siren stop is the same kind of signal (a brief city-wide dip), in speed instead of phone activity.
  - Method: again, same-day-type reference dates are the default counterfactual (p. 3).
  - Results-Discussion: "small groups usually do not stand out from the 'noise'" (p. 2) is a fair statement of why we need the whole city and several years.
- **Caveats.**
  - Preprint, descriptive, no participation or size estimate, no uncertainty. Four events in one month.
  - The baseline is loosely and inconsistently defined; do not cite it as a careful design.
  - Z thresholds of 5 and 30 come from eyeballing a histogram (p. 9); they are not tests.
- **Checks it suggests for us.**
  - Plot the Nov 10 within-day profile against the mean and spread of control-date profiles (their Figs. 4-6 style) for the paper's first figure; with hourly İBB data this is three points (08h, 09h, 10h), with the 2026 5-minute index it is a real curve.
  - Map of cell-level standardised contrasts on Nov 10 (their Fig. 8 style), with the caveat that cell-level z-scores are not independent.

### ngeni2022 - Ngeni, Mwakalonge & Siuhi (2022), The 2017 total solar eclipse in the United States: traffic management and lessons learned (Transp. Res. Interdiscip. Perspect. 13: 100510)

Text note: minus signs are lost in the text file (for example "  7%" is -7%). I checked signs against the table logic.

- **Question and setting.** How did interstate traffic volumes in the path of totality change before, during and after the 21 August 2017 eclipse (a Monday)?
- **Data and method.**
  - FHWA continuous count data from Automatic Traffic Recorder stations on interstates inside the path, July-September of 2016, 2017 and 2018; 11 states in three groups by local eclipse time (OR/ID/WY before noon; NE/KS/MO/IL around 1 pm; KY/TN/GA/SC between 1 and 2 pm) (p. 3).
  - Missing hours or days are imputed from the five preceding weeks by a weighted hour-of-day by day-of-week average (Eq. 1, p. 3).
  - **Baseline.** The same weekday in the previous five weeks. For the eclipse-day hourly analysis: five earlier Mondays, same hour (p. 4, p. 6). 2016 and 2018 are shown for visual comparison only (p. 3).
  - **Signal to size.** Percentage difference between the 2017 value and the edge of a band around the baseline mean (p. 5-6).
  - **Inference.** A band 95% CI = mean ± 1.96 · SD / sqrt(n), with n ≈ 5 (Eqs. 2-3, p. 4). "traffic changes are significant if they fall outside these interval bounds" (p. 5).
- **Main findings.**
  - Daily, OR/ID/WY combined: eclipse day +21% over the five-week mean, +14% the day before, +15% the day after (Table 1, p. 6). Wyoming had the largest swing, 68% (p. 6; Table 5 p. 8).
  - Hourly, OR/ID/WY, eclipse hours (Table 6, p. 9): at 10:00 volume was 93,227 against a band of 96,580 to 100,130; at 11:00 it was 89,070 against 104,552 to 110,230. The paper reports these as -7% and -19% relative to the upper bound and reads them as people having stopped to watch (p. 6-7). From 12:00 to 15:00 volume was 14%, 22%, 26% and 19% above the upper bound (p. 7; Table 6 p. 9).
  - Whole corridor: traffic fell below the band during the eclipse hours, by 13% measured from the upper bound, then rose 13% above the upper bound and stayed high for three hours (p. 9).
- **Usable for our paper.**
  - Literature: the nearest traffic-data precedent for "drivers stop for a scheduled event at a known clock time": an hourly dip during the event and a surge after (p. 6-7, p. 9). It uses the same counterfactual family as ours (same weekday, preceding weeks).
  - Method (contrast): their inference is a naive band from five days. Ours is randomization inference over dates. Citing this paper lets us say what the applied traffic literature usually does and why we do something stricter.
  - Robustness: they impute missing counts from the previous five weeks (p. 3); we should state what we do with missing cell-hours.
- **Caveats.**
  - **[my calculation]** The band is a confidence interval for the mean of the five baseline days, not a prediction interval for one new day. A prediction interval with n = 5 would be about mean ± 2.776 · SD · sqrt(1 + 1/5) ≈ ± 3.04 SD, against their ± 0.88 SD. Their bands are roughly 3.5 times too narrow, so "significant" is overstated throughout. Many ordinary hours fall outside the band (Table 6: almost every hour of the day does).
  - The eclipse-hour dip is confounded: volumes were far above normal all morning from inbound visitors (+28% to +155% between midnight and 08:00, Table 6 p. 9), so the dip mixes "stopped to watch" with "already arrived". It is not a clean stopping effect.
  - Percentages are measured from the band edge, not the mean, which is non-standard. **[my calculation]** Against the band midpoint the 10:00 and 11:00 values are about -5% and -17%.
  - Internal inconsistencies: the abstract says traffic declined 13% "three hours before" the eclipse (p. 1) while the text places the 13% drop during the eclipse hours (p. 9); summary point 3 swaps upper and lower bounds (p. 11). The stated baseline Mondays for the day -7 example include the day itself (8/14) (p. 4). Quote numbers from Table 6, not the abstract.
  - Volumes (counts), not speeds; interstates only (p. 11).
- **Checks it suggests for us.**
  - Do the count analogue: contrast in NUMBER_OF_VEHICLES at 09h vs 08h/10h on Nov 10 against controls. If the variable is a count of observed vehicles, a stop should change it little; if it moves, that says something about what it measures.
  - Show how many control dates fall outside a naive ± 1.96·SD/sqrt(n) band in our data, to illustrate why we use randomization inference.
  - Look for a post-event overshoot at 10h (their 12:00-15:00 surge). Our contrast uses 10h as a reference hour; if 10h is itself affected (release), the contrast is biased. Test with 08h-only and with 07h/11h references.

---

## Focus B - İBB data

Summary table of what each paper says the data are (details and pages below).

| Paper | Data set named | Period | Resolution | Units / count | How speed is measured |
|---|---|---|---|---|---|
| utku2023 | İBB hourly traffic density data set (open data URL) | Jan-May 2021 | hourly | 2,321 "points"; 8 columns | not stated |
| ozkurt2025 | İBB hourly traffic density data (open data URL) | 2022 | hourly | 8,539 records; location not stated | not stated |
| tanberk2023 | İBB Open Data Portal hourly traffic density data set (URL) | Jun 2020-May 2021 | hourly | 14,183,614 rows x 9 columns; "more than 7 thousand location points" | not stated |
| olug2024 | "IBB Traffic graph dataset" (source portal not named) | "four years" (years not given) | hourly | 2,451 "sensors"/locations | "sensors", type not stated |
| energies2021 | traffic density data "provided by IMM" | Jan-May 2020 | not stated | 1,455 sensors; passenger car units | "sensors", type not stated |
| takak2021 | speed data supplied by İBB (internal SQL database) | 2017 | 1 minute (aggregated to 15 min) | 7,000 sensors, with direction | "sensors", type not stated |
| alcan2022 | İBB traffic index (open data web service) | 2020 | hourly averages | one city-wide series, values 1-99 | not stated |

No paper in this group mentions probe vehicles, floating-car data, GPS, data providers, radar/RTMS, or how AVERAGE_SPEED is averaged.

### utku2023 - Utku (2023), Derin öğrenme tabanlı trafik yoğunluğu tahmini: İstanbul için bir vaka çalışması (Düzce Üniv. Bilim ve Teknoloji Dergisi 11: 1584-1598) [Turkish]

Text page N = journal page 1583 + N.

- **Question and setting.** One-step-ahead forecasting of hourly vehicle count and average speed at one location (Başakşehir Mahmutbey junction) with an LSTM, compared with LR, RF, SVM, MLP, CNN, RNN.
- **Data and method - exactly what it says about the İBB data.**
  - **Source.** "Saatlik trafik yoğunluğu veriseti" provided by İstanbul Büyükşehir Belediyesi, January 2021 to May 2021 (p. 5); reference [30] is `https://data.ibb.gov.tr/dataset/hourly-traffic-density-data-set`, accessed 25 May 2022 (p. 15).
  - **Columns.** Date_Time, Longitude, Latitude, Geohash, Minimum_Speed, Maximum_Speed, Average_Speed, Number_of_Vehicles (p. 5).
  - **Column meanings as given.** Date_Time is year/month/day and hour; Geohash is the location code derived from latitude and longitude; the three speed columns are the minimum, maximum and average speed values (p. 5). No units, no statement of what the average is taken over.
  - **NUMBER_OF_VEHICLES.** Interpreted as the hourly number of vehicles passing a given location: "belirli bir konumdan geçen saatlik araç sayısı" (p. 5). No source is given for this reading.
  - **Number of geohash cells.** The data set contains traffic information for 2,321 distinct points ("2321 farklı nokta") (p. 5). The paper does not say "cells" and does not state the geohash precision.
  - **Missing data.** Not discussed. The chosen location has 2,900 hourly rows for January-May 2021 (p. 5-6).
  - **How speed is measured.** Not stated for this data set. The introduction and conclusion speak in general terms about cities using sensors and cameras at junctions and about mobility data from mobile devices (p. 2, p. 12); neither passage is about the İBB data set.
  - Location choice: the point with the highest vehicle count, identified from its coordinates as Başakşehir Mahmutbey junction (p. 5).
  - From the PDF figures (p. 6): hourly vehicle counts at that point range up to roughly 1,300-1,350 (Şekil 3); hourly average speeds range from roughly 17 to 78 km/h (Şekil 4); the series ends in early May 2021.
  - Method: sliding window of 3 lags, min-max scaling, 80/20 split with 10% of training for validation, walk-forward validation (p. 7, p. 9).
- **Main findings.**
  - LSTM, vehicle count: MAE 71.1, RMSE 102.7, R² 0.897 (Table 1, p. 9).
  - LSTM, average speed: MAE 3.99, RMSE 6.23, R² 0.883 (Table 2, p. 10). Linear regression on three lags already gives R² 0.858 and MAE 4.74 (p. 10).
- **Usable for our paper.**
  - Data: a published description of the open data set's columns and of a point count (2,321 for Jan-May 2021) (p. 5).
  - Data: documents that users of the data read NUMBER_OF_VEHICLES as a throughput count (p. 5). We can cite this as the common interpretation while stating that İBB's own documentation does not establish it.
  - Robustness: one-hour-ahead prediction error at the busiest cell is about 4 km/h MAE (6 km/h RMSE) even with the best model (p. 10). This is a benchmark for hour-to-hour noise in a single cell and motivates averaging over many cells and dates.
- **Caveats.**
  - The paper does not validate its reading of NUMBER_OF_VEHICLES. **[my inference]** A maximum near 1,350 per hour at what the author calls Istanbul's busiest motorway junction (p. 6) is far below what a full count at such a junction would give, which is easier to square with a sample of vehicles than with a census. This is my reading of the figure, not a statement in the paper.
  - **[my calculation]** If the series runs from 1 January to 3 May 2021 (the last date visible in tanberk2023's screenshot of the same data set), that is 2,952 hours, so 2,900 rows would mean about 1.8% of hours missing at this cell. The paper gives no end date, so this is tentative.
  - It claims to be the first study using this data set (p. 4) but also cites Taş & Müngen (2021), who used İBB traffic data for 1 January 2020 to 1 January 2021 (p. 3).
  - One cell, five months that include COVID restrictions; nothing about events or holidays.
  - Do not cite this paper for geohash-6, for sensors, or for the averaging method. It states none of these.
- **Checks it suggests for us.**
  - Count distinct geohashes per month and per year in our 2020-2025 extract and report the range (they report 2,321 for early 2021; olug2024 reports 2,451 over four years).
  - Report the maximum hourly NUMBER_OF_VEHICLES at the busiest cells and compare with known counts (for example bridge crossings) to bound the sampling rate.

### ozkurt2025 - Özkurt, Kala, Konuk & Saylam (2025), Bulanık mantık destekli trafik yoğunluğu tahmini (Harran Üniv. Mühendislik Dergisi 10(3): 184-197) [Turkish]

Text page N = journal page 182 + N.

- **Question and setting.** A Mamdani fuzzy-logic model for "traffic density" in Istanbul using hourly İBB traffic records and daily weather, compared with regression, tree and LSTM models.
- **Data and method - exactly what it says about the İBB data.**
  - **Source.** Hourly traffic density data provided by İBB, obtained from the İBB open data portal, for 2022; 8,539 hourly records (p. 2, p. 3, p. 5). Reference [28] is the hourly traffic density data set URL, accessed 10 March 2025 (p. 15). Weather: Meteostat daily data, 365 rows (p. 5).
  - **Columns shown (Table 1, p. 5).** Tarih (timestamp), Asgari Hız (minimum speed), Azami Hız (maximum speed), Ortalama Hız (average speed), Araç Sayısı (number of vehicles). No longitude, latitude or geohash column is shown or mentioned.
  - **Sample rows (Table 1, p. 5).** 01-01-2022 00:00: min 40, max 97, mean 59, vehicles 32. 01:00: 45, 125, 79, 22. 02:00: 80, 177, 100, 9. 03:00: 110, 110, 110, 1.
  - **Column meanings as given (p. 5-6).** Minimum and maximum speed are the lowest and highest vehicle speeds recorded in that hour. Average speed "shows the general speed level of the traffic flow". Number of vehicles is the total number of vehicles passing the specified road in that hour (p. 6). Earlier on the same topic the variable is described as the total number of vehicles in traffic (p. 5). Average speed unit is km/h (p. 5).
  - **Missing data.** 8,539 records against 8,760 expected hours; the paper states "yaklaşık %2,5 oranında eksik kayıt" and says no systematic gap, outlier or meaningful deviation was found (p. 6). How the gaps were treated is not stated.
  - **Number of geohash cells.** Not stated. The paper never says which location or how many locations the 8,539 hourly records represent, or how they were obtained from the multi-location portal file.
  - **How speed is measured.** Not stated.
  - Method: inputs are vehicle count, average speed, temperature, precipitation (binary); 54 rules; centroid defuzzification (p. 8-9). Fuzzy sets for vehicle count: low 0-20, medium 20-60, high 60 and above with maximum at 100; for speed: low 0-20, medium 20-60, high 60+ km/h (p. 10). Five-fold time-ordered blocked cross-validation (p. 6).
- **Main findings.**
  - Mamdani model: MAE 5.32, RMSE 7.45, R² 0.87; LSTM 4.42 / 6.11 / 0.91; XGBoost 4.71 / 6.48 / 0.90; linear regression R² 0.47 (Table 5, p. 12).
- **Usable for our paper.**
  - Data: a second, independent report of the share of missing hours in the open data set: about 2.5% of hours in 2022, with no systematic pattern found (p. 6).
  - Data: the sample rows show two properties worth noting in our data section: maximum speeds well above legal limits (177 km/h) and hours with a single vehicle where minimum, maximum and mean coincide (p. 5). Both are consistent with the columns being statistics over individually observed vehicles.
  - Data: another instance of the "vehicles passing in that hour" reading of NUMBER_OF_VEHICLES (p. 6), again without a source.
- **Caveats.**
  - I could not find a definition of the dependent variable. "Trafik yoğunluğu" is predicted and scored (MAE 5.32 and so on) but the İBB file has no density column, and the paper does not say how the target was built or in what units the errors are. Do not cite the accuracy figures as evidence about the data.
  - With one record per hour and vehicle counts in the tens, the series is either one cell or some aggregate; the paper does not say. So it gives no information about cells.
  - The statement that average congestion in Istanbul exceeds 70% and reaches 85% at peaks (p. 2, p. 3) has no citation.
  - The two descriptions of the vehicle variable ("in traffic", p. 5; "passing the road", p. 6) are not the same thing, and neither is sourced.
  - Nothing on sensors, probes, geohash or averaging.
- **Checks it suggests for us.**
  - Report, for our extract, the share of missing cell-hours overall and specifically for the 08h, 09h, 10h hours on treated and control dates; test that missingness at 09h is not different on Nov 10.
  - Tabulate cell-hours with NUMBER_OF_VEHICLES = 1 (min = max = mean) and consider a minimum-count filter or count weights as a robustness check.
  - Flag MAXIMUM_SPEED outliers (above, say, 150 km/h) as a data-quality diagnostic.

### tanberk2023 - Tanberk & Can (2023), Smart Journey in Istanbul: a mobile application in smart cities for traffic estimation by harnessing time series (conference paper)

- **Question and setting.** A prototype mobile app that forecasts district-level traffic for the next 12 hours from İBB data plus weather, comparing LSTM, Transformer and XGBoost.
- **Data and method - what it says about the İBB data.**
  - **Source.** İBB Open Data Portal, hourly traffic density data set (ref. [17], the same URL as utku2023, accessed November 2022), June 2020 to May 2021 (p. 3, p. 6). Described as containing "Istanbul location density and traffic information hourly" (p. 3).
  - **Size.** After combining all files: 14,183,614 rows and 9 columns (p. 4). The introduction says "more than 14 million traffic data of more than 7 thousand location points" (p. 1).
  - **Columns (from the screenshot in Fig. 1, PDF p. 3).** _id, DATE_TIME, LONGITUDE, LATITUDE, GEOHASH, MINIMUM_SPEED, MAXIMUM_SPEED, AVERAGE_SPEED, NUMBER_OF_VEHICLES. The geohash strings shown have six characters (for example sxk37q, sx7cht).
  - **Values visible in the screenshots (PDF p. 3-4).** Cell-hour rows for 1 May 2021 with MINIMUM_SPEED of 1, 3, 4, 8, 10, 13, 37, 47; MAXIMUM_SPEED up to 146; NUMBER_OF_VEHICLES from 16 to 402 (Fig. 1). In the Tuzla district aggregate (Fig. 9), the minimum speed is 6 in all five rows shown for 1 June 2020 and 1 in four of the five rows shown for 3 May 2021; maximum speeds are 162 to 206 km/h.
  - **Processing.** Each row is assigned to the nearest of six manually chosen points (Tuzla, Bağcılar, Büyükçekmece, Ataşehir, Kağıthane, Fatih) by haversine distance and aggregated to district-hour (p. 4). Weather from NASA POWER, 57,048 rows (p. 3-4). One district's final series (Tuzla) has 7,891 hourly rows (p. 3).
  - A descriptive check on the first 10,000 rows of one month: morning (06-09) vs afternoon (17-20) totals of NUMBER_OF_VEHICLES are 816,233 vs 1,091,036, with AVERAGE_SPEED 59.00 vs 58.75; they conclude "the average speed is not changing while the vehicle numbers go up" (p. 3-4).
  - The all-rows hourly sum of NUMBER_OF_VEHICLES is shown in Fig. 6 (PDF p. 4): 106,448 at 2020-06-01 00:00, 193,575 at 2021-05-03 19:00, and 39 in the final hour 2021-05-03 23:00; the table has 7,895 hourly rows.
  - **NUMBER_OF_VEHICLES interpretation, missing data, speed measurement.** Not stated. The forecast target is "total number of vehicles" (p. 3).
- **Main findings.**
  - MAPE between 10% and 23% across six districts and three models; the Transformer is best in each district (10-13%) (Table I, p. 5).
- **Usable for our paper.**
  - Data: independent confirmation of the column names and that GEOHASH codes are six characters (Fig. 1, PDF p. 3). This is a figure, so cite as "as shown in" and prefer the portal itself as the primary source.
  - Data: evidence that MINIMUM_SPEED = 1 occurs in individual cell-hours in May 2021 (Fig. 1), which matches the brief's "never below 1".
  - Data: scale of the file, about 14.2 million rows for 11 months (p. 4).
- **Caveats.**
  - "More than 7 thousand location points" (p. 1) conflicts with 2,321 points in utku2023 and 2,451 in olug2024. **[my calculation]** 14,183,614 rows over 7,895 hours is about 1,800 rows per hour, which fits a few thousand cells, not seven thousand reporting every hour. The paper does not explain its figure; do not cite it for the number of cells.
  - The text says vehicle numbers rise by 20% in the afternoon (p. 3); the numbers printed give a 34% rise. **[my calculation]**
  - **[my inference]** The Tuzla screenshot suggests the lowest recorded speed may have been 6 km/h in June 2020 and 1 km/h in May 2021. Ten visible rows cannot establish this, but if the floor changed during our sample it matters for the "stopped vehicles are excluded" argument and for comparability across years.
  - **[my calculation]** 2020-06-01 to 2021-05-03 is 8,088 hours; 7,895 hourly rows implies about 2.4% of hours absent city-wide, close to ozkurt2025's 2.5% for 2022. The last hour is clearly partial (39 vehicles).
  - **[my inference]** City-wide sums of NUMBER_OF_VEHICLES in the low hundreds of thousands per hour (Fig. 6), added over all cells a vehicle passes through, look small for a city of several million vehicles; this again points to a sample. Note that 3 May 2021 fell inside a national lockdown, so the level is not typical.
  - Conference paper, normalised error metrics, no detail on train/test split.
- **Checks it suggests for us.**
  - **High priority:** tabulate the minimum of MINIMUM_SPEED by month for 2020-2025. If the floor moved (6 to 1 or otherwise), document it and check that the result does not depend on the years before the change.
  - Check for partial hours at file boundaries (month ends) and drop them.
  - Their speed-flat/volume-up observation (p. 3) suggests city-mean AVERAGE_SPEED is insensitive to volume; verify in our data, since our design relies on speed responding to a brief stop.

### olug2024 - Olug, Kaya, Tugay & Gunduz Oguducu (2024), IBB Traffic graph data: benchmarking and road traffic prediction model (arXiv:2408.01016)

- **Question and setting.** Introduces an "IBB Traffic graph dataset" for Istanbul as a benchmark and a congestion classifier (lag features + GLEE node embeddings + ExtraTrees).
- **Data and method - what it says the data are.**
  - "Sensor data collected at 2451 distinct locations" in Istanbul, over a four-year period, at one-hour intervals, covering urban roads and highways (p. 1-2). The years are not given and the İBB open data portal is not named or cited.
  - The locations are called sensors throughout, described as "strategically positioned at approximately equal intervals throughout the city" (p. 2).
  - Features per location-hour: minimum speed, maximum speed, average speed, number of passing vehicles. Added location features: continent, district, highway or not, population density (p. 2).
  - Graph: an unweighted edge joins two locations if they are adjacent; 6,667 edges, average degree about 2.7 (p. 2).
  - Congestion label: a rule on σ(s/v) against a threshold τ, where s is average speed and v the number of vehicles (Eq. 14, p. 5); τ is not reported. The speed-only rule (Eq. 13) is rejected because narrow urban streets have low average speed without congestion (p. 5).
  - Code and data repository: `https://github.com/erenolg/IBBTraffic` (p. 2).
  - **How speed is measured.** Only "sensors"; no type, technology, provider or averaging method.
- **Main findings.**
  - Best model: accuracy 0.9653, precision 0.9482, recall 0.9090, F1 0.9282, AUROC 0.9877 (p. 6; Table II p. 4).
  - Without the previous-hour and previous-week features accuracy is about 0.76-0.78 and F1 0.31-0.45; with them about 0.95 and 0.89-0.91 (Table I, p. 4). Embeddings help mainly when lag features are absent (p. 5).
- **Usable for our paper.**
  - Data: a second count of locations, 2,451 over four years (p. 1-2), and a second source that describes the four variables the same way.
  - Method: support for classifying cells by their own typical speed and not by an absolute threshold, because low speed on narrow streets is not congestion (p. 5). This backs our speed-class stratification being based on each cell's baseline.
  - Method / Robustness: the same hour one week earlier is a strong predictor of a cell's state (p. 5), which supports same-weekday controls; and adjacency structure exists (6,667 edges) if we want a spatial-correlation adjustment.
- **Caveats.**
  - **[my inference]** The 2,451 "sensors" are very likely geohash cell centroids, not physical devices: the count is close to utku2023's 2,321 points, the variables are identical to the portal's, and Fig. 1 (PDF p. 2) shows nodes on a regular lattice. The paper does not say this. Do not cite it as evidence that İBB's open data come from roadside sensors, and do not cite it for what the cells are.
  - No years, no missing-data statement, no τ, and the evaluation set appears small. The direction of the label in Eq. 14 is not explained.
  - Preprint.
- **Checks it suggests for us.**
  - Inspect the GitHub repository for their processed file: which years, how many cells per year, and whether they document the source.
  - Build a cell adjacency (shared geohash edges) and use it for a spatial-correlation robustness check (for example cluster by district, or report the effective number of independent cells).

### energies2021 - Alemdar, Kaya, Canale, Çodur & Campisi (2021), Evaluation of air quality index by spatial analysis depending on vehicle traffic during the COVID-19 outbreak in Turkey (Energies 14: 5729)

- **Question and setting.** How did traffic and air quality in Istanbul change between January-March and April-May 2020 (lockdown)? GIS mapping.
- **Data and method - what it says the data are.**
  - Traffic density data for five months (January-May 2020) "provided by IMM" (p. 6); elsewhere, the data are collected by IMM "and shared for academic studies" (p. 6). The open data portal is not mentioned.
  - "Real-time traffic density data are collected 24 h a day in the city with the help of 1455 sensors" (p. 6). Sensors were placed by the local municipality (p. 2) and sit on road networks with high mobility and dense traffic (p. 8, p. 11).
  - Vehicle data are in passenger car units; the variables are number of vehicles and average vehicle speed (p. 6).
  - Temporal resolution of the traffic data as used: not stated. Sensor type: not stated.
  - Air quality: 36 of 44 Ministry stations; PM10, SO2, CO, NO2, NOx (p. 6, p. 11).
  - Method: point-density maps for traffic, inverse-distance-weighted interpolation for pollutants (p. 7). A paired-samples t-test is reported for the pollutants only (Table 1, p. 7).
- **Main findings.**
  - Mean vehicle speed by month, January to May 2020: 57.50, 55.20, 56.90, 59.00, 58.56 km/h (p. 8). The paper summarises this as an increase of up to 7% (p. 12; abstract p. 1).
  - Pollutants fell between the two periods: PM10 21.2%, SO2 16.5%, CO 18.8%, NO2 28.6%, NOx 40.0% (Table 2, p. 9).
- **Usable for our paper.**
  - Data: the city-wide mean of İBB average speeds sits near 55-59 km/h (p. 8), a useful level for describing the data and for locating our 50-70 km/h class.
  - Data: İBB sensors are concentrated on busy road networks, so coverage is not representative of all streets (p. 8, p. 11). The same limitation should be stated for the geohash cells.
  - Results-Discussion: the largest mobility shock on record moved the monthly mean speed by only about 4-7% (p. 8, p. 12), which gives a scale for how small a one-to-two-minute stop is in an hourly mean.
- **Caveats.**
  - "1455 sensors" and "passenger car units" describe a sensor-based product. Whether this is the same product as the open hourly geohash file is not stated, and the counts differ (1,455 vs about 2,300-2,450 points). Do not use this paper to describe the geohash data.
  - No statistical test on the traffic variables; before/after monthly means with no control for season or weekday mix. The 7% is February-to-April, the largest pairwise gap. **[my calculation]** January-March mean 56.5 vs April-May mean 58.8 is about 4%.
  - Nothing about how speed is measured or averaged.
- **Checks it suggests for us.**
  - State the spatial coverage of our cells (share on motorways/arterials) and avoid claiming a city-wide driver participation rate.
  - Treat 2020 with care: lockdown-era traffic (and curfews) changes speed levels and the composition of drivers. Report results with and without 2020.

### takak2021 - Takak, Görmez, Türkmen & Güvensan (2021), Kısa, orta ve uzun vadeli trafik akış hızı tahmini ve görselleştirilme aracı (Int. J. Adv. Eng. Pure Sci. 33(4): 568-580) [Turkish]

Text page N = journal page 567 + N.

- **Question and setting.** A visual analysis and speed-forecasting tool for Istanbul built on İBB sensor speeds; forecasts up to one week ahead.
- **Data and method - what it says the data are.**
  - Speed data supplied by İBB and held in an MS SQL database: "2017 yılına ait 7000 algılayıcıdan dakikada bir kez alınan ölçümleri" (p. 2), i.e. 2017, 7,000 sensors, one measurement per minute. Each record carries sensor number, direction and time (p. 2).
  - The abstract says all speed measurements made within Istanbul province are recorded by İBB, and that the tool uses speeds from sensors at many points (p. 1).
  - One-minute data are grouped to 15 minutes for speed of processing (p. 3).
  - Sensor failures leave gaps in some hours (p. 6); missing data are named as a cause of high errors and interpolation is left to future work (p. 10-11).
  - Weather: hourly precipitation by station from the State Meteorological Service (p. 2).
  - Speed colour bands follow the "İBB navi" application: 0-20, 20-30, 30-45, 45-60, 60-75, 75+ km/h (p. 6).
  - **How speed is measured.** Only "algılayıcı/sensör" with a direction attribute. No technology (radar, loop, camera, Bluetooth), no provider, no definition of the per-minute value.
  - Forecast methods: (i) mean of the same weekday and time over the previous k weeks, V_0 = (1/k) Σ_{i=1..k} V_i (Eq. 2, p. 8); (ii) a single degree-7 polynomial over the day fitted to that mean (p. 7-8); (iii) separate polynomials by time-of-day segment (p. 8). k = 3 works best (p. 11). Tested on May and December at five high-variance locations (p. 8, p. 10).
- **Main findings.**
  - MAPE, May: 19.61 (segmented regression), 23.41 (single curve), 19.99 (previous-weeks mean); December: 28.37, 34.46, 29.38 (Tables 1-2, p. 10). Overall 23.99% MAPE and 8.52 MAE for the segmented regression (p. 10).
  - The plain mean of the previous three same weekdays is almost as good as the regressions (p. 10).
  - May is predicted better than December; error spikes fall mostly on Fridays (p. 10).
  - Against ARIMA(1,1,0), the regression approach is much better beyond about 12 hours ahead (p. 11).
- **Usable for our paper.**
  - Data: documents that İBB operates a dense fixed-sensor speed network (7,000 sensors, 1-minute, directional) (p. 2). This shows minute-level, directional data exist inside İBB even though the open file is hourly and non-directional.
  - Method: published precedent, on İBB data, for using the same weekday in the previous three weeks as the expected speed (Eq. 2, p. 8), which is our control-date logic.
  - Robustness: same-weekday prediction errors of 20-29% MAPE at volatile sites (p. 10) show how noisy single-date, single-site comparisons are; winter months are worse (p. 10). November is likely nearer December than May.
  - Robustness: sensor outages are a known feature of İBB data (p. 6, p. 10-11).
- **Caveats.**
  - This is the internal 2017 sensor database, not the open geohash data set (which starts in 2020). The paper does not link the two. Whether the open file is derived from these sensors is unknown from this paper.
  - Five locations chosen for maximum variability, so the error levels are upper-end.
  - No description of the sensing technology; do not cite it for "radar" or any other type.
- **Checks it suggests for us.**
  - Ask İBB (or check the portal metadata) whether the hourly geohash file aggregates the fixed-sensor network, and if so how sensors map to cells and how the hourly mean is formed (mean of 1-minute speeds vs mean over vehicles).
  - Compare our effect with the cross-date standard deviation of the control contrast by weekday; they find Fridays unusually hard to predict (p. 10). In our years Nov 10 fell on Tuesday (2020), Wednesday (2021), Thursday (2022), Friday (2023) and Sunday (2024), so weekday-specific noise differs by year.
  - A minute-level or 15-minute extract around 09:05 would remove hourly dilution; worth requesting.

### alcan2022 - Alcan & Kaçar (2022), Impact analysis of COVID-19 pandemic on Istanbul traffic with big data tools (Electrica 22(2): 226-236)

- **Question and setting.** Descriptive analysis of Istanbul's 2020 traffic index by hour, weekday, month and curfew status using Spark, plus classification of traffic level.
- **Data and method - what it says the data are.**
  - The 2020 Istanbul traffic index from the İBB open data portal (ref. [2], the "trafik-indeks-degeri-web-servisi" data set, p. 10). The data hold average index values at one-hour intervals (p. 2).
  - "The traffic index takes values ranging from 1 to 99"; larger means more congested; two columns, date and index value (p. 2). The authors add curfew and public-holiday indicators (p. 2).
  - How the index is computed, what it is based on, and how speed is measured: not stated.
  - Classes for prediction: 0-20 normal, 20-50 moderate, 50-100 heavy (p. 2). Features: month, day of month, weekday, hour, curfew, holiday; 70/30 split (p. 3, p. 5).
- **Main findings.**
  - Busiest hour is 18:00 on every weekday; weekend peak is 15:00 (p. 4). Friday has the highest daily mean; weekends are low (p. 4).
  - Monthly mean index: about 30 in January and February; 21 in March (31 before the first case on 11 March, 16 after); 10 in April, the lowest; 28 in September and October (p. 4-5).
  - Gradient-boosted trees (one-vs-rest) classify best; heavy traffic precision 0.82, recall 0.70 (Table IX, p. 9). Logistic regression and linear SVM never predict the heavy class (p. 5, p. 7).
- **Usable for our paper.**
  - Data: a published description of the İBB city-wide traffic index (range 1-99, higher is more congested) (p. 2), our second data source. Here it is used at hourly resolution.
  - Data / Robustness: 2020 was heavily distorted by the pandemic and curfews, with the index falling by half within March and to a third in April (p. 4). This justifies a without-2020 robustness check.
  - Method: calendar features alone (hour, weekday, month, holiday, curfew) predict the index class fairly well (p. 9), which supports within-day, same-weekday designs.
- **Caveats.**
  - No definition of the index, so it cannot be converted to speed or delay from this paper. No resolution finer than one hour is mentioned; our 5-minute index needs its own source.
  - Purely descriptive; no inference. Random 70/30 split of a time series, so the accuracy figures are optimistic.
  - The paper does not give curfew dates or hours, only that Wednesday was the single weekday with no curfew at any hour in 2020 (p. 4).
- **Checks it suggests for us.**
  - Find İBB's own definition of the index (and its sampling interval) before using the 2026 5-minute series; this paper cannot be the citation for it.
  - Check each 2020 treated and control date against the curfew calendar (10 November 2020 was a Tuesday) and drop or flag restricted dates.
  - With the hourly index for 2020-2024, run the same contrast as a city-wide check on the cell-level result: one series per date, no spatial-correlation issue.

---

## Cross-paper synthesis (what jointly matters most for our design)

1. Every Focus A study uses the same counterfactual family we do: the same clock time on comparable other days (bagrow2011 p. 7; pinter2021 p. 3; ngeni2022 p. 4, 6; takak2021 p. 8). None goes beyond it, so our design is standard on this point and stricter on inference.
2. Baseline choice drives the answer. Olexsak & Meier report that 274 Earth Hour figures rest on three kinds of baseline and call a single prior-week or prior-year comparison inadequate (p. 4-5). Widening the control pool and adding a weather-adjusted counterfactual is the direct response; report the estimate under each baseline.
3. Formal inference is absent or weak in all five event studies: a z > 1.5 threshold (bagrow), eyeballed z-bands (pinter), a mean ± 1.96·SD/sqrt(5) band that is several times too narrow (ngeni), no uncertainty at all (meier), and N = 10 OLS (botta). Randomization inference over dates is a real contribution; say so and show the naive band for contrast.
4. Converting a signal into participation needs ground truth. Only botta2015 has it (attendance). We do not, so "full-stop-equivalent minutes" should be presented as a rescaling of the speed contrast and a lower bound, not as a share of drivers who stopped.
5. Rebound is documented in the analogues: TV-pickup release after the dip (meier p. 4) and the post-eclipse surge (ngeni p. 7, 9). Our 10h reference hour may be contaminated; test alternative reference hours and look for overshoot in the 5-minute index.
6. For Focus B the main result is negative: none of the seven İBB papers states how the open hourly geohash data are produced. No paper mentions probes, GPS, providers, sensor technology or the averaging behind AVERAGE_SPEED. The "unknown averaging method" threat cannot be closed from the literature; it needs İBB's documentation or a direct query.
7. The papers disagree on what the units are: 2,321 "points" (utku), 2,451 "sensors" (olug), "more than 7 thousand location points" (tanberk), 1,455 sensors (energies2021), 7,000 one-minute sensors in 2017 (takak). Olug's and Alemdar's use of "sensor" should not be read as evidence that geohash cells are physical sensors. Geohash-6 is not stated in any text; it is only visible in tanberk2023's screenshot.
8. NUMBER_OF_VEHICLES is read as hourly vehicles passing by utku (p. 5), ozkurt (p. 6) and olug (p. 2), always without a source. Magnitudes in the papers' own figures (about 1,350 per hour at the busiest junction; single-vehicle hours; city sums near 10^5 per hour) look more like a sample than a census, but that is my inference. Describe the variable neutrally as "number of vehicles observed".
9. Data-quality facts we can cite: about 2.5% of hours missing in 2022 with no systematic pattern (ozkurt p. 6); sensor outages in İBB data (takak p. 6); implausible maximum speeds and single-vehicle cell-hours (ozkurt p. 5; tanberk Figs. 1, 9). The most important follow-up is to tabulate the MINIMUM_SPEED floor by month, since tanberk's screenshot hints it may have been 6 km/h in mid-2020 and 1 km/h by May 2021.
10. 2020 is an unusual year in both İBB sources (alcan p. 4-5; energies2021 p. 8), and single-site same-weekday predictions are noisy, more so in winter and on Fridays (takak p. 10). Report results without 2020 and leave-one-year-out, and keep dates, not cells, as the unit of inference.
