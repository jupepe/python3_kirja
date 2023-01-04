# Esimerkki: listan laskuoperaatiot

class ListCalculation:

    # Luokan konstruktori
    def __init__(self, num_list=None):
        if num_list is None:
            num_list = []
        self.num_list = num_list

    def print_values(self):
        print(f"{self.num_list}")

    def has_numbers(self):
        has_numbs = all(isinstance(item, int) or isinstance(item, float) for item in self.num_list)
        return has_numbs

    def count_sum(self):
        s = 0
        for value in self.num_list:
            s += value
        return s

    def count_avg(self):
        s = self.count_sum()
        return s / len(self.num_list)


numbs = list(range(1, 21))
calc = ListCalculation(numbs)
if calc.has_numbers():
    calc.print_values()
    my_sum = calc.count_sum()
    avg = calc.count_avg()
    print(f"Summa={my_sum}, keskiarvo={avg}")

flist = [x * 0.1 for x in range(0, 100)]
fcalc = ListCalculation(flist)
if fcalc.has_numbers():
    fcalc.print_values()
    my_sum = fcalc.count_sum()
    avg = fcalc.count_avg()
    print(f"Summa={my_sum}, keskiarvo={avg}")

no_calc = ListCalculation([1, 2, 2.4, 'abc'])
if not no_calc.has_numbers():
    print("Error: kaikki arvot eivät ole numeroita.")
    no_calc.print_values()
    # print(no_calc.count_avg()) # TypeError: unsupported operand type(s) for +=: 'float' and 'str'
