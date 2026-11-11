"""Huber robust version of the fixed-effects regression (scripts/07_regression.py).

The fixed effects and weather controls are estimated by Huber M-estimation (IRLS,
c = 1.345); date-level statistics are Huber-weighted means of the residuals, and the
political slopes are Huber M-estimates. Inference is the same placebo-date test.
Writes data/derived/huber_*.csv.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pandas as pd

from saygi import calendar as cal
from saygi import geo, panel, pooled, regress

OUT = Path("data/derived")
spec = importlib.util.spec_from_file_location("reg07", Path(__file__).parent / "07_regression.py")
reg07 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reg07)


def main() -> None:
    cd = panel.load_cellday()
    wx = regress.weather_hourly()
    C = geo.cells().drop_duplicates("GEOHASH").set_index("GEOHASH")
    sources = reg07.vote_sources(C)
    have = set(cd.date.unique())
    stats, meta = [], []
    slopes = {(s, c): [] for s in sources for c in ("main", "far")}
    for y in cal.YEARS:
        L = regress.long_panel(cd, y)
        dates = [d for d in cal.pool(y) if d in have]
        cls = pd.cut(
            pooled.baseline_speed(cd, dates), pooled.BINS, right=False, labels=pooled.LABELS
        ).astype(str)
        Lr, theta, s = regress.residualize_huber(L, wx)
        meta.append(dict(year=y, scale=s, share_downweighted=float((Lr.w < 1).mean()), **theta))
        R = regress.date_hour_means_w(Lr, cls)
        for con in ("main", "far", "pre"):
            stats.append(regress.date_stats(R, y, con).assign(contrast=con))
        for src, chp in sources.items():
            z = chp.reindex(Lr.GEOHASH.unique()).dropna()
            z = (z - z.mean()) / z.std()
            for con in ("main", "far"):
                slopes[(src, con)].append(regress.slope_stats_huber(Lr, z, cls, y, con))
        print(y, meta[-1], flush=True)
    pd.DataFrame(meta).to_csv(OUT / "huber_meta.csv", index=False)
    S = pd.concat(stats, ignore_index=True)
    S.to_csv(OUT / "huber_date_stats.csv", index=False)
    rows = [
        dict(contrast=con, **reg07.test(S[S.contrast == con], c))
        for con in ("main", "far", "pre")
        for c in pooled.CLASSES
    ]
    res = pd.DataFrame(rows)
    res.to_csv(OUT / "huber_results.csv", index=False)
    prow = []
    for (src, con), parts in slopes.items():
        P = pd.concat(parts, ignore_index=True)
        for c in pooled.CLASSES:
            for alt in ("less", "greater"):
                prow.append(dict(source=src, contrast=con, alt=alt, **reg07.test(P, c, alt)))
    pol = pd.DataFrame(prow)
    pol.to_csv(OUT / "huber_politics.csv", index=False)
    pd.set_option("display.width", 200)
    print(res[["contrast", "cls", "est", "minutes", "p", "n_neg"]].round(4).to_string())
    w = pol.pivot_table(index=["source", "contrast", "cls"], columns="alt", values="p")
    w["two"] = (2 * w.min(axis=1)).clip(upper=1)
    e = pol[pol.alt == "less"].set_index(["source", "contrast", "cls"])[["est", "n_neg"]]
    print(w.join(e)[["two", "est", "n_neg"]].round(4).to_string())


if __name__ == "__main__":
    main()
