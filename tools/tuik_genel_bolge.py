# Adapted from the author's tuik_scraper2.py: neighbourhood-level menu, one year, one province.
"""
TUIK - Milletvekili genel secimi Excel scraper
==============================================

Downloads TUIK's own Excel output for each year/province result. The workbook is
saved as-is; only the destination filename is controlled here.
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

BASE_URL = "https://biruni.tuik.gov.tr/secimdagitimapp/secim.zul"
OUTPUT_DIR = Path(os.environ.get("TUIK_OUT", "data/raw/elections/genel_bolge"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
PROGRESS_FILE = OUTPUT_DIR / "progress_downloads.json"
AUDIT_LOG = OUTPUT_DIR / "download_audit.jsonl"

PROBE_ONLY = False
WAIT_ZK = 1000
WAIT_REPORT = int(os.environ.get("TUIK_WAIT_REPORT_MS", "90000"))
WAIT_ROW = int(os.environ.get("TUIK_WAIT_ROW_MS", "12000"))
RETRY_MAX = 3
RECOVERY_WAIT = 5000
MAX_DOWNLOADS = int(os.environ.get("TUIK_MAX_DOWNLOADS", "0") or "0")

MENU_ITEM = os.environ.get(
    "TUIK_MENU", "Seçim çevresi ve bölgelerine göre milletvekili genel seçimi sonuçları"
)
YEAR_FILTER = os.environ.get("TUIK_YEAR", "2023")
PROV_FILTER = os.environ.get("TUIK_PROV", "istanbul")


class EmptyReportError(RuntimeError):
    """TUIK sometimes returns a header-only Oracle report before ZK state settles."""


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


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "_", normalized_words(text)).strip("_") or "unknown"


def combo_key(year, province):
    return f"{year}|||{province}"


def add_unique(items, value):
    if value not in items:
        items.append(value)


async def zk(page, ms=WAIT_ZK):
    await page.wait_for_timeout(ms)


async def recover_page(page):
    try:
        await page.goto(BASE_URL, wait_until="networkidle", timeout=60_000)
    except PWTimeout:
        print("\n    reload timeout - continuing", end="  ", flush=True)
    await zk(page, RECOVERY_WAIT)


def load_progress():
    if PROGRESS_FILE.exists():
        try:
            prog = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
            prog.setdefault("done", [])
            prog.setdefault("failed", [])
            prog.setdefault("year_provinces", {})
            return prog
        except Exception:
            pass
    return {"done": [], "failed": [], "year_provinces": {}}


def save_progress(prog):
    PROGRESS_FILE.write_text(json.dumps(prog, ensure_ascii=False, indent=2), encoding="utf-8")


def output_folder(year):
    folder = OUTPUT_DIR / slugify(year)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def output_path_from_download(folder, province, download):
    suffix = Path(download.suggested_filename or "").suffix or ".xls"
    return folder / f"{slugify(province)}{suffix.lower()}"


def find_existing_download(folder, province):
    stem = slugify(province)
    for suffix in (".xls", ".xlsx"):
        path = folder / f"{stem}{suffix}"
        if path.exists():
            return path
    return None


def split_region_location(location):
    match = re.match(r"^(.*?)\s*\((\d+)\s*\)$", clean(location))
    if not match:
        return clean(location), None
    return match.group(1).strip(), match.group(2)


def location_aliases(location):
    aliases = {location}
    if location.startswith("K."):
        aliases.add(location.replace("K.", "Kahraman"))
        aliases.add(location.replace("K.", "Kahraman "))
    return [normalized_words(alias) for alias in aliases if normalized_words(alias)]


REGION_LOCATION_ANCHORS = {
    ("ankara", "1"): ("Çankaya", "Etimesgut", "Gölbaşı"),
    ("ankara", "2"): ("Altındağ", "Keçiören", "Yenimahalle"),
    ("istanbul", "1"): ("Adalar", "Beykoz", "Kadıköy"),
    ("istanbul", "2"): ("Bayrampaşa", "Beşiktaş", "Beyoğlu"),
    ("istanbul", "3"): ("Avcılar", "Bağcılar", "Bahçelievler"),
    ("izmir", "1"): ("Balçova", "Buca", "Gaziemir"),
    ("izmir", "2"): ("Bornova", "Çiğli", "Karşıyaka"),
}


def phrase_in_words(phrase, text_words):
    phrase_words = normalized_words(phrase)
    if not phrase_words:
        return False
    pattern = r"(?<![a-z0-9])" + re.escape(phrase_words).replace(r"\ ", r"\s+") + r"(?![a-z0-9])"
    return bool(re.search(pattern, text_words))


def regional_location_in_text(location, text_words):
    base_location, region_no = split_region_location(location)
    if not region_no:
        return False
    for alias in location_aliases(base_location):
        base_pattern = re.escape(alias).replace(r"\ ", r"\s+")
        # Newer-year format: "Adana 1 nolu" (space-separated with "nolu" keyword)
        pattern = (
            r"(?<![a-z0-9])"
            + base_pattern
            + rf"(?:\s+[a-z0-9]+){{0,12}}\s+{region_no}\s+nolu(?![a-z0-9])"
        )
        if re.search(pattern, text_words):
            return True
        # 1991 compact format: "Adana(1)" → normalized to "adana 1" directly before
        # a non-alphanumeric boundary (no "nolu" keyword used in older reports)
        compact_pattern = (
            r"(?<![a-z0-9])" + base_pattern + r"\s+" + re.escape(region_no) + r"(?![a-z0-9])"
        )
        if re.search(compact_pattern, text_words):
            return True
    anchor_key = (norm_text(base_location), region_no)
    anchors = REGION_LOCATION_ANCHORS.get(anchor_key)
    if anchors and any(
        phrase_in_words(alias, text_words) for alias in location_aliases(base_location)
    ):
        return any(phrase_in_words(anchor, text_words) for anchor in anchors)
    return False


def location_in_text(location, text_words):
    if split_region_location(location)[1]:
        return regional_location_in_text(location, text_words)
    for alias in location_aliases(location):
        if phrase_in_words(alias, text_words):
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
        if location_in_text(location, text_words):
            add_unique(matched_locations, location)
    expected_found = location_in_text(expected_location, text_words)
    if expected_found:
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


def existing_download_is_valid(folder, year, province, known_provinces):
    path = find_existing_download(folder, province)
    if not path:
        return False
    audit = validate_download(path, province, known_provinces)
    if audit["expected_location_found"]:
        return True

    actual = audit["matched_locations"][0] if audit["matched_locations"] else "unknown"
    mismatch_path = mismatch_path_for(folder, province, actual, path.suffix or ".xls")
    path.replace(mismatch_path)
    append_audit(
        {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "scope": "national",
            "event": "existing_file_mismatch",
            "year": year,
            "expected_location": province,
            "final_path": str(path),
            "saved_path": str(mismatch_path),
            "ok": False,
            "error": "existing file did not validate for expected location",
            **audit,
        }
    )
    return False


async def click_row(page, label, timeout_ms=WAIT_ROW):
    target_norm = norm_text(label)
    deadline = time.monotonic() + timeout_ms / 1000
    while True:
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
                await row.click()
                await zk(page, 700)
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
                    if (style.display === "none" || style.visibility === "hidden") return false;
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
        if time.monotonic() >= deadline:
            return False
        await zk(page, 300)


async def reset(page):
    try:
        btn = page.locator("input[value='Ekran Temizle']")
        if await btn.count() > 0:
            await btn.first.click(timeout=2000)
            await zk(page, 1200)
    except Exception:
        pass

    if not await click_row(page, MENU_ITEM):
        raise RuntimeError(f"Could not select menu item {MENU_ITEM!r}")
    await zk(page, 1500)


async def click_year(page, year):
    """On the neighbourhood menu the years are radio buttons, not list rows."""
    labels = page.locator("td.hbox label:visible")
    n = 0
    for attempt in range(20):
        texts = [clean(x) for x in await labels.all_inner_texts()]
        n = len(texts)
        if any(texts):
            break
        if attempt in (4, 10):  # the menu row toggles; click it again to re-render the years
            await click_row(page, MENU_ITEM)
        await zk(page, 700)
    print(f"    year labels visible: {[clean(x) for x in await labels.all_inner_texts()][:12]}")
    for i in range(n):
        if clean(await labels.nth(i).inner_text()) == clean(year):
            await labels.nth(i).click(timeout=15000)
            break
    else:
        return False
    await zk(page, 2500)
    return True


async def read_years(page):
    years = []
    labels = await page.locator("td.hbox label:visible").all_inner_texts()
    for text in labels:
        text = clean(text)
        if re.match(r"^(19|20)\d{2}", text):
            add_unique(years, text)
    if years:
        return years
    rows = await page.locator(".listbox-btable tr, .listbox-body tr").all_inner_texts()
    for text in rows:
        text = clean(text)
        if re.match(r"^(19|20)\d{2}", text):
            add_unique(years, text)
    return years


async def read_provinces(page):
    menu_keywords = (
        "milletvekili",
        "seçim",
        "adaylar",
        "sandık",
        "siyasi",
        "bağımsız",
        "gümrük",
        "yurt",
        "bölge",
    )
    for _ in range(20):
        rows = await page.locator(".listbox-btable tr, .listbox-body tr").all_inner_texts()
        provinces = []
        for text in rows:
            text = clean(text)
            if not text:
                continue
            if re.match(r"^(19|20)\d{2}", text):
                continue
            if any(keyword in text.lower() for keyword in menu_keywords):
                continue
            add_unique(provinces, text)
        if provinces:
            return provinces
        await zk(page, 500)
    return []


async def ensure_mutlak(page):
    clicked = await page.evaluate(
        """
        () => {
            const norm = (value) => (value || "")
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
            const visible = (el) => {
                const style = window.getComputedStyle(el);
                if (style.display === "none" || style.visibility === "hidden") return false;
                const rect = el.getBoundingClientRect();
                return rect.width > 0 && rect.height > 0;
            };

            const labels = Array.from(document.querySelectorAll("label"))
                .filter((label) => norm(label.innerText || label.textContent).includes("mutlaksonuc"));
            if (!labels.length) return false;

            const label = labels.find(visible) || labels[0];
            const input = label.htmlFor ? document.getElementById(label.htmlFor) : null;
            if (input && input.checked) return true;
            if (visible(label)) {
                label.click();
                return true;
            }
            if (input) {
                input.click();
                return true;
            }
            return true;
        }
        """
    )
    if clicked:
        await zk(page, 800)


async def assert_selected_rows(page, year, province):
    selected = await page.evaluate(
        """
        () => Array.from(document.querySelectorAll(".itemsel, [z\\\\.sel='true']"))
            .map((el) => (el.innerText || el.textContent || "").replace(/\\s+/g, " ").trim())
            .filter(Boolean)
        """
    )
    if not any(norm_text(text) == norm_text(province) for text in selected):
        raise RuntimeError(f"Province {province!r} is not visibly selected")


async def select_excel_format(page):
    clicked = await page.evaluate(
        """
        () => {
            const visible = (el) => {
                const style = window.getComputedStyle(el);
                if (style.display === "none" || style.visibility === "hidden") return false;
                const rect = el.getBoundingClientRect();
                return rect.width > 0 && rect.height > 0;
            };
            const radios = Array.from(document.querySelectorAll("input[type='radio']"));
            const visibleRadios = radios.filter(visible);
            if (!visibleRadios.length) return false;

            const formatY = Math.max(...visibleRadios.map((radio) => radio.getBoundingClientRect().y));
            const visibleFormatRadios = visibleRadios
                .filter((radio) => Math.abs(radio.getBoundingClientRect().y - formatY) < 8)
                .sort((a, b) => a.getBoundingClientRect().x - b.getBoundingClientRect().x);
            if (!visibleFormatRadios.length) return false;

            const firstIndex = radios.indexOf(visibleFormatRadios[0]);
            const lastIndex = radios.indexOf(visibleFormatRadios[visibleFormatRadios.length - 1]);
            const formatRadios = radios.slice(firstIndex, lastIndex + 1);

            // Some legacy years hide the real Excel radio between visible HTML/PDF controls.
            const excelRadio = formatRadios[1] || visibleFormatRadios[1] || formatRadios[0];
            if (!excelRadio) return false;
            excelRadio.click();
            return true;
        }
        """
    )
    if not clicked:
        raise RuntimeError("Could not select Excel table format")
    await zk(page, 1000)


async def download_excel_report(page, folder, year, province, known_provinces=None):
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
    final_path = output_path_from_download(folder, province, download)
    suffix = final_path.suffix or ".xls"
    tmp_path = folder / f".{slugify(province)}.{int(time.time() * 1000)}.download{suffix}"
    await download.save_as(tmp_path)

    audit = validate_download(tmp_path, province, known_provinces)
    record = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "scope": "national",
        "year": year,
        "expected_location": province,
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
    mismatch_path = mismatch_path_for(folder, province, actual, suffix)
    tmp_path.replace(mismatch_path)
    record["saved_path"] = str(mismatch_path)
    record["ok"] = False
    record["error"] = "expected location was not found in downloaded workbook"
    append_audit(record)

    if audit["file_size"] < 20_000 and not audit["matched_locations"]:
        raise EmptyReportError(f"TUIK returned a header-only workbook for {province!r}")
    raise RuntimeError(
        f"Downloaded workbook did not validate for {province!r}; "
        f"matched locations: {audit['matched_locations'] or ['unknown']}"
    )


async def select_and_download(page, year, province, provinces):
    await reset(page)
    if not await click_year(page, year):
        raise RuntimeError(f"Could not select year {year!r}")
    await zk(page, 1500)
    if not await click_row(page, province):
        raise RuntimeError(f"Could not select {province!r}")
    await zk(page, 1500)
    await ensure_mutlak(page)
    await assert_selected_rows(page, year, province)
    return await download_excel_report(page, output_folder(year), year, province, provinces)


def rescue_mismatched(prog):
    """Re-validate files previously quarantined to _mismatched/ using the current
    validation logic.  Any file that now passes for its expected province is moved to
    the correct output path and marked done in the progress tracker.

    Returns the number of files rescued and the updated done_set.
    """
    done_set = set(prog.get("done", []))
    rescued = 0

    for year, provinces in prog.get("year_provinces", {}).items():
        mismatch_dir = output_folder(year) / "_mismatched"
        if not mismatch_dir.exists():
            continue

        slug_to_province = {slugify(p): p for p in provinces}
        seen_slugs: set[str] = set()

        for mfile in sorted(mismatch_dir.glob("*.xls*")):
            # Filename pattern: "<expected_slug>__actual_<actual_slug>__<timestamp>.xls"
            expected_slug = mfile.stem.split("__")[0]
            province = slug_to_province.get(expected_slug)
            if not province:
                continue

            key = combo_key(year, province)
            if key in done_set:
                continue
            if find_existing_download(output_folder(year), province):
                continue
            # Only rescue once per province (first matching file wins)
            if expected_slug in seen_slugs:
                continue

            audit = validate_download(mfile, province, provinces)
            if not audit["expected_location_found"]:
                continue

            final_path = output_folder(year) / f"{expected_slug}{mfile.suffix}"
            mfile.replace(final_path)
            seen_slugs.add(expected_slug)
            done_set.add(key)
            prog["done"] = sorted(done_set)
            prog["failed"] = [f for f in prog.get("failed", []) if f != key]
            save_progress(prog)
            append_audit(
                {
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                    "scope": "national",
                    "event": "rescued_from_mismatch",
                    "year": year,
                    "expected_location": province,
                    "final_path": str(final_path),
                    "rescued_from": str(mfile),
                    "ok": True,
                    **audit,
                }
            )
            rescued += 1
            print(f"  Rescued: {year} / {province}  →  {final_path.name}")

    return rescued, done_set


async def main():
    prog = load_progress()
    done_set = set(prog.get("done", []))

    print("=" * 65)
    print("  TUIK Milletvekili - Direct Excel Downloader")
    print("=" * 65)
    if done_set:
        print(f"  Resuming - {len(done_set)} combinations already done")

    if prog.get("year_provinces"):
        print("\n[0] Rescuing previously quarantined files with updated validation...")
        n_rescued, done_set = rescue_mismatched(prog)
        if n_rescued:
            print(f"  Rescued {n_rescued} file(s) from _mismatched/ folders.")
        else:
            print("  Nothing to rescue.")

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

        print("\n[1] Loading national election page...")
        await recover_page(page)

        await reset(page)
        years = await read_years(page)
        print(f"[2] Years ({len(years)}): {years}\n")

        if PROBE_ONLY:
            print("PROBE MODE - counting provinces per year:\n")
            total = 0
            for year in years:
                await reset(page)
                await click_row(page, year)
                provinces = await read_provinces(page)
                total += len(provinces)
                print(f"  {year:35s} -> {len(provinces):3d} provinces")
            print(f"\n  Total Excel downloads needed: {total}")
            await browser.close()
            return

        global_done = 0
        t_start = time.time()

        years = [y for y in years if YEAR_FILTER in y]
        print(f"    filtered years: {years}")
        for yi, year in enumerate(years, 1):
            print(f"\n{'=' * 65}")
            print(f"  YEAR [{yi}/{len(years)}]: {year}")
            print(f"{'=' * 65}")

            try:
                await reset(page)
                if not await click_year(page, year):
                    raise RuntimeError(f"Could not select year {year!r}")
                await zk(page, 1500)
                provinces = await read_provinces(page)
            except Exception as ex:
                print(f"  FAILED to initialize year: {ex}")
                await recover_page(page)
                continue

            print(f"    provinces offered: {provinces[:90]}")
            provinces = [p for p in provinces if PROV_FILTER in norm_text(p)]
            print(f"    filtered provinces: {provinces}")
            prog["year_provinces"][year] = provinces
            save_progress(prog)

            to_do = []
            year_folder = output_folder(year)
            for province in provinces:
                key = combo_key(year, province)
                if key in done_set and existing_download_is_valid(
                    year_folder, year, province, provinces
                ):
                    continue
                done_set.discard(key)
                to_do.append(province)
            prog["done"] = sorted(done_set)
            save_progress(prog)
            print(
                f"  Provinces: {len(provinces)} total | "
                f"{len(provinces) - len(to_do)} done | {len(to_do)} remaining"
            )
            if to_do:
                await recover_page(page)

            for pi, province in enumerate(to_do, 1):
                elapsed = time.time() - t_start
                eta = ""
                if global_done:
                    secs_per = elapsed / global_done
                    eta = f"  ETA ~{max(0, (len(to_do) - pi) * secs_per / 60):.0f}min"
                print(f"  [{pi}/{len(to_do)}] {province}{eta}", end="  ", flush=True)

                key = combo_key(year, province)
                path = None
                for attempt in range(1, RETRY_MAX + 1):
                    try:
                        path = await select_and_download(page, year, province, provinces)
                        break
                    except EmptyReportError as ex:
                        print(f"\n    attempt {attempt}: {ex}", end="  ", flush=True)
                        if attempt < RETRY_MAX:
                            await recover_page(page)
                    except Exception as ex:
                        print(f"\n    attempt {attempt}: {ex}", end="  ", flush=True)
                        if attempt < RETRY_MAX:
                            await recover_page(page)

                if path:
                    done_set.add(key)
                    prog["done"] = sorted(done_set)
                    prog["failed"] = [failed for failed in prog.get("failed", []) if failed != key]
                    save_progress(prog)
                    global_done += 1
                    print(f"Saved {path.relative_to(OUTPUT_DIR)}")
                    if MAX_DOWNLOADS and global_done >= MAX_DOWNLOADS:
                        print(f"\n  Reached TUIK_MAX_DOWNLOADS={MAX_DOWNLOADS}; stopping.")
                        await browser.close()
                        failed = prog.get("failed", [])
                        print("\n" + "=" * 65)
                        print(f"  Done: {len(done_set)} Excel files saved | Failed: {len(failed)}")
                        print(f"  Output folder: {OUTPUT_DIR.resolve()}")
                        print("=" * 65)
                        return
                    if pi < len(to_do):
                        await recover_page(page)
                else:
                    add_unique(prog.setdefault("failed", []), key)
                    save_progress(prog)
                    print("FAILED")

            print(f"\n  {year} done.")

        await browser.close()

    failed = prog.get("failed", [])
    print("\n" + "=" * 65)
    print(f"  Done: {len(done_set)} Excel files saved | Failed: {len(failed)}")
    if failed:
        print("  Failed combinations are listed in progress_downloads.json")
    print(f"  Output folder: {OUTPUT_DIR.resolve()}")
    print("=" * 65)


if __name__ == "__main__":
    try:
        import nest_asyncio

        nest_asyncio.apply()
        asyncio.get_event_loop().run_until_complete(main())
    except ImportError:
        asyncio.run(main())
