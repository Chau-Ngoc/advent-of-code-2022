from common import eliminate_overlap_ranges, referenced_row, sensors

coverage_ranges = []
for sensor in sensors:
    if sensor.distance_to_closest_beacon >= abs(referenced_row - sensor.y):
        start, stop = sensor.calculate_coverage_range_along_row(
            row=referenced_row
        )
        coverage_ranges.append(range(start, stop + 1))

ranges = eliminate_overlap_ranges(coverage_ranges)
print(len(ranges) - 1)
