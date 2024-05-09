import re





with open('./test.txt', 'r') as file:
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

    # Task 2
    gears = re.finditer(r'\*', line)
    for gear in gears:
        nbrs = nbrSymbolsAroundString(i, 0, len(line), r'\d+')
        gearNbrs = []
        for nbr in nbrs:
            # print(f'number: {nbr}')
            for i in range(gear.start()-1, gear.end()+1):
                # print(f'i: {i}')
                # print(f'span: {nbr.span()}')
                if i in range(*nbr.span()):
                    gearNbrs.append(int(nbr.group()))
                    # print('break!')
                    break
        if len(gearNbrs) >= 2:
            gearRatioSum += int(gearNbrs[0]) * int(gearNbrs[1])

print(f'Sum of valid numbers: {sum}')
print(f'Sum of gear ratios: {gearRatioSum}')





# # Task 2

# def isValidGear(lineNbr, start):
#     if lineNbr == 0:
#         inputRange = input[:2]
#     elif lineNbr == len(input)-1:
#         inputRange = input[-2:]
#     else:
#         inputRange = input[lineNbr-1:lineNbr+2]

#     adjacentNbrs = 0
#     gearRatio = 1
#     for line in inputRange:
#         line = line[:-2] # Kanske onödig rad...
#         if start == 0: start = 1
#         m = re.search(r'\d', line[start-1:start+2])
#         if m: 
#             adjacentNbrs +=1
#             gearRatio *= int(m.group())
#     if adjacentNbrs == 2:
#         return gearRatio
#     else:
#         return 0


# gearSum = 0
# for i, line in enumerate(input):
#     gears = re.finditer(r'\*', line)
#     for gear in gears:
#         gearRatioSum = isValidGear(i, gear.start())
#         if gearRatioSum != 0:
#             gearSum += gearRatioSum

# print(f'Total gear ratio sum: {gearSum}') # DEL 2 funkar ej än