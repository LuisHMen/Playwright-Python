from playwright.sync_api import Playwright, expect
import pytest

@pytest.mark.parametrize("username, password",
                         [("luis_hmen", "4hmen0"),
                          ("test_name", "710test"),
                          pytest.param("admin@admin.com", "admin123", marks=pytest.mark.xfail)])
def test_math(set_up, username, password):
    """
    browser = playwright.webkit.launch(headless=False, slow_mo=700)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://qa-practice.netlify.app/auth_ecommerce")
    """
    page = set_up

    user_field = page.get_by_role("textbox", name="Email")
    pass_field = page.get_by_role("textbox", name="Password")
    submit_button = page.get_by_role("button", name="Submit")
    error_message = page.locator(".alert-danger")

    user_field.fill(username)
    pass_field.fill(password)
    submit_button.click()
    expect(error_message).to_have_text("Bad credentials! Please try again! Make sure that you've registered.")