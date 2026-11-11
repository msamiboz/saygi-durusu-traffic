"""Stage 2: estimation and randomization inference on date-level statistics.

Input everywhere: `per_year`, a list (one entry per year) of arrays M with shape
(K_y,) or (K_y, m) for m outcomes/classes, and `ev`, the index of the event
date in each array. The statistic for "date d is the event" is the symmetric
difference from the other dates of the year,

    T_y(d) = M_y(d) - mean_{d' != d} M_y(d'),

optionally after removing a within-year linear trend fitted without d. The
pooled statistic is the equal-weight mean over years. The reference set is all
assignments of one date per year (exact enumeration, Monte Carlo if too many).
"""

from __future__ import annotations

import itertools

import numpy as np


def loo_stat(M: np.ndarray, t: np.ndarray | None = None, detrend: int = 0) -> np.ndarray:
    """T(d) for every date d. detrend = polynomial degree fitted on the other dates."""
    M = np.asarray(M, float)
    M2 = M.reshape(len(M), -1)
    K = len(M2)
    if detrend == 0:
        out = M2 - (M2.sum(0) - M2) / (K - 1)
    else:
        out = np.empty_like(M2)
        for i in range(K):
            m = np.arange(K) != i
            for j in range(M2.shape[1]):
                coef = np.polyfit(t[m], M2[m, j], detrend)
                out[i, j] = M2[i, j] - np.polyval(coef, t[i])
    return out.reshape(M.shape)


def scale(T: np.ndarray, ev: int, how: str) -> np.ndarray:
    """Optional within-year rescaling: 'z' (placebo sd) or 'rank' (mid-rank / K)."""
    T2 = T.reshape(len(T), -1)
    if how == "raw":
        return T
    if how == "z":
        sd = np.delete(T2, ev, axis=0).std(axis=0, ddof=1)
        return (T2 / sd).reshape(T.shape)
    if how == "rank":
        r = (T2[None, :, :] < T2[:, None, :]).sum(1) + 0.5 * (T2[None, :, :] == T2[:, None, :]).sum(
            1
        )
        return (r / len(T2)).reshape(T.shape)
    raise ValueError(how)


def reference(stats: list[np.ndarray], max_exact: int = 6_000_000, draws: int = 2_000_000,
              seed: int = 0) -> np.ndarray:  # fmt: skip
    """Pooled means over every assignment. stats[y] has shape (K_y, m)."""
    stats = [s.reshape(len(s), -1) for s in stats]
    n = int(np.prod([len(s) for s in stats]))
    if n <= max_exact:
        acc = stats[0]
        for s in stats[1:]:
            acc = (acc[:, None, :] + s[None, :, :]).reshape(-1, s.shape[1])
        return acc / len(stats)
    rng = np.random.default_rng(seed)
    acc = sum(s[rng.integers(0, len(s), draws)] for s in stats)
    return acc / len(stats)


def test(per_year, ev, t=None, detrend=0, how="raw", alternative="less", **kw) -> dict:
    """Pooled estimate, per-year estimates and one-sided randomization p-value."""
    T = [scale(loo_stat(M, None if t is None else t[i], detrend), ev[i], how)
         for i, M in enumerate(per_year)]  # fmt: skip
    by_year = np.array([np.atleast_1d(T[i][ev[i]]) for i in range(len(T))])
    obs = by_year.mean(axis=0)
    ref = reference(T, **kw)
    exact = len(ref) == int(np.prod([len(x) for x in T]))
    sign = 1 if alternative == "less" else -1
    le = (sign * ref <= sign * obs + 1e-12).mean(axis=0)
    p = le if exact else (le * len(ref) + 1) / (len(ref) + 1)
    return dict(est=obs, by_year=by_year, p=np.atleast_1d(p), n_assign=int(np.prod([len(x) for x in T])),
                exact=exact, ref=ref)  # fmt: skip


def stepdown(obs: np.ndarray, ref: np.ndarray) -> np.ndarray:
    """Romano-Wolf (2005) stepdown min-statistic adjusted p-values, one-sided (less).

    obs (m,), ref (N, m): the joint reference distribution, same assignment in
    every column. Columns are first put on a common scale (reference sd).
    """
    sd = ref.std(axis=0)
    z, zr = obs / sd, ref / sd
    order = np.argsort(z)  # most negative first
    adj = np.empty(len(z))
    running = 0.0
    for i, j in enumerate(order):
        rest = order[i:]
        pj = (zr[:, rest].min(axis=1) <= z[j] + 1e-12).mean()
        running = max(running, pj)
        adj[j] = running
    return adj


