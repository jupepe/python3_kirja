# Tekstitiedostojen käsittely

file_name = "files/email.csv"
with open(file_name) as f:
    all_lines = f.read()
    print(all_lines)

with open(file_name) as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    print(f'{i}: {line}')

with open(file_name) as f:
    lines = f.readlines()
all_lines = []
for line in lines:
    arr = line.rstrip().split(";")
    all_lines.append(arr)
for line in all_lines:
    print("\t".join(line))
