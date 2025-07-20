from playwright.sync_api import Playwright
from POM.Pages.login_fixture_page import Login
import pytest

@pytest.fixture(scope="function")
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless = False, slow_mo = 1000, args=["--start-maximized"])
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

@pytest.fixture(scope="session")
def session(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(7000)

    page.goto("https://qa-practice.netlify.app/auth_ecommerce")

    log = Login(page)

    log.enter_username("admin@admin.com")
    log.enter_password("admin123")
    log.submit_credentials()
    log.valid_login_sucessful("SHOPPING CART")

    # ---------------------
    yield page
    context.close()
    browser.close()