import re
from pathlib import Path

from utils import extract_text_lines_from_file

pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")

input_file = Path(__file__).parent / "input.txt"
input_content = extract_text_lines_from_file(input_file)
input_content = map(str.strip, input_content)

stack_1 = ["N", "B", "D", "T", "V", "G", "Z", "J"]
stack_2 = ["S", "R", "M", "D", "W", "P", "F"]
stack_3 = ["V", "C", "R", "S", "Z"]
stack_4 = ["R", "T", "J", "Z", "P", "H", "G"]
stack_5 = ["T", "C", "J", "N", "D", "Z", "Q", "F"]
stack_6 = ["N", "V", "P", "W", "G", "S", "F", "M"]
stack_7 = ["G", "C", "V", "B", "P", "Q"]
stack_8 = ["Z", "B", "P", "N"]
stack_9 = ["W", "P", "J"]

stacks = [
    stack_1,
    stack_2,
    stack_3,
    stack_4,
    stack_5,
    stack_6,
    stack_7,
    stack_8,
    stack_9,
]
