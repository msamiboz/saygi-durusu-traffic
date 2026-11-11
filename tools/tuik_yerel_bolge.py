# Adapted from the author's tuik_scraper_yerel.py: one election type, result type, year and province.
"""
TUIK - Mahalli idareler secimi Excel scraper
============================================

Downloads TUIK's own Excel output for each municipal election result. The
workbook is saved as-is; only the destination filename is controlled here.
"""

import asyncio
import hashlib
import html
import json
import os
import re
import time
from datetime import datetime
from pathlib import Path

from playwright.async_api import TimeoutError as PWTimeout
from playwright.async_api import async_playwright

# -- Config -------------------------------------------------------------------
BASE_URL = "https://biruni.tuik.gov.tr/secimdagitimapp/yerel.zul"
OUTPUT_DIR = Path(os.environ.get("TUIK_OUT", "data/raw/elections/yerel"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
PROGRESS_FILE = OUTPUT_DIR / "progress_downloads.json"
AUDIT_LOG = OUTPUT_DIR / "download_audit.jsonl"

SCRAPE_PLAN = [
    {
        "election_type": os.environ.get("TUIK_ELECTION", "Büyükşehir belediye başkanlığı"),
        "result_type": os.environ.get("TUIK_RESULT", "Bölge sonucu"),
    },
]
YEAR_FILTER = os.environ.get("TUIK_YEAR", "2024")
LOC_FILTER = os.environ.get("TUIK_PROV", "istanbul")

PROBE_ONLY = False
WAIT_ZK = 1000
WAIT_REPORT = int(os.environ.get("TUIK_WAIT_REPORT_MS", "90000"))
RETRY_MAX = 3
RECOVERY_WAIT = 5000
MAX_DOWNLOADS = int(os.environ.get("TUIK_MAX_DOWNLOADS", "0") or "0")
DEBUG_MISSING_LABELS = True

ELECTION_LABELS = {item["election_type"] for item in SCRAPE_PLAN}
RESULT_LABELS = {
    "İl ve İlçe sonucu",
    "Belediye sonucu",
    "Bölge sonucu",
    "Sandık sonucu",
    "Kazanan adayların listesi",
}


def clean(text):
    return re.sub(r"\s+", " ", (text or "").strip())


def norm_text(text):
    s = clean(text).replace("İ", "i").lower().replace("\u0307", "")
    for a, b in [
        ("ş", "s"),
        ("ğ", "g"),
        ("ı", "i"),
        ("ö", "o"),
        ("ü", "u"),
        ("ç", "c"),
    ]:
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "", s)


async def zk(page, ms=WAIT_ZK):
    await page.wait_for_timeout(ms)


async def recover_page(page):
    try:
        await page.goto(BASE_URL, wait_until="networkidle", timeout=60_000)
    except PWTimeout:
        print("\n    reload timeout - continuing", end="  ", flush=True)
    await zk(page, RECOVERY_WAIT)


def slugify(text):
    s = clean(text).replace("İ", "i").lower().replace("\u0307", "")
    for a, b in [
        ("ş", "s"),
        ("ğ", "g"),
        ("ı", "i"),
        ("ö", "o"),
        ("ü", "u"),
        ("ç", "c"),
    ]:
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_") or "unknown"


def combo_key(election_type, result_type, year, location):
    return "|||".join([election_type, result_type, year, location])


def context_key(election_type, result_type, year):
    return "|||".join([election_type, result_type, year])


def add_unique(items, value):
    if value not in items:
        items.append(value)


def load_progress():
    if PROGRESS_FILE.exists():
        try:
            prog = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
            prog.setdefault("done", [])
            prog.setdefault("failed", [])
            prog.setdefault("locations", {})
            return prog
        except Exception:
            pass
    return {"done": [], "failed": [], "locations": {}}


def save_progress(prog):
    PROGRESS_FILE.write_text(json.dumps(prog, ensure_ascii=False, indent=2), encoding="utf-8")


def output_folder(election_type, result_type, year):
    folder = OUTPUT_DIR / slugify(election_type) / slugify(result_type) / slugify(year)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def output_path_from_download(folder, location, download):
    suffix = Path(download.suggested_filename or "").suffix or ".xls"
    return folder / f"{slugify(location)}{suffix.lower()}"


def find_existing_download(folder, location):
    stem = slugify(location)
    for suffix in (".xls", ".xlsx"):
        path = folder / f"{stem}{suffix}"
        if path.exists():
            return path
    return None


def normalized_words(text):
    s = html.unescape(clean(text)).replace("İ", "i").lower().replace("\u0307", "")
    for a, b in [
        ("ş", "s"),
        ("ğ", "g"),
        ("ı", "i"),
        ("ö", "o"),
        ("ü", "u"),
        ("ç", "c"),
    ]:
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def is_aggregate_location(location):
    return "tum" in normalized_words(location).split()


def location_aliases(location):
    aliases = {location}
    if location.startswith("K."):
        aliases.add(location.replace("K.", "Kahraman"))
        aliases.add(location.replace("K.", "Kahraman "))
    return [normalized_words(alias) for alias in aliases if normalized_words(alias)]


def location_in_text(location, text_words):
    if is_aggregate_location(location):
        return True
    for alias in location_aliases(location):
        pattern = r"(?<![a-z0-9])" + re.escape(alias).replace(r"\ ", r"\s+") + r"(?![a-z0-9])"
        if re.search(pattern, text_words):
            return True
    return False


def decode_download_text(path):
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "cp1254", "iso-8859-9", "latin-1"):
        try:
            text = data.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        text = data.decode("latin-1", errors="replace")
    text = re.sub(r"<[^>]+>", " ", html.unescape(text))
    return clean(text)


