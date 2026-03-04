import pytest
import yaml
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import allure

# In your test file:
def test_example(driver, config):
    # config['base_url'] pulls "https://opensource-demo.orangehrmlive.com/..."
    driver.get(config['base_url'])

@pytest.fixture(scope="session")
def config():
    # Inside Docker, everything is usually relative to /app
    # This tries the direct path first, then a relative one
    possible_paths = [
        "config/config.yaml",
        "/app/config/config.yaml",
        "../config/config.yaml"
    ]

    for path in possible_paths:
        if os.path.exists(path):
            with open(path) as f:
                return yaml.safe_load(f)

    raise FileNotFoundError(f"Could not find config.yaml in any of: {possible_paths}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        try:
            if 'driver' in item.fixturenames:
                driver = item.funcargs['driver']
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Fail to take screenshot: {e}")

@pytest.fixture()
def driver(config):
    browser = os.getenv("BROWSER", config.get("browser", "chrome")).lower()
    hub_url = "http://selenium-hub:4444/wd/hub"
    driver = None  # Initialize to avoid errors

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        try:
            driver = webdriver.Remote(command_executor=hub_url, options=options)
        except Exception:
            # Local fallback
            driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        try:
            driver = webdriver.Remote(command_executor=hub_url, options=options)
        except Exception:
            driver = webdriver.Firefox(options=options)

    if driver is None:
        raise pytest.UsageError(f"Driver failed to initialize for browser: {browser}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()
