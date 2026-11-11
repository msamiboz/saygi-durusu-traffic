"""Fixed-effects regression version of the design, with placebo-date inference.

Sample, per year: every cell and every day within +-8 weeks of 10 November
(all weekdays, school-break days included, public holidays and lockdowns out),
hours 06-12. Outcome: ln v(g,d,h). The model is

    ln v(g,d,h) = a(g,d) + b(g,year,daytype,h) + c(break,h) + X(d,h)'theta
                  + sum_h beta_h * 1[d = 10 Nov] * 1[hour = h] + e

a(g,d)          absorbs everything that shifts a cell's whole morning on a day,
b(g,y,t,h)      each cell's usual hourly profile by day type (Mon-Thu, Fri, Sat, Sun),
c(break,h)      the hourly profile during the school break,
X(d,h)          hourly rain (mm), a wet-hour indicator and temperature.

Estimation is two-step (Frisch-Waugh): the fixed effects and controls are
partialled out of ln v WITHOUT the event dummies, and the date-level statistics
are formed from the residuals. Under the null of no effect this is the
covariance-adjusted randomization test of Rosenbaum (2002): any assignment of
the event to a same-weekday pool date gives a valid reference value.
"""

from __future__ import annotations

import json

import numpy as np
import pandas as pd

from . import calendar as cal

HOURS = list(range(6, 13))


def daytype(d: pd.Series) -> pd.Series:
    w = d.dt.dayofweek
    return np.select([w <= 3, w == 4, w == 5], ["MonThu", "Fri", "Sat"], "Sun")


def weather_hourly(path="data/raw/aux/weather_istanbul_hourly.json") -> pd.DataFrame:
    w = pd.DataFrame(json.load(open(path))["hourly"])
    w["time"] = pd.to_datetime(w["time"])
    w["date"], w["hour"] = w.time.dt.normalize(), w.time.dt.hour
    w["wet"] = (w.precipitation >= 0.2).astype(float)
    return w[["date", "hour", "precipitation", "wet", "temperature_2m"]].rename(
        columns={"precipitation": "rain", "temperature_2m": "temp"}
    )


def long_panel(cd: pd.DataFrame, year: int, weeks: int = 8, min_days: float = 0.6) -> pd.DataFrame:
    ev = cal.event(year)
    lo, hi = ev - pd.Timedelta(weeks=weeks), ev + pd.Timedelta(weeks=weeks, days=6)
    d = cd[(cd.date >= lo) & (cd.date <= hi)]
    keep = [
        x for x in d.date.unique() if not (cal.is_holiday(x) or cal.flags(x)["covid"]) or x == ev
    ]
    d = d[d.date.isin(keep)]
    # cells observed on the event date and on most days of the window
    on_ev = set(d[d.date == ev].GEOHASH)
    share = d.groupby("GEOHASH").date.nunique() / d.date.nunique()
    cells = [g for g in share.index[share >= min_days] if g in on_ev]
    d = d[d.GEOHASH.isin(cells)]
    L = d.melt(
        id_vars=["date", "GEOHASH"],
        value_vars=[f"v{h}" for h in HOURS],
        var_name="hour",
        value_name="v",
    )
    L = L.dropna()
    L = L[L.v > 0]
    L["hour"] = L.hour.str[1:].astype(int)
    L["y"] = np.log(L.v.astype(float))
    L["year"] = year
    L["dt"] = daytype(L.date)
    L["brk"] = [cal.in_school_break(x) for x in L.date]
    return L.drop(columns="v")


def _demean(
    cols: np.ndarray, groups: list[np.ndarray], iters: int = 30, tol: float = 1e-10
) -> np.ndarray:
    """Alternating projections onto the complement of several sets of fixed effects."""
    X = cols.astype(float).copy()
    for _ in range(iters):
        before = X.copy()
        for g in groups:
            n = np.bincount(g)
            for j in range(X.shape[1]):
                X[:, j] -= (np.bincount(g, weights=X[:, j]) / n)[g]
        if np.max(np.abs(X - before)) < tol:
            break
    return X


