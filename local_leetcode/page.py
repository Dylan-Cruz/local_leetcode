from typing import Dict
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

class LeetcodeProblem:
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    def load(self) -> None:
        print(f"Loading problem with URL: {self.url}")
        self.driver.get(self.url)
        print("Problem loaded.")

    def parse(self) -> Dict:
        driver = self.driver
        page_data = {}

        # parse the name and number from the title
        title_element = driver.find_element(By.CSS_SELECTOR, "div.text-title-large a")
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
            elements = driver.find_elements(By.CLASS_NAME, dc)
            if len(elements) > 0:
                page_data["difficulty"] = elements[0].text
                break

        
        # parse topics 
        topic_elements = driver.find_elements(By.XPATH, "//a[@target='_blank' and contains(@href, '/tag')]")
        topics = [element.get_attribute("innerText") for element in topic_elements]
        page_data["topics"] = topics

        # parse description div[data-track-load="description_content"]

        # parse solution stub 
        driver.find_element(By.XPATH, "//div[@id='editor']//button[contains(text(), 'C++')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='editor']//div[contains(text(), 'Python3')]").click()
        time.sleep(2)
        solution_lines = driver.find_elements(By.CSS_SELECTOR, "#editor div.monaco-scrollable-element div.view-line")
        page_data["solution_stub"] = "\n".join([line.text for line in solution_lines])

        print(page_data)
        return page_data

# {
#     "name": "Group Anagrams",
#     "number": 49,
#     "url": "https://leetcode.com/problems/group-anagrams/description/",
#     "difficulty": "Medium",
#     "topics": ["Array", "Hash Table", "String", "Sorting"],
# }
