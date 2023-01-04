# Dynaamiset argumentit funktiolle

def calc_unlimited_sum(*numbs):
    my_sum = 0
    print(f"type of args {type(numbs)}")
    for n in numbs:
        my_sum += n
    return my_sum


res_ul = calc_unlimited_sum(10, 20, 30, 45, 100, 16, .221)
print(f"Sum is {res_ul}")

numb_tuple = (10, 20, 30, 45, 100, 16, .221)
res_ul2 = calc_unlimited_sum(*numb_tuple)
print(f"Sum is {res_ul2}")
