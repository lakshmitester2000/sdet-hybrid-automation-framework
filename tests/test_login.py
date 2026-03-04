from pages.login_page import LoginPage
from utils.excel_utils import read_excel
from utils.logger import get_logger
import time
import pytest

logger = get_logger()

def test_login(driver, config):
    data = read_excel("data/login_data.xlsx", "Sheet1")
    base_url = config["base_url"]

    for row in data:
        username = row["username"]
        password = row["password"]

        logger.info(f"Testing login with username: {username}")

        login = LoginPage(driver)
        login.load(base_url)
        print("Current URL:", driver.current_url)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()

        # NEW: Wait for dashboard to appear
        time.sleep(10)
        print("Current URL:", driver.current_url)

        assert "dashboard" in driver.current_url.lower(), "Login did not go to dashboard"

        # Assert that login was successful by checking title contains "OrangeHRM"
        #assert "OrangeHRM" in login.get_title()

