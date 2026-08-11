def test_login_invalid_credentials(api_request_context):
    response = api_request_context.post(
        "verifyLogin",
        form={"email": "doesnotexist@example.com", "password": "wrongpass123"},
    )
    body = response.json()
    assert body["responseCode"] == 404


def test_login_without_email(api_request_context):
    response = api_request_context.post(
        "verifyLogin",
        form={"password": "wrongpass123"},
    )
    body = response.json()
    assert body["responseCode"] == 400


def test_login_wrong_method_get(api_request_context):
   
    response = api_request_context.get("verifyLogin")
    body = response.json()
    assert body["responseCode"] == 405


def test_search_product_without_param(api_request_context):
    response = api_request_context.post("searchProduct", form={})
    body = response.json()
    assert body["responseCode"] == 400


def test_products_list_wrong_method_put(api_request_context):
    
    response = api_request_context.put("productsList")
    body = response.json()
    assert body["responseCode"] == 405


def test_get_brands_list(api_request_context):
    response = api_request_context.get("brandsList")
    body = response.json()
    assert response.ok
    assert body["responseCode"] == 200
    assert isinstance(body["brands"], list)


def test_create_account_existing_email(api_request_context):
    
    payload = {
        "name": "Dup User",
        "email": "dup.test.user@example.com",
        "password": "Test@1234",
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "5",
        "birth_year": "1995",
        "firstname": "Dup",
        "lastname": "User",
        "company": "QA Training",
        "address1": "123 Test Street",
        "address2": "",
        "country": "India",
        "zipcode": "600001",
        "state": "Tamil Nadu",
        "city": "Salem",
        "mobile_number": "9876543210",
    }
    api_request_context.post("createAccount", form=payload)

    
    response = api_request_context.post("createAccount", form=payload)
    body = response.json()
    assert body["responseCode"] == 400

    
    api_request_context.delete(
        "deleteAccount",
        form={"email": payload["email"], "password": payload["password"]},
    )