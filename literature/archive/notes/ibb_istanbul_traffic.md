> Raw research notes (2026-11-10). Works listed in `../excluded.csv` (paywalled, no copy on hand) must not be cited; the citable set is `../references.csv`.

# İBB Open Traffic Data and the Quantitative Istanbul Traffic Literature

Scope: prior uses of the İBB "Saatlik Trafik Yoğunluk Veri Seti" (hourly traffic density data set), how it is constructed, and Istanbul traffic studies with event-type designs. This supports a paper estimating the delay caused by the 10 November 09:05 Atatürk remembrance siren.

Verification legend: **[V]** means I opened the primary source (full text or publisher/repository landing page) and confirmed authors, year, venue and DOI. **[P]** means it was partially verified, from a repository record or search snippet, and the full text was not read. **[U]** means unverified: it appeared only in search results or the page failed to load. Do not cite [U] items without checking them first.

## Which papers, theses, DergiPark articles, conference papers and Kaggle/GitHub projects use the İBB hourly traffic density data set, and what did they find about its properties?

### Takeaway
The data set has a thin academic footprint. I found two peer-reviewed DergiPark articles that clearly use it, both forecasting exercises at a single location. Neither uses it in a causal or event design, and neither documents how it is built. The other uses are student and hobby GitHub/Kaggle projects. No YÖK thesis surfaced. Our paper would likely be the first event-study use of the data set.

