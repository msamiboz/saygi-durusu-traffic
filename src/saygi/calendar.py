"""Event dates, public holidays, school breaks and placebo-date pools."""

from __future__ import annotations

import pandas as pd

YEARS = (2020, 2021, 2022, 2023, 2024)


def event(year: int) -> pd.Timestamp:
    return pd.Timestamp(year, 11, 10)


# National public holidays with fixed dates (month, day). 28 Oct is a half day.
FIXED = [(1, 1), (4, 23), (5, 1), (5, 19), (7, 15), (8, 30), (10, 28), (10, 29), (12, 31)]

# Religious holidays incl. the eve (arife): Ramazan Bayramı and Kurban Bayramı.
RELIGIOUS = [
    ("2020-05-23", "2020-05-26"), ("2020-07-30", "2020-08-03"),
    ("2021-05-12", "2021-05-15"), ("2021-07-19", "2021-07-23"),
    ("2022-05-01", "2022-05-04"), ("2022-07-08", "2022-07-12"),
    ("2023-04-20", "2023-04-23"), ("2023-06-27", "2023-07-01"),
    ("2024-04-09", "2024-04-12"), ("2024-06-15", "2024-06-19"),
]  # fmt: skip

# First-term school break (ara tatil), Ministry of National Education calendars.
SCHOOL_BREAK = {
    2020: ("2020-11-16", "2020-11-20"),
    2021: ("2021-11-15", "2021-11-19"),
    2022: ("2022-11-14", "2022-11-18"),
    2023: ("2023-11-13", "2023-11-17"),
    2024: ("2024-11-11", "2024-11-15"),
}

# COVID-19: full lockdowns and the first closure period (not comparable days).
COVID = [("2020-03-16", "2020-05-31"), ("2021-04-29", "2021-05-17")]


def _in(d: pd.Timestamp, spans) -> bool:
    return any(pd.Timestamp(a) <= d <= pd.Timestamp(b) for a, b in spans)


def is_holiday(d: pd.Timestamp) -> bool:
    return (d.month, d.day) in FIXED or _in(d, RELIGIOUS)


def in_school_break(d: pd.Timestamp) -> bool:
    return _in(d, SCHOOL_BREAK.values())


def flags(d: pd.Timestamp) -> dict:
    return dict(holiday=is_holiday(d), school_break=in_school_break(d), covid=_in(d, COVID))


def pool(
    year: int, weeks: int | None = 8, drop_break: bool = True, shift: int = 0
) -> list[pd.Timestamp]:
    """Candidate dates for year: same weekday as 10 Nov, within +-weeks weeks.

    weeks=None gives every same-weekday date of the calendar year. Public
    holidays and lockdown days are always dropped; school-break dates are
    dropped unless drop_break is False. The event date is always included.
    """
    ev = event(year) + pd.Timedelta(days=shift)  # shift != 0: placebo "event" on another day
    if weeks is None:
        ks = range(-60, 61)
    else:
        ks = range(-weeks, weeks + 1)
    out = []
    for k in ks:
        d = ev + pd.Timedelta(weeks=k)
        if weeks is None and d.year != year:
            continue
        f = flags(d)
        if k != 0 and (f["holiday"] or f["covid"] or (drop_break and f["school_break"])):
            continue
        out.append(d)
    return out
