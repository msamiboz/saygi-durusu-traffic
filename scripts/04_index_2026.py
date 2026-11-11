"""City-wide traffic index at 5-minute resolution around 09:05 on 10 Nov 2026.

Source: İBB traffic index web service (TrafficIndexHistory/{days}/5M), which
serves only the latest 60 days. The response saved on the evening of
10 Nov 2026 is kept in data/raw/index/ and the tidy version in data/derived/.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

RAW = Path("data/raw/index/idx_60_5M.json")
OUT = Path("data/derived")
EVENT = pd.Timestamp("2026-11-10")
HOLIDAYS = [pd.Timestamp("2026-10-28"), pd.Timestamp("2026-10-29")]


def tidy() -> pd.DataFrame:
    f = OUT / "traffic_index_5min_2026.csv"
    if RAW.exists():
        d = pd.DataFrame(json.load(open(RAW)))
        d["ts"] = pd.to_datetime(d.TrafficIndexDate)
        d = d.sort_values("ts").drop_duplicates("ts")[["ts", "TrafficIndex"]]
        d.columns = ["timestamp", "traffic_index"]
        d.to_csv(f, index=False)
    return pd.read_csv(f, parse_dates=["timestamp"])


def stat(w: pd.DataFrame, centre=(540, 545), gap=20) -> pd.Series:
    """Index in the two 5-minute bins around 09:05 minus the mean of the bins
    `gap` minutes earlier and later."""
    c = w[list(centre)].mean(axis=1)
    pre = w[[b - gap for b in centre]].mean(axis=1)
    post = w[[b + gap for b in centre]].mean(axis=1)
    return c - (pre + post) / 2


def main() -> None:
    d = tidy()
    d["date"] = d.timestamp.dt.normalize()
    d["bin"] = (d.timestamp.dt.hour * 60 + d.timestamp.dt.minute) // 5 * 5
    w = d.pivot_table(index="date", columns="bin", values="traffic_index")
    days = [x for x in w.index if x.dayofweek < 5 and x not in HOLIDAYS]
    w = w.loc[days, [b for b in w.columns if 7 * 60 <= b <= 11 * 60]].dropna()
    rows = []
    for gap in (15, 20, 30):
        s = stat(w, gap=gap)
        ctrl = s.drop(EVENT)
        tue = ctrl[[x for x in ctrl.index if x.dayofweek == EVENT.dayofweek]]
        rows.append(dict(gap=gap, event=s[EVENT], control_mean=ctrl.mean(), control_sd=ctrl.std(),
                         n_control=len(ctrl), rank_high=int((ctrl >= s[EVENT]).sum()) + 1,
                         p_high=(int((ctrl >= s[EVENT]).sum()) + 1) / (len(ctrl) + 1),
                         tuesday_mean=tue.mean(), n_tuesday=len(tue),
                         tuesday_rank_high=int((tue >= s[EVENT]).sum()) + 1))  # fmt: skip
    res = pd.DataFrame(rows)
    res.to_csv(OUT / "index_2026_test.csv", index=False)
    # profile for the figure: each day relative to its own 08:00-10:30 mean
    win = [b for b in w.columns if 8 * 60 <= b <= 10 * 60 + 30]
    rel = w[win].sub(w[win].mean(axis=1), axis=0)
    ctrl = rel.drop(EVENT)
    prof = pd.DataFrame({
        "bin": win, "event": rel.loc[EVENT].to_numpy(), "event_raw": w.loc[EVENT, win].to_numpy(),
        "control_median": ctrl.median().to_numpy(), "control_q10": ctrl.quantile(0.1).to_numpy(),
        "control_q90": ctrl.quantile(0.9).to_numpy(),
        "control_raw_median": w.drop(EVENT)[win].median().to_numpy(),
    })  # fmt: skip
    # first difference (change over 5 minutes) at each bin, event vs controls
    dif = w[win].diff(axis=1)
    prof["event_change"] = dif.loc[EVENT].to_numpy()
    prof["control_change_q05"] = dif.drop(EVENT).quantile(0.05).to_numpy()
    prof["control_change_q95"] = dif.drop(EVENT).quantile(0.95).to_numpy()
    prof["control_change_min"] = dif.drop(EVENT).min().to_numpy()
    prof.to_csv(OUT / "index_2026_profile.csv", index=False)
    print(res.round(3).to_string(index=False))
    print(prof[(prof.bin >= 520) & (prof.bin <= 580)].round(2).to_string(index=False))
    # largest 10-minute falls among all control days and bins in the window
    fall = w[win].shift(-2, axis=1) - w[win]
    print(
        "event 09:00->09:10 change:",
        fall.loc[EVENT, 540],
        " control distribution at that bin: min",
        fall.drop(EVENT)[540].min(),
        "q05",
        fall.drop(EVENT)[540].quantile(0.05),
    )
    print(
        "share of all control day-bins with a 10-min fall <= event's:",
        round(
            float(
                (fall.drop(EVENT)[[b for b in win if b <= 600]] <= fall.loc[EVENT, 540])
                .to_numpy()
                .mean()
            ),
            4,
        ),
    )


if __name__ == "__main__":
    main()
