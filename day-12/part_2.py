from collections import deque

from common import end_col_idx, end_row_idx, grid

q = deque()
q.append((0, end_row_idx, end_col_idx))

vis = {(end_row_idx, end_col_idx)}

while q:
    distance_from_end: int
    row_idx: int
    col_idx: int
    distance_from_end, row_idx, col_idx = q.popleft()
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
            ord(grid[row_idx][col_idx])
            - ord(grid[neighbor_row_idx][neighbor_col_idx])
            > 1
        ):
            continue
        elif grid[neighbor_row_idx][neighbor_col_idx] == "a":
            print(distance_from_end + 1)
            exit(0)
        vis.add((neighbor_row_idx, neighbor_col_idx))
        q.append((distance_from_end + 1, neighbor_row_idx, neighbor_col_idx))
