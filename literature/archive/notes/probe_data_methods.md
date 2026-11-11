> Raw research notes (2026-11-10). Works listed in `../excluded.csv` (paywalled, no copy on hand) must not be cited; the citable set is `../references.csv`.

# Measuring short-lived traffic shocks with probe / floating car data: methods and measurement issues

Scope: annotated bibliography plus methods memo for estimating the delay from the 10 November 09:05 remembrance siren stop in Istanbul (İBB hourly geohash-6 data: AVERAGE_SPEED, MINIMUM_SPEED, MAXIMUM_SPEED, NUMBER_OF_VEHICLES; validation with TomTom MOVE Traffic Stats in 15-minute slots).

Verification legend used throughout:
- **[V]** bibliographic details (authors, year, venue, pages/DOI) confirmed in this session from a publisher, RePEc, TRID, NBER or repository page.
- **[V-partial]** venue confirmed, DOI or pages not confirmed.
- **[UNVERIFIED]** cited from background knowledge; not confirmed in this session. Check before citing.

---

## Q1. Time-mean vs space-mean speed, harmonic vs arithmetic averaging, and how per-cell-hour probe averages relate to travel time and delay

### Takeaway
Travel time and delay are governed by space-mean speed (total distance / total time, equivalently the harmonic mean of per-traversal speeds over a fixed distance). An arithmetic mean of per-vehicle (or per-traversal) speeds is a time-mean-type statistic that over-weights fast vehicles and overstates speed, with the error largest at low speeds, exactly where a stop puts us. Whether İBB's AVERAGE_SPEED is "right" depends on what is averaged: an arithmetic mean of time-sampled GPS pings is an estimator of space-mean speed (Edie-type), while an arithmetic mean of per-vehicle segment speeds is not.

