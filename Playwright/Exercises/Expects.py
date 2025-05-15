from playwright.sync_api import Page, expect

def test_empty_form(page: Page):
    page.goto("https://validaciones.rodrigovillanueva.com.mx/Form1.html")

    # Define a Timeout.
    page.set_default_timeout(7000)

    # Elements.
    # Inputs.
    nombre = page.locator("#nombre")
    apellidos = page.locator("#apellidos")
    telefono = page.locator("#tel")
    email = page.locator("#email")
    direccion = page.locator("#direccion")
    # Buttons.
    Btn_Enviar = page.get_by_role("button", name="Enviar")
    Btn_Limpiar = page.get_by_role("button", name="Limpiar")
    # Messages.
    confirmacion = page.get_by_text("El formulario se ha enviado correctamente.", exact=True)

    # Actions.
    expect(nombre).to_be_empty()
    expect(apellidos).to_be_enabled()
    expect(telefono).to_be_empty()
    expect(email).to_be_visible()
    expect(direccion).to_be_empty()

    Btn_Enviar.click()
    
    expect(page.locator("#errorNombre")).to_contain_text("Nombre inválido")
    expect(page.locator("#errorApellidos")).to_contain_text("Apellidos inválidos")
    expect(page.locator("#errorTel")).to_contain_text("Teléfono inválido")
    expect(page.locator("#errorEmail")).to_contain_text("Email inválido")
    expect(page.locator("#errorDireccion")).to_contain_text("Dirección inválida")

    page.screenshot(path="Playwright/Exercises/screenshots/all_red.png")

    page.close()

# command to execute: pytest --slowmo 1000 --headed Playwright/Exercises/Expects.py
