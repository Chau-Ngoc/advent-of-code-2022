import re

from utils import extract_text_lines_from_file

input_content = extract_text_lines_from_file("input.txt")
input_content = map(str.strip, input_content)

pattern = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

overlaps = 0

for line in input_content:
    match = pattern.match(line)
    (a1, b1, a2, b2) = tuple(map(int, match.groups()))

    if a2 <= a1 <= b2 or a2 <= b1 <= b2 or a1 <= a2 <= b1 or a1 <= b2 <= b1:
        overlaps += 1

print(overlaps)
