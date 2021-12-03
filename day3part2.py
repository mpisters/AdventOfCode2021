import json

import pandas as pd
import numpy as np

data_list = open("day3part2.txt").read().split("\n")
new_list = []
for i in range(len(data_list)):
    row = [int(a) for a in data_list[i]]
    new_list.append(row)

filtered_list = list(filter(lambda item: len(item) > 0, new_list))
column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

df = pd.DataFrame(np.array(filtered_list), columns=column_names)
oxygen_df = df.copy()
scrubber_df = df.copy()
for col in df.columns:
    total_count = oxygen_df[col].value_counts()
    index = oxygen_df.index
    number_of_rows = len(index)
    if number_of_rows == 1:
        break
    b = json.loads(total_count.to_json())
    if '0' not in b or ('1' in b and b['1'] >= b['0']):
        is_one = oxygen_df[col] == 1
        oxygen_df = oxygen_df[is_one]
    else:
        is_zero = oxygen_df[col] == 0
        oxygen_df = oxygen_df[is_zero]

oxygen_row = oxygen_df.values[0]
oxygen_list = oxygen_row.tolist()
oxygen_list = [str(item) for item in oxygen_list]
oxygen_string = "".join(oxygen_list)
oxygen_number = int(oxygen_string, 2)

scrubber_df = df.copy()

for col in df.columns:
    total_count = scrubber_df[col].value_counts()
    index = scrubber_df.index
    number_of_rows = len(index)
    if number_of_rows <= 1:
        break
    b = json.loads(total_count.to_json())
    if '1' not in b or ('0' in b and b['1'] < b['0']):
        is_one = scrubber_df[col] == 1
        all_true = list(filter(lambda item: item is True, is_one.tolist()))
        if len(all_true) == 0:
            continue
        scrubber_df = scrubber_df[is_one]
    else:
        is_zero = scrubber_df[col] == 0
        all_true = list(filter(lambda item: item is True, is_zero.tolist()))
        if len(all_true) == 0:
            continue
        scrubber_df = scrubber_df[is_zero]

scrubber_row = scrubber_df.values[0]
scrubber_list = scrubber_row.tolist()
scrubber_list = [str(item) for item in scrubber_list]
scrubber_string = "".join(scrubber_list)
scrubber_number = int(scrubber_string, 2)

print(oxygen_number, scrubber_number, oxygen_number * scrubber_number)
