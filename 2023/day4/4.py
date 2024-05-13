import re

with open('input4.txt', 'r') as file:
    
    sum = 0
    for line in file:
        m = re.search(r'([\d\s]+) \| ([\d\s]+)', line[6:])
        winning_nbrs = m.group(1)
        playing_nbrs = m.group(2)
        winning_nbrs = re.findall(r'\d+', winning_nbrs)
        playing_nbrs = re.findall(r'\d+', playing_nbrs)
        wins = 0
        for nbr in playing_nbrs:
            if nbr in winning_nbrs:
                wins += 1
        if wins > 0:
            sum += 2**(wins-1)
print(f'Sum of points: {sum}')


        