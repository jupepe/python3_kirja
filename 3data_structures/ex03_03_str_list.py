# list ja str

def append_words(*args):
    res = ""
    for x in args:
        res += str(x) + " "
    return res.rstrip()


words = ["this", "is", "a", "list", 10, None, True, (5 != 5), 6.7]
word_list = append_words(*words)
print(f"'{word_list}', jonka tyyppi on {type(word_list)}.")
