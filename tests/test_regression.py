"""Ported code must reproduce the pilot's published numbers exactly."""

from pathlib import Path

import pandas as pd
import pytest

from saygi import did, ibb
from saygi.inference import summarize

FIX = Path(__file__).parent / "fixtures"


def test_summary_matches_pilot():
    out = summarize(pd.read_csv(FIX / "did_by_class.csv"))
    ref = pd.read_csv(FIX / "results_summary.csv")
    pd.testing.assert_frame_equal(out, ref, check_dtype=False, rtol=1e-9)


def test_headline_numbers():
    ref = pd.read_csv(FIX / "results_summary.csv").set_index("cls")
    assert round(ref.loc["50-70", "dk"], 2) == 0.73
    assert round(ref.loc["30-50", "dk"], 2) == 0.45
    assert ref.loc["50-70", "p_RI"] == 8 / 1024


@pytest.mark.skipif(not ibb.DEFAULT_RAW.exists(), reason="raw İBB data not downloaded")
def test_raw_reproduces_did_by_class():
    out = did.did_by_class(ibb.load()).round(5)
    ref = pd.read_csv(FIX / "did_by_class.csv")
    pd.testing.assert_frame_equal(out, ref, check_dtype=False, atol=1.5e-5)
