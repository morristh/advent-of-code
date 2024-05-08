import re

max_red = 12
max_green = 13
max_blue = 14
IDsum = 0
IDpowersum = 0
with open('2.txt', 'r') as input:
    for line in input:
        gameID = int(re.match(r'\s*Game\s(\d+)', line).group(1))
        reds = re.findall(r'(\d+)\sred', line)
        greens = re.findall(r'(\d+)\sgreen', line)
        blues = re.findall(r'(\d+)\sblue', line)
        max_reds = max(list(map(int, reds)))
        max_greens = max(list(map(int, greens)))
        max_blues = max(list(map(int, blues)))
        
        # Task 1
        if max_reds <= max_red and max_greens <= max_green and max_blues <= max_blue:
            IDsum += int(gameID)

        # Task 2
        IDpowersum += max_reds * max_greens * max_blues
        

print(f'Sum of game IDs: {IDsum}')
print(f'Sum of power of sets: {IDpowersum}')

