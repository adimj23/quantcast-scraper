import csv

filename = "/Users/adisrinivasan/UIUC/Quantcast/CSVFiles/Quantcast Info - Hispanic Union.csv"

with open(filename) as csvfile:
    readCSV = csv.reader(csvfile)
    names = []
    for row in readCSV:
        name = row[0]

        names.append(name)

names.pop(0)

print(names)

NAMES = names