def append_audit(record):
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def validate_download(path, expected_location, known_locations=None):
    data = path.read_bytes()
    text = decode_download_text(path)
    text_words = normalized_words(text)
    matched_locations = []
    for location in known_locations or []:
        if is_aggregate_location(location):
            continue
        if location_in_text(location, text_words):
            add_unique(matched_locations, location)
    expected_found = location_in_text(expected_location, text_words)
    if expected_found and not is_aggregate_location(expected_location):
        add_unique(matched_locations, expected_location)
    return {
        "expected_location_found": expected_found,
        "matched_locations": matched_locations,
        "file_size": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "text_sample": text[:500],
    }


def mismatch_path_for(folder, expected_location, actual, suffix):
    mismatch_dir = folder / "_mismatched"
    mismatch_dir.mkdir(parents=True, exist_ok=True)
    return (
        mismatch_dir
        / f"{slugify(expected_location)}__actual_{slugify(actual)}__{int(time.time() * 1000)}{suffix}"
    )


def existing_download_is_valid(
    folder,
    election_type,
    result_type,
    year,
    location,
    known_locations,
):
    path = find_existing_download(folder, location)
    if not path:
        return False
    audit = validate_download(path, location, known_locations)
    if audit["expected_location_found"]:
        return True

    actual = audit["matched_locations"][0] if audit["matched_locations"] else "unknown"
    mismatch_path = mismatch_path_for(folder, location, actual, path.suffix or ".xls")
    path.replace(mismatch_path)
    append_audit(
        {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "scope": "municipal",
            "event": "existing_file_mismatch",
            "election_type": election_type,
            "result_type": result_type,
            "year": year,
            "expected_location": location,
            "final_path": str(path),
            "saved_path": str(mismatch_path),
            "ok": False,
            "error": "existing file did not validate for expected location",
            **audit,
        }
    )
    return False


