from pages.subscription_page import SubscriptionPage
from utils.test_data import SUBSCRIPTION_EMAIL


def test_verify_subscription_home(page):

    subscription = SubscriptionPage(page)

    subscription.open_home_page()

    subscription.scroll_to_bottom()

    subscription.verify_subscription_heading()

    subscription.subscribe(
        SUBSCRIPTION_EMAIL
    )

    subscription.verify_subscription_success()