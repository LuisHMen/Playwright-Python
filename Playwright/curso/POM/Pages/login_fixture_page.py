from playwright.sync_api import Playwright, Page, expect

class Login:
    def __init__(self, page):
        self.page = page
        # Elements
        self.username_field = page.get_by_role("textbox", name="Email")
        self.password_field = page.get_by_role("textbox", name="Password")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.title = page.locator('.section-header')
        self.error_message = page.locator(".alert-danger")

    def navigate(self, url):
        self.page.goto(url)

    def enter_username(self, username):
        expect(self.username_field).to_be_enabled()
        self.username_field.fill(username)
    
    def enter_password(self, password):
        expect(self.password_field).to_be_enabled()
        self.password_field.fill(password)
    
    def submit_credentials(self):
        self.submit_button.click()
    
    def valid_login_sucessful(self, message):
        expect(self.title).to_have_text(message)
    
    def read_error_message(self, error_message):
        expect(self.error_message).to_have_text(error_message)