# Decimal-luokka

from decimal import Decimal

print(Decimal("3.14"))
print(Decimal(42))

print(f"{Decimal('NaN')}")
print(f"{Decimal(str(2e1000))}, {Decimal(str(-2e1000))}")

print(f"{Decimal(16.949999)} vs {Decimal(str(16.949999))}")

a = Decimal('3.14')
b = 3.14
try:
    print(a + b)
except TypeError as exp:
    print(repr(exp))
print(a + Decimal(str(b)))
