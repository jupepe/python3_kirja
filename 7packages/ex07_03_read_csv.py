# csv-luokka

with open('files/persons.csv', newline='') as f:
    for line in f.readlines():
        print(line, end="")

import csv

with open('files/persons.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        print("\t".join(row))
