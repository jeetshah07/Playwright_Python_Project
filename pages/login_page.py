from utils.test_data import BASE_URL


class LoginPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.login_link = page.get_by_text("Signup / Login")
        self.email_input = page.locator("input[data-qa='login-email']")
        self.password_input = page.locator("input[data-qa='login-password']")
        self.login_button = page.get_by_role("button", name="Login")
        self.invalid_login_message = page.get_by_text(
            "Your email or password is incorrect!"
        )

    # Actions
    def open_login_page(self):
        self.page.goto(BASE_URL)
        self.login_link.click()

    def enter_email(self, email):
        self.email_input.fill(email)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    # Validations
    def get_invalid_login_message(self):
        return self.invalid_login_message