# Merkkijonojen käsittely

py_str = "Hello Python Programmers"
print(py_str[::-1])
print(py_str[24:12:-1])
print(py_str[11:0:-1])

print(py_str.upper()[13:24])
print(py_str.lower()[0:12])

print('m', py_str.count('m'))
print('o', py_str.count('o'))

print(py_str[0:5], py_str[0:5].isalpha())
print(py_str[0:7], py_str[0:7].isalpha())

print(py_str.find('Pyt'))
print(py_str.find('Pr'))

print(py_str.index('Pyt'))
print(py_str.index('Pr'))

print(py_str.rfind('o'))
print(py_str.rindex('o'))

print(py_str.replace('Python', 'Python with Robot Framework'))
