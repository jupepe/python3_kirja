# tuple vs. list

my_list = list(range(1, 11))
my_tuple = tuple(range(1, 11))

print(f'my_list={my_list} with size {my_list.__sizeof__()} {type(my_list)}')
print(f'my_tuple={my_tuple} with size {my_tuple.__sizeof__()} {type(my_tuple)}')

my_list[9] = 11
my_list.remove(1)
my_list.remove(3)
try:
    my_list.remove(0)
except ValueError as exp:
    print(f"Error: {exp}")

print(f'my_list=...{my_list}, koko on {my_list.__sizeof__()} {type(my_list)} {id(my_list)} ')

my_tuple2 = tuple(my_list)
print(f'my_tuple={my_tuple2}, koko on {my_tuple2.__sizeof__()} {type(my_tuple2)} {id(my_tuple2)}')

try:
    my_tuple[9] = 11
except TypeError as exp:
    print(f"Error: {exp}")

try:
    my_tuple.remove(3)
except AttributeError as exp:
    print(f"Error: {exp}")

print(id(my_tuple))
my_tuple += (20,)
print(id(my_tuple))
