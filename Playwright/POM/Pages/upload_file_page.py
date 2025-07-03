from playwright.sync_api import expect

class upload_file:
    def __init__(self, page):
        self.page = page
        # Elements
        self.file_field = page.locator('#file_upload')
        self.submit_btn = page.get_by_role("button", name="Submit")
        self.confirmation_message = page.locator('#file_upload_response')

    def navigate(self, url):
        self.page.goto(url)
    
    def upload_file(self, file):
        self.file_field.set_input_files(file)
    
    def submit_file(self):
        self.submit_btn.click()

    def read_confirmation_message(self, message):
        expect(self.confirmation_message).to_have_text(message)