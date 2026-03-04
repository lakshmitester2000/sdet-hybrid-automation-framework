import pytest
from utils.api_client import APIClient


@pytest.fixture
def api():
    return APIClient("https://api.staging.example.com")


def test_user_can_view_profile(api, driver):
    # 1. API Layer: Create a user via POST (Backend)
    user_data = {"name": "John Doe", "email": "john@example.com"}
    response = api.post("/users", json=user_data)
    assert response.status_code == 201

    # 2. UI Layer: Verify user exists on the Dashboard (Frontend)
    driver.get("https://staging.example.com/login")
    # ... Selenium login logic here ...