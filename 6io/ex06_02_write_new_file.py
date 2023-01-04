# Tekstitiedoston kirjoittaminen
import random


def write_to_file(fname, lines):
    with open(fname, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)


def generate_unicode_lines(lines):
    start = 1
    end = 10000
    arr = []
    for k in range(0, lines):
        str_codes = ""
        str_chr = ""
        for i in range(0, 80):
            val = random.randint(start, end)
            str_codes += ascii(chr(val))
            str_chr += chr(val)
        arr.append(str_chr + "\n")
    return arr


output_fn = "files/random_unicode.txt"
all_lines = generate_unicode_lines(10)
print("".join(all_lines[:1]), "".join(all_lines[-2:-1]))
write_to_file(output_fn, all_lines)
