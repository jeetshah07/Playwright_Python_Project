from playwright.sync_api import expect
from utils.test_data import BASE_URL


class CartPage:

    def __init__(self, page):
        self.page = page

        # Navigation
        self.products_link = page.locator(
            "a[href='/products']"
        ).first

        # First Product
        self.first_product = page.locator(
            ".product-image-wrapper"
        ).nth(0)

        self.first_add_to_cart = page.locator(
            ".overlay-content .add-to-cart"
        ).nth(0)

        # Second Product
        self.second_product = page.locator(
            ".product-image-wrapper"
        ).nth(1)

        self.second_add_to_cart = page.locator(
            ".overlay-content .add-to-cart"
        ).nth(1)

        # Modal Buttons
        self.continue_shopping = page.get_by_role(
            "button",
            name="Continue Shopping"
        )

        self.view_cart = page.get_by_role(
            "link",
            name="View Cart"
        )

        # Cart Table
        self.cart_rows = page.locator(
            "#cart_info_table tbody tr"
        )

    # -------------------------

    def open_products_page(self):
        self.page.goto(BASE_URL)
        self.products_link.click()

    def add_first_product(self):
        self.first_product.hover()
        self.first_add_to_cart.click()

    def continue_shopping_click(self):
        self.continue_shopping.click()

    def add_second_product(self):
        self.second_product.hover()
        self.second_add_to_cart.click()

    def open_cart(self):
        self.view_cart.click()

    def verify_two_products(self):
        expect(self.cart_rows).to_have_count(2)