async def click_row(page, label):
    target_norm = norm_text(label)
    rows = page.locator(
        ".listbox-btable tr, .listbox-body tr, .z-listbox-body tr, .z-listitem, [role='option']"
    )
    for i in range(await rows.count()):
        row = rows.nth(i)
        try:
            if not await row.is_visible():
                continue
            if norm_text(await row.inner_text()) != target_norm:
                continue
            await row.scroll_into_view_if_needed()
            div = row.locator("div").first
            if await div.count() > 0:
                try:
                    await div.click()
                except Exception:
                    await row.click()
            else:
                await row.click()
            return True
        except Exception:
            continue

    clicked = await page.evaluate(
        """
        (targetNorm) => {
            const norm = (value) => {
                return (value || "")
                    .replace(/İ/g, "i")
                    .toLowerCase()
                    .normalize("NFD")
                    .replace(/[\\u0300-\\u036f]/g, "")
                    .replace(/ı/g, "i")
                    .replace(/ş/g, "s")
                    .replace(/ğ/g, "g")
                    .replace(/ö/g, "o")
                    .replace(/ü/g, "u")
                    .replace(/ç/g, "c")
                    .replace(/[^a-z0-9]+/g, "");
            };
            const visible = (el) => {
                const style = window.getComputedStyle(el);
                if (style.display === "none" || style.visibility === "hidden") {
                    return false;
                }
                const rect = el.getBoundingClientRect();
                return rect.width > 0 && rect.height > 0;
            };
            const selectors = [
                ".listbox-btable tr",
                ".listbox-body tr",
                ".z-listbox-body tr",
                ".z-listitem",
                "[role='option']",
                "tr",
                "td",
                "div",
                "span"
            ].join(",");
            const candidates = Array.from(document.querySelectorAll(selectors))
                .filter(visible)
                .filter((el) => norm(el.innerText || el.textContent) === targetNorm);
            for (const el of candidates) {
                const clickable = el.closest(".z-listitem, tr, [role='option']") || el;
                clickable.scrollIntoView({block: "center"});
                clickable.click();
                return true;
            }
            return false;
        }
        """,
        target_norm,
    )
    if clicked:
        await zk(page, 700)
        return True
    if DEBUG_MISSING_LABELS:
        await dump_click_candidates(page, label)
    return False


async def dump_click_candidates(page, missing_label):
    try:
        values = await page.evaluate(
            """
            () => {
                const clean = (value) => (value || "").replace(/\\s+/g, " ").trim();
                const visible = (el) => {
                    const style = window.getComputedStyle(el);
                    if (style.display === "none" || style.visibility === "hidden") {
                        return false;
                    }
                    const rect = el.getBoundingClientRect();
                    return rect.width > 0 && rect.height > 0;
                };
                const selectors = [
                    ".listbox-btable tr",
                    ".listbox-body tr",
                    ".z-listbox-body tr",
                    ".z-listitem",
                    "[role='option']",
                    "label"
                ].join(",");
                const seen = new Set();
                const out = [];
                for (const el of document.querySelectorAll(selectors)) {
                    if (!visible(el)) continue;
                    const text = clean(el.innerText || el.textContent);
                    if (!text || seen.has(text)) continue;
                    seen.add(text);
                    out.push(text);
                    if (out.length >= 40) break;
                }
                return out;
            }
            """
        )
        print(f"\n    Could not find visible row {missing_label!r}.")
        print("    Visible row/label candidates:")
        for value in values:
            print(f"      - {value}")
    except Exception:
        pass


async def click_radio_label(page, label):
    target_norm = norm_text(label)
    clicked = await page.evaluate(
        """
        (targetNorm) => {
            const clean = (s) => (s || "").replace(/\\s+/g, " ").trim();
            const visible = (el) => {
                const style = window.getComputedStyle(el);
                if (style.display === "none" || style.visibility === "hidden") {
                    return false;
                }
                const rect = el.getBoundingClientRect();
                return rect.width > 0 && rect.height > 0;
            };
            const norm = (value) => {
                return clean(value)
                    .replace(/İ/g, "i")
                    .toLowerCase()
                    .normalize("NFD")
                    .replace(/[\\u0300-\\u036f]/g, "")
                    .replace(/ı/g, "i")
                    .replace(/ş/g, "s")
                    .replace(/ğ/g, "g")
                    .replace(/ö/g, "o")
                    .replace(/ü/g, "u")
                    .replace(/ç/g, "c")
                    .replace(/[^a-z0-9]+/g, "");
            };
            for (const el of document.querySelectorAll("label, span, td, div")) {
                if (!visible(el)) continue;
                if (norm(el.innerText || el.textContent) !== targetNorm) continue;
                const ownRadio = el.matches("input[type='radio']")
                    ? el
                    : el.querySelector("input[type='radio']");
                if (ownRadio) {
                    ownRadio.click();
                    return true;
                }
                let prev = el.previousElementSibling;
                while (prev) {
                    if (prev.matches && prev.matches("input[type='radio']")) {
                        prev.click();
                        return true;
                    }
                    prev = prev.previousElementSibling;
                }
                if (el.tagName.toLowerCase() === "label") {
                    el.click();
                    return true;
                }
                el.click();
                return true;
            }
            return false;
        }
        """,
        target_norm,
    )
    if clicked:
        await zk(page, 700)
    return clicked


