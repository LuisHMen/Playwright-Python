from playwright.sync_api import Playwright, Page, expect

class Login:
    def __init__(self, page):
        self.page = page
        # Elements
        self.username_field = page.get_by_placeholder('Username')
        self.password_field = page.get_by_placeholder('Password')
        self.submit_button = page.locator('#login-button')
        self.title = page.locator('.title')
        self.error_message = page.locator('[data-test="error"]')

    def navigate(self):
        self.page.goto("https://www.saucedemo.com")

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