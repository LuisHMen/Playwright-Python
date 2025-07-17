from Pages.login_fixture_page import Login

def test_using_fixture(set_up) -> None:
    page = set_up

    fix = Login(page)

    #fix.navigate("/auth_ecommerce")
    fix.enter_username("admin@admin.com")
    fix.enter_password("admin123")
    fix.submit_credentials()
    fix.valid_login_sucessful("SHOPPING CART")

def test_login_fail(set_up) -> None:
    page = set_up

    fix = Login(page)

    fix.enter_username("admin@admin.com")
    fix.submit_credentials()
    fix.read_error_message("Bad credentials! Please try again! Make sure that you've registered.")