from playwright.sync_api import Playwright, expect

class combos:
    def __init__(self, page):
        self.page = page
        self.combo1 = page.locator('#comboBox1')
        self.combo2 = page.locator('#comboBox2')
        self.os = page.locator('#os')
        self.version = page.locator('#version')
        self.submit_btn = page.get_by_role("button", name="Enviar")
        self.confirmation_message = page.locator('#flashMessage')
    
    def navigate(self):
        self.page.goto("https://validaciones.rodrigovillanueva.com.mx/ComboBox_ok.html")

    def select_combo1(self, value_one):
        self.combo1.select_option(value = value_one)
    
    def select_combo2(self, value_two):
        self.combo2.select_option(value = value_two)
    
    def select_os(self, operarive_system):
        self.os.select_option(value = operarive_system)
    
    def select_version(self, version):
        self.version.select_option(value = version)
    
    def submit_form(self):
        self.submit_btn.click()

    def read_confirmation_message(self, message):
        expect(self.confirmation_message).to_have_text(message)