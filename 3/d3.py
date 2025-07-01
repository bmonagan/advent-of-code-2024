import os
import re 



data = ""
with open('3/d3_input.txt', 'r') as file:
    for line in file:
        data += line

mem_clean = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
### TRIED IT THIS WAY BUT GOT A LOWER NUMBER THAT DID NOT CORRECTLY GET ALL THE DATA    
# need to find data that is in the correct format
# correct format would be mul(int,int)
# correct_sequences = []

# parts_raw = data.split("mul(")
# print(parts_raw)

# for section in parts_raw:
#     i = 0
#     if not section[i].isdigit():
#         continue
#     while section[i].isdigit():
#         i += 1
#     if section[i] != ",":
#         continue
#     else:
#         i += 1
#     if not section[i].isdigit():
#         continue
    
#     while section[i].isdigit():
#         i += 1
    

#     if section[i] == ")" and i == len(section) - 1:
#         correct_sequences.append(section[:len(section)-1 ])
#     else:
#         continue
print(mem_clean)
summ = 0
for x,y in mem_clean:
    multi = int(x) * int(y)
    summ += multi

print(summ)

    
        