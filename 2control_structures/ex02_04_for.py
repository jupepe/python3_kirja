# for

for numb in range(1, 11):
    print(numb, " ", end="")
print()

for numb in range(10, 0, -1):
    print(numb, " ", end="")
print()

for i in range(10, 30, 5):
    print(i)

mj = "Python"
for ch in mj:
    print(ch, " ", end="")
print()

for i in range(len(mj)):
    print(f"{i}: {mj[i]}")

mj = "P,y,t,h,o,n"
for item in mj.split(","):
    print(item, " ", end="")
print()

# break
mj = "P,y,t,h,o,n"
for item in mj.split(","):
    if item == "h":
        break
    print(item, " ", end="")
print()

# continue
for numb in range(1, 11):
    if numb % 2 == 1:
        continue
    print(numb, " ", end="")
print()
