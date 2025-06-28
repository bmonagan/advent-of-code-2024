with open('1/day_1_input.txt', 'r') as file:
    for line in file:
        line = line.split()
        left = line[0]
        right = line[1]
        print(left,right)
