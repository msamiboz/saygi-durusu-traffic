# 09 Traffic flow theory and probe data: reading notes

Reader group: wardrop1952, knoop2009, rakha2005, herrera2010, lighthill1955, richards1956, akbar2023, kreindler2024.

Page convention: `(p. N)` is the PDF page, the same number as the `=== page N ===` marker in `literature/txt/<key>.txt`. Where the journal page differs, the mapping is given once per paper. Formulas that the text files garble (Wardrop, Rakha) were checked against the PDF page images. Lighthill-Whitham and Richards are scans and were read entirely from the PDF images.

Two things to know before reading on:

1. **`kreindler2024.pdf` is the Econometrica Supplementary Material, not the article.** The road-technology estimates (main-text equation 6, Table III, Figure 4) are not on disk. Everything below about Kreindler comes from the supplement only.
2. **`herrera2010.pdf` is the 2009 Berkeley working paper** (UCB-ITS-VWP-2009-8, five authors), not the typeset Transportation Research C version. Page numbers refer to the working paper.

Statements marked **[our inference]** are not made by the paper.

---

### wardrop1952 - Wardrop (1952), Some theoretical aspects of road traffic research

Journal page = PDF page + 324 (PDF p. 6 is journal p. 330). The PDF has 38 pages and runs into the printed discussion.

- **Question and setting.** A methods paper from the UK Road Research Laboratory: how to define and measure mean speed, overtaking, capacity, signal delay, queue growth, route choice, and how to run "before-and-after" studies.
- **Data and method.** Mostly derivation. Illustrations: speed distribution of 450 veh/h eastbound on Western Avenue, Greenford (Table 1, p. 4); running speed against flow for Central London streets grouped by width (Fig. 3, p. 12); a random-number simulation of 2,000 arrivals at a fixed-time signal (p. 17).
- **Main findings**
  - *Definitions.* Split the stream into sub-streams i with flow q_i, speed v_i and concentration k_i = q_i / v_i (eq. 1, p. 4). Time-mean speed: `v_t = sum(q_i v_i) / Q`, a flow-weighted mean (eq. 2, p. 5). Space-mean speed: `v_s = sum(k_i v_i) / K`, a concentration-weighted mean (eq. 3, p. 5). Hence `Q = K v_s` (eq. 5), with no analogue for v_t (p. 6).
  - *Which measurement gives which mean (p. 6).* Arithmetic mean of spot speeds of vehicles passing a point (short-base timing or radar) gives the time-mean. Mean transit time over a short base, then length / mean time, gives the space-mean. Two aerial photographs a short interval apart, distance moved per vehicle, arithmetic mean, gives the space-mean. From spot speeds the space-mean is the harmonic mean `n / sum(1/v)`. From an instantaneous (aerial) sample the time-mean is `sum(v^2) / sum(v)`.
  - *The relation, confirmed.* Eq. (6), p. 6 (journal p. 330): `v_t = v_s + sigma_s^2 / v_s`, where `sigma_s^2 = sum(k_i (v_i - v_s)^2) / K` is the variance of the **space** distribution (eq. 7, p. 7). Equivalent form `v_t = v_s (1 + c_s^2)` with c_s the space coefficient of variation (eq. 8, p. 7). The proof is Appendix II, p. 32 (journal p. 356): substitute q_i = k_i v_i into eq. 2 and expand around v_s. It is an exact identity, so v_t >= v_s always, with equality only when all speeds are equal.
  - *Magnitudes.* Greenford example: time-mean 33.5 mph (sd 9.1, CV 0.27), space-mean 30.1 mph (sd 10.1, CV 0.34), and eq. 8 checks (p. 7). CV is "usually" 0.25 to 0.35, so the time-mean exceeds the space-mean by 6 to 12 per cent (p. 7; synopsis p. 1).
  - *Consistency rule.* Which mean is used may matter little in a given study, but the same one must be used throughout: "the same mean should be used throughout any investigation" (p. 7).
  - *Speed versus journey time (pp. 7-9).* Choosing between the two means is choosing between speed and journey time. Times add across road sections, speeds do not (p. 8). Journey times are right-skewed, speeds more symmetric; in Central London (about 5 controlled intersections per mile) the CV was 20 to 25 per cent lower for speeds, so about 60 per cent as many runs give the same proportional accuracy (p. 9).
  - *Running speed versus journey speed.* Running speed is the average speed while in motion; journey speed includes stops (glossary, p. 31). The London speed-flow relation is for running speed: `v_r = 31 - (q + 430) / (3 (w - 6))` mph, capped at 24 mph, valid down to 10 mph, q in veh/h, w street width in feet (p. 12).
  - *A stopped stream.* When traffic stops completely, speed is zero and so is flow (p. 11).
  - *Signal delay, uniform arrivals.* Mean delay per vehicle on a phase is approximately `(r + a)^2 / (2 c (1 - q/p))`, with r red time, a lost time, c cycle, q arrival flow, p saturation flow (eq. 14, p. 14; exact version eq. 13). With random arrivals the uniform formula holds to about 50 per cent saturation, is about 20 per cent too low at 75 per cent, and delay then rises quickly (p. 17).
  - *Queue growth behind an obstruction (p. 19, journal p. 343).* Queue length grows at `u = (q - q0) / (q0/v0 - q/v)` (eq. 19). For a complete blockage, `u = q / (k_1 - q/v)` with k_1 the stationary-queue concentration (eq. 21). Example: 18 ft stopped headway, arrivals at 15 mph and 500 veh/h, queue grows at 1.9 mph.
  - *Before-and-after studies (pp. 24-29, 36-37).* Test d / s(d) against the normal. Sample size per period `n = gamma (sigma/delta)^2`, with gamma = 21.0 for 5 per cent significance and 10 per cent risk of missing a true difference, 26.0 for 5 and 5 (Table 2, p. 27). With journey-time CV about 1:4, about 160 runs each way detect a 10 per cent change (p. 27). Cover the same hours of the same days of the week before and after, and use the same weights before and after (p. 37). Space-mean speed equals vehicle-miles / vehicle-hours (p. 29). Use speeds for sensitive statistical tests but journey times to state gains and losses (p. 29). Journey times of vehicles following each other closely are highly correlated, so such a sample is worth less than its size (p. 30).