### Cited Findings
- **Wardrop, J. G. (1952). "Some theoretical aspects of road traffic research." *Proceedings of the Institution of Civil Engineers*, Part II, 1(3): 325–362. DOI 10.1680/ipeds.1952.11259. [V]** Classic source for the distinction between time-mean and space-mean speed (and for Wardrop's equilibrium principles). Note: DOI 10.1680/ipeds.1952.11362 is a separate correspondence piece (1(5): 767–768), not the paper. — [Structurae record](https://structurae.net/en/literature/journal-article/some-theoretical-aspects-of-road-traffic-research); [Wikipedia on Wardrop, listing both DOIs](https://en.wikipedia.org/wiki/John_Glen_Wardrop); [scanned copy](https://people.irisa.fr/Nicolas.Markey/PDF/Papers/pice1(3)-War.pdf)
  - *Design implication:* cite as the canonical origin of the TMS/SMS distinction and of the identity relating them (TMS = SMS + variance/SMS).
- **Knoop, V. L., Hoogendoorn, S. P., & van Zuylen, H. J. (2009). "Empirical differences between time mean speed and space mean speed." In *Traffic and Granular Flow '07*, Springer, pp. 351–356. DOI 10.1007/978-3-540-77074-9_36. [V]** Using individual vehicle passages on a Dutch motorway, the time-mean average overestimates mean speed relative to the space-mean speed, by up to a factor of four, with the largest errors at low speeds; this distorts derived densities, jam density and shock-wave speeds. They use van Lint's relation $v_T = \sigma_M^2 / v_M + v_M$. — [TU Delft repository](https://repository.tudelft.nl/record/uuid:4b4e33a5-06b4-4bad-90f6-79f7c9fdee01); [RePEc/IDEAS](https://ideas.repec.org/h/spr/sprchp/978-3-540-77074-9_36.html); [Springer](https://rd.springer.com/chapter/10.1007/978-3-540-77074-9_36)
  - *Design implication:* in a cell-hour containing a 1–2 min stop, speed dispersion rises sharply; if AVERAGE_SPEED is a time-mean-type arithmetic average, the stop's effect on the average is attenuated relative to its effect on travel time. This is a second reason (beyond stop filtering) for a lower-bound interpretation.
- **Rakha, H., & Zhang, W. (2005). "Estimating traffic stream space mean speed and reliability from dual- and single-loop detectors." *Transportation Research Record* 1925: 38–47. [V-partial; DOI not confirmed]** Proposes estimating space-mean speed from time-mean speed using the variance about the time-mean speed; reports 0–1% estimation error; derives relations between space/time mean speed variances and travel-time variance. — [TRID record](https://trid.trb.org/view/775960)
  - *Design implication:* İBB gives MIN and MAX but no variance. A Rakha–Zhang-type correction ($v_S \approx v_T - \sigma_T^2/v_T$) could be approximated with a range-based variance proxy (e.g. $\sigma \approx$ (MAX−MIN)/4) as a sensitivity check showing that a TMS→SMS correction would *increase* the measured treatment effect in the stop hour (dispersion rises in that hour). Label as a heuristic; the range proxy is our own construction, not from the paper.
- **TomTom Traffic Stats definitions page** explicitly states the harmonic mean is "appropriate for situations when the average of rates is needed," and route outputs include average travel time, median travel time and harmonic average speed. — [TomTom Traffic Stats definitions](https://docs.tomtom.com/traffic-stats/documentation/user-guide/how-it-works/definitions); [TomTom route analysis results](https://docs.tomtom.com/traffic-stats/documentation/user-guide/output-results/route-analysis-results)
  - *Design implication:* for the validation, use TomTom's average travel time (or harmonic average speed), not arithmetic average speed, so that the validation measure is travel-time-consistent.
- **Edie, L. C. (1963/1965). Generalized definitions of flow, density and speed over a time–space region (speed = total distance travelled / total time spent). [UNVERIFIED — exact title/venue not confirmed this session; commonly cited as Edie, "Discussion of traffic stream measurements and definitions," Proc. 2nd Int. Symp. on the Theory of Traffic Flow, 1963/1965].**
- **Hall, F. L. "Traffic stream characteristics," chapter in the FHWA *Revised Monograph on Traffic Flow Theory* (Gartner, Messer, Rathi eds., c. 1996/1997). [UNVERIFIED]**; **Daganzo, C. F. (1997). *Fundamentals of Transportation and Traffic Operations*. Pergamon. [UNVERIFIED]** Standard textbook treatments of TMS/SMS, Edie's definitions, cumulative-count (N-curve) delay accounting and shockwave analysis.

### Inferences
- **Key algebra (our derivation, consistent with Edie's definition).** If a probe reports at a fixed time interval and AVERAGE_SPEED is the arithmetic mean over all pings in a cell-hour, then for each vehicle the ping-mean of speed approximates $\frac{1}{T}\int v\,dt = L/T$, and pooling over vehicles weights each vehicle by its time in the cell. The pooled ping mean is then total distance / total time, i.e. Edie's space-mean speed — the travel-time-relevant quantity. If instead AVERAGE_SPEED is an arithmetic mean of one speed per vehicle-traversal, it is time-mean-like and biased upward, more so when dispersion is high (the stop hour). We do not know which İBB uses; the memo should state both cases.
- **Conversion formula, hourly.** If $v$ is a space-mean speed and $D = \ln v_1 - \ln v_0$ is the DiD in log speed, then a vehicle driving throughout the hour covers in 60 treated minutes the distance it would have covered in $60e^{D}$ counterfactual minutes. Lost (full-stop-equivalent) minutes are therefore

$$\Delta_{60} = 60\,(1 - e^{D}).$$

  For an exact k-minute full stop by every vehicle present all hour, measured correctly, $v_1 = v_0 (60-k)/60$ and the formula returns exactly k. So the formula undoes hourly dilution *only* if (a) the speed is space-mean, (b) the stop is recorded (not filtered), and (c) vehicles are present the whole hour. Violations of (a) and (b) both bias $\lvert D \rvert$ toward zero; violation of (c) changes the interpretation to "per vehicle-hour of driving."
- **Conversion formula, TomTom 15-minute slots.** If $D_{TT}$ is the DiD in log travel time (positive for delay), lost minutes per 15 minutes of treated driving are $15(1-e^{-D_{TT}})$. This is the same object as the hourly formula with $D_{TT} = -D$ (log travel time = −log speed for a fixed route). The memo should state the sign convention explicitly: plugging a log-*speed* D into $15(1-e^{-D})$ gives the wrong sign. If D is log speed, the 15-minute analogue is $15(1-e^{D})$.
- **Aggregation consistency across the two sources:** a full-stop-equivalent of k minutes should appear as ≈k minutes in the hourly bin and ≈k minutes summed across the 15-min slots that contain the stop and its discharge. Comparing per-bin numbers directly (hourly vs one 15-min slot) is not like-for-like.

### Gaps
- No public documentation found of how İBB computes AVERAGE_SPEED (ping mean vs traversal mean vs vehicle mean) or what NUMBER_OF_VEHICLES counts (distinct devices vs pings). Asking İBB / the data provider is the most valuable single step.
- Did not verify Edie, Hall, or Daganzo citations in this session.
- DOI for Rakha & Zhang (2005) not confirmed; check Crossref/SAGE (TRR uses the 10.3141 prefix for older papers — unverified).

---

## Q2. Bias from filtering stopped vehicles / zero-speed pings; map-matching and stop filtering; how commercial providers compute average speed and travel time

### Takeaway
Filtering stationary pings removes precisely the time spent stopped from the denominator of any distance/time speed measure, so a pure full stop becomes nearly invisible in speed aggregates; what remains measurable is deceleration, queue creep and discharge. This makes the İBB estimate a lower bound, and possibly a weak one. Commercial providers publish little on stationary-point handling; TomTom documents sample size and time sets but not the averaging/filtering, HERE recommends "path processing" to smooth out signal stops, and INRIX documents outlier tuning only.

### Cited Findings
- **TomTom Traffic Stats (MOVE).** Sample size = number of GPS devices observed on a segment in the date range and time set, with no scaling or estimation; repeat passes of one vehicle are each counted; exported as BS_HITS. Time sets are hour ranges in local time. TomTom advises excluding the last three days (incomplete probe data). Segments are created wherever a road attribute changes and have no fixed length. A "full traversal" option counts only trips crossing the entire route (reduces sample size). Passenger probes come mainly from smartphones, PNDs and some car brands; fleet probes from trucks, taxis, delivery; pedestrian data is filtered out. The page does **not** document how average speed/travel time is computed or how stationary vehicles and outliers are treated. — [TomTom definitions](https://docs.tomtom.com/traffic-stats/documentation/user-guide/how-it-works/definitions)
- **TomTom route-level outputs** include average and median travel time, harmonic average speed, 15th/85th percentile speeds, a travel time ratio relative to a base time set, Planning Time Index and 5th–95th percentile travel times; average sample size is reported per segment. The docs do not state how segment averages aggregate to a route. — [TomTom route analysis results](https://docs.tomtom.com/traffic-stats/documentation/user-guide/output-results/route-analysis-results)
- **TomTom Route Analysis API** has a minimum-sample-size threshold: if the average sample size for a route/date range/time set falls below it, the job is rejected; default limits allow up to 24 date ranges, max one year. — [TomTom Route Analysis API](https://developer.tomtom.com/traffic-stats/documentation/api/route-analysis)
- **HERE Traffic Analytics** recommends path processing to reduce the short-term effect of traffic signals and stop signs on speeds; switching it off restricts queries to raw GPS probe speed observations. — [HERE Traffic Analytics: path data](https://docs.here.com/traffic-analytics/docs/path-data)
- **INRIX** describes tuning outlier removal to separate genuinely fast vehicles from GPS artifacts and widening its ML training set to include previously filtered higher-speed probes; nothing on stationary vehicles. — [INRIX blog](https://inrix.com/blog/transparency-as-a-product-feature-introducing-inrix-speeds-updates/)
- **Japan NILIM (national institute) annual report 2016** proposes separating parked/stopped vehicles from congested traffic using section travel time: parked vehicles take much longer to traverse than vehicles slowed by a jam. — [NILIM annual report 2016](https://www.nilim.go.jp/english/annual/annual2016/pdf_file/52.pdf)
  - *Design implication:* a provider-side rule of this kind would treat a 1–2 min synchronized stop of moving traffic as congestion (kept), but a rule based on instantaneous speed (drop pings below ~1 km/h, as İBB's MINIMUM_SPEED ≥ 1 suggests) would drop the stopped pings.
- **Signalized-intersection FCD study (Atlantis Press):** most zero-speed samples occur at signal-controlled intersections, and naive speed updates with zero-speed samples give unreasonable values — a standard motivation for dropping them. — [Atlantis Press PDF](https://www.atlantis-press.com/article/8314.pdf) [bibliographic details not extracted; check authors/venue]
- **Oklahoma DOT / FHWA report:** outlier removal mainly affects travel-time reliability measures (TTI, buffer time index, planning time index), so cleaning must be handled carefully. — [ODOT highlighter](https://aem-prod.oklahoma.gov/content/dam/ok/en/odot/documents/research/highlighter-2300-fhwa-ok-17-02.pdf)
  - *Design implication:* TomTom's percentile and PTI outputs are more sensitive to provider cleaning than averages; use averages/medians as the primary validation outcome.
- **MeTS-10 (metropolitan segment speeds from FCD in 10 cities)** calls its confidence-based filtering pragmatic and says its effects deserve investigation. — [arXiv 2302.08761](https://arxiv.org/pdf/2302.08761)
- **Herrera, J. C., Work, D. B., Herring, R., Ban, X., Jacobson, Q., & Bayen, A. M. (2010). "Evaluation of traffic data obtained via GPS-enabled mobile phones: The Mobile Century field experiment." *Transportation Research Part C* 18(4): 568–583. DOI 10.1016/j.trc.2009.10.006. [V]** 100 vehicles with GPS phones on I-880; 2–3% penetration was enough for accurate traffic-flow velocity estimates. Introduced "virtual trip lines" (speed recorded at crossing points). — [Berkeley ITS](https://its.berkeley.edu/publications/evaluation-traffic-data-obtained-gps-enabled-mobile-phones-mobile-century-field); [PDF](https://lab-work.github.io/download/Herrera2010.pdf)
  - *Design implication:* supports the claim that probe penetration on Istanbul arterials at 09:00 is plausibly enough for cell-hour speeds; also, crossing-point (VTL-type) sampling records speed at fixed locations and would miss a stop that happens between crossing points.

### Inferences
- **Mechanics of the lower bound (our derivation).** With space-mean speed $\bar v = \sum d / \sum t$, a stop of length s per vehicle adds s to $\sum t$ and 0 to $\sum d$. If stopped pings are dropped, s is removed from $\sum t$ and $\bar v$ is unaffected by the stop itself. Only (i) braking/acceleration phases, (ii) slow creep above the 1 km/h threshold, and (iii) queue discharge below free-flow speed lower the average. So $\lvert D\rvert$ measures a fraction of the true delay; $60(1-e^{D})$ is then a lower bound on full-stop-equivalent minutes. If AVERAGE_SPEED is time-mean-type (Q1), the bound is looser still.
- **Signature to check in the data:** if stationary pings are filtered, NUMBER_OF_VEHICLES (if it counts pings or ping-weighted devices) should fall in the 09:00 hour relative to the counterfactual, while MINIMUM_SPEED stays near 1 km/h. A drop in ping count is itself a measure of stopped time and could be used to *correct* the bound: under fixed-interval pinging, missing pings ≈ stopped vehicle-time. If NUMBER_OF_VEHICLES counts distinct devices, it should not fall. This is a cheap test of what İBB counts.
- MINIMUM_SPEED never below 1 km/h is consistent with a ≥1 km/h filter but also with rounding/truncation or with per-vehicle-trip speeds (a vehicle-hour average is rarely < 1 km/h). The memo should list these alternative explanations.
- TomTom: if its travel time is computed from full traversal times (start–end timestamps), the stop *is* included in travel time even if stationary pings are discarded for speed. Traversal-based travel time is therefore likely closer to the true delay than ping-based speed, which is a reason to expect the TomTom-based estimate to exceed the İBB one. This is an inference; TomTom does not document it.

### Gaps
- No public documentation found for Google Maps, Yandex (relevant for Istanbul), HERE or INRIX on how stationary pings are treated in speed or travel-time products.
- No peer-reviewed study found that directly quantifies the bias from dropping zero-speed pings for a synchronized stop.
- TomTom's 15-minute time-set resolution is not stated on the definitions page (time sets are described in hours); confirm that MOVE Traffic Stats accepts 15-minute time sets for the account tier before relying on it.

---

## Q3. Economics/transport papers using probe or sensor data for causal event studies of short shocks: time aggregation and counterfactuals

### Takeaway
The causal literature uses shocks lasting hours to weeks (strikes, policy changes), with hourly or daily outcomes, and counterfactuals from the same time-of-day on non-event days (RD in date, DiD across days or untreated roads). No paper found studies a minutes-long coordinated stop. The closest template is DiD on time-of-day × day with route or road fixed effects, using high-frequency queried travel times.

### Cited Findings
- **Anderson, M. L. (2014). "Subways, strikes, and slowdowns: The impacts of public transit on traffic congestion." *American Economic Review* 104(9): 2763–2796. DOI 10.1257/aer.104.9.2763. [V]** 2003 Los Angeles transit strike (35 days); regression discontinuity in date; Caltrans PeMS freeway loop-detector data, weekday peak hours; average highway delay rises 47% when transit stops. Data are loop detectors, not probes. — [RePEc](https://econpapers.repec.org/RePEc:aea:aecrev:v:104:y:2014:i:9:p:2763-96); [NBER w18757](https://www.nber.org/papers/w18757); [Scipedia summary on PeMS](https://www.scipedia.com/public/Anderson_2014a)
  - *Design implication:* cite for RD-in-time with a flexible date function and for using peak-hour subsets; our shock is far shorter, so the analogue is RD/DiD in time-of-day within the event day vs. the same slot on comparison days.
- **Bauernschuster, S., Hener, T., & Rainer, H. (2017). "When labor disputes bring cities to a standstill: The impact of public transit strikes on traffic, accidents, air pollution, and health." *AEJ: Economic Policy* 9(1): 1–37. DOI 10.1257/pol.20150414. [V]** 71 one-day strikes in Germany's five largest cities (2002–2011); generalized DiD comparing strike days with non-strike days; strikes raise car traffic, congestion, accidents and pollution. — [RePEc](https://econpapers.repec.org/RePEc:aea:aejpol:v:9:y:2017:i:1:p:1-37); [CESifo WP 5313](https://www.cesifo.org/DocDL/cesifo1_wp5313.pdf)
  - *Design implication:* template for event-day vs. comparison-day DiD with city/hour/day-of-week fixed effects; the 10 November design (09:00 hour on 10 Nov vs. same hour on other weekdays, differenced against other hours) is a direct analogue.
- **Adler, M. W., Liberini, F., Russo, A., & van Ommeren, J. N. (2021). "The congestion relief benefit of public transit: evidence from Rome." *Journal of Economic Geography* 21(3): 397–431. [V-partial; DOI not confirmed]** Uses hourly variation in transit service disruptions during frequent, varying-intensity strikes in Rome; travel times of cars, motorcycles and buses; data from Rome's mobility agency. — [RePEc](https://econpapers.repec.org/RePEc:oup:jecgeo:v:21:y:2021:i:3:p:397-431.); [CESifo WP](https://www.cesifo.org/DocDL/cesifo1_wp7693.pdf)
  - *Design implication:* closest in time resolution (hourly treatment intensity); supports an hourly design with hour-of-day × day fixed effects.
- **Hanna, R., Kreindler, G., & Olken, B. A. (2017). "Citywide effects of high-occupancy vehicle restrictions: Evidence from 'three-in-one' in Jakarta." *Science* 357(6346): 89–93. [V-partial: Science 357, 89 (7 July 2017) confirmed; DOI not confirmed in session]** Repeated Google Maps API queries per route (every ~20 min in the working paper; press reports ~10 min after the change); travel time rose ~46% in morning and ~87% in evening peak after HOV removal (AAAS coverage; check against paper). DiD on routes × time of day, before vs. after. — [NBER w23295](https://www.nber.org/system/files/working_papers/w23295/w23295.pdf); [AAAS news](https://www.aaas.org/news/life-jakartas-fast-lane-requires-carpooling); [Supplementary materials](https://economics.mit.edu/sites/default/files/publications/aan2747_Hanna_SM.pdf)
  - *Design implication:* best precedent for using queried commercial travel times at sub-hourly resolution for causal estimates, and for reporting effects as minutes per km or percentage travel time. Supports the TomTom 15-min validation.
- **Akbar, P. A., Couture, V., Duranton, G., & Storeygard, A. (2023). "Mobility and congestion in urban India." *American Economic Review* 113(4): 1083–1111. DOI 10.1257/aer.20181662. [V]** City speed indices from 57 million simulated trips queried from a web mapping service (Google Maps) across 180 Indian cities; decomposes speed into uncongested speed and congestion; validated against actual trip data. The 2018 working paper had 154 cities / 22 million trips. — [AEA](https://www.aeaweb.org/doi/10.1257/aer.20181662); [RePEc](https://econpapers.repec.org/RePEc:aea:aecrev:v:113:y:2023:i:4:p:1083-1111); [Berkeley Haas newsroom](https://newsroom.haas.berkeley.edu/research/big-data-traffic-study-identifies-indias-fastest-and-slowest-cities-2/)
  - *Design implication:* methodological precedent for speeds as log outcomes with trip/route fixed effects and for travel-time (not speed) based indices; also for separating free-flow from congestion components, analogous to separating the stop from the baseline hour.
- **Kreindler, G. (2024). "Peak-hour road congestion pricing: Experimental evidence and equilibrium implications." *Econometrica* 92(4): 1233–1268. DOI 10.3982/ECTA18422. [V]** Bangalore field experiment measured with smartphone GPS; finds a moderate, roughly linear effect of traffic density on delay. — [Econometric Society](https://econometricsociety.org/doi/10.3982/ECTA18422); [NBER w30903](https://www.nber.org/papers/w30903)
  - *Design implication:* evidence on the density–delay relation useful for arguing how much queue discharge a 1–2 min stop should generate on arterials.
- **Yang, J., Purevjav, A.-O., & Li, S. (2020). "The marginal cost of traffic congestion and road pricing: Evidence from a natural experiment in Beijing." *AEJ: Economic Policy* 12(1): 418–453. [UNVERIFIED]** Uses road-segment speed data and Beijing's license-plate driving restriction.

### Inferences
- The common counterfactual is "same slot, other days" plus "other slots, same day" (DiD in day × time-of-day) with location fixed effects. For 10 November: treated cell-hour = 09:00–10:00 on 10 Nov; controls = 09:00 on comparison weekdays (same weekday, adjacent weeks, excluding holidays) and other hours on 10 Nov (08:00, 10:00). Event-day-specific shocks (weather, the day being a commemoration day with ceremonies and road closures) are the main threat; the 08:00 and 10:00 hours on 10 Nov act as placebos.
- Because published work uses longer shocks, there is no established convention for converting log-speed effects to minutes of a coordinated stop; our full-stop-equivalent formula needs its own justification (Q1) and should be presented as a contribution.

### Gaps
- Did not find or verify papers on Uber/ride-hailing entry, lane closures, COVID lockdowns or sporting events using INRIX/HERE probe data; these are plausibly relevant but none were confirmed in this session.
- Did not find any study of Turkey-specific probe data (İBB, Yandex, TomTom Istanbul) used for causal inference.
- Adler et al. (2021) effect sizes and exact data source (probe vs. sensor) not confirmed.

---

## Q4. Queue dynamics: propagation of a 1–2 minute full stop, queue discharge, and window choice

### Takeaway
Kinematic-wave (LWR) theory predicts that a full stop creates a backward-moving stopping shockwave while traffic is halted and, on release, a recovery wave; vehicles arriving during and after the stop keep being delayed until the queue discharges at capacity. Total delay therefore exceeds the stop length and extends beyond it in time by roughly queue/(capacity − demand). For a 1–2 minute stop at 09:05, the hourly bin contains the whole episode unless demand is near capacity; in 15-minute slots the discharge can spill into 09:15–09:30.

### Cited Findings
- **Lighthill, M. J., & Whitham, G. B. (1955). "On kinematic waves II. A theory of traffic flow on long crowded roads." *Proceedings of the Royal Society A* 229(1178): 317–345. [V-partial; DOI not confirmed in session, commonly given as 10.1098/rspa.1955.0089 — UNVERIFIED]** — [Typeset record](https://typeset.io/papers/on-kinematic-waves-ii-a-theory-of-traffic-flow-on-long-55n849bh5r)
- **Richards, P. I. (1956). "Shock waves on the highway." *Operations Research* 4(1): 42–51. DOI 10.1287/opre.4.1.42. [V]** — [Wikipedia: Traffic wave (citing INFORMS DOI)](https://en.wikipedia.org/wiki/Traffic_wave)
- **TU Delft OCW, Chapter 8 "Shock wave analysis"** treats a temporary blockade with the fundamental diagram, tracking queue-formation and clearing waves; wave speed = Δq/Δk between adjacent traffic states. — [TU Delft OCW](https://ocw.tudelft.nl/wp-content/uploads/Chapter-8.-Shock-wave-analysis.pdf); [Open Exam Prep summary](https://open-exam-prep.com/study-guides/ptoe/traffic-flow-theory/shockwave-analysis-queuing) (secondary, teaching material)
- **Empirical queue dissipation** (MPRA working paper): dissipation time roughly linear in queued vehicles; morning queues and upgrades lengthen dissipation. — [EconPapers MPRA 53161](https://econpapers.repec.org/RePEc:pra:mprapa:53161) [authors and title not extracted; check]
- **Knoop et al. (2009)** note that TMS/SMS errors distort shock-wave speed estimates. — [TU Delft repository](https://repository.tudelft.nl/record/uuid:4b4e33a5-06b4-4bad-90f6-79f7c9fdee01)

### Inferences
- **Deterministic queue arithmetic (standard textbook result, our statement; check against Daganzo 1997).** Let demand be q (veh/min) per lane and saturation/discharge flow C. A full stop of s minutes accumulates $N = q s$ vehicles. After release the queue clears in $t_c = N/(C-q) = qs/(C-q)$ minutes, and total delay is the triangle area

$$W = \tfrac{1}{2}\, s\,(s + t_c)\, q = \tfrac{1}{2}\,\frac{q\,C\,s^2}{C-q}.$$

  Example: $q/C = 0.5$, s = 2 min gives $t_c$ = 2 min, so the disruption lasts about 4 min after 09:05; at $q/C = 0.8$ it gives $t_c$ = 8 min (episode ends about 09:15). With saturation flow near 30 veh/min/lane on urban arterials, this is short relative to an hour.
- **Implications for windows.**
  - Hourly İBB: the 09:00–10:00 bin contains onset (09:05), stop, and discharge unless $q/C$ is close to 1. 08:00–09:00 is a clean pre-period (no anticipation is expected for a siren, except near ceremonies). 10:00–11:00 should show no effect and serves as a placebo; a nonzero 10:00 effect points to confounding (ceremonies, closures) rather than queue spillover.
  - TomTom 15-min: the stop sits in 09:00–09:15; discharge may spill into 09:15–09:30 near capacity. Pre-specify the cumulative effect over 09:00–09:30 (or 09:00–09:45) as the headline, with 08:45–09:00 as a pre-trend check. Summed minutes across slots are comparable to the hourly full-stop-equivalent.
  - Route travel time: a vehicle whose trip straddles 09:05 is assigned to a slot by departure (or arrival) time; a trip starting 08:55 on a 15-min route can absorb the stop but be booked in 08:45–09:00 or 09:00–09:15 depending on TomTom's rule (undocumented). Keep routes short relative to 15 min to limit this.
- **Coordinated stop vs. stop-and-go:** because all vehicles stop together (rather than a bottleneck forming from the front), the shockwave picture is closer to a city-wide red signal of length s than to a lane-drop. Signalized-intersection delay theory (uniform-delay term of Webster-type formulas) is the natural reference. [Webster (1958) not verified in this session.]

### Gaps
- No study found of a coordinated, city-wide stop of 1–2 minutes (e.g., remembrance sirens in Turkey or Israel's Yom HaZikaron / Yom HaShoah sirens) measured with traffic data. Searching Israeli siren traffic studies could be worthwhile.
- No empirical evidence found on whether drivers resume immediately at 09:06–09:07 or queue discharge on Istanbul arterials (signals, mixed traffic) is slower than textbook saturation flow.

---

## Q5. Literature on how a k-minute coordinated stop maps to measured delay in aggregated data (dilution)

### Takeaway
No paper found that treats this mapping directly. It follows from the definitions in Q1: under correctly measured space-mean speed, a k-minute stop for vehicles present all hour lowers hourly log speed by $\ln((60-k)/60)$, and $60(1-e^{D})$ recovers k exactly. Measured dilution is larger than this because of time-mean averaging, stop filtering, partial presence of vehicles in the cell, and network spillover, all of which push the estimate toward zero.

### Cited Findings
- The relevant building blocks are Edie's distance/time speed (Q1, unverified citation), the TMS/SMS gap rising with dispersion — [Knoop et al. 2009](https://repository.tudelft.nl/record/uuid:4b4e33a5-06b4-4bad-90f6-79f7c9fdee01) — and the effect of temporal sampling and interpolation on FCD measurements — [TU Delft repository: sampling rate paper, IJGI, DOI 10.3390/ijgi5010001 (reported in search snippet; not opened)](https://repository.tudelft.nl/file/File_551497d1-bb7f-40bc-9564-019f1468833b).
- TomTom's travel-time-ratio output (current time set vs base time set) gives a direct ratio that converts with the same formula. — [TomTom route analysis results](https://docs.tomtom.com/traffic-stats/documentation/user-guide/output-results/route-analysis-results)

### Inferences
- **Dilution table (our derivation, correct-measurement benchmark):**

| Full stop k (min) | Hourly $D = \ln(1-k/60)$ | 15-min slot $D = \ln(1-k/15)$ |
|---|---|---|
| 1 | −0.0168 | −0.0690 |
| 2 | −0.0339 | −0.1431 |
| 3 (stop + discharge) | −0.0513 | −0.2231 |

  Our hourly estimates can be benchmarked against these: an estimate well below $\lvert -0.017\rvert$ implies most of the stop is not recorded (filtering) or vehicles stopped for less than a minute.
- **Partial presence.** A vehicle present in the cell for $\tau < 60$ minutes contributes to the hour in proportion to its time (under ping weighting). If stopped pings are kept, the stop raises its time share; so the formula measures lost minutes per vehicle-hour of driving, which equals per-vehicle stop length only if the stop happens to everyone present. Vehicles that enter the cell after 09:07 dilute the effect. Report results as "full-stop-equivalent minutes per vehicle-hour in the 09:00 hour" rather than "minutes each driver stopped."
- **Bounds summary for the memo:**
  1. Stationary-ping filtering: biases $\lvert D\rvert$ toward 0 (main lower-bound argument).
  2. Time-mean averaging (if used): biases toward 0, and more in the high-dispersion stop hour.
  3. Partial presence and post-stop arrivals: dilute toward 0 for "per stopping driver" interpretations.
  4. Queue discharge: pushes $\lvert D\rvert$ up (true delay > stop length), partly offsetting 1–3; this is real delay caused by the siren, not bias.
  5. Composition change (vehicles that stop drop out of the ping sample, leaving disproportionately moving vehicles): toward 0.
  Net: the hourly İBB estimate is a lower bound on siren-caused delay, and TomTom traversal-based travel times are expected to give a larger number.

### Gaps
- No published paper found that formalizes dilution of short coordinated stops in hourly probe aggregates; the derivations above are ours and should be presented as such.
- Whether TomTom travel times include stationary time (traversal timestamps) is undocumented; confirming with TomTom support would turn the validation from "consistent" to "upper/lower-bound pair."
