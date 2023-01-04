# write csv
import csv


def csv_writer(data, fname, quote=False):
    with open(fname, "w", newline="") as csv_file:
        if not quote:
            writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_NONE)
        else:
            writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_ALL)
        for line in data:
            writer.writerow(line)


data = ["id,first_name,last_name".split(","),
        "1,Jim,Carter".split(","),
        "2,Ronald,Barnes".split(","),
        "3,Philip,Jackson".split(","),
        "4,Pamela,O'Reilly".split(",")
        ]

fn = "files/output.csv"
csv_writer(data, fn)

fn = "files/output2.csv"
csv_writer(data, fn, True)

with open('files/output.csv', newline='') as f:
    for line in f.readlines():
        print(line, end="")

with open('files/output2.csv', newline='') as f:
    for line in f.readlines():
        print(line, end="")