async def reset(page):
    try:
        btn = page.locator("input[value='Ekran Temizle']")
        if await btn.count() > 0:
            await btn.first.click(timeout=2000)
            await zk(page, 1200)
    except Exception:
        pass


async def prepare_selection(page, election_type, result_type, year=None):
    await reset(page)
    if not await click_row(page, election_type):
        raise RuntimeError(f"Could not select election type {election_type!r}")
    await zk(page, 1500)
    if result_type and not await click_radio_label(page, result_type):
        raise RuntimeError(f"Could not select result type {result_type!r}")
    if year:
        if not await click_radio_label(page, year) and not await click_row(page, year):
            raise RuntimeError(f"Could not select year {year!r}")
        await zk(page, 1500)


async def read_listbox_groups(page):
    groups = []
    boxes = page.locator(
        ".listbox-btable, .listbox-body, .z-listbox-body, .z-listbox, [class*='listbox']"
    )
    for bi in range(await boxes.count()):
        rows = boxes.nth(bi).locator("tr, .z-listitem, [role='option']")
        texts = []
        for ri in range(await rows.count()):
            row = rows.nth(ri)
            try:
                if await row.is_visible():
                    value = clean(await row.inner_text())
                    if value:
                        add_unique(texts, value)
            except Exception:
                continue
        if texts:
            groups.append(texts)
    return groups


async def read_years(page):
    years = []
    for group in await read_listbox_groups(page):
        for text in group:
            if re.fullmatch(r"(19|20)\d{2}", text):
                add_unique(years, text)
    radio_years = await page.evaluate(
        """
        () => {
            const clean = (value) => (value || "").replace(/\\s+/g, " ").trim();
            const visible = (el) => {
                const style = window.getComputedStyle(el);
                if (style.display === "none" || style.visibility === "hidden") {
                    return false;
                }
                const rect = el.getBoundingClientRect();
                return rect.width > 0 && rect.height > 0;
            };
            const out = [];
            const seen = new Set();
            for (const el of document.querySelectorAll("label, span, td, div")) {
                if (!visible(el)) continue;
                const text = clean(el.innerText || el.textContent);
                if (!/^(19|20)\\d{2}$/.test(text) || seen.has(text)) continue;
                seen.add(text);
                out.push(text);
            }
            return out;
        }
        """
    )
    for year in radio_years:
        add_unique(years, year)
    return years


def is_location_label(text):
    if not text:
        return False
    if text in ELECTION_LABELS or text in RESULT_LABELS:
        return False
    if re.fullmatch(r"(19|20)\d{2}", text):
        return False
    lowered = text.lower()
    blocked_parts = (
        "mahalli idareler seçimi",
        "sonucu",
        "sandık",
        "kazanan",
        "üyeliği",
        "başkanlığı",
        "seçimi",
    )
    return not any(part in lowered for part in blocked_parts)


async def read_locations(page):
    for _ in range(20):
        candidate_groups = []
        for group in await read_listbox_groups(page):
            locations = [text for text in group if is_location_label(text)]
            if locations:
                candidate_groups.append(locations)
        if candidate_groups:
            unique = []
            for location in max(candidate_groups, key=len):
                add_unique(unique, location)
            return unique
        await page.wait_for_timeout(500)
    return []


async def select_excel_format(page):
    clicked = await page.evaluate(
        """
        () => {
            const visible = (el) => {
                const style = window.getComputedStyle(el);
                if (style.display === "none" || style.visibility === "hidden") {
                    return false;
                }
                const rect = el.getBoundingClientRect();
                return rect.width > 0 && rect.height > 0;
            };
            const groups = new Map();
            for (const radio of Array.from(document.querySelectorAll("input[type='radio']")).filter(visible)) {
                const rect = radio.getBoundingClientRect();
                const key = radio.name || `__${Math.round(rect.y)}`;
                if (!groups.has(key)) groups.set(key, []);
                groups.get(key).push(radio);
            }
            const candidates = Array.from(groups.values())
                .map((items) => items.sort((a, b) => a.getBoundingClientRect().x - b.getBoundingClientRect().x))
                .filter((items) => items.length === 3)
                .sort((a, b) => b[0].getBoundingClientRect().y - a[0].getBoundingClientRect().y);
            if (!candidates.length) return false;
            candidates[0][1].click();
            return true;
        }
        """
    )
    if not clicked:
        raise RuntimeError("Could not select Excel table format")
    await zk(page, 1000)


