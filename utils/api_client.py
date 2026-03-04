import pytest

from pages.login_page import LoginPage


@pytest.fixture
def api(config):
    # Use the same base URL as your UI (e.g., https://opensource-demo.orangehrmlive.com)
    # Strip the '/web/index.php...' part to get just the domain
    base_domain = config['base_url'].split('/web')[0]
    return APIClient(base_domain)


def test_user_can_view_profile(api, driver, config):
    # 1. UI Layer: Login to get the 'Membership Card'
    login_page = LoginPage(driver)
    login_page.load(config['base_url'])
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    # 2. Sync: Pass the browser's secret tokens to the API tool
    api.sync_with_browser(driver)

    # 3. API Layer: Create a real user in the OrangeHRM database
    user_data = {
        "username": "testuser2026",  # Change this every time you run!
        "password": "Password123",
        "status": True,
        "userRoleId": 2,
        "empNumber": 7  # Use a real ID from your PIM list
    }

    # The real OrangeHRM API endpoint for creating users
    response = api.post("/web/index.php/api/v2/admin/users", json=user_data)

    # 4. Verification
    # OrangeHRM API usually returns 200 OK for a successful creation
    assert response.status_code == 200
    print("User successfully created via API!")
