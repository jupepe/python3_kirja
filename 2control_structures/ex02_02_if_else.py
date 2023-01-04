# if-lauseke

# numb = 42

# Pyydetään syöte käyttäjältä input()-funktiolla
numb_input = input("Anna numero> ")
numb = int(numb_input)

if numb > 42:
    print(f"{numb} on suurempi kuin 42")

if numb == 42:
    print("Luku on 42")

if numb < 42:
    print(f"{numb} on pienempi kuin 42")

# numb = 21
if numb > 42:
    print(f"{numb} on suurempi kuin 42")
elif numb == 42:
    print("Luku on 42")
elif 0 <= numb < 42:
    print(f"{numb} on välillä 0 - 42")
else:
    print(f"{numb} on pienempi kuin nolla")
