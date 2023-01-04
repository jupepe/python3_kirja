# Oliot

# int-metodit
i = 10
print(i.__sizeof__())  # 24 tavua
print(i.__class__)

# float-metodit
f = 10.11
print(f.__sizeof__())  # 28 tavua
print(f.__class__)

# Object-kantaluokka
olio = object()
print(olio.__sizeof__())  # 16 tavua
print(olio.__class__)

try:
    olio.nimi = "Testiolio"
except AttributeError as err:
    print(err)

print(dir(olio))

print(type(olio))
print(repr(olio))
print(olio)


class OwnClass:
    pass


ow = OwnClass()
print(type(ow))
print(ow.__class__)
print(ow.__sizeof__())

print(dir(ow))
print(ow.__dict__)


# Luokan toteutus
class FirstClass:
    pass


class SecondClass(FirstClass):
    pass


my_first_class = FirstClass()
my_second_class = SecondClass()
print(my_first_class)
print(my_second_class)

print(my_first_class.__sizeof__())
print(my_first_class.__class__)
print(my_second_class.__sizeof__())
print(my_second_class.__class__)


class MyPython:
    def show(self):
        print("I'm a MyPython class")

    def todo(self):
        print("TODO something")

    def show_version(self):
        pass


my_python = MyPython()
my_python.show()
my_python.todo()

MyPython.todo(my_python)


class MyPython:
    def __init__(self):
        self.versio = "3.9"
        self.kayttojarjestelma = "Linux"

    def vaihda_kayttojarjestelma(self, kayttojarjestelma):
        self.kayttojarjestelma = kayttojarjestelma

    def nayta_tiedot(self):
        print(f"Python-versio {self.versio} käyttöjärjestelmässä {self.kayttojarjestelma}.")


mypy = MyPython()
mypy.nayta_tiedot()
mypy.vaihda_kayttojarjestelma("Windows")
mypy.nayta_tiedot()

print(mypy.__dict__)

print(dir(mypy))

mypy.versio = "3.10.5"
mypy.kayttojarjestelma = "MacOS"
mypy.nayta_tiedot()

mypy = MyPython()
mypy.nayta_tiedot()
mypy.vaihda_kayttojarjestelma("Windows")
mypy.nayta_tiedot()

mypy1 = MyPython()
mypy1.versio = "11"
mypy1.vaihda_kayttojarjestelma("Windows")

mypy2 = mypy1
mypy2.versio = "3.10"
mypy2.vaihda_kayttojarjestelma("MacOs")

mypy1.nayta_tiedot()
mypy2.nayta_tiedot()

print(f"mypy1: {id(mypy1)} vs. mypy2: {id(mypy2)} vs. uusi {id(MyPython())}")
