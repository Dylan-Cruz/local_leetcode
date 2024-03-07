import json
from typing import Dict
import argparse
import os
from bs4 import BeautifulSoup
import requests


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


def load_page(url: str) -> BeautifulSoup:
    print(f"Loading problem with URL: {args.url}")
    response = requests.get(args.url, timeout=5)
    page = BeautifulSoup(response.text, "html.parser")
    print("Problem loaded.")
    return page


def parse_meta_data(page: BeautifulSoup) -> Dict:

    return {}


def parse_problem(page: BeautifulSoup) -> Dict:
    pass


def parse_solution(page: BeautifulSoup) -> Dict:
    pass


def make_project_dir(out_dir: str, problem_number: str, problem_name: str) -> str:
    if os.path.exists(out_dir):
        dir_name = problem_number + "_" + problem_name.lower().replace(" ", "_")
        new_path = os.path.join(out_dir, dir_name)
        os.mkdir(new_path)
        return new_path

    raise FileNotFoundError(f"The directory {out_dir} does not exist.")


def output_write_up_file(out_dir: str) -> None:
    with open(os.path.join(out_dir, "write_up.md"), "w", encoding="utf-8") as f:
        f.write("# Write Up\n\n")
        f.write("## Approach\n\n")
        f.write("## Time Complexity\n\n")
        f.write("## Space Complexity\n")


def output_meta_file(out_dir: str, page: BeautifulSoup) -> None:
    data = {
        "name": "Group Anagrams",
        "number": "49",
        "url": "https://leetcode.com/problems/group-anagrams/description/",
        "difficulty": "Medium",
        "topics": ["Array", "Hash Table", "String", "Sorting"],
    }

    # create the meta.json file
    with open(os.path.join(out_dir, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def output_problem_file(out_dir: str, page: BeautifulSoup) -> None:

    # create the problem.md file
    with open(os.path.join(out_dir, "problem.md"), "w", encoding="utf-8") as f:
        f.write("# ")


def output_solution_file(out_dir: str, page: BeautifulSoup) -> None:

    # create the solution.py file
    with open(os.path.join(out_dir, "solution.py"), "w", encoding="utf-8") as f:
        f.write("Solution Stub")


args = parseArgs()
page = load_page(args.url)
meta_data = parse_meta_data(page)
# path = make_dir(args.out_dir, problem_meta_data["number"], problem_meta_data["name"])
# output_write_up_file(path)
# output_meta_file(path, problem_meta_data)
# output_problem_file(path, problem)
# output_solution_file(path, solution)
