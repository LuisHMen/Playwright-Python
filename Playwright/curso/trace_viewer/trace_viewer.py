from playwright.sync_api import Playwright, expect

def test_shopping_cart(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=2000, args=["--start-maximized"])
    context = browser.new_context()
    page = context.new_page()
    #page.set_default_timeout(5000)

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots = True, snapshots = True)

    page.goto('https://qa-practice.netlify.app/products_list')

    add_to_card_btn = page.get_by_role("button", name="ADD TO CART")
    item_name = page.locator('.cart-item-title')
    total_pay = page.locator('.cart-total-price')
    purchase_btn = page.get_by_role("button", name="PURCHASE")
    confirmation_msg = page.locator('#message')

    add_to_card_btn.nth(4).click()
    add_to_card_btn.nth(0).click()
    expect(item_name.nth(0)).to_have_text('Nokia 105, Black')
    expect(item_name.nth(1)).to_have_text('Apple iPhone 12, 128GB, Black')
    expect(total_pay).to_have_text('$925.98')
    purchase_btn.click()
    expect(confirmation_msg).to_have_text('Congrats! Your order of $925.98 has been registered!')

    # ---------------------
    context.tracing.stop(path='Playwright/Practices/trace_viewer/trace.zip')
    context.close()
    browser.close()