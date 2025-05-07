import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

def test_title(page: Page):
    page.goto("https://demoqa.com")
    expect(page).to_have_title(re.compile("QA"))
    
    page.locator("text = Elements").click()
    page.locator("text = Text Box").click()

    page.get_by_placeholder("Full Name").fill("Luis Hernández")
    page.get_by_placeholder("name@example.com").fill("luis@test.com")
    page.locator("#currentAddress").fill("Avengers Tower.")
    page.locator("#permanentAddress").fill("Narnia.")
    page.get_by_role("button", name = "Submit").click()
    expect(page.locator("#output")).to_be_visible()
    page.screenshot(path = "Playwright/Exercises/Form1.png")

# command to execute: pytest --slowmo 1000 --headed Playwright/Exercises/Form1.py