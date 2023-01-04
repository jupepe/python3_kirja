# formatointi (format())

n = 10.12
# print("versio " + n)  # TypeError: can only concatenate str (not "float") to str
print("versionumero " + str(n))
print("versionumero {}".format(n))

print("versionumero {:.3f}".format(n))
print("versionumero {:.{precision}f}".format(n, precision=6))

print(f"versionumero {n}")
print(f"versionumero {n:.3f}")

vers = "Versio"
print(f"{vers:10s} {n:.3f}")
print(f"{vers:10s} {n:.6f}")

points = 17
total = 21
res = points / total
print('Oikeat vastaukset: {:.2%}'.format(res))
print(f'Oikeat vastaukset: {((points - 2) / total):.2%}')
