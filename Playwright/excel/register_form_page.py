from playwright.sync_api import expect

class register:
    def __init__(self, page):
        self.page = page
        # Elements
        self.name_field = page.get_by_role("textbox", name="First Name")
        self.last_name_field = page.get_by_role("textbox", name="Last Name")
        self.phone_field = page.get_by_placeholder("Enter phone number")
        self.country_selector = page.locator("#countries_dropdown_menu")
        self.email_field = page.get_by_role("textbox", name="Email")
        self.password_field = page.get_by_role("textbox", name="Password")
        self.checkbox = page.locator(".form-check-input")
        self.submit_button = page.get_by_role("button", name="Register")
        self.confirmation_message = page.locator("#message")

    def navigate(self, url):
        self.page.goto(url)

    def enter_name(self, name):
        expect(self.name_field).to_be_enabled()
        self.name_field.fill(name)
    
    def enter_last_name(self, last_name):
        expect(self.last_name_field).to_be_enabled()
        self.last_name_field.fill(last_name)

    def enter_phone_number(self, phone_number):
        expect(self.phone_field).to_be_enabled()
        self.phone_field.fill(phone_number)
    
    def select_country(self, country):
        expect(self.country_selector).to_be_enabled()
        self.country_selector.select_option(country)

    def enter_email(self, email):
        expect(self.email_field).to_be_enabled()
        self.email_field.fill(email)

    def enter_password(self, password):
        expect(self.password_field).to_be_enabled()
        self.password_field.fill(password)
    
    def check_terms_box(self):
        self.checkbox.check()
        expect(self.checkbox).to_be_checked()
    
    def submit_register(self):
        self.submit_button.click()
    
    def read_confirmation_msg(self, message):
        expect(self.confirmation_message).to_have_text(message)