
from typing import Dict
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page import LeetcodeProblem
from writer import Writer


def parseArgs() -> argparse.Namespace:
    # Create the parser
    parser = argparse.ArgumentParser(
        description="Scrapes web content from leetcode and creates a local directory in which you can implement your solution."
    )

    # Add the arguments
    parser.add_argument(
        "url", type=str, help="The URL of the leetcode problem to scrape"
    )
    parser.add_argument("out_dir", type=str, help="The path to the output directory")

    # Parse the arguments
    return parser.parse_args()


def scrape_problem_data() -> Dict:
    print(f"Scraping url: {args.url}...")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless") # triggers cloudflare human check
    with webdriver.Chrome(options=chrome_options) as browser:
        browser.implicitly_wait(5)
        page = LeetcodeProblem(browser, args.url)
        page.load()
        return page.parse()


args = parseArgs()
problem_data = scrape_problem_data()
print("Generating output...")
writer = Writer(args.out_dir, problem_data)
writer.write()
print("Done")