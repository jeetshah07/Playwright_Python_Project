from pages.products_page import ProductsPage


def test_verify_products(page):

    products = ProductsPage(page)

    products.open_products_page()

    products.verify_products_page()

    products.open_first_product()

    products.verify_product_details()