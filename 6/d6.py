map = []
with open("6/d6_input.txt","r") as file:
    for line in file:
        line = line[0:-1]
        map.append(line)


starting_point = None
direction = None

n = len(map)
m = len(map[0])
directions = {
    "<":"Left",
    ">":"Right",
    "^": "Up",
    "V": "Down"}
for i in range(n):
    for j in range(m):
        if map[i][j] in directions:
            starting_point = [i,j]
            direction = directions[map[i][j]]


x_count = 0



