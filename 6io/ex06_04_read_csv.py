# Esimerkki: Tiedoston sisältö olioiksi

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def to_string(self):
        return "{} ({}) \thas got a grade {}.".format(self.name, self.age, self.grade)


students = []
with open('files/students.txt') as fpath:
    lines = [line for line in fpath]
    lines = lines[1:]
    for line in lines:
        name, grade, age = line.strip().split(',')
        st = Student(name, int(grade), int(age))
        students.append(st)

for st in sorted(students, key=lambda s: s.age, reverse=True):
    print(st.to_string())

for st in sorted(students, key=lambda s: s.name, reverse=False):
    print(st.to_string())
