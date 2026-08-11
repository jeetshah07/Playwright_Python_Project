from pages.login_page import LoginPage
from pages.account_page import AccountPage
from utils.test_data import EMAIL, PASSWORD


def test_logout(page):

    login = LoginPage(page)
    account = AccountPage(page)

    login.open_login_page()

    login.login(
        EMAIL,
        PASSWORD
    )

    account.verify_login_success()

    account.click_logout()

    account.verify_logout_success()