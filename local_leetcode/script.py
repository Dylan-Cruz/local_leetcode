import os
from typing import Dict
import argparse
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page import LeetcodeProblem
from writer import Writer


def valid_directory(path: str) -> str:
    if os.path.isdir(path):
        return path
    raise argparse.ArgumentTypeError(f"{path} is not a directory.")


def valid_url(url: str) -> str:
    parsed_url = urlparse(url)
    if bool(parsed_url.netloc):
        return url
    else:
        raise argparse.ArgumentTypeError(f"{url} is not a valid URL.")


def parseArgs() -> argparse.Namespace:
    # Create the parser
    parser = argparse.ArgumentParser(
        description="Scrapes web content from leetcode and creates a local directory in which you can implement your solution."
    )

    # Add the arguments
    parser.add_argument(
        "url", type=valid_url, help="The URL of the leetcode problem to scrape"
    )
    parser.add_argument(
        "out_dir", type=valid_directory, help="The path to the output directory"
    )

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
