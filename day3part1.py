import json

import pandas as pd
import numpy as np

data_list = open("day3part1.txt").read().split("\n")
new_list = []
for i in range(len(data_list)):
    row = [int(a) for a in data_list[i]]
    new_list.append(row)

filtered_list = list(filter(lambda item: len(item) > 0, new_list))
column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

df = pd.DataFrame(np.array(filtered_list), columns=column_names)

gamma = []
epsilon = []

for col in df.columns:
    a = df[col].value_counts()
    b = json.loads(a.to_json())
    if b['1'] > b['0']:
        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0')
        epsilon.append('1')

gamma = "".join(gamma)
epsilon = "".join(epsilon)

bit_gamma = int(gamma, 2)
bit_beta = int(epsilon, 2)
print(bit_gamma, bit_beta, bit_beta * bit_gamma)
