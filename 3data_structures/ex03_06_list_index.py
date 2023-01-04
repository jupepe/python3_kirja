# Listan alkioiden tulostaminen

lang_word = "Python Java C# C++ JavaScript Rust Scala Groovy"
lang_arr = lang_word.split(" ")
for i in range(0, len(lang_arr)):  # tai for i in range(len(lang_arr)):
    print(f"{i}\t => \t{lang_arr[i]}")

for i, word in enumerate(lang_arr):
    print(f"{i}\t => \t{word}")

for i, word in enumerate(lang_arr, 1):
    print(f"{i}\t => \t{word}")

lang_2d = [[i, lang_arr[i]] for i in range(len(lang_arr))]
print(lang_2d)

# zip
for val in zip(range(len(lang_arr)), lang_arr):
    print(f"{val[0]}\t => \t{val[1]}")

sorted_langs = []
for row in zip(range(len(lang_arr)), lang_arr, sorted(lang_arr), reversed(sorted(lang_arr))):
    sorted_langs.append(row)
print(sorted_langs)
sorted_langs
