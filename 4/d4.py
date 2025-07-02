from collections import deque
data = []
with open('4/d4_input.txt', 'r') as file:
    for line in file:
        data.append(list(line))

n = len(data)
m = len(data[0])


# add x indices to stack
# pop and check for m in diaganol range around
# have while q include if its XMAS
q = deque()

directions = [
    (-1,  0), # up
    ( 1,  0), # down
    ( 0, -1), # left
    ( 0,  1), # right
    (-1, -1), # up-left
    (-1,  1), # up-right
    ( 1, -1), # down-left
    ( 1,  1)  # down-right
]
chain = ["X", "M", "A", "S"]
xmases = 0

for i in range(n):
    for j in range(m):
        if data[i][j] == "X":
            for dr, dc in directions:
                ni, nj = i, j
                found = True
                for k in range(1, 4):  # Already at "X", check next 3 letters
                    ni += dr
                    nj += dc
                    if 0 <= ni < n and 0 <= nj < m and data[ni][nj] == chain[k]:
                        continue
                    else:
                        found = False
                        break
                if found:
                    xmases += 1

print(xmases)







