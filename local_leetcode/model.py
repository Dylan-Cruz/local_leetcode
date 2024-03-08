from typing import Dict
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LeetcodeProblem:
    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url

    def load(self) -> None:
        print(f"Loading problem with URL: {self.url}")
        self.browser.get(self.url)
        print("Problem loaded.")

    def parse(self) -> Dict:
        browser = self.browser
        page_data = {}

        # parse the name and number from the title
        title_element = browser.find_element(By.CSS_SELECTOR, "div.text-title-large a")
        title_components = title_element.text.split(". ")
        page_data["name"] = title_components[1]
        page_data["number"] = title_components[0]

        # store the url
        page_data["url"] = self.url

        # parse difficulty
        difficulty_classes = [
            "text-difficulty-easy",
            "text-difficulty-medium",
            "text-difficulty-hard",
        ]

        for dc in difficulty_classes:
            elements = browser.find_elements(By.CLASS_NAME, dc)
            if len(elements) > 0:
                page_data["difficulty"] = elements[0].text
                break

        # parse topics //a[@target='_blank' and contains(@href, '/tag')]
        # parse description div[data-track-load="description_content"]
        # parse solution stub #editor div.monaco-scrollable-element

        return page_data


# {
#     "name": "Group Anagrams",
#     "number": 49,
#     "url": "https://leetcode.com/problems/group-anagrams/description/",
#     "difficulty": "Medium",
#     "topics": ["Array", "Hash Table", "String", "Sorting"],
# }
