# dict-sanakirja

import operator

grades = {'bill': 4, 'jill': 1, 'jim': 3, 'mary': 3}
print(type(grades))

for value in grades.values():
    print(value)

for key in grades.keys():
    print(key)

for key in grades.keys():
    print(key, '\t', grades[key])

for key, value in grades.items():
    print(key, '\t', value)

sorted_grades = sorted(grades.items(), key=operator.itemgetter(0))
print(type(sorted_grades))
print(sorted_grades)

sorted_grades = tuple(sorted(grades.items(), key=operator.itemgetter(1), reverse=True))
print(type(sorted_grades))
print(sorted_grades)
