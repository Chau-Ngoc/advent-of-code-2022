from collections import deque
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

q = deque()
q.append((0, start_row_idx, start_col_idx))

vis = {(start_row_idx, start_col_idx)}

while q:
    distance_from_start: int
    row_idx: int
    col_idx: int
    distance_from_start, row_idx, col_idx = q.popleft()
    for neighbor_row_idx, neighbor_col_idx in [
        (row_idx + 1, col_idx),
        (row_idx - 1, col_idx),
        (row_idx, col_idx + 1),
        (row_idx, col_idx - 1),
    ]:
        if (
            neighbor_row_idx < 0
            or neighbor_col_idx < 0
            or neighbor_row_idx >= len(grid)
            or neighbor_col_idx >= len(grid[0])
        ):
            continue
        elif (neighbor_row_idx, neighbor_col_idx) in vis:
            continue
        elif (
            ord(grid[neighbor_row_idx][neighbor_col_idx])
            - ord(grid[row_idx][col_idx])
            > 1
        ):
            continue
        elif (
            neighbor_row_idx == end_row_idx and neighbor_col_idx == end_col_idx
        ):
            print(distance_from_start + 1)
            exit(0)
        vis.add((neighbor_row_idx, neighbor_col_idx))
        q.append((distance_from_start + 1, neighbor_row_idx, neighbor_col_idx))
