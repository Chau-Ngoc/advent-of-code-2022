from pathlib import Path

from common import Point, get_move_and_value, is_adjacent_or_overlap, pattern

from utils import extract_text_lines_from_file

input_file = Path(__file__).parent / "input.txt"
input_content = map(str.strip, extract_text_lines_from_file(input_file))

knots = [Point(0, 0) for i in range(10)]
head = knots[0]

tail_visited_positions = {(0, 0)}

for line in input_content:
    move, value = get_move_and_value(line, pattern)

    for step in range(int(value)):
        head.moves[move]()

        for i in range(1, 10):
            current_knot = knots[i]
            prev_knot = knots[i - 1]

            if not is_adjacent_or_overlap(current_knot, prev_knot):
                current_knot.follow(prev_knot)

                tail = knots[-1]
                tail_visited_positions.add((tail.x, tail.y))

print(len(tail_visited_positions))
