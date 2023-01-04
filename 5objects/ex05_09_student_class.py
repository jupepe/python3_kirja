# Esimerkki: olioiden järjestäminen
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def to_string(self):
        return "{},{},{}".format(self.name, self.grade, self.age)


student_list = [Student('jim', 4, 21), Student('jane', 3, 23), Student('anne', 5, 24)]
student_list.append(Student('niles', 2, 17))
student_list.append(Student('jonas', 2, 19))
student_list.append(Student('kim', 5, 25))

for st in sorted(student_list, key=lambda s: s.name):
    print(st)

for st in sorted(student_list, key=lambda s: s.grade, reverse=True):
    print(st.to_string())

for st in sorted(student_list, key=lambda s: s.grade, reverse=False):
    print(st.to_string())
