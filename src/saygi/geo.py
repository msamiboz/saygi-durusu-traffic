"""Assign geohash cells to Istanbul districts, sides of the Bosphorus and 2024 vote shares."""

from __future__ import annotations

import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

AUX = Path("data/raw/aux")
ASIA = {"Adalar", "Ataşehir", "Beykoz", "Çekmeköy", "Kadıköy", "Kartal", "Maltepe", "Pendik",
        "Sancaktepe", "Sultanbeyli", "Şile", "Tuzla", "Ümraniye", "Üsküdar"}  # fmt: skip


def district_polygons() -> dict:
    """District name -> shapely geometry, from an OpenStreetMap Overpass export."""
    from shapely.geometry import LineString
    from shapely.ops import polygonize, unary_union

    els = json.load(open(AUX / "istanbul_districts_osm.json"))["elements"]
    out = {}
    for e in els:
        lines = [
            LineString([(p["lon"], p["lat"]) for p in m["geometry"]])
            for m in e["members"]
            if m["type"] == "way"
            and m.get("role") in ("outer", "")
            and len(m.get("geometry", [])) > 1
        ]
        polys = list(polygonize(unary_union(lines)))
        if polys:
            out[e["tags"]["name"]] = unary_union(polys)
    return out


def votes_2024() -> pd.DataFrame:
    """2024 metropolitan mayoral election by district (CHP and AK Party vote shares, %).
    Parsed from the English Wikipedia article "2024 Istanbul mayoral election"."""
    w = open(AUX / "wiki_en_election.txt").read()
    sec = w[w.index("==== Results by district ====") : w.index("=== District elections ===")]
    rows = []
    for block in sec.split("|-"):
        m = re.search(r"\[\[(?:[^\]|]*\|)?(?:\{\{white\|)?([^\]}|]+)", block)
        nums = re.findall(r"^\|\s*([\d,]+(?:\.\d+)?)\s*$", block, flags=re.M)
        if m and len(nums) >= 4:
            rows.append(dict(district=m.group(1).strip(), chp=float(nums[1]), akp=float(nums[3])))
    return pd.DataFrame(rows)


def cells() -> pd.DataFrame:
    """GEOHASH, lat, lon, district, side, chp, akp (cached in data/interim/cells.parquet)."""
    cache = Path("data/interim/cells.parquet")
    if cache.exists():
        return pd.read_parquet(cache)
    from shapely.geometry import Point
    from shapely.strtree import STRtree

    co = pd.read_parquet("data/raw/geohash_coords.parquet").dropna()
    polys = district_polygons()
    names = list(polys)
    tree = STRtree([polys[n] for n in names])
    pts = [Point(xy) for xy in zip(co.LONGITUDE, co.LATITUDE)]
    idx = tree.nearest(pts)
    co["district"] = [names[i] for i in idx]
    inside = [polys[n].contains(p) for n, p in zip(co.district, pts)]
    co["inside"] = inside
    co["side"] = ["Asia" if d in ASIA else "Europe" for d in co.district]
    v = votes_2024()
    fix = {"Eyüp": "Eyüpsultan", "Kağıthane": "Kâğıthane"}
    v["district"] = v.district.replace(fix)
    co = co.merge(v, on="district", how="left")
    co.to_parquet(cache)
    return co


_B32 = "0123456789bcdefghjkmnpqrstuvwxyz"


def geohash_bbox(gh: str) -> tuple[float, float, float, float]:
    """(lon_min, lat_min, lon_max, lat_max) of a geohash cell."""
    lat, lon, even = [-90.0, 90.0], [-180.0, 180.0], True
    for ch in gh:
        bits = _B32.index(ch)
        for k in range(4, -1, -1):
            rng = lon if even else lat
            mid = (rng[0] + rng[1]) / 2
            if bits >> k & 1:
                rng[0] = mid
            else:
                rng[1] = mid
            even = not even
    return lon[0], lat[0], lon[1], lat[1]


def mahalle_weights(path=AUX / "istanbul_mahalle.geojson") -> pd.DataFrame:
    """Area share of each neighbourhood (mahalle) in each geohash cell.

    Neighbourhood polygons come from the land registry (tapu kadastro) and were
    prepared for another project; they are close to, not identical with, the
    current administrative neighbourhoods. Areas use a local equirectangular
    scaling (cos 41 degrees), which is accurate enough for shares within a cell.
    """
    from shapely.geometry import box, shape
    from shapely.strtree import STRtree

    gj = json.load(open(path))
    feats = [(f["properties"], shape(f["geometry"])) for f in gj["features"]]
    geoms = [g.buffer(0) for _, g in feats]
    tree = STRtree(geoms)
    co = pd.read_parquet("data/raw/geohash_coords.parquet").dropna()
    rows = []
    for gh in co.GEOHASH.unique():
        b = box(*geohash_bbox(gh))
        for i in tree.query(b):
            a = geoms[i].intersection(b).area
            if a > 0:
                p = feats[i][0]
                rows.append(dict(GEOHASH=gh, ilce=p["ilce_adi"], mahalle=p["mahalle_adi"],
                                 mahalle_id=p["mahalle_id"], share=a / b.area))  # fmt: skip
    return pd.DataFrame(rows)


