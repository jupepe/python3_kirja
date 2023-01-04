# funktioita tuplen käsittelyyn


def count_average(item_list):
    my_sum = counter = 0
    for idx, item in enumerate(item_list):
        if isinstance(item, (int, float)):
            my_sum = item
            counter += 1
    return my_sum / counter


def pipe_to_string(item_list):
    my_str = ""
    for idx, item in enumerate(item_list):
        my_str += str(item) + ","
    return my_str[:-1]


items = ("one", "two", "three", 1, 2, 3, 1.1, 2.2, 3.3, None)
print(pipe_to_string(items))

avg = count_average(items)
print("Keskiarvo: {}, ja kahdella desimaalilla {:.2f}".format(avg, avg))