- **Usable for our paper**
  - Method: cite eq. 6 (p. 6) and Appendix II (p. 32) for the time-mean/space-mean identity.
  - Method: `60 (1 - exp(D))` is a statement about time, so it needs a speed that equals vehicle-km / vehicle-hours (p. 29), that is, the space-mean.
  - Data: the taxonomy on p. 6 classifies probe averaging schemes. Fixed-interval pings are repeated "aerial photographs" and give a space-type distribution; one spot speed per passage gives a time-type distribution **[our inference from p. 6]**.
  - Data: if stationary pings are dropped, İBB's AVERAGE_SPEED is a running speed, not a journey speed, in Wardrop's terms (p. 31) **[our inference]**.
  - Method: test on (log) speed, report in minutes. Wardrop recommends exactly this split (pp. 9, 29).
  - Method / Robustness: same hours and same weekdays for comparison periods (p. 37) supports same-weekday control dates; the consistency rule (p. 7) supports a within-source DiD and warns against comparing İBB and TomTom levels.
  - Inference: serial correlation between neighbouring vehicles (p. 30) is an early statement of why the effective sample is not the vehicle or cell count.
  - Results-Discussion: eq. 21 (p. 19) for how fast a queue grows behind a stopped vehicle that blocks a lane.
- **Caveats**
  - The identity is derived for a stationary mixture of constant-speed streams. Wardrop does not treat a stop inside the averaging period. Applying it to an hour that contains a stop is our extension (see the derivation section).
  - The 6 to 12 per cent figure comes from 1950s British roads with CV 0.25 to 0.35. It is not a congested-traffic number.
  - Eq. 6 goes from space to time and needs sigma_s, which point measurements do not give.
  - Earlier notes say "60(1 - e^D) recovers lost minutes only under space-mean speed" and attach it to Wardrop. Wardrop supplies the identity and the vehicle-miles / vehicle-hours definition; the claim about our conversion is our own.
- **Checks or analyses it suggests for us**
  - Simulate one cell-hour with a k-minute stop under each averaging scheme (pings with zeros, pings without zeros, spot/distance-weighted, per-vehicle) and report what `60 (1 - exp(D))` returns.
  - Use `n = gamma (sigma/delta)^2` as a rough power check at the date level: with 5 treated dates, 5 per cent significance and 10 per cent miss risk, the detectable delta is about 2 sigma of the date-level contrast (sqrt(21/5) = 2.05) **[our arithmetic, equal-n normal approximation]**.

---

### knoop2009 - Knoop, Hoogendoorn and van Zuylen (2009), Empirical differences between time mean speed and space mean speed

Book pages 351-356 = PDF pp. 1-6.

- **Question and setting.** How large is the gap between the arithmetic mean of spot speeds and the space-mean speed in real loop data, and what does it do to density, jam density and shock-wave speed? Amsterdam ring road, three-lane motorway, 100 km/h limit.
- **Data and method.** Individual vehicle passages (time and speed) from dual loops, 16 June to 11 July 2005, lanes pooled (p. 3). Local mean `v_L` = arithmetic mean of passing speeds (eq. 4, p. 2). Space mean `v_M` = harmonic mean of the same speeds, valid under stationarity (eq. 5, p. 2). Aggregation windows of 10 s, 20 s, 1, 2, 5 and 15 min. Windows next to a change between congested and free flow (threshold 70 km/h) are dropped so that the stationarity assumption holds (p. 3). No directly observed space-mean speed.
- **Main findings**
  - Restates the identity `v_T = v_M + sigma_M^2 / v_M` (eq. 1, attributed to van Lint) and notes it cannot convert time-mean to space-mean because sigma_M is unknown from local measurements (p. 2).
  - Why the local mean is too high: a vehicle passes the detector within the window only if it is closer than `t_agg * v_i`, so faster vehicles are over-represented; weighting each passage by 1/v_i undoes this and yields the harmonic mean (eqs. 6-7, p. 3).
  - The gap is concentrated at low speeds and is close to nil at high speeds (Fig. 1 left, p. 4). Read off the figure: the average ratio space-mean / time-mean at about 20 km/h is roughly 0.67 (10 s windows), 0.58 (60 s) and 0.56 (900 s); at about 40 km/h roughly 0.77, 0.72 and 0.58; it is near 1 above roughly 70 to 100 km/h. Longer windows widen the gap (p. 4).
  - The "factor four" is the extreme: with 10 s windows the density computed with the local mean can differ from the space-mean-based density by up to fourfold (p. 4; abstract p. 1). The authors say this is much larger than Rakha and Zhang's results and give three reasons: larger truck-car speed differences than in the USA, pooling lanes with keep-right overtaking, and four weeks of data producing more extreme points (p. 4).
  - Fundamental-diagram fits are better with the space-mean (fit error 85 against 112 (km/h)^2 at 10 s; 37 against 40 at 900 s; Table 1, p. 5). Jam-density estimates are mostly lower with the time-mean (for example 87 against 131 veh/km/lane at 900 s), with unstable outliers (525, 249) (Table 1, pp. 5-6).
  - Observed shock-wave speed is approximately 20 km/h and matches the congested branch only when the space-mean is used; shock speed is `omega = delta q / delta rho` (eq. 8, p. 5).
- **Usable for our paper**
  - Data / Method: the direction and speed-dependence of the bias if AVERAGE_SPEED is an arithmetic mean of passage-type speeds: large below about 50 km/h, negligible in free flow (Fig. 1, p. 4).
  - Method: the sampling argument on p. 3 (a passage-based sample over-represents fast vehicles) carries over to any crossing-triggered probe report **[our inference]**.
  - Results-Discussion: a measured backward wave speed of about 20 km/h for restart and queue waves (p. 5).
- **Caveats**
  - The earlier notes' "up to 4x, worst at low speeds" is the maximum over 10 s windows on a lane-pooled motorway, stated for densities. The average overstatement at 20 km/h is roughly 1.5 to 1.8x (Fig. 1). It should not be quoted as a typical bias for hourly urban probe means.
  - The paper is about loop passages. It says nothing about GPS pings. If İBB averages fixed-interval pings, this bias does not apply at all.
  - The harmonic mean equals the space-mean only under stationarity (p. 2, p. 6), and transition windows were removed. A stop-and-release is exactly the non-stationary case. A loop records no passage while traffic is stopped, so neither mean sees the stopped time **[our inference]**.
  - Using Knoop as "a candidate explanation for the null in congested cells" is our hypothesis. The paper supports only that passage-based means overstate speed more at low speed.
- **Checks or analyses it suggests for us**
  - Test whether the treatment effect in log speed varies smoothly with baseline speed, and compare the shape with the three predictions in the derivation section.
  - If any sub-hourly or vehicle-level İBB data can be obtained, compute both arithmetic and harmonic means for one day to learn which one AVERAGE_SPEED tracks.

---

### rakha2005 - Rakha and Zhang (2005), Estimating traffic stream space mean speed and reliability from dual- and single-loop detectors

Journal pages 38-47 = PDF pp. 1-10.

