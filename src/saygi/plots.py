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
