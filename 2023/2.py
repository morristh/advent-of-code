import csv

# Really ugly implementation
# Task 1
max_red = 12
max_green = 13
max_blue = 14

sum = 0
with open('2023/2.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for gameNbr, game in enumerate(reader):
        valid = True
        for i, set in enumerate(game):
            if i == 0:
                set = set[7:]
            nbr_cubes = ''
            nbr = 0
            for j, c in enumerate(set):
                if ord(c) >= ord('0') and ord(c) <= ord('9'):
                    nbr_cubes += c
                elif len(nbr_cubes) > 0:
                    nbr = int(nbr_cubes)
                if len(set[j:]) >= 3:
                    if set[j:j+3] == 'red' and nbr > max_red:
                        valid = False
                    elif set[j:j+5] == 'green' and nbr > max_green:
                        valid = False
                    elif set[j:j+4] == 'blue' and nbr > max_blue:
                        valid = False
                if c == ';':
                    nbr_cubes = ''
                    nbr = 0
        if valid: 
            sum += (gameNbr + 1)
        
print(f'Sum of valid IDs: {sum}')

# Task 2
sum = 0
with open('2023/2.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for gameNbr, game in enumerate(reader):
        min_red = 0
        min_green = 0
        min_blue = 0
        for i, set in enumerate(game):
            if i == 0:
                set = set[7:]
            nbr_cubes = ''
            nbr = 0
            for j, c in enumerate(set):
                if ord(c) >= ord('0') and ord(c) <= ord('9'):
                    nbr_cubes += c
                elif len(nbr_cubes) > 0:
                    nbr = int(nbr_cubes)
                if len(set[j:]) >= 3:
                    if set[j:j+3] == 'red' and nbr > min_red:
                        min_red = nbr
                    elif set[j:j+5] == 'green' and nbr > min_green:
                        min_green = nbr
                    elif set[j:j+4] == 'blue' and nbr > min_blue:
                        min_blue = nbr
                if c == ';':
                    nbr_cubes = ''
                    nbr = 0
        print(f' {min_red}   {min_green}   {min_blue}')
        sum += min_red * min_green * min_blue
        
print(f'Sum of power of IDs: {sum}')
