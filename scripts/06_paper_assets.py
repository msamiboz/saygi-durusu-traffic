"""Turn data/derived/ into LaTeX tables (paper/tables/) and number macros
(paper/numbers.tex), so that no number in the manuscript is typed by hand."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

D, T = Path("data/derived"), Path("paper/tables")
T.mkdir(parents=True, exist_ok=True)
CLS = {
    "all": "All cells",
    "<30": "$<30$",
    "30-50": "30--50",
    "50-70": "50--70",
    ">=70": r"$\geq 70$",
}
macros: dict[str, str] = {}


def m(name: str, value) -> None:
    assert name.isalpha(), name
    macros[name] = str(value)


def f(x, d=2):
    s = f"{x:.{d}f}"
    if float(s) == 0:
        s = s.lstrip("-")
    return s.replace("-", r"\ensuremath{-}")


def pval(p):
    """Exact share of assignments: three decimals, four when below 0.001."""
    if p >= 0.001:
        return f"{p:.3f}"
    return f"{p:.4f}" if p >= 0.0001 else r"\ensuremath{<}0.0001"


def mins(x):
    return 60 * (1 - np.exp(x))


def write(name: str, lines: list[str]) -> None:
    (T / f"{name}.tex").write_text("\n".join(lines) + "\n")


def main() -> None:
    main_t = pd.read_csv(D / "table_main.csv")
    yrs = pd.read_csv(D / "table_years.csv")
    rob = pd.read_csv(D / "table_robustness.csv")
    oth = pd.read_csv(D / "table_outcomes.csv")
    het = pd.read_csv(D / "table_heterogeneity.csv")
    dif = pd.read_csv(D / "table_class_differences.csv")
    prof = pd.read_csv(D / "speed_profile.csv")
    cur = pd.read_csv(D / "hour_curvature.csv")
    idx = pd.read_csv(D / "index_2026_test.csv")
    ip = pd.read_csv(D / "index_2026_profile.csv")
    fl = pd.read_csv(D / "floor_by_month.csv")
    dist = pd.read_csv(D / "table_districts.csv")
    dep = json.load(open(D / "dependence.json"))
    meta = json.load(open(D / "omnibus.json"))
    omni = meta["omnibus_p"]
    S = pd.read_csv(D / "date_stats_main.csv")

    # ---------------- Table 1: sample by year
    L = [r"\begin{tabular}{llrrrr}", r"\toprule",
         r"Year & Weekday of & Dates in & Cells & Median probe & Lowest recorded \\",
         r" & 10 November & the pool & & vehicles, 09h & speed (km/h) \\", r"\midrule"]  # fmt: skip
    for _, r in yrs.iterrows():
        L.append(f"{int(r.year)} & {r.weekday} & {int(r.pool_dates)} & {int(r.cells):,} & "
                 f"{int(r.median_vehicles)} & {int(r.floor)} \\\\".replace(",", "\\,"))  # fmt: skip
    L += [r"\bottomrule", r"\end{tabular}"]
    write("sample", L)

    # ---------------- Table 2: main results
    L = [r"\begin{tabular}{lrrrrrrr}", r"\toprule",
         r"Usual 09h speed & Cells & Effect & Full-stop & 90\% interval & Years & \multicolumn{2}{c}{$p$-value} \\",
         r"\cmidrule(lr){7-8}",
         r"(km/h) & & ($\times 100$) & minutes & (minutes) & negative & single & stepdown \\", r"\midrule"]  # fmt: skip
    for _, r in main_t.iterrows():
        lo, hi = sorted([mins(r.ci_lo), mins(r.ci_hi)])
        sd = "--" if np.isnan(r.p_stepdown) else pval(r.p_stepdown)
        L.append(f"{CLS[r.cls]} & {int(r.cells):,} & {f(100 * r.est)} & {f(r.minutes)} & "
                 f"{f(lo)} to {f(hi)} & {int(r.n_neg)} of {int(r.n_years)} & {pval(r.p)} & {sd} \\\\"
                 .replace(",", "\\,"))  # fmt: skip
        if r.cls == "all":
            L.append(r"\addlinespace")
    L += [r"\bottomrule", r"\end{tabular}"]
    write("main", L)

    # ---------------- Table 3: robustness (all cells and 50-70 side by side)
    a = rob[rob.cls == "all"].set_index("spec")
    b = rob[rob.cls == "50-70"].set_index("spec")
    groups = [
        ("Placebo-date pool", ["Main: +-8 weeks, school-break dates dropped", "Pilot dates only (3, 17, 24 Nov)",
                               "Adjacent weeks only (3 and 17 Nov)", "+-4 weeks", "+-12 weeks",
                               "All same-weekday dates of the year", "School-break dates kept"]),
        ("Trend and scaling", ["Linear trend removed within year", "Quadratic trend removed within year",
                               "Statistic scaled by placebo s.d. (z)", "Rank statistic",
                               "Adjusted for rain and temperature"]),
        ("Reference hours", ["Reference hour 08 only", "Reference hour 10 only", "Reference hours 07, 08, 10, 11",
                             "Reference hours 07 and 11", "Reference hours 06, 07, 11, 12 (none adjacent)",
                             "Net of curvature at placebo hours 07 and 11"]),
        ("Cells", ["Balanced cells (observed on every date)", "Cells with >= 10 vehicles at 09h",
                   "Cells weighted by probe vehicles", "Speed class from other days"]),
        ("Years", [f"Without {y}" for y in range(2020, 2025)]
         + ["Weekday events only (2020-2023)", "1 km/h floor years only (2021-2024)"]),
    ]  # fmt: skip
    nice = {"Main: +-8 weeks, school-break dates dropped": r"Main specification ($\pm 8$ weeks)",
            "Reference hours 06, 07, 11, 12 (none adjacent)": "Reference hours 06, 07, 11, 12",
            "+-4 weeks": r"$\pm 4$ weeks", "+-12 weeks": r"$\pm 12$ weeks",
            "Cells with >= 10 vehicles at 09h": r"Cells with $\geq 10$ vehicles at 09h",
            "Statistic scaled by placebo s.d. (z)": "Statistic scaled by placebo s.d.",
            "Weekday events only (2020-2023)": "Weekday events only (2020--2023)",
            "1 km/h floor years only (2021-2024)": "1 km/h floor years only (2021--2024)"}  # fmt: skip
    L = [r"\begin{tabular}{lrrrrrr}", r"\toprule",
         r" & \multicolumn{3}{c}{All cells} & \multicolumn{3}{c}{Cells at 50--70 km/h} \\",
         r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}",
         r"Specification & Minutes & $p$ & Years $<0$ & Minutes & $p$ & Years $<0$ \\", r"\midrule"]  # fmt: skip
    for g, specs in groups:
        L.append(rf"\multicolumn{{7}}{{l}}{{\textit{{{g}}}}} \\")
        for s in specs:
            cells = []
            for t in (a, b):
                if s in t.index:
                    r = t.loc[s]
                    scaled = s.startswith("Statistic scaled") or s == "Rank statistic"
                    neg = int(r.n_neg) if s != "Rank statistic" else "--"
                    cells += ["--" if scaled else f(r.minutes), pval(r.p),
                              f"{neg} of {int(r.n_years)}" if neg != "--" else "--"]  # fmt: skip
                else:
                    cells += ["--", "--", "--"]
            L.append(f"\\quad {nice.get(s, s)} & " + " & ".join(cells) + r" \\")
        L.append(r"\addlinespace")
    L[-1] = r"\bottomrule"
    L.append(r"\end{tabular}")
    write("robustness", L)

    # ---------------- Table 4: other outcomes and placebo hours
    L = [r"\begin{tabular}{lrrrrrr}", r"\toprule",
         r" & \multicolumn{3}{c}{All cells} & \multicolumn{3}{c}{Cells at 50--70 km/h} \\",
         r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}",
         r"Outcome & Effect ($\times 100$) & $p$ & Years & Effect ($\times 100$) & $p$ & Years \\", r"\midrule"]  # fmt: skip
    first = [
        "Minimum speed (log)",
        "Minimum speed (log), reference hour 08 only",
        "Minimum speed (log), reference hour 10 only",
    ]
    for s in first + [x for x in oth.spec.unique() if x not in first]:
        if s.startswith("Placebo event"):
            L.append(r"\addlinespace") if s.endswith("9 November") else None
        cells = []
        for c in ("all", "50-70"):
            r = oth[(oth.spec == s) & (oth.cls == c)].iloc[0]
            k = int(r.n_pos) if s.startswith("Share") else int(r.n_neg)
            cells += [f(100 * r.est), pval(r.p), f"{k} of {int(r.n_years)}"]
        lab = s.replace("<=", r"$\leq$")
        if s.startswith("Placebo hour 07"):
            L.append(r"\addlinespace")
        lab = lab.replace("Minimum speed (log), reference", r"\quad reference")
        L.append(f"{lab} & " + " & ".join(cells) + r" \\")
    L += [r"\bottomrule", r"\end{tabular}"]
    write("outcomes", L)

    # ---------------- Table 5: heterogeneity within the 50-70 class
    L = [
        r"\begin{tabular}{lrrrrr}",
        r"\toprule",
        r"Group & Cells & Effect ($\times 100$) & Minutes & Years negative & $p$ \\",
        r"\midrule",
    ]
    order = {"Asia": 1, "Europe": 0, "CHP < 45%": 0, "CHP 45-52%": 1, "CHP > 52%": 2,
             "< 30 vehicles": 0, "30-100 vehicles": 1, "> 100 vehicles": 2}  # fmt: skip
    for s in het.spec.unique():
        L.append(rf"\multicolumn{{6}}{{l}}{{\textit{{{s}}}}} \\")
        for _, r in het[het.spec == s].sort_values("group", key=lambda x: x.map(order)).iterrows():
            g = (
                r.group.replace("<", "$<$")
                .replace(">", "$>$")
                .replace("%", r"\%")
                .replace("-", "--")
            )
            g = g.replace("Europe", "European side").replace("Asia", "Asian side")
            L.append(f"\\quad {g} & {int(r.cells)} & {f(100 * r.est)} & {f(r.minutes)} & "
                     f"{int(r.n_neg)} of {int(r.n_years)} & {pval(r.p)} \\\\")  # fmt: skip
        L.append(r"\addlinespace")
    L[-1] = r"\bottomrule"
    L.append(r"\end{tabular}")
    write("heterogeneity", L)

    # ---------------- Table 6: year-level estimates
    L = [
        r"\begin{tabular}{lrrrrr}",
        r"\toprule",
        r"Usual 09h speed (km/h) & 2020 & 2021 & 2022 & 2023 & 2024 \\",
        r"\midrule",
    ]
    for c in CLS:
        L.append(f"{CLS[c]} & " + " & ".join(f(100 * v) for v in yrs[f"est_{c}"]) + r" \\")
        if c == "all":
            L.append(r"\addlinespace")
    L += [r"\bottomrule", r"\end{tabular}"]
    write("years", L)

    # ---------------- regression tables
    rg = pd.read_csv(D / "regression_results.csv")
    rc = rg[rg.model == "controls"].set_index(["contrast", "cls"])
    rn = rg[rg.model == "nocontrols"].set_index(["contrast", "cls"])
    L = [r"\begin{tabular}{lrrrrrr}", r"\toprule",
         r" & \multicolumn{2}{c}{09 vs 08 and 10} & \multicolumn{2}{c}{09 vs 06, 07, 11, 12} & \multicolumn{2}{c}{09 vs 08} \\",
         r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}",
         r"Usual 09h speed (km/h) & Minutes & $p$ & Minutes & $p$ & Minutes & $p$ \\", r"\midrule"]  # fmt: skip
    for c in CLS:
        cells = []
        for con in ("main", "far", "pre"):
            r = rc.loc[(con, c)]
            cells += [f(r.minutes), pval(r.p)]
        L.append(f"{CLS[c]} & " + " & ".join(cells) + r" \\")
        if c == "all":
            L.append(r"\addlinespace")
    L += [r"\addlinespace", r"\multicolumn{7}{l}{\textit{Without weather controls}} \\"]
    for c in ("all", "50-70"):
        cells = []
        for con in ("main", "far", "pre"):
            r = rn.loc[(con, c)]
            cells += [f(r.minutes), pval(r.p)]
        L.append(f"\\quad {CLS[c]} & " + " & ".join(cells) + r" \\")
    L += [r"\bottomrule", r"\end{tabular}"]
    write("regression", L)
    pol = pd.read_csv(D / "regression_politics.csv")
    pw = pol.pivot_table(index=["source", "contrast", "cls"], columns="alt", values="p")
    pw["two"] = (2 * pw.min(axis=1)).clip(upper=1)
    pe = pol[pol.alt == "less"].set_index(["source", "contrast", "cls"])
    srcs = [
        ("district_local2024", "District"),
        ("mahalle_general2023", "General"),
        ("mahalle_local2024", "Neighbourhood"),
    ]
    L = [r"\begin{tabular}{lrrrrrr}", r"\toprule",
         r" & \multicolumn{2}{c}{District, 2024 local} & \multicolumn{2}{c}{Neighbourhood, 2023 general} & \multicolumn{2}{c}{Neighbourhood, 2024 local} \\",
         r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}",
         r"Usual 09h speed (km/h) & Slope & $p$ & Slope & $p$ & Slope & $p$ \\", r"\midrule"]  # fmt: skip
    for con, title in (("main", "Panel A: 09:00 against 08:00 and 10:00"),
                       ("far", "Panel B: 09:00 against 06:00, 07:00, 11:00 and 12:00")):  # fmt: skip
        L.append(rf"\multicolumn{{7}}{{l}}{{\textit{{{title}}}}} \\")
        for c in CLS:
            cells = []
            for src, _ in srcs:
                r, q = pe.loc[(src, con, c)], pw.loc[(src, con, c)]
                cells += [f(100 * r.est) + rf"$^{{{int(r.n_neg)}}}$", pval(q.two)]
            L.append(f"\\quad {CLS[c]} & " + " & ".join(cells) + r" \\")
        L.append(r"\addlinespace")
    L[-1] = r"\bottomrule"
    L.append(r"\end{tabular}")
    write("politics", L)
    for src, sn in srcs:
        fam = pw.loc[src].loc[["main", "far"]]
        m(f"nSig{sn}", int((fam.two < 0.05).sum()))
        for con, cn in (("main", "Main"), ("far", "Far")):
            for c, k in (("<30", "Slow"), ("50-70", "Fast"), ("30-50", "Mid"), ("all", "All")):
                m(f"slope{sn}{cn}{k}", f(100 * pe.loc[(src, con, c)].est))
                m(f"pSlope{sn}{cn}{k}", pval(pw.loc[(src, con, c)].two))
                m(f"negSlope{sn}{cn}{k}", int(pe.loc[(src, con, c)].n_neg))
                m(f"pSlope{sn}{cn}{k}Holm", pval(min(1.0, len(fam) * pw.loc[(src, con, c)].two)))
    m("nSlopeTests", 10)
    m("pSideRegMin", pval(pw.loc["side"].two.min()))
    cg = pd.read_csv(D / "cell_votes_mahalle_general2023.csv")
    m("nCellsGeneral", f"{len(cg):,}".replace(",", "\\,"))
    m("sdChpGeneral", f(cg.chp.std(), 1))
    cv = pd.read_csv(D / "cell_votes_mahalle_local2024.csv")
    m("nCellsMahalle", f"{len(cv):,}".replace(",", "\\,"))
    m("sdChpMahalle", f(cv.chp.std(), 1))
    m("medMatched", f"{100 * cv.matched_share.median():.0f}")
    for con, nm in (("main", "Main"), ("far", "Far"), ("pre", "Pre")):
        for c, cn in (("all", "All"), ("50-70", "Fast"), ("<30", "Slow"), ("30-50", "Mid")):
            m(f"reg{nm}{cn}", f(rc.loc[(con, c)].minutes))
            m(f"pReg{nm}{cn}", pval(rc.loc[(con, c)].p))
    m("regNoCtlFast", f(rn.loc[("main", "50-70")].minutes))
    m("pRegNoCtlFast", pval(rn.loc[("main", "50-70")].p))
    m("negRegMainFast", int(rc.loc[("main", "50-70")].n_neg))

    # ---------------- numbers
    g = main_t.set_index("cls")
    fast, allc = g.loc["50-70"], g.loc["all"]
    m("nYears", len(yrs))
    m("nDates", int(allc.dates))
    m("nPlacebo", int(allc.dates) - len(yrs))
    m("nAssign", f"{int(allc.n_assign):,}".replace(",", "\\,"))
    m("cellsAll", f"{int(allc.cells):,}".replace(",", "\\,"))
    m("cellsFast", int(fast.cells))
    m("shareFast", f"{100 * fast.cells / allc.cells:.0f}")
    m("estAll", f(100 * allc.est))
    m("minAll", f(allc.minutes))
    m("pAll", pval(allc.p))
    m("negAll", int(allc.n_neg))
    m("estFast", f(100 * fast.est))
    m("minFast", f(fast.minutes))
    m("secFast", f"{60 * fast.minutes:.0f}")
    m("pFast", pval(fast.p))
    m("pFastStep", pval(fast.p_stepdown))
    m("pFastHolm", pval(fast.p_holm))
    m("pFastSign", pval(fast.p_sign))
    lo, hi = sorted([mins(fast.ci_lo), mins(fast.ci_hi)])
    m("ciFastLo", f(lo))
    m("ciFastHi", f(hi))
    lo, hi = sorted([mins(allc.ci_lo), mins(allc.ci_hi)])
    m("ciAllLo", f(lo))
    m("ciAllHi", f(hi))
    m("pOmnibus", pval(omni))
    m("minMid", f(g.loc["30-50"].minutes))
    m("pMid", pval(g.loc["30-50"].p))
    m("pMidStep", pval(g.loc["30-50"].p_stepdown))
    m("minSlow", f(g.loc["<30"].minutes))
    m("pSlow", pval(g.loc["<30"].p))
    m("minMotor", f(g.loc[">=70"].minutes))
    m("pMotor", pval(g.loc[">=70"].p))
    for nm, lab in (("Slow", "<30"), ("Mid", "30-50"), ("Motor", ">=70")):
        r = dif[dif.contrast == f"50-70 minus {lab}"].iloc[0]
        m(f"pDiff{nm}", pval(r.p))
    rb = rob[rob.cls == "50-70"].set_index("spec")
    ra = rob[rob.cls == "all"].set_index("spec")
    names = {"Pilot": "Pilot dates only (3, 17, 24 Nov)", "Adjacent": "Adjacent weeks only (3 and 17 Nov)",
             "Four": "+-4 weeks", "Twelve": "+-12 weeks", "Year": "All same-weekday dates of the year",
             "Break": "School-break dates kept", "Trend": "Linear trend removed within year",
             "Pre": "Reference hour 08 only", "Post": "Reference hour 10 only",
             "Wide": "Reference hours 07, 08, 10, 11", "Net": "Net of curvature at placebo hours 07 and 11",
             "Other": "Speed class from other days", "Rain": "Adjusted for rain and temperature",
             "Weekday": "Weekday events only (2020-2023)", "Balanced": "Balanced cells (observed on every date)",
             "Rank": "Rank statistic"}  # fmt: skip
    for k, s in names.items():
        m(f"minRob{k}", f(rb.loc[s].minutes))
        m(f"pRob{k}", pval(rb.loc[s].p))
        if s in ra.index:
            m(f"minRobAll{k}", f(ra.loc[s].minutes))
            m(f"pRobAll{k}", pval(ra.loc[s].p))
    m("nAssignYear", f"{int(rb.loc[names['Year']].n_assign):,}".replace(",", "\\,"))
    loo = rb.loc[[f"Without {y}" for y in range(2020, 2025)]]
    m("minLooLo", f(loo.minutes.min()))
    m("minLooHi", f(loo.minutes.max()))
    m("pLooMax", pval(loo.p.max()))
    allspecs = rb[~rb.index.isin(["Statistic scaled by placebo s.d. (z)", "Rank statistic"])]
    m("minRobLo", f(allspecs.minutes.min()))
    m("minRobHi", f(allspecs.minutes.max()))
    m("nRobSpecs", len(rb))
    m("nRobSig", int((rb.p < 0.05).sum()))
    o = oth.set_index(["spec", "cls"])
    r = o.loc[("Minimum speed (log)", "50-70")]
    m("minspFast", f(100 * r.est))
    m("minspFastPct", f(100 * (1 - np.exp(r.est)), 1))
    m("pMinspFast", pval(r.p))
    r = o.loc[("Minimum speed (log)", "all")]
    m("minspAll", f(100 * r.est))
    m("minspAllPct", f(100 * (1 - np.exp(r.est)), 1))
    m("pMinspAll", pval(r.p))
    m("negMinspAll", int(r.n_neg))
    m("pMaxFast", pval(o.loc[("Maximum speed (log)", "50-70")].p))
    m("maxFast", f(100 * o.loc[("Maximum speed (log)", "50-70")].est))
    m("pVehFast", pval(o.loc[("Number of vehicles (log)", "50-70")].p))
    m("vehFast", f(100 * o.loc[("Number of vehicles (log)", "50-70")].est))
    r = o.loc[("Share of cells with minimum speed <= 2 km/h", "50-70")]
    m("floorShareFast", f(100 * r.est, 1))
    m("pFloorShareFast", pval(r.p))
    for h in ("07", "11"):
        key = [
            k for k in o.index.get_level_values(0).unique() if k.startswith(f"Placebo hour {h}")
        ][0]
        nm = "Seven" if h == "07" else "Eleven"
        m(f"plac{nm}Fast", f(100 * o.loc[(key, "50-70")].est))
        m(f"pPlac{nm}Fast", pval(o.loc[(key, "50-70")].p))
        m(f"plac{nm}All", f(100 * o.loc[(key, "all")].est))
        m(f"pPlac{nm}All", pval(o.loc[(key, "all")].p))
    c9 = cur[(cur.cls == "50-70")]
    m("nHoursLow", int((c9.est < c9.q05).sum()))
    m("nHours", len(c9))
    low = [f"{h:02d}" for h in c9[c9.est < c9.q05].hour]
    m("hoursLowList", (", ".join(low[:-1]) + " and " + low[-1]) if len(low) > 1 else "".join(low))
    m("curNine", f(100 * c9[c9.hour == 9].est.iloc[0]))
    m("pCurNine", pval(c9[c9.hour == 9].p.iloc[0]))
    m("curTen", f(100 * c9[c9.hour == 10].est.iloc[0]))
    m("curEight", f(100 * c9[c9.hour == 8].est.iloc[0]))
    # speed profile
    pb = prof.set_index("bin")
    m("minBinFifty", f(mins(pb.loc["[50, 60)"].est)))
    m("pBinFifty", pval(pb.loc["[50, 60)"].p))
    m("minBinSixty", f(mins(pb.loc["[60, 70)"].est)))
    m("pBinSixty", pval(pb.loc["[60, 70)"].p))
    # heterogeneity
    h = het.set_index("group")
    m("minEurope", f(h.loc["Europe"].minutes))
    m("minAsia", f(h.loc["Asia"].minutes))
    m("pSideDiff", pval(max(h.loc["Europe"].p_diff_vs_first, 0) if not np.isnan(h.loc["Europe"].p_diff_vs_first)
                        else h.loc["Asia"].p_diff_vs_first))  # fmt: skip
    m("minChpLow", f(h.loc["CHP < 45%"].minutes))
    m("minChpMid", f(h.loc["CHP 45-52%"].minutes))
    m("minChpHigh", f(h.loc["CHP > 52%"].minutes))
    pol = het[het.spec.str.startswith("CHP")]
    m("pChpDiffMin", pval(pol.p_diff_vs_first.min()))
    m("nDistricts", len(dist))
    m("corrChp", f(np.corrcoef(dist.chp, dist.est)[0, 1]))
    m("nDistNeg", int((dist.est < 0).sum()))
    # dependence
    m("designEffect", f(dep["design_effect"], 1))
    m("naiveSe", f(100 * dep["naive_se"]))
    m("dateSd", f(100 * dep["date_sd"]))
    # years
    y = yrs.set_index("year")
    for yy, nm in zip(
        range(2020, 2025), ("Twenty", "TwentyOne", "TwentyTwo", "TwentyThree", "TwentyFour")
    ):
        m(f"minFast{nm}", f(mins(y.loc[yy, "est_50-70"])))
        m(f"pool{nm}", int(y.loc[yy, "pool_dates"]))
    ym = {yy: mins(y.loc[yy, "est_50-70"]) for yy in range(2020, 2025)}
    lo_y, hi_y = min(ym, key=ym.get), max(ym, key=ym.get)
    m("yearFastLo", lo_y)
    m("yearFastHi", hi_y)
    m("minFastYearLo", f(ym[lo_y]))
    m("minFastYearHi", f(ym[hi_y]))
    # speed floor
    fl["y"] = fl.ym.str[:4].astype(int)
    m("floorShareEarly", f(100 * fl[fl.y == 2020].share_min_le5.mean(), 1))
    m("floorShareLate", f(100 * fl[fl.y >= 2021].share_min_le5.mean(), 0))
    m("nMonths", meta["months"])
    m("cellHours", f"{meta['cell_hours'] / 1e6:.0f}")
    # index 2026
    r = idx[idx.gap == 20].iloc[0]
    m("idxStat", f(r.event, 1))
    m("idxCtrlMean", f(r.control_mean, 1))
    m("idxCtrlSd", f(r.control_sd, 1))
    m("idxN", int(r.n_control))
    m("idxRank", int(r.rank_high))
    m("idxP", pval(r.p_high))
    m("idxRankShort", int(idx[idx.gap == 15].rank_high.iloc[0]))
    m("idxRankLong", int(idx[idx.gap == 30].rank_high.iloc[0]))
    e = ip.set_index("bin")
    m("idxBefore", int(e.loc[540, "event_raw"]))
    m("idxAfter", int(e.loc[550, "event_raw"]))
    m("idxFall", int(e.loc[540, "event_raw"] - e.loc[550, "event_raw"]))
    brk = json.load(open(D / "break_check.json"))
    late = [brk[k] for k in ("2021", "2022", "2023")]
    m("breakLo", f"{min(late):.0f}")
    m("breakHi", f"{max(late):.0f}")
    m("vehLo", int(yrs.median_vehicles.min()))
    m("vehHi", int(yrs.median_vehicles.max()))
    sens = json.load(open(D / "sensitivity.json"))["50-70"]
    ok = [float(k) for k, v in sens.items() if v < 0.05]
    m("gammaMax", f"{max(ok):g}")
    pw = pd.read_csv(D / "power.csv").set_index(["cls", "minutes"]).power
    m("powerAllHalf", f"{100 * pw[('all', 0.5)]:.0f}")
    m("powerFastHalf", f"{100 * pw[('50-70', 0.5)]:.0f}")
    m("powerAllQuarter", f"{100 * pw[('all', 0.25)]:.0f}")
    m("powerFastQuarter", f"{100 * pw[('50-70', 0.25)]:.0f}")
    far = rb.loc["Reference hours 06, 07, 11, 12 (none adjacent)"]
    m("minRobFar", f(far.minutes))
    m("pRobFar", pval(far.p))
    m("negRobFar", int(far.n_neg))
    fa = ra.loc["Reference hours 06, 07, 11, 12 (none adjacent)"]
    m("minRobAllFar", f(fa.minutes))
    m("pRobAllFar", pval(fa.p))
    nbt = pd.read_csv(D / "table_neighbours.csv").set_index(["hour", "cls"])
    m("estTenFast", f(100 * nbt.loc[(10, "50-70"), "est"]))
    m("pTenFast", pval(nbt.loc[(10, "50-70"), "p_fast"]))
    m("posTenFast", int(nbt.loc[(10, "50-70"), "n_years"] - nbt.loc[(10, "50-70"), "n_neg"]))
    m("estTenAll", f(100 * nbt.loc[(10, "all"), "est"]))
    m("pTenAll", pval(nbt.loc[(10, "all"), "p_fast"]))
    m("estEightFast", f(100 * nbt.loc[(8, "50-70"), "est"]))
    m("pEightFast", pval(nbt.loc[(8, "50-70"), "p_slow"]))
    m("estNineFar", f(100 * nbt.loc[(9, "50-70"), "est"]))
    m("pRobZ", pval(rb.loc["Statistic scaled by placebo s.d. (z)"].p))
    m("minRobTen", f(rb.loc["Cells with >= 10 vehicles at 09h"].minutes))
    m("minRobQuad", f(rb.loc["Quadratic trend removed within year"].minutes))
    pools = rb.loc[[names[k] for k in ("Pilot", "Adjacent", "Four", "Twelve", "Year", "Break")]]
    m("minPoolLo", f(min(pools.minutes.min(), fast.minutes)))
    m("minPoolHi", f(max(pools.minutes.max(), fast.minutes)))
    m("pPoolMax", pval(max(pools.p.max(), fast.p)))
    msp = o.loc[("Minimum speed (log), reference hour 08 only", "50-70")]
    m("minspPreFast", f(100 * (1 - np.exp(msp.est)), 1))
    m("pMinspPreFast", pval(msp.p))
    msq = o.loc[("Minimum speed (log), reference hour 10 only", "50-70")]
    m("minspPostFast", f(100 * (1 - np.exp(msq.est)), 1))
    m("pMinspPostFast", pval(msq.p))
    wv = rb.loc["Cells weighted by probe vehicles"]
    m("minRobWeighted", f(wv.minutes))
    m("pRobWeighted", pval(wv.p))
    # pool description
    S["date"] = pd.to_datetime(S.date)
    m("poolFirst", S.date.dt.strftime("%d %B").iloc[S.k.argmin()].lstrip("0"))
    # results table in README.md, between the two markers
    names_md = {
        "all": "All cells",
        "<30": "< 30",
        "30-50": "30–50",
        "50-70": "50–70",
        ">=70": "≥ 70",
    }
    md = [
        "| Usual 09h speed (km/h) | Cells | Effect (log points ×100) | Full-stop minutes | 90% interval (min) "
        "| Years negative | p | p (stepdown) |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for _, r in main_t.iterrows():
        lo, hi = sorted([mins(r.ci_lo), mins(r.ci_hi)])
        sd = "" if np.isnan(r.p_stepdown) else f"{r.p_stepdown:.3f}"
        md.append(
            f"| {names_md[r.cls]} | {int(r.cells):,} | {100 * r.est:.2f} | {r.minutes:.2f} | "
            f"{lo:.2f} to {hi:.2f} | {int(r.n_neg)} of {int(r.n_years)} | {r.p:.3f} | {sd} |"
        )
    md += [
        "",
        f"Reference-hour check, 50–70 km/h cells: against 08:00 only {rb.loc[names['Pre']].minutes:.2f} min "
        f"(p = {rb.loc[names['Pre']].p:.3f}); against 10:00 only {rb.loc[names['Post']].minutes:.2f} min "
        f"(p = {rb.loc[names['Post']].p:.3f}); against 06, 07, 11, 12 {far.minutes:.2f} min (p = {far.p:.3f}). "
        f"{int(allc.dates)} dates, {int(allc.n_assign):,} assignments.",
    ]
    readme = Path("README.md")
    if readme.exists() and "<!-- results:start -->" in readme.read_text():
        txt = readme.read_text()
        i, j = txt.index("<!-- results:start -->"), txt.index("<!-- results:end -->")
        readme.write_text(txt[:i] + "<!-- results:start -->\n" + "\n".join(md) + "\n" + txt[j:])
    out = ["% generated by scripts/06_paper_assets.py -- do not edit"]
    out += [f"\\newcommand{{\\{k}}}{{{v}}}" for k, v in macros.items()]
    Path("paper/numbers.tex").write_text("\n".join(out) + "\n")
    print(len(macros), "macros,", len(list(T.glob("*.tex"))), "tables")


if __name__ == "__main__":
    main()
