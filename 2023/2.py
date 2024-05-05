import csv

with open('2.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)
        break