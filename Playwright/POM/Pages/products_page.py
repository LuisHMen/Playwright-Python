from playwright.sync_api import expect

class products:
    def __init__(self, page):
        self.page = page
        # Elements
        self.filter_btn = page.locator(".product_sort_container")
        self.price = page.locator(".inventory_item_price")
        
        def filter_products(self, option):
            self.filter_btn.select_option(option)

        def add_to_cart(self, product_name):
            self.add_to_cart_btn = page.locator(f"#add-to-cart-{product_name}").click()

        def validate_order_by_low_price(self, low_price):
            expect(self.inventory_item_price).to_have_text(low_price)

        def validate_order_by_high_price(self, high_price):
            expect(self.inventory_item_price).to_have_text(high_price)