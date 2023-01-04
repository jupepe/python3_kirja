# list ja for

langs = ['Python', 'Java', 'C#', 'C++', 'JavaScript']
for lang in langs:
    print("lang {}".format(lang))

lang_word = "Python Java C# C++ JavaScript Rust Scala"
for word in lang_word.split(" "):
    print(word)

a = [1, 2, 3]
b = a
print(id(a), id(b))
print(a, b)

a.append(4)
b.append(5)
print(id(a), id(b))
print(a, b)