def residualize(L: pd.DataFrame, wx: pd.DataFrame, controls=True) -> tuple[pd.DataFrame, dict]:
    """Residuals of ln v after fixed effects and weather controls (no event dummies)."""
    L = L.merge(wx, on=["date", "hour"], how="left")
    for c in ("rain", "wet", "temp"):
        L[c] = L[c].fillna(L[c].mean())
    g1 = pd.factorize(L.GEOHASH + "|" + L.date.astype(str))[0]
    g2 = pd.factorize(L.GEOHASH + "|" + L.dt + "|" + L.hour.astype(str))[0]
    g3 = pd.factorize(L.brk.astype(str) + "|" + L.hour.astype(str))[0]
    xs = ["rain", "wet", "temp"] if controls else []
    M = _demean(L[["y", *xs]].to_numpy(), [g1, g2, g3])
    y = M[:, 0]
    theta = {}
    if xs:
        X = M[:, 1:]
        b = np.linalg.lstsq(X, y, rcond=None)[0]
        y = y - X @ b
        theta = dict(zip(xs, map(float, b)))
    L["r"] = y
    return L, theta


def date_hour_means(L: pd.DataFrame, groups: pd.Series | None = None) -> pd.DataFrame:
    """Mean residual by date, hour and group (group = 'all' plus any labels given)."""
    out = [L.groupby(["date", "hour"]).r.mean().rename("R").reset_index().assign(cls="all")]
    if groups is not None:
        lab = L.GEOHASH.map(groups)
        ok = lab.notna()
        out.append(
            L[ok]
            .assign(cls=lab[ok])
            .groupby(["cls", "date", "hour"])
            .r.mean()
            .rename("R")
            .reset_index()
        )
    return pd.concat(out, ignore_index=True)


CONTRASTS = {
    "main": {9: 1, 8: -0.5, 10: -0.5},
    "far": {9: 1, 6: -0.25, 7: -0.25, 11: -0.25, 12: -0.25},
    "pre": {9: 1, 8: -1},
}


def date_stats(R: pd.DataFrame, year: int, contrast="main") -> pd.DataFrame:
    """Same-weekday pool dates of the year with the contrast of residual means."""
    ev = cal.event(year)
    W = R.pivot_table(index=["cls", "date"], columns="hour", values="R")
    M = sum(w * W[h] for h, w in CONTRASTS[contrast].items()).rename("M").reset_index()
    M = M[M.date.dt.dayofweek == ev.dayofweek]
    M = M[[not cal.in_school_break(d) or d == ev for d in M.date]]
    M["year"], M["k"] = year, ((M.date - ev).dt.days // 7).astype(int)
    return M


def event_profile(R: pd.DataFrame, year: int) -> pd.DataFrame:
    """Hour-by-hour residual on the event date minus the same-weekday placebo mean."""
    ev = cal.event(year)
    S = R[R.date.dt.dayofweek == ev.dayofweek]
    S = S[[not cal.in_school_break(d) or d == ev for d in S.date]]
    e = S[S.date == ev].set_index(["cls", "hour"]).R
    p = S[S.date != ev].groupby(["cls", "hour"]).R.mean()
    return (e - p).rename("diff").reset_index().assign(year=year)


def slope_stats(
    L: pd.DataFrame, z: pd.Series, cls_of: pd.Series, year: int, contrast="main"
) -> pd.DataFrame:
    """Per date and speed class: OLS slope of the cell-level residual contrast on z
    (e.g. a standardized vote share). One number per date, used for placebo inference."""
    ev = cal.event(year)
    W = L.pivot_table(index=["GEOHASH", "date"], columns="hour", values="r")
    c = sum(w * W[h] for h, w in CONTRASTS[contrast].items()).rename("c").reset_index().dropna()
    c = c[c.date.dt.dayofweek == ev.dayofweek]
    c = c[[not cal.in_school_break(d) or d == ev for d in c.date]]
    c["z"], c["cls"] = c.GEOHASH.map(z), c.GEOHASH.map(cls_of)
    c = c.dropna()
    rows = []
    for cls_, g in [("all", c), *c.groupby("cls")]:
        for d, h in g.groupby("date"):
            zz = h.z - h.z.mean()
            b = (
                float((zz * (h.c - h.c.mean())).sum() / (zz**2).sum())
                if (zz**2).sum() > 0
                else np.nan
            )
            rows.append(dict(cls=cls_, date=d, M=b, year=year, k=(d - ev).days // 7, n=len(h)))
    return pd.DataFrame(rows)
