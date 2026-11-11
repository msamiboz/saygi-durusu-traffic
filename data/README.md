# Data

Nothing in `data/raw/` or `data/interim/` is committed. Only aggregated results in
`data/derived/` are versioned.

## İBB hourly traffic density (main source)

- Data set: *Saatlik Trafik Yoğunluk Veri Seti*, İBB Açık Veri Portalı,
  <https://data.ibb.gov.tr/dataset/hourly-traffic-density-data-set>
- One CSV per month, January 2020 – January 2025 (61 files, 100–140 MB each). Columns:
  `DATE_TIME, LATITUDE, LONGITUDE, GEOHASH, MINIMUM_SPEED, MAXIMUM_SPEED, AVERAGE_SPEED,
  NUMBER_OF_VEHICLES`; one row per geohash-6 cell and hour.
- `scripts/01_download_ibb.py` streams each file, converts it to
  `data/raw/monthly/traffic_density_YYYYMM.parquet` and deletes the CSV. The portal throttles
  bulk downloads, so the script may have to be run several times. Single dates can be pulled
  through the CKAN datastore API with `saygi.bulk.fetch_dates`.
- Things the portal does not document and the data show:
  - `MINIMUM_SPEED` is never 0. Until December 2020 almost no cell-hour is below 6 km/h;
    from January 2021 the floor is 1 km/h (`data/derived/floor_by_month.csv`).
  - Some days and hours are missing.
  - `NUMBER_OF_VEHICLES` is a sample of vehicles (median about 40–65 per cell at 09h).
- License: [İBB Open Data License](https://data.ibb.gov.tr/license). Required attribution:
  "Atıf 4.0 Uluslararası (CC BY 4.0) kapsamında lisanslanan kamu sektörü bilgilerini içerir."

## İBB traffic index, five-minute resolution

- Web service `https://api.ibb.gov.tr/tkmservices/api/TrafficData/v1/TrafficIndexHistory/{days}/5M`.
  It returns at most the latest 60 days. The response saved on 10 November 2026 covers
  11 September – 10 November 2026; the tidy copy is `data/derived/traffic_index_5min_2026.csv`
  (timestamp, traffic_index; 1–99, higher is more congested).

## Auxiliary inputs (`data/raw/aux/`, downloaded by `saygi.aux`)

| File | Source | License |
|---|---|---|
| `weather_istanbul_hourly.json` | Open-Meteo archive API, 41.015 N 28.979 E | CC BY 4.0 |
| `istanbul_districts_osm.json` | OpenStreetMap via Overpass (admin level 6) | ODbL |
| `wiki_en_election.txt` | Wikipedia, "2024 Istanbul mayoral election" (district results) | CC BY-SA |

## Calendar

Public holidays, religious holidays, lockdown periods and the schools' first-term break are
coded in `src/saygi/calendar.py`. Break weeks (Ministry of National Education calendars):
16–20 Nov 2020, 15–19 Nov 2021, 14–18 Nov 2022, 13–17 Nov 2023, 11–15 Nov 2024.

## Derived files (`data/derived/`, CC BY 4.0)

| File | Content |
|---|---|
| `date_stats_main.csv` | date-level statistic `M(y,d)` by year, date and speed class |
| `table_main.csv` | estimates, minutes, p-values (single, stepdown, Holm), intervals by class |
| `table_robustness.csv` | every robustness specification |
| `table_outcomes.csv`, `table_levels.csv` | other outcomes, placebo hours, placebo events |
| `table_heterogeneity.csv`, `table_districts.csv` | side, vote share, probe density, districts |
| `table_years.csv`, `speed_profile.csv`, `hour_stats.csv`, `hour_curvature.csv` | by year, by 10 km/h band, by hour |
| `power.csv`, `sensitivity.json`, `dependence.json`, `omnibus.json`, `break_check.json` | design diagnostics |
| `floor_by_month.csv` | share of cell-hours at or below 5 and 1 km/h, by month |
| `index_2026_test.csv`, `index_2026_profile.csv`, `traffic_index_5min_2026.csv` | five-minute index |

## Neighbourhood votes and boundaries

- Votes: TÜİK election statistics, "Belediye ve bölgelerine göre 31 Mart 2024 Büyükşehir Belediye
  Başkanlığı Seçimi sonucu" (Bölge sonucu, İstanbul), downloaded with `tools/tuik_yerel_bolge.py`
  into `data/raw/elections/yerel/`. 960 neighbourhoods with valid votes, CHP and AK PARTİ shares.
- 2023 general election (main measure): TÜİK "Seçim çevresi ve bölgelerine göre milletvekili
  genel seçimi sonuçları", one report per district (39), downloaded with
  `tools/tuik_genel_istanbul.py` into `data/raw/elections/genel_bolge/2023/`; 962 neighbourhoods.
  The menu needs both an electoral region and a district selected.
- Boundaries: land-registry (tapu kadastro) neighbourhood polygons prepared for another project
  (`mah_polygon.Rdata`), exported to `data/raw/aux/istanbul_mahalle.geojson`; 805 polygons.
- Each geohash cell gets the area-weighted CHP share of the neighbourhoods it overlaps
  (`saygi.geo.mahalle_weights`, `saygi.geo.cell_votes`); cells with less than half their area
  matched to a vote record are dropped. Output: `data/derived/cell_votes_mahalle_local2024.csv`.
