from pages.signup_page import SignupPage
from pages.register_page import RegisterPage
from pages.account_page import AccountPage

from utils.helper import generate_email
from utils.test_data import (
    NAME,
    REGISTER_PASSWORD,
    FIRST_NAME,
    LAST_NAME,
    COMPANY,
    ADDRESS,
    COUNTRY,
    STATE,
    CITY,
    ZIPCODE,
    MOBILE
)


def test_register_user(page):

    signup = SignupPage(page)
    register = RegisterPage(page)
    account = AccountPage(page)

    # Generate a unique email
    email = generate_email()

    # Open Signup Page
    signup.open_signup_page()

    # Signup
    signup.signup(
        NAME,
        email
    )

    # Fill Registration Form
    register.fill_personal_information(
        REGISTER_PASSWORD
    )

    register.select_date_of_birth(
        "10",
        "5",
        "2004"
    )

    register.select_newsletter()

    register.select_special_offers()

    register.fill_address_information(
        FIRST_NAME,
        LAST_NAME,
        COMPANY,
        ADDRESS,
        COUNTRY,
        STATE,
        CITY,
        ZIPCODE,
        MOBILE
    )

    register.click_create_account()

    register.verify_account_created()

    register.click_continue()

    account.verify_login_success()