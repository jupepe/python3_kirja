# set-joukkojen väliset operaatiot

set1 = set(range(1, 7))
set2 = set(range(4, 9))
print(f'set1={set1} ja set2={set2}')

union_set = set1.union(set2)
print(f'Yhdistelmä={union_set}')

set_int = set1.intersection(set2)
print(f'Leikkaus={set_int}')

set1_diff = set1.difference(set2)
print(f'set1 ero set2={set1_diff}')

set2_diff = set2.difference(set1)
print(f'set2 ero set1={set2_diff}')

set3 = set(range(1, 4))
if set3.issubset(set1):
    print(f'{set3} on joukon {set1} alijoukko')
if not (set3.issubset(set2)):
    print(f'{set3} ei ole joukon {set2} alijoukko')
