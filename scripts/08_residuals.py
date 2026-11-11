"""Residual diagnostics for the fixed-effects regression (figures/fig_residuals.*).

A: hourly mean residual on 10 November against the same-weekday placebo dates (50-70 km/h cells)
B: distribution of cell-hour residuals
C: residuals against fitted values (binned)
D: date-level residual contrast for every pool date, by year (the input to the placebo test)
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from saygi import calendar as cal
from saygi import panel, plots, pooled, regress


def main() -> None:
    cd = panel.load_cellday()
    wx = regress.weather_hourly()
    have = set(cd.date.unique())
    prof, resid, fit, stats = [], [], [], []
    rng = np.random.default_rng(0)
    for y in cal.YEARS:
        L = regress.long_panel(cd, y)
        dates = [d for d in cal.pool(y) if d in have]
        cls = pd.cut(
            pooled.baseline_speed(cd, dates), pooled.BINS, right=False, labels=pooled.LABELS
        ).astype(str)
        Lr, _ = regress.residualize(L, wx)
        R = regress.date_hour_means(Lr, cls)
        stats.append(regress.date_stats(R, y, "main"))
        ev = cal.event(y)
        S = R[(R.cls == "50-70") & (R.date.dt.dayofweek == ev.dayofweek)]
        S = S[[not cal.in_school_break(d) or d == ev for d in S.date]]
        prof.append(S.assign(year=y, event=S.date == ev))
        k = rng.choice(len(Lr), min(len(Lr), 200_000), replace=False)
        resid.append(Lr.r.to_numpy()[k])
        fit.append((Lr.y - Lr.r).to_numpy()[k])
        print(y, "residual sd", round(float(Lr.r.std()), 4), flush=True)
    P = pd.concat(prof, ignore_index=True)
    S = pd.concat(stats, ignore_index=True)
    r, f = np.concatenate(resid), np.concatenate(fit)
    pd.DataFrame({"fitted": f, "resid": r}).sample(50_000, random_state=0).to_csv(
        "data/derived/residual_sample.csv", index=False
    )
    P.to_csv("data/derived/residual_hour_profile.csv", index=False)
    plots.residuals(P, S, f, r, "figures/fig_residuals")
    print(
        "sd",
        r.std().round(4),
        "kurtosis",
        round(float(((r - r.mean()) ** 4).mean() / r.var() ** 2), 1),
    )


if __name__ == "__main__":
    main()
