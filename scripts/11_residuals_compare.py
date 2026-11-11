"""Residual diagnostics for the two tail treatments (figures/fig_residuals_tails.*).

A. Precision weighting: plain fixed-effects residuals standardized by each cell's own
   residual s.d. from days outside the pool, e = r * sqrt(precision).
B. Robust background: residuals from the Huber fit, scaled by the Huber scale s.
Rows: A, B. Columns: distribution against a normal, normal Q-Q, residual vs fitted,
date-level 09:00 contrast for 50-70 km/h cells.
"""

from __future__ import annotations

import json

import numpy as np
import pandas as pd

from saygi import calendar as cal
from saygi import panel, plots, regress


def main() -> None:
    cd = panel.load_cellday()
    wx = regress.weather_hourly()
    rng = np.random.default_rng(0)
    samp = {"A": [], "B": []}
    stats = {"A": pd.read_csv("data/derived/tails_date_stats_precision.csv", parse_dates=["date"]),
             "B": pd.read_csv("data/derived/tails_date_stats_robust_background.csv", parse_dates=["date"])}  # fmt: skip
    for y in cal.YEARS:
        L = regress.long_panel(cd, y)
        Lp, _ = regress.residualize(L, wx)
        prec = regress.cell_precision(Lp, y)
        Lp["e"] = Lp.r * np.sqrt(Lp.GEOHASH.map(prec))
        Lh, _, s = regress.residualize_huber(L, wx)
        Lh["e"] = Lh.r / s
        for k, D in (("A", Lp.dropna(subset=["e"])), ("B", Lh)):
            i = rng.choice(len(D), min(len(D), 120_000), replace=False)
            samp[k].append(
                pd.DataFrame({"e": D.e.to_numpy()[i], "fitted": np.exp((D.y - D.r).to_numpy()[i])})
            )
        print(y, "done", flush=True)
    summ = {}
    for k in samp:
        S = pd.concat(samp[k], ignore_index=True)
        S.to_csv(f"data/derived/residuals_tails_{k}.csv", index=False)
        e = S.e.to_numpy()
        z = (e - e.mean()) / e.std()
        summ[k] = dict(sd=float(e.std()), kurtosis=float((z**4).mean()), skew=float((z**3).mean()),
                       share_beyond_4sd=float((np.abs(z) > 4).mean()))  # fmt: skip
        samp[k] = S
    json.dump(summ, open("data/derived/residuals_tails_summary.json", "w"), indent=1)
    plots.residuals_tails(samp, stats, "figures/fig_residuals_tails")
    print(json.dumps(summ, indent=1))


if __name__ == "__main__":
    main()
