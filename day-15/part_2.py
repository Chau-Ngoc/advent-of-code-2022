from common import calculate_tuning_frequency, sensors

low_bound = 0
high_bound = 4_000_000

for row in range(0, high_bound + 1):
    coverage_ranges = []
    for sensor in sensors:
        if sensor.distance_to_closest_beacon >= abs(row - sensor.y):
            start, stop = sensor.calculate_coverage_range_along_row(row=row)
            coverage_ranges.append((start, stop))

    coverage_ranges.sort()

    q = []
    for index, (lo, hi) in enumerate(coverage_ranges):
        if len(q) == 0:
            lo = max(low_bound, lo)
            q.append([lo, hi])
            continue

        if lo <= q[-1][1] + 1:
            q[-1][1] = max(hi, q[-1][1])
        elif lo > q[-1][1] + 1:
            q.append([lo, hi])

        if q[-1][1] > high_bound:
            q[-1][1] = high_bound
            break

    if len(q) == 2:
        print(calculate_tuning_frequency(q[0][1] + 1, row))
        exit(0)
