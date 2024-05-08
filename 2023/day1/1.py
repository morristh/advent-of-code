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

def is_number(string: str, start: int)-> bool:
    numbers = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    string = string[start:]
    for idx, number in enumerate(numbers):
        if len(string) >= len(number):
            if string[:len(number)] == number:
                return idx + 1
    return -1

with open('2023/1.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    sum = 0
    for line in reader:
        first, second = -1, -1
        for idx, c in enumerate(line[0]):
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                if first == -1:
                    first = c
                second = c
            else:
                num = is_number(string=line[0], start=idx)
                if num > 0 and num <= 9:
                    if first == -1:
                        first = num
                    second = num
        sum += int(str(first) + str(second))
print(f'code is: {sum}')
            
