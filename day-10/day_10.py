import re
from pathlib import Path

from utils import extract_text_lines_from_file

input_file = Path(__file__).parent / "input.txt"

input_content = map(str.strip, extract_text_lines_from_file(input_file))
pattern = re.compile(r"addx (?P<value>[-\d]+)")

desired_cycles = [20, 60, 100, 140, 180, 220]
jobs = {
    "noop": 1,
    "addx": 2,
}

statuses = ["#", " "]
pixels = ""
count = 0

cycle = 0
x_register = 1

result = 0

for index, line in enumerate(input_content):
    number_of_cycles = jobs[line[:4]]

    is_noop = True
    for i in range(number_of_cycles):
        count += 1
        prev_x_register = x_register

        if line.startswith("noop"):
            cycle += 1
        elif line.startswith("addx"):
            if is_noop:
                is_noop = False
                cycle += 1
            else:
                match = pattern.match(line)
                x_register += int(match["value"])
                cycle += 1

        signal_strength = prev_x_register * cycle

        if cycle in desired_cycles:
            result += signal_strength

        sprite = [prev_x_register - 1, prev_x_register, prev_x_register + 1]
        if (cycle - 1) % 40 in sprite:
            pixels += statuses[0]
        else:
            pixels += statuses[1]

        if count == 40:
            count = 0
            pixels += "\n"

print(result)
print(pixels)
