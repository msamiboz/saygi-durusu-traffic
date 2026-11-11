import numpy as np
import pandas as pd
from conftest import make_ibb

from saygi import did
from saygi.inference import ri


def test_recovers_injected_minutes(ibb_effect):
    est = did.pooled(did.did_table(ibb_effect))
    m = did.minutes(est[did.TREAT].mean())
    assert abs(m - 1.0) < 0.1


def test_null_has_no_effect(ibb_null):
    est = did.pooled(did.did_table(ibb_null))
    assert abs(did.minutes(est[did.TREAT].mean())) < 0.2


def test_ri_detects_effect(ibb_effect):
    real, p, n = ri(did.pooled(did.did_table(ibb_effect)))
    assert n == 4**5
    assert real < 0 and p == 1 / 1024


def test_ri_null_is_calibrated():
    """Under the null, p < 0.05 should happen in about 5% of seeds."""
    ps = [ri(did.pooled(did.did_table(make_ibb(0.0, n_geo=30, seed=s))))[1] for s in range(80)]
    assert 0.0 <= np.mean(np.array(ps) < 0.05) <= 0.15
    assert 0.35 < np.mean(ps) < 0.65


def test_zero_speeds_and_unbalanced_cells_dropped(ibb_null):
    df = ibb_null.copy()
    df.loc[(df.GEOHASH == "g0000") & (df.day == 3) & (df.hour == 9), "AVERAGE_SPEED"] = 0
    df = df[~((df.GEOHASH == "g0001") & (df.day == 17))]
    D = did.did_table(df)
    geos = D.index.get_level_values("GEOHASH")
    assert "g0000" not in geos and "g0001" not in geos


def test_did_by_class_shape(ibb_effect):
    t = did.did_by_class(ibb_effect)
    assert set(t.cls) <= set(did.CLASS_ORDER)
    assert list(t.columns) == ["cls", "year", "day", "did", "se", "n"]
    allrows = t[t.cls == "all"]
    assert len(allrows) == 5 * 4
    assert (t.groupby(["year", "day"]).n.sum() == 2 * allrows.set_index(["year", "day"]).n).all()
    assert isinstance(t, pd.DataFrame)
