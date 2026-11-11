"""Download every monthly file of the İBB hourly traffic density data set.

Each monthly CSV (100-140 MB) is streamed to a temporary file, converted to a
compact parquet in data/raw/monthly/ and deleted. Cell coordinates are stored
once in data/raw/geohash_coords.parquet.
"""

from __future__ import annotations

import re
import subprocess
import sys
import time
from pathlib import Path

import pandas as pd

PACKAGE = "https://data.ibb.gov.tr/api/3/action/package_show?id=hourly-traffic-density-data-set"
OUT = Path("data/raw/monthly")
COORDS = Path("data/raw/geohash_coords.parquet")
NUMERIC = ["MINIMUM_SPEED", "MAXIMUM_SPEED", "AVERAGE_SPEED", "NUMBER_OF_VEHICLES"]


def resources() -> list[tuple[str, str]]:
    """[(yyyymm, url)] for every monthly CSV, from the CKAN package record."""
    import json

    import requests

    cache = Path("data/raw/resources.json")
    if cache.exists():
        return [tuple(x) for x in json.load(open(cache))]
    for attempt in range(8):
        try:
            res = requests.get(PACKAGE, timeout=30).json()["result"]["resources"]
            break
        except Exception:  # noqa: BLE001
            if attempt == 7:
                raise
            time.sleep(5)
    out = []
    for r in res:
        m = re.search(r"(\d{6})\.csv$", r["url"])
        if m:
            out.append((m.group(1), r["url"]))
    cache.parent.mkdir(parents=True, exist_ok=True)
    json.dump(sorted(out), open(cache, "w"))
    return sorted(out)


def convert(csv: Path, yyyymm: str) -> pd.DataFrame:
    df = pd.read_csv(csv, dtype=str)
    df.columns = [c.strip().upper() for c in df.columns]
    for c in NUMERIC:  # some files store numerics as text
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["DATE_TIME"] = pd.to_datetime(df["DATE_TIME"], errors="coerce")
    df = df.dropna(subset=["DATE_TIME", "GEOHASH", "AVERAGE_SPEED"])
    coords = None
    if {"LATITUDE", "LONGITUDE"} <= set(df.columns):
        coords = (
            df[["GEOHASH", "LATITUDE", "LONGITUDE"]]
            .drop_duplicates("GEOHASH")
            .assign(
                LATITUDE=lambda x: pd.to_numeric(x.LATITUDE, errors="coerce"),
                LONGITUDE=lambda x: pd.to_numeric(x.LONGITUDE, errors="coerce"),
            )
        )
    out = df[["DATE_TIME", "GEOHASH", *NUMERIC]].copy()
    for c in NUMERIC:
        out[c] = out[c].round().astype("int32")
    out["GEOHASH"] = out["GEOHASH"].astype("category")
    OUT.mkdir(parents=True, exist_ok=True)
    out.to_parquet(OUT / f"traffic_density_{yyyymm}.parquet", compression="zstd")
    if coords is not None:
        if COORDS.exists():
            coords = pd.concat([pd.read_parquet(COORDS), coords]).drop_duplicates("GEOHASH")
        coords.to_parquet(COORDS)
    return out


def download_all(order: list[str] | None = None, pause: float = 20) -> None:
    res = dict(resources())
    fails = 0
    months = order or sorted(res)
    tmp = Path("data/raw/_tmp.csv")
    for ym in months:
        target = OUT / f"traffic_density_{ym}.parquet"
        if target.exists() or ym not in res:
            continue
        cmd = ["curl", "-sS", "-L", "--connect-timeout", "30",
               "--speed-limit", "20000", "--speed-time", "30",  # abort stalled transfers
               "--max-time", "900", "-o", str(tmp), res[ym]]  # fmt: skip
        tmp.unlink(missing_ok=True)
        rc = subprocess.run(cmd).returncode
        if rc != 0 or not tmp.exists():
            # the portal throttles bulk downloads; stop this pass and retry later
            print(ym, "download failed", rc, file=sys.stderr, flush=True)
            fails += 1
            if fails >= 2:
                return
            continue
        fails = 0
        time.sleep(pause)
        try:
            df = convert(tmp, ym)
            print(ym, len(df), "rows", file=sys.stderr, flush=True)
        except Exception as e:  # noqa: BLE001
            print(ym, "convert failed", e, file=sys.stderr, flush=True)
        tmp.unlink(missing_ok=True)


def load_months(months: list[str] | None = None, columns=None) -> pd.DataFrame:
    files = sorted(OUT.glob("traffic_density_*.parquet"))
    if months is not None:
        files = [f for f in files if f.stem[-6:] in set(months)]
    parts = [pd.read_parquet(f, columns=columns) for f in files]
    if not parts:
        return pd.DataFrame(columns=columns or ["DATE_TIME", "GEOHASH", *NUMERIC])
    df = pd.concat(parts, ignore_index=True)
    if "GEOHASH" in df:
        df["GEOHASH"] = df["GEOHASH"].astype(str)
    return df


PARTIAL = Path("data/raw/partial")


def fetch_dates(dates, hours=range(24), pause: float = 0.2) -> None:
    """Fallback when the bulk CSV endpoint is throttled: pull single dates through
    the datastore API and store them as partial monthly files in data/raw/partial/.
    """
    import json

    import requests

    api = "https://data.ibb.gov.tr/api/3/action/datastore_search"
    rid = {ym: url.split("/resource/")[1].split("/")[0] for ym, url in resources()}
    PARTIAL.mkdir(parents=True, exist_ok=True)
    for d in dates:
        d = pd.Timestamp(d)
        ym = f"{d:%Y%m}"
        out = PARTIAL / f"day_{d:%Y%m%d}.parquet"
        if out.exists() or (OUT / f"traffic_density_{ym}.parquet").exists():
            continue
        recs = []
        for h in hours:
            ts, off = f"{d:%Y-%m-%d} {h:02d}:00:00", 0
            while True:
                params = {"resource_id": rid[ym], "limit": 5000, "offset": off,
                          "filters": json.dumps({"DATE_TIME": [ts]})}  # fmt: skip
                for attempt in range(6):
                    try:
                        page = requests.get(api, params=params, timeout=120).json()["result"][
                            "records"
                        ]
                        break
                    except Exception:  # noqa: BLE001
                        if attempt == 5:
                            raise
                        time.sleep(3 * (attempt + 1))
                recs += page
                if len(page) < 5000:
                    break
                off += 5000
            time.sleep(pause)
        df = pd.DataFrame(recs)
        for c in NUMERIC:
            df[c] = pd.to_numeric(df[c], errors="coerce").round().astype("int32")
        df["DATE_TIME"] = pd.to_datetime(df["DATE_TIME"])
        df[["DATE_TIME", "GEOHASH", *NUMERIC]].to_parquet(out, compression="zstd")
        print(d.date(), len(df), "rows", file=sys.stderr, flush=True)
