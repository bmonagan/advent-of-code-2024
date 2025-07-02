from collections import defaultdict
data = []
with open('4/d4_input.txt', 'r') as file:
    for line in file:
        data.append(list(line))

n = len(data)
m = len(data[0])


# M.S
# .A.
# M.S
xmases = 0

for i in range(1, n-1):
    for j in range(1, m-1):
        if data[i][j] == "A":
            # Diagonal 1: top-left to bottom-right
            diag1 = data[i-1][j-1] + data[i][j] + data[i+1][j+1]
            # Diagonal 2: top-right to bottom-left
            diag2 = data[i-1][j+1] + data[i][j] + data[i+1][j-1]
            valid1 = diag1 == "MAS" or diag1 == "SAM"
            valid2 = diag2 == "MAS" or diag2 == "SAM"
            if valid1 and valid2:
                xmases += 1

print(xmases)