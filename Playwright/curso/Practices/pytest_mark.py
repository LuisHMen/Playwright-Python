from playwright.sync_api import Playwright, expect
import pytest

@pytest.mark.xfail(reason="Possible bug.")
def test_dropdown_second_level(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    page = browser.new_page()
    page.set_default_timeout(5000)

    page.goto("https://qa-practice.netlify.app/dropdowns")

    page.get_by_role("button", name="Dropdown").click()
    expect(page.get_by_role("listitem").filter(has_text="Some other action")).to_be_visible()
    # This test fail because the link is not visible, as expected.
    page.get_by_role("link", name="Second level - 1").click()
        
    page.close()

@pytest.mark.skip("The country does not exist.")
def test_select_an_unexisting_country(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    page = browser.new_page()
    page.set_viewport_size({'width': 1280, 'height': 720})

    page.goto("https://qa-practice.netlify.app/dropdowns")
        
    page.locator("#dropdown-menu").select_option("Esparta")
    expect(page.locator("#dropdown-menu")).to_contain_text("Esparta")

    page.close()

def test_select_a_country(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    page = browser.new_page()
    page.set_viewport_size({'width': 1280, 'height': 720})

    page.goto("https://qa-practice.netlify.app/dropdowns")
        
    page.locator("#dropdown-menu").select_option("Mexico")
    expect(page.locator("#dropdown-menu")).to_contain_text("Mexico")

    page.close()