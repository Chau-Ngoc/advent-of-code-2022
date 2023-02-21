import json
import re
from functools import reduce

from utils import extract_text_lines_from_file

TOTAL_SPACE = 70_000_000
REQUIRED_UNUSED_SPACE = 30_000_000


class Directory:
    def __init__(self, directory_name):
        self.name = directory_name
        self.size = 0

    def __repr__(self):
        return json.dumps({"name": self.name, "size": self.size})

    def cum_sum(self, size):
        self.size += size


input_content = map(str.strip, extract_text_lines_from_file("input.txt"))

cd_pattern = re.compile(r"\$ cd ([\w/.]+)")
file_pattern = re.compile(r"(\d+) [\w.]+")

directories = {}

cwd = "/"
directory = Directory(cwd)
directories[cwd] = directory

for line in input_content:
    if match := cd_pattern.match(line):
        dir_name = match.group(1)

        match dir_name:
            case "/":
                continue
            case "..":
                cwd = cwd[: cwd.rfind("/")]

                if cwd == "/":
                    dir_name = cwd
            case _:
                cwd += f"/{dir_name}"

        if directories.get(cwd) is not None:
            prev_directory = directory
            directory = directories[cwd]
            directory.cum_sum(prev_directory.size)
        else:
            directory = Directory(dir_name)
            directories[cwd] = directory

    elif match := file_pattern.match(line):
        file_size = float(match.group(1))
        directory.cum_sum(file_size)

sizes = []
for _, directory in directories.items():
    sizes.append(directory.size)

sizes_under_100k = filter(lambda x: x <= 100_000, sizes)
sum_under_100k = reduce(lambda x1, x2: x1 + x2, sizes_under_100k)

used_space = max(*sizes)
required_available_space = REQUIRED_UNUSED_SPACE - (TOTAL_SPACE - used_space)

sizes_to_delete = filter(lambda x: x >= required_available_space, sizes)
size_to_delete = min(*sizes_to_delete)

print(size_to_delete)
