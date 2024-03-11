from typing import Dict
import os


class Writer:
    def __init__(self, out_dir: str, page_data: Dict):
        self.out_dir = out_dir
        self.page_data = page_data

    def __make_project_dir(self) -> str:
        if os.path.exists(self.out_dir):
            problem_number = self.page_data["number"]
            problem_name = self.page_data["name"]
            dir_name = problem_number + "_" + problem_name.lower().replace(" ", "_")
            new_path = os.path.join(self.out_dir, dir_name)
            os.mkdir(new_path)
            return new_path

        raise FileNotFoundError(f"The directory {self.out_dir} does not exist.")

    def __output_write_up_file(self):
        pass

    def write(self):
        self.__make_project_dir()
