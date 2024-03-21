from typing import Dict
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from markdownify import markdownify as md


EDITOR_TEXT_SELECTOR = (
    By.CSS_SELECTOR,
    "#editor div.editor-scrollable",
)  # targets the solution stub text in the editor, not including line numbers

LANGUAGE_BUTTON_SELECTOR = (
    By.XPATH,
    "//div[@id='editor']//button//*[name() = 'svg'][contains(@class, 'fa-chevron-down')]",
)  # targets the chevron icon that triggers the language selection in the editor

TARGET_LANGUAGE_SELECTOR = (
    By.XPATH,
    "//div[@id='editor']//div[contains(text(), '{target_language}')]",
)  # targets a button in the language selection pop over with the text of the target language. must call format passing the desired language


class LeetcodeProblemPage:
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    def load(self) -> None:
        print(f"Loading problem with URL: {self.url}")
        self.driver.get(self.url)
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(
                [
                    By.CSS_SELECTOR,
                    "div.text-title-large a",
                ]
            )
        )
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
        topic_elements = driver.find_elements(
            By.XPATH, "//a[@target='_blank' and contains(@href, '/tag')]"
        )
        topics = [element.get_attribute("innerText") for element in topic_elements]
        page_data["topics"] = topics

        # parse description into markdown
        desc_root = driver.find_element(
            By.CSS_SELECTOR, "div[data-track-load='description_content']"
        )
        desc_html = desc_root.get_attribute("innerHTML")
        page_data["description_html"] = desc_html
        desc_markdown = md(desc_html)
        page_data["description_markdown"] = desc_markdown

        # parse solution stub
        self.select_language("Python3")

        editor = driver.find_element(
            By.CSS_SELECTOR, "#editor div.monaco-scrollable-element"
        )
        page_data["solution_stub"] = editor.text

        return page_data

    def select_language(self, language: str) -> None:
        """
        Selects the specified programming language in the editor.
        Note that it must be different than the value previsouly selected.

        Args:
            language (str): The name of the language to select.

        Raises:
            NoSuchElementException: If the language button or target language is not found.
        """
        driver = self.driver

        # get the current text of the editor
        editor_text = driver.find_element(*EDITOR_TEXT_SELECTOR).text

        # interact with the page to select desired language
        driver.find_element(*LANGUAGE_BUTTON_SELECTOR).click()

        driver.find_element(
            TARGET_LANGUAGE_SELECTOR[0],
            TARGET_LANGUAGE_SELECTOR[1].format(target_language=language),
        ).click()

        # wait for the text to have changed
        WebDriverWait(driver, 5).until(
            lambda driver: editor_text
            not in driver.find_element(*EDITOR_TEXT_SELECTOR).text
        )
