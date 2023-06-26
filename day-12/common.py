from pathlib import Path

from utils import extract_text_lines_from_file

input_file = Path(__file__).parent / "input.txt"
input_content = list(extract_text_lines_from_file(input_file))

grid = [list(x.strip()) for x in input_content]

start_row_idx = start_col_idx = end_row_idx = end_col_idx = 0
for row_index, row in enumerate(grid):
    for col_index, item in enumerate(row):
        if item == "S":
            start_row_idx = row_index
            start_col_idx = col_index
            grid[row_index][col_index] = "a"
        if item == "E":
            end_row_idx = row_index
            end_col_idx = col_index
            grid[row_index][col_index] = "z"
