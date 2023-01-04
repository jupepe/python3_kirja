# Merkkijonojen indeksointi
kieli = 'Python'
print(kieli[0])

print(kieli[5])

try:
    print(kieli[6])
except Exception as exp:
    print(repr(exp))

print(kieli[-1])

print(kieli[-6])

print(kieli[0:3])

print(kieli[3:6])

print(kieli[-1:-4:-1])

print(kieli[-1:2:-1])

print(kieli[::-1])
