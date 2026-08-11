from playwright.sync_api import expect


class AccountPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.logged_in_text = page.get_by_text("Logged in as")
        self.logout_button = page.get_by_text("Logout")
        self.login_heading = page.get_by_text("Login to your account")

    # Actions
    def click_logout(self):
        self.logout_button.click()

    # Validations
    def verify_login_success(self):
        expect(self.logged_in_text).to_be_visible()

    def verify_logout_success(self):
        expect(self.login_heading).to_be_visible()