# Esimerkkejä poikkeuskäsittelystä
import sys


def exp_handled():
    try:
        r = "20" + 10
    except Exception as exp:
        print(f"Poikkeus: {repr(exp)}!")


def unhandled_convert(mj):
    return float(mj)


exp_handled()

try:
    unhandled_convert(10)
    # unhandled_convert() # TypeError: unhandled_convert() missing 1 required positional argument: 'mj'
    unhandled_convert("Go")
except ValueError as err:
    print(f"{repr(err)}")
except TypeError as err:
    print(f"{repr(err)}")

try:
    exp_handled("arg1", "arg2")
except TypeError as exp:
    print(f"{exp}\nYksityiskohtaisempaa tietoa virheestä: {sys.exc_info()}")
