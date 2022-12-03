from utils import extract_text_lines_from_file, str_to_int

input_content = extract_text_lines_from_file("input.txt")
input_content = list(map(lambda x: x.strip(), input_content))


calories = map(str_to_int, input_content)

max_cal = 0
current_cal = 0
for cal in calories:
    if cal is not None:
        current_cal += cal
        continue

    if current_cal >= max_cal:
        max_cal = current_cal
        current_cal = 0
    else:
        current_cal = 0

print(max_cal)
