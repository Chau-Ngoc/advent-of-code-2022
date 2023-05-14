from pathlib import Path

from common import Point, get_move_and_value, is_adjacent_or_overlap, pattern

from utils import extract_text_lines_from_file

input_file = Path(__file__).parent / "input.txt"
input_content = map(str.strip, extract_text_lines_from_file(input_file))

head = Point(0, 0)
tail = Point(0, 0)

tail_visited_positions = {(0, 0)}

for input_line in input_content:
    move, value = get_move_and_value(input_line, pattern)

    for step in range(int(value)):
        prev_head_x = head.x
        prev_head_y = head.y

        head.moves[move]()

        if not is_adjacent_or_overlap(head, tail):
            tail.x = prev_head_x
            tail.y = prev_head_y

            tail_visited_positions.add((tail.x, tail.y))

print(len(tail_visited_positions))
