"""Draw every figure of the paper from data/derived/ into figures/."""

from pathlib import Path

import pandas as pd

from saygi import plots

D, F = Path("data/derived"), Path("figures")

if __name__ == "__main__":
    F.mkdir(exist_ok=True)
    plots.placebo_dates(
        pd.read_csv(D / "date_stats_main.csv", parse_dates=["date"]), F / "fig_placebo_dates"
    )
    plots.speed_profile(pd.read_csv(D / "speed_profile.csv"), F / "fig_speed_profile")
    plots.hour_curvature(pd.read_csv(D / "hour_curvature.csv"), F / "fig_hour_curvature")
    plots.index_2026(pd.read_csv(D / "index_2026_profile.csv"), F / "fig_index_2026")
    plots.floor(pd.read_csv(D / "floor_by_month.csv"), F / "fig_speed_floor")
    plots.districts(pd.read_csv(D / "table_districts.csv"), F / "fig_districts")
    print("figures written to", F)
