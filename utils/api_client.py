import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        # Helps bypass basic bot detection
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })

    def sync_with_browser(self, driver):
        """Copies cookies and the secret XSRF-TOKEN from Selenium to the API."""
        for cookie in driver.get_cookies():
            self.session.cookies.set(cookie['name'], cookie['value'])
            if cookie['name'] == 'XSRF-TOKEN':
                # This is the 'Handstamp' needed for OrangeHRM
                self.session.headers.update({'X-XSRF-TOKEN': cookie['value']})

    def post(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=json)

