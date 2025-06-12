from playwright.sync_api import Playwright, Page
from Pages.combobox_page import combos
import random

# pytest Playwright/POM/selector.py

def test_select_values(playwright: Playwright):
    browser = playwright.webkit.launch(args=["--start-maximized"], headless=False, slow_mo=500)
    page = browser.new_page()
    page.set_default_timeout(5000)

    com = combos(page)
    com.navigate()
    com.select_combo1('Valor 2')
    com.select_combo2('Valor 5')
    com.select_os('Mac')
    com.select_version('macOS Mojave')
    com.submit_form()
    com.read_confirmation_message("Formulario enviado exitosamente")

    page.close()
    browser.close()

def test_select_random_values(playwright: Playwright):
    browser = playwright.webkit.launch(args=["--start-maximized"], headless=False, slow_mo=1000)
    page = browser.new_page()
    page.set_default_timeout(5000)

    com = combos(page)
    com.navigate()
    com.select_combo1('Valor 3')
    com.select_combo2('Valor 1')
    com.select_os('Windows')

    options = ['Windows 7', 'Windows 10', 'Windows 11']
    random_option = random.choice(options)
    com.select_version(random_option)

    com.submit_form()
    com.read_confirmation_message("Formulario enviado exitosamente")

    page.screenshot(path="Playwright/POM/images/selector.png")
    
    page.close()
    browser.close()