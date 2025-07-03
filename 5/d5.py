from collections import defaultdict


with open('5/d5_input.txt','r') as input:
    pairs = defaultdict(list)
    data = []

    fl = input.readline()
    x = fl.split("|")

    for line in input:
        line = line.strip()
        if "|" in line:
            split_line = line.split('|')
            pairs[split_line[1].strip()].append(split_line[0].strip())
        else:
            data_split = [item.strip() for item in line.split(",") if item.strip()]
            if data_split:
                data.append(data_split)



good_pair_sum = 0
good_count = 0
total_count = 0

for page_list in data:
    Good = True
    total_count += 1 
    for idx,page in enumerate(page_list):
        
        for requirement in pairs[page]:
            if requirement in page_list[idx:]:
                Good = False
    if Good:
        good_count += 1 
        mid = len(page_list) // 2
        good_pair_sum += int(page_list[mid])


print(good_pair_sum)