# timeit-moduuli
from timeit import timeit


def count_sum_while(last):
    s = 0
    i = 0
    while i < last:
        s += i
        i += 1
    return s


def count_sum_for(last):
    s = 0
    for i in range(last):
        s += i
    return s


def count_sum_range(last):
    return sum(range(last))


res = timeit("count_sum_while(100000)", number=1000, globals=locals())
print(f"while:\t {res:.2f}s")
res = timeit("count_sum_for(100000)", number=1000, globals=locals())
print(f"for:\t {res:.2f}s")
res = timeit("count_sum_range(100000)", number=1000, globals=locals())
print(f"sum:\t {res:.2f}s")
print(count_sum_for(100000))
print(count_sum_while(100000))
print(count_sum_range(100000))

# numpy -kirjaston pitää olla asennettuna
import numpy as np

np_array = np.array(range(100000))
print(np_array.sum(dtype=np.int64))
res = timeit("np_array.sum(dtype=np.int64)", number=1000, globals=locals())
print(f"numpy sum:\t {res:.2f}s")
