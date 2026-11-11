> Raw research notes (2026-11-10). Works listed in `../excluded.csv` (paywalled, no copy on hand) must not be cited; the citable set is `../references.csv`.

# Measuring synchronized collective acts and rituals with passive big data (annotated bibliography for the 10 November 09:05 siren traffic paper)

Verification legend used throughout:
- **[V]** = bibliographic details (authors, year, venue, DOI/URL) confirmed this session on a publisher, repository, RePEc or library page.
- **[V-partial]** = some details confirmed (e.g., venue/DOI) but not all (e.g., full author list, pages).
- **[U]** = NOT verified this session; do not cite without checking.

A correction to the brief: the Earth Hour paper by Olexsak and Meier is in **Energy Research & Social Science**, not *Energy Policy*. I found no Earth Hour paper in *Energy Policy*.

## Q1. Electricity as a sensor of synchronized behaviour: TV pickup, Earth Hour, moments of silence, prayer/iftar

### Takeaway
Electricity grids are the oldest "passive sensor" of synchronized collective acts. There are two kinds of signal: positive spikes (TV pickup, when many kettles go on at once at the end of a programme or at half-time) and negative dips (Earth Hour; national two-minute silences). The closest analogue to our siren is the **grid dip during a national moment of silence**: Armistice Day in the UK (about 620 MW in 2010), Queen Elizabeth II's funeral (about 500 MW extra drop during the two-minute silence), and Ontario's Remembrance Day (about 235 MW). These figures, though, come from grid-operator press statements, not peer-reviewed counterfactual analyses. The peer-reviewed Earth Hour literature shows how fragile such estimates are to the choice of baseline.

