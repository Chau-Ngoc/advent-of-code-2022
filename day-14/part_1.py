from common import coords_ranges, max_y, units_rest

to_void = False
su_x = 500
su_y = 0
while not to_void:
    if (su_x, su_y + 1) in coords_ranges:
        if (su_x - 1, su_y + 1) in coords_ranges:
            if (su_x + 1, su_y + 1) in coords_ranges:
                coords_ranges.add((su_x, su_y))
                units_rest += 1
                su_x = 500
                su_y = 0
                continue
            else:
                su_x += 1
        else:
            su_x -= 1

    su_y += 1

    if su_y >= max_y:
        to_void = True

print(units_rest)