async def download_excel_report(
    page,
    folder,
    election_type,
    result_type,
    year,
    location,
    known_locations=None,
):
    await select_excel_format(page)
    async with page.expect_download(timeout=WAIT_REPORT) as info:
        clicked = await page.evaluate(
            """
            () => {
                const button = Array.from(document.querySelectorAll("input"))
                    .find((el) => el.value === "Raporu Oluştur");
                if (!button) return false;
                button.click();
                return true;
            }
            """
        )
        if not clicked:
            await page.locator("input[value='Raporu Oluştur']").click()
    download = await info.value
    final_path = output_path_from_download(folder, location, download)
    suffix = final_path.suffix or ".xls"
    tmp_path = folder / f".{slugify(location)}.{int(time.time() * 1000)}.download{suffix}"
    await download.save_as(tmp_path)

    audit = validate_download(tmp_path, location, known_locations)
    record = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "scope": "municipal",
        "election_type": election_type,
        "result_type": result_type,
        "year": year,
        "expected_location": location,
        "suggested_filename": download.suggested_filename,
        "final_path": str(final_path),
        **audit,
    }

    if audit["expected_location_found"]:
        tmp_path.replace(final_path)
        record["saved_path"] = str(final_path)
        record["ok"] = True
        append_audit(record)
        return final_path

    actual = audit["matched_locations"][0] if audit["matched_locations"] else "unknown"
    mismatch_path = mismatch_path_for(folder, location, actual, suffix)
    tmp_path.replace(mismatch_path)
    record["saved_path"] = str(mismatch_path)
    record["ok"] = False
    record["error"] = "expected location was not found in downloaded workbook"
    append_audit(record)
    raise RuntimeError(
        f"Downloaded workbook did not validate for {location!r}; "
        f"matched locations: {audit['matched_locations'] or ['unknown']}"
    )


