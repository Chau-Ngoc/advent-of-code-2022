from common import coords_ranges, floor, units_rest

is_blocked = False
su_x = 500
su_y = 0
while not is_blocked:
    if (su_x, su_y + 1) in coords_ranges or su_y + 1 == floor:
        if (su_x - 1, su_y + 1) in coords_ranges or su_y + 1 == floor:
            if (su_x + 1, su_y + 1) in coords_ranges or su_y + 1 == floor:
                coords_ranges.add((su_x, su_y))
                units_rest += 1
                su_x = 500
                su_y = 0
                if (su_x, su_y) in coords_ranges:
                    is_blocked = True
                continue
            else:
                su_x += 1
        else:
            su_x -= 1

    su_y += 1

print(units_rest)
