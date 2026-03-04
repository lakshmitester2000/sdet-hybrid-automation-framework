from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class LoginPage(BasePage):

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self, base_url):
        self.driver.get(base_url)

    def enter_username(self, username):
        time.sleep(1)
        self.wait_for_visibility(*self.USERNAME)
        self.send_keys(*self.USERNAME, text=username)

    def enter_password(self, password):
        time.sleep(1)
        self.wait_for_visibility(*self.PASSWORD)
        self.send_keys(*self.PASSWORD, text=password)

    def click_login(self):
        self.wait_for_visibility(*self.LOGIN_BTN)
        self.click(*self.LOGIN_BTN)