import requests
import allure

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    @allure.step("Sending GET request to {endpoint}")
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params)
        return response

    @allure.step("Sending POST request to {endpoint}")
    def post(self, endpoint, data=None, json=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data, json=json)
        return response