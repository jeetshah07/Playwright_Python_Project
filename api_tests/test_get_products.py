def test_get_products(api_request_context):

    response = api_request_context.get("productsList") 

    print("FINAL URL:", response.url)
    print("STATUS:", response.status)

    body = response.json()

    assert response.ok
    assert body["responseCode"] == 200
    assert isinstance(body["products"], list)