import numpy as np
import pandas as pd

from utils import extract_text_lines_from_file, str_to_nan

input_content = extract_text_lines_from_file("input.txt")
input_content = list(map(lambda x: x.strip(), input_content))


calories = map(str_to_nan, input_content)

cal_groups = []
current_cal = 0
for cal in calories:
    if cal not in [np.nan]:
        current_cal += cal
    else:
        cal_groups.append(current_cal)
        current_cal = 0

cal_groups_array = np.array(cal_groups)
df = pd.DataFrame(cal_groups_array)

top_3_df = df.sort_values(by=0, ascending=False).head(3)
top_3_cal = top_3_df.aggregate("sum")

print(top_3_cal)
