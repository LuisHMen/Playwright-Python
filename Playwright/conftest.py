from playwright.sync_api import Playwright
import pytest

@pytest.fixture(scope="function")
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless = False, slow_mo = 1000, args=["--start-maximized"])
    # Create a new incognito browser context.
    context = browser.new_context(
        # no_viewport=True
        viewport={'width': 1500, 'height': 800}
        # record_video_dir="Playwright/POM/videos"
    )
    page = context.new_page()

    page.goto("https://qa-practice.netlify.app/auth_ecommerce")

    # ---------------------
    yield page
    context.close()
    browser.close()