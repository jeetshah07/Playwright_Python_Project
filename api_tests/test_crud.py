import time

EMAIL = f"demo.user.{int(time.time())}@example.com"
PASSWORD = "Test@1234"

USER_DATA = {
    "name": "Demo User",
    "email": EMAIL,
    "password": PASSWORD,
    "title": "Mr",
    "birth_date": "10",
    "birth_month": "5",
    "birth_year": "1995",
    "firstname": "Demo",
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


def test_1_create_account(api_request_context):
    response = api_request_context.post("createAccount", form=USER_DATA)
    body = response.json()
    assert body["responseCode"] == 201


def test_2_get_account(api_request_context):
    response = api_request_context.get("getUserDetailByEmail", params={"email": EMAIL})
    body = response.json()
    assert body["responseCode"] == 200
    assert body["user"]["email"] == EMAIL


def test_3_update_account(api_request_context):
    USER_DATA["name"] = "Demo User (Updated)"
    USER_DATA["city"] = "Chennai"

    response = api_request_context.put("updateAccount", form=USER_DATA)
    body = response.json()
    assert body["responseCode"] == 200


def test_4_delete_account(api_request_context):
    response = api_request_context.delete("deleteAccount", form={"email": EMAIL, "password": PASSWORD})
    body = response.json()
    assert body["responseCode"] == 200