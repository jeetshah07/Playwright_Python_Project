from playwright.sync_api import expect

from pages.login_page import LoginPage

from utils.test_data import (
    INVALID_EMAIL,
    INVALID_PASSWORD
)


def test_invalid_login(page):

    login = LoginPage(page)

    login.open_login_page()

    login.login(
        INVALID_EMAIL,
        INVALID_PASSWORD
    )

    expect(
    login.get_invalid_login_message()
    ).to_be_visible()
    