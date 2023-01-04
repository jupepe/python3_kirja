# Muuttujan tunniste (id)

a = 42
b = 100
c = a

print(id(a), id(b))

print(id(a), id(c))

c = 6
print(id(a), id(c))
