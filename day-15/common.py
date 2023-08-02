import itertools
import re
from pathlib import Path

from utils import extract_text_lines_from_file


class Sensor:
    def __init__(self, x, y, closest_beacon: "Beacon"):
        self.x = x
        self.y = y
        self.closest_beacon = closest_beacon

        self.distance_to_closest_beacon = (
            self._calculate_distance_to_closest_beacon()
        )

    def _calculate_distance_to_closest_beacon(self):
        return abs(self.closest_beacon.x - self.x) + abs(
            self.closest_beacon.y - self.y
        )

    def calculate_coverage_range_along_row(self, row=2_000_000):
        dy = abs(self.y - row)
        dx = abs(self.distance_to_closest_beacon - dy)
        return self.x - dx, self.x + dx

    def __repr__(self):
        return (
            f"({self.x}, {self.y}): closest beacon is at"
            f" ({self.closest_beacon.x}, {self.closest_beacon.y})"
        )


class Beacon:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def eliminate_overlap_ranges(ranges: list) -> set:
    chain = itertools.chain(*ranges)
    return set(chain)


def calculate_tuning_frequency(x: int, y: int) -> int:
    return x * 4000000 + y


input_file = Path(__file__).parent / "input.txt"
input_content = map(str.strip, extract_text_lines_from_file(input_file))
pattern = re.compile(
    r"Sensor at x=(?P<sens_x>-?\d+), y=(?P<sens_y>-?\d+): closest beacon is at"
    r" x=(?P<bea_x>-?\d+), y=(?P<bea_y>-?\d+)"
)
referenced_row = 2_000_000

sensors = []
for line in input_content:
    match = pattern.match(line)
    sens_x, sens_y, bea_x, bea_y = map(int, match.groups())
    beacon = Beacon(bea_x, bea_y)
    sensor = Sensor(sens_x, sens_y, beacon)

    sensors.append(sensor)
