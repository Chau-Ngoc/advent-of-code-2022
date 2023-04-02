import re

from utils import extract_text_lines_from_file


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def move_point_left(point: Point):
    point.x -= 1


def move_point_right(point: Point):
    point.x += 1


def move_point_up(point: Point):
    point.y += 1


def move_point_down(point: Point):
    point.y -= 1


def get_move_and_value(line, line_pattern):
    match = line_pattern.fullmatch(line)
    return match["move"], match["value"]


def is_adjacent_or_overlap(head_point: Point, tail_point: Point):
    if head_point.x == tail_point.x and head_point.y == tail_point.y:
        return True
    elif (
        abs(head_point.x - tail_point.x) == 1
        and abs(head_point.y - tail_point.y) == 1
    ):
        return True
    elif (
        abs(head_point.x - tail_point.x) == 1
        and abs(head_point.y - tail_point.y) == 0
    ):
        return True
    elif (
        abs(head_point.y - tail_point.y) == 1
        and abs(head_point.x - tail_point.x) == 0
    ):
        return True
    else:
        return False


input_content = map(str.strip, extract_text_lines_from_file("input.txt"))

moves = {
    "L": move_point_left,
    "R": move_point_right,
    "U": move_point_up,
    "D": move_point_down,
}
pattern = re.compile(r"(?P<move>[A-Z]) (?P<value>\d+)")

head = Point(0, 0)
tail = Point(0, 0)

tail_visited_positions = {(0, 0)}

for input_line in input_content:
    move, value = get_move_and_value(input_line, pattern)

    for step in range(int(value)):
        prev_head_x = head.x
        prev_head_y = head.y

        moves[move](head)

        if not is_adjacent_or_overlap(head, tail):
            tail.x = prev_head_x
            tail.y = prev_head_y

            tail_visited_positions.add((tail.x, tail.y))

print(len(tail_visited_positions))
