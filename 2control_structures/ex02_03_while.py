# while

n = 10
summa = 0
i = 1

while i <= n:
    summa += i
    i = i + 1

print("Summa on", summa)

n = 10
summa = 0
i = 1

while i <= n:
    summa += i
    i = i + 1
    if i > 5:
        break

print("Summa on", summa)

n = 10
summa = 0
i = 1

while i <= n:
    summa += i
    i = i + 1
else:
    print("i on", i)

print("Summa on", summa)
