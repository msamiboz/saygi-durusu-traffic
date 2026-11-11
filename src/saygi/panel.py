"""Build compact analysis panels from the monthly parquet files.

cellday   one row per (date, GEOHASH): average speed at hours 6-12, and minimum
          speed, maximum speed and vehicle count at hours 8-10 (wide, int16).
cityhour  one row per (date, hour): city-wide summaries, used for descriptives
          and for auditing the minimum-speed floor.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from . import bulk

DERIVED = Path("data/interim")
HOURS_AVG = range(6, 13)
HOURS_AUX = (8, 9, 10)


def _one_month(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    df = df[df.AVERAGE_SPEED > 0].copy()
    df["date"] = df.DATE_TIME.dt.normalize()
    df["hour"] = df.DATE_TIME.dt.hour.astype("int8")
    df = df.drop_duplicates(["date", "hour", "GEOHASH"])
    lv = np.log(df.AVERAGE_SPEED.to_numpy(float))
    city = (
        df.assign(
            lv=lv,
            lmin=np.log(df.MINIMUM_SPEED.clip(lower=1).to_numpy(float)),
            lveh=np.log(df.NUMBER_OF_VEHICLES.clip(lower=1).to_numpy(float)),
            min_le5=(df.MINIMUM_SPEED <= 5).to_numpy(),
            min_le1=(df.MINIMUM_SPEED <= 1).to_numpy(),
        )
        .groupby(["date", "hour"], observed=True)
        .agg(
            lv=("lv", "mean"),
            lmin=("lmin", "mean"),
            lveh=("lveh", "mean"),
            veh=("NUMBER_OF_VEHICLES", "sum"),
            n=("lv", "size"),
            min_le5=("min_le5", "mean"),
            min_le1=("min_le1", "mean"),
            min_speed=("MINIMUM_SPEED", "min"),
        )
        .reset_index()
    )
    d = df[df.hour.isin(list(HOURS_AVG))]
    wide = d.pivot(index=["date", "GEOHASH"], columns="hour", values="AVERAGE_SPEED")
    wide.columns = [f"v{h}" for h in wide.columns]
    aux = d[d.hour.isin(HOURS_AUX)]
    for col, tag in (("MINIMUM_SPEED", "mn"), ("MAXIMUM_SPEED", "mx"), ("NUMBER_OF_VEHICLES", "n")):
        w = aux.pivot(index=["date", "GEOHASH"], columns="hour", values=col)
        w.columns = [f"{tag}{h}" for h in w.columns]
        wide = wide.join(w)
    wide = wide.reset_index()
    for c in wide.columns[2:]:
        wide[c] = wide[c].astype("float32")
    wide["GEOHASH"] = wide["GEOHASH"].astype(str)
    return wide, city


def build(force: bool = False) -> None:
    DERIVED.mkdir(parents=True, exist_ok=True)
    cells, cities = [], []
    for f in sorted(bulk.OUT.glob("traffic_density_*.parquet")):
        ym = f.stem[-6:]
        cf, hf = DERIVED / f"cellday_{ym}.parquet", DERIVED / f"cityhour_{ym}.parquet"
        if force or not cf.exists():
            wide, city = _one_month(pd.read_parquet(f))
            wide.to_parquet(cf, compression="zstd")
            city.to_parquet(hf)
        cells.append(cf)
        cities.append(hf)
    # single dates fetched through the API while a monthly file is unavailable
    full = {f.stem[-6:] for f in bulk.OUT.glob("traffic_density_*.parquet")}
    for f in sorted(DERIVED.glob("cellday_p*.parquet")) + sorted(
        DERIVED.glob("cityhour_p*.parquet")
    ):
        f.unlink()
    days = [f for f in sorted(bulk.PARTIAL.glob("day_*.parquet")) if f.stem[4:10] not in full]
    for f in days:
        wide, city = _one_month(pd.read_parquet(f))
        wide.to_parquet(DERIVED / f"cellday_p{f.stem[4:]}.parquet", compression="zstd")
        city.to_parquet(DERIVED / f"cityhour_p{f.stem[4:]}.parquet")
        cities.append(DERIVED / f"cityhour_p{f.stem[4:]}.parquet")
    pd.concat([pd.read_parquet(f) for f in cities], ignore_index=True).to_parquet(
        DERIVED / "cityhour.parquet"
    )


def load_cellday(months: list[str] | None = None) -> pd.DataFrame:
    files = sorted(DERIVED.glob("cellday_??????.parquet")) + sorted(
        DERIVED.glob("cellday_p*.parquet")
    )
    if months is not None:
        files = [f for f in files if f.stem.split("_")[1].lstrip("p")[:6] in set(months)]
    return pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)


def load_hours(months: list[str], hours=range(24)) -> pd.DataFrame:
    """Long cell-hour table for the given months (for event-study hour profiles)."""
    parts = [bulk.load_months(months, columns=["DATE_TIME", "GEOHASH", "AVERAGE_SPEED"])]
    full = {f.stem[-6:] for f in bulk.OUT.glob("traffic_density_*.parquet")}
    for f in sorted(bulk.PARTIAL.glob("day_*.parquet")):
        if f.stem[4:10] in set(months) - full:
            parts.append(pd.read_parquet(f, columns=["DATE_TIME", "GEOHASH", "AVERAGE_SPEED"]))
    df = pd.concat(parts, ignore_index=True)
    df["GEOHASH"] = df["GEOHASH"].astype(str)
    df = df[df.AVERAGE_SPEED > 0]
    df["date"] = df.DATE_TIME.dt.normalize()
    df["hour"] = df.DATE_TIME.dt.hour.astype("int8")
    return df[df.hour.isin(list(hours))].drop(columns="DATE_TIME")
