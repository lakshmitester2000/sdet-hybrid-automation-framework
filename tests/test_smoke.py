import pytest
from selenium import webdriver

def test_google_connection(driver):
    """Simple test to verify Grid connectivity."""
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    print("\n🚀 Smoke Test Passed: Connection to Selenium Grid is successful!")

