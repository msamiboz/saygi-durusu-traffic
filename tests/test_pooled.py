"""Main design on synthetic data: a known injected stop must be recovered."""

import numpy as np
import pandas as pd
import pytest

from saygi import calendar as cal
from saygi import dateri, pooled


def make_cellday(effect_min=0.0, n_cells=150, years=(2021, 2022, 2023), seed=0, date_sd=0.004):
    rng = np.random.default_rng(seed)
    rows = []
    for y in years:
        base = rng.uniform(20, 95, n_cells)
        for d in cal.pool(y, 4):
            shock = rng.normal(0, date_sd)  # common to all cells on the date
            row = {"date": d, "GEOHASH": [f"g{i:03d}" for i in range(n_cells)]}
            day = rng.normal(0, 0.03, n_cells)
            for h in range(6, 13):
                lv = np.log(base) + day + rng.normal(0, 0.02, n_cells) + (shock if h == 9 else 0)
                if h == 9 and d == cal.event(y):
                    lv += np.log(1 - effect_min / 60)
                row[f"v{h}"] = np.exp(lv)
            for h in (8, 9, 10):
                row[f"mn{h}"] = np.maximum(1, row[f"v{h}"] / 4)
                row[f"mx{h}"] = row[f"v{h}"] * 1.8
                row[f"n{h}"] = rng.integers(5, 200, n_cells).astype(float)
            rows.append(pd.DataFrame(row))
    return pd.concat(rows, ignore_index=True)


def arrays(S, cls="all"):
    py, ev = [], []
    for _, g in S[S.cls == cls].groupby("year"):
        g = g.sort_values("date").reset_index(drop=True)
        py.append(g.M.to_numpy())
        ev.append(int(g.index[g.k == 0][0]))
    return py, ev


def test_pool_rules():
    for y in cal.YEARS:
        p = cal.pool(y)
        assert cal.event(y) in p
        assert all(d.dayofweek == cal.event(y).dayofweek for d in p)
        assert not any(cal.in_school_break(d) or cal.is_holiday(d) for d in p if d != cal.event(y))
    assert pd.Timestamp("2021-11-17") in cal.pool(2021, drop_break=False)


def test_recovers_injected_stop():
    S = pooled.all_years(make_cellday(1.5), weeks=4, years=(2021, 2022, 2023))
    py, ev = arrays(S)
    r = dateri.test(py, ev)
    assert abs(60 * (1 - np.exp(r["est"][0])) - 1.5) < 0.4
    assert r["exact"] and r["p"][0] <= 2 / r["n_assign"]
    assert (r["by_year"] < 0).all()


def test_null_p_values_are_roughly_uniform():
    ps = []
    for s in range(60):
        S = pooled.all_years(
            make_cellday(0.0, n_cells=40, seed=s), weeks=4, years=(2021, 2022, 2023)
        )
        ps.append(dateri.test(*arrays(S))["p"][0])
    assert 0.35 < np.mean(ps) < 0.65
    assert np.mean(np.array(ps) < 0.05) <= 0.15


def test_classification_does_not_depend_on_event_date():
    cd = make_cellday(3.0)
    d = cal.pool(2021, 4)
    a = pooled.baseline_speed(cd, d)
    b = pooled.baseline_speed(cd, list(reversed(d)))
    pd.testing.assert_series_equal(a, b)


def test_interval_and_sign_flip():
    S = pooled.all_years(make_cellday(1.5), weeks=4, years=(2021, 2022, 2023))
    py, ev = arrays(S)
    hl, (lo, hi) = dateri.interval(py, ev)
    true = np.log(1 - 1.5 / 60)
    assert lo < hl < hi < 0 and abs(hl - true) < 0.006
    assert dateri.sign_flip([-1.0, -2.0, -0.5, -1.5, -3.0]) == pytest.approx(1 / 32)
    assert dateri.sign_flip([1.0, -1.0, 1.0, -1.0]) > 0.3


def test_stepdown_and_holm():
    rng = np.random.default_rng(1)
    ref = rng.normal(0, 1, (20000, 4))
    obs = np.array([-3.5, -0.2, 0.3, -1.0])
    adj = dateri.stepdown(obs, ref)
    raw = (ref <= obs).mean(axis=0)
    assert (adj >= raw - 1e-12).all() and adj[0] < 0.01 and adj[2] > 0.5
    assert adj[0] <= 4 * raw[0] + 0.002
    h = dateri.holm(np.array([0.001, 0.04, 0.5, 0.03]))
    assert h[0] == pytest.approx(0.004) and (np.diff(np.sort(h)) >= 0).all()


def test_sensitivity_is_monotone_and_power_rises():
    S = pooled.all_years(make_cellday(1.0), weeks=4, years=(2021, 2022, 2023))
    py, ev = arrays(S)
    s = dateri.sensitivity(py, ev, gammas=(1, 2, 4))
    assert s[1] <= s[2] <= s[4]
    assert s[1] == pytest.approx(dateri.test(py, ev)["p"][0])
    assert dateri.power(py, ev, 2.0, sims=60) >= dateri.power(py, ev, 0.05, sims=60)
