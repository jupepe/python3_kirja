# Avainsanamuotoiset argumentit funktiossa


def concat_items(**kwargs):
    res = ""
    for k, v in kwargs.items():
        res += k + ":\t" + str(v) + "\n"
    return res


def concat_vals(**kwargs):
    res = ""
    for val in kwargs.values():
        res += str(val) + ","
    return res[:-1]


kw1 = concat_vals(first_name="Teppo", last_name='Testaaja', profession='Testausinsinööri', gender='mies', age=31)
print(kw1)

pr2 = {
    'first_name': "Kiia",
    'last_name': "Koodaaja",
    'profession': "Ohjelmistokehittäjä",
    'gender': "nainen",
    'age': 35,
    'salary': 3000
}

kw2 = concat_vals(**pr2)
print(kw2)

print(concat_items(**pr2))