- **Question and setting.** Traffic management centres store time-mean speeds; traffic models need space-mean speeds. How can the latter be estimated from the former using the variance that a detector could store?
- **Data and method.** One day of individual-vehicle dual-loop records (resolution 1/60 s) on I-880, median lane and lane 4 of a five-lane section, aggregated to 5-minute arithmetic and harmonic means and their variances (pp. 2-3). Derivation by a second-order series expansion of travel times around their mean (pp. 4-7), following Dailey's approach.
- **Main findings**
  - Wardrop's relation restated as eq. 2: `u_T = u_S + sigma_S^2 / u_S` (p. 2).
  - Proposed inverse, eq. 4: `u_S ≈ u_T - sigma_T^2 / u_T`, where sigma_T^2 is the variance of speeds about the **time**-mean within the polling interval (p. 3). The derivation's last step is eq. 17, `u_T ≈ u_S + sigma_T^2 / u_T`, obtained by setting u_S / u_T ≈ 1 and assuming small speed deviations (p. 7).
  - Variance relation, eq. 20: `sigma_S^2 = sigma_T^2 + (sigma_T^2 / u_T)^2`, so the space variance exceeds the time variance; field check slope 0.99, R^2 above 99 per cent (p. 7).
  - Accuracy: both Wardrop's formula and eq. 4 reproduce the measured 5-minute means within 0 to 1 per cent; the error grows with the speed CV but stays under 4 km/h for CVs from 0 to 50 per cent (pp. 1, 3).
  - Empirical gap between the two means: typically 1 to 5 per cent, 10 to 30 per cent in congestion (p. 3). Fig. 1a shows a peak above 35 per cent in the afternoon congestion on the median lane; Fig. 2a peaks near 15 per cent on lane 4 (pp. 2-3, read off the figures). Regression of space-mean on time-mean: 1.0135 x - 2.31 (median lane, p. 2) and 1.0051 x - 1.491 (lane 4, p. 3), both R^2 above 0.99.
  - A purely empirical linear conversion (Garber and Hoel, `u_T = 0.966 u_S + 3.541`) does not transfer: the same form fitted to I-880 gives 0.986 and 2.389 (p. 3).
  - Single-loop estimators: Hall-Persaud's volume/occupancy speed is a space-mean; Dailey's is a time-mean, `u_T = u_S (1 + sigma_T^2 / u_T^2)` (eq. 41, p. 9). They differ by exactly the Wardrop term.
  - Travel-time reliability: `sigma_t ≈ (t_bar / u_bar) sigma_S`, so CV of travel time ≈ CV of space speed (eqs. 46-47, p. 9), derived for speed CV below about 10 per cent.
- **Usable for our paper**
  - Method: eq. 4 (p. 3) is the citable formula for converting an arithmetic mean of spot speeds to a space-mean when the variance is known.
  - Data: 1 to 5 per cent in free flow against 10 to 30 per cent in congestion (p. 3) is a more defensible magnitude than Knoop's factor four for the possible level bias in a passage-type average.
  - Method: eq. 20 and eqs. 46-47 link speed dispersion to travel-time dispersion if we ever discuss reliability.
- **Caveats**
  - Eq. 4 is an approximation that assumes the two means differ by a few per cent. It is not exact like Wardrop's.
  - sigma_T is the variance of individual spot speeds within the interval. The paper offers nothing on a range-based proxy. The (MAX - MIN)/4 proxy in the earlier notes is our construction, and MAX and MIN over an hour of pings are extremes of a very large sample, so range/4 has no claim to estimate sigma.
  - The correction applies to a time-type (passage) distribution. If AVERAGE_SPEED is a mean over fixed-interval pings it is already space-type, and applying eq. 4 would correct in the wrong place.
  - Vehicles that are stopped never pass the detector, so they never enter sigma_T. Eq. 4 cannot recover stopped time. The earlier notes' expectation that a time-mean to space-mean correction "would increase the measured treatment effect" holds only if the stop widens the dispersion of the *recorded* speeds, which a stationary-ping filter largely prevents **[our inference]**.
  - One day, one freeway site, two lanes. The paper locates I-880 in Los Angeles (p. 2); it is the Bay Area freeway also used by Herrera et al.
- **Checks or analyses it suggests for us**
  - Report the eq. 4 correction only as a labelled sensitivity bound, computed separately for the treated and control hours, and show whether MAX - MIN actually moves in the 09h hour on 10 November. If it does not, say that the correction is uninformative.
  - Ask İBB whether a within-hour speed variance or percentile exists; with a variance, eq. 4 becomes usable.

---

### herrera2010 - Herrera, Work, Herring, Ban and Bayen (2009 working paper; published 2010), Mobile Century field experiment

File on disk is the working paper; PDF pp. 3-28 carry the paper's own page numbers 1-26.

- **Question and setting.** Can GPS phones in a few per cent of vehicles give traffic speeds and travel times good enough for monitoring? One freeway (I-880 near Union City, California), one day (8 February 2008).
- **Data and method.** 100 rented cars with Nokia N95 phones, 165 student drivers, looping 6 to 10 miles for 8 hours (p. 10). Two data streams: (a) each phone logged position and speed every 3 seconds, kept on the phone and analysed afterwards ("trajectory data"); (b) "virtual trip lines" (VTLs), fixed locations at which a phone sends one anonymous speed reading when it crosses (pp. 8, 12). Comparison data: 17 PeMS loop stations in the study section (flow and occupancy every 30 s, flow-weighted speed every 5 min; dual loops treated as single loops for speed, footnote p. 11; p. 15), and 4,268 individual travel times from licence-plate re-identification on video, at least 10 per cent of vehicles (p. 17). No ground-truth point speed exists; travel time is the benchmark.
- **Main findings**
  - *Two sampling schemes.* Temporal sampling: report every T seconds regardless of position. Spatial sampling: report on crossing fixed points, like loops (p. 6).
  - *Time sampling weights by time spent.* With time-interval sampling, more low-speed observations arrive during congestion, since vehicles stay longer in congested stretches and there are more of them per unit length (p. 15).
  - *Trajectory speed field uses Edie's definition*: speed in a space-time region = total distance travelled / total time spent by all vehicles in it (p. 15).
  - *VTL speeds are time-mean speeds.* VTL readings are aggregated in 5-minute periods as a "temporal mean speed" (p. 17; p. 20).
  - *Accuracy.* Travel times obtained by integrating the VTL speed field lie almost always within one standard deviation of the video mean travel time; loop-based ones are too short, meaning loops overstate speed (p. 17). Below 40 mph only 31 per cent of paired 5-minute loop and VTL speeds agree within 5 mph; above 55 mph, 70 per cent (p. 18). Loop speeds are mostly higher than VTL speeds and the gap is larger at low speed (p. 18).
  - *Penetration.* Design target 2 to 5 per cent of flow, justified by earlier studies saying no more than 5 per cent is needed (p. 11). Achieved average 2 to 3 per cent (p. 23). Fewer than 3 per cent of morning and 1 per cent of afternoon 5-minute periods at a station had no probe; 50 per cent of morning and 35 per cent of afternoon periods had at least 2 per cent penetration (p. 22). Fewer than 5 per cent of trajectories gave coverage qualitatively comparable to 17 loop stations (p. 15).
  - *Sources of probe/loop disagreement listed by the authors* (pp. 20-21): different measurement and aggregation methods, small samples, and selection of drivers (hired students; slower near the off-ramps they used).
  - *Shock waves from probe trajectories (Appendix, pp. 27-28).* An accident produced backward waves visible in the trajectories. With a triangular diagram and jam spacing 26 ft (jam density about 200 veh/mile/lane): free speed 65 mph, restart-side wave w = -15.6 mph, critical density about 40 veh/mile/lane, capacity about 2,570 veh/h/lane. Queue speeds 3 to 7 mph (average 6), implying 867 veh/h/lane and 144 veh/mile/lane in the queue; PeMS measured 850. Queue-formation shock at -3.6 mph via `u_s = (q_queue - q_front) / (k_queue - k_front)`, implying an upstream flow of 1,300 veh/h/lane against 1,100 measured.
