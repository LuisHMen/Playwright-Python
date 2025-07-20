from playwright.sync_api import Playwright, expect

class shopping:
    def __init__(self, page):
        self.page = page
        
        # Elements
        self.add_to_card_btn = page.get_by_role("button", name="ADD TO CART")
        self.item_name = page.locator('.cart-item-title')
        self.total_pay = page.locator('.cart-total-price')
        self.checkout_btn = page.get_by_role("button", name="PROCEED TO CHECKOUT")
        
        self.shipping_details = page.get_by_role("heading", name="Shipping Details")
        self.phone_number = page.get_by_role("textbox", name="Enter phone number")
        self.street = page.get_by_role("textbox", name="Little Streets")
        self.city = page.get_by_role("textbox", name="London")
        self.country = page.locator("#countries_dropdown_menu")

        self.submit_btn = page.get_by_role("button", name="Submit Order")
        self.confirmation_msg = page.locator("#message")

    # Actions
    def add_products(self):
        self.add_to_card_btn.nth(4).click()
        self.add_to_card_btn.nth(0).click()
    
    def confirm_products_added(self, product1, product2):
        expect(self.item_name.nth(0)).to_have_text(product1)
        expect(self.item_name.nth(1)).to_have_text(product2)
    
    def calculate_total_cost(self, cost):
        expect(self.total_pay).to_have_text(cost)
    
    def proceed_to_checkout(self, title):
        self.checkout_btn.click()
        expect(self.shipping_details).to_have_text(title)
    
    def enter_shipping_details(self, phone, street, city, country):
        self.phone_number.fill(phone)
        self.street.fill(street)
        self.city.fill(city)
        self.country.select_option(country)
        self.submit_btn.click()
    
    def confirm_order(self, confirmation):
        expect(self.confirmation_msg).to_have_text(confirmation)