# tuple

langs_tuple = ('Python', 'Java', 'C#', 'C++', 'JavaScript')
print(type(langs_tuple))
print(type(langs_tuple[0][-1]))
langs_tuple

lang_word = "Python Java C# C++ JavaScript PHP Rust Scala Groovy"
word_list = []
for word in lang_word.split(" "):
    word_list.append(word)
word_tuple = tuple(word_list)
print(type(word_tuple))
print(word_tuple)

print(f'Listan koko {word_list.__sizeof__()} vs. tuplen koko {word_tuple.__sizeof__()}.')
