from pathlib import Path

from utils import extract_text_lines_from_file

input_file = Path(__file__).parent / "input.txt"
input_content = extract_text_lines_from_file(input_file)
input_content = map(str.strip, input_content)

combinations = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

my_score = 0
for combination in input_content:
    my_score += combinations[combination]

print(my_score)
