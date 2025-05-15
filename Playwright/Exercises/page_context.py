from playwright.sync_api import Playwright, expect

def test_manage_window(playwright: Playwright):
    # slow_mo Tiempo que toma cada acción en ejecutarse.
    # args Argumentos para el browser. En este caso, para maximizar la ventana.
    browser = playwright.webkit.launch(headless = False, slow_mo = 1000, args=["--start-maximized"])
    # Create a new incognito browser context.
    context = browser.new_context(
        no_viewport=True
        # viewport={'width': 1500, 'height': 800}
    )
    # Create a new page in a pristine context.
    page = context.new_page()

    page.goto("https://demoqa.com")
    expect(page).to_have_title("DEMOQA")

    context.close()
    browser.close()

# command to execute: pytest Playwright/Exercises/page_context.py