### Cited Findings
**Peer-reviewed uses of the hourly geohash data set**
- **[V] Utku, A. (2023).** "Derin Öğrenme Tabanlı Trafik Yoğunluğu Tahmini: İstanbul İçin Bir Vaka Çalışması" [Deep-learning-based traffic density prediction: a case study for Istanbul]. *Düzce Üniversitesi Bilim ve Teknoloji Dergisi* 11: 1584–1598. DOI: 10.29130/dubited.1139534. — [PDF](https://dergipark.org.tr/tr/download/article-file/2521442)
  - It uses January–May 2021 of the İBB hourly data set, with the columns Date_Time, Longitude, Latitude, Geohash, Min/Max/Average_Speed and Number_of_Vehicles. It cites the data set as data.ibb.gov.tr/dataset/hourly-traffic-density-data-set, accessed 25 May 2022.
  - It reports **2,321 distinct locations (geohashes)** in that period.
  - It picks the cell with the highest vehicle count, which it identifies as the Başakşehir Mahmutbey junction (TEM / Basın Ekspres / Kuzey Marmara). That cell has **2,900 hourly rows over Jan–May 2021**, out of roughly 3,600 possible hours. This implies hourly gaps even in the busiest cell. The missing-hour count is my own arithmetic.
  - It describes Number_of_Vehicles loosely as the "hourly number of vehicles passing a location". That reading treats the column as a flow count, which the official dictionary does not support (see the construction section).
  - Its LSTM reaches R² ≈ 0.90 for vehicle count (MAE ≈ 71 vehicles) and for average speed.
  - **Relation to our design:** it is citable as a prior use of the data set and documents its spatial coverage (around 2,300 cells in 2021). It gives no causal design and no construction details.
- **[V] Özkurt, C., Kala, A., Konuk, K., Saylam, A. N. (2025).** "Bulanık Mantık Destekli Trafik Yoğunluğu Tahmini" [Fuzzy-logic-based traffic congestion prediction]. *Harran Üniversitesi Mühendislik Dergisi* 10(3): 184–197. DOI: 10.46578/humder.1680871. — [PDF](https://dergipark.org.tr/en/download/article-file/4793568)
  - It uses the İBB hourly data set for 2022, aggregated to **8,539 hourly records** against the 8,760 expected. That is about 2.5% missing hours, which the authors judge non-systematic.
  - They merge the hourly data with daily Meteostat weather data and fit a Mamdani fuzzy model.
  - Their sample rows are revealing. At 01-01-2022 03:00 the row shows min = max = avg = 110 km/h with **Number of vehicles = 1**, and the 02:00 row shows 9 vehicles. Night-time cells can therefore rest on one or a few probe vehicles.
  - **Relation to our design:** this is direct evidence of small-sample noise in low-count cell-hours. It supports weighting by NUMBER_OF_VEHICLES or applying a minimum-count filter. It also supports reporting the missing-hour rate.

**Related İBB-data papers (not the geohash set, but useful)**
- **[V] Takak, I., Görmez, H., Türkmen, H. İ., Güvensan, M. A. (2021).** "Kısa, Orta ve Uzun Vadeli Trafik Akış Hızı Tahmini ve Görselleştirilme Aracı" [Short-, medium- and long-term traffic flow speed prediction and visualization tool]. *Int. J. Adv. Eng. Pure Sci.* 33(4): 568–580. DOI: 10.7240/jeps.883711. — [PDF](https://dergipark.org.tr/tr/download/article-file/1590162)
  - It uses İBB speed data for 2017 from about **7,000 sensors sampled once per minute**, obtained directly from İBB rather than from the open portal.
  - Regression forecasts reach up to one week ahead with a MAPE of 23.99%. The paper mentions gaps caused by sensor failures.
  - **Relation:** shows that İBB holds minute-level sensor speeds that researchers can obtain on request. That is the natural sub-hour complement to our hourly data.
- **[V] Alcan, U., Kaçar, F. (2022).** "Impact Analysis of COVID-19 Pandemic on Istanbul Traffic with Big Data Tools." *Electrica* 22(2): 226–236. DOI: 10.54614/electrica.2022.210005. — [AVESİS record](https://avesis.iuc.edu.tr/yayin/983c66b0-2a3e-4b85-b87d-c9da9f2a203c/impact-analysis-of-covid-19-pandemic-on-istanbul-traffic-with-big-data-tools); [TR Dizin](https://search.trdizin.gov.tr/yayin/detay/529359)
  - It uses İBB's openly published **hourly traffic index** for 2020, which is a separate data set from the geohash set, together with a curfew-time data set. It processes them with Spark, Elasticsearch and Kibana.
  - I read only the record and abstract. Its quantitative findings are not verified.
  - **Relation:** it is the closest prior İBB-open-data event analysis (curfews). It uses the city-wide index, not geohash cells.
- **[P] Olug, E., Kaya, K., Tugay, R., Gunduz Oguducu, S. (2024).** "IBB Traffic Graph Data: Benchmarking and Road Traffic Prediction Model." arXiv:2408.01016. — [arXiv](https://arxiv.org/abs/2408.01016)
  - It builds a graph benchmark from İBB sensor data at **2,451 locations**. The search summary says it covers four years at hourly frequency, but I did not confirm that from the abstract.
  - **Relation:** a possible alternative or validation source built on fixed sensors.
- **[P] Tanberk, S., Can, M. (2022/2023).** "Smart Journey in Istanbul: A Mobile Application in Smart Cities for Traffic Estimation by Harnessing Time Series." arXiv:2212.09448. The listing links DOI 10.1109/ASYU58738.2023.10296669, an ASYU 2023 IEEE conference paper. — [arXiv](https://arxiv.org/abs/2212.09448)
  - It forecasts Istanbul traffic load with weather data using LSTM, Transformer and XGBoost. The abstract does not say which İBB data set it uses. A search summary says it aggregates to district level, which I did not confirm.

**GitHub / Kaggle (non-peer-reviewed; cite only as illustrations of use, if at all)**
- **[P] MervePoslu/istanbul_traffic_data_visualization.** An R visualization of the March 2021 file. Its README defines NUMBER_OF_VEHICLES as distinct vehicles in a geohash in a given hour. — [GitHub](https://github.com/MervePoslu/istanbul_traffic_data_visualization)
- **[P] Busraayazicioglu/TrafikYogunluguAnalizi.** A Keras density-prediction project. — [GitHub](https://github.com/Busraayazicioglu/TrafikYogunluguAnalizi)
- **[U] SaynaSarvar/city-comes-into-focus.** A map of evening traffic built from the October 2024 file. The search snippet says geohash-6 is about 0.6 × 0.9 km and the file has 744 hours. The repo returned HTTP 404 when fetched. — [GitHub](https://github.com/SaynaSarvar/city-comes-into-focus)
- **[U] quangtrananhyeuem/Data_Repair_Steps_in_Next_Hour_Traffic_Forecasting.** The snippet describes an "ICIIT 2027 submission" using 36 monthly files from 2022–2024 (58.4 million records) and the 150 busiest cells, with a holiday analysis. It is unreviewed and was not opened. — [GitHub](https://github.com/quangtrananhyeuem/Data_Repair_Steps_in_Next_Hour_Traffic_Forecasting)
- **[P] Kaggle mirrors.** "Istanbul Municipality Traffic Density Data 2024Aug" ([Kaggle](https://www.kaggle.com/datasets/muratsahin1992/istanbul-municipality-traffic-density-data-2024aug)) and the notebook "Hourly Traffic Data Analysis for ISTANBUL City" ([Kaggle](https://www.kaggle.com/code/batuhan007/hourly-traffic-data-anaiysis-for-istanbul-city-1m)). There are also "Istanbul Traffic Density Data 2019" uploads ([merouz](https://www.kaggle.com/datasets/merouz/istanbul-traffic-density-data-2019), [smhrcn](https://www.kaggle.com/datasets/smhrcn/istanbul-traffic-density-data-2019)). The portal starts in 2020, so the provenance of the 2019 files is unclear and should be checked.
- **[U] LinkedIn series "From Chaos to Clarity: Unraveling Istanbul's Traffic Congestion Enigma" (J. Antony).** It reports that religious holidays (Ramazan and Kurban Bayramı) have the lowest median density over 2020–2023 and that COVID restrictions cut density. This is a blog, not citable as evidence. — [Part 3](https://www.linkedin.com/pulse/from-chaos-clarity-unraveling-istanbuls-traffic-enigma-joseph-antony-1c)

### Inferences
- The two peer-reviewed uses treat NUMBER_OF_VEHICLES as if it were a traffic count. Our paper should state plainly that it counts distinct sampled probe vehicles, and set out what follows from that (see the construction section).
- The missing hours (Utku's busiest cell has about 2,900 of about 3,600 hours; Özkurt et al. report 2.5% missing) imply that cell-hours are *absent* rather than zero-filled when no probe is observed. The panel is unbalanced, and low-traffic cells drop out at night.
- No study I found uses the data set for a causal, event-study or difference-in-differences design. That is a novelty claim for us, though it should be phrased carefully because searching was not exhaustive.

### Gaps
- No YÖK Ulusal Tez Merkezi thesis using the data set was found. The YÖK search interface is not reachable by web search, so a manual search there for "trafik yoğunluk İBB", "geohash" and "açık veri trafik" is still needed.
- I did not find English-language international journal articles (Elsevier, Springer, MDPI) that use the geohash data set. Google Scholar was not directly queryable.
- The full texts of Alcan & Kaçar (2022) and Olug et al. (2024) were not read.

## What do İBB, UYM and data.ibb.gov.tr say about how the data set is constructed?

### Takeaway
Official documentation is minimal. The portal says Istanbul is split into equal geographic parts (geohash-6) and that each cell-hour reports the number of *distinct* ("tekil") vehicles and their average, maximum and minimum speeds. It does not name the probe provider. It does not say how the average is computed (vehicle-weighted or not, space-mean or time-mean), what speed thresholds apply, or whether zero or stationary speeds are excluded. The best indirect evidence on the source is İBB's own description of its traffic-speed pipeline: fleet "araç takip" GPS data from **8 traffic data providers**, plus İBB Yol Gösteren app users, plus radar and Bluetooth sensors. The data set is very probably built from that probe stream, but İBB has not said so for this data set.

### Cited Findings
**Portal metadata (primary)**
- **Title:** "Saatlik Trafik Yoğunluk Veri Seti" / "Hourly Traffic Density Data Set".
- **Publisher:** İBB Ulaşım Dairesi Başkanlığı. Group: Mobilite. Licence: İBB Açık Veri Lisansı. Format: CSV.
- **Coverage:** monthly files from **January 2020 to January 2025** (61 resources). The data set was created 9 Nov 2020 and last updated 16 Apr 2025. The page says updates "will be made at a later date".
- **Download pattern:** `.../resource/<id>/download/traffic_density_YYYYMM.csv`.
- Source: [data.ibb.gov.tr dataset page](https://data.ibb.gov.tr/dataset/hourly-traffic-density-data-set)
- **Resource description:** each file holds, for Istanbul "geographically divided into equal parts", the number of individual vehicles in each part and their average, maximum and minimum speeds. The Turkish text reads "tekil araçların sayısı, bu araçlara ait ortalama hız, maksimum hız ve minimum hızları". — [May 2021 resource page (EN)](https://data.ibb.gov.tr/en/dataset/hourly-traffic-density-data-set/resource/00d72836-d035-462d-a66e-408883216195); [Feb 2024 resource (TR)](https://data.istanbul/dataset/hourly-traffic-density-data-set/resource/601cd734-9a62-44e0-89e5-bbfc2161d389)

**Official data dictionary** (May 2021 resource page)

| Column | Type | Official definition |
|---|---|---|
| DATE_TIME | varchar | "YYYY-MM-DD HH24:MI:SS", with hourly breaks |
| LATITUDE / LONGITUDE | float8 | Coordinates. The Turkish label for LATITUDE wrongly says "Boylam" (longitude) |
| GEOHASH | varchar | Geohash of the coordinates, length 6 |
| MINIMUM_SPEED / MAXIMUM_SPEED / AVERAGE_SPEED | int4 | km/h for the geohash area in the given hour. Stored as integers, so values are rounded or truncated |
| NUMBER_OF_VEHICLES | int4 | "The number of different vehicles in the relevant geohash area in the given hour" |

Source: [resource page](https://data.ibb.gov.tr/en/dataset/hourly-traffic-density-data-set/resource/00d72836-d035-462d-a66e-408883216195). That page has no statement on the data source, the averaging method, speed thresholds or zero-speed handling.

**Open documentation request**
- An open data request on the portal titled "Saatlik Trafik Yoğunluk Veri Seti için veri sözlüğü (DATE_TIME, NUMBER_OF_VEHICLES) açıklaması" asks İBB to explain these two fields. It was posted about three weeks before 10 Nov 2026, the requester says it is for an academic study, and it has no İBB reply. This confirms that the meaning of the timestamp and of the count is publicly undocumented. — [data.ibb.gov.tr/datarequest](https://data.ibb.gov.tr/datarequest)
- A search snippet mentions a request to add February 2025 to September 2026. I did not confirm it on the listing page.

**İBB's probe and sensor pipeline (indirect, but primary İBB authorship)**
- **[V] Dilek, E., Kurt, Y., Öztürk, S., Erşahin, M., Özcan, Ö., Ünal, A.** "'İBB Yol Gösteren' ile Akıllı Hareketlilik" [Smart mobility with İBB Yol Gösteren]. Conference paper hosted by İBB UYM. The year and venue are not printed on the PDF; it describes the app launched in April 2017, so it is probably 2017–2018. — [uym.ibb.gov.tr PDF](https://uym.ibb.gov.tr/documents/library/IBBYolGosteren.pdf)
  - Speed data come from "8 farklı trafik veri sağlayıcısı" (8 different traffic data providers). One provider is the Yol Gösteren app's own users while driving. The others include speed and GPS positions from "farklı araç takip sistemleri" (different fleet-tracking systems).
  - İBB traffic measurement sensors (radar and Bluetooth) are also blended in.
  - Probe points are map-matched to the nearest road segment within roughly 40 m precision and treated as that segment's "mobile speed".
  - Speeds are pre-processed by server software and stored in a database.
  - The İBB **Trafik İndeksi** (congestion %) is computed from a blended average speed on the main arterials, using a method developed by Ulaşım Daire Başkanlığı engineers.
  - **No commercial provider is named.**
- **[P] UYM "Trafik Bilgilendirme" page.** It describes instantaneous density data sent to UYM by field traffic-measurement systems. — [uym.ibb.gov.tr](https://uym.ibb.gov.tr/hizmetler/trafik-bilgilendirme)
- **[P] Yıldırım & Çataltepe (2010, ITU).** They report that the İBB Traffic Control Center published averaged speeds from **327 RTMS sensors at about 1–2 minute intervals**. — [ITU PDF](https://web.itu.edu.tr/~cataltepe/pdf/2010_TBV_Trafik.pdf)
- **[V] Takak et al. (2021).** About 7,000 sensors with one-minute readings in 2017 (see the first section).

### Inferences
- **Probe source.** The word "tekil araç" (distinct vehicle), the distinct-vehicle counting, the min/max speed per cell, and single-vehicle cell-hours (count = 1 with min = max = avg in Özkurt et al.) all point to anonymised vehicle-level GPS probe data with persistent IDs, almost certainly the fleet-tracking and app probe stream described in the Yol Gösteren paper. Fixed sensors cannot identify distinct vehicles or produce min/max per vehicle in a geohash. This is an inference; İBB does not state it for this data set.
- **What NUMBER_OF_VEHICLES is.** It is a *sample size of probe vehicles*, not traffic volume. Its level depends on fleet penetration, which changes over time and differs by road type and by commercial vs private vehicles. For our design:
  - (a) use it as a precision weight and a minimum-count filter, not as a flow outcome;
  - (b) treat any siren-hour change in it with care, since stopped vehicles still report positions and may raise distinct-vehicle counts within an hour.
- **Zero speeds.** It is undocumented whether stationary pings (speed 0) are included. If MINIMUM_SPEED = 0 appears in congested cells, zeros are likely included. If the minimum is never below some threshold (e.g. 1–5 km/h), a filter is likely. **This is directly checkable in our raw files.** We should tabulate the distribution of MINIMUM_SPEED, and the share of zeros, by hour. If stopped vehicles are dropped, a one-minute full stop at 09:05 would be *understated* in AVERAGE_SPEED.
- **Averaging method.** It is unknown whether AVERAGE_SPEED averages pings (time-mean over GPS samples) or vehicles. Ping-weighting would over-represent slow or stopped vehicles, since they emit more pings per cell. That raises the measured siren effect relative to a vehicle-weighted average. This should be stated as a measurement caveat.
- **Timestamp convention.** It is undocumented whether DATE_TIME 09:00:00 marks the start of the hour (09:00–09:59, which would contain the 09:05 siren) or its end. That matters for our treatment window. A check: compare the morning-peak timing against the İBB hourly traffic index or TomTom.
- **Coverage window.** The data end in January 2025. The available 10 November events are therefore 2020 (COVID restrictions), 2021, 2022, 2023 and 2024. Check which weekday each fell on, since a weekend siren day changes the baseline.
- **Integer storage.** Speeds are integers, which caps resolution at 1 km/h. This is relevant for small effects in averaged cells.

### Gaps
- No public İBB statement names the probe provider(s) for this data set or the share of probes by source. Contacting İBB Ulaşım Dairesi Başkanlığı or the açık veri team, or filing a portal data request, is recommended.
- The averaging method, speed thresholds, zero-speed handling, the cell centroid used for LATITUDE/LONGITUDE, and the timestamp convention are all undocumented.
- The year and venue of the Yol Gösteren paper are unconfirmed. It is likely a Turkish national transport congress (e.g. Ulaşım Kongresi), but this is unverified.
- I found no news on a specific İBB commercial floating-car-data partnership (e.g. with TomTom, HERE, Yandex or Başarsoft). The search was limited.

## Which Istanbul traffic studies use event-type designs (COVID, Ramadan, openings, holidays, earthquakes, football, marathon closures), and how does Istanbul rank on TomTom and INRIX?

### Takeaway
Event-type quantitative work on Istanbul traffic is sparse. COVID-19 is the only event with several studies, using the İBB traffic index, RTMS sensors, bridge toll counts or surveys. I found **no peer-reviewed study** on Ramadan or iftar timing, the Avrasya Tunnel or Yavuz Sultan Selim Bridge openings, football matches, marathon closures or earthquakes that uses İBB, TomTom or Yandex speed data. Istanbul ranks at or near the top of global congestion indices, which is useful as motivation.

### Cited Findings
**COVID-19**
- **[V] Alcan & Kaçar (2022), Electrica.** Uses the İBB hourly traffic index for 2020 and curfew timings (see the first section). — [AVESİS](https://avesis.iuc.edu.tr/yayin/983c66b0-2a3e-4b85-b87d-c9da9f2a203c/impact-analysis-of-covid-19-pandemic-on-istanbul-traffic-with-big-data-tools)
- **[V] Ergin, M. E., Ozen, H., Ilıcalı, M. (2022).** "The Evaluation of the Impacts on Traffic of the Countermeasures on Pandemic in Istanbul." *Sustainable Civil Infrastructures* (Springer). DOI: 10.1007/978-3-030-79801-7_66. — [Ticaret Üniv. repository](https://acikerisim.ticaret.edu.tr/items/c7294975-b4d6-4199-bc44-072e47f6e237)
  - Data: a survey of about 150,000 respondents, RTMS sensors and electronic toll data.
  - Morning and evening peaks **did not shift** despite staggered working hours.
  - Weekday counts on both Bosphorus bridges were down about 14% in Nov 2020 vs Nov 2019.
  - Survey-estimated private car use rose 9%.
  - **Relation:** this is the Nov 2020 baseline context for our 2020 siren observation. Traffic was depressed that month, and curfews covered weekends and 21:00–05:00 on weekdays. A 09:05 weekday siren falls outside curfew hours.
- **[P] Energies 14(18): 5729 (2021).** "Evaluation of Air Quality Index by Spatial Analysis Depending on Vehicle Traffic during the COVID-19 Outbreak in Turkey." DOI: 10.3390/en14185729. A search snippet says it uses İBB traffic density and speed data and reports average traffic speed up by as much as 7% after lockdowns. The MDPI page returned 403, so authors and methods are not verified. — [MDPI](https://www.mdpi.com/1996-1073/14/18/5729)
- **[P] "The impacts of COVID-19 on travel behavior and initial perception of public transport measures in Istanbul"** (PMC8828301). A survey study, not speed data. Authors not verified. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8828301/)

**Ramadan / iftar, holidays, openings**
- No peer-reviewed Istanbul study found.
- **[P] News:** Türkiye Today reports that İBB's congestion map showed traffic falling to about 1% at iftar at the start of Ramadan. That is a news claim based on the İBB index and should be checked before use. — [Türkiye Today](https://www.turkiyetoday.com/turkiye/istanbuls-traffic-grinds-to-halt-as-ramadan-begins-in-one-of-worlds-most-congested-cities-126496/)
  - **Relation:** iftar is the clearest analogue in Istanbul of a *synchronized, scheduled, city-wide* behavioural shock in traffic. An iftar-hour event study in the same İBB data would be a natural placebo or validation exercise for our method.
- **Avrasya Tunnel (opened 20 Dec 2016):** only news, operator self-reports (e.g. the [Avrasya Tüneli 2023 Endeksi](https://www.avrasyatuneli.com/_assets/pdf/Avrasya-Tuneli-2023-Endeksi.pdf)) and a pre-opening critique by the Şehir Plancıları Odası ([Diken](https://www.diken.com.tr/?p=368514)). No independent before/after speed study was found.
- **Yavuz Sultan Selim Bridge, Marmaray, metro openings, earthquakes, football, Istanbul Marathon:** no quantitative speed or delay studies found in this search. These are gaps, not evidence of absence.

**Sub-hour resolution Istanbul studies (all forecasting, none event studies)**
- **[P] Yıldırım, Ü. & Çataltepe, Z.** "Short time traffic speed prediction using pattern recognition and feature selection methods". ITU, about 2008. It uses İBB RTMS speeds at 1–2 minute resolution and forecasts 5–60 minutes ahead. — [ITU Polen record](https://polen.itu.edu.tr/entities/publication/c97fd643-3dc3-4799-b83d-e43e046c826e/full); [2010 PDF](https://web.itu.edu.tr/~cataltepe/pdf/2010_TBV_Trafik.pdf); related article in *Türkiye Bilişim Vakfı Bilgisayar Bilimleri ve Mühendisliği Dergisi* ([DergiPark](https://dergipark.org.tr/en/pub/tbbmd/issue/22242/238772)). Authors and year come from search snippets and need confirming.
- **[P] Sabancı University (2018), "Traffic speed prediction with neural networks".** Search snippets say it uses floating-car speeds at one-minute resolution. Authors not verified. — [Sabancı repository](https://research.sabanciuniv.edu/id/eprint/34866/)
- **[V] Takak et al. (2021).** One-minute data from about 7,000 sensors, 2017 (see above).
- **[U] FSM Bridge RTMS study (2019).** A DergiPark article, not opened. — [PDF](https://dergipark.org.tr/en/download/article-file/2835030)
- **[U] Okan University, "Prediction of Short Term Traffic Speeds Using Deep Learning Models".** Not opened. — [GCRIS](https://gcris.okan.edu.tr/entities/publication/cedf1c82-9f0d-4500-af55-fe70ee605219/full)

**Congestion rankings**
- **[V] TomTom Traffic Index, Istanbul, 2025 data:**
  - congestion level 62%, up 2.6 percentage points on 2024;
  - 10 km takes 22 min 54 s on average;
  - rush-hour average speed 20.7 km/h;
  - the worst day was 23 Dec 2025, at 93%.
  - The page did not show a world rank or hours lost in the extracted text, and it is unclear whether the figures are for the city or the metro area.
  - Source: [tomtom.com](https://www.tomtom.com/traffic-index/istanbul-traffic/)
- **[P] INRIX 2024 Global Traffic Scorecard.** Istanbul ranks #1 in the world with 105 hours lost per driver, +15% on 2023, ahead of New York and Chicago (102 each). — [Hürriyet Daily News](https://hurriyetdailynews.com/istanbul-tops-2024-global-traffic-congestion-rankings-204482); [Daily Sabah](https://www.dailysabah.com/turkiye/istanbul-leads-global-traffic-congestion-rankings-in-2024/news/amp); [INRIX press release](https://inrix.com/press-releases/2024-global-traffic-scorecard-us/). Cite the INRIX primary source.

### Inferences
- Our siren design (a pre-announced, roughly one-minute, city-wide stop at a known clock time, repeated each year) has no direct precedent in the Istanbul literature. The closest analogues are the iftar synchronization and the COVID curfews, and only the curfews have a published analysis on İBB data (Alcan & Kaçar).
- The İBB hourly data cannot resolve a one-minute stop directly. Any effect shows up as a dilution within the 09:00 hour bin, if that bin is hour-beginning. That makes minute-level sources (İBB RTMS or segment speeds, available on request per Takak et al. 2021 and Yıldırım & Çataltepe) the main robustness candidates.
- High baseline congestion (TomTom rush-hour speed around 21 km/h, INRIX #1) means a 09:05 stop lands in the morning peak. Queue spillback could extend the delay well beyond one minute, which is a mechanism worth stating.

### Gaps
- Many relevant studies could not be fully verified: the Energies 2021 authors, Olug et al.'s period and frequency, the Sabancı and Okan theses, and the ITU work's exact citation.
- No Istanbul-specific Yandex Traffic research use was found.
- No TomTom world rank for Istanbul was obtained for 2024 or 2025.
- No search was done of Scopus/Web of Science or of YÖK Tez directly. These are recommended next steps: "Istanbul" AND ("traffic speed" OR "congestion") AND ("event" OR "holiday" OR "Ramadan" OR "curfew"), and YÖK for "İBB trafik yoğunluk" and "trafik endeksi".
