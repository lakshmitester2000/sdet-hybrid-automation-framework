import pytest
import random  # Added this to make unique usernames
from utils.api_client import APIClient
from pages.login_page import LoginPage


@pytest.fixture
def api(config):
    # This automatically gets the correct base URL from your config.yaml
    base_domain = config['base_url'].split('/web')[0]
    return APIClient(base_domain)


def test_user_can_view_profile(api, driver, config):
    # 1. UI Layer: LOGIN FIRST
    # We do this to get the "Membership Card" (Cookies) from the browser
    login_page = LoginPage(driver)
    login_page.load(config['base_url'])
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    # 2. SYNC STEP:
    # This tells the API Tool to "steal" the login tokens from the browser
    api.sync_with_browser(driver)

    # 3. API Layer: CREATE USER
    # We use a random number so the test doesn't fail if you run it twice
    random_id = random.randint(100, 999)
    user_data = {
        "username": f"testuser_{random_id}",
        "password": "Password123",
        "status": True,
        "userRoleId": 2,
        "empNumber": 7  # Ensure this ID exists in your PIM list!
    }

    # Making the actual API call to OrangeHRM
    response = api.post("/web/index.php/api/v2/admin/users", json=user_data)

    # 4. VERIFICATION
    # Check if the API said "200 OK" (Success)
    assert response.status_code == 200
    print(f"Successfully created user: testuser_{random_id}")

    # Check if the browser is on the Dashboard
    assert "dashboard" in driver.current_url.lower()