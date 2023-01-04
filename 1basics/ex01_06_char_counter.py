# Merkkijonofunktiot

kieli = 'Python 3-kieli'
print(len(kieli))

print(kieli.upper())

kieli = 'Python 3-kieli'
print(kieli.islower())
print(kieli.lower())
print(kieli.lower().islower())

print(kieli.swapcase())

input_str = input("Anna merkkijono>")
# input_str = "Anna tänne merkkijono tai merkillinen jono merkkejä"
counter_a = input_str.lower().count('a')
counter_e = input_str.lower().count('e')

print("a/A kirjaimien lukumäärä: ", counter_a)
print("e/E kirjaimien lukumäärä: ", counter_e)
