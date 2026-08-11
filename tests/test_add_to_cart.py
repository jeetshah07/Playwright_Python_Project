from pages.cart_page import CartPage


def test_add_products_to_cart(page):

    cart = CartPage(page)

    cart.open_products_page()

    cart.add_first_product()

    cart.continue_shopping_click()

    cart.add_second_product()

    cart.open_cart()

    cart.verify_two_products()
    