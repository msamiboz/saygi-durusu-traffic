import numpy as np
import pandas as pd
import pytest


def make_ibb(effect_min: float = 0.0, n_geo: int = 200, years=range(2020, 2025), seed: int = 0):
    """Synthetic İBB panel; on Nov 10 at 09h speeds drop as if every vehicle
    stood still for `effect_min` of the 60 minutes."""
    rng = np.random.default_rng(seed)
    rows = []
    for y in years:
        base = rng.uniform(20, 90, n_geo)
        for d in (3, 10, 17, 24):
            day_fx = rng.normal(0, 0.02, n_geo)
            for h in range(6, 13):
                lv = np.log(base) + day_fx - 0.05 * (h == 8) + rng.normal(0, 0.03, n_geo)
                if d == 10 and h == 9:
                    lv += np.log(1 - effect_min / 60)
                v = np.exp(lv)
                rows.append(
                    pd.DataFrame(
                        {
                            "GEOHASH": [f"g{i:04d}" for i in range(n_geo)],
                            "AVERAGE_SPEED": v,
                            "MINIMUM_SPEED": np.maximum(1, v / 3),
                            "MAXIMUM_SPEED": v * 2,
                            "NUMBER_OF_VEHICLES": rng.integers(10, 300, n_geo),
                            "year": y,
                            "day": d,
                            "hour": h,
                        }
                    )
                )
    return pd.concat(rows, ignore_index=True)


@pytest.fixture
def ibb_null():
    return make_ibb(0.0)


@pytest.fixture
def ibb_effect():
    return make_ibb(1.0)
