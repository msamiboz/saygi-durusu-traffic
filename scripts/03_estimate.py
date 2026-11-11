"""All estimates of the paper. Reads data/interim/, writes data/derived/*.csv.

Run after 01_download_ibb.py and 02_build_panels.py.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from saygi import calendar as cal
from saygi import dateri, geo, panel, pooled

OUT = Path("data/derived")
OUT.mkdir(parents=True, exist_ok=True)
MAIN_WEEKS = 8


def minutes(x):
    return 60 * (1 - np.exp(x))


def arrays(S: pd.DataFrame, cls, years=None):
    """Date-level statistics of one class as per-year arrays (M, event index, week index)."""
    s = S[S.cls == cls]
    py, ev, tt, yrs = [], [], [], []
    for y, g in s.groupby("year"):
        if years is not None and y not in years:
            continue
        g = g.dropna(subset=["M"]).sort_values("date").reset_index(drop=True)
        if not (g.k == 0).any():  # no data on the (placebo) event date in this year
            continue
        py.append(g.M.to_numpy())
        ev.append(int(g.index[g.k == 0][0]))
        tt.append(g.k.to_numpy(float))
        yrs.append(y)
    return py, ev, tt, yrs


def run(S, cls, years=None, **kw):
    py, ev, tt, yrs = arrays(S, cls, years)
    r = dateri.test(py, ev, tt, **kw)
    r["years"] = yrs
    r["n_dates"] = [len(x) for x in py]
    return r


def row(label, S, cls, years=None, alt="less", **kw):
    r = run(S, cls, years, alternative=alt, **kw)
    by = r["by_year"].ravel()
    n = S[(S.cls == cls) & (S.k == 0)]
    if years is not None:
        n = n[n.year.isin(years)]
    return dict(
        spec=label, cls=cls, est=r["est"][0], minutes=minutes(r["est"][0]), p=r["p"][0],
        n_assign=r["n_assign"], exact=r["exact"], n_years=len(by),
        n_neg=int((by < 0).sum()), n_pos=int((by > 0).sum()),
        by_year=json.dumps(dict(zip(map(int, r["years"]), np.round(by, 5).tolist()))),
        p_sign=dateri.sign_flip(by if alt == "less" else -by),
        cells=int(round(n.n.mean())), dates=int(sum(r["n_dates"])),
    )  # fmt: skip


def stats(cd, weeks=MAIN_WEEKS, drop_break=True, years=cal.YEARS, **kw):
    have = set(cd.date.unique())
    out = []
    for y in years:
        dates = [d for d in cal.pool(y, weeks, drop_break, kw.get("shift", 0)) if d in have]
        out.append(pooled.date_stats(cd, y, dates, **kw))
    return pd.concat(out, ignore_index=True)


def group_stats(cd, fn, weeks=MAIN_WEEKS, **kw):
    have = set(cd.date.unique())
    out = []
    for y in cal.YEARS:
        dates = [d for d in cal.pool(y, weeks) if d in have]
        out.append(pooled.date_stats(cd, y, dates, groups=fn(y, dates), **kw))
    return pd.concat(out, ignore_index=True)


def main() -> None:
    cd = panel.load_cellday()
    S = stats(cd)
    S.to_csv(OUT / "date_stats_main.csv", index=False)

    # ------------------------------------------------------------ Table: main, by class
    rows = [row("main", S, c) for c in pooled.CLASSES]
    main_t = pd.DataFrame(rows)
    # joint reference distribution over the four speed classes (same assignment in each)
    py = [np.column_stack([arrays(S, c, [y])[0][0] for c in pooled.LABELS]) for y in cal.YEARS]
    ev = [arrays(S, pooled.LABELS[0], [y])[1][0] for y in cal.YEARS]
    joint = dateri.test(py, ev)
    adj = dateri.stepdown(joint["est"], joint["ref"])
    main_t["p_stepdown"] = [np.nan, *adj]
    main_t["p_holm"] = [np.nan, *dateri.holm(main_t.p.to_numpy()[1:])]
    main_t["p_bonf"] = [np.nan, *np.minimum(1, 4 * main_t.p.to_numpy()[1:])]
    # omnibus: is the most negative class more negative than under random dates?
    sd = joint["ref"].std(axis=0)
    omni = float(((joint["ref"] / sd).min(axis=1) <= (joint["est"] / sd).min() + 1e-12).mean())
    hl, ci = [], []
    for c in pooled.CLASSES:
        a = arrays(S, c)
        h, (lo, hi) = dateri.interval(a[0], a[1])
        hl.append(h)
        ci.append((lo, hi))
    main_t["hl"] = hl
    main_t["ci_lo"] = [c[0] for c in ci]
    main_t["ci_hi"] = [c[1] for c in ci]
    main_t.to_csv(OUT / "table_main.csv", index=False)

    # difference between classes: 50-70 minus each other class (joint assignment)
    diffs = []
    j = pooled.LABELS.index("50-70")
    for i, c in enumerate(pooled.LABELS):
        if i == j:
            continue
        d_obs = joint["est"][j] - joint["est"][i]
        d_ref = joint["ref"][:, j] - joint["ref"][:, i]
        diffs.append(
            dict(contrast=f"50-70 minus {c}", diff=d_obs, p=float((d_ref <= d_obs + 1e-12).mean()))
        )
    pd.DataFrame(diffs).to_csv(OUT / "table_class_differences.csv", index=False)

    # ------------------------------------------------------------ year-level description
    yr = []
    for y in cal.YEARS:
        s = S[(S.year == y) & (S.cls == "all")]
        m = cd[cd.date == cal.event(y)]
        yr.append(dict(year=y, weekday=cal.event(y).day_name(), pool_dates=len(s),
                       cells=int(s[s.k == 0].n.iloc[0]), median_vehicles=float(m.n9.median()),
                       floor=int(np.nanpercentile(cd[cd.date.dt.year == y].mn9, 1))))  # fmt: skip
    for c in pooled.CLASSES:
        r = run(S, c)
        for i in range(len(r["years"])):
            yr[i][f"est_{c}"] = float(r["by_year"].ravel()[i])
    pd.DataFrame(yr).to_csv(OUT / "table_years.csv", index=False)

    # ------------------------------------------------------------ speed profile (10 km/h bins)
    bins = [0, 20, 30, 40, 50, 60, 70, 80, 90, 200]
    Sf = stats(cd, bins=bins)
    prof = []
    for c in sorted(
        [c for c in Sf.cls.unique() if c != "all"], key=lambda s: float(s[1:].split(",")[0])
    ):
        r = run(Sf, c)
        q = np.quantile(r["ref"], [0.05, 0.5, 0.95])
        prof.append(dict(bin=c, est=r["est"][0], p=r["p"][0], q05=q[0], q50=q[1], q95=q[2],
                         n_neg=int((r["by_year"] < 0).sum()),
                         cells=int(Sf[(Sf.cls == c) & (Sf.k == 0)].n.mean())))  # fmt: skip
    pd.DataFrame(prof).to_csv(OUT / "speed_profile.csv", index=False)

    # ------------------------------------------------------------ robustness
    rob = []
    for c in ("all", "50-70"):
        rob.append(row("Main: +-8 weeks, school-break dates dropped", S, c))
        P = stats(cd, weeks=2, drop_break=False)
        rob.append(row("Pilot dates only (3, 17, 24 Nov)", P[P.k.isin([-1, 0, 1, 2])], c))
        P2 = P[P.k.isin([-1, 0, 1])]
        rob.append(row("Adjacent weeks only (3 and 17 Nov)", P2, c))
        rob.append(row("+-4 weeks", stats(cd, weeks=4), c))
        rob.append(row("+-12 weeks", stats(cd, weeks=12), c))
        rob.append(row("All same-weekday dates of the year", stats(cd, weeks=None), c))
        rob.append(row("School-break dates kept", stats(cd, drop_break=False), c))
        rob.append(row("Linear trend removed within year", S, c, detrend=1))
        rob.append(row("Quadratic trend removed within year", S, c, detrend=2))
        rob.append(row("Statistic scaled by placebo s.d. (z)", S, c, how="z"))
        rob.append(row("Rank statistic", S, c, how="rank"))
        for con, lab in (("8", "Reference hour 08 only"), ("10", "Reference hour 10 only"),
                         ("7,8,10,11", "Reference hours 07, 08, 10, 11"), ("7,11", "Reference hours 07 and 11"),
                         ("6,7,11,12", "Reference hours 06, 07, 11, 12 (none adjacent)")):  # fmt: skip
            rob.append(row(lab, stats(cd, contrast=con), c))
        rob.append(row("Net of curvature at placebo hours 07 and 11", stats(cd, contrast="net"), c))
        rob.append(row("Balanced cells (observed on every date)", stats(cd, min_share=1.0), c))
        rob.append(row("Cells with >= 10 vehicles at 09h", stats(cd, min_veh=10), c))
        rob.append(row("Cells weighted by probe vehicles", stats(cd, weighted=True), c))
        if c != "all":
            rob.append(row("Speed class from other days", stats(cd, baseline="other"), c))
        for y in cal.YEARS:
            rob.append(row(f"Without {y}", S, c, years=[z for z in cal.YEARS if z != y]))
        rob.append(row("Weekday events only (2020-2023)", S, c, years=[2020, 2021, 2022, 2023]))
        rob.append(row("1 km/h floor years only (2021-2024)", S, c, years=[2021, 2022, 2023, 2024]))
    # weather: remove the part of M explained by rain and temperature (year-demeaned OLS)
    w = json.load(open("data/raw/aux/weather_istanbul_hourly.json"))["hourly"]
    wx = pd.DataFrame(w)
    wx["time"] = pd.to_datetime(wx["time"])
    wx = wx[wx.time.dt.hour.isin([7, 8, 9, 10])]
    wd = wx.groupby(wx.time.dt.normalize()).agg(
        rain=("precipitation", "sum"), temp=("temperature_2m", "mean")
    )
    for c in ("all", "50-70"):
        s = S[S.cls == c].merge(wd, left_on="date", right_index=True, how="left")
        s["wet"] = (s.rain >= 0.5).astype(float)
        X = s[["wet", "temp"]] - s.groupby("year")[["wet", "temp"]].transform("mean")
        yv = s.M - s.groupby("year").M.transform("mean")
        beta = np.linalg.lstsq(X.to_numpy(), yv.to_numpy(), rcond=None)[0]
        s2 = s.assign(M=s.M - X.to_numpy() @ beta)
        rob.append(row("Adjusted for rain and temperature", s2, c))
    pd.DataFrame(rob).to_csv(OUT / "table_robustness.csv", index=False)
    wd.loc[[cal.event(y) for y in cal.YEARS]].to_csv(OUT / "weather_event_days.csv")

    # ------------------------------------------------------------ other outcomes, placebo hours
    oth = []
    for o, lab, alt, yrs in (
        ("min_speed", "Minimum speed (log)", "less", None),
        ("max_speed", "Maximum speed (log)", "less", None),
        ("vehicles", "Number of vehicles (log)", "less", None),
        (
            "min_le2",
            "Share of cells with minimum speed <= 2 km/h",
            "greater",
            [2021, 2022, 2023, 2024],
        ),
    ):
        So = stats(cd, outcome=o)
        for c in ("all", "50-70"):
            oth.append(row(lab, So, c, years=yrs, alt=alt))
    for con, lab in (
        ("8", "Minimum speed (log), reference hour 08 only"),
        ("10", "Minimum speed (log), reference hour 10 only"),
    ):
        Sm = stats(cd, outcome="min_speed", contrast=con)
        for c in ("all", "50-70"):
            oth.append(row(lab, Sm, c))
    for con, lab in (
        ("h7", "Placebo hour 07 (vs 06 and 08)"),
        ("h11", "Placebo hour 11 (vs 10 and 12)"),
    ):
        Sp = stats(cd, contrast=con)
        for c in ("all", "50-70"):
            oth.append(row(lab, Sp, c))
    # which hour moves? each neighbouring hour against hours not adjacent to the event
    nb = []
    for con, lab in (("h8x", "08"), ("6,7,11,12", "09"), ("h10x", "10")):
        for o in ("speed",):
            Sn = stats(cd, contrast=con, outcome=o)
            for c in ("all", "50-70"):
                lo, hi = row(lab, Sn, c, alt="less"), row(lab, Sn, c, alt="greater")
                nb.append(dict(hour=lab, outcome=o, cls=c, est=lo["est"], p_slow=lo["p"], p_fast=hi["p"],
                               n_neg=lo["n_neg"], n_years=lo["n_years"], by_year=lo["by_year"]))  # fmt: skip
    pd.DataFrame(nb).to_csv(OUT / "table_neighbours.csv", index=False)
    for sh, lab in ((-1, "Placebo event on 9 November"), (1, "Placebo event on 11 November")):
        Sp = stats(cd, shift=sh)
        for c in ("all", "50-70"):
            oth.append(row(lab, Sp, c))
    Sl = stats(cd, outcome="speed_level")
    lev = pd.DataFrame([row("Average speed in levels (km/h)", Sl, c) for c in ("all", "50-70")])
    lev.to_csv(OUT / "table_levels.csv", index=False)

    # ------------------------------------------------------------ power and sensitivity
    pw, sens = [], {}
    for c in ("all", "50-70"):
        a = arrays(S, c)
        for mm in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0):
            pw.append(dict(cls=c, minutes=mm, power=dateri.power(a[0], a[1], mm)))
        sens[c] = dateri.sensitivity(a[0], a[1], gammas=(1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6))
    pd.DataFrame(pw).to_csv(OUT / "power.csv", index=False)
    json.dump(sens, open(OUT / "sensitivity.json", "w"), indent=1)
    pd.DataFrame(oth).to_csv(OUT / "table_outcomes.csv", index=False)

    # ------------------------------------------------------------ heterogeneity within 50-70
    C = geo.cells().drop_duplicates("GEOHASH").set_index("GEOHASH")

    def cls_of(y, dates):
        b = pooled.baseline_speed(cd, dates)
        return pd.cut(b, pooled.BINS, right=False, labels=pooled.LABELS).astype(str)

    def by(extra):
        def fn(y, dates):
            k = cls_of(y, dates)
            e = extra(y, dates, k.index)
            return (e.astype(str)).where((k == "50-70") & e.notna())

        return fn

    def veh(y, dates, idx):
        n = cd[cd.date.isin(dates)].groupby("GEOHASH").n9.mean().reindex(idx)
        return pd.cut(
            n, [0, 30, 100, 1e9], labels=["< 30 vehicles", "30-100 vehicles", "> 100 vehicles"]
        )

    het = []
    for name, extra in (
        ("Side of the Bosphorus", lambda y, d, idx: C.side.reindex(idx)),
        ("CHP vote share 2024 (district)", lambda y, d, idx: pd.cut(
            C.chp.reindex(idx), [0, 45, 52, 100], labels=["CHP < 45%", "CHP 45-52%", "CHP > 52%"])),
        ("Probe vehicles at 09h", veh),
    ):  # fmt: skip
        G = group_stats(cd, by(extra))
        labs = [c for c in G.cls.unique() if c != "all"]
        pyj = [np.column_stack([arrays(G, c, [y])[0][0] for c in labs]) for y in cal.YEARS]
        evj = [arrays(G, labs[0], [y])[1][0] for y in cal.YEARS]
        jt = dateri.test(pyj, evj)
        for i, c in enumerate(labs):
            r = row(name, G, c)
            r["group"] = c
            # is this group different from the first group listed? (two-sided)
            d_obs = jt["est"][i] - jt["est"][0]
            d_ref = jt["ref"][:, i] - jt["ref"][:, 0]
            r["p_diff_vs_first"] = (
                float((np.abs(d_ref) >= abs(d_obs) - 1e-12).mean()) if i else np.nan
            )
            het.append(r)
    pd.DataFrame(het).to_csv(OUT / "table_heterogeneity.csv", index=False)

    # district-level estimates (50-70 class cells are few per district, so all cells 30-90)
    def dist(y, dates):
        b = pooled.baseline_speed(cd, dates)
        return C.district.reindex(b.index).where((b >= 50) & (b < 70))

    G = group_stats(cd, dist)
    dr = []
    for c in [c for c in G.cls.unique() if c != "all"]:
        n = G[(G.cls == c) & (G.k == 0)].n
        if len(n) < 5 or n.min() < 5:
            continue
        r = row("district", G, c)
        r.update(
            district=c,
            chp=float(C[C.district == c].chp.iloc[0]),
            side=C[C.district == c].side.iloc[0],
        )
        dr.append(r)
    pd.DataFrame(dr).to_csv(OUT / "table_districts.csv", index=False)

    # ------------------------------------------------------------ dependence within a date
    C0 = pooled.contrast_matrix(cd, [d for d in cal.pool(2022) if d in set(cd.date.unique())])
    dev = C0.sub(C0.mean(axis=1), axis=0).dropna()
    var_cell = float(dev.var(axis=0, ddof=1).mean())
    var_date = float(dev.mean(axis=0).var(ddof=1))
    m = len(dev)
    icc = (var_date - var_cell / m) / var_cell
    json.dump(dict(year=2022, cells=m, var_cell=var_cell, var_date_mean=var_date,
                   naive_se=float(np.sqrt(var_cell / m)), date_sd=float(np.sqrt(var_date)),
                   design_effect=var_date / (var_cell / m), icc=icc),
              open(OUT / "dependence.json", "w"), indent=1)  # fmt: skip

    # ------------------------------------------------------------ hour-by-hour curvature
    have = set(cd.date.unique())
    H = pd.concat([pooled.hour_stats(y, [d for d in cal.pool(y, MAIN_WEEKS) if d in have], cd)
                   for y in cal.YEARS], ignore_index=True)  # fmt: skip
    H.to_csv(OUT / "hour_stats.csv", index=False)
    cur = []
    for c in ("all", "50-70"):
        W = (
            H[H.cls == c]
            .pivot_table(index=["year", "date", "k"], columns="hour", values="H")
            .reset_index()
        )
        for h in range(1, 23):
            if not {h - 1, h, h + 1} <= set(W.columns):
                continue
            Sx = W[["year", "date", "k"]].assign(cls=c, M=W[h] - (W[h - 1] + W[h + 1]) / 2, n=1)
            r = run(Sx, c)
            q = np.quantile(r["ref"], [0.05, 0.95])
            cur.append(dict(cls=c, hour=h, est=r["est"][0], p=r["p"][0], q05=q[0], q95=q[1],
                            n_neg=int((r["by_year"] < 0).sum())))  # fmt: skip
    pd.DataFrame(cur).to_csv(OUT / "hour_curvature.csv", index=False)

    # ------------------------------------------------------------ data audit: speed floor
    ch = pd.read_parquet(panel.DERIVED / "cityhour.parquet")
    # school break: speed at 07-08h on the date one week after the event vs neighbouring weeks
    brk = {}
    for y in (2020, 2021, 2022, 2023):
        ev = cal.event(y)
        dates = [ev + pd.Timedelta(weeks=k) for k in range(-4, 5) if k != 0]
        w = ch[ch.date.isin(dates) & ch.hour.isin([7, 8])].groupby("date").lv.mean()
        b_ = ev + pd.Timedelta(weeks=1)
        brk[y] = float(100 * (np.exp(w[b_] - w.drop(b_).mean()) - 1))
    json.dump(brk, open(OUT / "break_check.json", "w"), indent=1)
    ch["ym"] = ch.date.dt.to_period("M").astype(str)
    ch["w5"], ch["w1"] = ch.min_le5 * ch.n, ch.min_le1 * ch.n
    fl = ch.groupby("ym")[["n", "w5", "w1"]].sum()
    fl = pd.DataFrame(
        {"cell_hours": fl.n, "share_min_le5": fl.w5 / fl.n, "share_min_le1": fl.w1 / fl.n}
    )
    fl.to_csv(OUT / "floor_by_month.csv")
    print(
        main_t[
            ["cls", "est", "minutes", "p", "p_stepdown", "p_holm", "n_neg", "hl", "ci_lo", "ci_hi"]
        ].round(4)
    )
    print("omnibus p", omni)
    from saygi import bulk

    n_months = len(list(bulk.OUT.glob("traffic_density_*.parquet")))
    json.dump(dict(omnibus_p=omni, months=n_months, cell_hours=int(ch.n.sum())),
              open(OUT / "omnibus.json", "w"))  # fmt: skip


if __name__ == "__main__":
    main()
