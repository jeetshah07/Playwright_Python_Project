from playwright.sync_api import expect
from pages.login_page import LoginPage
from utils.test_data import EMAIL, PASSWORD

def test_login(page):

    login = LoginPage(page)

    login.open_login_page()

    login.login(
    EMAIL,
    PASSWORD
)

    expect(
        page.get_by_text("Logged in as")
    ).to_be_visible()