async def main():
    prog = load_progress()
    done_set = set(prog.get("done", []))

    print("=" * 72)
    print("  TUIK Mahalli Idareler - Direct Excel Downloader")
    print("=" * 72)
    if done_set:
        print(f"  Resuming - {len(done_set)} combinations already done")

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        ctx = await browser.new_context(
            viewport={"width": 1280, "height": 900},
            locale="tr-TR",
            accept_downloads=True,
        )
        page = await ctx.new_page()
        page.set_default_timeout(90_000)

        print("\n[1] Loading municipal election page...")
        try:
            await page.goto(BASE_URL, wait_until="networkidle", timeout=60_000)
        except PWTimeout:
            print("    timeout - continuing")
        await zk(page, RECOVERY_WAIT)

        if PROBE_ONLY:
            print("\nPROBE MODE - counting locations per election/result/year:\n")
            total = 0
            for item in SCRAPE_PLAN:
                await prepare_selection(page, item["election_type"], item["result_type"])
                years = await read_years(page)
                print(f"{item['election_type']} / {item['result_type']} -> {years}")
                for year in years:
                    await prepare_selection(page, item["election_type"], item["result_type"], year)
                    locations = await read_locations(page)
                    total += len(locations)
                    print(f"  {year:4s} -> {len(locations):3d} locations")
            print(f"\n  Total Excel downloads needed: {total}")
            await browser.close()
            return

        global_done = 0
        t_start = time.time()

        for ei, item in enumerate(SCRAPE_PLAN, 1):
            election_type = item["election_type"]
            result_type = item["result_type"]
            print(f"\n{'=' * 72}")
            print(f"  ELECTION [{ei}/{len(SCRAPE_PLAN)}]: {election_type}")
            print(f"  RESULT TYPE: {result_type}")
            print(f"{'=' * 72}")

            try:
                await prepare_selection(page, election_type, result_type)
                years = await read_years(page)
            except Exception as ex:
                print(f"  FAILED to initialize election: {ex}")
                continue

            print(f"  Years ({len(years)}): {years}")

            years = [y for y in years if YEAR_FILTER in y]
            print(f"  filtered years: {years}")
            for yi, year in enumerate(years, 1):
                print(f"\n{'-' * 72}")
                print(f"  YEAR [{yi}/{len(years)}]: {year}")
                print(f"{'-' * 72}")

                try:
                    await prepare_selection(page, election_type, result_type, year)
                    locations = await read_locations(page)
                except Exception as ex:
                    print(f"  FAILED to read locations: {ex}")
                    continue

                print(f"  locations offered ({len(locations)}): {locations[:60]}")
                locations = [x for x in locations if LOC_FILTER in norm_text(x)]
                print(f"  filtered locations: {locations}")
                loc_context = context_key(election_type, result_type, year)
                prog.setdefault("locations", {})[loc_context] = locations
                save_progress(prog)

                to_do = []
                year_folder = output_folder(election_type, result_type, year)
                for loc in locations:
                    key = combo_key(election_type, result_type, year, loc)
                    if key in done_set and existing_download_is_valid(
                        year_folder,
                        election_type,
                        result_type,
                        year,
                        loc,
                        locations,
                    ):
                        continue
                    done_set.discard(key)
                    to_do.append(loc)
                prog["done"] = sorted(done_set)
                save_progress(prog)
                print(
                    f"  Locations: {len(locations)} total | "
                    f"{len(locations) - len(to_do)} done | {len(to_do)} remaining"
                )
                if to_do:
                    await recover_page(page)

                for li, location in enumerate(to_do, 1):
                    elapsed = time.time() - t_start
                    eta = ""
                    if global_done:
                        secs_per = elapsed / global_done
                        eta = f"  ETA ~{max(0, (len(to_do) - li) * secs_per / 60):.0f}min"
                    print(f"  [{li}/{len(to_do)}] {location}{eta}", end="  ", flush=True)

                    key = combo_key(election_type, result_type, year, location)
                    path = None
                    for attempt in range(1, RETRY_MAX + 1):
                        try:
                            await prepare_selection(page, election_type, result_type, year)
                            if not await click_row(page, location):
                                raise RuntimeError(f"Could not select {location!r}")
                            await zk(page, 1500)
                            folder = output_folder(election_type, result_type, year)
                            path = await download_excel_report(
                                page,
                                folder,
                                election_type,
                                result_type,
                                year,
                                location,
                                locations,
                            )
                            break
                        except Exception as ex:
                            print(
                                f"\n    attempt {attempt}: {ex}",
                                end="  ",
                                flush=True,
                            )
                            if attempt < RETRY_MAX:
                                await recover_page(page)

                    if path:
                        done_set.add(key)
                        prog["done"] = sorted(done_set)
                        prog["failed"] = [
                            failed for failed in prog.get("failed", []) if failed != key
                        ]
                        save_progress(prog)
                        global_done += 1
                        print(f"Saved {path.relative_to(OUTPUT_DIR)}")
                        if MAX_DOWNLOADS and global_done >= MAX_DOWNLOADS:
                            print(f"\n  Reached TUIK_MAX_DOWNLOADS={MAX_DOWNLOADS}; stopping.")
                            await browser.close()
                            failed = prog.get("failed", [])
                            print("\n" + "=" * 72)
                            print(
                                f"  Done: {len(done_set)} Excel files saved | Failed: {len(failed)}"
                            )
                            print(f"  Output folder: {OUTPUT_DIR.resolve()}")
                            print("=" * 72)
                            return
                    else:
                        add_unique(prog.setdefault("failed", []), key)
                        save_progress(prog)
                        print("FAILED")

        await browser.close()

    failed = prog.get("failed", [])
    print("\n" + "=" * 72)
    print(f"  Done: {len(done_set)} Excel files saved | Failed: {len(failed)}")
    if failed:
        print("  Failed combinations are listed in progress_downloads.json")
    print(f"  Output folder: {OUTPUT_DIR.resolve()}")
    print("=" * 72)


if __name__ == "__main__":
    try:
        import nest_asyncio

        nest_asyncio.apply()
        asyncio.get_event_loop().run_until_complete(main())
    except ImportError:
        asyncio.run(main())
