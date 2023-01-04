# Funktion määrittely

def oma_funktio():
    print("Heippa funktio!")


oma_funktio()


def calc_sum(a, b):
    return a + b


print(calc_sum(10, 20))
print(calc_sum(100, 200))

# lambda-funktio
plus_five = lambda x: x + 5

print(plus_five(10))
print(plus_five(plus_five((plus_five(10)))))

calc_sum_lambda = lambda x, y: x + y

print(calc_sum_lambda(10, 20))
print(calc_sum_lambda(100, 200))


def combine_names_func(first, last):
    return first.title() + " " + last.title()


combine_names = lambda first, last: first.title() + " " + last.title()

print(combine_names_func("Pekko", "Aikapoika"))
print(combine_names("Pekko", "Aikapoika"))
