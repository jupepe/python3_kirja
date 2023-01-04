# list

ikalista = ["Matti", 50, "Pekka", 45]
print(ikalista)
print(type(ikalista))

ikalista = list()
ikalista.extend(["Matti", 50, "Pekka", 45])
print(ikalista)
print(type(ikalista))

ikalista = ["Matti", 50, "Pekka", 45]
print(ikalista[0])
print(ikalista[2])

print(ikalista[-1])

print(len(ikalista))

for i in range(len(ikalista)):
    print(ikalista[i])

for item in ikalista:
    print(item)

numbers = [1, 2, 3, 4, 5]
res = 0
for x in numbers:
    res += x
print(res)


def count_sum(arr):
    total_sum = 0
    for val in arr:
        total_sum += val
    return total_sum


range_list = list(range(0, 5))
res = count_sum(range_list)
print(res)

flist = [x * 0.01 for x in range(0, 500)]
s3 = count_sum(flist)
print(f"Listan {flist[0:3]} ,..., {flist[-3:len(flist)]} summa on '{s3:.2f}'")
