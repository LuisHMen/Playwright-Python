from playwright.sync_api import Playwright, expect

def test_checkbox(playwright: Playwright):
    browser = playwright.chromium.launch(headless = False, slow_mo = 1000, args=["--start-maximized"])
    context = browser.new_context(viewport={'width': 1500, 'height': 800})
    context.set_default_timeout(1000)  # Set default timeout to 1 second
    # page.set_default_timeout(7000)
    page = context.new_page()

    page.goto("https://validaciones.rodrigovillanueva.com.mx/Radios_Ok.html")

    # Elements.
    name = page.get_by_placeholder("Nombre")
    Telefono = page.get_by_placeholder("Telefono")
    option1 = page.get_by_label("Opción 1")
    option2 = page.get_by_label("Opción 2")
    optionA = page.get_by_label("Opción A")
    optionB = page.get_by_label("Opción B")
    btn_enviar = page.locator("[type='submit']")
    btn_limpiar = page.locator(".btn-secondary")

    # Actions
    name.fill("Luis Hernández")
    Telefono.fill("5511223344")
    expect(option1).to_be_visible()
    option1.check()
    expect(optionB).to_be_visible()
    optionB.check()

    page.screenshot(path="Playwright/screenshots/checkbox.png")

    # btn_enviar.click()
    btn_limpiar.click()

    expect(name).to_be_empty()
    expect(Telefono).to_be_empty()
    expect(option2).not_to_be_checked()
    expect(optionB).not_to_be_checked()

    context.close()
    browser.close()

# command to execute: pytest Playwright/Exercises/checkbox.py