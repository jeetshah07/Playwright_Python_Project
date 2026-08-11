from playwright.sync_api import expect


class RegisterPage:

    def __init__(self, page):
        self.page = page

        # Personal Information
        self.title_mr = page.locator("#id_gender1")
        self.title_mrs = page.locator("#id_gender2")
        self.password = page.locator("#password")

        # Date of Birth
        self.day = page.locator("#days")
        self.month = page.locator("#months")
        self.year = page.locator("#years")

        # Checkboxes
        self.newsletter = page.locator("#newsletter")
        self.special_offers = page.locator("#optin")

        # Address Information
        self.first_name = page.locator("#first_name")
        self.last_name = page.locator("#last_name")
        self.company = page.locator("#company")
        self.address = page.locator("#address1")
        self.country = page.locator("#country")
        self.state = page.locator("#state")
        self.city = page.locator("#city")
        self.zipcode = page.locator("#zipcode")
        self.mobile = page.locator("#mobile_number")

        # Buttons
        self.create_account_button = page.locator(
            "button[data-qa='create-account']"
        )

        self.account_created_text = page.get_by_text("Account Created!")
        self.continue_button = page.locator(
            "a[data-qa='continue-button']"
        )

    def fill_personal_information(self, password):
        self.title_mr.check()
        self.password.fill(password)

    def select_date_of_birth(self, day, month, year):
        self.day.select_option(day)
        self.month.select_option(month)
        self.year.select_option(year)

    def select_newsletter(self):
        self.newsletter.check()

    def select_special_offers(self):
        self.special_offers.check()

    def fill_address_information(
        self,
        first_name,
        last_name,
        company,
        address,
        country,
        state,
        city,
        zipcode,
        mobile
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.company.fill(company)
        self.address.fill(address)
        self.country.select_option(country)
        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zipcode)
        self.mobile.fill(mobile)

    def click_create_account(self):
        self.create_account_button.click()

    def verify_account_created(self):
        expect(self.account_created_text).to_be_visible()

    def click_continue(self):
        self.continue_button.click()