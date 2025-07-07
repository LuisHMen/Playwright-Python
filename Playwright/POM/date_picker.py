from playwright.sync_api import sync_playwright, Playwright
from Playwright.POM.Pages.date_picker_page import date_picker

def test_enter_values(playwright: Playwright):
#with sync_playwright() as play:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000, args=["--start-maximized"])
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000)

    dt = date_picker(page)
    dt.navigate()
    dt.enter_letters("LuisHMen")
    dt.enter_alphabetic_text("John117")
    dt.enter_email("test.pruebas@pruebas.com")
    dt.enter_url("https://example.com")
    dt.enter_date("2025-06-29")
    dt.submit_form()
    dt.read_confirmation_message("Formulario enviado exitosamente")

    # ---------------------
    context.close()
    browser.close()