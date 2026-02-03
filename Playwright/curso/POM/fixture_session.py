from Pages.shopping_page import shopping

def test_add_to_cart(session) -> None:
    page = session
    shop = shopping(page)

    shop.add_products()
    shop.confirm_products_added("Nokia 105, Black", "Apple iPhone 12, 128GB, Black")

def test_calculate_cost(session) -> None:
    page = session
    shop = shopping(page)

    shop.calculate_total_cost("$925.98")

def test_checkout_products(session) -> None:
    page = session
    shop = shopping(page)

    shop.proceed_to_checkout("Shipping Details")

def test_enter_shipping_details(session) -> None:
    page = session
    shop = shopping(page)

    shop.enter_shipping_details("5511223344", "Wallaby 991", "Gothan", "Nicaragua")

def test_confirm_order(session) -> None:
    page = session
    shop = shopping(page)
    
    shop.confirm_order("Congrats! Your order of $925.98 has been registered and will be shipped to Wallaby 991, Gothan - Nicaragua.")