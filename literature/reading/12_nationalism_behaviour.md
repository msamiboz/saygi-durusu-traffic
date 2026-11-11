# 12 - Nationalism measured through behaviour: reading notes

Reader group 12. Papers: depetris2020, madestam2011, dinas2024, parravano2015, skitka2005, carter2011.
All six text files were read in full (reference lists skimmed). Figures and two tables were checked against the PDFs
(dinas2024 pp. 8-12, skitka2005 pp. 9-11, parravano2015 pp. 7-8).

Page numbers are PDF pages as marked in `literature/txt/<key>.txt`. Offsets to printed pages:
depetris2020 printed = PDF - 1 (working-paper layout); madestam2011 printed = PDF - 2; dinas2024 journal page = PDF + 487;
skitka2005 journal page = PDF + 1994; carter2011 journal page = PDF + 1010; parravano2015 PDF = PLOS page.

Two things to know before using these notes:

1. **None of the six papers studies traffic, sirens, moments of silence, or any synchronized ritual.** They support the
   framing (public, visible acts as measures of national attachment; norms versus preferences), not our measurement.
2. Only two of the six actually observe behaviour directly (dinas2024, parravano2015: flag counts). depetris2020 measures
   attitudes by survey and conflict from event data; madestam2011 does not observe participation at all; skitka2005 is a
   self-reported checklist; carter2011 is a priming experiment.

---

### depetris2020 - Depetris-Chauvin, Durante and Campante (2020), Building Nations Through Shared Experiences: African football

Note: the PDF on disk is the September 2019 pre-publication version (p. 1), not the AER typeset. Check numbers and page
references against the published article (AER 110(5): 1572-1602) before quoting.

- **Question and setting.** Do shared collective experiences build national identity? Tested with national football
  team results in sub-Saharan Africa, 2002-2015 for attitudes and 1997-2015 for conflict (pp. 2-3).

- **Data and method.**
  - *National attachment is measured by a survey item, not behaviour.* Afrobarometer rounds 2-6 ask respondents to choose
    between national and ethnic identity on a 5-point scale; the outcome is a dummy for the two
    answers that put ethnic above national identity (pp. 7-8). 57 survey rounds, 25 countries (p. 7).
  - Matches: 69 official matches (Africa Cup of Nations and World Cup qualifiers and finals) with interviews within
    15 days before or after; 31 wins, 29 losses, 9 draws. A 30-day window gives 85 matches; 66 friendlies serve as a
    placebo (p. 7).
  - Estimator (eq. 1, p. 11): Outcome = a + b*Post + individual controls + country x match FE + language-group x year FE
    + day-of-week, day-of-month and month dummies. Identification comes from interview timing relative to the match,
    within the same country, match and language group. Benchmark sample: 37,060 respondents exposed to exactly one
    match (pp. 11, 15). Standard errors clustered by country x year.
  - Multiple testing: False Discovery Rate adjusted p-values (Anderson 2008) across 11 outcomes and across the
    heterogeneity interactions (pp. 11, 15, 18).
  - Balance table for respondent and interviewer characteristics (pp. 12-13); three imbalances after victories
    (education, gender, rural), two of which work against the finding.
  - Conflict: ACLED country-week events. Treated = countries that qualified for the Africa Cup of Nations in the last
    round; control = countries in the same group that could still qualify before the last match day and did not.
    49 treated and 60 control country x campaign pairs (pp. 24-25). Eq. 2 (p. 24): log(1 + events) on Post-Qualification,
    4 lags of the outcome, week-relative-to-qualification dummies (-25 to +25), calendar-month FE, country x campaign FE;
    clustered by country x campaign.

- **Main findings.**
  - Being interviewed after any match: -0.036 (SE 0.014) on ethnic identification. This is entirely victories:
    post-victory -0.053 (SE 0.016, FDR p = 0.010), post-draw -0.026 (0.039), post-defeat -0.000 (0.017) (p. 15).
    -5.3 pp is a decrease of more than 37% relative to the mean (p. 14).
  - Event-study in 3-day bins: no movement before the match, effect persists and grows over the 15 days after (pp. 14, 16).
  - Friendly-match victories: +0.019 (0.015), no effect (p. 18). Rival opponents: interaction -0.061 (0.020). Home
    versus away: interaction 0.014 (0.031), no difference (pp. 17-18).
  - Trust in countrymen +0.063 (0.021), 14% of the mean; inter-ethnic trust +0.140 (0.040), 30% of the mean (pp. 20, 22).
    Dislike of foreign neighbours +0.019 (0.018), not significant (p. 22).
  - No effect on trust in the ruling party, presidential approval, or economic optimism, which the authors read as
    evidence against a pure mood effect (pp. 22-23).
  - Conflict: Post-Qualification -0.090 (0.039) with lags, i.e. 8.6% fewer events (100*(exp(-0.09)-1)); pre-period
    placebo (12 weeks before) 0.028 (0.054); similar size in weeks 1-12 and 13-25 (pp. 26-27). Robust to dropping the
    tournament weeks (-0.092, p. 33).
  - State presence (schools, post offices, paved roads) dampens the victory effect: interaction 0.049 (0.027), FDR
    p = 0.13 (pp. 18-19). The authors read this as substitution between shared experiences and other nation-building.

