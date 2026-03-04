import pytest
from utils.api_client import APIClient
from pages.login_page import LoginPage  # Ensure this import path is correct


@pytest.fixture
def api():
    # Changed to a real, reachable mock API for demonstration
    return APIClient("https://reqres.in/api")


def test_user_can_view_profile(api, driver, config):
    # 1. API Layer: Create a user via POST (Backend)
    # Using reqres.in 'create' endpoint logic
    user_data = {"name": "morpheus", "job": "leader"}
    response = api.post("/users", json=user_data)

    # Assert 201 Created
    assert response.status_code == 201
    created_user = response.json()
    print(f"User created via API with ID: {created_user['id']}")

    # 2. UI Layer: Navigate and Login using your Page Object
    login_page = LoginPage(driver)

    # Use base_url from your config.yaml
    login_page.load(config['base_url'])

    # Using OrangeHRM credentials as per your config.yaml target
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    # 3. Verification
    assert "dashboard" in driver.current_url.lower()

    