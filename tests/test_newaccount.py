from pages.login_page import LoginPage
from utils.excel_utils import read_excel
from utils.logger import get_logger
import time
import pytest

logger = get_logger()

def test_login(driver, config):
    data = read_excel("data/login_data.xlsx", "Sheet1")
    base_url = config["base_url"]
