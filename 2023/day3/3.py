import re

with open('./input3.txt', 'r') as file:
    input = file.readlines()


def nbrSymbolsAroundString(lineNbr, start, end, sym):
    # Special case for first and last line
    if lineNbr == 0:
        inputRange = input[:2]
    elif lineNbr == len(input)-1:
        inputRange = input[-2:]
    else:
        inputRange = input[lineNbr-1:lineNbr+2]

    nbrSym = []
    for line in inputRange:
        if start == 0: start = 1 #To not loop to last idx
        m = re.finditer(sym, line[start-1:end+1])
        nbrSym += m
    return nbrSym

sum = 0
gearRatioSum = 0
for i, line in enumerate(input):
    # Task 1
    nbrs = re.finditer(r'\d+', line)
    for nbr in nbrs:
        if len(nbrSymbolsAroundString(i, nbr.start(), nbr.end(), r'[^\d|.|\s]')) > 0:
            sum += int(nbr.group())

print(f'Sum of valid numbers: {sum}')

# Task 2

with open('input3.txt', 'r') as file:
    input = file.readlines()

gear_sum = 0
for i, line in enumerate(input):
    gears = re.finditer(r'\*', line)
    for gear in gears:
        if i == 0:
            inputRange = input[:2]
        elif i == len(input)-1:
            inputRange = input[-2:]
        else:
            inputRange = input[i-1:i+2]
        valid_nbrs = []
        for nbrs_list in inputRange:
            nbrs = re.finditer(r'\d+', nbrs_list)
            for nbr in nbrs:
                if gear.start() in range(nbr.start() - 1, nbr.end()+1):
                    valid_nbrs.append(int(nbr.group()))
        if len(valid_nbrs) == 2:
            gear_sum += valid_nbrs[0] * valid_nbrs[1]

print(f'Gear ratio sum: {gear_sum}')

        