import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture()
def driver(config):
    browser = config.get("browser", "chrome")

    if browser == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-site-isolation-trials")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--remote-allow-origins=*")

        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()