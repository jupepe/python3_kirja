# Poikkeukset

try:
    a = 5 / 0
    print(a)
except ZeroDivisionError as exp:
    print(f"Nollalla jako: {exp}!")
except Exception as exp:
    print(f"Poikkeus: {repr(exp)}!")

luku = "kymmenen"
try:
    if not type(luku) is int:
        raise TypeError(f"'{luku}' Sallitaan vain kokonaisluvut")
except TypeError as exp:
    print(f"TypeError: {exp}")
except Exception as exp:
    print(f"Poikkeus: {repr(exp)}!")

luku = "kymmenen"
try:
    x = int(luku)
except Exception as exp:
    print(f"Poikkeus: {repr(exp)}!")
