from playwright.sync_api import expect
from utils.test_data import BASE_URL


class CasesPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.test_cases_link = page.locator(
            "a[href='/test_cases']"
        ).first

        self.page_heading = page.locator(
            "h2.title.text-center"
        )

    # Actions
    def open_test_cases_page(self):
        self.page.goto(BASE_URL)
        self.test_cases_link.click()

    def verify_test_cases_page(self):
        expect(self.page).to_have_url(
            "https://automationexercise.com/test_cases"
        )

        expect(self.page_heading).to_have_text(
            "Test Cases"
        )