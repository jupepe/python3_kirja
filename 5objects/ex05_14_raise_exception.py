# Esimerkki: itse aiheutetut poikkeustilanteet
import random as rnd


def rand_values(count, min_value=0, max_value=10):
    values = []
    while len(values) < count:
        try:
            res = rnd.randrange(min_value - 5, max_value + 5)
            if res > max_value:
                raise ValueError(f"Error: Generated {res} > {max_value}")
            elif res < min_value:
                raise ValueError(f"Error: Generated {res} < {min_value}")
            values.append(res)
        except ValueError as err:
            print(f"{err}")
    return values


values = rand_values(20, 1, 30)
print(values)
