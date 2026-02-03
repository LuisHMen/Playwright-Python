import time
from playwright.sync_api import Page, expect

def test_form1(page: Page):
    page.goto("https://validaciones.rodrigovillanueva.com.mx/Form1.html")

    # Define a Timeout.
    page.set_default_timeout(7000)

    page.locator("#nombre").fill("Luis")
    page.locator("#apellidos").fill("Hernandez")
    page.locator("#tel").fill("5511223344")
    page.locator("#email").fill("luis@pruebas.com")
    page.locator("#direccion").fill("Where Peter Parker lives.")

    # Time to wait for the next step to execute.
    time.sleep(3)
    page.get_by_role("button", name="Enviar").click()

    expect(page.get_by_text("El formulario se ha enviado correctamente.", exact=True)).to_be_visible()
    page.screenshot(path="Playwright/Exercises/screenshots/SaveForm.png")

    page.get_by_role("button", name="Limpiar").click()
    page.screenshot(path="Playwright/Exercises/forms/screenshots/CleanForm.png")
    
    page.close()

# command to execute: pytest --slowmo 1000 --headed Playwright/Exercises/inputs1.py
