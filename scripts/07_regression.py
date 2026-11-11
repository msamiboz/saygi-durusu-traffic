"""Fixed-effects regression version of the design and the political-gradient tests.

Writes data/derived/regression_*.csv. Run after 03_estimate.py.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from saygi import calendar as cal
from saygi import dateri, geo, panel, pooled, regress

OUT = Path("data/derived")


def arrays(S, cls):
    py, ev = [], []
    for _, g in S[S.cls == cls].groupby("year"):
        g = g.dropna(subset=["M"]).sort_values("date").reset_index(drop=True)
        if not (g.k == 0).any():
            continue
        py.append(g.M.to_numpy())
        ev.append(int(g.index[g.k == 0][0]))
    return py, ev


def test(S, cls, alt="less"):
    py, ev = arrays(S, cls)
    r = dateri.test(py, ev, alternative=alt)
    by = r["by_year"].ravel()
    return dict(cls=cls, est=float(r["est"][0]), minutes=60 * (1 - np.exp(r["est"][0])), p=float(r["p"][0]),
                n_neg=int((by < 0).sum()), n_years=len(by), n_assign=r["n_assign"],
                p_sign=dateri.sign_flip(by if alt == "less" else -by),
                by_year=";".join(f"{x:.5f}" for x in by))  # fmt: skip


def vote_sources(C: pd.DataFrame) -> dict[str, pd.Series]:
    """CHP share per cell from each available source (district 2024 always; neighbourhood
    2024 local and 2023 general when the TÜİK reports are present). Neighbourhood shares are
    area-weighted over the neighbourhoods a cell overlaps; cells whose matched area is below
    half of the cell are left out."""
    out = {"district_local2024": C.chp}
    wpath = Path("data/interim/cell_mahalle.parquet")
    if not wpath.exists():
        geo.mahalle_weights().to_parquet(wpath)
    w = pd.read_parquet(wpath)
    files = {
        "mahalle_local2024": Path("data/raw/elections/yerel/buyuksehir_belediye_baskanligi/bolge_sonucu/2024/istanbul.xls"),
        "mahalle_general2023": sorted(Path("data/raw/elections/genel_bolge").rglob("*.xls")),
    }  # fmt: skip
    for name, f in files.items():
        paths = f if isinstance(f, list) else ([f] if f.exists() else [])
        if not paths:
            continue
        if name == "mahalle_general2023":
            v = geo.tuik_general_neighbourhood_votes(paths, name)
        else:
            v = pd.concat([geo.tuik_neighbourhood_votes(x, name) for x in paths], ignore_index=True)
        v = v.groupby("key", as_index=False).agg(chp=("chp", "mean"), akp=("akp", "mean"))
        cv = geo.cell_votes(w, v)
        cv[cv.matched_share >= 0.5].to_csv(OUT / f"cell_votes_{name}.csv")
        out[name] = cv.loc[cv.matched_share >= 0.5, "chp"]
    return out


def main() -> None:
    cd = panel.load_cellday()
    wx = regress.weather_hourly()
    C = geo.cells().drop_duplicates("GEOHASH").set_index("GEOHASH")
    have = set(cd.date.unique())
    stats = {k: [] for k in ("controls", "nocontrols")}
    sources = vote_sources(C)
    print("vote sources:", {k: len(v) for k, v in sources.items()}, flush=True)
    prof, slopes_side = [], []
    slopes = {(src, con): [] for src in sources for con in ("main", "far")}
    for y in cal.YEARS:
        L = regress.long_panel(cd, y)
        dates = [d for d in cal.pool(y) if d in have]
        base = pooled.baseline_speed(cd, dates)
        cls = pd.cut(base, pooled.BINS, right=False, labels=pooled.LABELS).astype(str)
        for tag, ctl in (("controls", True), ("nocontrols", False)):
            Lr, theta = regress.residualize(L, wx, controls=ctl)
            R = regress.date_hour_means(Lr, cls)
            for con in ("main", "far", "pre"):
                stats[tag].append(regress.date_stats(R, y, con).assign(contrast=con))
            if ctl:
                prof.append(regress.event_profile(R, y))
                # political gradient: CHP share, standardized over the cells in the panel
                for src, chp in sources.items():
                    z = chp.reindex(Lr.GEOHASH.unique()).dropna()
                    z = (z - z.mean()) / z.std()
                    for con in ("main", "far"):
                        slopes[(src, con)].append(regress.slope_stats(Lr, z, cls, y, con))
                side = (C.side.reindex(Lr.GEOHASH.unique()) == "Asia").astype(float)
                slopes_side.append(regress.slope_stats(Lr, side, cls, y, "main"))
                print(y, "theta", {k: round(v, 4) for k, v in theta.items()}, "cells", Lr.GEOHASH.nunique(),
                      "days", Lr.date.nunique(), flush=True)  # fmt: skip

    rows = []
    for tag, parts in stats.items():
        S = pd.concat(parts, ignore_index=True)
        S.to_csv(OUT / f"regression_date_stats_{tag}.csv", index=False)
        for con in ("main", "far", "pre"):
            for c in pooled.CLASSES:
                rows.append(dict(model=tag, contrast=con, **test(S[S.contrast == con], c)))
    res = pd.DataFrame(rows)
    res.to_csv(OUT / "regression_results.csv", index=False)

    P = pd.concat(prof, ignore_index=True)
    P.groupby(["cls", "hour"])["diff"].agg(["mean", "min", "max"]).reset_index().to_csv(
        OUT / "regression_profile.csv", index=False
    )

    srows = []
    for (src, con), parts in slopes.items():
        S = pd.concat(parts, ignore_index=True)
        S.to_csv(OUT / f"regression_chp_slopes_{src}_{con}.csv", index=False)
        for c in pooled.CLASSES:
            for alt in ("less", "greater"):
                r = test(S, c, alt)
                srows.append(dict(source=src, contrast=con, alt=alt, **r))
    S = pd.concat(slopes_side, ignore_index=True)
    for c in pooled.CLASSES:
        for alt in ("less", "greater"):
            srows.append(
                dict(source="side", contrast="main_asia_vs_europe", alt=alt, **test(S, c, alt))
            )
    pd.DataFrame(srows).to_csv(OUT / "regression_politics.csv", index=False)
    pd.set_option("display.width", 200)
    print(
        res[res.model == "controls"][["contrast", "cls", "est", "minutes", "p", "n_neg"]]
        .round(4)
        .to_string()
    )
    print(
        res[res.model == "nocontrols"][["contrast", "cls", "est", "minutes", "p", "n_neg"]]
        .round(4)
        .to_string()
    )
    sp = pd.DataFrame(srows)
    print(
        sp[sp.alt == "greater"][["contrast", "cls", "est", "p", "n_neg", "n_years", "by_year"]]
        .round(4)
        .to_string()
    )


if __name__ == "__main__":
    main()
