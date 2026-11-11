"""Stage 1 of the main design: date-level statistics from cell-day contrasts.

For year y, the pool P_y holds the event date (10 Nov) and placebo dates of the
same weekday. For cell g and date d the within-day contrast is

    c(g,d) = f(x9) - [f(x8) + f(x10)] / 2        (f = log, or identity for shares)

Cells enter if they are observed on the event date and on at least `min_share`
of the pool dates. The date-level statistic is the mean cell-demeaned contrast

    M(y,d) = mean_g [ c(g,d) - mean_{d' in P_y} c(g,d') ]

computed for all cells and by speed class (mean 09h speed on the placebo dates).
Everything after this (estimates, tests, intervals) uses only M(y,d).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from . import calendar as cal

BINS = [0, 30, 50, 70, 999]
LABELS = ["<30", "30-50", "50-70", ">=70"]
CLASSES = ["all", *LABELS]

# outcome -> (column prefix, transform)
OUTCOMES = {
    "speed": ("v", "log"),
    "speed_level": ("v", "level"),
    "min_speed": ("mn", "log"),
    "max_speed": ("mx", "log"),
    "vehicles": ("n", "log"),
    "min_le2": ("mn", "le2"),
    "min_le6": ("mn", "le6"),
}
# contrast name -> {hour: weight}; weights on reference hours sum to -1
CONTRASTS = {
    "8,10": {9: 1, 8: -0.5, 10: -0.5},
    "8": {9: 1, 8: -1},
    "10": {9: 1, 10: -1},
    "7,8,10,11": {9: 1, 7: -0.25, 8: -0.25, 10: -0.25, 11: -0.25},
    "7,11": {9: 1, 7: -0.5, 11: -0.5},
    # main contrast net of the mean curvature at the placebo hours 07 and 11
    "net": {9: 1, 8: -0.25, 10: -0.25, 7: -0.5, 11: -0.5, 6: 0.25, 12: 0.25},
    "6,7,11,12": {9: 1, 6: -0.25, 7: -0.25, 11: -0.25, 12: -0.25},  # no adjacent hour
    # the neighbouring hours themselves, against hours not adjacent to the event
    "h8x": {8: 1, 6: -0.25, 7: -0.25, 11: -0.25, 12: -0.25},
    "h10x": {10: 1, 6: -0.25, 7: -0.25, 11: -0.25, 12: -0.25},
    "h7": {7: 1, 6: -0.5, 8: -0.5},  # placebo hours
    "h11": {11: 1, 10: -0.5, 12: -0.5},
}


def _f(x: pd.Series, how: str) -> pd.Series:
    if how == "log":
        return np.log(x.clip(lower=1))
    if how == "level":
        return x.astype(float)
    thr = {"le2": 2, "le6": 6}[how]
    return (x <= thr).astype(float).where(x.notna())


def contrast_matrix(cd: pd.DataFrame, dates, outcome="speed", contrast="8,10") -> pd.DataFrame:
    """Cells x dates matrix of within-day contrasts for the given pool dates."""
    pre, how = OUTCOMES[outcome]
    d = cd[cd.date.isin(dates)]
    c = sum(w * _f(d[f"{pre}{h}"], how) for h, w in CONTRASTS[contrast].items())
    return (
        pd.DataFrame({"date": d.date.values, "g": d.GEOHASH.values, "c": c.values})
        .pivot(index="g", columns="date", values="c")
        .reindex(columns=list(dates))
    )


def baseline_speed(cd: pd.DataFrame, dates, how: str = "pool") -> pd.Series:
    """Mean 09h speed per cell. 'pool': over all pool dates including the event
    date, so the classification is invariant to which date is called the event.
    'other': over all other days between the first and last pool date."""
    if how == "pool":
        d = cd[cd.date.isin(dates)]
    else:
        d = cd[(cd.date >= min(dates)) & (cd.date <= max(dates)) & ~cd.date.isin(dates)]
    return d.groupby("GEOHASH").v9.mean()


def date_stats(cd, year, dates, outcome="speed", contrast="8,10", min_share=0.75,
               groups: pd.Series | None = None, baseline="pool", bins=None,
               min_veh: float = 0, weighted: bool = False, shift: int = 0) -> pd.DataFrame:  # fmt: skip
    """Long table: year, date, k, cls, M, n (cells contributing on that date).

    weighted: weight cells by their mean number of probe vehicles at 09h.
    shift: treat 10 Nov + shift days as the event (placebo events)."""
    ev = cal.event(year) + pd.Timedelta(days=shift)
    C = contrast_matrix(cd, dates, outcome, contrast)
    keep = C[ev].notna() & (C.notna().mean(axis=1) >= min_share)
    if min_veh:
        nveh = cd[cd.date.isin(dates)].groupby("GEOHASH").n9.mean().reindex(C.index)
        keep &= (nveh >= min_veh).to_numpy()
    C = C[keep]
    dev = C.sub(C.mean(axis=1), axis=0)
    if groups is None:
        base = baseline_speed(cd, dates, baseline).reindex(C.index)
        if bins is None:
            groups = pd.cut(base, BINS, right=False, labels=LABELS).astype(object)
        else:
            groups = pd.cut(base, bins, right=False).astype(str).where(base.notna())
    else:
        groups = groups.reindex(C.index)
    w = None
    if weighted:
        w = cd[cd.date.isin(dates)].groupby("GEOHASH").n9.mean().reindex(C.index).fillna(0)
    rows = []
    for cls in ["all", *sorted(pd.unique(groups.dropna()), key=str)]:
        sel = slice(None) if cls == "all" else (groups == cls).to_numpy()
        sub = dev[sel]
        for d in dates:
            if w is None:
                mval = sub[d].mean()
            else:
                ok = sub[d].notna()
                mval = np.average(sub[d][ok], weights=w[sel][ok]) if ok.any() else np.nan
            rows.append(dict(year=year, date=d, k=round((d - ev).days / 7), cls=cls,
                             M=mval, n=int(sub[d].notna().sum())))  # fmt: skip
    return pd.DataFrame(rows)


def all_years(cd, weeks=8, drop_break=True, years=cal.YEARS, **kw) -> pd.DataFrame:
    out = []
    for y in years:
        dates = [
            d
            for d in cal.pool(y, weeks, drop_break, kw.get("shift", 0))
            if d in set(cd.date.unique())
        ]
        out.append(date_stats(cd, y, dates, **kw))
    return pd.concat(out, ignore_index=True)


def hour_stats(year: int, dates, cd: pd.DataFrame, min_share: float = 0.75) -> pd.DataFrame:
    """Hour-by-hour analogue of M: for each pool date d, hour h and speed class,

        H(d,h) = mean_g [ ln v(g,d,h) - mean_{d'} ln v(g,d',h) ].

    Reads the monthly (or partial daily) raw files for the pool dates only.
    """
    from . import bulk

    dates = list(dates)
    months = sorted({f"{d:%Y%m}" for d in dates})
    parts = []
    for ym in months:
        f = bulk.OUT / f"traffic_density_{ym}.parquet"
        files = [f] if f.exists() else sorted(bulk.PARTIAL.glob(f"day_{ym}*.parquet"))
        for ff in files:
            d = pd.read_parquet(ff, columns=["DATE_TIME", "GEOHASH", "AVERAGE_SPEED"])
            d = d[d.DATE_TIME.dt.normalize().isin(dates) & (d.AVERAGE_SPEED > 0)]
            parts.append(d.assign(GEOHASH=d.GEOHASH.astype(str)))
    df = pd.concat(parts, ignore_index=True)
    df["date"] = df.DATE_TIME.dt.normalize()
    df["hour"] = df.DATE_TIME.dt.hour
    df["lv"] = np.log(df.AVERAGE_SPEED.astype(float))
    df = df.drop_duplicates(["date", "hour", "GEOHASH"])
    base = baseline_speed(cd, dates)
    cls = pd.cut(base, BINS, right=False, labels=LABELS).astype(object)
    ev = cal.event(year)
    rows = []
    for h, g in df.groupby("hour"):
        W = g.pivot(index="GEOHASH", columns="date", values="lv").reindex(columns=dates)
        if ev not in W or W[ev].notna().sum() == 0:
            continue
        W = W[W[ev].notna() & (W.notna().mean(axis=1) >= min_share)]
        dev = W.sub(W.mean(axis=1), axis=0)
        k = cls.reindex(dev.index)
        for c in CLASSES:
            sub = dev if c == "all" else dev[(k == c).to_numpy()]
            for d in dates:
                rows.append(dict(year=year, date=d, k=round((d - ev).days / 7), hour=h, cls=c,
                                 H=sub[d].mean(), n=int(sub[d].notna().sum())))  # fmt: skip
    return pd.DataFrame(rows)
