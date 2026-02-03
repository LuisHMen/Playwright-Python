from playwright.sync_api import expect

class date_picker():
    def __init__(self, page):
        self.page = page
        # Elements
        self.range_field = page.locator('#range-date-calendar')
        self.apply_btn = page.get_by_role('button', name="Apply")
        self.date_field = page.locator('input#calendar')
    
    def navigate(self, url):
        self.page.goto(url)
    
    def select_date_range(self, start_date, end_date):
        self.range_field.click()
        self.page.get_by_role("cell", name=start_date, exact=True).first.click()
        self.page.get_by_role("cell", name=end_date).first.click()

    def click_apply_btn(self):
        self.apply_btn.click()

    def confirm_date_range(self, date_range):
        expect(self.range_field).to_have_value(date_range)
    
    def select_date(self, day):
        self.date_field.click()
        self.page.get_by_role("cell", name=day).click()
        self.page.get_by_role("cell", name=day).press("Escape")