- **Usable for our paper.**
  - *Introduction / Literature.* An AER paper establishes that shared national experiences have measurable effects on
    identity and on violence (pp. 2-4). The conclusion explicitly extends the argument to civic events that favour
    emotional participation (p. 35). This motivates why the extent of participation in a civic ritual is worth
    measuring.
  - *Literature.* The paper separates softer symbolic tools (flag, anthem; Billig's banal nationalism), which it says can
    maintain an identity that already exists but are unlikely to create one, from collectively shared experiences
    (p. 5). The 10 November stop sits between the two: a symbolic act that is also a shared experience. This is our
    reading, not the paper's.
  - *Literature.* The home/away null is interpreted as showing the effect is "not driven by direct participation in the
    event" (p. 4). Shared experience in this paper is imagined and mediated. Our object is the opposite case, physical
    and synchronous co-participation, so the paper is a contrast, not a precedent.
  - *Method / Robustness.* Three design elements transfer directly: (i) FDR-adjusted p-values when several outcomes or
    subgroups are tested (p. 11); (ii) a low-stakes placebo event that looks like the treatment (friendlies, p. 18);
    (iii) leave-one-out over waves, countries and matches, plus DFBETA-based exclusion of influential matches
    (fn. 11, p. 16).

- **Caveats.**
  - The paper measures the *consequences* of a shared experience, not participation in one. It cannot be cited as a
    precedent for measuring ritual participation from behaviour.
  - The treatment is a victory. Matches as such (defeats, draws) do nothing. There is no claim that recurring,
    predictable commemorations have effects; the paper finds that unexpected achievements matter more (pp. 28-30).
  - National attachment is self-reported relative to ethnic identity, a construct specific to the African setting.
  - Our earlier notes (`notes/commemoration_turkey.md`) give "37% less likely", "30% more likely to trust other
    ethnicities" and "about 9% fewer conflict episodes". These match the abstract (p. 1); the regression-based conflict
    figure is 8.6% (p. 26). Not overstated, but they are relative to low baselines (-5.3 pp and +14.0 pp in absolute
    terms).

- **Checks or analyses it suggests for us.**
  - Report FDR-adjusted (Anderson 2008) p-values across the five speed classes, next to the unadjusted randomization
    p-values.
  - Plot the within-day profile in event-study form (each hour 06h-12h relative to a reference hour, 10 Nov minus
    controls) to show a flat pre-period, as in their Fig. 2 (p. 16).
  - Leave-one-year-out estimates (five estimates), the analogue of dropping one wave or country at a time.
  - A "friendly match" placebo: another date with a public ceremony but no stop-the-traffic custom, same 09h contrast.

---

### madestam2011 - Madestam and Yanagizawa-Drott (working paper, 2011/2012), Shaping the Nation: Fourth of July

Status: HKS Faculty Research Working Paper RWP12-034, dated August 2012, manuscript dated November 2011. The cover
page states that papers in the series have not undergone formal review (p. 1). Cite as a working paper.

- **Question and setting.** Does participating in Fourth of July celebrations, in childhood or adulthood, change
  party identification, turnout and vote choice in the United States? Cohorts born 1920-1990 (pp. 3-4).

- **Data and method.**
  - *Participation is not observed.* The authors say so directly: "data on historical attendance is unavailable"
    (p. 4). Absence of rain on 4 July in the county is used as a proxy for participation.
  - Outcomes: 25 ANES cross-sections 1954-2008. Rainfall: NOAA daily data from about 18,000 stations, July 1920-2008,
    averaged to county level; counties with at least 50 years of data (p. 10). County of childhood is unknown; the
    sample is restricted to respondents living in their region of birth, which the authors treat as classical
    measurement error (p. 11). When 4 July falls on a Sunday they use 5 July rain because the holiday is observed
    then (fn. 13, p. 11).
  - Childhood treatment: number of rain-free 4 Julys at ages 4-18 (mean 9.10, SD 2.90, range 0-15; within-county SD
    1.63) (pp. 16, 19, 39). Adult treatment: dummy for a rain-free 4 July in the survey year (mean 0.624; p. 39).
  - Reduced form (eq. 6, p. 16): y = lambda * R + county FE + birth-cohort FE + survey-year FE + state trends +
    covariates; SEs clustered by state. Persistence by non-linear least squares (eq. 7): y = delta^t * theta * R,
    with t = years since age 18.
  - Lower-bound logic (p. 15): with participation T = a' + gamma*R + mu and 0 < gamma <= 1, the reduced form
    identifies theta = beta*gamma <= beta. The persistence parameter delta is identified even though gamma is not.
  - "First stage" is indirect: state-year panel 1990-2009 (940 obs) of whether at least one newspaper reported a
    cancelled parade, fireworks or barbecue, regressed on the share of counties with rain (pp. 10-11, 18, 40).
  - Placebos: rain on 2, 3, 5 and 6 July, in childhood and in adulthood (pp. 6, 20).
  - Exogeneity check: covariates do not predict rain; joint p = 0.248 (childhood) and 0.841 (adult) (pp. 19, 41).

- **Main findings.**
  - Rain raises cancellation reports: share of rainy counties -> +0.107 (SE 0.043) on any cancellation; adjacent days
    jointly zero, p = 0.762 (p. 40). Anecdotes: Washington Metro ridership down by more than 100,000 on a rainy 4 July
    2004; a Houston event at about half its usual 100,000 (p. 10).
  - Childhood, per additional rain-free 4 July: Republican identification +0.61 pp (SE 0.30 pp), 1.7% of the 36.2%
    base (pp. 19-20, 42); turnout +0.88 pp (0.25) (pp. 21, 43); voting Republican +0.85 pp (0.39) (pp. 21, 43); no
    effect on voting Democrat (0.0004, SE 0.0033; p. 43). Placebo days: joint p = 0.801, 0.867, 0.625 (pp. 20-21).
  - Critical ages: party identification 4-8 (0.0090, SE 0.0040) and 9-13; turnout 9-13 (0.0130, SE 0.0036); nothing
    at ages 0-3 (pp. 23, 45).
  - Persistence: delta_child = 1.046 and 1.025 for party identification (Table 6, p. 44; the text on p. 22 gives 1.045
    and 1.023); about 0.985-0.996 for turnout, half-life of at least 45 years (p. 22).
  - Adults: a rain-free 4 July in the survey year raises Republican identification by 1.78 pp (SE 0.70); no
    significant effect on turnout or vote; delta_adult between 0.71 and 0.87 across specifications, half-life about 2.4 years at 0.746 (pp. 24, 46-47).
  - Context figures (surveys cited by the authors): in 2011 an estimated 151 million adults attended a barbecue,
    104 million watched fireworks or a community event, 31 million saw a parade; a majority report displaying flags;
    Republicans attend more and rate the holiday as more important (p. 3).

- **Usable for our paper.**
  - *Introduction / Literature.* The best-known economics paper on a national holiday could not observe who took part
    and had to proxy participation with weather (p. 4). Direct behavioural measurement of participation in a national
    ritual is therefore a gap we can claim to address, for one ritual in one city.
  - *Literature.* The paper names the mechanisms by which national days matter: rituals that reconfirm societal
    commitments and national identity (Durkheim, Turner, Etzioni) and, via Chwe (2001), events that create common
    knowledge and so coordinate behaviour (p. 7 and fn. 4). The Chwe reference is the useful one for a siren: a public
    signal that everyone knows everyone else hears.
  - *Method.* The lower-bound argument theta = beta*gamma <= beta (p. 15) has the same structure as our claim that
    excluding stopped vehicles makes our estimate a lower bound. Useful as a stylistic model for stating the bound
    formally.
  - *Robustness.* Adjacent-day placebos with a joint test (pp. 20, 42-43) are the direct model for placebo dates
    around 10 November.
  - *Results-Discussion.* The authors flag that peer effects could create a social multiplier (Glaeser et al. 2003),
    so the effect may rise with the number of participants, and that they cannot test this for lack of attendance data
    (fn. 15 p. 12; fn. 20 p. 15). Supports stating that aggregate participation is not a sum of independent choices.
  - *Results-Discussion.* Participation is politically selected (Republicans attend more, p. 3). The analogue is that
    stopping on 10 November is unlikely to be politically neutral across Istanbul districts.

- **Caveats.**
  - No first stage on attendance. The only evidence that rain lowers participation is newspaper mentions of
    cancellations at state-year level after 1990, for an effect estimated on childhoods from the 1920s on.
  - It is an effect-of-participation paper. It says nothing on how to measure participation, and nothing on
    commemorations of mourning; the Fourth is festive and held outdoors, which is why rain matters.
  - Internal inconsistencies, typical of a draft: the Republican-parents benchmark is 1/70 (pp. 6, 28) and 1/72
    (p. 26); the canvassing comparison uses a turnout effect of 0.78 pp (p. 28) while the headline is 0.88 pp (p. 21);
    the introduction says reinforcement of 2.5% per year (p. 5), the results say 2.3 to 4.5 (p. 22); Carter et al. is
    described as finding an 8 pp higher McCain vote (p. 28), while Carter et al. report 27.2% versus 16.5%, a gap of
    10.7 pp (carter2011 p. 4).
  - **Correction to our earlier notes.** `notes/commemoration_turkey.md` says one rain-free Fourth raises Republican
    identification "by about 2%", Republican vote "by about 4%" and turnout "by 0.9%". Those figures are not in this
    version of the paper. This version reports percentage points: +0.61 pp identification (1.7% of the base), +0.85 pp
    Republican vote, +0.88 pp turnout, and childhood is ages 4-18, not "before age 18". The earlier figures presumably
    come from a different version's abstract; I could not confirm that from the file on disk. Quote the pp figures.

- **Checks or analyses it suggests for us.**
  - Placebo days: run the identical 09h contrast and DiD for 9 and 11 November (and 8 and 12 where the weekday type
    matches), and report a joint test, as they do for 2, 3, 5 and 6 July.
  - Calendar handling: they move the treatment to 5 July when the 4th is a Sunday. Our analogue is to check how the
    estimate behaves by day of week. By my calendar arithmetic (verify against the data), 10 November fell on Tue 2020,
    Wed 2021, Thu 2022, Fri 2023 and Sun 2024, so one of five years is a weekend with a different 09h traffic regime.
    Report with and without 2024.
  - Rain enters our design differently: it is a direct confound of speed, not a participation shifter. Their
    covariate-balance test suggests the simple analogue: show that rain and temperature on 10 November are not unusual
    relative to control dates, year by year.
  - State the lower bound formally in their style: if observed speed excludes vehicles below 1 km/h, the measured
    contrast D_obs satisfies |D_obs| <= |D_true| under stated conditions. Whether the conditions hold depends on the
    unknown averaging method, which is our problem, not theirs.

---

### dinas2024 - Dinas, Martinez and Valentim (2024), Social Norm Change, Political Symbols, and Expression of Stigmatized Preferences

- **Question and setting.** Why did displays of the Spanish flag rise after the 1 October 2017 Catalan referendum
  ("O-1")? The claim is that the rise reflects "a change in norms rather than in preferences" (p. 1): the flag was
  stigmatized by its association with Francoism, and first-movers' displays lowered the perceived cost for others.

- **Data and method.**
  - *How street displays are measured.* A random sample of 315 Madrid streets was walked and every flag on a building
    facade was coded, 8 January to 13 March 2019. The same streets were coded back in time with Google Street View:
    eight time points before O-1 and three after. Flags on public buildings are removed. Non-national flags are kept
    for a placebo. The Francoist flag counts as national; the Republican flag does not (p. 6 and fn. 2). Outcomes:
    flags per street, log flags, and a dummy for any flag (p. 7).
  - Measurement validity: the fieldwork count sits almost exactly on the linear interpolation between the adjacent
    Street View dates (p. 7; Fig. 2, p. 8). The number of streets observable in Street View varies a lot by year
    (n = 52 to 293 in Fig. 2, p. 8).
  - Design 1: pre/post within Madrid with street-clustered SEs, with and without linear and quadratic trends (p. 7).
  - Design 2: DiD with Lisbon and Athens, same sampling and coding; two common pre-periods (2008-9, 2014-15) against
    the 2019 fieldwork; street and period FE (p. 6). The authors say explicitly this is not a most-similar-case
    counterfactual, only a complementary control (p. 6). Placebo: 2014-15 treated as the post period (p. 8).
  - Mechanism: face-to-face survey of a representative Madrid sample, 11-28 June 2019, with all flags in each
    respondent's street coded on 13-26 July 2019, adding about 400 streets (p. 7 and fn. 4). Table 1 has 943
    observations (p. 12).
  - Exposure: flags in the respondent's own street, and log distance from home to the nearest flag (pp. 8-9).
  - Norm perception follows Bicchieri: first-order belief (is a balcony flag appropriate?) and second-order belief (do
    more than half of your neighbours think so?) (p. 9).
  - Private versus public preference: two explicit Franco items versus a list experiment item on Franco; analyses
    exclude respondents who themselves hang a flag, to separate exposure from ownership (pp. 9-10, fn. 14).
  - Clustering test: mean nearest-neighbour distance between flags within a street, compared with 100 simulations per
    street that place the same number of flags at random over the street's house numbers; regression of distance on a
    "real" dummy with street FE (pp. 13-14).

- **Main findings.**
  - Before O-1 there were almost no flags: baseline 0.16 per street. After, about three more per street, roughly a
    19-fold increase; the share of streets with at least one flag went from under 5% to about 50% (p. 7). In household
    terms about one flag per 94 households, which the authors call a lower bound (p. 7).
  - DiD: +1.6 flags per street against Athens, +3.6 against Lisbon; +67 pp in the any-flag dummy against Lisbon and
    about half that against Athens; pre-period placebo effects negligible (pp. 7-8). Non-national flags also rose a
    little (p. 8).
  - Earlier spikes were short-lived: the 2012 European Championship (fn. 5, p. 7; Fig. 2 p. 8) and the 2010 World Cup,
    after which flags returned to the previous level and reported attachment to the flag did not rise (pp. 3, 18).
    The authors' explanation: a celebratory flag has an innocent interpretation, so it does not signal a
    counter-normative preference.
  - Exposure raises both first- and second-order appropriateness beliefs (p. 9; Fig. 5, p. 11). The paper gives these
    only graphically; I could not extract point estimates from the text.
  - Exposure raises explicit pro-Franco answers but not the list-experiment answer. In streets without flags,
    agreement with the pro-Franco item is 11% lower when asked explicitly than implicitly; in streets with flags it is
    7% higher (p. 11). The authors call this suggestive.
  - Who hangs a flag: left-right self-placement 0.0442 (SE 0.0086) per scale point; it loses significance once Franco
    attitudes enter (Franco human-rights item 0.0451, SE 0.0138). Attitudes to Catalans and salience of territorial
    integrity do not predict hanging (Table 1, p. 12).
  - Neighbourhoods that voted more for the right before O-1 saw a larger increase in flags (0.042, SE 0.02), which
    the authors concede is also compatible with a true-preference account (p. 12).
  - Exposure makes non-left respondents more willing to state pro-Franco views and produces a backlash among the left
    (p. 13; Fig. 6, p. 12).
  - Clustering: observed nearest-flag distance is 3.2 street numbers smaller than simulated (Table 2: -3.225, SE 0.529;
    simulated mean 7.91), about 40% less; in metres -33.2 (SE 7.2) against 81.6, also about 40% (pp. 13-15). National
    flags cluster more than other flags, which the authors use against a pure imitation account, and survey pairs
    show no within-street sorting on demographics or attitudes (p. 14).
  - Private preferences did not move with flags: parishes with more flags show no increase in right-wing vote share
    (p. 15).
  - Displays fell again after 2018 despite stronger elite mobilisation in 2019 (p. 17; Fig. 2, p. 8).

- **Usable for our paper.**
  - *Literature / Results-Discussion.* The definition of a social norm the authors adopt from Bicchieri (p. 3): a rule
    followed on condition that one believes enough others follow it (empirical expectations) and that enough others
    think it should be followed or would sanction deviation (normative expectations). This is the cleanest statement
    of what "norm-driven" should mean in our text. A driver stopping at 09:05 plausibly satisfies both conditions; our
    data can speak to neither directly.
  - *Introduction / Literature.* Precedent for treating a countable, publicly visible act in the street, aggregated
    over small spatial units and tracked over time from an administrative or commercial image archive, as a measure of
    public expression of national sentiment (pp. 2, 6-7).
  - *Results-Discussion (support).* Public expression responds to perceived acceptability and to what neighbours
    visibly do, and it clusters in space beyond what sorting explains (pp. 9, 13-14). That supports describing the
    stop as participation in a visible, mutually observed practice.
  - *Results-Discussion (caution).* The central result is that public behaviour moved while private preferences did
    not (pp. 10-11, 15). The same logic applied to us: the size of the slowdown tells us about the strength of the
    norm in public, not about how many drivers privately revere Ataturk. The paper's Kuran-style model (p. 11) makes
    the mechanism explicit: people trade off integrity utility against reputational utility.
  - *Results-Discussion.* The contingency point (pp. 4, 17-18): a symbol only signals a preference when no innocent
    interpretation is available. At the level of the individual driver, a stop at 09:05 has an innocent
    interpretation that flags lack: the car in front stopped.
  - *Robustness.* Placebo outcome (non-national flags), placebo period (2014-15 as fake post), and a
    measurement-continuity check across two data sources (pp. 7-8).
  - *Method.* They use the logged outcome because DiD in levels is sensitive to functional form when treated and
    control baselines differ (p. 7). Same reason our contrast is in logs across speed classes.

- **Caveats.**
  - **Direction of the norm is reversed relative to our case.** In Madrid the flag was the *counter-normative* act
    that became acceptable. On 10 November stopping is the *normative* act and driving on is the deviation. What
    transfers is the mechanism (behaviour conditional on perceived norm), not the story of first-movers eroding a
    stigma. If anything, the paper's logic implies that compliance with an established norm can overstate private
    agreement.
  - Flags are placed by residents at fixed addresses, at leisure, and stay up for weeks or months. A stop is a
    one-to-two-minute act by people passing through. The paper's reference group is the street of residence (pp. 8-9);
    drivers in a cell are not its residents.
  - The mechanism evidence is cross-sectional (survey 20 months after O-1), with exposure measured at the street of
    residence. Sorting is addressed by tests, not by design. The list experiment item differs in wording from the
    explicit items, which the authors acknowledge prevents comparing levels (p. 10).
  - Athens and Lisbon are admitted not to be proper counterfactuals (p. 6); the DiD range (1.6 to 3.6) is wide.
  - Earlier notes: `notes/commemoration_turkey.md` says displays rose "to more than three per street". The paper says
    an increase of about three, from a base of 0.16 (p. 7); only the October 2018 Street View point exceeds three
    (Fig. 2, p. 8). Write "about three". The same note calls flag display "costless-but-normed". In this paper the
    display was costly in reputation; that is the point of the paper.
  - `review.md` marks this entry "methods not verified from full text". They are now verified as described above.

- **Checks or analyses it suggests for us.**
  - Placebo outcome in their spirit: apply the identical estimator to an hour on 10 November that has no ritual
    content (for example the 14h contrast against 13h and 15h), and to 09h on the adjacent days.
  - Fake-treatment period: assign "treatment" to one of the control dates and re-estimate, which our randomization
    inference already does implicitly; report the placebo estimates themselves, not only the p-value.
  - Heterogeneity by pre-determined district politics (vote shares), reported as descriptive only, with their own
    caveat that it cannot separate preference from norm (p. 12), plus ours that cell traffic is not cell residents.
  - Continuity across sources: they show the fieldwork count lies on the Street View trend. Our hourly cell data end
    in January 2025 and the 5-minute index covers October-November 2026, so there is no overlapping date. The
    feasible version is to aggregate the 2026 5-minute dip to an hourly contrast and compare its size with the hourly
    estimates.
  - Year-by-year estimates: their series shows displays peaking and then receding (p. 8). With five years we can only
    describe, not test, a trend.

---

### parravano2015 - Parravano, Noguera, Hermida and Tena-Sanchez (2015), Secessionist flags in Barcelona

- **Question and setting.** Among people who already favour a Catalan referendum, does the decision to hang a flag on
  the balcony depend on how many neighbours do so? Direct observation in Barcelona, July and September-December 2013
  (pp. 2-3).

- **Data and method.**
  - *Study 1 (electoral-district scale).* Observers counted every Catalan flag (senyera or estelada), one per household,
    private dwellings only, in a stratified random sample of 276 electoral districts, 26% of the city: 213,667
    households, 293,144 registered voters, 5,479 flags, during the second and third weeks of July 2013 (pp. 4, 6).
    Flag density is related to the 2012 vote share of five pro-referendum parties.
  - Benchmark without social influence: every pro-referendum voter hangs a flag with the same probability
    p_u = (N_F/N_H)/(N_SV/N_RE) = 0.06075, giving the line Y_u = 6.075 X (Y in percent of households, X = pro-referendum
    votes per registered elector). Social influence index I_SI = p_lf/(100 p_u) - 1, where p_lf is the slope of a
    linear fit of Y on X (p. 7). A simulated distribution places flags at random with probability p_u (p. 9).
  - *Study 2 (balcony scale).* 82 block facades in 16 areas chosen in a 2x2 design (flag density above/below average;
    wide/narrow street), 4,817 households, recorded daily on facade templates from 4 to 18 September 2013 (the national
    day, the Diada, is 11 September), plus 19 November and 20 December: 17 observations per block (p. 4).
  - Clustering index (eq. 3-4, p. 18): C_obs(k,t) = (lambda_ran(k,t) - lambda_obs(k,t)) / sigma_ran(k,t), where lambda
    is the mean nearest-neighbour distance between flags on facade k on day t, and lambda_ran, sigma_ran are the mean
    and SD over 10,000 random placements of the same number of flags on a facade of the same shape. Computable in 1,040
    of 1,394 block-days (those with at least two flags).
  - No regression, no standard errors, no formal test statistics. Evidence is comparison with random benchmarks.

- **Main findings.**
  - Only 2.6% of households displayed a flag, against 42.2% pro-referendum vote per elector (pp. 6-7). The authors
    stress that hanging is costlier than not hanging and that staying anonymous is the default even for supporters
    (p. 6).
  - Correlation of flag density with vote share r = 0.64, with large dispersion at given vote share (mean relative
    dispersion 0.58) (p. 7).
  - Non-linearity: only 111 of 276 districts lie above the uniform-probability line; density is below the line where
    supporters are a minority and above it where they are a clear majority (pp. 7-8). Reported I_SI = 0.81 (p. 7).
  - The pattern holds within income halves (I_SI = 1.15 and 1.60), which the authors use against an income-homophily
    explanation (p. 9).
  - Excess of extremes: observed median density 2.20% against 2.56% simulated; 9 districts with zero flags, which the
    random benchmark cannot produce (pp. 9, 11). In study 2, 20 of 82 facades had zero flags on at least one day, 9
    never had one. The authors read the excess zeros as inhibition against being the first to display (p. 22).
  - Dynamics around the national day: 306 households had a flag on 4 September (long-term flaggers), declining 24% over 103
    days; 612 hung one for the first time later, of which 582 are attributed to the Diada, declining 70% (pp. 12-14).
    Fitted time scales: growth before the Diada about 2 days, decay after about 14 days, then about a year (p. 14).
    The probability that a supporter displays rose from 12.7% to 34.3% in the week before the Diada and fell to 16.9%
    three months later (p. 14).
  - 63 flags appeared only on 11 September and came down the next day. The authors note that these need not express
    support for secession, because Catalans hung a flag that day long before the dispute (p. 14).
  - Supporters in low-support environments hang later and remove earlier than those in high-support environments;
    both reach about 25% on the Diada itself (pp. 15-16).
  - Clustering: 63% of the 1,040 block-days have C_obs > 0 against 50% expected (p. 18), on every observation day
    (p. 20). The share with positive clustering rises about 10% from 4 to 9 September, falls about 20% over the next
    three days, and then recovers (p. 20). Near the Diada the non-linearity index is also low (p. 21).
  - The authors' summary rule: "do A if enough members of the relevant group do so" (p. 24).

- **Usable for our paper.**
  - *Introduction / Data.* An explicit argument for direct observation of behaviour over surveys, experiments and
    online traces: it avoids self-report bias and artificial settings (p. 2). The same argument justifies traffic data.
  - *Literature.* Conditions that make a behaviour a good candidate for social influence: easily observed by anyone
    nearby, binary, and with a clear meaning (p. 2). Stopping on the road at 09:05 has all three.
  - *Results-Discussion (support).* Field evidence that the public expression of a political or national attachment
    depends on the local share of others doing the same, with stimulation where they are a majority and inhibition
    where they are not (pp. 7, 22-23). This supports reading spatial variation in the slowdown as variation in local
    norm strength.
  - *Results-Discussion (caution).* Three points cut against an individual-preference reading:
    (i) most people who hold the preference do not display it (2.6% versus 42%), so absence of the act is not absence
    of the preference (pp. 6-7);
    (ii) the same preference produces different behaviour in different surroundings (pp. 7, 15-16);
    (iii) acts performed only on the national day are, in the authors' own words, not necessarily expressions of the
    political preference; they are tradition (p. 14).
  - *Results-Discussion.* Under a strong city-wide stimulus (the national day) the local-influence signatures weaken
    (pp. 20-21). A siren is a far stronger common stimulus than a national day. This is our extrapolation; the paper
    does not discuss sirens.
  - *Method.* Benchmarking an observed spatial pattern against many random placements that keep the count fixed
    (10,000 draws, p. 18) is the same inferential idea as our randomization inference, applied to space instead of
    dates.

- **Caveats.**
  - The paper cannot identify which influence mechanism operates, and says so (pp. 2, 24). Homophily and sorting are
    ruled out by argument (residential choices predate the conflict; neighbours' propensities are not observable when
    choosing a home), not by design (p. 23).
  - No inferential statistics; claims of significance are informal.
  - Arithmetic inconsistency: with the reported p_lf = 10.1 and 100 p_u = 6.075, I_SI = 10.1/6.075 - 1 = 0.66, not the
    reported 0.81 (p. 7). A slope of about 11.0 would give 0.81; the red line in Fig. 2 (p. 8) looks closer to 10.7.
    Do not quote 0.81 without this note. Also p. 9 describes both income subsets as lying under the median; the second must be
    above it.
  - Vote shares are attributed from the district to the facade (Fig. 7 caption p. 15; pp. 20-21), an ecological step.
  - Data are not public (p. 1).
  - **No analogue of physical blocking.** Flag clustering is evidence of social influence because one balcony does not
    force the next. On a road, one stopped car forces the cars behind it to stop. Spatial or temporal clustering of
    the slowdown in traffic data therefore cannot be read as social influence. This is the main limit on the analogy
    and it is ours to state; the paper has nothing on it.
  - Earlier notes: `notes/commemoration_turkey.md` describes flag display as "costless-but-normed" and
    "street-level" counts. The authors say the act is costly relative to anonymity (p. 6), and the units are electoral
    districts and block facades at balcony resolution, not streets. `review.md` glosses the paper as "a driver stops
    because the car ahead stops"; that conflates social influence with mechanical blocking and should be reworded.

- **Checks or analyses it suggests for us.**
  - Their non-linearity test, adapted: plot cell- or district-level slowdown on 10 November against a pre-determined
    proxy for local support and compare with a proportional benchmark. Interpret with care, since through-traffic
    breaks the link between cell and residents, and report as descriptive.
  - Their distribution test, adapted: compare the cross-cell distribution of the 09h contrast on 10 November with the
    same distribution on control dates. Under a uniform shift only the location moves. Excess mass in both tails
    (cells with near-total stops and cells with none) would be the analogue of their excess of zeros and of very dense
    districts (pp. 9, 11).
  - Their 2x2 by street width: split cells by road class, which our speed classes already approximate. The pilot
    result (effect in 30-70 km/h cells, none in congested cells) should be discussed as a physical-feasibility pattern
    before any norm interpretation.
  - Use the 2026 5-minute index to describe onset and recovery times around 09:05, in the spirit of their growth and
    decay time scales (p. 14). A fast symmetric dip is what a siren-coordinated stop predicts; a slow recovery would
    indicate queue discharge.

---

### skitka2005 - Skitka (2005), Patriotism or Nationalism? Post-September 11 flag display

- **Question and setting.** Was the wave of American flag display after 11 September 2001 an expression of patriotism
  (love of country, in-group solidarity), of nationalism (uncritical support for authority, out-group hostility), or
  both (the overkill hypothesis)? United States, survey fielded 28 December 2001 to 14 January 2002 (pp. 1, 4-5).

- **Data and method.**
  - National probability sample from the Knowledge Networks web panel, N = 605, 88% within-panel cooperation (p. 5).
  - *Flag display is self-reported, retrospectively, on a checklist*: flag at home, on the car, on clothing or
    jewellery. Two outcomes: any display, and number of ways (0-3) (p. 8). No observation of behaviour.
  - Predictors: nationalism (four right-wing authoritarianism items, alpha = .89), perceived threat (8 items,
    alpha = .92), change in feelings toward in-groups and out-groups since 9/11, a single item on feeling a surge of
    patriotism, counts of moral-outrage behaviours (0-4) and non-flag value-affirming behaviours such as giving blood
    or money (0-7) (pp. 5-8).
  - Analysis: correlations and standardized OLS on the full sample and by census region (pp. 9-12). Cross-sectional,
    no identification strategy.

- **Main findings.**
  - 74% reported at least one form of display; 25% reported all three (p. 8). Other surveys put display at 74-82%
    (p. 2).
  - Bivariate: display correlates with self-reported patriotism (r = .47; extent r = .52), value-affirming behaviours
    (.35; .40), in-group enhancement (.30; .36); with nationalism .05 (ns) for any display and .11 for extent; with
    out-group derogation .03 (ns) and .12 (Table 2, p. 9).
  - Standardized regression (Table 3, p. 11; checked against the PDF): self-reported patriotism .34 (extent) and .33
    (any); value-affirming behaviours .18 and .15; in-group enhancement .15 and .11; nationalism .05 (ns) and .08
    (p < .05); out-group derogation .00 and .08 (p < .05); education -.12 and -.14; income .13 and .14. R = .60 and .54.
  - Nationalism and patriotism correlate weakly (r = .18); in-group enhancement and out-group derogation are
    uncorrelated (pp. 13-14).
  - The pattern holds in all four regions; self-reported patriotism and value-affirming behaviour are the consistent
    predictors (pp. 12-13).
  - Display later fell to 56% after the Iraq war began, and the author speculates its meaning shifted; she concludes
    "what this meaning is in any given context seems likely to vary" (p. 14).

- **Usable for our paper.**
  - *Literature.* A mass symbolic behaviour after a national shock was tied to solidarity and value affirmation
    (the same cluster as giving blood) much more than to hostility or deference to authority (pp. 11, 14). This
    supports describing the 09:05 stop as civic or solidaristic participation without implying aggressive nationalism.
  - *Literature.* The patriotism/nationalism distinction itself (pp. 2-3), if we need vocabulary for what the stop does
    and does not express.
  - *Results-Discussion (caution).* The author names conformity and fear of being criticised as unpatriotic as
    explanations she did not measure (p. 15). The meaning of a display depends on context and can drift (p. 14).
  - *Introduction (scale).* A reference point for how widespread a national symbolic act can be: about three quarters
    of adults (pp. 2, 8). Self-reported, so not comparable to an observed rate.

- **Caveats.**
  - Not behavioural data. Our earlier note ("treats flag display as a behavioural indicator, N=605") should say
    self-reported retrospective display.
  - Purely correlational, and the main predictor is a single self-report item on patriotism measured in the same
    questionnaire. Shared method variance and social desirability are obvious concerns; the paper does not address
    them beyond noting the item correlates with value-affirming behaviours (p. 15).
  - Nationalism and out-group derogation are uncorrelated with any display in the bivariate table (p. 10), but in the
    regression both carry small significant coefficients on any display (.08; Table 3, p. 11). The text mentions this
    for nationalism only. The accurate summary is that they are much weaker predictors, not that they are unrelated.
  - Table 2 lists a mean of 1.26 (SD 0.44) for a display variable the note says is coded 0/1 (p. 9). The coding is
    unclear; do not reuse that mean.
  - Voluntary display after an attack is not a recurring, scheduled ritual. Nothing here concerns commemoration days.

- **Checks or analyses it suggests for us.**
  - None quantitative. For interpretation: avoid the word "nationalism" for what the stop reveals unless we define it;
    "national attachment" or "civic ritual participation" matches the evidence better.
  - If any existing Turkish survey asks about stopping on 10 November, the patriotism-versus-conformity question she
    leaves open (p. 15) is the one to look for. I have not checked whether such a survey exists.

---

### carter2011 - Carter, Ferguson and Hassin (2011), A single exposure to the American flag

- **Question and setting.** Does brief incidental exposure to the national flag shift political attitudes and voting,
  and for how long? Two experiments with American adults, 2008-2010 (pp. 1-2).

- **Data and method.**
  - Pilot (n = 51): which party displays the flag more; would a flag affect your vote (p. 2).
  - Experiment 1: online panel recruited through social-network advertising, four sessions over 8 months. 235
    participants in non-competitive states were randomized; a 72 x 45 pixel flag appeared in the corner of one survey
    page in Session 2 (11 October to 3 November 2008) for the treated group. Session 2 n = 197, Session 3 (post
    election) n = 191, Session 4 (July 2009) n = 71, i.e. 37.2% of Session 3; 8 fast responders excluded
    (pp. 2-3). Outcomes: voting intention, warmth, IATs, beliefs, reported vote, later evaluations.
  - Experiment 2 (spring 2010): lab, 70 participants, 66 analysed; photographs of buildings with or without flags
    (pp. 5-6).
  - Analysis: t-tests and one chi-square.

- **Main findings.**
  - Pilot: participants saw Republicans as the party that displays the flag more; 90.2% believed a flag "would not
    influence their behavior" (pp. 1-2).
  - Session 2: voting intention toward McCain t(181) = 2.02, p = .04, d = 0.30; explicit warmth p = .03, d = 0.35;
    IAT p < .05, d = 0.31; beliefs p = .07 (pp. 3-4).
  - Reported vote: McCain 27.2% in the flag condition versus 16.5% in control, chi-square(1, N = 166) = 2.81,
    p < .05 one-tailed; no direct effect once voting intention is controlled (p = .25) (pp. 4-5).
  - Eight months later (n = 71): lower approval of Obama d = 0.44; warmth d = 0.80; beliefs d = 0.60 (p. 5).
  - Experiment 2: more conservative beliefs, 3.10 versus 2.65, t(64) = -2.04, p < .05 (p. 6).
  - Effects not moderated by ideology; the authors propose a shift toward the perceived prototypical citizen (pp. 6-7).

- **Usable for our paper.**
  - *Literature (one sentence at most).* National symbols are claimed to influence political judgment without people
    being aware of it (pp. 1-2, 7). The 90.2% figure could support a remark that self-reports about symbolic
    influence are unreliable, which is a reason to prefer behavioural measures.
  - Nothing for Data, Method, Robustness or Results.

- **Caveats.**
  - The paper is about the effect of seeing a symbol on attitudes. It does not measure national attachment, expression
    of it, or participation in anything. `review.md` rates it "peripheral"; I agree.
  - Evidence is thin by the paper's own numbers: p-values of .04, .03, .07 at Session 2; the vote result is
    chi-square = 2.81, significant only one-tailed; the 8-month result rests on 71 of 191 participants; larger effects
    after attrition, which the authors discuss but cannot resolve (p. 5).
  - Not from the paper and not checked here: I recall that the flag-priming effect of Experiment 2 was among the
    effects that did not replicate in a large multi-lab replication project (Many Labs, 2014). Verify before citing
    the paper for any substantive claim. If confirmed, drop it or cite it only alongside the replication.
  - The symbol's partisan valence is specific to the United States (p. 6). No inference to the Turkish flag or to
    Ataturk imagery is licensed.

- **Checks or analyses it suggests for us.** None.

---

## What supports, and what cautions against, the reading we want

Reading to be assessed: the 09:05 slowdown is revealed, norm-driven participation in a civil ritual.

**Supports**

- Public, visible, binary acts with a clear meaning are established objects of measurement for expressed national
  attachment (dinas2024 pp. 2, 6-7; parravano2015 p. 2).
- Directly observed behaviour is argued to be preferable to self-report (parravano2015 p. 2), and people misjudge how
  symbols affect them (carter2011 p. 2).
- Such acts depend on what others nearby visibly do: clustering 40% tighter than random in Madrid (dinas2024
  pp. 13-15), 63% of block-days positively clustered in Barcelona (parravano2015 p. 18), stimulation and inhibition by
  local majority (parravano2015 pp. 7, 22-23). "Norm-driven" has a precise definition available (dinas2024 p. 3).
- National days are theorised as rituals that reconfirm commitments and create common knowledge (madestam2011 p. 7),
  and shared experiences have measurable downstream effects (depetris2020 pp. 14-15, 26; madestam2011 pp. 19-21).
- Mass symbolic acts align with solidarity and value affirmation more than with out-group hostility (skitka2005 p. 11).
- Participation in a national ritual has been hard to observe; the leading holiday paper had no attendance data
  (madestam2011 p. 4).

**Cautions**

- Public behaviour can change with no change in private preference (dinas2024 pp. 10-11, 15). Behaviour reveals the
  norm as perceived, not individual attachment.
- Most holders of a preference do not perform the act (parravano2015 pp. 6-7), and acts done on the national day may be
  tradition without the preference (parravano2015 p. 14). Neither stopping nor driving on maps cleanly to a preference.
- Conformity and fear of criticism are named and unmeasured (skitka2005 p. 15); meaning drifts with political context
  (skitka2005 p. 14; dinas2024 pp. 17-18).
- In the flag studies the norm ran against the act (dinas2024) or the act was costly and rare (parravano2015). On
  10 November the act is the norm. The mechanism transfers; the first-mover narrative does not.
- Flags belong to residents at known addresses; vehicles in a cell are passing through. Spatial heterogeneity cannot be
  tied to local residents' politics without an ecological leap (already present in parravano2015 p. 20).
- A stopped car physically stops the cars behind. None of the six papers has anything comparable. In traffic data,
  clustering and non-linearity are expected mechanically and cannot identify social influence.
- None of the six papers concerns moments of silence, sirens or traffic.

## Cross-paper synthesis

1. What we can defend is "public participation in a civic ritual, shaped by a shared norm". What we cannot defend from this literature is "revealed individual preference" or "revealed nationalism"; dinas2024 and parravano2015 are evidence against that step, not for it.
2. Use the Bicchieri definition quoted in dinas2024 (p. 3) to define norm-driven behaviour once, then state plainly that our data observe compliance and not the beliefs behind it.
3. Our contribution relative to this group is measurement: madestam2011 had no participation data (p. 4), depetris2020 and skitka2005 rely on surveys, and the two flag papers measure a slow, residential act. A synchronized one-minute act measured city-wide is new, to the extent of these six papers.
4. The analogy "a driver stops because others stop" must distinguish social influence (flags) from mechanical blocking (queues). Our aggregate effect contains a physical multiplier; say so, and do not interpret clustering.
5. The pilot pattern (effect at 30-70 km/h, none in congested cells) should first be read as physical feasibility of stopping and measurement (the 1 km/h floor), and only then, cautiously, as participation.
6. Placebos are the most transferable design element: adjacent days with a joint test (madestam2011), a look-alike low-stakes event (depetris2020), a placebo outcome and a fake treatment period (dinas2024).
7. Multiple testing across speed classes should be handled with FDR-adjusted p-values as in depetris2020 (p. 11), reported next to the randomization p-values.
8. Benchmarking against random placement with counts held fixed (parravano2015 p. 18; dinas2024 p. 13) is the same logic as our randomization inference; cite them when explaining it to a social-science audience.
9. Calendar and context matter: holiday-on-Sunday handling (madestam2011 fn. 13), displays that rise and recede with politics (dinas2024 p. 8; skitka2005 p. 14). Report by year and flag the weekend year; treat any trend as descriptive.
10. Corrections to carry into the paper and earlier notes: madestam2011 effects are 0.61, 0.85 and 0.88 percentage points, not "2%, 4%, 0.9%"; dinas2024 is "about three flags per street"; flag display is not "costless"; skitka2005 is self-report; parravano2015's I_SI = 0.81 does not follow from its own inputs; carter2011 should be cited sparingly if at all.
