import re
from pathlib import Path

import numpy as np

from utils import extract_text_lines_from_file


def coords_to_ranges(coords):
    ranges = set()
    for index, (x, y) in enumerate(coords):
        try:
            nxt_x, nxt_y = coords[index + 1]
        except IndexError:
            ranges.update({(int(x), int(y))})
            break

        if y == nxt_y:
            start = int(x)
            stop = int(nxt_x)
            _range = {
                (x, int(y))
                for x in range(
                    start, stop, int((stop - start) / abs(stop - start))
                )
            }
        else:
            start = int(y)
            stop = int(nxt_y)
            _range = {
                (int(x), y)
                for y in range(
                    start, stop, int((stop - start) / abs(stop - start))
                )
            }

        ranges.update(_range)

    return ranges


input_file = Path(__file__).parent / "input.txt"
input_content = list(map(str.strip, extract_text_lines_from_file(input_file)))

input_array = np.array(input_content)
uniques = np.unique(input_array).tolist()

pattern = re.compile(r"(\d+),(\d+)")
max_y = 0
coords_ranges = set()
for i in range(len(uniques)):
    coords = pattern.findall(uniques[i])
    ranges = coords_to_ranges(coords)
    coords_ranges.update(ranges)

    for _, y in coords:
        if int(y) > max_y:
            max_y = int(y)

units_rest = 0
floor = max_y + 2
