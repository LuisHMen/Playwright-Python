from playwright.sync_api import Playwright
from pages.login_page import login

# pytest Playwright/pom/login.py

def test_valid_login(playwright: Playwright):
    browser = playwright.chromium.launch(headless = False, slow_mo=500)
    page = browser.new_page()
    page.set_default_timeout(7000)

    log_in = login(page)
    log_in.navigate("https://www.saucedemo.com")
    log_in.type_username("standard_user")
    log_in.type_password("secret_sauce")
    log_in.submit_credentials()
    log_in.login_successful("Products")

    page.close()
    browser.close()