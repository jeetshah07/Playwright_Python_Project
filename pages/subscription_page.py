from playwright.sync_api import expect
from utils.test_data import BASE_URL


class SubscriptionPage:

    def __init__(self, page):
        self.page = page

        # Navigation
        self.cart_link = page.locator(
            "a[href='/view_cart']"
        ).first

        # Subscription
        self.subscription_heading = page.locator(
            "h2"
        ).filter(
            has_text="Subscription"
        )

        self.email_box = page.locator(
            "#susbscribe_email"
        )

        self.subscribe_button = page.locator(
            "#subscribe"
        )

        self.success_message = page.locator(
            ".alert-success"
        )

    # -------------------------
    # Home Page
    # -------------------------

    def open_home_page(self):
        self.page.goto(BASE_URL)

    # -------------------------
    # Cart Page
    # -------------------------

    def open_cart_page(self):
        self.page.goto(BASE_URL)
        self.cart_link.click()

    # -------------------------
    # Common Methods
    # -------------------------

    def scroll_to_bottom(self):
        self.page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

    def verify_subscription_heading(self):
        expect(
            self.subscription_heading
        ).to_be_visible()

    def subscribe(self, email):
        self.email_box.fill(email)
        self.subscribe_button.click()

    def verify_subscription_success(self):
        expect(
            self.success_message
        ).to_contain_text(
            "You have been successfully subscribed!"
        )