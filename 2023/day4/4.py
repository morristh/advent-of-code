import re

with open('input4+.txt', 'r') as file:
    input = file.readlines()

pointSum = 0
nbrCards = [1] * len(input) # We start with one of each card

for gameNbr, line in enumerate(input):
    m = re.search(r'([\d\s]+) \| ([\d\s]+)', line[6:])
    winning_nbrs = m.group(1)
    playing_nbrs = m.group(2)
    winning_nbrs = re.findall(r'\d+', winning_nbrs)
    playing_nbrs = re.findall(r'\d+', playing_nbrs)
    wins = 0
    for nbr in playing_nbrs:
        if nbr in winning_nbrs:
            wins += 1
    
    # Task 1
    if wins > 0:
        pointSum += 2**(wins-1)

    # Task 2
    for game in range(gameNbr+1, gameNbr+wins+1):
        if game < len(input):
            nbrCards[game] += nbrCards[gameNbr]
cardSum = sum(nbrCards)

print(f'Sum of points: {pointSum}')
print(f'Total number of cards: {cardSum}')

        