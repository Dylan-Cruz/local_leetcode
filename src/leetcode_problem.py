from typing import Dict
from selenium.webdriver.remote.webdriver import WebDriver


class LeetcodeProblem:
    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url

    def load(self) -> None:
        print(f"Loading problem with URL: {self.url}")
        self.browser.get(self.url)
        print("Problem loaded.")

    def parse_page(self) -> Dict:
        return {}