- **Usable for our paper**
  - Data / Method: the temporal-versus-spatial sampling distinction (p. 6) and the statement that time sampling over-represents slow traffic (p. 15) are the citable basis for "a mean over fixed-interval pings is a space-mean type quantity". Edie's definition is quoted on p. 15.
  - Data: crossing-triggered reports are time-mean speeds (pp. 17, 20). A stop between trip lines generates no report **[our inference]**.
  - Data: 2 to 3 per cent penetration gave usable 5-minute speeds on a freeway carrying about 6,000 veh/h (pp. 11, 22-23). Scale argument for hourly cells: an hour pools twelve such periods.
  - Results-Discussion: observed wave speeds (-15.6 mph restart-side, -3.6 mph queue growth) and queue speed (6 mph) as real magnitudes for a stop-and-release (pp. 27-28).
  - Literature: probe data can be more accurate than loops, so loops are not ground truth (pp. 17-18).
- **Caveats**
  - The 2 to 3 per cent claim is worded as a suggestion from one day on one freeway with hired drivers. Penetration was not varied to find a threshold. Nothing in the paper concerns arterials; the earlier notes' "supports probe adequacy on arterials" goes beyond it. The authors say the urban extension was still under way (p. 23).
  - The authors attribute loop/VTL gaps to single-loop speed estimation and detector bias, not to time-mean versus space-mean averaging. Do not cite it as evidence of Wardrop bias.
  - No statement on how stationary readings are handled. The 3-second log includes whatever the GPS reports; no filter is described.
  - The appendix numbers depend on an assumed jam spacing; the authors show flows change by about ±12 per cent for 23 to 30 ft (p. 28).
- **Checks or analyses it suggests for us**
  - Establish from İBB or its vendor whether reports are time-triggered or event/distance-triggered. This single fact decides between the cases in the derivation section.
  - Use NUMBER_OF_VEHICLES as a penetration proxy: drop or down-weight cell-hours with very few vehicles, and show results are stable above a count threshold.
  - If the 5-minute city index is built from the same pings, check whether the 09:05 bin drops by something like k/5 (pings kept) or barely moves (stationary pings dropped).

---

### lighthill1955 - Lighthill and Whitham (1955), On kinematic waves II: a theory of traffic flow on long crowded roads

Scanned. Journal page = PDF page + 315 (PDF p. 2 is journal p. 317).

- **Question and setting.** A continuum theory of how changes in flow propagate along a long crowded road, applied to a moving "hump" of traffic, to bottlenecks and to stop-and-start at a controlled junction.
- **Data and method.** Theory from two premises: conservation of vehicles and a flow-concentration curve q(k) for each stretch of road. One empirical curve for a three-lane section of the Great West Road (Fig. 1, p. 8) and observed stop-start data from the Rotterdam tunnel and the Road Research Laboratory (Fig. 19, p. 29). The authors state that quantitative agreement was not yet known (p. 4).
- **Main findings**
  - *Definitions (p. 5).* Over a short slice dx and an interval tau: flow `q = n / tau` (eq. 1); concentration `k = sum(dt) / (tau dx)` (eq. 2), where dt is each vehicle's time on the slice; `v = q / k = dx / mean(dt)` (eq. 3). This is Wardrop's space-mean speed: speeds weighted by time spent on the slice. The time-mean, the unweighted mean of crossing speeds, exceeds it and is not used. From spot speeds the space-mean is the harmonic mean (eq. 4).
  - *Wave speed.* Flow changes travel at `U = delta q / delta k` (eq. 6, p. 6); small changes at `c = dq/dk` (eq. 7, p. 6); `c = v + k dv/dk < v` on a crowded road (eq. 8, p. 10). Waves never travel faster than vehicles; beyond the capacity concentration they travel backwards.
  - *Shock waves.* Where denser traffic lies ahead, waves run together into a shock whose speed is the slope of the chord joining the two states on the q-k curve (pp. 11-12). It is approximately the mean of the wave speeds either side (eq. 9, p. 13). Vehicles slow abruptly on entering a hump and speed up only gradually on leaving it (pp. 12-13).
  - *Jam geometry.* Stopped headway about 17 ft in Britain, rising about 1.2 ft per mph, consistent with a 0.8 s reaction time (p. 7).
  - *Sudden stoppage (p. 23, journal p. 338).* A stop sends a single shock back into the oncoming stream; behind it flow is zero and concentration is about k_j. Shock speed = slope of the chord from the oncoming state (k_i, q_i) to (k_j, 0), that is `-q_i / (k_j - k_i)`, which is Wardrop's eq. 21.
  - *Release (pp. 23-24).* The front vehicle is taken to leave at free speed v_F. A starting wave runs backwards through the queue at c_j, the slope of the q-k curve at jam. Between them is a fan of continuous waves, no shock. The wave that stays at the stop line carries the capacity flow q_m (also p. 8, where this is proposed as the way to measure q_m and k_m).
  - *How long the stop line runs at capacity (p. 24, journal p. 339).* With stoppage T_r and inflow q_i: `T_f = q_i T_r / (q_m - q_i)` (eq. 15). The junction can cope only if `q_i (T_r + T_g) < q_m T_g` (eq. 13).
  - *Shock path after release (p. 25).* `t = q_i T_r / (q - q_i - c (k - k_i))` with position x = c t, tracing k from 0 to k_j (eq. 17); eq. 15 is the special case c = 0.
  - *Over-saturated signals* produce an oscillating crawl whose amplitude fades with distance upstream (pp. 25-27, Fig. 17, eqs. 18-20).
  - *Stated limits when used on a small scale (pp. 27-29).* Acceleration time is ignored; it can be absorbed as a lost time of the order of 5 to 10 s per start, added to the stoppage (p. 27). Random fluctuations over times comparable with the stop are ignored (pp. 27-28). Measured stop-start traffic shows much lower concentration and higher speed at a given flow than the steady curve (Fig. 19, pp. 28-29). Part of that discrepancy is an averaging artefact: a time-average at a fixed point mixes very different states (p. 28). Drivers anticipate, which diffuses shocks; an inertia-plus-diffusion extension is sketched (eq. 21, p. 29).
  - *Scope.* The theory is for long, "crowded" roads, meaning concentration high enough that more vehicles lower mean speed; below that (up to about 50 veh/mile on the wide road of Fig. 1) speed is flat and c = v (pp. 9-10).
