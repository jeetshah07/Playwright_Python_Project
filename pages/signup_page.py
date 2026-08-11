from utils.test_data import BASE_URL


class SignupPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.signup_link = page.get_by_text("Signup / Login")

        self.name_input = page.locator(
            "input[data-qa='signup-name']"
        )

        self.email_input = page.locator(
            "input[data-qa='signup-email']"
        )

        self.signup_button = page.get_by_role(
            "button",
            name="Signup"
        )

        self.existing_email_message = page.get_by_text(
            "Email Address already exist!"
        )

    # Actions
    def open_signup_page(self):
        self.page.goto(BASE_URL)
        self.signup_link.click()

    def enter_name(self, name):
        self.name_input.fill(name)

    def enter_email(self, email):
        self.email_input.fill(email)

    def click_signup(self):
        self.signup_button.click()

    def signup(self, name, email):
        self.enter_name(name)
        self.enter_email(email)
        self.click_signup()

    # Validation
    def get_existing_email_message(self):
        return self.existing_email_message
    
