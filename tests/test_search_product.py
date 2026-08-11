from pages.products_page import ProductsPage
from utils.test_data import SEARCH_PRODUCT


def test_search_product(page):

    products = ProductsPage(page)

    products.open_products_page()

    products.verify_products_page()

    products.search_product(
        SEARCH_PRODUCT
    )

    products.verify_searched_products()

    products.verify_product_is_displayed(
        SEARCH_PRODUCT
    )