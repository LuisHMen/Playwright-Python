from playwright.sync_api import Playwright, expect
import pytest

@pytest.mark.parametrize("username, password",
                         [("luis_hmen", "4hmen0"),
                          ("test_name", "710test"),
                          pytest.param("admin@admin.com", "admin123", marks=pytest.mark.xfail)])
def test_option_1(set_up, username, password):
    page = set_up

    user_field = page.get_by_role("textbox", name="Email")
    pass_field = page.get_by_role("textbox", name="Password")
    submit_button = page.get_by_role("button", name="Submit")
    error_message = page.locator(".alert-danger")

    user_field.fill(username)
    pass_field.fill(password)
    submit_button.click()
    expect(error_message).to_have_text("Bad credentials! Please try again! Make sure that you've registered.")

table = [("luis_hmen", "4hmen0"),
        ("test_name", "710test"),
        pytest.param("admin@admin.com", "admin123", marks=pytest.mark.xfail)]

@pytest.mark.parametrize("username, password", table)
def test_option_2(set_up, username, password):
    page = set_up

    user_field = page.get_by_role("textbox", name="Email")
    pass_field = page.get_by_role("textbox", name="Password")
    submit_button = page.get_by_role("button", name="Submit")
    error_message = page.locator(".alert-danger")

    user_field.fill(username)
    pass_field.fill(password)
    submit_button.click()
    expect(error_message).to_have_text("Bad credentials! Please try again! Make sure that you've registered.")

data = {
    'argnames': 'username, password',
    'argvalues': [("luis_hmen", "4hmen0"),
                  ("test_name", "710test"),
                  ("admin@admin.com", "test432")]
        }

@pytest.mark.parametrize(**data)
def test_option_3(set_up, username, password) -> None:
    page = set_up

    user_field = page.get_by_role("textbox", name="Email")
    pass_field = page.get_by_role("textbox", name="Password")
    submit_button = page.get_by_role("button", name="Submit")
    error_message = page.locator(".alert-danger")

    user_field.fill(username)
    pass_field.fill(password)
    submit_button.click()
    expect(error_message).to_have_text("Bad credentials! Please try again! Make sure that you've registered.")