import heapq
from collections import defaultdict

left_col = []
right_col = defaultdict(int)

with open('1/day_1_input.txt', 'r') as file:
    for line in file:
        line = line.split()
        left = int(line[0])
        right = int(line[1])
        left_col.append(left)
        right_col[right] += 1



answer = 0

for n in left_col:
    multi = right_col[n]
    similarity_mutliple = n * multi
    answer += similarity_mutliple



print(answer)