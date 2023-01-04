# listojen läpikäynti

kauppalista = ["kahvi", "maito", "makkara"]
for tuote in kauppalista:
    print(tuote)

for i in range(len(kauppalista)):
    print(f"{i}:\t{kauppalista[i]}")

kauppalista = ["kahvi", "maito", "tomaatti", "makkara"]
for tuote in kauppalista:
    print(tuote)
else:
    print(f"Silmukka loppui ja viimeinen tuote oli {tuote}.")