- **Usable for our paper**
  - Method: eqs. 1-3 (p. 5) define the speed that equals distance over time and justify calling it the space-mean.
  - Results-Discussion: eq. 15 (p. 24) gives the after-stop capacity-discharge time for a *point* stoppage: 2 minutes at q_i / q_m = 0.8 gives 8 minutes, the figure already in our review; 0.9 gives 18 minutes.
  - Results-Discussion: the lost time of 5 to 10 s per start (p. 27) is the citable size of the restart transient.
  - Data / Discussion: the remark that fixed-point time-averages during stop-start mix states (p. 28) supports the "hourly dilution" caveat.
  - Literature: origin of the kinematic-wave model, with Richards.
- **Caveats**
  - The stoppage analysed is at a fixed point with traffic still arriving. A siren that stops every vehicle where it is at the same moment is a different initial condition. In this theory a spatially uniform pause leaves the concentration profile unchanged, so no shock forms and nothing remains to discharge **[our inference; the paper does not treat this case]**.
  - Eq. 15 therefore gives an upper-end scenario that applies only where some location acts as a stop line while upstream traffic keeps coming (partial compliance, or stopped vehicles blocking lanes).
  - The paper has no measurement of probe or hourly speeds, and the authors themselves flag weak quantitative accuracy for short stop-start events.
  - Our earlier note marked the DOI unverified; `references.csv` now lists 10.1098/rspa.1955.0089, which matches the DOI printed on the PDF cover page (p. 1).
- **Checks or analyses it suggests for us**
  - Test the 10h hour for a rebound or residual slowdown. From eq. 15 a 2-minute point stop still has the stop line at capacity after 53 minutes only if q_i / q_m exceeds about 0.964 **[our arithmetic]**, so spill-over into the 10h control hour should be confined to near-capacity cells.
  - Look in the 5-minute index for an asymmetric profile: sharp fall at 09:05, gradual recovery (pp. 12-13).

---

### richards1956 - Richards (1956), Shock waves on the highway

Scanned. Journal page = PDF page + 40 (PDF p. 2 is journal p. 42).

- **Question and setting.** The same continuum idea as Lighthill-Whitham, derived independently with a linear speed-density law, giving closed-form results for a stream that is stopped at a point and released, and for a traffic light.
- **Data and method.** Pure theory. Two assumptions: traffic is a continuous density D(x, t), and speed depends only on local density, `V = a (b - D)` (eq. 1, p. 3). With fractional density d = D / D_max and maximum speed c: `V = c (1 - d)` (eq. 4, p. 3). The author says the theory needs many vehicles and cannot give precise results for very light traffic (pp. 2-3).
- **Main findings**
  - Conservation: `∂d/∂t + c (1 - 2d) ∂d/∂x = 0` (p. 4). Points of constant density d_0 move at `(1 - 2 d_0) c` (p. 4): forwards below half the jam density, backwards above it.
  - Shock speed between densities d_1 and d_2: `U = c (1 - d_1 - d_2)` (eqs. 8-9, p. 5). Shocks form wherever density increases in the direction of travel (p. 6).
  - Flow: `F = c D_max d (1 - d)` (eq. 10, p. 7); capacity is at d = 1/2 and equals c D_max / 4.
  - *Stop at a point for a time theta, initial density a (pp. 7-9).*
    - While stopped, a jam (d = 1) grows backwards at `U = -a c` (p. 7).
    - On release a starting wave runs back at `-c` and catches the stopping shock after `t_0 = a theta / (1 - a)` (eq. 11, p. 8). The jam then has its greatest length, c t_0.
    - After that the shock position L behind the stop point is `L = 2c [ (a - 1/2) t + sqrt(a theta t (1 - a)) ]` (eq. 14, p. 9), and the peak density at the shock is `a + sqrt(theta a (1 - a) / t)` (eq. 15, p. 9).
    - Density at the stop point is 1/2 (capacity flow) for all t > 0 until the shock returns (p. 9).
    - If a < 1/2 the shock returns to the stop point at `t_r = theta a (1 - a) / (1/2 - a)^2` (eq. 16, p. 9). Example given: a = 3/8 (speed 5/8 of maximum) gives t_r = 15 theta, so a 5-minute halt takes 75 minutes to clear (p. 9).
    - If a >= 1/2 the shock never returns; it weakens, falling below a 10 per cent speed change after about `100 theta a / (1 - a)` (p. 9).
  - *Traffic light* with red theta in cycle T: the queue clears each cycle only if `a <= (1/2)(1 - sqrt(theta / T))` (eq. 17, p. 10). Above that, throughput is capped at `(1/4) D_max c (T - theta) / T` (eq. 18, p. 10) and density jumps to an average of `(1/2)(1 + sqrt(theta / T))`. With equal red and green the threshold is about 1/7 and the backed-up density about 6/7, a sixfold cut in speed (p. 11).
- **Usable for our paper**
  - Results-Discussion: closed-form amplification of a point stop. Eq. 16 (p. 9) and Lighthill-Whitham's eq. 15 are the same result under the linear law, since q_i / q_m = 4a(1 - a) and 1 - q_i / q_m = 4 (1/2 - a)^2 **[our algebra]**.
  - Results-Discussion: the threshold behaviour (eq. 17) is a compact way to say that an interruption is harmless in light traffic and persistent in heavy traffic.
  - Literature: the "R" in LWR.
- **Caveats**
  - Same scope limit as Lighthill-Whitham: the stop is at one point with continuing arrivals. It is not a model of everyone stopping in place.
  - The linear law makes the starting wave travel at the full free speed c. Measured restart waves are far slower (about 20 km/h in Knoop p. 5; 15.6 mph in Herrera p. 28). The formulas in terms of q_i / q_m are safer than those in terms of c.
  - No acceleration limits, no random arrivals, no data. Not a source for any empirical magnitude.
  - The earlier notes cite Richards as "same (the LWR model)". That is fair, but the paper adds the explicit clearing-time formula, and that formula is what our "8 minutes at q/C = 0.8" claim actually rests on.
