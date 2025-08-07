from playwright.sync_api import Playwright
from POM.Pages.login_fixture_page import Login
from excel.register_form_page import register
import pytest

# A Python function becomes a pytest fixture when decorated with @pytest.fixture. 
# This decorator signals to pytest that the function should be treated as a fixture.

# Setup and Teardown:
# Fixtures can manage both setup and teardown.
# Code before a yield statement in a fixture function constitutes the setup phase.
# Code after a yield statement constitutes the teardown phase, which executes after the test(s) that used the fixture have completed.

# Scope:
# Fixtures can have different scopes (e.g., function, class, module, session), 
# determining how frequently they are executed and their lifetime.

# Fixture function.
# A function-scoped fixture runs before each test function that requests it.

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

# A session-scoped fixture runs once per pytest session.
# This means you can keep a session active while tests are running.

@pytest.fixture(scope="session")
def session(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(7000)

    log = Login(page)

    log.navigate("https://qa-practice.netlify.app/auth_ecommerce")
    log.enter_username("admin@admin.com")
    log.enter_password("admin123")
    log.submit_credentials()
    log.valid_login_sucessful("SHOPPING CART")

    # ---------------------
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def set_up_excel(playwright: Playwright):
    browser = playwright.chromium.launch(headless = False, slow_mo = 700, args=["--start-maximized"])
    context = browser.new_context(viewport={'width': 1500, 'height': 800})
    page = context.new_page()
    page.set_default_timeout(7000)

    excel = register(page)

    excel.navigate("https://qa-practice.netlify.app/register")

    # ---------------------
    yield page
    context.close()
    browser.close()