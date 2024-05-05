import csv

# Part 1
with open('2023/1.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    sum = 0
    for line in reader:
        first, second = -1, -1
        for c in line[0]:
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                if first == -1:
                    first = c
                second = c
        sum += int(first + second)
print(f'code is: {sum}')

# Part 2
# TODO
            
