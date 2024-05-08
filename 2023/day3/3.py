import re





with open('./test.txt', 'r') as file:
    input = file.readlines()

def isValidNumber(lineNbr, start, end):
    if lineNbr == 0:
        inputRange = input[:2]
    elif lineNbr == len(input)-1:
        inputRange = input[-2:]
    else:
        inputRange = input[lineNbr-1:lineNbr+2]
    for line in inputRange:
        line = line[:-2] # Kanske onödig rad...
        if start == 0: start = 1
        m = re.search(r'[^\d|.|\s]', line[start-1:end+1])
        if m: 
            return True
    return False


sum = 0
for i, line in enumerate(input):
    nbrs = re.finditer(r'\d+', line)
    for nbr in nbrs:
        if isValidNumber(i, nbr.start(), nbr.end()): 
            sum += int(nbr.group())


print(f'Sum of valid numbers: {sum}')

# Task 2

def isValidGear(lineNbr, start):
    if lineNbr == 0:
        inputRange = input[:2]
    elif lineNbr == len(input)-1:
        inputRange = input[-2:]
    else:
        inputRange = input[lineNbr-1:lineNbr+2]

    adjacentNbrs = 0
    gearRatio = 1
    for line in inputRange:
        line = line[:-2] # Kanske onödig rad...
        if start == 0: start = 1
        m = re.search(r'\d', line[start-1:start+2])
        if m: 
            adjacentNbrs +=1
            gearRatio *= int(m.group())
    if adjacentNbrs == 2:
        return gearRatio
    else:
        return 0


gearSum = 0
for i, line in enumerate(input):
    gears = re.finditer(r'\*', line)
    for gear in gears:
        gearRatio = isValidGear(i, gear.start())
        if gearRatio != 0:
            gearSum += gearRatio

print(f'Total gear ratio sum: {gearSum}') # DEL 2 funkar ej än