- **Checks or analyses it suggests for us**
  - Heterogeneity by baseline load: under a point-stop mechanism, delay per affected vehicle rises with a(1 - a) / (1/2 - a)^2, so the effect should rise steeply towards capacity. Our pilot shows the opposite (no effect in congested cells), which is evidence against queue amplification being what we measure, or evidence of the measurement limits in the derivation section.

---

### akbar2023 - Akbar, Couture, Duranton and Storeygard (2023), Mobility and congestion in urban India

File on disk is the accepted manuscript; PDF p. 2 carries the manuscript's page 1. Published pages 1083-1111.

- **Question and setting.** How fast is motor travel in 180 Indian cities, and how much of the variation is slow roads rather than congestion?
- **Data and method.** 57,103,181 simulated trip instances queried from Google Maps between 5 June and 13 November 2019, for 2,730,969 trips (pp. 2, 9). Each instance returns route length, duration under current traffic and duration with no traffic (p. 9). About 21 instances per trip spread over times of day, plus repeats at the same time on other days (p. 8). Trip speed is length / duration for the whole trip. City indices are city fixed effects from `log S_i = X_i' beta + s_c + e_i`, with log trip length, log distance to centre, 30-minute time-of-day indicators, day indicators, trip type and weather (eq. 2, p. 14; pp. 17-18). Validation with 90,894 real weekday trips in 89 cities recorded each second by a commissioned app (p. 12).
- **Main findings**
  - *Mean speed two ways.* A city mean `sum(D_i) / sum(T_i)` is length-weighted (eq. 1, p. 14). It ranks cities differently from the regression index (rank correlation 0.68), because trip length strongly predicts speed and varies across cities (p. 22, footnote 18). Elasticity of speed to trip length: 0.22 (p. 19).
  - *Exact decomposition.* Congestion factor = log duration - log no-traffic duration = log uncongested speed - log speed, so speed index = uncongested index - congestion factor (eq. 3, p. 16).
  - *Levels.* Mean trip speed 23.6 km/h (sd 6.9); trips take about 14 per cent longer than without traffic (Table 1, pp. 9-10).
  - *Time of day and week.* Fastest to slowest half-hour differs by slightly more than 25 per cent across all cities, more than 35 per cent in the largest decile, and about a factor of two in central Mumbai (pp. 20-21). Weekdays differ little; Sundays are about 4.5 per cent faster (p. 19). Adverse weather lowers speed modestly (p. 19).
  - *Variance.* Uncongested speed accounts for 70 per cent of the variance of the speed index and the congestion factor for 13 per cent; at 6-8 pm, 57 and 26 per cent (Table 4, p. 23).
  - *Day-to-day noise.* At peak times the 90th percentile trip duration across weekdays is on average 6 per cent above the median; 4 to 8 per cent in over 80 per cent of cities, 8 per cent in the top population decile (p. 22).
  - *Is the source real-time?* In the average city 97 per cent of peak-time trips show different durations on different days within a 5-minute time-of-day window; the minimum over cities is 78 per cent (p. 11).
  - *Events show up.* Most public holidays shift speed significantly: about two thirds are faster, by 0.5 to 4.5 per cent; about a quarter are slower, half of those during Ganesh Chaturthi processions. Strikes mostly slow traffic (pp. 11-12; details in their Appendix B, not on disk).
  - *Validation.* Night-versus-peak speed gap in large cities: 29.4 per cent in the simulated sample, 28.0 in the real trips, 31.7 in Google replications of those trips (p. 12).
  - *Aggregation pitfall.* Uber Movement averages travel times of trips passing through zones, which under-samples slow trip starts and ends and overstates speed (p. 13).
- **Usable for our paper**
  - Literature / Method: precedent for log speed as the outcome with time-of-day and day indicators, and for expressing congestion as a log difference from a reference speed (eq. 3, p. 16). Our within-day contrast has the same form with adjacent hours as the reference.
  - Data: phone-derived speeds register holidays, festivals and strikes at the 0.5 to 4.5 per cent scale (pp. 11-12). Our pilot effect in log speed (about -0.012) is in that range, so it is not implausibly small for this kind of data.
  - Inference: day-to-day variation of about 6 per cent at the 90th percentile for the same trip and time (p. 22) is a benchmark for date-level noise, and a reason the effective sample is dates.
  - Data: composition matters. Averages over segments or locations are not averages over trips (p. 13; p. 22 footnote 18). A cell-hour mean is a location average.
  - Robustness: weekday differences are small, Sundays differ (p. 19), supporting same-weekday controls when 10 November falls on a weekend.
- **Caveats**
  - The paper does **not** estimate a speed-density or travel time-volume relation. It has no volume or density data and says its cross-city data cannot identify congestion crowd-out (p. 24). For that relation it points to Kreindler and to Akbar and Duranton (p. 24, footnote 21).
  - The data are routing-engine predictions for hypothetical trips, not probe pings, and the engine's averaging and filtering are undisclosed. The authors guess it may use a high percentile of observed block speeds to separate motor vehicles from others (p. 32); that is their speculation.
  - The claim that one phone per block suffices to detect slowed traffic is an argument (p. 11), not a test.
  - The holiday and strike estimates are daily, not minutes-long; no result concerns a synchronized stop.
- **Checks or analyses it suggests for us**
  - Report the date-level standard deviation of our within-day contrast on control dates next to the 6 per cent benchmark.
  - Check whether NUMBER_OF_VEHICLES-weighted and unweighted cell averages give the same answer, as a composition check in the spirit of footnote 18.
  - Add weather controls or a weather-residualised contrast, since they find a modest weather effect.

---

### kreindler2024 - Kreindler (2024), Supplement to "Peak-hour road congestion pricing" (Bangalore)

**Only the 26-page Supplementary Material is on disk.** Notes are limited to what the supplement states.

