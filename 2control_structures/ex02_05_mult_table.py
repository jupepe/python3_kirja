# Esimerkki: Kertotaulun laskeminen

# str_ul = "12"
# upper_limit = int(str_ul)
str_ul = input("Anna numero> ")
upper_limit = int(str_ul)

for x in range(1, upper_limit + 1):
    for y in range(1, upper_limit + 1):
        res = x * y
        print(f'{res:4d}', end="")
    print()

print()

# while versio
x = 1
while x <= upper_limit:
    y = 1
    while y <= upper_limit:
        res = x * y
        print(f'{res:4d}', end="")
        y += 1
    x += 1
    print()
