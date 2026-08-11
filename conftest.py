import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext

BASE_URL = "https://automationexercise.com/api/" 


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:

    request_context = playwright.request.new_context(
        base_url=BASE_URL
    )

    yield request_context

    request_context.dispose()