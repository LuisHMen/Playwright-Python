from playwright.sync_api import Playwright, expect

def test_order_by_names(playwright: Playwright):
    browser = playwright.webkit.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    context.set_default_timeout(5000)
    page = context.new_page()

    page.goto("https://datatables.net/extensions/select/examples/checkbox/checkbox.html")

    # Elements
    rows_sorted = page.locator('.sorting_1')
    column_name = page.locator('//*[@id="example"]/thead/tr/th[2]/div')

    # Actions / Validations
    column_name.click()
    expect(rows_sorted).to_have_count(10)

     # ---------------------
    context.close()
    browser.close()

def test_search_by_position(playwright: Playwright):
    browser = playwright.webkit.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    context.set_default_timeout(5000)
    page = context.new_page()

    page.goto("https://datatables.net/extensions/select/examples/checkbox/checkbox.html")

    # Elements
    search_field = page.locator("input#dt-search-0")

    # Actions
    search_field.fill("Office Manager")
    page.mouse.wheel(0, 400)
    for i in range (1, 4):
        expect(page.locator(f"//tbody/tr[{i}]/td[3]")).to_have_text("Office Manager")
    
    page.screenshot(path="Playwright/Practices/screenshots/table.png")

     # ---------------------
    context.close()
    browser.close()