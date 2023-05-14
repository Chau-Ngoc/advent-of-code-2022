from pathlib import Path

from utils import extract_text_lines_from_file

input_file = Path(__file__).parent / "input.txt"
input_content = extract_text_lines_from_file(input_file)
input_content = map(str.strip, input_content)

combinations = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

my_score = 0
for combination in input_content:
    my_score += combinations[combination]

print(my_score)
