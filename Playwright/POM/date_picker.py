from playwright.sync_api import Playwright
from Pages.date_picker_page import date_picker

def test_enter_values(playwright: Playwright):
#with sync_playwright() as play:
    browser = playwright.webkit.launch(headless=False, slow_mo=1000, args=["--start-maximized"])
    context = browser.new_context()
    page = context.new_page()

    dp = date_picker(page)
    dp.navigate("https://qa-practice.netlify.app/calendar")
    dp.select_date_range("7", "21")
    dp.click_apply_btn()
    dp.confirm_date_range("01/07/2018 - 01/21/2018")
    dp.select_date("17")

    # ---------------------
    context.close()
    browser.close()