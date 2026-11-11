"""Download all monthly İBB traffic density files to data/raw/monthly/ (parquet)
and the auxiliary inputs (weather, district boundaries, election results).

The portal throttles bulk downloads: rerun the script until all months are present.
Autumn months (Sep-Dec) are fetched first because every analysis needs them.
"""

from saygi import aux, bulk

if __name__ == "__main__":
    aux.all_()
    months = [ym for ym, _ in bulk.resources()]
    first = [m for m in months if m[4:] in ("11", "10", "09", "12", "01")]
    bulk.download_all(first + [m for m in months if m not in first])
    missing = [m for m in months if not (bulk.OUT / f"traffic_density_{m}.parquet").exists()]
    print("missing months:", missing or "none")
