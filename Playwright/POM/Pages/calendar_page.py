from playwright.sync_api import expect

class date_picker:
    def __init__(self, page):
        self.page = page
        # Elements
        self.letters = page.locator('#onlyLetters')
        self.alphanumeric = page.locator('#alphanumeric')
        self.email = page.locator('#emailFormat')
        self.url = page.locator('#urlFormat')
        self.date = page.get_by_placeholder("Fecha")
        self.submit_btn = page.get_by_role("button", name="Enviar")
        self.confirmation_message = page.locator('#flashMessage')
    
    def navigate(self):
        self.page.goto('https://validaciones.rodrigovillanueva.com.mx/Campos_Dos_OK.html')
    
    def enter_letters(self, text):
        self.letters.fill(text)
    
    def enter_alphabetic_text(self, text):
        self.alphanumeric.fill(text)
    
    def enter_email(self, email):
        self.email.fill(email)

    def enter_url(self, url):
        self.url.fill(url)
    
    def enter_date(self, date):
        self.date.fill(date)
    
    def submit_form(self):
        self.submit_btn.click()
     
    def read_confirmation_message(self, message):
        expect(self.confirmation_message).to_have_text(message)