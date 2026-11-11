"""Figures of the paper (static, print-first). One accent colour for the event,
neutral grey for placebo dates; identity is also carried by marker shape/fill."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from . import dateri  # noqa: E402

EVENT, PLACEBO, INK, MUTED, GRID = "#2a78d6", "#8a8985", "#0b0b0b", "#52514e", "#e4e3df"
plt.rcParams.update({
    "font.size": 8, "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": MUTED,
    "ytick.color": MUTED, "axes.linewidth": 0.6, "axes.spines.top": False,
    "axes.spines.right": False, "legend.frameon": False, "savefig.bbox": "tight",
    "pdf.fonttype": 42, "font.family": "DejaVu Sans",
})  # fmt: skip


def _save(fig, path):
    fig.savefig(f"{path}.pdf")
    fig.savefig(f"{path}.png", dpi=200)
    plt.close(fig)


def placebo_dates(S: pd.DataFrame, path, classes=("all", "50-70"),
                  titles=("All cells", "Cells at 50-70 km/h")) -> None:  # fmt: skip
    fig, axes = plt.subplots(1, len(classes), figsize=(6.8, 2.6), sharey=True, sharex=True)
    rng = np.random.default_rng(3)
    for ax, c, title in zip(axes, classes, titles):
        s = S[S.cls == c]
        years = sorted(s.year.unique())
        for i, y in enumerate(years):
            g = s[s.year == y].dropna(subset=["M"]).sort_values("date").reset_index(drop=True)
            T = dateri.loo_stat(g.M.to_numpy()) * 100
            ev = g.k.to_numpy() == 0
            ax.scatter(T[~ev], i + rng.uniform(-0.13, 0.13, (~ev).sum()), s=16, facecolors="none",
                       edgecolors=PLACEBO, linewidths=0.8, zorder=2,
                       label="Placebo dates (same weekday)" if i == 0 else None)  # fmt: skip
            ax.scatter(T[ev], [i], s=34, color=EVENT, marker="D", zorder=3, edgecolors="white",
                       linewidths=0.6, label="10 November" if i == 0 else None)  # fmt: skip
        ax.axvline(0, color=MUTED, lw=0.6, zorder=1)
        ax.set_yticks(range(len(years)), [str(y) for y in years])
        ax.set_title(title, fontsize=8.5, loc="left", color=INK)
        ax.set_xlabel(
            "09h speed relative to 08h and 10h,\ndate minus other dates (log points × 100)"
        )
        ax.grid(axis="x", color=GRID, lw=0.5)
        ax.invert_yaxis()
    axes[0].legend(
        loc="upper left", bbox_to_anchor=(0, 1.32), ncol=2, fontsize=7.5, handletextpad=0.3
    )
    _save(fig, path)


def speed_profile(prof: pd.DataFrame, path) -> None:
    fig, ax = plt.subplots(figsize=(4.6, 2.7))
    x = np.arange(len(prof))
    ax.vlines(x, prof.q05 * 100, prof.q95 * 100, color=PLACEBO, lw=5, alpha=0.35, zorder=1,
              label="5th-95th percentile under random dates")  # fmt: skip
    ax.scatter(x, prof.est * 100, s=30, color=EVENT, marker="D", zorder=3, edgecolors="white",
               linewidths=0.6, label="10 November")  # fmt: skip
    ax.axhline(0, color=MUTED, lw=0.6)
    labs = [b.replace("[", "").replace(")", "").replace(", ", "-") for b in prof.bin]
    labs[-1] = "≥" + labs[-1].split("-")[0]
    ax.set_xticks(x, labs)
    ax.set_xlabel("Cell's usual 09h speed (km/h)")
    ax.set_ylabel("Effect on 09h speed\n(log points × 100)")
    ax.grid(axis="y", color=GRID, lw=0.5)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, fontsize=7.5, handletextpad=0.4)
    _save(fig, path)


def hour_curvature(cur: pd.DataFrame, path, cls="50-70") -> None:
    c = cur[cur.cls == cls]
    fig, ax = plt.subplots(figsize=(4.8, 2.6))
    ax.vlines(c.hour, c.q05 * 100, c.q95 * 100, color=PLACEBO, lw=5, alpha=0.35, zorder=1,
              label="5th-95th percentile under random dates")  # fmt: skip
    ax.scatter(c.hour, c.est * 100, s=26, color=EVENT, marker="D", zorder=3, edgecolors="white",
               linewidths=0.6, label="10 November")  # fmt: skip
    ax.axhline(0, color=MUTED, lw=0.6)
    ax.set_xticks(range(1, 23, 2), [f"{h:02d}" for h in range(1, 23, 2)])
    ax.set_xlabel("Hour h")
    ax.set_ylabel("Speed in hour h relative to h−1 and h+1\n(log points × 100)")
    ax.grid(axis="y", color=GRID, lw=0.5)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, fontsize=7.5, handletextpad=0.4)
    _save(fig, path)


def index_2026(prof: pd.DataFrame, path) -> None:
    fig, ax = plt.subplots(figsize=(4.8, 2.6))
    t = prof.bin / 60
    ax.fill_between(t, prof.control_q10, prof.control_q90, color=PLACEBO, alpha=0.25, lw=0,
                    label="Other weekdays, 10th-90th percentile")  # fmt: skip
    ax.plot(t, prof.control_median, color=PLACEBO, lw=1.2, label="Other weekdays, median")
    ax.plot(t, prof.event, color=EVENT, lw=1.8, marker="o", ms=2.5, label="10 November 2026")
    ax.axvline(9 + 5 / 60, color=INK, lw=0.7, ls=(0, (3, 2)))
    ax.text(9 + 5 / 60 + 0.02, ax.get_ylim()[1], "09:05", va="top", fontsize=7.5, color=INK)
    ax.set_xticks(
        [8, 8.5, 9, 9.5, 10, 10.5], ["08:00", "08:30", "09:00", "09:30", "10:00", "10:30"]
    )
    ax.set_xlabel("Time of day")
    ax.set_ylabel("Traffic index minus the day's\n08:00-10:30 mean (points)")
    ax.grid(axis="y", color=GRID, lw=0.5)
    ax.legend(loc="lower left", fontsize=7.5)
    _save(fig, path)


def floor(fl: pd.DataFrame, path) -> None:
    fig, ax = plt.subplots(figsize=(4.8, 2.3))
    x = pd.PeriodIndex(fl.ym, freq="M").to_timestamp()
    ax.plot(x, fl.share_min_le5 * 100, color=EVENT, lw=0, marker="o", ms=3.5, mfc="none", mew=0.9)
    ax.set_ylabel("Cell-hours with minimum\nspeed ≤ 5 km/h (%)")
    ax.set_xlabel("Month")
    ax.set_ylim(-2, None)
    ax.grid(axis="y", color=GRID, lw=0.5)
    _save(fig, path)


def districts(d: pd.DataFrame, path) -> None:
    fig, ax = plt.subplots(figsize=(4.6, 2.8))
    for side, mk in (("Europe", "o"), ("Asia", "s")):
        g = d[d.side == side]
        ax.scatter(g.chp, g.est * 100, s=22, marker=mk, facecolors="none", edgecolors=EVENT,
                   linewidths=1.0, label="European side" if side == "Europe" else "Asian side")  # fmt: skip
    ax.axhline(0, color=MUTED, lw=0.6)
    ax.set_xlabel("CHP vote share in the district, 2024 mayoral election (%)")
    ax.set_ylabel("Effect on 09h speed\n(log points × 100)")
    ax.grid(axis="y", color=GRID, lw=0.5)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, fontsize=7.5, handletextpad=0.4)
    _save(fig, path)


def residuals(P: pd.DataFrame, S: pd.DataFrame, fitted, resid, path) -> None:
    """Four-panel residual diagnostic for the fixed-effects regression."""
    fig, ax = plt.subplots(2, 2, figsize=(7.4, 5.6))
    # A: hourly profile, 50-70 cells
    a = ax[0, 0]
    pl = P[~P.event]
    for (_, _), g in pl.groupby(["year", "date"]):
        g = g.sort_values("hour")
        a.plot(g.hour, g.R * 100, color=PLACEBO, lw=0.6, alpha=0.35)
    ev = P[P.event].groupby("hour").R.mean() * 100
    a.plot(
        ev.index,
        ev.values,
        color=EVENT,
        lw=2,
        marker="D",
        ms=4,
        label="10 November (mean of 5 years)",
    )
    a.plot([], [], color=PLACEBO, lw=0.8, label="Placebo dates")
    a.axhline(0, color=MUTED, lw=0.6)
    a.axvspan(8.5, 9.5, color=EVENT, alpha=0.07, lw=0)
    a.set_xlabel("Hour")
    a.set_ylabel("Mean residual (log points × 100)")
    a.set_title("A  Hourly residuals, 50–70 km/h cells", loc="left", fontsize=8.5)
    a.legend(fontsize=7, loc="lower left")
    # B: distribution
    b = ax[0, 1]
    b.hist(resid * 100, bins=np.linspace(-60, 60, 121), color=EVENT, alpha=0.75)
    b.set_yscale("log")
    b.set_xlabel("Cell-hour residual (log points × 100)")
    b.set_ylabel("Count (log scale)")
    b.set_title("B  Distribution of residuals", loc="left", fontsize=8.5)
    # C: residual vs fitted, binned
    c = ax[1, 0]
    fv = np.exp(np.asarray(fitted))
    bins = np.quantile(fv, np.linspace(0, 1, 31))
    idx = np.clip(np.digitize(fv, bins) - 1, 0, 29)
    mid = [np.median(fv[idx == i]) for i in range(30)]
    q = [np.quantile(resid[idx == i] * 100, [0.1, 0.5, 0.9]) for i in range(30)]
    q = np.array(q)
    c.fill_between(
        mid, q[:, 0], q[:, 2], color=PLACEBO, alpha=0.3, lw=0, label="10th–90th percentile"
    )
    c.plot(mid, q[:, 1], color=EVENT, lw=1.6, label="Median")
    c.axhline(0, color=MUTED, lw=0.6)
    c.set_xscale("log")
    c.set_xlabel("Fitted speed (km/h, log scale)")
    c.set_ylabel("Residual (log points × 100)")
    c.set_title("C  Residuals against fitted values", loc="left", fontsize=8.5)
    c.legend(fontsize=7, loc="upper right")
    # D: date-level contrast
    d = ax[1, 1]
    s = S[S.cls == "50-70"]
    rng = np.random.default_rng(3)
    for i, (_y, g) in enumerate(s.groupby("year")):
        e = g.k == 0
        d.scatter(g.M[~e] * 100, i + rng.uniform(-0.15, 0.15, (~e).sum()), s=14, facecolors="none",
                  edgecolors=PLACEBO, linewidths=0.8)  # fmt: skip
        d.scatter(
            g.M[e] * 100, [i], s=34, color=EVENT, marker="D", edgecolors="white", linewidths=0.6
        )
    d.set_yticks(range(5), [str(y) for y in sorted(s.year.unique())])
    d.axvline(0, color=MUTED, lw=0.6)
    d.invert_yaxis()
    d.set_xlabel("09h vs 08h and 10h, residual (log points × 100)")
    d.set_title("D  Date-level contrast, 50–70 km/h cells", loc="left", fontsize=8.5)
    for axx in ax.ravel():
        axx.grid(axis="y", color=GRID, lw=0.5)
    fig.tight_layout()
    _save(fig, path)


def residuals_tails(samp: dict, stats: dict, path) -> None:
    """2 x 4 residual diagnostic: rows A (precision weighting) and B (robust background)."""
    from scipy import stats as st

    titles = {"A": "A  Precision weighting", "B": "B  Robust background (Huber fit)"}
    fig, ax = plt.subplots(2, 4, figsize=(10.5, 5.2))
    for i, k in enumerate(("A", "B")):
        e = samp[k].e.to_numpy()
        z = (e - e.mean()) / e.std()
        # distribution vs normal, log scale
        a = ax[i, 0]
        bins = np.linspace(-8, 8, 97)
        a.hist(z, bins=bins, density=True, color=EVENT, alpha=0.7, label="Residuals")
        a.plot(bins, st.norm.pdf(bins), color=INK, lw=1, label="Normal")
        a.set_yscale("log")
        a.set_ylim(1e-6, 1)
        a.set_xlabel("Standardized residual")
        a.set_ylabel(titles[k] + "\n\nDensity (log scale)")
        a.legend(fontsize=6.5, loc="upper right")
        # Q-Q
        b = ax[i, 1]
        q = np.linspace(0.0005, 0.9995, 400)
        b.plot(st.norm.ppf(q), np.quantile(z, q), color=EVENT, lw=1.6)
        lim = [-4, 4]
        b.plot(lim, lim, color=MUTED, lw=0.7, ls=(0, (3, 2)))
        b.set_xlabel("Normal quantile")
        b.set_ylabel("Residual quantile")
        # residual vs fitted (binned)
        c = ax[i, 2]
        fv = samp[k].fitted.to_numpy()
        edges = np.quantile(fv, np.linspace(0, 1, 31))
        idx = np.clip(np.digitize(fv, edges) - 1, 0, 29)
        mid = np.array([np.median(fv[idx == j]) for j in range(30)])
        qq = np.array([np.quantile(z[idx == j], [0.1, 0.5, 0.9]) for j in range(30)])
        c.fill_between(
            mid, qq[:, 0], qq[:, 2], color=PLACEBO, alpha=0.3, lw=0, label="10th–90th pct"
        )
        c.plot(mid, qq[:, 1], color=EVENT, lw=1.5, label="Median")
        c.axhline(0, color=MUTED, lw=0.6)
        c.set_xscale("log")
        c.set_xticks([20, 30, 50, 70, 100], ["20", "30", "50", "70", "100"])
        c.minorticks_off()
        c.set_xlabel("Fitted speed (km/h)")
        c.set_ylabel("Standardized residual")
        c.legend(fontsize=6.5, loc="upper right")
        # date-level contrast, 50-70
        d = ax[i, 3]
        s = stats[k]
        s = s[(s.cls == "50-70") & (s.contrast == "main")]
        rng = np.random.default_rng(3)
        for j, (_y, g) in enumerate(s.groupby("year")):
            ev = g.k == 0
            T = (g.M - (g.M.sum() - g.M) / (len(g) - 1)) * 100
            d.scatter(T[~ev], j + rng.uniform(-0.15, 0.15, (~ev).sum()), s=12, facecolors="none",
                      edgecolors=PLACEBO, linewidths=0.8)  # fmt: skip
            d.scatter(T[ev], [j], s=30, color=EVENT, marker="D", edgecolors="white", linewidths=0.6)
        d.set_yticks(range(5), [str(y) for y in sorted(s.year.unique())])
        d.axvline(0, color=MUTED, lw=0.6)
        d.invert_yaxis()
        d.set_xlabel("09h contrast, date minus\nother dates (log points × 100)")
        for axx in ax[i]:
            axx.grid(axis="y", color=GRID, lw=0.5)
    for j, t in enumerate(
        ("Distribution", "Normal Q–Q", "Residual vs fitted", "Date level, 50–70 km/h")
    ):
        ax[0, j].set_title(t, fontsize=8.5, loc="left")
    fig.tight_layout()
    _save(fig, path)
