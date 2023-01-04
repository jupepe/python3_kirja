# Boolean-totuusarvot

onko_tosi = True
print(onko_tosi)
print(type(onko_tosi))

onko_tosi = False
print(onko_tosi)
print(type(onko_tosi))

muunnettu_arvo = bool(10)
print(muunnettu_arvo, type(muunnettu_arvo))

muunnettu_arvo = bool(0)
print(muunnettu_arvo, type(muunnettu_arvo))

muunnettu_arvo = bool(0.0)
print(muunnettu_arvo, type(muunnettu_arvo))

muunnettu_arvo = bool("kymmenen")
print(muunnettu_arvo, type(muunnettu_arvo))

muunnettu_arvo = bool("")
print(muunnettu_arvo, type(muunnettu_arvo))

a = 42
b = 100
print(b > a, type(b > a))
print(b < a, type(b < a))

print(a > 0 and a < 100, type(a > 0 and a < 100))

print(0 < a < 100, type(0 < a < 100))
