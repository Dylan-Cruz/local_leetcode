import json
from typing import Dict
import os


class Writer:
    def __init__(self, out_dir: str, page_data: Dict):
        self.out_dir = out_dir
        self.page_data = page_data

    def __make_project_dir(self) -> str:
        problem_number = self.page_data["number"]
        problem_name = self.page_data["name"]
        
        dir_name = problem_number.ljust(4, '0') + "_" + problem_name.lower().replace(" ", "_")
        new_path = os.path.join(self.out_dir, dir_name)
        os.mkdir(new_path)
        return new_path

    def __output_write_up_file(self):
        with open(
            os.path.join(self.out_dir, "write_up.md"), "w", encoding="utf-8"
        ) as f:
            f.write("# Write Up\n\n")
            f.write("## Approach\n\n")
            f.write("## Time Complexity\n\n")
            f.write("## Space Complexity\n")

    def __output_meta_file(self) -> None:
        with open(os.path.join(self.out_dir, "meta.json"), "w", encoding="utf-8") as f:
            json.dump(self.page_data, f, indent=4)

    def __output_problem_file(self) -> None:
        with open(os.path.join(self.out_dir, "problem.md"), "w", encoding="utf-8") as f:
            f.write(f"# {self.page_data['number']} {self.page_data['name']}\n\n")
            f.write(self.page_data["description_markdown"])

    def __output_solution_file(self) -> None:
        with open(
            os.path.join(self.out_dir, "solution.py"), "w", encoding="utf-8"
        ) as f:
            f.write(self.page_data["solution_stub"])

    def write(self):
        self.out_dir = self.__make_project_dir()
        self.__output_write_up_file()
        self.__output_meta_file()
        self.__output_problem_file()
        self.__output_solution_file()
