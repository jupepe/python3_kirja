# Kokoelman järjestäminen

person1 = ("Bill", 1979)
person2 = ("Jill", 1995)
person3 = ("Jim", 1963)
person4 = ("Mary", 1987)
persons = (person1, person2, person3, person4)
print(persons)
persons

persons_by_age = sorted(persons, key=lambda p: p[1], reverse=False)
print(persons_by_age)
persons_by_age

persons_by_name = sorted(persons, key=lambda p: p[0], reverse=True)
print(persons_by_name)
persons_by_name
