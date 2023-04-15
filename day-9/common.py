import re


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moves = {
            "L": self.move_left,
            "R": self.move_right,
            "U": self.move_up,
            "D": self.move_down,
        }

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def follow(self, another_point: "Point"):
        dx = (
            0
            if another_point.x == self.x
            else (another_point.x - self.x) / abs(another_point.x - self.x)
        )
        dy = (
            0
            if another_point.y == self.y
            else (another_point.y - self.y) / abs(another_point.y - self.y)
        )
        self.x += dx
        self.y += dy


def get_move_and_value(line, line_pattern):
    match = line_pattern.fullmatch(line)
    return match["move"], match["value"]


def is_adjacent_or_overlap(first_point: Point, second_point: Point):
    if first_point.x == second_point.x and first_point.y == second_point.y:
        return True
    elif (
        abs(first_point.x - second_point.x) == 1
        and abs(first_point.y - second_point.y) == 1
    ):
        return True
    elif (
        abs(first_point.x - second_point.x) == 1
        and abs(first_point.y - second_point.y) == 0
    ):
        return True
    elif (
        abs(first_point.y - second_point.y) == 1
        and abs(first_point.x - second_point.x) == 0
    ):
        return True
    else:
        return False


pattern = re.compile(r"(?P<move>[A-Z]) (?P<value>\d+)")
