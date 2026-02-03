from playwright.sync_api import expect

class login:
    def __init__(self, page):
        self.page = page
        # Elements
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.submit_btn = page.locator("#login-button")
        self.title = page.locator(".title")

    def navigate(self, url):
        self.page.goto(url)

    def type_username(self, username):
        expect(self.username_field).to_be_enabled()
        self.username_field.fill(username)

    def type_password(self, password):
        expect(self.password_field).to_be_enabled()
        self.password_field.fill(password)
    
    def submit_credentials(self):
        self.submit_btn.click()
    
    def login_successful(self, message):
        expect(self.title).to_have_text(message)