# Sanakirjaan lisääminen

def add_to_dict(name, grade, grades):
    grades[name] = grade
    return grades


all_grades = {}
add_to_dict('bill', 4, all_grades)
add_to_dict('jill', 1, all_grades)
add_to_dict('jim', 3, all_grades)
add_to_dict('mary', 3, all_grades)
print(all_grades)

all_grades['kim'] = 5
print(all_grades)
