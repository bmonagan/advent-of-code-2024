# So, a report only counts as safe if both of the following are true:
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

safe = 0
data = []

with open('2/d2_input.txt', 'r') as file:
    for line in file:
        line = line.split()
        intline = []
        for number in line:
            xnumber = int(number)
            intline.append(xnumber)

        data.append(intline)
        


        

safe = 0
for row in data:
    if row[0] == row[1]:
        continue
    if row[0] < row[1]:
        direction = 1 # 1 is increasing
    elif row[0] > row[1]:
        direction = 0 # 0 is decreasing

    for i in range(1,len(row)):
        upper = row[i]
        lower = row[i-1]

        if 1 > abs(upper-lower) or 3 < abs(upper-lower):
            break
        if direction == 1:
            if upper <= lower:
                break
        elif direction == 0:
            if upper >= lower:
                break
        
        if i == len(row) - 1:
            safe += 1 
    


print(safe)