- **Question and setting.** The article estimates commuters' value of time and schedule flexibility from a congestion-charge experiment in Bangalore and combines them with an estimated road technology to simulate optimal peak pricing. The supplement gives identification proofs, estimation details, robustness figures and tables.
- **Data and method (as described in the supplement).** 497 experimental commuters tracked by smartphone GPS, 51,424 trips; median trip 24.5 minutes and 5.93 km (Table SM.I, p. 18). Travel delay from Google Maps and from GPS trips, related to hourly traffic density or volume built from the GPS trips (Figs. SM6-SM8, pp. 13-15). Policy simulations on a 5-minute departure grid from 5 am to 2 pm (p. 9).
- **Main findings (supplement only)**
  - *Functional form.* Instantaneous travel delay is modelled as linear in normalised density: `x(h) = lambda_0 + lambda_1 d(h) / N`, described as following main-text equation 6 (p. 8). A power version with exponent nu is used for robustness (Fig. SM9 notes, p. 16), and a power fit is used in the per-date graphs (Fig. SM7, p. 14). In the stylised identification model, travel time is `lambda_0 + lambda_1 log V(h)` with V a kernel-smoothed volume (eq. S1, p. 5); this is for tractability, not the estimated technology.
  - *Scale invariance.* Because the relation depends on normalised density, the effect of one extra trip on total travel time does not depend on the true traffic volume or on the sample size used to build density (Proposition 5, pp. 8-9).
  - *How GPS-trip delay is measured.* Weekday trips longer than 2 km, **without stops along the way**, and with a diameter-to-length ratio above 0.6; average delay over trips starting in each hour-day (Fig. SM6 notes, p. 13).
  - *Stability.* The density-delay relation is re-plotted by calendar date for dates with at least 571 GPS trips (Fig. SM7, p. 14) and for 46 major arteries using 268,292 trip segments, excluding trips that touch an artery for less than 200 m, with Newey-West errors at a 3-hour lag (Fig. SM8, p. 15).
  - *Comparison.* The log-log estimates are plotted against Akbar and Duranton's for Bogotá (Fig. SM6 panel D, p. 13). The supplement gives no numbers for either.
  - *GPS data quality.* The share of days with good-quality GPS data is 0.41 before the experiment (Table SM.IV, p. 21) and 0.76 in the control group during it (Table SM.V, p. 22), unaffected by treatment.
- **Usable for our paper**
  - Literature / Method: travel time per distance ("delay") is the natural additive outcome, modelled as linear in density (p. 8). A stop adds minutes to travel time directly, which is why we convert log-speed effects to minutes.
  - Data: an explicit precedent for removing trips with stops when building a GPS speed measure (p. 13). It shows that stop filtering is routine in probe-based measures, and it is precisely what would hide a siren stop.
  - Inference: hourly traffic series treated as serially correlated over several hours (3-hour Newey-West lag, p. 15).
  - Data: the invariance result (pp. 8-9) says a relation in normalised density can be learned from a small probe sample, relevant to using NUMBER_OF_VEHICLES as a relative, not absolute, density measure **[our inference]**.
- **Caveats**
  - The earlier notes' sentence that the paper "finds a moderate, roughly linear effect of traffic density on delay" cannot be confirmed from this file. The supplement confirms the linear specification, not the size or the fit. Akbar et al. describe the same result as linear in speed against vehicles on the road (akbar2023 p. 24, footnote 21), which is not the same statement as linear in delay. Read the main article before citing a magnitude or the word "linear".
  - The units of "delay" are not restated in the supplement.
  - The relation is an equilibrium, hour-level technology. It is not a model of queue discharge after a short stop, and using it "for arguing how much queue discharge a short stop generates" (review table) asks more of it than it offers.
  - Median trip speed implied by Table SM.I is about 14.5 km/h (5.93 km in 24.5 minutes, our division of two medians), so the setting is far more congested than our 50-70 km/h cells.
- **Checks or analyses it suggests for us**
  - Obtain the main article (NBER WP 30903 or Econometrica 92(4)) and verify equation 6, Table III and Figure 4 before the paper cites the density-delay relation.
  - Consider reporting the effect also in delay units, `1/v` in minutes per km, where a k-minute stop is additive.

---

## Derivation support: a k-minute stop in an hourly probe mean

Everything in this section is **our derivation**. The papers supply the definitions and constants named in brackets; none of them treats a synchronized stop.

**Set-up.** One cell, one hour (60 minutes). Without the siren every vehicle moves at v_0. With it, each vehicle brakes linearly for t_d, stands for s, and accelerates linearly for t_a. Distance lost per vehicle is v_0 k*, with

`k* = s + (t_d + t_a) / 2`   (true full-stop-equivalent minutes).

A share pi of vehicles complies. The number of vehicles in the cell at any instant is unchanged by a simultaneous stop, because nobody enters or leaves while everyone stands.

| Averaging scheme behind AVERAGE_SPEED | Hourly mean | `60 (1 - exp(D))` returns | Paper basis |
|---|---|---|---|
| A. Fixed-interval pings, all kept | v_0 (1 - pi k*/60) | pi k*, exact | Wardrop p. 6 (aerial method), p. 29; L-W eqs. 1-3 p. 5; Herrera p. 15 |
| B. Fixed-interval pings, stationary ones dropped | v_0 (60 - pi k*) / (60 - pi s) | about pi (t_d + t_a)/2: braking and restart only; s disappears | Wardrop running speed p. 31; L-W lost time p. 27 |
| C. Distance- or crossing-triggered reports (spot speeds) | mean weighted by distance, `sum(v^2)/sum(v)` | about pi (t_d + t_a)/6; s disappears | Wardrop p. 6, eq. 6; Knoop p. 3; Herrera pp. 6, 17 |
| D. One speed per vehicle traversal, arithmetic mean over vehicles | v_0 [1 - (tau/60) pi k*/(tau + k*)] | pi tau k* / (tau + k*), below both tau and k* | Wardrop eq. 2; Akbar p. 22 fn. 18 |
| D'. One travel time per traversal, distance / total time | v_0 (1 - pi k*/60) | pi k* | Wardrop p. 29 |

