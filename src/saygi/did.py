"""Within-day difference-in-differences on İBB geohash speeds.

    c(g,y,d) = ln v(9) - [ln v(8) + ln v(10)] / 2
    D(g,y)   = c(g,y,Nov 10) - mean_{d in controls} c(g,y,d)
    minutes  = 60 * (1 - exp(D))      full-stop-equivalent minutes in the 09:00 hour

Every day of the year is in turn treated as the "event" day, which gives the
placebo distribution used by randomization inference.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

DAYS = (3, 10, 17, 24)
TREAT = 10
CLASS_BINS = [0, 30, 50, 70, 999]
CLASS_LABELS = ["<30", "30-50", "50-70", ">=70"]
CLASS_ORDER = ["all", *CLASS_LABELS]


def contrast(df: pd.DataFrame, outcome: str = "AVERAGE_SPEED") -> pd.DataFrame:
    """Balanced (year, GEOHASH) x day table of within-day contrasts c."""
    d = df[df.hour.isin([8, 9, 10]) & (df[outcome] > 0)].copy()
    d["lv"] = np.log(d[outcome])
    w = d.pivot_table(index=["year", "GEOHASH", "day"], columns="hour", values="lv")
    w["c"] = w[9] - (w[8] + w[10]) / 2
    return w["c"].unstack("day").dropna()


def did_table(df: pd.DataFrame, outcome: str = "AVERAGE_SPEED") -> pd.DataFrame:
    """Index (year, GEOHASH); one column per day treated as the event day."""
    c = contrast(df, outcome)
    days = list(c.columns)
    return pd.DataFrame({t: c[t] - c[[x for x in days if x != t]].mean(axis=1) for t in days})


def pooled(D: pd.DataFrame) -> pd.DataFrame:
    """Mean over geohashes within year (rows = year, columns = treated day)."""
    return D.groupby(level="year").mean()


def minutes(x, window: float = 60.0):
    """Full-stop-equivalent minutes for a log-speed DiD x over a window of `window` minutes."""
    return window * (1 - np.exp(x))


def speed_class(df: pd.DataFrame, treat: int = TREAT) -> pd.Series:
    """Class of each (year, GEOHASH) by mean 09:00 speed on the control days."""
    base = (
        df[(df.hour == 9) & df.day.isin([d for d in DAYS if d != treat])]
        .groupby(["year", "GEOHASH"])
        .AVERAGE_SPEED.mean()
    )
    return pd.cut(base, CLASS_BINS, right=False, labels=CLASS_LABELS)


def did_by_class(df: pd.DataFrame) -> pd.DataFrame:
    """Long table cls, year, day, did, se, n (the pilot's data/did_by_class.csv)."""
    D = did_table(df)
    bins = speed_class(df)
    groups = {"all": D.index}
    for lab in CLASS_LABELS:
        groups[lab] = bins[bins == lab].index.intersection(D.index)
    rows = []
    for cls, idx in groups.items():
        sub = D.loc[idx]
        for y, g in sub.groupby(level="year"):
            for day in g.columns:
                v = g[day]
                rows.append(
                    dict(
                        cls=cls,
                        year=y,
                        day=day,
                        did=v.mean(),
                        se=v.std(ddof=1) / np.sqrt(len(v)),
                        n=len(v),
                    )
                )
    return pd.DataFrame(rows)


def city_hourly(df: pd.DataFrame) -> pd.DataFrame:
    """City-wide mean log speed, mean vehicle count and cell count by year/day/hour."""
    d = df[df.AVERAGE_SPEED > 0].assign(lv=lambda x: np.log(x.AVERAGE_SPEED))
    return (
        d.groupby(["year", "day", "hour"])
        .agg(lv=("lv", "mean"), veh=("NUMBER_OF_VEHICLES", "mean"), n=("lv", "size"))
        .reset_index()
    )
