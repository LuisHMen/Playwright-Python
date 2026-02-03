from playwright.sync_api import Playwright
from Pages.login_page import Login

# pytest Playwright/curso/POM/login.py

def test_valid_login(playwright: Playwright):
    browser = playwright.webkit.launch(headless = False, slow_mo = 1000)
    page = browser.new_page()
    page.set_default_timeout(5000)

    log = Login(page)
    log.navigate()
    log.enter_username('standard_user')
    log.enter_password('secret_sauce')
    log.submit_credentials()
    log.valid_login_sucessful('Products')

    page.close()
    browser.close()

def test_invalid_login(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.set_default_timeout(5000)

    error_message="Epic sadface: Username and password do not match any user in this service"

    log = Login(page)
    log.navigate()
    log.enter_username('invalid_user')
    log.enter_password('invalid_password')
    log.submit_credentials()
    log.read_error_message(error_message)

    page.close()
    browser.close()