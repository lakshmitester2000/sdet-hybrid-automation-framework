from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def click(self, by, locator):
        self.find(by, locator).click()

    def send_keys(self, by, locator, text):
        element = self.find(by, locator)
        element.clear()
        element.send_keys(text)

    def wait_for_visibility(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )

    def get_title(self):
        return self.driver.title