tau is the free traversal time of the cell (a geohash-6 cell is roughly 0.6 to 1 km across at Istanbul's latitude, so about 0.6 to 1 minute at 60 km/h; our approximation).

**Checks on the table.**

- *Scheme A needs no "present all hour" condition.* Ping counts are proportional to vehicle-time in the cell, so the ping mean is total distance / total time for the cell (Edie's definition as quoted by Herrera p. 15). With mixed speeds replace v_0 by the space-mean v_s.
- *Scheme C through Wardrop's identity.* Over the hour the space distribution has mass p = s/60 at zero and 1 - p at v_0. Then v_s = v_0 (1 - p) and sigma_s^2 = v_0^2 p (1 - p), so eq. 6 gives v_t = v_s + sigma_s^2 / v_s = v_0. A flow-weighted mean is exactly blind to a full stop. This is the sharpest form of "time-mean overstates": the extra variance created by the stop offsets the fall in the space-mean one for one.
- *Why the time-mean/space-mean bias does not difference out.* ln v_t = ln v_s + ln(1 + c_s^2) (Wardrop eq. 8). A DiD in ln v_t equals the DiD in ln v_s plus the DiD in ln(1 + c_s^2), and the stop raises c_s^2 in the treated hour only.
- *Rakha-Zhang cannot repair B or C.* Their sigma_T is computed from recorded speeds; stopped time is not recorded, so the correction term does not grow with s.

**Size of the transient term.** With constant braking rate b and acceleration a, t_d + t_a = v_0 (1/b + 1/a), so under scheme B the measured effect is proportional to baseline speed. Lighthill-Whitham's lost time of 5 to 10 s per start (p. 27) is the restart half; if braking loses a similar amount (our assumption), scheme B returns roughly 0.15 to 0.35 minutes at full compliance, whatever s is.

**Reading the pilot against the table (illustrative arithmetic, not a result).**

- Under A, 0.73 minutes in 50-70 km/h cells means pi k* = 0.73: with k* between 1 and 2 minutes, a compliance-equivalent of 37 to 73 per cent.
- Under B, 0.73 minutes exceeds the 0.15 to 0.35 predicted from ordinary braking and restart. Either stationary pings are only partly removed, or the transient is several times longer than a single vehicle's (staggered stopping, slow restart in platoons), or the scheme is not B.
- Under D, tau k*/(tau + k*) with tau of 0.6 to 1 minute and k* of 1 to 2 minutes gives 0.4 to 0.7 minutes, close to the pilot level.
- The gradient across speed classes discriminates. A predicts the same minutes in every class (for equal compliance). B predicts minutes proportional to v_0: the ratio for 60 against 40 km/h is 1.5, and the pilot ratio is 0.73/0.45 = 1.6. D predicts more minutes in slower cells (larger tau), the opposite of the pilot.
- So the pilot's level looks like A-with-partial-compliance or D, and its gradient looks like B. This is unresolved, and it is the main reason to pin down İBB's method.

**Queueing after the stop.**

- *Universal simultaneous stop.* The density profile is frozen and released; kinematic-wave theory then predicts no shock and no discharge period. After-effects come only from restart lost time and, in dense platoons, from the restart wave moving back at roughly 20 to 25 km/h (Knoop p. 5; Herrera p. 28; L-W p. 23), which delays the last vehicle of a platoon of length l by l divided by that speed.
- *Point stop with continuing arrivals* (partial compliance, a stopped vehicle blocking a lane, a stop line): queue grows at `q / (k_j - q/v)` (Wardrop eq. 21; L-W p. 23); after release the stop point runs at capacity for `T_f = q k / (q_m - q)` (L-W eq. 15; Richards eq. 16). Total delay is `(1/2) q k^2 / (1 - q/q_m)` and the mean delay per affected vehicle is k/2 (consistent with Wardrop eq. 14 for one red phase; our algebra). Example with k = 2: T_f is 8 minutes at q/q_m = 0.8, 18 at 0.9, and reaches into the 10h hour only above about 0.96.
- *Overlap with stops that would have happened anyway.* In signalised or congested cells vehicles are already stationary for part of each cycle (Wardrop eqs. 13-14). A siren stop that coincides with a red phase adds less than k, and under scheme B the baseline already excludes that standing time. The null in congested cells is therefore consistent with a measurement limit, with overlap, and with low baseline speed under B; the data in hand cannot separate them.

**Diagnostics that separate the schemes.**

1. NUMBER_OF_VEHICLES in the 09h hour on 10 November against controls: under B with ping counts it falls by about pi s/60 (1.7 to 3.3 per cent for 1 to 2 minutes at full compliance); if it counts devices, or under A, it does not move.
2. Effect against baseline speed within and across classes: flat in minutes (A), proportional to speed (B), decreasing in speed (D).
3. MINIMUM_SPEED: under A with raw pings it would be 0 in nearly every urban cell-hour. A floor of 1 km/h in all hours rules out A-with-raw-zeros unless the field is floored or computed per vehicle.
4. The 5-minute index at 09:05-09:10: a fall of order k/5 (20 to 40 per cent) under A, a small fall under B or C.
5. MAX - MIN in the treated hour: unchanged under B, which would make the Rakha-Zhang range proxy uninformative.

---

## Cross-paper synthesis

1. Wardrop's identity is confirmed: `v_t = v_s + sigma_s^2 / v_s`, eq. 6 on PDF p. 6 (journal p. 330), proved in Appendix II (PDF p. 32); sigma_s is the variance of the space distribution, and the identity is exact.
2. Minutes lost are a travel-time quantity, so `60 (1 - exp(D))` is valid only for a speed equal to vehicle-distance over vehicle-time (Wardrop p. 29; Lighthill-Whitham p. 5; Edie via Herrera p. 15).
3. A mean over fixed-interval pings with stationary pings kept is that quantity and returns the stop exactly; time sampling weights by time spent (Herrera p. 15).
4. Dropping stationary pings turns it into Wardrop's running speed (p. 31): the standing time vanishes and only braking and restart remain, of the order of the 5 to 10 s lost time per start (Lighthill-Whitham p. 27), scaling with baseline speed.
5. A passage- or distance-weighted mean is blind to a full stop: Wardrop's own identity returns v_0, because the stop's added variance offsets the fall in the space-mean. Rakha-Zhang's correction (`v_s ≈ v_t - sigma_T^2 / v_t`, p. 3) cannot recover it, since stopped vehicles never enter sigma_T.
6. Empirical time-mean/space-mean gaps are 6 to 12 per cent (Wardrop p. 7), 1 to 5 per cent in free flow and 10 to 30 per cent in congestion (Rakha p. 3), and on average 1.5 to 1.8x near 20 km/h on a lane-pooled motorway (Knoop Fig. 1, p. 4). Knoop's factor four is an extreme for 10 s windows and should not be cited as typical.
7. Kinematic-wave results (L-W eq. 15, p. 24; Richards eq. 16, p. 9; Wardrop eq. 21, p. 19) describe a stop at a point with continuing arrivals. A stop by everyone at once creates no shock in that theory, so the "8 minutes of discharge at q/C = 0.8" is an upper-end scenario tied to partial compliance or blocking, not a baseline prediction.
8. Probe adequacy: 2 to 3 per cent penetration gave usable 5-minute freeway speeds in one experiment (Herrera pp. 22-23); this says nothing about arterials, and loops are not ground truth (pp. 17-18).
9. Economics precedents use log speed or delay from routing or GPS data with time-of-day and day controls (Akbar eq. 2-3; Kreindler supplement p. 8), detect day-level events of 0.5 to 4.5 per cent (Akbar pp. 11-12), and filter out trips with stops (Kreindler p. 13). Akbar has no speed-density model, and Kreindler's main article is not on disk.
10. Most important for our design: the mapping from a k-minute stop to hourly log speed ranges from exact (pings kept) to near zero (stationary pings dropped or passage-weighted), so the İBB averaging rule must be established or bracketed with the five diagnostics above before the minutes are interpreted.
