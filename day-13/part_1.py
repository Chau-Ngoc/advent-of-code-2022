from pathlib import Path

from common import compare, eval_str

from utils import extract_text_lines_from_file

input_file = Path(__file__).parent.resolve() / "input.txt"
input_content = list(map(eval_str, extract_text_lines_from_file(input_file)))

sum_of_indices = 0

for i in range(0, len(input_content), 3):
    first = input_content[i]
    second = input_content[i + 1]

    result = compare(first, second)

    if result < 0:
        sum_of_indices += (i + 3) // 3

print(sum_of_indices)
