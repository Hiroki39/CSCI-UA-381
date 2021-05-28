import os
import json

target_dir = '../../Datasets/babynames/'
txt_files = [f for f in os.listdir(target_dir) if f.endswith('.txt')]

name_dict = {}

for curr_file in txt_files:
    with open(target_dir + curr_file) as f:
        lines = f.read().splitlines()
    year = int(curr_file[3:7])
    decade_str = f"{(year - 1) // 10 * 10 + 1}-{((year - 1) // 10 + 1) * 10}"
    if decade_str not in name_dict:
        name_dict[decade_str] = {}
    for line in lines:
        name, gender, count = line.split(',')
        if name not in name_dict[decade_str]:
            name_dict[decade_str][name] = {'M': 0, 'F': 0}
        name_dict[decade_str][name][gender] += int(count)

with open("babynames.json", "w") as f:
    json.dump(name_dict, f)
