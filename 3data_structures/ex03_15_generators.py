# Generaattorit

def reverse_str(word):
    for i in range(len(word) - 1, -1, -1):
        yield word[i]


for ch in reverse_str("Hello Python"):
    print(ch)


def pow_two_three(nlist):
    for n in range(0, len(nlist)):
        yield nlist[n] ** 2, nlist[n] ** 3


for res in pow_two_three([1, 2, 3, 4, 5, 1e2]):
    print(type(res))
    print(res)

# Generointilauseke
from random import seed
from random import random

seed(1)

generator = (random() for num in range(10))
for num in generator:
    print(num)
