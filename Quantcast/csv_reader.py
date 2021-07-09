import csv

filename = "Quantcast-Measurement-websites-in-the-Top-1-Million-Sites.csv"

with open(filename) as csvfile:
    readCSV = csv.reader(csvfile)
    names = []
    for row in readCSV:
        name = row[1]

        names.append(name)

names.pop(0)
names.pop(0)

print(names)

NAMES = names