### Cited Findings
**Earth Hour**
- **[V] Meier, A.K. & Olexsak, S.J. (2014). "The electricity impacts of Earth Hour: An international comparative analysis of energy-saving behavior." *Energy Research & Social Science* 2, 159–182. DOI 10.1016/j.erss.2014.04.014.** Sources disagree on author order: the LBL record lists Meier first, while the journal PDF and search summaries list Olexsak first. The volume and page numbers come from a search summary, and the LBL page gives no pages. The paper compiles 274 measurements of demand change during Earth Hour across 10 countries over 6 years. The average reduction is 4%, ranging from +2% (New Zealand) to −28% (Canada). The authors frame it as evidence that coordinated behaviour can shift regional demand, which could be used during temporary shortfalls. — [LBL record](https://eta-publications.lbl.gov/publications/electricity-impacts-earth-hour); [eScholarship PDF](https://escholarship.org/uc/item/4bj0h7bc); earlier conference version: [Olexsak & Meier, eceee Summer Study 2013](https://www.eceee.org/library/conference_proceedings/eceee_Summer_Studies/2013/8-dynamics-of-consumption/the-electricity-impacts-of-earth-hour-and-other-coordinated-energy-demand-shifting-actions/2013/8-011-13_Olexsak.pdf/)
  - *Relevance:* This is the canonical "meta-measurement" of a synchronized voluntary act from grid data, and it collects heterogeneous estimates made by grid operators. Each estimate is a % change against some baseline, and the abstract does not say which. For us it shows (a) the effect expressed as a % of a counterfactual load, analogous to our % speed loss, and (b) the risk of heterogeneous, operator-chosen baselines. That argues for our pre-registered same-weekday control-day design.
- **[V-partial] Shanghai smart-meter study of Earth Hour, World Environment Day and Energy Saving Week (APPAM 2020 conference paper; IAEE proceedings abstract).** Authors were not captured. It uses 15-minute smart-meter data with a two-step local-linear method that first removes weather, seasonal and day-of-week effects. It finds commercial reductions of about 4–5% for some campaigns, but a **rebound after Earth Hour**. — [APPAM](https://appam.confex.com/appam/sc20/webprogram/Paper34260.html); [IAEE abstract](https://iaee.org/en/publications/proceedingsabstractpdf.aspx?id=17261)
  - *Relevance:* This is a model for (i) explicitly netting out day-of-week and weather before measuring the event dip, and (ii) checking for **post-event rebound or displacement**. We should do the same: catch-up congestion after 09:06 could offset part of the stop, or spill into the 10:00 hour.
- **[U, non-peer-reviewed] Solomon (Sydney) working-paper blog.** It argues that once trend and day effects are controlled, the Earth Hour dip is about 2.1% and statistically insignificant. — [Institutional Economics](https://institutional-economics.com/section/the_failure_of_earth_hour)
  - *Relevance:* A cautionary example of a synchronized-event effect disappearing under a proper counterfactual and inference. It motivates our randomization inference.

**TV pickup (positive spikes)**
- **[V, grey literature] National Grid ESO / NESO press material.** TV pickup is a demand surge synchronized with breaks in popular broadcasts. Reported pickups: about 2,800 MW at the end of the 1990 World Cup semi-final (England–West Germany); 1,400 MW at half-time of the Euro 2020 semi-final against Denmark; 1,350 MW at half-time of the 2019 Rugby World Cup final. ESO forecasts these and holds reserve. Pickups have shrunk as viewing moved to streaming, because there is no longer a single "end time". — [NESO news on Euro 2020 final](https://www.neso.energy/news/its-coming-ohm-national-grid-eso-expects-2gw-spike-during-euro-2020-final); [Designing Buildings wiki summary](https://www.designingbuildings.co.uk/wiki/TV_pickup); [Drax, "biggest TV moments"](https://drax.com/?p=708)
  - *Relevance:* The grid operator **converts a MW spike into a participation-equivalent number** (kettles ≈ households) and forecasts it in advance. Our conversion of speed loss into "full-stop-equivalent minutes" is the traffic analogue. The baseline is usually the operator's own demand forecast, which is an implicit counterfactual. I found no peer-reviewed econometric study of TV pickup.

**National moments of silence (closest analogue)**
- **[V, grey literature] Armistice Day 2010, UK:** National Grid reported a 620 MW reduction during the two-minute silence, "a city the size of Bristol", and attributed the size partly to the wars in Iraq and Afghanistan. **Armistice Day 1996:** a dip "the size of Leeds" as factories shut down machinery; this was the first weekday observance since the 1930s. — [blog reproducing the BBC/National Grid report, 2010](https://carbonfeednews.blogspot.com/2010/11/bn-uks-two-minute-silence-cuts-power.html); [archived BBC2 Ceefax page, 11 Nov 1996](https://al.zerostem.io/~al/teletext/bbc2/1996-11-11-0002.1/111.html). These are secondary or archival copies; the original BBC URL was not found.
- **[V, grey literature] Queen Elizabeth II funeral, 19 Sept 2022:** demand fell about 2 GW as people switched to the broadcast, then a further about 500 MW during the two-minute silence, before recovering. — [inkl / news report](https://inkl.com/news/huge-power-drop-recorded-across-uk-during-the-queen-s-funeral)
- **[V] IESO (Ontario) news, Nov 2021:** about 235 MW drop during the 11:00 Remembrance Day moment of silence ("a city the size of Waterloo"). — [IESO](https://ieso.ca/Sector-Participants/IESO-News/2021/11/Electricity-Demand-Drops-as-Ontario-Observes-Moment-of-Silence)
  - *Relevance (all three):* These are the **most direct precedents** for our paper: a national remembrance silence at a fixed clock time, measured with passive infrastructure data, and translated into an intuitive equivalent ("a city the size of X"). They also show the gap our paper fills. None publishes a counterfactual method or uncertainty, and all are minute-resolution grid observations described in press releases. Our design adds an explicit same-weekday control, randomization inference, and a transparent conversion (full-stop-equivalent minutes).

**Prayer times / Ramadan / iftar**
- **[V, grey literature] Jordan NEPCO:** grid load drops about 8% during Ramadan (about 150 MW), attributed to shorter working hours. A 2008 statement attributes about 200 MW to families gathering at one house for iftar. — [Jordan Times](https://jordantimes.com/news/local/electricity-usage-drops-ramadan-working-hours-reduced); [Zawya 2008](https://www.zawya.com/en/business/jordan-warm-weather-expected-to-prevail-as-energy-consumption-drops-n1h793h8)
- **[V-partial] University of Southampton MSc dissertation (Yakoub, 2024)** on smart-meter energy use in Ramadan. It hypothesises two daily peaks around mealtimes; the sample is small and non-representative. — [eprints.soton.ac.uk](https://eprints.soton.ac.uk/494893/1/MC2024KT8001_Hanaa_Yakoub.pdf)

### Inferences
- In this literature the effect is usually reported in **physical units (MW)** and then converted into a **population-equivalent metaphor** (households, "a city the size of Bristol"). Our "full-stop-equivalent minutes" fits this tradition, but we should state the conversion's assumptions explicitly, since the grid literature almost never does.
- The silence dips (about 0.5 GW in the UK, about 0.2 GW in Ontario) are typically reported as differences from the operator's forecast or from adjacent minutes. That is a within-day, pre/post contrast. Our within-day DiD against same-weekday controls is a strict generalization of that practice.
- Earth Hour's rebound finding, together with the Sydney critique, suggests reporting (i) the effect in the siren hour and (ii) any compensating effect in adjacent hours.

### Gaps
- I found **no peer-reviewed econometric study of a moment-of-silence grid dip**. The evidence is press releases and secondary copies. This is a genuine gap that our paper can claim to partly fill (for traffic).
- I found no peer-reviewed analysis of TV pickup (ESO data are public; the analyses are operator material).
- I found no peer-reviewed study of electricity load at iftar or prayer times in Turkey or the Gulf. TEİAŞ / EPİAŞ hourly data could support one, but I found no published paper.
- I did not access the Meier & Olexsak full text, so I cannot report their baseline definition. The abstract does not state it.
- There is no Earth Hour paper in *Energy Policy* that I could verify (the brief's attribution appears to be wrong).

## Q2. Water use / sewage flow during halftime or national events ("Super Bowl flush")

### Takeaway
The "halftime flush" is widely reported by utilities but almost entirely outside the peer-reviewed literature. The only peer-reviewed item located is a 1975 ASCE brief report on wastewater from football spectators at Penn State, which estimated a per-spectator contribution: an early "conversion to per-participant units".

### Cited Findings
- **[V-partial] ASCE *Journal of the Environmental Engineering Division* (1975), Brief Report, DOI 10.1061/JEEGAV.0000339.** It reports a significant increase in wastewater flow at the Penn State treatment plant on football days and uses flow records to estimate wastewater contribution per spectator. The publisher page returned 403, so **authors, volume and pages are unverified**. — [ASCE Library](https://ascelibrary.com/doi/10.1061/JEEGAV.0000339)
  - *Relevance:* An early example of converting an aggregate infrastructure anomaly into a **per-participant equivalent**, using a game-day vs non-game-day contrast as the counterfactual.
- **[V, grey literature] Melbourne Water "Flush Factor":** compares water flow during televised match breaks with usual consumption. It reported a 13% rise at half-time in a Matildas match and 33% at the end of another match. — [Melbourne Water](https://melbournewater.com.au/node/7246)
- **[V, grey literature] NYC water demand, Super Bowl 2018:** compared with the two preceding Sundays, with spikes at the start and end of the halftime show and at the end of the game. — reported in [WWD Magazine, "The Super Bowl Flush"](https://www.wwdmag.com/super-bowl-flush)
  - *Relevance:* This is exactly our counterfactual logic: the **same weekday in adjacent weeks as control days**.
- **[V, grey literature] Henderson and North Las Vegas, NV:** treatment-plant flows on Super Bowl Sunday (peak about 27 MGD vs 21 MGD normal; a 10-minute peak to 39 MGD vs a 17 MGD daily average). Other utilities (Portland; Westminster, CO) report the spike as negligible. Operators note that travel time through sewers smooths the spike. — [Las Vegas Review-Journal via PressReader](https://www.pressreader.com/usa/las-vegas-review-journal-sunday/20170205/283085593919577); [9News](https://www.9news.com/article/sports/nfl/superbowl/sewer-wastewater-municipal-systems-dont-back-up-break-malfunction-super-bowl-flush/536-5cb9e4c9-18f3-4718-a490-e862cce46c32); [Westminster CO](https://westminsterco.gov/closures-delays/city-sewer-system-is-ready-for-the-big-game-uniflush)
  - *Relevance:* This is a **measurement-smoothing lesson**. Sewage flow low-pass-filters a minutes-long shock, the same way hourly geohash averaging dilutes a 1–2 minute stop. We should explicitly model the dilution: a full stop of *d* minutes appears in an hourly mean as roughly *d/60* of the hour's speed.

### Inferences
- Water and sewage data reproduce the TV-pickup logic (synchronized break → synchronized appliance use). Utilities that use same-weekday comparisons (NYC) are applying the same counterfactual as our design.
- The "dilution by aggregation" problem (sewer travel time; our hourly aggregation) is a shared methodological theme worth a paragraph in our paper.

### Gaps
- I found no recent peer-reviewed systematic study of halftime water or sewage spikes.
- The authors and pages of the 1975 ASCE report are unverified (paywall/403).
- The widely repeated "Super Bowl flush" myth has no single authoritative source; the original NYC 2018 data presentation was not retrieved.

## Q3. Mobile phone / CDR / app data and traffic data during collective events (sports, emergencies, religious periods, eclipse)

### Takeaway
Network-science CDR studies show that planned collective events leave measurable, timed signatures in phone activity. They typically use **"same weekday in preceding weeks" baselines** and z-score anomalies, and phone activity scales linearly with crowd size, which enables conversion to participant counts. Traffic studies of synchronized events, chiefly the 2017 US eclipse, measure minutes-to-hours-long flow and crash anomalies against day-of-week-matched controls. I found no peer-reviewed traffic-flow study of iftar, Friday prayer, or a minute's silence.

### Cited Findings
**Phone / CDR**
- **[V] Bagrow, J.P., Wang, D. & Barabási, A.-L. (2011). "Collective response of human populations to large-scale emergencies." *PLoS ONE* 6(3): e17680. DOI 10.1371/journal.pone.0017680.** CDRs for about 10 million subscribers (European country, 2007–09). Eight emergencies compared with eight planned events (concerts, sports): emergencies show a sharp "jump-decay" call anomaly lasting 3–5 hours, while planned events build gradually over 7+ hours. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3068136); [arXiv](https://ar5iv.labs.arxiv.org/html/1106.0560)
  - *Relevance:* The **canonical big-data event study** of collective behaviour. It contrasts anomalies with normal activity patterns for the same time window (as I understand it, typical weekday activity; check the full text) and distinguishes planned vs unplanned shocks. Our siren is the extreme planned, clock-synchronized case: a jump of about 1–2 minutes with no gradual build-up, which hourly data can only partly resolve.
- **[V] Botta, F., Moat, H.S. & Preis, T. (2015). "Quantifying crowd size with mobile phone and Twitter data." *Royal Society Open Science* 2(5): 150162.** Open access; data at Dryad doi 10.5061/dryad.1rk60. Milan, Nov–Dec 2013 (Telecom Italia). Calls/SMS in the San Siro cell scale linearly with match attendance (adjusted R² = 0.937, N = 10). — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4453255); [Exeter repository](https://ore.exeter.ac.uk/repository/handle/10871/122099?show=full)
  - *Relevance:* A model for **converting a passive-data signal into a participation count** via an explicit calibration, with **few events (N = 10)**. Our "full-stop-equivalent" conversion is a calibration-free analogue. If we had ground truth (e.g., the share of drivers who stop, from dashcam or survey), we could calibrate in the same way.
- **[V] Pintér, G. & Felde, I. (2021). "Analyzing the Behavior of Soccer Fans from a Mobile Phone Network Perspective: Euro 2016, a Case Study." arXiv:2108.09291 (preprint; no journal reference on arXiv).** Vodafone Hungary CDRs, Budapest, June 2016. Activity rises above the average of preceding weekdays before kickoff, falls until half-time, and goals create significant peaks. — [arXiv](https://arxiv.org/abs/2108.09291)
  - *Relevance:* A minute-resolution signature of a synchronized national event. The baseline is the average of preceding weekdays (descriptive only, no formal inference), and it is a **same-weekday-style control**.
- **[V, industry, not peer-reviewed]** Ramadan app-usage reports (AppsFlyer, Adjust) show shifts in activity after iftar/taraweeh and pre-suhoor. Methods are opaque. — [AppsFlyer SE Asia/Pakistan report](https://www.appsflyer.com/resources/reports/ramadan-se-asia-pakistan-report/)

**Traffic during synchronized events**
- **[V] Ngeni, F., Mwakalonge, J. & Siuhi, S. (2022). [Title as indexed in DOAJ: study of traffic during the 21 Aug 2017 total solar eclipse.] *Transportation Research Interdisciplinary Perspectives* 13: 100510. DOI 10.1016/j.trip.2021.100510.** FHWA count data for the states in totality. Traffic fell 13% three hours before the eclipse and rose 13% two hours after, compared with regular traffic. The exact title was not captured. — [DOAJ](https://doaj.org/article/aef14866fa284d709b528600033e1be3)
  - *Relevance:* A peer-reviewed transport study of a **clock-synchronized, minutes-long collective event**, using comparison to "regular" traffic. It is the closest transport-journal analogue to our siren.
- **[V-partial] Upchurch, J. (2018). "Total Solar Eclipse on August 21, 2017: Special Event with Coast-to-Coast Traffic Congestion." *TR News* 317, 3–9 (TRB practitioner magazine).** Up to 13 hours of congestion on some Interstates. — [TRID](https://trid.trb.org/View/1552782); [PDF via AAS](https://eclipse.Aas.Org/sites/eclipse.aas.org/files/TRNews_TSE2017_Traffic.pdf)
- **[V-partial] Redelmeier and colleagues (2024), *JAMA Internal Medicine* research letter.** Fatal crashes around the 2017 eclipse rose 31%. **Control intervals were matched on day of week** and adjacent weeks to absorb seasonal and weekly variation. The co-author list and DOI were not captured. — [AccuWeather summary](https://www.accuweather.com/en/solar-eclipse-2024/total-solar-eclipse-in-2017-drew-a-brief-surge-in-traffic-accidents-analysis-shows/1634929); [WRAL](https://www.wral.com/total-solar-eclipse-in-2017-drew-a-brief-surge-in-traffic-accidents-analysis-shows/21346165/)
  - *Relevance:* Redelmeier's "event day vs same weekday one week before and after" design (also used in his earlier work on other events) is **exactly our control-day logic**, and is citable as precedent in a top medical journal.

### Inferences
- Across CDR and traffic studies, the dominant counterfactual is **"same time of day, same weekday, nearby weeks"**. This directly supports our choice of same-weekday control days.
- Phone-data studies sometimes calibrate signal → participants (Botta et al.). Grid studies use metaphors. Traffic studies rarely convert at all. Our full-stop-equivalent minutes would be a novel, explicit conversion in transport.

### Gaps
- I found **no peer-reviewed study using traffic speed or flow data around a national minute's silence** (Turkey's 10 November siren, Israel's Yom HaShoah/Yom HaZikaron sirens, UK/Commonwealth 11 November). Israel's sirens are an obvious comparison case; I found no paper on them in this search, so the absence is not confirmed beyond these queries.
- I found no peer-reviewed traffic-speed study of iftar (Turkey/Gulf/Indonesia) or Friday prayer. Evidence is limited to crash and insurance timing (see Q4) and press.
- I did not find Turkish-language (DergiPark) studies on İBB data around iftar or 10 November. A DergiPark search is recommended.
- I could not confirm Bagrow et al.'s exact baseline definition from the abstract.

## Q4. Behavioural measurement of civil/religious ritual effects (Ramadan fasting and traffic, etc.)

### Takeaway
The strongest economics paper here is Gulek (2024, *J. Development Economics*). It identifies the effect of Ramadan fasting on crashes in Turkey using the timing of rush hour relative to fasting hours, finding about a 25% increase in accident probability. A cluster of medical and public-health studies document pre-iftar crash peaks (Pakistan, Saudi Arabia, Jordan, UAE) with simpler before/after comparisons.

### Cited Findings
- **[V] Gulek, A. (2024). "Driving while hungry: The effect of fasting on traffic accidents." *Journal of Development Economics* 168: 103260. DOI 10.1016/j.jdeveco.2024.103260.** Turkey. Fasting raises the probability of an accident by about 25% (less than drunk driving, more than mild sleep deprivation). Identification exploits rush-hour traffic patterns that are not adjusted during Ramadan, so exposure stays constant while the fasting state changes. — [RePEc/IDEAS](https://ideas.repec.org/a/eee/deveco/v168y2024ics0304387824000099.html); [author page](https://ahmetgulek.github.io)
  - *Relevance:* A Turkish case of **ritual timing used as quasi-experimental variation**, with a design that holds traffic exposure fixed via within-day timing, much like our within-day DiD. It is directly citable for "religious/civil ritual timing → measurable traffic outcomes in Turkey". The precise estimator (DiD across hours × Ramadan vs non-Ramadan) was not confirmed from the full text.
- **[V-partial] Pakistan, *Eastern Mediterranean Health Journal* (2013) 19 Suppl 3: S147–S151.** Rescue 1122 Punjab data show more road traffic crashes during Ramadan than in preceding months, peaking in the hours before iftar. The authors were not captured. — [WHO EMRO PDF](https://applications.emro.who.int/emhj/v19/Supp3/EMHJ_2013_19_Supp3_S147_S151.pdf?ua=1)
- **[V-partial] Jordan (Irbid), *Neurosciences* (Saudi) 11(1) (2006).** A hospital-based study of road-crash patients in Ramadan vs other months. — [nsj PDF](https://nsj.org.sa/content/11/1/21.full.pdf); [NSJ record](https://nsj.researchcommons.org/journal/vol11/iss1/6)
- **[V-partial] Turkey ED visits in Ramadan, *Disaster and Emergency Medicine Journal* (2019),** DOI-style ID DEMJ.2019.0008. — [Via Medica PDF](https://journals.viamedica.pl/disaster_and_emergency_medicine/article/download/DEMJ.2019.0008/48910)
- **[V, press] UAE insurance-claim analyses:** Ramadan crashes concentrate between noon and 18:00, with 14:00–16:00 the peak. Other UAE studies find a morning rush peak; findings conflict across datasets. — [Khaleej Times](https://www.khaleejtimes.com/uae/uae-road-accidents-spike-before-iftar-during-ramadan-2pm-4pm-most-dangerous); [The National 2026](https://www.thenationalnews.com/news/uae/2026/02/19/ramadan-road-safety-warning-issued-as-earlier-finish-to-working-day-raises-accident-risk)
  - *Relevance:* These show that ritual timing is a recognised **traffic-safety exposure**. A side point for our paper: the siren stop itself may carry crash risk (sudden stops on fast roads), which we could note as an extension.

### Inferences
- Gulek's paper gives the econ framing: synchronized ritual timing produces sharp, predictable variation that can be exploited within day. Our siren is a cleaner case: a single minute, nationally synchronized, with no change in work hours.
- The medical literature on pre-iftar crash peaks uses month-vs-month comparisons. We can contrast our tighter same-weekday, within-day design.

### Gaps
- I did not obtain Gulek's full text, so the exact estimator, data source (likely Turkish crash records) and inference method are unconfirmed.
- I found no study measuring the **economic cost** of a civil ritual (e.g., the time cost of the 10 November stop or of Yom HaZikaron sirens) from behaviour data. This looks like an open niche.

## Q5. Methodological lessons: counterfactuals, conversion to participation-equivalents, inference with few events

### Takeaway
Three counterfactual families recur: (1) **same-weekday / adjacent-week controls** (NYC water, Pintér & Felde, Redelmeier's eclipse design; Bagrow et al. likely similar); (2) **operator forecasts** as implicit counterfactuals (National Grid, IESO); (3) **model-based detrending** of weather, season and day-of-week (Shanghai Earth Hour). Conversion into participation units ranges from metaphor ("city the size of Bristol") to calibration (Botta et al., per-spectator wastewater). With few events, the econometric literature on DiD with few treated units (Conley & Taber 2011; Ferman & Pinto 2019) and randomization/permutation inference is the right anchor.

### Cited Findings
- **[V-partial] Ferman, B. & Pinto, C. (2019). "Inference in differences-in-differences with few treated groups and heteroskedasticity." *Review of Economics and Statistics* 101.** They extend Conley–Taber to heteroskedasticity from varying group sizes, which can invalidate existing methods even with many observations per group. Issue, pages and DOI were not captured. — [MPRA working version](https://mpra.ub.uni-muenchen.de/68271/1/MPRA_paper_68271.pdf); [FGV record](https://oasisbr.ibict.br/vufind/Record/FGV_8989660f4d33ddd678d7f60481fb4f5a)
  - *Relevance:* In our design the treated unit is (one day × the 09:00 hour) and the controls are other days and hours. Geohash cells differ in observation counts, so the **heteroskedasticity concern applies directly**. Our randomization inference over placebo days and hours should be justified with this paper and Conley–Taber.
- **[V-partial] Conley, T.G. & Taber, C.R. (2011). "Inference with 'Difference in Differences' with a Small Number of Policy Changes." *Review of Economics and Statistics* 93(1): 113–125.** Venue and year were confirmed via Ferman–Pinto's discussion; volume and pages are from my own prior knowledge and were **not checked this session**. It uses the control-group residual distribution to make inference with few treated groups. — discussed in [MPRA 68271](https://mpra.ub.uni-muenchen.de/68271/1/MPRA_paper_68271.pdf)
- **[V-partial] Alvarez, L. & Ferman, B. (2023), arXiv:2302.03131.** Extends to staggered adoption and notes that DiD estimators with few treated units are not consistent or asymptotically normal. — [arXiv](https://arxiv.org/pdf/2302.03131.pdf)
  - *Relevance:* If we pool multiple years of 10 November, each year is a treated "event". This paper and Conley–Taber justify permutation over placebo dates over asymptotic standard errors.

### Inferences
- Our design (within-day DiD, same-weekday controls, randomization inference over placebo dates and hours) **combines the best practices scattered across this literature**: the same-weekday controls of utility and CDR studies, the detrending of the Earth Hour smart-meter work, and the few-treated-units inference of Conley–Taber and Ferman–Pinto. None of the electricity, water or CDR event studies reviewed here reports formal inference for a single minutes-long event. This is a contribution we can claim.
- Conversion: we should present (a) the raw effect (% speed loss in affected geohash-hours), (b) the full-stop-equivalent minutes per vehicle (effect × 60), and (c) a population metaphor (total vehicle-minutes ≈ X), matching how grid operators communicate, but with the assumptions spelled out.
- Aggregation dilution (hourly speeds; compare sewer smoothing) means the hourly DiD estimate is a **lower bound on peak stop intensity**. It is an exact average of minute-level slowdown only if speeds are vehicle- or time-weighted within the hour; this should be checked against İBB's averaging definition.

### Gaps
- **Not verified this session (from prior knowledge only; check before citing):** Abadie, Diamond & Hainmueller (2010) synthetic control, *JASA* 105(490), 493–505; Fisher-style randomization inference references, e.g., Imbens & Rubin (2015) *Causal Inference for Statistics, Social, and Biomedical Sciences*, CUP; MacKinnon & Webb on wild bootstrap with few treated clusters (cited inside Ferman–Pinto as MacKinnon & Webb 2015a working paper). All **[U]**.
- I found no study in this literature using synthetic control for a minutes-long collective event. The utility and CDR literature relies on simple same-weekday averages.
- I could not locate the full methods of most grid-operator silence measurements (baseline = forecast? adjacent minutes?), so the comparison with our design rests on press descriptions.
