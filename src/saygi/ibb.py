"""Download and cache the İBB hourly traffic density data set.

Source: İBB Açık Veri Portalı, "Saatlik Trafik Yoğunluk Veri Seti"
https://data.ibb.gov.tr/dataset/hourly-traffic-density-data-set
License: Istanbul Metropolitan Municipality Open Data License.
"""

from __future__ import annotations

import itertools
import json
import sys
import time
from pathlib import Path

import pandas as pd

API = "https://data.ibb.gov.tr/api/3/action/datastore_search"

# November resource IDs (from package_show, 2026-11-10)
RESOURCES = {
    2020: "93f996f1-70da-4500-951a-693c7e7066f6",
    2021: "b9131a98-99eb-4870-8960-e5f58f82e350",
    2022: "7f463362-a580-41d9-a86a-a542818e7542",
    2023: "e6a18077-2bd9-4201-8d4a-5398b0e2d99c",
    2024: "bedd5ab2-9a00-4966-9921-9672d4478a51",
}
DAYS = (3, 10, 17, 24)
HOURS = range(6, 13)
FIELDS = "GEOHASH,AVERAGE_SPEED,MINIMUM_SPEED,MAXIMUM_SPEED,NUMBER_OF_VEHICLES"
NUMERIC = ["AVERAGE_SPEED", "MINIMUM_SPEED", "MAXIMUM_SPEED", "NUMBER_OF_VEHICLES"]
DEFAULT_RAW = Path("data/raw/ibb_november.parquet")


def fetch(year: int, day: int, hour: int, page: int = 5000) -> pd.DataFrame:
    import requests

    ts = f"{year}-11-{day:02d} {hour:02d}:00:00"
    out, off = [], 0
    while True:
        params = {
            "resource_id": RESOURCES[year],
            "limit": page,
            "offset": off,
            "filters": json.dumps({"DATE_TIME": [ts]}),
            "fields": FIELDS,
        }
        for attempt in range(5):
            try:
                r = requests.get(API, params=params, timeout=120)
                r.raise_for_status()
                recs = r.json()["result"]["records"]
                break
            except Exception:  # noqa: BLE001 - retry any network/JSON error
                if attempt == 4:
                    raise
                time.sleep(2**attempt)
        out += recs
        if len(recs) < page:
            break
        off += page
    df = pd.DataFrame(out)
    df["year"], df["day"], df["hour"] = year, day, hour
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for c in NUMERIC:  # the 2023 file returns numerics as strings
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def download(path: Path = DEFAULT_RAW, years=RESOURCES, days=DAYS, hours=HOURS) -> pd.DataFrame:
    parts = []
    for y, d, h in itertools.product(years, days, hours):
        parts.append(fetch(y, d, h))
        print(y, d, h, len(parts[-1]), file=sys.stderr)
        time.sleep(0.2)
    df = clean(pd.concat(parts, ignore_index=True))
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path)
    return df


def load(path: Path = DEFAULT_RAW) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"{path} missing; run scripts/01_download_ibb.py first")
    return clean(pd.read_parquet(path))