def _norm_name(s: str) -> str:
    s = str(s).replace("İ", "i").replace("I", "ı").lower()
    for a, b in (
        ("ş", "s"),
        ("ğ", "g"),
        ("ı", "i"),
        ("ö", "o"),
        ("ü", "u"),
        ("ç", "c"),
        ("â", "a"),
        ("î", "i"),
    ):
        s = s.replace(a, b)
    for suf in (" mahallesi", " mah.", " mh.", " mah"):
        s = s.replace(suf, "")
    return "".join(ch for ch in s if ch.isalnum())


def tuik_neighbourhood_votes(path, election: str) -> pd.DataFrame:
    """Parse a TÜİK 'bölge sonucu' report (HTML saved as .xls) into one row per
    neighbourhood: ilce, mahalle, valid votes and CHP / AK PARTİ shares (%)."""
    t = pd.read_html(path, encoding="windows-1254")
    t = max(t, key=len)
    head = t.iloc[0].tolist()
    t = t.iloc[1:].copy()
    t.columns = [str(h) for h in head]
    ilce_col, mah_col = head[1], head[2]
    valid = [h for h in head if str(h).startswith("Geçerli oy")][0]
    t[ilce_col] = t[ilce_col].ffill()
    m = t[t[mah_col].notna()].copy()
    for c in (valid, "CHP", "AK PARTİ"):
        m[c] = pd.to_numeric(m[c], errors="coerce")
    m = m[m[valid] > 0]
    out = pd.DataFrame({"ilce": m[ilce_col].astype(str).str.strip(), "mahalle": m[mah_col].astype(str).str.strip(),
                        "valid": m[valid], "chp": 100 * m["CHP"] / m[valid], "akp": 100 * m["AK PARTİ"] / m[valid]})  # fmt: skip
    out["election"] = election
    out["key"] = out.ilce.map(_norm_name) + "|" + out.mahalle.map(_norm_name)
    return out.reset_index(drop=True)


def cell_votes(weights: pd.DataFrame, votes: pd.DataFrame) -> pd.DataFrame:
    """Area-weighted neighbourhood vote shares for each geohash cell. Neighbourhoods
    without a matching vote record are dropped and the weights renormalized."""
    w = weights.copy()
    w["key"] = w.ilce.map(_norm_name) + "|" + w.mahalle.map(_norm_name)
    w = w.merge(votes[["key", "chp", "akp"]], on="key", how="left")
    matched = w.groupby("GEOHASH").apply(lambda g: g.loc[g.chp.notna(), "share"].sum() / g.share.sum(),
                                         include_groups=False).rename("matched_share")  # fmt: skip
    w = w[w.chp.notna()]
    agg = w.groupby("GEOHASH").apply(
        lambda g: pd.Series({"chp": np.average(g.chp, weights=g.share), "akp": np.average(g.akp, weights=g.share),
                             "n_mahalle": len(g)}),
        include_groups=False,
    )  # fmt: skip
    return agg.join(matched)


def tuik_general_neighbourhood_votes(paths, election: str = "general2023") -> pd.DataFrame:
    """Parse TÜİK 'Seçim çevresi ve bölgelerine göre milletvekili genel seçimi sonuçları'
    reports (one HTML-as-.xls file per district) into one row per neighbourhood or village."""
    rows = []
    for path in paths:
        t = max(pd.read_html(path, encoding="windows-1254"), key=len)
        head = [str(h) for h in t.iloc[0].tolist()]
        valid = head.index("Geçerli oy sayısı")
        chp, akp = head.index("CHP"), head.index("AK PARTİ")
        ilce = None
        for _, r in t.iloc[1:].iterrows():
            if isinstance(r.iloc[2], str) and not r.iloc[2].startswith("Seçim çevresi"):
                ilce = r.iloc[2].strip()
            kind = r.iloc[5]
            if ilce and isinstance(kind, str) and kind.strip() in ("Mah.", "Köyü", "Köy", "Bld."):
                v = pd.to_numeric(r.iloc[valid], errors="coerce")
                if v and v > 0:
                    rows.append(dict(ilce=ilce, mahalle=str(r.iloc[3]).strip(), kind=kind.strip(), valid=v,
                                     chp=100 * float(r.iloc[chp]) / v, akp=100 * float(r.iloc[akp]) / v))  # fmt: skip
    out = pd.DataFrame(rows)
    out["election"] = election
    out["key"] = out.ilce.map(_norm_name) + "|" + out.mahalle.map(_norm_name)
    return out
