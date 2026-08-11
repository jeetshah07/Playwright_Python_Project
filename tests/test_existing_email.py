from playwright.sync_api import expect

from pages.signup_page import SignupPage
from utils.test_data import NAME, EMAIL


def test_register_existing_email(page):

    signup = SignupPage(page)

    signup.open_signup_page()

    signup.signup(
        NAME,
        EMAIL
    )

    expect(
    signup.get_existing_email_message()
    ).to_be_visible()