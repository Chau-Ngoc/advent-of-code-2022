from pathlib import Path

from common import compare

input_file = Path(__file__).parent.resolve() / "input.txt"
with open(input_file) as file:
    input_content = list(map(eval, file.read().split()))

two = [[2]]
six = [[6]]
two_index = 1
six_index = 2

for line in input_content:
    if compare(two, line) > 0:
        two_index += 1
        six_index += 1
    elif compare(six, line) > 0:
        six_index += 1

print(two_index * six_index)
