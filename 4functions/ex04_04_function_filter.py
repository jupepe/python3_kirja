# funktioita listan käsittelyyn


def print_all(item_list):
    for idx, item in enumerate(item_list):
        print(f"{idx}, {type(item)}: {item}")


def print_numbers(item_list):
    for idx, item in enumerate(item_list):
        if isinstance(item, (int, float)):
            print(f"{idx}, {type(item)}: {item}")


items = ["one", "two", "three", 1, 2, 3, 1.1, 2.2, 3.3, None]
print_all(items)

print_numbers(items)
