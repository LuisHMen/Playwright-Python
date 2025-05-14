# Same as the Inpunts1.py file, but in this one the elements were added to variables.

import time
from playwright.sync_api import Page, expect

def test_form1(page: Page):
    page.goto("https://validaciones.rodrigovillanueva.com.mx/Form1.html")

    # Define a Timeout.
    page.set_default_timeout(7000)

    # Elementos.
    nombre = page.locator("#nombre")
    apellidos = page.locator("#apellidos")
    telefono = page.locator("#tel")
    email = page.locator("#email")
    direccion = page.locator("#direccion")
    Btn_Enviar = page.get_by_role("button", name="Enviar")
    Btn_Limpiar = page.get_by_role("button", name="Limpiar")
    confirmacion = page.get_by_text("El formulario se ha enviado correctamente.", exact=True)

    # Acciones.
    nombre.fill("Luis")
    apellidos.fill("Hernandez")
    telefono.fill("5511223344")
    email.fill("luis@pruebas.com")
    direccion.fill("Where Peter Parker lives.")

    # Time to wait for the next step to execute.
    time.sleep(3)
    Btn_Enviar.click()

    expect(confirmacion).to_be_visible()
    page.screenshot(path="Playwright/Exercises/Inputs1_Img/SaveForm.png")

    Btn_Limpiar.click()
    page.screenshot(path="Playwright/Exercises/Inputs1_Img/CleanForm.png")
    
    page.close()

# command to execute: pytest --slowmo 1000 --headed Playwright/Exercises/Inputs.py
