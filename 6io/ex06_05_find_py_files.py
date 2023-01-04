# Hakemiston käsittely
import os

start_dir = "."  # haettava hakemisto, suhteellinen polku
pattern = ".py"  # suodatin tiedoston nimille
# pattern = ".csv"  # suodatin tiedoston nimille
os.chdir(start_dir)

for fn in (f for f in os.listdir(start_dir) if f.endswith(pattern) and os.path.isfile(f)):
    line_number = 1
    print(f"Reading file '{fn}'...\n")
    with open(fn) as fnFile:
        for line in fnFile.readlines():
            print(f"{line_number}: {line}", end=" ")
            line_number += 1
