import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as play:
        browser = await play.chromium.launch(headless = False)
        page = await browser.new_page()
        await page.goto("https://demoqa.com") # "http://whatsmyuseragent.org/"
        print(await page.title())
        # await page.screenshot(path = "async.png")
        await browser.close()

asyncio.run(main())