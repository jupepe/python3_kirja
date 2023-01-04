# Esimerkki map ja lambda

def divide_items(numbers):
    return list(map(lambda n: n // 5, numbers))


print(divide_items([1, 12, 20, 34, 52]))


def divide_items(numbers):
    div_5 = lambda n: n // 5
    return list(map(div_5, numbers))


def main():
    print(divide_items([1, 12, 20, 34, 52]))


if __name__ == '__main__':
    main()
