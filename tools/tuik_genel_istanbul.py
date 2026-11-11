"""Download the 2023 general-election results by neighbourhood (bölge) for Istanbul from
TÜİK, one report per district (İlçe), using the helpers of tuik_genel_bolge.py (adapted
from the author's tuik_scraper2.py). The neighbourhood menu requires an electoral region
AND a district. Output: data/raw/elections/genel_bolge/2023/<region>_<district>.xls."""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import tuik_genel_bolge as t  # noqa: E402
from playwright.async_api import async_playwright  # noqa: E402

YEAR = "2023"
REGIONS = ["İstanbul (1)", "İstanbul (2)", "İstanbul (3)"]
OUT = Path("data/raw/elections/genel_bolge/2023")


async def open_region(page, region):
    await t.recover_page(page)
    if not await t.click_row(page, t.MENU_ITEM):
        raise RuntimeError("menu")
    await t.zk(page, 3000)
    await page.get_by_text(YEAR, exact=True).first.click()
    await t.zk(page, 4000)
    if not await t.click_row(page, region):
        raise RuntimeError(f"region {region}")
    await t.zk(page, 3000)


async def districts(page):
    """Rows of the listbox headed 'İlçe:'."""
    return await page.evaluate(
        """() => {
            const heads = Array.from(document.querySelectorAll('*')).filter(e => e.children.length === 0 && (e.textContent || '').trim() === 'İlçe:');
            for (const h of heads) {
                let box = h;
                for (let i = 0; i < 8 && box; i++) {
                    const rows = box.querySelectorAll('.listbox-btable tr, .listbox-body tr, tr');
                    const names = Array.from(rows).map(r => (r.innerText || '').trim()).filter(x => x && x !== 'İlçe:');
                    if (names.length > 1 && names.length < 60) return names;
                    box = box.parentElement;
                }
            }
            return [];
        }"""
    )


async def download(page, region, ilce):
    await t.select_excel_format(page)
    async with page.expect_download(timeout=t.WAIT_REPORT) as info:
        await page.locator("input[value='Raporu Oluştur']").click()
    d = await info.value
    path = OUT / f"{t.slugify(region)}_{t.slugify(ilce)}.xls"
    await d.save_as(path)
    return path


async def main():
    OUT.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(headless=True, args=["--no-sandbox"])
        ctx = await b.new_context(
            viewport={"width": 1280, "height": 1100}, locale="tr-TR", accept_downloads=True
        )
        page = await ctx.new_page()
        page.set_default_timeout(120_000)
        for region in REGIONS:
            await open_region(page, region)
            names = await districts(page)
            print(region, "districts:", names, flush=True)
            for ilce in names:
                path = OUT / f"{t.slugify(region)}_{t.slugify(ilce)}.xls"
                if path.exists() and path.stat().st_size > 1000:
                    continue
                for attempt in range(3):
                    try:
                        await open_region(page, region)
                        if not await t.click_row(page, ilce):
                            raise RuntimeError(f"district {ilce}")
                        await t.zk(page, 2000)
                        await t.ensure_mutlak(page)
                        print("  ", ilce, "->", await download(page, region, ilce), flush=True)
                        break
                    except Exception as ex:  # noqa: BLE001
                        print(
                            "  ", ilce, "attempt", attempt + 1, "failed:", str(ex)[:150], flush=True
                        )
        await b.close()


asyncio.run(main())
