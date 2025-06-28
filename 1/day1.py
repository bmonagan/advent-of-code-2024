# pair up smallest number in the left list with the smallest number in the right list
#trying to find total distance between the two lists

import heapq

left_col = []
right_col = []

with open('1/day_1_input.txt', 'r') as file:
    for line in file:
        line = line.split()
        left = int(line[0])
        right = int(line[1])
        left_col.append(left)
        right_col.append(right)


def heap_strat(left_col: list,right_col: list) -> int:
    heapq.heapify(right_col)
    heapq.heapify(left_col)


    answer = 0
    while left_col and right_col:
        left = heapq.heappop(left_col)
        right = heapq.heappop(right_col)

        difference = abs(right-left)
        answer += difference


    print(answer)
def sort_scan(left_col: list,right_col: list) -> int:
    lc = sorted(left_col)
    rc = sorted(right_col)
 
    answer = 0
    for i in range(len(lc)):
        difference = abs(lc[i] - rc[i])
        
        answer += difference

    
    print(answer)
sort_scan(left_col,right_col)
heap_strat(left_col,right_col)

