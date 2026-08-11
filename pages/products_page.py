from playwright.sync_api import expect
from utils.test_data import BASE_URL


class ProductsPage:

    def __init__(self, page):
        self.page = page

        # Navigation
        self.products_link = page.locator(
            "a[href='/products']"
        ).first

        # Products Page
        self.all_products_heading = page.locator(
            "h2.title.text-center"
        )

        # First Product
        self.first_view_product = page.locator(
            "a[href='/product_details/1']"
        )

        # Product Details
        self.product_name = page.locator(
            ".product-information h2"
        )

        self.category = page.locator(
            ".product-information p"
        ).nth(0)

        self.price = page.locator(
            ".product-information span span"
        )

        self.availability = page.get_by_text(
            "Availability:"
        )

        self.condition = page.get_by_text(
            "Condition:"
        )

        self.brand = page.get_by_text(
            "Brand:"
        )

        # Search Product
        self.search_box = page.locator(
            "#search_product"
        )

        self.search_button = page.locator(
            "#submit_search"
        )

        self.searched_products_heading = page.locator(
            "h2.title.text-center"
        )

        self.searched_product = page.locator(
            ".features_items .productinfo p"
        ).first

    # ----------------------------
    # Navigation Methods
    # ----------------------------

    def open_products_page(self):
        self.page.goto(BASE_URL)
        self.products_link.click()

    # ----------------------------
    # TC08 Methods
    # ----------------------------

    def verify_products_page(self):
        expect(self.page).to_have_url(
            "https://automationexercise.com/products"
        )

        expect(
            self.all_products_heading
        ).to_contain_text(
            "All Products"
        )

    def open_first_product(self):
        self.first_view_product.click()

    def verify_product_details(self):

        expect(self.product_name).to_be_visible()

        expect(self.category).to_be_visible()

        expect(self.price).to_be_visible()

        expect(self.availability).to_be_visible()

        expect(self.condition).to_be_visible()

        expect(self.brand).to_be_visible()

    # ----------------------------
    # TC09 Methods
    # ----------------------------

    def search_product(self, product_name):
        self.search_box.fill(product_name)
        self.search_button.click()

    def verify_searched_products(self):
        self.page.wait_for_load_state("networkidle")
        expect(
        self.searched_products_heading
        ).to_be_visible(timeout=10000)
        expect(
        self.searched_products_heading
    ).to_contain_text(
        "Searched Products"
    )

    def verify_product_is_displayed(self, product_name):
        expect(
            self.searched_product
        ).to_have_text(
            product_name
        )