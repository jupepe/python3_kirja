# Merkkijono (string)

kieli = 'Python'
print(kieli)

kieli += ' 3'
print(kieli)
print(type(kieli))

print("Minä 'lainasin' kaupasta karkkipussin.")
print('Minä "lainasin" kaupasta karkkipussin.')

print('Minä \'lainasin\' kaupasta karkkipussin.')
print("Minä \"lainasin\" kaupasta karkkipussin.")

mj_luku = "42.195"
print(type(mj_luku))
mj_luku = str(42.195)
print(type(mj_luku))

maraton = "Matka oli " + str(42.195) + " km."
print(maraton)

print(f"Matka oli {42.195} km.")
print("Matka oli {:.3f} km.".format(42.195))

luku = float(mj_luku)
print(type(luku))

mj_monta_rivia = """jatkaa
seuraavalla
riville"""
print(mj_monta_rivia)

skandit = "abc ja \xe5\xe4\xf6"
print(skandit)
