"""Two treatments of heavy-tailed residuals that keep the event's own extreme values.

A. Precision weighting: plain fixed-effects residuals; each cell weighted by the
   inverse of its residual variance on days outside the same-weekday pool
   (inverse-variance / weighted least squares; cf. Ferman and Pinto 2019).
B. Robust background: fixed effects and weather fitted by Huber M-estimation, then the
   event statistic is a plain, unweighted mean of the residuals (Rosenbaum 2002).
C. Check: how often Huber downweights 09:00 cell-hours on 10 November vs placebo dates.
Writes data/derived/tails_*.csv.
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
    sources = {k: v for k, v in reg07.vote_sources(C).items()}
    have = set(cd.date.unique())
    stats = {"precision": [], "robust_background": []}
    slopes = {(m, s, c): [] for m in stats for s in sources for c in ("main", "far")}
    check = []
    for y in cal.YEARS:
        L = regress.long_panel(cd, y)
        dates = [d for d in cal.pool(y) if d in have]
        cls = pd.cut(
            pooled.baseline_speed(cd, dates), pooled.BINS, right=False, labels=pooled.LABELS
        ).astype(str)
        # A. precision weighting on plain residuals
        Lp, _ = regress.residualize(L, wx)
        prec = regress.cell_precision(Lp, y)
        R = regress.date_hour_means_prec(Lp, prec, cls)
        for con in ("main", "far", "pre"):
            stats["precision"].append(regress.date_stats(R, y, con).assign(contrast=con))
        # B. Huber background, plain mean of residuals
        Lh, _, s = regress.residualize_huber(L, wx)
        R = regress.date_hour_means(Lh, cls)
        for con in ("main", "far", "pre"):
            stats["robust_background"].append(regress.date_stats(R, y, con).assign(contrast=con))
        for src, chp in sources.items():
            z = chp.reindex(L.GEOHASH.unique()).dropna()
            z = (z - z.mean()) / z.std()
            for con in ("main", "far"):
                slopes[("precision", src, con)].append(
                    regress.slope_stats_weighted(Lp, z, cls, prec, y, con)
                )
                slopes[("robust_background", src, con)].append(
                    regress.slope_stats(Lh, z, cls, y, con)
                )
        # C. downweighting of 09:00 cell-hours, event vs same-weekday placebo dates
        ev = cal.event(y)
        H = Lh[(Lh.hour == 9) & Lh.date.isin(dates)]
        H = H.assign(cls=H.GEOHASH.map(cls))
        for c in ("all", "50-70", "<30"):
            g = H if c == "all" else H[H.cls == c]
            e, p = g[g.date == ev], g[g.date != ev]
            check.append(dict(year=y, cls=c,
                              event_down=float((e.w < 1).mean()), placebo_down=float((p.w < 1).mean()),
                              event_down_neg=float(((e.w < 1) & (e.r < 0)).mean()),
                              placebo_down_neg=float(((p.w < 1) & (p.r < 0)).mean()),
                              event_strong=float((e.w < 0.5).mean()), placebo_strong=float((p.w < 0.5).mean())))  # fmt: skip
        print(y, "done", flush=True)
    res = []
    for m, parts in stats.items():
        S = pd.concat(parts, ignore_index=True)
        S.to_csv(OUT / f"tails_date_stats_{m}.csv", index=False)
        for con in ("main", "far", "pre"):
            for c in pooled.CLASSES:
                res.append(dict(method=m, contrast=con, **reg07.test(S[S.contrast == con], c)))
    res = pd.DataFrame(res)
    res.to_csv(OUT / "tails_results.csv", index=False)
    pol = []
    for (m, src, con), parts in slopes.items():
        P = pd.concat(parts, ignore_index=True)
        for c in pooled.CLASSES:
            for alt in ("less", "greater"):
                pol.append(
                    dict(method=m, source=src, contrast=con, alt=alt, **reg07.test(P, c, alt))
                )
    pol = pd.DataFrame(pol)
    pol.to_csv(OUT / "tails_politics.csv", index=False)
    ck = pd.DataFrame(check)
    ck.to_csv(OUT / "tails_huber_check.csv", index=False)
    pd.set_option("display.width", 220)
    print(
        res[res.cls.isin(["all", "50-70", "<30"])][
            ["method", "contrast", "cls", "minutes", "p", "n_neg"]
        ]
        .round(4)
        .to_string()
    )
    w = pol.pivot_table(index=["method", "source", "contrast", "cls"], columns="alt", values="p")
    w["two"] = (2 * w.min(axis=1)).clip(upper=1)
    e = pol[pol.alt == "less"].set_index(["method", "source", "contrast", "cls"])[["est", "n_neg"]]
    t = w.join(e)[["two", "est", "n_neg"]].reset_index()
    print(
        t[t.cls.isin(["<30", "50-70", "all"]) & (t.source != "mahalle_local2024")]
        .round(4)
        .to_string()
    )
    print(
        ck.groupby("cls")[[c for c in ck.columns if c not in ("year", "cls")]]
        .mean()
        .round(4)
        .to_string()
    )


if __name__ == "__main__":
    main()
