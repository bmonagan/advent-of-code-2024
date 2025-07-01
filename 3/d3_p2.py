import re 



mem = ""
with open('3/d3_input.txt', 'r') as file:
    for line in file:
        mem += line
sum_mul = 0
do_sum = True
for x in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', mem):
    match x[0]:
        case 'do()':
            do_sum = True
        case 'don\'t()':
            do_sum = False
        case _:
            if do_sum:
                sum_mul += int(x[1]) * int(x[2])

print(sum_mul)