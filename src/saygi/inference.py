"""Randomization inference over which day of each year is the event day."""

from __future__ import annotations

import itertools

import numpy as np
import pandas as pd

TREAT = 10


def ri(
    est: pd.DataFrame,
    treat: int = TREAT,
    alternative: str = "less",
    max_exact: int = 200_000,
    draws: int = 20_000,
    seed: int = 0,
):
    """est: rows = year, columns = candidate event days (NaN = date missing).

    Statistic: equal-weight mean over years of the treated day's estimate.
    Returns (observed, p, number_of_assignments). `alternative` is "less"
    (speed falls) or "greater" (e.g. travel time rises).
    """
    per_year = [row.dropna().to_numpy() for _, row in est.iterrows()]
    real = float(est[treat].mean())
    n = int(np.prod([len(v) for v in per_year]))
    if n <= max_exact:
        sims = np.array([np.mean(c) for c in itertools.product(*per_year)])
    else:
        rng = np.random.default_rng(seed)
        sims = np.mean([rng.choice(v, draws) for v in per_year], axis=0)
    if alternative == "less":
        p = float(np.mean(sims <= real + 1e-12))
    elif alternative == "greater":
        p = float(np.mean(sims >= real - 1e-12))
    else:
        raise ValueError(alternative)
    return real, p, n


def summarize(did_long: pd.DataFrame, treat: int = TREAT) -> pd.DataFrame:
    """Pilot's results_summary.csv from the long did_by_class table."""
    from .did import minutes

    rows = []
    for cls, g in did_long.groupby("cls", sort=False):
        est = g.pivot(index="year", columns="day", values="did")
        real, p, _ = ri(est, treat)
        plac = est[[d for d in est.columns if d != treat]].to_numpy().ravel()
        weekday = [y for y in (2021, 2022, 2023) if y in est.index]
        rows.append(
            dict(
                cls=cls,
                did=real,
                dk=minutes(real),
                sn=60 * minutes(real),
                p_RI=p,
                neg_years=f"{int((est[treat] < 0).sum())}/{len(est)}",
                placebo_mean=plac.mean(),
                placebo_sd=plac.std(ddof=1),
                did_2021_23=est.loc[weekday, treat].mean(),
                n_geo=int(g[g.day == treat].n.mean()),
            )
        )
    return pd.DataFrame(rows)
