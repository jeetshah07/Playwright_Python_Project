import pytest


@pytest.mark.parametrize("search_term", ["top", "dress", "jean", "saree"])
def test_search_product(api_request_context, search_term):
    response = api_request_context.post("searchProduct", form={"search_product": search_term})
    body = response.json()
    assert body["responseCode"] == 200