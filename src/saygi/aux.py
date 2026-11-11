"""Download the auxiliary inputs: weather, district boundaries, election results
and the five-minute traffic index. Everything goes to data/raw/ (not committed)."""

from __future__ import annotations

import json
from pathlib import Path

AUX = Path("data/raw/aux")
INDEX = Path("data/raw/index")
UA = {"User-Agent": "saygi-durusu-traffic/0.2 (research)"}


def weather() -> None:
    """Hourly weather for central Istanbul, Open-Meteo archive (CC BY 4.0)."""
    import requests

    url = ("https://archive-api.open-meteo.com/v1/archive?latitude=41.015&longitude=28.979"
           "&start_date=2020-01-01&end_date=2025-01-31"
           "&hourly=temperature_2m,precipitation,rain,snowfall,wind_speed_10m,cloud_cover"
           "&timezone=Europe%2FIstanbul")  # fmt: skip
    (AUX / "weather_istanbul_hourly.json").write_text(requests.get(url, timeout=120).text)


def districts() -> None:
    """Istanbul district boundaries from OpenStreetMap (ODbL), via an Overpass mirror."""
    import requests

    q = ('[out:json][timeout:120];area["name"="İstanbul"]["admin_level"="4"]->.a;'
         'relation(area.a)["admin_level"="6"]["boundary"="administrative"];out geom;')  # fmt: skip
    for host in ("https://maps.mail.ru/osm/tools/overpass", "https://overpass-api.de"):
        try:
            r = requests.post(f"{host}/api/interpreter", data={"data": q}, headers=UA, timeout=200)
            if r.ok and len(r.json()["elements"]) >= 39:
                (AUX / "istanbul_districts_osm.json").write_text(r.text)
                return
        except Exception:  # noqa: BLE001
            continue
    raise RuntimeError("no Overpass mirror returned the district boundaries")


def election() -> None:
    """2024 Istanbul mayoral election by district, from English Wikipedia (CC BY-SA)."""
    import requests

    p = dict(action="parse", page="2024 Istanbul mayoral election", prop="wikitext",
             format="json", redirects=1)  # fmt: skip
    r = requests.get("https://en.wikipedia.org/w/api.php", params=p, headers=UA, timeout=60)
    (AUX / "wiki_en_election.txt").write_text(r.json()["parse"]["wikitext"]["*"])


def index(days: int = 60) -> None:
    """Latest `days` days of the İBB traffic index at 5-minute resolution. The service
    keeps only about 60 days, so the 2026 file used in the paper cannot be re-downloaded
    later; its tidy copy is committed in data/derived/traffic_index_5min_2026.csv."""
    import requests

    url = f"https://api.ibb.gov.tr/tkmservices/api/TrafficData/v1/TrafficIndexHistory/{days}/5M"
    data = requests.get(url, timeout=300).json()
    INDEX.mkdir(parents=True, exist_ok=True)
    last = max(x["TrafficIndexDate"] for x in data)[:10]
    json.dump(data, open(INDEX / f"idx_{days}_5M_{last}.json", "w"))


def all_() -> None:
    AUX.mkdir(parents=True, exist_ok=True)
    for fn in (weather, districts, election):
        fn()