def holm(p: np.ndarray) -> np.ndarray:
    p = np.asarray(p, float)
    order = np.argsort(p)
    adj, running = np.empty(len(p)), 0.0
    for i, j in enumerate(order):
        running = max(running, min(1.0, (len(p) - i) * p[j]))
        adj[j] = running
    return adj


def sign_flip(by_year: np.ndarray) -> float:
    """Canay-Romano-Shaikh sign-change test on year-level estimates (one-sided, less)."""
    x = np.asarray(by_year, float).ravel()
    flips = np.array(list(itertools.product([1, -1], repeat=len(x))))
    return float(((flips * x).mean(axis=1) <= x.mean() + 1e-12).mean())


def interval(per_year, ev, level=0.90, t=None, detrend=0, grid=None, **kw) -> tuple:
    """Hodges-Lehmann estimate and two-sided interval by inverting the raw test under
    a constant additive effect tau on the event dates."""
    base = test(per_year, ev, t, detrend, **kw)
    est = float(base["est"][0])
    sd = float(base["ref"].std())
    grid = np.linspace(est - 6 * sd, est + 6 * sd, 241) if grid is None else grid
    a = (1 - level) / 2
    keep, pl = [], []
    for tau in grid:
        adj = []
        for i, M in enumerate(per_year):
            M = np.array(M, float).copy()
            M[ev[i]] -= tau
            adj.append(M)
        r = test(adj, ev, t, detrend, **kw)
        lo = float((r["ref"] <= r["est"] + 1e-12).mean())
        hi = float((r["ref"] >= r["est"] - 1e-12).mean())
        pl.append(lo - hi)
        if lo > a and hi > a:
            keep.append(tau)
    hl = float(grid[np.argmin(np.abs(np.array(pl)))])
    return hl, (min(keep), max(keep)) if keep else (np.nan, np.nan)


def power(per_year, ev, minutes, window=60.0, sims=2000, alpha=0.05, seed=0) -> float:
    """Share of simulated events detected at level alpha. Each simulation picks one
    placebo date per year (the true event date is removed), lowers its statistic by
    the log-speed effect of a full stop of `minutes`, and reruns the raw test."""
    rng = np.random.default_rng(seed)
    base = [np.delete(np.asarray(M, float), e) for M, e in zip(per_year, ev)]
    delta = np.log(1 - minutes / window)
    hits = 0
    for _ in range(sims):
        pick = [int(rng.integers(len(M))) for M in base]
        adj = [M.copy() for M in base]
        for M, i in zip(adj, pick):
            M[i] += delta
        hits += test(adj, pick)["p"][0] <= alpha
    return hits / sims


def sensitivity(per_year, ev, gammas=(1, 1.25, 1.5, 2, 3, 4, 6)) -> dict:
    """Rosenbaum-type bound: largest one-sided p-value when, within each year, the
    odds that a date is the event date may differ between dates by a factor of at
    most gamma. The worst case puts the high odds on each year's most negative
    dates; the cut-off in each year is found by coordinate ascent."""
    T = [loo_stat(M) for M in per_year]
    obs = float(np.mean([t[e] for t, e in zip(T, ev)]))

    def pmax(g, cuts):
        prob, tot = np.ones(1), np.zeros(1)
        for t, c in zip(T, cuts):
            w = np.where(t <= c, g, 1.0)
            w = w / w.sum()
            prob = (prob[:, None] * w[None, :]).ravel()
            tot = (tot[:, None] + t[None, :]).ravel()
        return float(prob[tot / len(T) <= obs + 1e-12].sum())

    out = {}
    for g in gammas:
        cuts = [t[e] for t, e in zip(T, ev)]
        best = pmax(g, cuts)
        for _ in range(3):
            for i, t in enumerate(T):
                for c in np.sort(t):
                    trial = cuts.copy()
                    trial[i] = c
                    v = pmax(g, trial)
                    if v > best:
                        best, cuts = v, trial
        out[g] = best
    return out
