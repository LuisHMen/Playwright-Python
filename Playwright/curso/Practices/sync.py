from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    # slow_mo Tiempo que toma cada acción en ejecutarse.
    browser = play.webkit.launch(headless = False, slow_mo = 3000)
    page = browser.new_page()
    page.goto("https://demoqa.com") # "http://whatsmyuseragent.org/"
    print(page.title())
    # page.screenshot(path = "async.png")
    browser.close()